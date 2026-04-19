"""R61 Track 4 — Charge-neutrality scoring and harmonic flagging.

Replaces Track 3's pair-cleanliness + sterile-count with:
  - charge-neutrality score (R48 CP synchronization rule)
  - charged-extras count (dark extras don't penalize)
  - harmonic flag (same signed reduced form → triplet scored 0)

Produces a re-scored shortlist plus a hybrid-candidate list that
surfaces triplets using mixed neutrality mechanisms — e.g. a ±pair
for two modes + an |n_tube|≥2 mode for the third (no pair needed).

Run:
    python track4_charge_neutrality.py
"""

from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass
from typing import Iterable

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "outputs")
sys.path.insert(0, SCRIPT_DIR)

from track2_candidates import (  # type: ignore
    Mode,
    Triplet,
    mu2,
    enumerate_modes,
    paired_fermion_modes,
    find_ratio_triplets,
    Lz_over_hbar,
    _clip01,
    _RATIO_CAP,
    _SIMPL_CAP,
    _SPIN_CAP,
)
from track3_sterile_scoring import fermion_candidates  # type: ignore


# ---------------------------------------------------------------------------
# New primitives
# ---------------------------------------------------------------------------

def reduced_form(n_tube: int, n_ring: int) -> tuple[int, int, int]:
    """Return (n_tube/d, n_ring/d, d) where d = gcd(|n_tube|, |n_ring|).

    For (0, 0) returns (0, 0, 0).  Signed reduced form preserves the
    sign of each component (so (1,2) and (-1,2) have different signed
    reduced forms but are both fundamental = coprime)."""
    if n_tube == 0 and n_ring == 0:
        return (0, 0, 0)
    d = math.gcd(abs(n_tube), abs(n_ring))
    if d == 0:
        d = max(abs(n_tube), abs(n_ring))
    return (n_tube // d, n_ring // d, d)


def is_coprime(n_tube: int, n_ring: int) -> bool:
    _, _, d = reduced_form(n_tube, n_ring)
    return d == 1


def is_harmonic(mode: Mode) -> bool:
    return not is_coprime(mode.n_tube, mode.n_ring)


def is_charged(mode: Mode, eps: float, s: float, delta: float) -> bool:
    """Per R48: mode carries charge iff |n_tube| = 1 AND its ±n_tube partner
    has mu² splitting/mean > delta (i.e., not Majorana-degenerate).

    |n_tube| ≥ 2 → never charged (R48 CP synchronization fails).
    |n_tube| = 1 with paired partner → neutral (Majorana).
    |n_tube| = 1 solo (partner split too wide) → charged.
    """
    if abs(mode.n_tube) >= 2:
        return False
    if abs(mode.n_tube) != 1:
        return False  # n_tube = 0, treated as neutral (no charge mechanism)
    partner_mu2 = mu2(-mode.n_tube, mode.n_ring, eps, s)
    mean = 0.5 * (mode.mu2 + partner_mu2)
    if mean <= 0:
        return True
    rel_split = abs(mode.mu2 - partner_mu2) / mean
    return rel_split > delta


def charge_neutrality_score(
    triplet: Triplet, eps: float, s: float, delta: float
) -> tuple[float, list[str]]:
    """Average per-mode neutrality credit.  Returns (score, mechanism list)."""
    per_mode = []
    mechanisms = []
    for m in (triplet.a, triplet.b, triplet.c):
        if abs(m.n_tube) >= 2:
            per_mode.append(1.0)
            mechanisms.append("R48")  # inherently uncharged via CP sync
        elif abs(m.n_tube) == 1:
            partner_mu2 = mu2(-m.n_tube, m.n_ring, eps, s)
            mean = 0.5 * (m.mu2 + partner_mu2)
            if mean <= 0:
                per_mode.append(0.0)
                mechanisms.append("degen-fail")
            else:
                rel_split = abs(m.mu2 - partner_mu2) / mean
                if rel_split <= delta:
                    per_mode.append(1.0)
                    mechanisms.append("Majorana")
                else:
                    # partial credit inversely proportional to how far beyond delta
                    excess = rel_split / delta - 1
                    per_mode.append(max(0.0, 1.0 - excess))
                    mechanisms.append("Majorana-weak")
        else:
            per_mode.append(0.0)
            mechanisms.append("none")
    return sum(per_mode) / 3.0, mechanisms


def charged_extras_count(
    triplet: Triplet, all_fermion_in_window: list[Mode], eps: float, s: float, delta: float
) -> int:
    """Count modes in window (not triplet members) that would be charged
    under R48.  Dark extras (|n_tube|≥2 or Majorana-paired) are excluded.
    """
    triplet_ids = {
        (triplet.a.n_tube, triplet.a.n_ring),
        (triplet.b.n_tube, triplet.b.n_ring),
        (triplet.c.n_tube, triplet.c.n_ring),
    }
    count = 0
    for m in all_fermion_in_window:
        if (m.n_tube, m.n_ring) in triplet_ids:
            continue
        if is_charged(m, eps, s, delta):
            count += 1
    return count


def harmonic_flag(triplet: Triplet) -> tuple[float, list[tuple[int, int, int]]]:
    """Return (1.0 if no two modes share a signed reduced form, else 0.0)
    along with the list of reduced forms for inspection."""
    rfs = [reduced_form(m.n_tube, m.n_ring) for m in (triplet.a, triplet.b, triplet.c)]
    signed_rfs = [(rf[0], rf[1]) for rf in rfs]
    score = 1.0 if len(set(signed_rfs)) == 3 else 0.0
    return score, rfs


# ---------------------------------------------------------------------------
# Seven-criterion scoring
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Scores7:
    ratio_exactness: float
    charge_neutrality: float
    mode_simplicity: float
    spin_quality: float
    lowest_bonus: float
    charged_extras: float   # score (1 minus count/cap)
    no_harmonic: float      # 0 or 1
    composite: float
    spins: tuple[float, float, float]
    n_charged_extras: int
    neutrality_mechanisms: tuple[str, str, str]
    reduced_forms: tuple[tuple[int,int,int], tuple[int,int,int], tuple[int,int,int]]


_CHARGED_CAP = 3  # charged_score → 0 at 3 charged extras


def score_triplet_7(
    triplet: Triplet,
    eps: float,
    s: float,
    is_lowest: bool,
    all_fermion_in_window: list[Mode],
    pair_delta: float,
    weights: tuple[float, ...],
) -> Scores7:
    ratio_err = abs(triplet.ratio - 33.6) / 33.6
    r_score = _clip01(1.0 - ratio_err / _RATIO_CAP)

    cn_score, mechanisms = charge_neutrality_score(triplet, eps, s, pair_delta)

    simpl_sum = sum(abs(m.n_tube) + abs(m.n_ring) for m in (triplet.a, triplet.b, triplet.c))
    m_score = _clip01(1.0 - simpl_sum / _SIMPL_CAP)

    spins = tuple(
        Lz_over_hbar(m.n_tube, m.n_ring, eps) for m in (triplet.a, triplet.b, triplet.c)
    )
    spin_err_sum = sum(abs(sp - 0.5) for sp in spins)
    s_score = _clip01(1.0 - spin_err_sum / _SPIN_CAP)

    low_bonus = 1.0 if is_lowest else 0.0

    ce_count = charged_extras_count(triplet, all_fermion_in_window, eps, s, pair_delta)
    ce_score = _clip01(1.0 - ce_count / _CHARGED_CAP)

    nh_score, rfs = harmonic_flag(triplet)

    composite = (
        weights[0] * r_score
        + weights[1] * cn_score
        + weights[2] * m_score
        + weights[3] * s_score
        + weights[4] * low_bonus
        + weights[5] * ce_score
        + weights[6] * nh_score
    )

    return Scores7(
        ratio_exactness=r_score,
        charge_neutrality=cn_score,
        mode_simplicity=m_score,
        spin_quality=s_score,
        lowest_bonus=low_bonus,
        charged_extras=ce_score,
        no_harmonic=nh_score,
        composite=composite,
        spins=spins,
        n_charged_extras=ce_count,
        neutrality_mechanisms=tuple(mechanisms),
        reduced_forms=tuple(rfs),
    )


# ---------------------------------------------------------------------------
# Ranker
# ---------------------------------------------------------------------------

@dataclass
class PointResult4:
    eps: float
    s: float
    n_triplets: int
    best: Triplet | None
    best_scores: Scores7 | None


def _modeset_key(t: Triplet) -> frozenset:
    return frozenset([
        (t.a.n_tube, t.a.n_ring),
        (t.b.n_tube, t.b.n_ring),
        (t.c.n_tube, t.c.n_ring),
    ])


def rank_candidates_7(
    eps_grid: np.ndarray,
    s_grid: np.ndarray,
    weights: tuple[float, ...],
    pair_delta: float = 0.1,      # Majorana tolerance for charge check
    enum_delta: float = 0.5,      # LOOSE filter so hybrid triplets survive
    tol: float = 0.027,
    target: float = 33.6,
    nt_max: int = 3,
    nr_max: int = 6,
) -> list[PointResult4]:
    """Rank (ε, s) points by best-triplet composite under seven criteria.

    Note: enum_delta is intentionally loose (0.5) so triplets like
    (1,1)(−1,1)(2,3) survive the pair filter; the TIGHT pair check
    for charge neutrality uses pair_delta=0.1 inside the scorer.
    """
    results: list[PointResult4] = []
    sterile_nt_max = max(nt_max, 10)
    sterile_nr_max = max(nr_max, 6)
    for eps in eps_grid:
        for s in s_grid:
            modes = enumerate_modes(float(eps), float(s), nt_max, nr_max)
            paired = paired_fermion_modes(modes, float(eps), float(s), enum_delta)
            triplets = find_ratio_triplets(paired, target, tol)
            if not triplets:
                results.append(PointResult4(float(eps), float(s), 0, None, None))
                continue
            wide_modes = enumerate_modes(float(eps), float(s), sterile_nt_max, sterile_nr_max)
            all_fermion = fermion_candidates(wide_modes)
            lowest = min(triplets, key=lambda t: (t.a.mu2, t.b.mu2, t.c.mu2))
            best: Triplet | None = None
            best_scores: Scores7 | None = None
            for t in triplets:
                # Window for charged-extras count: [µ²_a, µ²_c]
                window_modes = [m for m in all_fermion
                                if t.a.mu2 < m.mu2 < t.c.mu2]
                sc = score_triplet_7(
                    t, float(eps), float(s), t is lowest,
                    window_modes, pair_delta, weights,
                )
                if best_scores is None or sc.composite > best_scores.composite:
                    best = t
                    best_scores = sc
            results.append(PointResult4(float(eps), float(s), len(triplets), best, best_scores))
    return results


def deduplicate(results: list[PointResult4], top_n: int) -> list[PointResult4]:
    seen: dict[frozenset, PointResult4] = {}
    for r in results:
        if r.best is None or r.best_scores is None:
            continue
        key = _modeset_key(r.best)
        if key not in seen or seen[key].best_scores.composite < r.best_scores.composite:
            seen[key] = r
    uniq = list(seen.values())
    uniq.sort(key=lambda r: -r.best_scores.composite)
    return uniq[:top_n]


# ---------------------------------------------------------------------------
# Smoke tests T13–T16
# ---------------------------------------------------------------------------

def smoke_tests() -> list[tuple[str, bool, str]]:
    out: list[tuple[str, bool, str]] = []

    # -- T13 --------------------------------------------------------------
    # is_charged rules
    eps, s, delta = 2.0, 0.022, 0.1
    modes = enumerate_modes(eps, s, nt_max=3, nr_max=4)
    def _find(n_t, n_r):
        for m in modes:
            if m.n_tube == n_t and m.n_ring == n_r:
                return m
        return None
    # (1,1) paired with (-1,1): rel_split = 4s / mean ≈ 0.073 at these params
    m_1_1 = _find(1, 1)
    m_m1_1 = _find(-1, 1)
    m_2_3 = _find(2, 3)
    # At s=0.022, (1,1)/(-1,1) splitting is clean → not charged
    paired_neutral = (not is_charged(m_1_1, eps, s, delta)) and (not is_charged(m_m1_1, eps, s, delta))
    # At s=0.06, (1,1)/(-1,1) splitting rel ≈ 0.23 > delta → charged
    s2 = 0.06
    modes_s2 = enumerate_modes(eps, s2, nt_max=3, nr_max=4)
    m_1_1_s2 = [m for m in modes_s2 if m.n_tube == 1 and m.n_ring == 1][0]
    pair_split_charged = is_charged(m_1_1_s2, eps, s2, delta)
    # (2,3) always neutral (|n_tube|≥2)
    n23_neutral = not is_charged(m_2_3, eps, s, delta)
    n23_neutral_s2 = not is_charged(
        [m for m in modes_s2 if m.n_tube == 2 and m.n_ring == 3][0], eps, s2, delta
    )
    ok = paired_neutral and pair_split_charged and n23_neutral and n23_neutral_s2
    detail = (f"(1,1)/(−1,1) @ s=0.022 neutral: {paired_neutral}; "
              f"(1,1) @ s=0.06 charged: {pair_split_charged}; "
              f"(2,3) neutral regardless of s: {n23_neutral and n23_neutral_s2}")
    out.append(("T13 is_charged rule matches R48 expectations", ok, detail))

    # -- T14 --------------------------------------------------------------
    # Family A at (ε=2, s=0.022): charged_extras count.
    # In window [1.206, 4.162], candidates: (±2,1), (±3,1) at n_ring=1.
    # Their ±n_tube partners are also in window → all dark (Majorana-paired).
    # So charged extras should be 0.
    eps, s = 2.0, 0.022
    modes_w = enumerate_modes(eps, s, nt_max=10, nr_max=6)
    all_fermion = fermion_candidates(modes_w)
    def _find_w(n_t, n_r):
        for m in modes_w:
            if m.n_tube == n_t and m.n_ring == n_r:
                return m
        return None
    fa_a = _find_w(1, 1); fa_b = _find_w(-1, 1); fa_c = _find_w(1, 2)
    fa_triplet = Triplet(fa_a, fa_b, fa_c,
                          (fa_c.mu2 - fa_a.mu2) / (fa_b.mu2 - fa_a.mu2))
    window = [m for m in all_fermion if fa_a.mu2 < m.mu2 < fa_c.mu2]
    count = charged_extras_count(fa_triplet, window, eps, s, delta=0.1)
    ok = count == 0
    out.append(("T14 charged_extras_count for Family A at (ε=2, s=0.022) = 0", ok,
                f"count = {count} (expected 0: all steriles are Majorana-paired)"))

    # -- T15 --------------------------------------------------------------
    # Harmonic flag: (−2,2) reduces to (−1,1); sharing with (−1,1) → flagged 0.
    # Family A has three distinct reduced forms → flagged 1.
    # Build a test triplet (1,1), (-1,1), (-2,2)
    m_m2_2 = _find_w(-2, 2)
    if m_m2_2 is None:
        out.append(("T15 harmonic flag", False, "Could not find (-2,2) in enumeration"))
    else:
        rf_neg22 = reduced_form(-2, 2)
        hr_triplet = Triplet(fa_a, fa_b, m_m2_2,
                              (m_m2_2.mu2 - fa_a.mu2) / (fa_b.mu2 - fa_a.mu2))
        harm_flag, harm_rfs = harmonic_flag(hr_triplet)
        fa_flag, fa_rfs = harmonic_flag(fa_triplet)
        ok = (harm_flag == 0.0) and (fa_flag == 1.0) and rf_neg22 == (-1, 1, 2)
        detail = (f"reduced_form(-2,2) = {rf_neg22}; "
                  f"(1,1)(−1,1)(−2,2) harmonic_flag = {harm_flag}; "
                  f"Family A harmonic_flag = {fa_flag}")
        out.append(("T15 harmonic flag detects (-2,2) ~ (-1,1)", ok, detail))

    # -- T16 --------------------------------------------------------------
    # User's hybrid triplet: (1,1), (-1,1), (2,3) at ε=5, s≈0.0564 (solved
    # analytically for exact ratio 33.6).
    # Tests the CHARGE NEUTRALITY scoring: (2,3) should get full R48 credit;
    # (±1,1) pair at s=0.0564 is moderately split (rel ≈ 0.22), giving
    # reduced Majorana-weak credit.
    eps_h = 5.0
    s_hybrid = 0.0564
    modes_h = enumerate_modes(eps_h, s_hybrid, nt_max=3, nr_max=4)
    def _find_h(n_t, n_r):
        for m in modes_h:
            if m.n_tube == n_t and m.n_ring == n_r:
                return m
        return None
    hm_a = _find_h(1, 1); hm_b = _find_h(-1, 1); hm_c = _find_h(2, 3)
    if None in (hm_a, hm_b, hm_c):
        out.append(("T16 hybrid triplet (1,1)(−1,1)(2,3) scores via mixed mechanisms",
                    False, "modes not found"))
    else:
        ratio = (hm_c.mu2 - hm_a.mu2) / (hm_b.mu2 - hm_a.mu2)
        hy_triplet = Triplet(hm_a, hm_b, hm_c, ratio)
        cn, mech = charge_neutrality_score(hy_triplet, eps_h, s_hybrid, delta=0.1)
        # Required: (2,3) uses R48 mechanism; CN > 0 (something is neutral)
        has_R48 = "R48" in mech
        cn_positive = cn > 0.3
        # Ratio is a separate concern (tested via scoring pipeline elsewhere)
        ok = has_R48 and cn_positive
        detail = (f"ratio={ratio:.3f}; "
                  f"charge_neutrality={cn:.3f}; "
                  f"mechanisms={mech}")
        out.append(("T16 hybrid triplet (1,1)(−1,1)(2,3) scores via mixed mechanisms",
                    ok, detail))

    return out


# ---------------------------------------------------------------------------
# Outputs
# ---------------------------------------------------------------------------

def _write_shortlist_7(shortlist: list[PointResult4], path: str) -> None:
    with open(path, "w") as f:
        f.write("# R61 Track 4 — charge-neutrality shortlist\n\n")
        f.write("Seven-criterion composite (equal weights).  ")
        f.write("Charge-neutrality replaces pair cleanliness; charged-extras ")
        f.write("replaces sterile count; harmonic flag (0 if any two triplet ")
        f.write("members share signed reduced form) is added.\n\n")
        f.write("Pair enum filter is LOOSE (rel_split ≤ 0.5) so hybrid ")
        f.write("triplets using |n_tube|≥2 modes can surface.  The charge ")
        f.write("check inside scoring uses tight delta = 0.1.\n\n")
        f.write("Deduplicated by mode-set.\n\n")
        f.write("| # | ε_ν | s_ν | triplet | composite | ratio | CN | simpl | spin | low | C-ex (n) | !harm | mechanisms |\n")
        f.write("|--:|-----|-----|---------|----------:|------:|---:|------:|-----:|----:|---------:|------:|:-----------|\n")
        for i, r in enumerate(shortlist, start=1):
            t = r.best; sc = r.best_scores
            trip = (f"({t.a.n_tube:+d},{t.a.n_ring:+d}) "
                    f"({t.b.n_tube:+d},{t.b.n_ring:+d}) "
                    f"({t.c.n_tube:+d},{t.c.n_ring:+d})")
            mech = "/".join(sc.neutrality_mechanisms)
            f.write(
                f"| {i} | {r.eps:.3f} | {r.s:.5f} | {trip} | {sc.composite:.3f} | "
                f"{sc.ratio_exactness:.2f} | {sc.charge_neutrality:.2f} | "
                f"{sc.mode_simplicity:.2f} | {sc.spin_quality:.2f} | "
                f"{int(sc.lowest_bonus)} | {sc.charged_extras:.2f} ({sc.n_charged_extras}) | "
                f"{int(sc.no_harmonic)} | {mech} |\n"
            )


def _write_hybrid_candidates(shortlist: list[PointResult4], path: str) -> None:
    """Pull out triplets that use mixed neutrality mechanisms (at least one
    |n_tube|≥2 mode alongside Majorana-paired modes)."""
    with open(path, "w") as f:
        f.write("# R61 Track 4 — hybrid-mechanism candidates\n\n")
        f.write("Triplets combining Majorana-paired (|n_tube|=1) modes with ")
        f.write("inherently-uncharged (|n_tube|≥2) modes.  These rely on R48's ")
        f.write("CP synchronization rule rather than pair degeneracy for one ")
        f.write("or more mass eigenstates.\n\n")
        hybrids = [r for r in shortlist if "R48" in r.best_scores.neutrality_mechanisms]
        if not hybrids:
            f.write("(No hybrid-mechanism triplets in top shortlist.)\n")
            return
        f.write("| rank | ε_ν | s_ν | triplet | mechanisms | composite | !harm |\n")
        f.write("|-----:|-----|-----|---------|:-----------|----------:|------:|\n")
        for r in hybrids:
            t = r.best; sc = r.best_scores
            trip = (f"({t.a.n_tube:+d},{t.a.n_ring:+d}) "
                    f"({t.b.n_tube:+d},{t.b.n_ring:+d}) "
                    f"({t.c.n_tube:+d},{t.c.n_ring:+d})")
            mech = "/".join(sc.neutrality_mechanisms)
            rank = next(i+1 for i, x in enumerate(shortlist)
                        if _modeset_key(x.best) == _modeset_key(t))
            f.write(
                f"| {rank} | {r.eps:.3f} | {r.s:.5f} | {trip} | {mech} | "
                f"{sc.composite:.3f} | {int(sc.no_harmonic)} |\n"
            )


def _save_heatmap_4(eps_grid: np.ndarray, s_grid: np.ndarray,
                     results: list[PointResult4], path: str) -> str | None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return None
    scores = np.zeros((len(eps_grid), len(s_grid)))
    by_pt = {(round(r.eps, 5), round(r.s, 8)): r for r in results}
    for i, e in enumerate(eps_grid):
        for j, s in enumerate(s_grid):
            r = by_pt.get((round(float(e), 5), round(float(s), 8)))
            if r is not None and r.best_scores is not None:
                scores[i, j] = r.best_scores.composite
    fig, ax = plt.subplots(figsize=(7, 5))
    im = ax.pcolormesh(s_grid, eps_grid, scores, shading="auto", cmap="viridis")
    ax.set_xscale("log")
    ax.set_xlabel(r"$s_\nu$")
    ax.set_ylabel(r"$\varepsilon_\nu$")
    ax.set_title("R61 T4 composite score (charge-neutrality + harmonic flag)")
    fig.colorbar(im, ax=ax, label="composite score")
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("R61 Track 4 — charge-neutrality scoring and harmonic flagging")
    print("=" * 70)
    print()

    print("Smoke tests:")
    print("-" * 70)
    smokes = smoke_tests()
    all_pass = True
    for name, ok, detail in smokes:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")
        print(f"         {detail}")
        all_pass = all_pass and ok
    print()

    # -- Grid --
    eps_grid = np.linspace(2.0, 10.0, 17)
    base_s = np.geomspace(0.005, 0.1, 41).tolist()
    s_grid = np.array(sorted(set(base_s + [0.022, 0.060])))  # include hybrid s

    # -- Rank under equal weights --
    w_equal = (1/7,) * 7
    print("Ranking under equal 7-criterion weights...")
    results = rank_candidates_7(
        eps_grid, s_grid, weights=w_equal,
        pair_delta=0.1, enum_delta=0.5,  # loose enum, tight charge check
        tol=0.027, target=33.6, nt_max=3, nr_max=6,
    )
    good = [r for r in results if r.best_scores is not None]
    print(f"  {len(good)} / {len(results)} (ε, s) points have viable triplets")
    if good:
        scores_arr = np.array([r.best_scores.composite for r in good])
        print(f"  composite: min={scores_arr.min():.3f}, max={scores_arr.max():.3f}, "
              f"mean={scores_arr.mean():.3f}")

    shortlist = deduplicate(results, 15)
    print()
    print("Top-15 unique candidates (by mode-set):")
    print(f"  {'rank':<5}{'ε_ν':<8}{'s_ν':<10}{'comp':<7}{'!harm':<7}{'CN':<6}{'mechanisms':<30}triplet")
    for i, r in enumerate(shortlist, start=1):
        t = r.best; sc = r.best_scores
        trip = (f"({t.a.n_tube:+d},{t.a.n_ring:+d}) "
                f"({t.b.n_tube:+d},{t.b.n_ring:+d}) "
                f"({t.c.n_tube:+d},{t.c.n_ring:+d})")
        mech = "/".join(sc.neutrality_mechanisms)
        print(f"  {i:<5}{r.eps:<8.3f}{r.s:<10.5f}{sc.composite:<7.3f}"
              f"{int(sc.no_harmonic):<7}{sc.charge_neutrality:<6.2f}"
              f"{mech:<30}{trip}")
    print()

    # -- Outputs --
    os.makedirs(OUT_DIR, exist_ok=True)
    shortlist_path = os.path.join(OUT_DIR, "track4_shortlist.md")
    _write_shortlist_7(shortlist, shortlist_path)
    print(f"  shortlist:                  {shortlist_path}")

    hybrid_path = os.path.join(OUT_DIR, "track4_hybrid_candidates.md")
    _write_hybrid_candidates(shortlist, hybrid_path)
    print(f"  hybrid candidates:          {hybrid_path}")

    heatmap_path = _save_heatmap_4(
        eps_grid, s_grid, results,
        os.path.join(OUT_DIR, "track4_score_heatmap.png"),
    )
    if heatmap_path:
        print(f"  heatmap:                    {heatmap_path}")

    print()
    print("=" * 70)
    print(f"Smoke tests: {'ALL PASS' if all_pass else 'FAILURES PRESENT'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
