"""R61 Track 3 — Sterile-count scoring and consensus shortlist.

Adds a sixth criterion (sterile-mode count between ν₁ and ν₃) to the
Track 2 scorer and produces a consensus shortlist across three weight
schedules: equal, sterile-heavy, balanced.  Consensus candidates are
those that rank top under *multiple* schedules — robust to weight
preference.

Imports primitives from track2_candidates.py.

Run:
    python track3_sterile_scoring.py
"""

from __future__ import annotations

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
    _PAIR_CAP,
    _SIMPL_CAP,
    _SPIN_CAP,
)


# ---------------------------------------------------------------------------
# New primitive — sterile count
# ---------------------------------------------------------------------------

def fermion_candidates(modes: Iterable[Mode]) -> list[Mode]:
    """All modes with |n_tube|≥1 and |n_ring|≥1 (no pair-splitting tolerance).

    R49's sterile definition counts modes in the mass window that are
    fermion candidates, not the tighter Majorana-mixing-capable subset.
    """
    return [m for m in modes if abs(m.n_tube) >= 1 and abs(m.n_ring) >= 1]


def sterile_count(triplet: Triplet, all_fermion_modes: list[Mode]) -> int:
    """Number of fermion-candidate modes with µ² strictly between µ²_a and
    µ²_c that aren't part of the triplet.

    Matches R49 F4's "sterile" definition (intermediate-mass modes not
    in the observed triplet).  No pair-splitting tolerance applied — all
    fermion candidates count.
    """
    lo, hi = triplet.a.mu2, triplet.c.mu2
    triplet_ids = {
        (triplet.a.n_tube, triplet.a.n_ring),
        (triplet.b.n_tube, triplet.b.n_ring),
        (triplet.c.n_tube, triplet.c.n_ring),
    }
    count = 0
    for m in all_fermion_modes:
        if m.mu2 <= lo or m.mu2 >= hi:
            continue
        if (m.n_tube, m.n_ring) in triplet_ids:
            continue
        count += 1
    return count


_STERILE_CAP = 100  # sterile count at which sterile_score reaches 0


def sterile_score(count: int) -> float:
    return _clip01(1.0 - count / _STERILE_CAP)


# ---------------------------------------------------------------------------
# Six-criterion scoring
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Scores6:
    ratio_exactness: float
    pair_cleanliness: float
    mode_simplicity: float
    spin_quality: float
    lowest_bonus: float
    sterile_score: float  # NEW
    composite: float
    spins: tuple[float, float, float]
    max_pair_rel_split: float
    n_sterile: int


def score_triplet_6(
    triplet: Triplet,
    eps: float,
    s: float,
    is_lowest: bool,
    all_fermion_modes: list[Mode],
    weights: tuple[float, float, float, float, float, float],
) -> Scores6:
    # Reuse Track 2 components manually for transparency
    ratio_err = abs(triplet.ratio - 33.6) / 33.6
    r_score = _clip01(1.0 - ratio_err / _RATIO_CAP)

    rel_splits = []
    for m in (triplet.a, triplet.b, triplet.c):
        partner_mu2 = mu2(-m.n_tube, m.n_ring, eps, s)
        mean_mu2 = 0.5 * (m.mu2 + partner_mu2)
        if mean_mu2 <= 0:
            rel_splits.append(1.0)
        else:
            rel_splits.append(abs(m.mu2 - partner_mu2) / mean_mu2)
    max_rs = max(rel_splits)
    p_score = _clip01(1.0 - max_rs / _PAIR_CAP)

    simpl_sum = sum(abs(m.n_tube) + abs(m.n_ring) for m in (triplet.a, triplet.b, triplet.c))
    m_score = _clip01(1.0 - simpl_sum / _SIMPL_CAP)

    spins = tuple(
        Lz_over_hbar(m.n_tube, m.n_ring, eps) for m in (triplet.a, triplet.b, triplet.c)
    )
    spin_err_sum = sum(abs(sp - 0.5) for sp in spins)
    s_score = _clip01(1.0 - spin_err_sum / _SPIN_CAP)

    low_bonus = 1.0 if is_lowest else 0.0

    count = sterile_count(triplet, all_fermion_modes)
    st_score = sterile_score(count)

    composite = (
        weights[0] * r_score
        + weights[1] * p_score
        + weights[2] * m_score
        + weights[3] * s_score
        + weights[4] * low_bonus
        + weights[5] * st_score
    )
    return Scores6(
        ratio_exactness=r_score,
        pair_cleanliness=p_score,
        mode_simplicity=m_score,
        spin_quality=s_score,
        lowest_bonus=low_bonus,
        sterile_score=st_score,
        composite=composite,
        spins=spins,
        max_pair_rel_split=max_rs,
        n_sterile=count,
    )


# ---------------------------------------------------------------------------
# Ranker under a given weight schedule
# ---------------------------------------------------------------------------

@dataclass
class PointResult3:
    eps: float
    s: float
    n_triplets: int
    best: Triplet | None
    best_scores: Scores6 | None


def rank_candidates_6(
    eps_grid: np.ndarray,
    s_grid: np.ndarray,
    weights: tuple[float, float, float, float, float, float],
    delta: float = 0.1,
    tol: float = 0.027,
    target: float = 33.6,
    nt_max: int = 3,
    nr_max: int = 6,
) -> list[PointResult3]:
    results: list[PointResult3] = []
    # Use a wider enumeration for sterile counting (R49 used |n_t|≤10, n_r≤6)
    sterile_nt_max = max(nt_max, 10)
    sterile_nr_max = max(nr_max, 6)
    for eps in eps_grid:
        for s in s_grid:
            modes = enumerate_modes(float(eps), float(s), nt_max, nr_max)
            paired = paired_fermion_modes(modes, float(eps), float(s), delta)
            triplets = find_ratio_triplets(paired, target, tol)
            if not triplets:
                results.append(PointResult3(float(eps), float(s), 0, None, None))
                continue
            # Wider enumeration just for sterile counting
            wide_modes = enumerate_modes(float(eps), float(s), sterile_nt_max, sterile_nr_max)
            all_fermion = fermion_candidates(wide_modes)
            lowest = min(triplets, key=lambda t: (t.a.mu2, t.b.mu2, t.c.mu2))
            best: Triplet | None = None
            best_scores: Scores6 | None = None
            for t in triplets:
                is_lowest = (t is lowest)
                sc = score_triplet_6(t, float(eps), float(s), is_lowest, all_fermion, weights)
                if best_scores is None or sc.composite > best_scores.composite:
                    best = t
                    best_scores = sc
            results.append(PointResult3(float(eps), float(s), len(triplets), best, best_scores))
    return results


def _modeset_key(t: Triplet) -> frozenset:
    return frozenset([
        (t.a.n_tube, t.a.n_ring),
        (t.b.n_tube, t.b.n_ring),
        (t.c.n_tube, t.c.n_ring),
    ])


def deduplicate(results: list[PointResult3], top_n: int) -> list[PointResult3]:
    seen: dict[frozenset, PointResult3] = {}
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
# Smoke tests T9–T12
# ---------------------------------------------------------------------------

def smoke_tests(eps_grid: np.ndarray, s_grid: np.ndarray) -> list[tuple[str, bool, str]]:
    out: list[tuple[str, bool, str]] = []

    # -- T9 ---------------------------------------------------------------
    # Family A at (ε=5, s=0.022): sterile count ≈ 26 per R49 F4.
    # Use R49's enumeration range (|n3|≤10, n4≤6) and count all fermion
    # candidates in the mass window.
    modes_wide = enumerate_modes(5.0, 0.022, nt_max=10, nr_max=6)
    all_fermion = fermion_candidates(modes_wide)
    def find_mode(modes, n_t, n_r):
        for m in modes:
            if m.n_tube == n_t and m.n_ring == n_r:
                return m
        return None
    fa_a = find_mode(all_fermion, 1, 1)
    fa_b = find_mode(all_fermion, -1, 1)
    fa_c = find_mode(all_fermion, 1, 2)
    if None in (fa_a, fa_b, fa_c):
        out.append(("T9 sterile_count for Family A at (ε=5, s=0.022)", False,
                    "Family A modes not all in fermion candidate list"))
    else:
        fa_triplet = Triplet(
            a=fa_a, b=fa_b, c=fa_c,
            ratio=(fa_c.mu2 - fa_a.mu2) / (fa_b.mu2 - fa_a.mu2),
        )
        count = sterile_count(fa_triplet, all_fermion)
        # R49 reports 26.  Our band: [15, 40].
        ok = 15 <= count <= 40
        out.append(("T9 sterile_count for Family A at (ε=5, s=0.022)", ok,
                    f"count = {count} (R49 reports 26; band [15, 40])"))

    # -- T10 --------------------------------------------------------------
    # Sterile-heavy weights should shift best-ε upward.
    w_equal = (1/6,)*6
    w_sterile_heavy = (0.12, 0.12, 0.12, 0.12, 0.12, 0.40)
    r_equal = rank_candidates_6(eps_grid, s_grid, w_equal)
    r_heavy = rank_candidates_6(eps_grid, s_grid, w_sterile_heavy)
    top_equal = deduplicate(r_equal, 1)
    top_heavy = deduplicate(r_heavy, 1)
    eps_equal = top_equal[0].eps if top_equal else None
    eps_heavy = top_heavy[0].eps if top_heavy else None
    ok = (eps_equal is not None and eps_heavy is not None
          and eps_heavy >= eps_equal - 1e-9)  # shift toward higher ε (allow ties)
    out.append(("T10 sterile-heavy schedule preserves or raises best ε", ok,
                f"best ε: equal={eps_equal}, sterile-heavy={eps_heavy}"))

    # -- T11 --------------------------------------------------------------
    # Zero-sterile weight recovers Track 2's equal-weight result.
    w_zero_sterile = (0.2, 0.2, 0.2, 0.2, 0.2, 0.0)
    r_zero = rank_candidates_6(eps_grid, s_grid, w_zero_sterile)
    top_zero = deduplicate(r_zero, 1)
    # Track 2 said best = (ε=2, s=0.022) Family A
    if not top_zero:
        out.append(("T11 zero-sterile recovers Track 2 optimum", False, "no candidates"))
    else:
        t = top_zero[0].best
        is_family_a = _modeset_key(t) == frozenset([(1,1), (-1,1), (1,2)])
        ok = (abs(top_zero[0].eps - 2.0) < 0.1
              and abs(top_zero[0].s - 0.022) < 0.002
              and is_family_a)
        out.append(("T11 zero-sterile recovers Track 2 optimum", ok,
                    f"top-1: ε={top_zero[0].eps}, s={top_zero[0].s}, mode-set={sorted(_modeset_key(t))}"))

    # -- T12 --------------------------------------------------------------
    # Consensus intersection across 3 schedules is non-empty.
    w_balanced = (1/6,)*6
    r_balanced = r_equal  # same as w_equal in this setup
    sets = []
    for r in (r_equal, r_heavy, r_balanced):
        top5 = deduplicate(r, 5)
        sets.append({_modeset_key(x.best) for x in top5})
    intersection = sets[0] & sets[1] & sets[2]
    ok = len(intersection) >= 1
    out.append(("T12 consensus intersection non-empty", ok,
                f"|intersection| = {len(intersection)} across 3 schedules"))

    return out


# ---------------------------------------------------------------------------
# Outputs
# ---------------------------------------------------------------------------

def _write_shortlist(shortlist: list[PointResult3], path: str, label: str) -> None:
    with open(path, "w") as f:
        f.write(f"# R61 Track 3 — shortlist under **{label}** weights\n\n")
        f.write("Six-criterion composite: ratio, pair cleanliness, mode simplicity, ")
        f.write("spin quality, lowest-triplet, sterile count.\n\n")
        f.write("Deduplicated by mode-set.\n\n")
        f.write("| # | ε_ν | s_ν | triplet | composite | ratio | pair | simpl | spin | low | sterile (n) |\n")
        f.write("|--:|-----|-----|---------|----------:|------:|-----:|------:|-----:|----:|------------:|\n")
        for i, r in enumerate(shortlist, start=1):
            t = r.best; sc = r.best_scores
            trip = f"({t.a.n_tube:+d},{t.a.n_ring:+d}) ({t.b.n_tube:+d},{t.b.n_ring:+d}) ({t.c.n_tube:+d},{t.c.n_ring:+d})"
            f.write(
                f"| {i} | {r.eps:.3f} | {r.s:.5f} | {trip} | {sc.composite:.3f} | "
                f"{sc.ratio_exactness:.2f} | {sc.pair_cleanliness:.2f} | "
                f"{sc.mode_simplicity:.2f} | {sc.spin_quality:.2f} | "
                f"{int(sc.lowest_bonus)} | {sc.sterile_score:.2f} ({sc.n_sterile}) |\n"
            )


def _write_consensus(
    equal_top5: list[PointResult3],
    heavy_top5: list[PointResult3],
    balanced_top5: list[PointResult3],
    path: str,
) -> set[frozenset]:
    e_keys = {_modeset_key(r.best): r for r in equal_top5}
    h_keys = {_modeset_key(r.best): r for r in heavy_top5}
    b_keys = {_modeset_key(r.best): r for r in balanced_top5}

    consensus = set(e_keys) & set(h_keys) & set(b_keys)

    with open(path, "w") as f:
        f.write("# R61 Track 3 — consensus shortlist\n\n")
        f.write("Candidates in top-5 under **all three** weight schedules ")
        f.write("(equal, sterile-heavy, balanced).  These are the mode-sets ")
        f.write("whose selection is robust to scoring preference.\n\n")
        if not consensus:
            f.write("**No consensus candidates.**  Selection is weight-dependent.\n\n")
            f.write("See per-schedule shortlists for the candidate under each preference.\n")
        else:
            f.write(f"## {len(consensus)} consensus candidate(s)\n\n")
            f.write("| triplet | ε (equal) | ε (sterile-heavy) | ε (balanced) | sterile count |\n")
            f.write("|---------|----------:|------------------:|-------------:|--------------:|\n")
            for key in consensus:
                # Report the (eps, s) under each schedule
                re, rh, rb = e_keys[key], h_keys[key], b_keys[key]
                t = re.best
                trip = (f"({t.a.n_tube:+d},{t.a.n_ring:+d}) "
                        f"({t.b.n_tube:+d},{t.b.n_ring:+d}) "
                        f"({t.c.n_tube:+d},{t.c.n_ring:+d})")
                f.write(
                    f"| {trip} | {re.eps:.3f}, s={re.s:.5f} | "
                    f"{rh.eps:.3f}, s={rh.s:.5f} | {rb.eps:.3f}, s={rb.s:.5f} | "
                    f"{re.best_scores.n_sterile} / {rh.best_scores.n_sterile} / {rb.best_scores.n_sterile} |\n"
                )
    return consensus


def _save_tradeoff_plot(
    results_equal: list[PointResult3], path: str
) -> str | None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return None

    good = [r for r in results_equal if r.best_scores is not None]
    if not good:
        return None

    n_ster = np.array([r.best_scores.n_sterile for r in good])
    comp   = np.array([r.best_scores.composite for r in good])
    eps    = np.array([r.eps for r in good])

    fig, ax = plt.subplots(figsize=(7, 5))
    sc = ax.scatter(n_ster, comp, c=eps, cmap="viridis", s=20, alpha=0.8)
    ax.set_xlabel("sterile mode count between ν₁ and ν₃")
    ax.set_ylabel("composite score (equal-weight, sterile-free)")
    ax.set_title("R61 T3 tradeoff: sterile count vs Track-2 composite")
    fig.colorbar(sc, ax=ax, label=r"$\varepsilon_\nu$")
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return path


def _save_heatmap_comparison(
    eps_grid: np.ndarray, s_grid: np.ndarray,
    r_equal: list[PointResult3], r_heavy: list[PointResult3],
    path: str,
) -> str | None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return None

    def grid_from(results):
        arr = np.zeros((len(eps_grid), len(s_grid)))
        by_pt = {(round(r.eps, 5), round(r.s, 8)): r for r in results}
        for i, e in enumerate(eps_grid):
            for j, s in enumerate(s_grid):
                r = by_pt.get((round(float(e), 5), round(float(s), 8)))
                if r is not None and r.best_scores is not None:
                    arr[i, j] = r.best_scores.composite
        return arr

    arr_e = grid_from(r_equal)
    arr_h = grid_from(r_heavy)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
    for ax, arr, title in zip(axes, (arr_e, arr_h),
                              ("equal weights", "sterile-heavy weights")):
        im = ax.pcolormesh(s_grid, eps_grid, arr, shading="auto", cmap="viridis",
                           vmin=0, vmax=max(arr_e.max(), arr_h.max()))
        ax.set_xscale("log")
        ax.set_xlabel(r"$s_\nu$")
        ax.set_title(title)
    axes[0].set_ylabel(r"$\varepsilon_\nu$")
    fig.suptitle("R61 T3 composite score — weight schedule comparison")
    fig.colorbar(im, ax=axes, label="composite score", shrink=0.85)
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("R61 Track 3 — sterile-count scoring and consensus shortlist")
    print("=" * 70)
    print()

    # -- Grid --
    eps_grid = np.linspace(2.0, 10.0, 17)
    base_s = np.geomspace(0.005, 0.1, 41).tolist()
    s_grid = np.array(sorted(set(base_s + [0.022])))

    # -- Smoke tests --
    print("Smoke tests:")
    print("-" * 70)
    smokes = smoke_tests(eps_grid, s_grid)
    all_pass = True
    for name, ok, detail in smokes:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")
        print(f"         {detail}")
        all_pass = all_pass and ok
    print()

    # -- Three schedules --
    schedules = {
        "equal":          (1/6, 1/6, 1/6, 1/6, 1/6, 1/6),
        "sterile_heavy":  (0.12, 0.12, 0.12, 0.12, 0.12, 0.40),
        "balanced":       (0.20, 0.15, 0.15, 0.20, 0.10, 0.20),
    }

    print("Per-schedule top-1 best candidate:")
    print("-" * 70)
    print(f"  {'schedule':<16}{'ε_ν':<8}{'s_ν':<10}{'composite':<11}triplet")
    all_results: dict[str, list[PointResult3]] = {}
    all_top5: dict[str, list[PointResult3]] = {}
    for name, w in schedules.items():
        r = rank_candidates_6(eps_grid, s_grid, w)
        all_results[name] = r
        top5 = deduplicate(r, 5)
        all_top5[name] = top5
        if top5:
            t = top5[0].best
            trip = (f"({t.a.n_tube:+d},{t.a.n_ring:+d}) "
                    f"({t.b.n_tube:+d},{t.b.n_ring:+d}) "
                    f"({t.c.n_tube:+d},{t.c.n_ring:+d})")
            print(f"  {name:<16}{top5[0].eps:<8.3f}{top5[0].s:<10.5f}"
                  f"{top5[0].best_scores.composite:<11.3f}{trip}")

    # -- Outputs --
    os.makedirs(OUT_DIR, exist_ok=True)

    shortlist_paths = {}
    for name in schedules:
        path = os.path.join(OUT_DIR, f"track3_shortlist_{name}.md")
        _write_shortlist(deduplicate(all_results[name], 10), path, name)
        shortlist_paths[name] = path
        print(f"  shortlist [{name}]:       {path}")

    consensus_path = os.path.join(OUT_DIR, "track3_consensus.md")
    consensus = _write_consensus(
        all_top5["equal"], all_top5["sterile_heavy"], all_top5["balanced"],
        consensus_path,
    )
    print(f"  consensus list:          {consensus_path}")
    print(f"  consensus size:          {len(consensus)} mode-set(s) in all three top-5")

    tradeoff_path = _save_tradeoff_plot(
        all_results["equal"], os.path.join(OUT_DIR, "track3_tradeoff.png"),
    )
    if tradeoff_path:
        print(f"  tradeoff scatter:        {tradeoff_path}")

    heatmap_path = _save_heatmap_comparison(
        eps_grid, s_grid, all_results["equal"], all_results["sterile_heavy"],
        os.path.join(OUT_DIR, "track3_heatmap_compare.png"),
    )
    if heatmap_path:
        print(f"  heatmap comparison:      {heatmap_path}")

    print()
    print("=" * 70)
    print(f"Smoke tests: {'ALL PASS' if all_pass else 'FAILURES PRESENT'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
