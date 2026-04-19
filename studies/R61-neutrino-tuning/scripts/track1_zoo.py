"""R61 Track 1 — Zoo enumerator, pair filter, triplet finder, Δm² comb.

Self-contained toolkit for the neutrino-sheet paired-mode zoo analysis.
Five primitives + four smoke tests + a reference zoo-density sweep.

Run as:
    python track1_zoo.py

No dependencies beyond numpy + matplotlib (matplotlib optional; falls
back to text output if unavailable).
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from typing import Iterable

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "outputs")


@dataclass(frozen=True)
class Mode:
    n_r: int
    n_t: int
    mu2: float

    def __repr__(self) -> str:
        return f"({self.n_r:+d},{self.n_t:+d}):µ²={self.mu2:.4f}"


# ---------------------------------------------------------------------------
# Primitive 1 — mass formula and mode enumeration
# ---------------------------------------------------------------------------

def mu2(n_r: int, n_t: int, eps: float, s: float) -> float:
    """µ² = (n_r·ε)² + (n_t − n_r·s)² on a 2-torus with aspect ε and shear s."""
    return (n_r * eps) ** 2 + (n_t - n_r * s) ** 2


def enumerate_modes(eps: float, s: float, nr_max: int, nt_max: int) -> list[Mode]:
    """Return all integer modes (|n_r|≤nr_max, 0≤n_t≤nt_max), excluding (0,0)."""
    modes: list[Mode] = []
    for n_r in range(-nr_max, nr_max + 1):
        for n_t in range(0, nt_max + 1):
            if n_r == 0 and n_t == 0:
                continue
            modes.append(Mode(n_r, n_t, mu2(n_r, n_t, eps, s)))
    modes.sort(key=lambda m: m.mu2)
    return modes


# ---------------------------------------------------------------------------
# Primitive 2 — pair filter
# ---------------------------------------------------------------------------

def paired_fermion_modes(
    modes: Iterable[Mode], eps: float, s: float, delta: float
) -> list[Mode]:
    """Keep fermion candidates (|n_r|≥1) whose ±n_r partner exists at
    splitting/mean_µ² ≤ delta.  Excludes all n_r=0 modes (spin 1)."""
    keep: list[Mode] = []
    for m in modes:
        if abs(m.n_r) < 1:
            continue
        partner_mu2 = mu2(-m.n_r, m.n_t, eps, s)
        mean = 0.5 * (m.mu2 + partner_mu2)
        if mean <= 0:
            continue
        rel_split = abs(m.mu2 - partner_mu2) / mean
        if rel_split <= delta:
            keep.append(m)
    keep.sort(key=lambda m: m.mu2)
    return keep


# ---------------------------------------------------------------------------
# Primitive 3 — triplet finder
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Triplet:
    a: Mode
    b: Mode
    c: Mode
    ratio: float


def find_ratio_triplets(
    modes: list[Mode], target: float, tol: float
) -> list[Triplet]:
    """All (a,b,c) with µ_a²<µ_b²<µ_c² and (µ_c²−µ_a²)/(µ_b²−µ_a²) ≈ target."""
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


# ---------------------------------------------------------------------------
# Primitive 4 — Δm² comb predictor
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CombEntry:
    nt_from: int
    nt_to: int
    dm2_mean: float    # in eV² (once E₀² is applied)
    dm2_spread: float  # max−min over sampled n_r values, in eV²
    dmu2_mean: float   # dimensionless µ² mean
    dmu2_spread: float


def delta_m2_comb(
    eps: float, s: float, E0_sq_eV2: float, max_dn: int = 5, nr_sample: int = 3
) -> list[CombEntry]:
    """Predict Δm² clusters from integer n_tube transitions.

    For each (a, b) with 1 ≤ a < b ≤ max_dn, sample Δµ² over
    |n_r| ≤ nr_sample and return mean and spread.  Clusters sit at
    positions fixed by integer structure once (eps, s, E0_sq) are set.
    """
    entries: list[CombEntry] = []
    for a in range(1, max_dn):
        for b in range(a + 1, max_dn + 1):
            samples = []
            for n_r in range(-nr_sample, nr_sample + 1):
                # Skip n_r = 0 only if it gives a degenerate/trivial result.
                samples.append(
                    mu2(n_r, b, eps, s) - mu2(n_r, a, eps, s)
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
# Primitive 5 — zoo-density sweep
# ---------------------------------------------------------------------------

def zoo_sweep(
    eps_grid: np.ndarray,
    s_grid: np.ndarray,
    delta: float,
    tol: float,
    ratio_target: float,
    nr_max: int = 3,
    nt_max: int = 6,
) -> np.ndarray:
    """Count 33.6-matching triplets of paired fermion modes at each (ε, s).

    Returns a 2D array indexed [i_eps, j_s] of triplet counts.
    """
    counts = np.zeros((len(eps_grid), len(s_grid)), dtype=int)
    for i, eps in enumerate(eps_grid):
        for j, s in enumerate(s_grid):
            modes = enumerate_modes(eps, s, nr_max, nt_max)
            paired = paired_fermion_modes(modes, eps, s, delta)
            triplets = find_ratio_triplets(paired, ratio_target, tol)
            counts[i, j] = len(triplets)
    return counts


# ---------------------------------------------------------------------------
# Smoke tests T1–T4
# ---------------------------------------------------------------------------

def _approx(a: float, b: float, tol: float) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(b))


def smoke_tests() -> list[tuple[str, bool, str]]:
    results: list[tuple[str, bool, str]] = []

    # -- T1 ---------------------------------------------------------------
    modes = enumerate_modes(5.0, 0.022, 3, 5)
    lookup = {(m.n_r, m.n_t): m.mu2 for m in modes}
    expected = {(1, 1): 25.956484, (-1, 1): 26.044484, (1, 2): 28.912484}
    deviations = [abs(lookup[(nr, nt)] - v) for (nr, nt), v in expected.items()]
    ok = all(d < 1e-6 for d in deviations)
    detail = f"max |Δµ²| = {max(deviations):.2e} vs expected tol 1e-6"
    results.append(("T1 enumerate_modes reproduces Family A µ²", ok, detail))

    # -- T2 ---------------------------------------------------------------
    paired = paired_fermion_modes(modes, 5.0, 0.022, delta=0.1)
    paired_set = {(m.n_r, m.n_t) for m in paired}
    required = {(1, 1), (-1, 1), (1, 2), (-1, 2), (2, 1), (-2, 1)}
    absent_nr0 = all((0, nt) not in paired_set for nt in range(0, 6))
    has_required = required.issubset(paired_set)
    ok = absent_nr0 and has_required
    missing = required - paired_set
    detail = (
        f"nr=0 excluded: {absent_nr0}; "
        f"required subset present: {has_required}"
        + (f"; missing: {missing}" if missing else "")
    )
    results.append(("T2 paired_fermion_modes filters correctly", ok, detail))

    # -- T3 ---------------------------------------------------------------
    triplets = find_ratio_triplets(paired, target=33.6, tol=0.01)
    family_a = any(
        (t.a.n_r, t.a.n_t) == (1, 1)
        and (t.b.n_r, t.b.n_t) == (-1, 1)
        and (t.c.n_r, t.c.n_t) == (1, 2)
        for t in triplets
    )
    count_ok = len(triplets) >= 11
    ok = family_a and count_ok
    detail = f"triplets found = {len(triplets)}, Family A present = {family_a}"
    results.append(("T3 find_ratio_triplets reproduces Family A + zoo", ok, detail))

    # -- T4 ---------------------------------------------------------------
    # Calibrate E₀² so the (1→2) cluster mean sits at atmospheric Δm²
    # (2.53e-3 eV²).  Mean Δµ² over n_r∈[-3,3] for (1,2)−(1,1) transitions.
    # At s=0.022 this mean is ≈ 3.0 (since +s and −s shifts cancel across
    # symmetric n_r sampling), so E₀² ≈ 2.53e-3 / 3.
    # Use the real computed mean instead of 3 to avoid hard-coding.
    comb_dummy = delta_m2_comb(5.0, 0.022, E0_sq_eV2=1.0, max_dn=5, nr_sample=3)
    dmu2_1to2 = next(e.dmu2_mean for e in comb_dummy if (e.nt_from, e.nt_to) == (1, 2))
    E0_sq = 2.53e-3 / dmu2_1to2
    comb = delta_m2_comb(5.0, 0.022, E0_sq_eV2=E0_sq, max_dn=5, nr_sample=3)
    c12 = next(e for e in comb if (e.nt_from, e.nt_to) == (1, 2))
    c13 = next(e for e in comb if (e.nt_from, e.nt_to) == (1, 3))
    t4_a = _approx(c12.dm2_mean, 2.53e-3, tol=1e-4)
    t4_b = _approx(c13.dm2_mean, 6.77e-3, tol=0.01)  # 1%
    ok = t4_a and t4_b
    detail = (
        f"1→2: {c12.dm2_mean:.3e} eV² (target 2.53e-3); "
        f"1→3: {c13.dm2_mean:.3e} eV² (target 6.77e-3)"
    )
    results.append(("T4 delta_m2_comb produces expected clusters", ok, detail))

    return results


# ---------------------------------------------------------------------------
# Reference zoo-density sweep + heatmap
# ---------------------------------------------------------------------------

def reference_sweep() -> tuple[np.ndarray, np.ndarray, np.ndarray, list[tuple[float, float, int]]]:
    eps_grid = np.linspace(1.0, 10.0, 19)     # 0.5 steps
    s_grid   = np.geomspace(0.005, 0.1, 21)    # log-spaced around 0.022
    counts = zoo_sweep(
        eps_grid=eps_grid,
        s_grid=s_grid,
        delta=0.1,
        tol=0.01,
        ratio_target=33.6,
        nr_max=3,
        nt_max=6,
    )

    # Top-10 densest (eps, s) points
    flat = [
        (float(eps_grid[i]), float(s_grid[j]), int(counts[i, j]))
        for i in range(counts.shape[0])
        for j in range(counts.shape[1])
    ]
    flat.sort(key=lambda t: -t[2])
    top10 = flat[:10]

    return eps_grid, s_grid, counts, top10


def _save_heatmap(eps_grid: np.ndarray, s_grid: np.ndarray, counts: np.ndarray) -> str | None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:  # pragma: no cover
        print(f"[warn] matplotlib unavailable ({exc}); skipping heatmap.")
        return None

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "track1_zoo_density.png")
    fig, ax = plt.subplots(figsize=(7, 5))
    # Display with s on x-axis (log), eps on y-axis
    im = ax.pcolormesh(
        s_grid, eps_grid, counts,
        shading="auto", cmap="viridis",
    )
    ax.set_xscale("log")
    ax.set_xlabel(r"$s_\nu$")
    ax.set_ylabel(r"$\varepsilon_\nu$")
    ax.set_title("R61 T1 zoo density — 33.6-ratio paired triplets per (ε, s)")
    fig.colorbar(im, ax=ax, label="triplet count")
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    return out_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("R61 Track 1 — neutrino-sheet zoo enumerator")
    print("=" * 60)
    print()

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

    print("Reference zoo sweep (eps ∈ [1, 10], s ∈ [0.005, 0.1]):")
    print("-" * 60)
    eps_grid, s_grid, counts, top10 = reference_sweep()
    print(f"  grid shape: {counts.shape}  (eps × s)")
    print(f"  counts: min={counts.min()}, max={counts.max()}, "
          f"mean={counts.mean():.1f}")
    print()
    print("  Top-10 densest (ε, s) points:")
    print(f"    {'rank':<6}{'ε_ν':<10}{'s_ν':<14}{'triplet count':<14}")
    for rank, (eps, s, n) in enumerate(top10, start=1):
        print(f"    {rank:<6}{eps:<10.3f}{s:<14.5f}{n:<14}")
    print()

    heatmap_path = _save_heatmap(eps_grid, s_grid, counts)
    if heatmap_path:
        print(f"  heatmap saved: {heatmap_path}")

    # Also dump a compact table for findings.md
    os.makedirs(OUT_DIR, exist_ok=True)
    table_path = os.path.join(OUT_DIR, "track1_zoo_counts.txt")
    with open(table_path, "w") as f:
        f.write("# R61 Track 1 zoo-density sweep\n")
        f.write("# columns: eps_nu, s_nu, triplet_count (33.6 ratio, paired fermion modes)\n")
        for i in range(counts.shape[0]):
            for j in range(counts.shape[1]):
                f.write(f"{eps_grid[i]:.4f}\t{s_grid[j]:.6f}\t{counts[i,j]}\n")
    print(f"  table saved:   {table_path}")

    # Diagnostic: Family A sweet spot
    # ε=5.0, s≈0.022 should appear among the denser points
    target_eps, target_s = 5.0, 0.022
    i_eps = int(np.argmin(np.abs(eps_grid - target_eps)))
    j_s = int(np.argmin(np.abs(s_grid - target_s)))
    family_a_count = int(counts[i_eps, j_s])
    print(f"  Family A neighborhood (ε≈{eps_grid[i_eps]:.2f}, "
          f"s≈{s_grid[j_s]:.4f}): {family_a_count} triplets")

    print()
    print("=" * 60)
    print(f"Smoke tests: {'ALL PASS' if all_pass else 'FAILURES PRESENT'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
