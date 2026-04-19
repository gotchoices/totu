"""R61 Track 2 — Candidate ranking and best-fit selection.

Under R49's convention: µ² = (n_tube/ε)² + (n_ring − n_tube·s)² with
tuple (n_tube, n_ring).  ±n_tube are C-conjugate pairs.  Spin-½ via
R49's finite-ε formula L_z/ℏ = 2π²·q²·(2+ε²) / I²(p, q, ε).

Composite scoring per triplet: ratio exactness, pair cleanliness,
mode simplicity, spin quality, lowest-triplet bonus.  Ranks (ε, s)
by best-triplet composite and emits a shortlist + per-candidate
detail.

Run:
    python track2_candidates.py
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from typing import Iterable

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "outputs")


# ---------------------------------------------------------------------------
# Convention-aligned primitives (R49 form)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Mode:
    """Torus mode.  n_tube = first coord, n_ring = second coord (R49 form)."""
    n_tube: int
    n_ring: int
    mu2: float

    def __repr__(self) -> str:
        return f"({self.n_tube:+d},{self.n_ring:+d}):µ²={self.mu2:.5f}"


def mu2(n_tube: int, n_ring: int, eps: float, s: float) -> float:
    """R49 form: µ² = (n_tube/ε)² + (n_ring − n_tube·s)²."""
    return (n_tube / eps) ** 2 + (n_ring - n_tube * s) ** 2


def enumerate_modes(eps: float, s: float, nt_max: int, nr_max: int) -> list[Mode]:
    """All (|n_tube|≤nt_max, 0≤n_ring≤nr_max), excluding (0, 0)."""
    out: list[Mode] = []
    for n_t in range(-nt_max, nt_max + 1):
        for n_r in range(0, nr_max + 1):
            if n_t == 0 and n_r == 0:
                continue
            out.append(Mode(n_t, n_r, mu2(n_t, n_r, eps, s)))
    out.sort(key=lambda m: m.mu2)
    return out


def paired_fermion_modes(
    modes: Iterable[Mode], eps: float, s: float, delta: float
) -> list[Mode]:
    """Keep modes with |n_tube|≥1 AND |n_ring|≥1 whose −n_tube partner has
    µ² splitting/mean ≤ delta.

    The |n_ring|≥1 requirement excludes pure-tube modes (n_ring=0), which
    have L_z/ℏ = 0 under R49's formula and are not fermion candidates.  This
    matches R49's implicit convention (all of Families A, B, C have n_ring≥1).
    """
    keep: list[Mode] = []
    for m in modes:
        if abs(m.n_tube) < 1 or abs(m.n_ring) < 1:
            continue
        partner_mu2 = mu2(-m.n_tube, m.n_ring, eps, s)
        mean_mu2 = 0.5 * (m.mu2 + partner_mu2)
        if mean_mu2 <= 0:
            continue
        rel_split = abs(m.mu2 - partner_mu2) / mean_mu2
        if rel_split <= delta:
            keep.append(m)
    keep.sort(key=lambda m: m.mu2)
    return keep


@dataclass(frozen=True)
class Triplet:
    a: Mode
    b: Mode
    c: Mode
    ratio: float


def find_ratio_triplets(
    modes: list[Mode], target: float, tol: float
) -> list[Triplet]:
    out: list[Triplet] = []
    n = len(modes)
    for i in range(n):
        for j in range(i + 1, n):
            d21 = modes[j].mu2 - modes[i].mu2
            if d21 <= 1e-12:
                continue
            for k in range(j + 1, n):
                d31 = modes[k].mu2 - modes[i].mu2
                if d31 <= d21:
                    continue
                ratio = d31 / d21
                if abs(ratio - target) / target <= tol:
                    out.append(Triplet(modes[i], modes[j], modes[k], ratio))
    return out


@dataclass(frozen=True)
class CombEntry:
    nt_from: int
    nt_to: int
    dm2_mean: float
    dm2_spread: float
    dmu2_mean: float
    dmu2_spread: float


def delta_m2_comb(
    eps: float, s: float, E0_sq_eV2: float, max_dn: int = 5, nr_sample: int = 3
) -> list[CombEntry]:
    """Clusters from n_ring transitions under R49 convention.

    Note: under R49 form, µ² = (n_tube/ε)² + (n_ring − n_tube·s)², so the
    'comb' is driven by Δn_ring transitions at fixed n_tube, since that is
    what produces the 33.6 ratio.
    """
    entries: list[CombEntry] = []
    for a in range(1, max_dn):
        for b in range(a + 1, max_dn + 1):
            samples = []
            for n_t in range(-nr_sample, nr_sample + 1):
                samples.append(
                    mu2(n_t, b, eps, s) - mu2(n_t, a, eps, s)
                )
            arr = np.array(samples)
            dmu2_mean = float(arr.mean())
            dmu2_spread = float(arr.max() - arr.min())
            entries.append(
                CombEntry(
                    nt_from=a,
                    nt_to=b,
                    dm2_mean=dmu2_mean * E0_sq_eV2,
                    dm2_spread=dmu2_spread * E0_sq_eV2,
                    dmu2_mean=dmu2_mean,
                    dmu2_spread=dmu2_spread,
                )
            )
    entries.sort(key=lambda e: e.dm2_mean)
    return entries


# ---------------------------------------------------------------------------
# R49 spin-½ formula (finite-ε)
# ---------------------------------------------------------------------------

_spin_cache: dict[tuple[int, int, float], float] = {}


def compute_I(p: int, q: int, eps: float, n_samples: int = 2048) -> float:
    """∫₀²π √(p²ε² + q²(1 + ε cos(p·t))²) dt — the geodesic length integral."""
    t = np.linspace(0.0, 2 * np.pi, n_samples, endpoint=False)
    dt = 2 * np.pi / n_samples
    rho = 1.0 + eps * np.cos(p * t)
    integrand = np.sqrt(p * p * eps * eps + q * q * rho * rho)
    return float(np.sum(integrand) * dt)


def Lz_over_hbar(p: int, q: int, eps: float) -> float:
    """L_z/ℏ per R49 formula: 2π²·q²·(2+ε²)/I² then divided by |q|.

    Returns 0 for q = 0 (no ring winding means no spin axis).
    """
    if abs(q) == 0:
        return 0.0
    key = (abs(int(p)), abs(int(q)), round(float(eps), 5))
    if key not in _spin_cache:
        I = compute_I(abs(p), abs(q), eps)
        S = 2.0 * np.pi ** 2 * q * q * (2.0 + eps * eps) / (I * I)
        _spin_cache[key] = S / abs(q)
    return _spin_cache[key]


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Scores:
    ratio_exactness: float   # [0, 1], 1 is best
    pair_cleanliness: float  # [0, 1]
    mode_simplicity: float   # [0, 1]
    spin_quality: float      # [0, 1]
    lowest_bonus: float      # 0 or 1
    composite: float         # weighted sum
    spins: tuple[float, float, float] = field(default=(0.0, 0.0, 0.0))
    max_pair_rel_split: float = 0.0


# Fixed-scale normalization parameters (not data-driven to keep the scorer
# interpretable).  Anything worse than these caps gets score 0.
_RATIO_CAP = 0.01       # 1% ratio error
_PAIR_CAP = 0.1         # 10% pair splitting/mean
_SIMPL_CAP = 20         # sum of |n_tube|+|n_ring| per triplet
_SPIN_CAP = 1.5         # sum of |Lz−0.5| across 3 modes


def _clip01(x: float) -> float:
    return max(0.0, min(1.0, x))


def score_triplet(
    triplet: Triplet,
    eps: float,
    s: float,
    is_lowest: bool,
    weights: tuple[float, float, float, float, float] = (0.2, 0.2, 0.2, 0.2, 0.2),
) -> Scores:
    # ratio exactness
    ratio_err = abs(triplet.ratio - 33.6) / 33.6
    ratio_score = _clip01(1.0 - ratio_err / _RATIO_CAP)

    # pair cleanliness: for each of a, b, c compute ±n_tube splitting / mean
    rel_splits = []
    for m in (triplet.a, triplet.b, triplet.c):
        partner_mu2 = mu2(-m.n_tube, m.n_ring, eps, s)
        mean_mu2 = 0.5 * (m.mu2 + partner_mu2)
        if mean_mu2 <= 0:
            rel_splits.append(1.0)
        else:
            rel_splits.append(abs(m.mu2 - partner_mu2) / mean_mu2)
    max_rs = max(rel_splits)
    pair_score = _clip01(1.0 - max_rs / _PAIR_CAP)

    # mode simplicity
    simpl_sum = sum(abs(m.n_tube) + abs(m.n_ring) for m in (triplet.a, triplet.b, triplet.c))
    simpl_score = _clip01(1.0 - simpl_sum / _SIMPL_CAP)

    # spin quality
    spins = tuple(
        Lz_over_hbar(m.n_tube, m.n_ring, eps) for m in (triplet.a, triplet.b, triplet.c)
    )
    spin_err_sum = sum(abs(sp - 0.5) for sp in spins)
    spin_score = _clip01(1.0 - spin_err_sum / _SPIN_CAP)

    # lowest-triplet bonus
    lowest = 1.0 if is_lowest else 0.0

    composite = (
        weights[0] * ratio_score
        + weights[1] * pair_score
        + weights[2] * simpl_score
        + weights[3] * spin_score
        + weights[4] * lowest
    )
    return Scores(
        ratio_exactness=ratio_score,
        pair_cleanliness=pair_score,
        mode_simplicity=simpl_score,
        spin_quality=spin_score,
        lowest_bonus=lowest,
        composite=composite,
        spins=spins,
        max_pair_rel_split=max_rs,
    )


# ---------------------------------------------------------------------------
# Ranker
# ---------------------------------------------------------------------------

@dataclass
class PointResult:
    eps: float
    s: float
    n_triplets: int
    best: Triplet | None
    best_scores: Scores | None


def rank_candidates(
    eps_grid: np.ndarray,
    s_grid: np.ndarray,
    delta: float = 0.1,
    tol: float = 0.01,
    target: float = 33.6,
    nt_max: int = 3,
    nr_max: int = 6,
    weights: tuple[float, float, float, float, float] = (0.2, 0.2, 0.2, 0.2, 0.2),
) -> list[PointResult]:
    results: list[PointResult] = []
    for eps in eps_grid:
        for s in s_grid:
            modes = enumerate_modes(float(eps), float(s), nt_max, nr_max)
            paired = paired_fermion_modes(modes, float(eps), float(s), delta)
            triplets = find_ratio_triplets(paired, target, tol)
            if not triplets:
                results.append(PointResult(float(eps), float(s), 0, None, None))
                continue
            lowest = min(triplets, key=lambda t: (t.a.mu2, t.b.mu2, t.c.mu2))
            best: Triplet | None = None
            best_scores: Scores | None = None
            for t in triplets:
                is_lowest = (t is lowest)
                sc = score_triplet(t, float(eps), float(s), is_lowest, weights)
                if best_scores is None or sc.composite > best_scores.composite:
                    best = t
                    best_scores = sc
            results.append(
                PointResult(float(eps), float(s), len(triplets), best, best_scores)
            )
    return results


# ---------------------------------------------------------------------------
# Smoke tests T5–T8
# ---------------------------------------------------------------------------

def _approx(a: float, b: float, rel_tol: float = 1e-3, abs_tol: float = 0.0) -> bool:
    return abs(a - b) <= max(abs_tol, rel_tol * max(1.0, abs(b)))


def smoke_tests() -> list[tuple[str, bool, str]]:
    out: list[tuple[str, bool, str]] = []

    # -- T5 ---------------------------------------------------------------
    # R49 formula + E₀ = 29.25 meV on Family A reproduces published masses.
    eps, s = 5.0, 0.022
    mu2_11 = mu2(1, 1, eps, s)
    mu2_m11 = mu2(-1, 1, eps, s)
    mu2_12 = mu2(1, 2, eps, s)
    # Pin E₀ via m₁ = 29.2 meV → E₀ = 29.2 / √µ²(1,1)
    E0_pin = 29.2 / np.sqrt(mu2_11)
    m1 = E0_pin * np.sqrt(mu2_11)
    m2 = E0_pin * np.sqrt(mu2_m11)
    m3 = E0_pin * np.sqrt(mu2_12)
    ok = _approx(m1, 29.2, 1e-3) and _approx(m2, 30.5, 1e-2) and _approx(m3, 58.2, 1e-2)
    detail = f"E₀ = {E0_pin:.3f} meV; m = ({m1:.3f}, {m2:.3f}, {m3:.3f}) meV"
    out.append(("T5 R49 formula reproduces Family A masses", ok, detail))

    # -- T6 ---------------------------------------------------------------
    # Lz/ℏ(0, 1, 0) = 1.0 analytically; at ε=1, = 3/8 = 0.375.
    v_eps0 = Lz_over_hbar(0, 1, 0.0)
    v_eps1 = Lz_over_hbar(0, 1, 1.0)
    ok = _approx(v_eps0, 1.0, 1e-3) and _approx(v_eps1, 0.375, 1e-2)
    detail = f"Lz/ℏ(0,1,0) = {v_eps0:.4f}; Lz/ℏ(0,1,1) = {v_eps1:.4f}"
    out.append(("T6 Spin formula matches analytical limits", ok, detail))

    # -- T7 ---------------------------------------------------------------
    # R49 F7: Family A spins L_z/ℏ ≈ 0.36–0.37 at ε=5.
    sp_11 = Lz_over_hbar(1, 1, 5.0)
    sp_m11 = Lz_over_hbar(-1, 1, 5.0)
    sp_12 = Lz_over_hbar(1, 2, 5.0)
    in_band = lambda v: 0.30 <= v <= 0.45
    ok = in_band(sp_11) and in_band(sp_m11) and in_band(sp_12)
    detail = f"spins (1,1)={sp_11:.4f}, (-1,1)={sp_m11:.4f}, (1,2)={sp_12:.4f}"
    out.append(("T7 Family A spins match R49 F7 band [0.30, 0.45]", ok, detail))

    # -- T8 ---------------------------------------------------------------
    # Ranking at (ε=5, s=0.022) places Family A in top 3 under equal-weights.
    eps = 5.0
    s = 0.022
    modes = enumerate_modes(eps, s, nt_max=3, nr_max=6)
    paired = paired_fermion_modes(modes, eps, s, delta=0.1)
    triplets = find_ratio_triplets(paired, 33.6, 0.01)
    lowest = min(triplets, key=lambda t: (t.a.mu2, t.b.mu2, t.c.mu2))
    scored = []
    for t in triplets:
        sc = score_triplet(t, eps, s, t is lowest)
        scored.append((t, sc))
    scored.sort(key=lambda ts: -ts[1].composite)
    # Family A = (1,1), (-1,1), (1,2) — check presence in top 3
    family_a_in_top3 = False
    for t, _sc in scored[:3]:
        ids = {(t.a.n_tube, t.a.n_ring), (t.b.n_tube, t.b.n_ring), (t.c.n_tube, t.c.n_ring)}
        if ids == {(1, 1), (-1, 1), (1, 2)}:
            family_a_in_top3 = True
            break
    ok = family_a_in_top3
    top3_desc = "; ".join(
        f"score={sc.composite:.3f} {t.a}/{t.b}/{t.c}"
        for t, sc in scored[:3]
    )
    detail = f"top-3 at Family A geometry: {top3_desc}"
    out.append(("T8 Family A present in top-3 at its geometry", ok, detail))

    return out


# ---------------------------------------------------------------------------
# Shortlist + outputs
# ---------------------------------------------------------------------------

def _deduplicate_by_modeset(results: list[PointResult], top_n: int) -> list[PointResult]:
    """Collapse near-identical candidates: same triplet mode-set across (ε, s)
    slots keep only the highest-scoring representative."""
    seen: dict[frozenset, PointResult] = {}
    for r in results:
        if r.best is None or r.best_scores is None:
            continue
        key = frozenset(
            [(r.best.a.n_tube, r.best.a.n_ring),
             (r.best.b.n_tube, r.best.b.n_ring),
             (r.best.c.n_tube, r.best.c.n_ring)]
        )
        if key not in seen or seen[key].best_scores.composite < r.best_scores.composite:
            seen[key] = r
    uniq = list(seen.values())
    uniq.sort(key=lambda r: -r.best_scores.composite)
    return uniq[:top_n]


def write_shortlist_md(shortlist: list[PointResult], path: str) -> None:
    with open(path, "w") as f:
        f.write("# R61 Track 2 — ν-sheet candidate shortlist\n\n")
        f.write("Ranked by composite score with equal weights (0.2 each) across ")
        f.write("five criteria: ratio exactness, pair cleanliness, mode simplicity, ")
        f.write("spin quality, lowest-triplet bonus.\n\n")
        f.write("Deduplicated by mode-set — each unique triplet appears once at its ")
        f.write("best-scoring (ε, s) point.\n\n")
        f.write("| # | ε_ν | s_ν | triplet | ratio | composite | ratio | pair | simpl | spin | lowest |\n")
        f.write("|--:|-----|-----|---------|------:|----------:|------:|-----:|------:|-----:|-------:|\n")
        for i, r in enumerate(shortlist, start=1):
            t = r.best; sc = r.best_scores
            trip = f"({t.a.n_tube:+d},{t.a.n_ring:+d}) · ({t.b.n_tube:+d},{t.b.n_ring:+d}) · ({t.c.n_tube:+d},{t.c.n_ring:+d})"
            f.write(
                f"| {i} | {r.eps:.3f} | {r.s:.5f} | {trip} | {t.ratio:.3f} | "
                f"{sc.composite:.3f} | {sc.ratio_exactness:.2f} | {sc.pair_cleanliness:.2f} | "
                f"{sc.mode_simplicity:.2f} | {sc.spin_quality:.2f} | {int(sc.lowest_bonus)} |\n"
            )


def write_candidate_detail(result: PointResult, path: str, solar_dm2_21: float = 7.53e-5) -> None:
    """Per-candidate report with masses, Δm² comb, and spin table."""
    t = result.best
    sc = result.best_scores
    # Calibrate E₀ so Δm²₂₁ = solar value: Δµ²₂₁ = t.b.mu2 − t.a.mu2, E₀² = solar / Δµ²₂₁
    dmu2_21 = t.b.mu2 - t.a.mu2
    E0_sq_eV2 = solar_dm2_21 / dmu2_21
    E0_meV = np.sqrt(E0_sq_eV2) * 1000
    m1_meV = np.sqrt(t.a.mu2) * E0_meV
    m2_meV = np.sqrt(t.b.mu2) * E0_meV
    m3_meV = np.sqrt(t.c.mu2) * E0_meV
    Sigma_m = m1_meV + m2_meV + m3_meV
    dmu2_31 = t.c.mu2 - t.a.mu2
    dm2_31 = dmu2_31 * E0_sq_eV2

    comb = delta_m2_comb(result.eps, result.s, E0_sq_eV2=E0_sq_eV2, max_dn=5, nr_sample=3)

    with open(path, "w") as f:
        f.write(f"# Candidate: ε_ν = {result.eps:.3f}, s_ν = {result.s:.5f}\n\n")
        f.write(f"Composite score: **{sc.composite:.3f}**\n\n")
        f.write("## Distinguished triplet\n\n")
        f.write("| Mode (n_tube, n_ring) | µ² | mass (meV) | L_z/ℏ |\n")
        f.write("|-----------------------|---:|-----------:|------:|\n")
        for m, mi_meV, spin in [
            (t.a, m1_meV, sc.spins[0]),
            (t.b, m2_meV, sc.spins[1]),
            (t.c, m3_meV, sc.spins[2]),
        ]:
            f.write(f"| ({m.n_tube:+d}, {m.n_ring:+d}) | {m.mu2:.5f} | {mi_meV:.3f} | {spin:.4f} |\n")
        f.write(f"\nRatio (µ_c²−µ_a²)/(µ_b²−µ_a²) = **{t.ratio:.4f}** (target 33.6)\n\n")
        f.write(f"E₀ (calibrated to Δm²₂₁ = {solar_dm2_21:.3e} eV²): **{E0_meV:.2f} meV**\n\n")
        f.write(f"Δm²₃₁ predicted: **{dm2_31:.3e} eV²** (atmospheric target 2.53×10⁻³)\n\n")
        f.write(f"Σm (triplet): **{Sigma_m:.1f} meV**\n\n")
        f.write("## Score breakdown\n\n")
        f.write(f"- Ratio exactness: {sc.ratio_exactness:.3f}\n")
        f.write(f"- Pair cleanliness (max rel split): {sc.pair_cleanliness:.3f} (raw max = {sc.max_pair_rel_split:.4f})\n")
        f.write(f"- Mode simplicity: {sc.mode_simplicity:.3f}\n")
        f.write(f"- Spin quality: {sc.spin_quality:.3f}\n")
        f.write(f"- Lowest-triplet bonus: {int(sc.lowest_bonus)}\n\n")
        f.write("## Predicted Δm² comb\n\n")
        f.write("| Δn_ring | mean (eV²) | spread (eV²) | dimensionless µ² |\n")
        f.write("|:--------|-----------:|-------------:|-----------------:|\n")
        for e in comb:
            f.write(
                f"| {e.nt_from} → {e.nt_to} | {e.dm2_mean:.3e} | {e.dm2_spread:.3e} | "
                f"{e.dmu2_mean:.3f} ± {e.dmu2_spread/2:.3f} |\n"
            )


def weight_sensitivity_audit(
    eps_grid: np.ndarray,
    s_grid: np.ndarray,
    base_weights: tuple[float, ...] = (0.2, 0.2, 0.2, 0.2, 0.2),
    perturbation: float = 0.5,
    top_n: int = 5,
    **kwargs,
) -> dict:
    """Perturb each weight by ±perturbation×base and see if the top-5 rankings
    are stable by mode-set identity."""
    base_results = rank_candidates(eps_grid, s_grid, weights=base_weights, **kwargs)
    base_shortlist = _deduplicate_by_modeset(base_results, top_n)
    base_keys = [
        frozenset([(r.best.a.n_tube, r.best.a.n_ring),
                   (r.best.b.n_tube, r.best.b.n_ring),
                   (r.best.c.n_tube, r.best.c.n_ring)])
        for r in base_shortlist
    ]
    audit = {"perturbations": []}
    for i in range(5):
        for sign in (+1, -1):
            w = list(base_weights)
            w[i] = w[i] * (1 + sign * perturbation)
            # Renormalize
            total = sum(w)
            w = tuple(wi / total for wi in w)
            alt_results = rank_candidates(eps_grid, s_grid, weights=tuple(w), **kwargs)
            alt_shortlist = _deduplicate_by_modeset(alt_results, top_n)
            alt_keys = [
                frozenset([(r.best.a.n_tube, r.best.a.n_ring),
                           (r.best.b.n_tube, r.best.b.n_ring),
                           (r.best.c.n_tube, r.best.c.n_ring)])
                for r in alt_shortlist
            ]
            overlap = len(set(base_keys) & set(alt_keys))
            top1_same = (len(base_keys) > 0 and len(alt_keys) > 0 and base_keys[0] == alt_keys[0])
            crit_name = ["ratio", "pair", "simpl", "spin", "lowest"][i]
            audit["perturbations"].append({
                "criterion": crit_name,
                "sign": sign,
                "weights": w,
                "overlap_with_base_top5": overlap,
                "top1_unchanged": top1_same,
            })
    audit["base_weights"] = base_weights
    audit["base_top5_keys"] = [str(k) for k in base_keys]
    return audit


def _save_heatmap(eps_grid: np.ndarray, s_grid: np.ndarray,
                  results: list[PointResult], out_path: str) -> str | None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:
        print(f"[warn] matplotlib unavailable ({exc}); skipping heatmap.")
        return None
    scores = np.zeros((len(eps_grid), len(s_grid)))
    by_point = {(round(r.eps, 5), round(r.s, 8)): r for r in results}
    for i, e in enumerate(eps_grid):
        for j, s in enumerate(s_grid):
            r = by_point.get((round(float(e), 5), round(float(s), 8)))
            if r is None or r.best_scores is None:
                scores[i, j] = 0.0
            else:
                scores[i, j] = r.best_scores.composite
    fig, ax = plt.subplots(figsize=(7, 5))
    im = ax.pcolormesh(s_grid, eps_grid, scores, shading="auto", cmap="viridis")
    ax.set_xscale("log")
    ax.set_xlabel(r"$s_\nu$")
    ax.set_ylabel(r"$\varepsilon_\nu$")
    ax.set_title("R61 T2 best-triplet composite score across (ε_ν, s_ν)")
    fig.colorbar(im, ax=ax, label="composite score")
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return out_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("R61 Track 2 — ν-sheet candidate ranking")
    print("=" * 60)
    print()

    # -- Smoke tests --
    print("Smoke tests:")
    print("-" * 60)
    results = smoke_tests()
    all_pass = True
    for name, ok, detail in results:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")
        print(f"         {detail}")
        all_pass = all_pass and ok
    print()

    # -- Reference sweep --
    # Tolerance 2.7% = R49's experimental 1σ on 33.6 ± 0.9.
    # Dense log-spaced s grid + Family A's known s=0.022 inserted explicitly
    # so the sweep is robust to grid discretization.
    print("Reference sweep (ε_ν ∈ [2, 10], s_ν ∈ [0.005, 0.1]):")
    print("-" * 60)
    eps_grid = np.linspace(2.0, 10.0, 17)
    base_s = np.geomspace(0.005, 0.1, 41).tolist()
    s_grid = np.array(sorted(set(base_s + [0.022])))
    point_results = rank_candidates(
        eps_grid=eps_grid,
        s_grid=s_grid,
        delta=0.1,
        tol=0.027,
        target=33.6,
        nt_max=3,
        nr_max=6,
    )
    any_triplets = [r for r in point_results if r.best_scores is not None]
    if any_triplets:
        print(f"  {len(any_triplets)} / {len(point_results)} (ε, s) points have at least one triplet")
        scores_arr = np.array([r.best_scores.composite for r in any_triplets])
        print(f"  composite score: min={scores_arr.min():.3f}, max={scores_arr.max():.3f}, mean={scores_arr.mean():.3f}")

    # -- Shortlist --
    top_n = 10
    shortlist = _deduplicate_by_modeset(point_results, top_n)
    print()
    print(f"Top-{top_n} unique candidates (by mode-set):")
    print(f"  {'rank':<5}{'ε_ν':<8}{'s_ν':<10}{'composite':<11}triplet")
    for i, r in enumerate(shortlist, start=1):
        t = r.best
        trip = f"({t.a.n_tube:+d},{t.a.n_ring:+d}) ({t.b.n_tube:+d},{t.b.n_ring:+d}) ({t.c.n_tube:+d},{t.c.n_ring:+d})"
        print(f"  {i:<5}{r.eps:<8.3f}{r.s:<10.5f}{r.best_scores.composite:<11.3f}{trip}")
    print()

    # -- Write outputs --
    os.makedirs(OUT_DIR, exist_ok=True)
    shortlist_path = os.path.join(OUT_DIR, "track2_shortlist.md")
    write_shortlist_md(shortlist, shortlist_path)
    print(f"  shortlist saved:  {shortlist_path}")

    top_dir = os.path.join(OUT_DIR, "track2_top_candidates")
    os.makedirs(top_dir, exist_ok=True)
    for i, r in enumerate(shortlist[:5], start=1):
        cand_path = os.path.join(top_dir, f"candidate_{i:02d}.md")
        write_candidate_detail(r, cand_path)
    print(f"  top-5 details:    {top_dir}/")

    heatmap_path = _save_heatmap(
        eps_grid, s_grid, point_results,
        os.path.join(OUT_DIR, "track2_score_heatmap.png"),
    )
    if heatmap_path:
        print(f"  heatmap saved:    {heatmap_path}")

    # -- Weight sensitivity --
    print()
    print("Weight sensitivity audit (±50% perturbation, top-5 mode-set overlap):")
    print("-" * 60)
    audit = weight_sensitivity_audit(
        eps_grid, s_grid,
        perturbation=0.5, top_n=5,
        delta=0.1, tol=0.027, target=33.6, nt_max=3, nr_max=6,
    )
    for p in audit["perturbations"]:
        sign = "+" if p["sign"] > 0 else "−"
        stable = "✓" if p["top1_unchanged"] else "×"
        print(f"  [{stable}] weight {p['criterion']:<8}{sign}50%: "
              f"top-5 overlap = {p['overlap_with_base_top5']}/5; "
              f"top-1 unchanged = {p['top1_unchanged']}")

    print()
    print("=" * 60)
    print(f"Smoke tests: {'ALL PASS' if all_pass else 'FAILURES PRESENT'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
