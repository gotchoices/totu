"""
R60 Track 5 Part 2: α-decoupling locus (analytical + numerical).

Derive in closed form when Q = 0 for a single-sheet mode (n_t, n_r),
then verify numerically against the Track 1 alpha_coulomb extractor.

DERIVATION (single sheet, e.g., e-sheet alone with sign_e = +1,
other sheets uncoupled).  The relevant 4×4 sub-metric (e_t, e_r,
ℵ, t) with shorthand u = s·ε:

       e_t       e_r           ℵ      t
  e_t [ k        k·u           σ      0 ]
  e_r [ k·u      k(1+u²)       0      0 ]
  ℵ   [ σ        0             g      τ ]
  t   [ 0        0             τ     -1 ]

where σ = √α (= sign × σ_ta), τ = 4πα (= σ_at), g = g_aa = 1.

The α extraction formula:
  Q = n_t · G⁻¹[e_t, t] + n_r · G⁻¹[e_r, t]
  α = Q² / (4π)

Computing G⁻¹[e_t, t] and G⁻¹[e_r, t] by cofactor expansion:
  G⁻¹[e_t, t] = +σ k τ (1 + u²) / det(G_4×4)
  G⁻¹[e_r, t] = −σ k u τ / det(G_4×4)

Substituting:
  Q = (σ k τ / det) · [n_t (1 + u²) − n_r · u]

Setting Q = 0 (and σ k τ ≠ 0, det ≠ 0):
  n_t (1 + u²) − n_r · u = 0
  n_r / n_t = u + 1/u
  i.e.   **n_r/n_t = sε + 1/(sε)**

Equivalently u = sε satisfies:  n_t · u² − n_r · u + n_t = 0
=> u = (n_r ± √(n_r² − 4 n_t²)) / (2 n_t)

Real solutions exist iff n_r² ≥ 4 n_t².  Charge-1 modes (1, n_r):
  - (1, 0):  no real u  (n_r² = 0 < 4)
  - (1, 1):  no real u  (1 < 4)
  - (1, 2):  u = 1                (single root, double)
  - (1, 3):  u = (3 ± √5)/2 ≈ 0.382 or 2.618
  - (1, n):  u = (n ± √(n²−4))/2

For n = 1 the (1,1) mode never decouples — useful for ν₁, ν₂.
For n = 2 the (1,2) mode decouples on the curve sε = 1.
For n ≥ 3 the mode has TWO decoupling curves.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok, alpha_coulomb,
    mode_6_to_11, ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI,
)


# ── Analytical locus ──────────────────────────────────────────────────

def decoupling_u(n_t: int, n_r: int):
    """Return the u = sε values where Q = 0 for mode (n_t, n_r).
    Empty list if no real root (mode never decouples)."""
    disc = n_r*n_r - 4*n_t*n_t
    if disc < 0:
        return []
    if disc == 0:
        return [n_r / (2 * n_t)]
    sqrt_d = math.sqrt(disc)
    return [(n_r - sqrt_d) / (2 * n_t),
            (n_r + sqrt_d) / (2 * n_t)]


# ── Numerical Q(s, ε) for verification ────────────────────────────────

def alpha_e_only(eps_e: float, s_e: float,
                  k_e: float = 1.0/EIGHT_PI,
                  n_e_t: int = 1, n_e_r: int = 2):
    """Compute α_Coulomb on e-sheet alone for given (ε_e, s_e), free k_e.

    Returns (α/α, Q).  Other sheets (p, ν) are uncoupled identity blocks.
    L_ring_e is set to 1 fm (irrelevant — Q does not depend on L)."""
    p = Params(
        eps_e=eps_e, s_e=s_e,
        eps_p=1.0, s_p=0.0,
        eps_nu=1.0, s_nu=0.0,
        k_e=k_e, k_p=1.0, k_nu=1.0,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=+1.0, sign_p=0.0, sign_nu=0.0,
        L_ring_e=1.0, L_ring_p=1.0, L_ring_nu=1.0,
    )
    G = build_metric_11(p)
    if not signature_ok(G):
        return float("nan"), float("nan")
    # Mode (n_e_t, n_e_r, 0, 0, 0, 0)
    n11 = mode_6_to_11((n_e_t, n_e_r, 0, 0, 0, 0))
    a = alpha_coulomb(G, n11)
    # Recover Q from α: Q² = 4π·α, Q = ±√(4π·α).  We just want |Q|/α
    return a / ALPHA, math.sqrt(4 * PI * a)


def smoke_locus_check():
    print("─" * 72)
    print("Smoke check: predicted decoupling u vs numerical α_e zero")
    print("─" * 72)
    test_modes = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 5), (1, 5)]
    for nt, nr in test_modes:
        roots = decoupling_u(nt, nr)
        print(f"  Mode ({nt}, {nr}): predicted u =", end="")
        if not roots:
            print(" (none — mode never decouples)")
        else:
            print(" " + ", ".join(f"{u:.6f}" for u in roots))


def verify_locus_numerical():
    print()
    print("─" * 72)
    print("Numerical verification: α_e/α along sε = 1 for (1, 2) mode")
    print("─" * 72)
    print(f"  Predicted decoupling at sε = 1.0")
    print(f"  {'ε':>6s}  {'s':>6s}  {'sε':>6s}  {'α_e/α':>12s}")
    test_points = [
        (0.5, 2.0),   # sε = 1.0, predicted Q = 0
        (1.0, 1.0),   # sε = 1.0, predicted Q = 0
        (2.0, 0.5),   # sε = 1.0, predicted Q = 0
        (0.5, 1.0),   # sε = 0.5, off-locus
        (1.0, 0.5),   # sε = 0.5, off-locus
        (1.0, 2.0),   # sε = 2.0, off-locus (signature might break)
    ]
    for eps, s in test_points:
        ratio, Q = alpha_e_only(eps, s)
        sε = s * eps
        if math.isnan(ratio):
            print(f"  {eps:>6.2f}  {s:>6.2f}  {sε:>6.2f}  (signature fails)")
        else:
            print(f"  {eps:>6.2f}  {s:>6.2f}  {sε:>6.2f}  {ratio:>12.6e}")
    print()
    print("─" * 72)
    print("Numerical verification: α_e/α along sε = 0.382 and 2.618 for (1, 3) mode")
    print("─" * 72)
    u1 = (3 - math.sqrt(5)) / 2
    u2 = (3 + math.sqrt(5)) / 2
    print(f"  Predicted decoupling at sε = {u1:.4f} and sε = {u2:.4f}")
    print(f"  {'ε':>6s}  {'s':>6s}  {'sε':>6s}  {'α_e/α (using mode (1,3))':>30s}")
    for eps, s in [
        (0.5, u1/0.5),   # sε = u1
        (1.0, u1),       # sε = u1
        (2.0, u1/2.0),   # sε = u1
        (0.5, u2/0.5),   # sε = u2 (likely sig break)
        (1.0, u2),       # sε = u2
        (0.5, 1.0),      # off-locus
    ]:
        ratio, Q = alpha_e_only(eps, s, n_e_t=1, n_e_r=3)
        sε = s * eps
        if math.isnan(ratio):
            print(f"  {eps:>6.2f}  {s:>6.2f}  {sε:>6.2f}  (signature fails)")
        else:
            print(f"  {eps:>6.2f}  {s:>6.2f}  {sε:>6.2f}  {ratio:>30.6e}")
    print()
    print("─" * 72)
    print("Numerical verification: (1, 1) mode — should NEVER decouple")
    print("─" * 72)
    print(f"  Predicted: no real u solves Q = 0 (n_r² < 4 n_t²)")
    print(f"  {'ε':>6s}  {'s':>6s}  {'sε':>6s}  {'α_e/α (using mode (1,1))':>30s}")
    for eps, s in [(0.5, 1.0), (1.0, 1.0), (1.0, 1.5), (0.1, 1.5), (1.0, 0.5)]:
        ratio, Q = alpha_e_only(eps, s, n_e_t=1, n_e_r=1)
        sε = s * eps
        if math.isnan(ratio):
            print(f"  {eps:>6.2f}  {s:>6.2f}  {sε:>6.2f}  (signature fails)")
        else:
            print(f"  {eps:>6.2f}  {s:>6.2f}  {sε:>6.2f}  {ratio:>30.6e}")
    print()


# ── Mode summary table ────────────────────────────────────────────────

def mode_summary():
    print("=" * 72)
    print("Decoupling loci for low-charge modes (formula: sε satisfies "
          "n_r/n_t = sε + 1/(sε))")
    print("=" * 72)
    print(f"  {'mode':>10s}  {'n_r²−4n_t²':>12s}  {'decoupling sε values'}")
    for nt in (1, 2, 3):
        for nr in range(0, 11):
            roots = decoupling_u(nt, nr)
            disc = nr*nr - 4*nt*nt
            roots_str = (
                ", ".join(f"{u:.4f}" for u in roots)
                if roots else "(none — never decouples)"
            )
            print(f"  ({nt:>2d}, {nr:>2d})  {disc:>12d}  {roots_str}")
    print()
    print("Key practical implications:")
    print("  • (1, 1) mode (used by ν₁, ν₂ in R49 Family A): NEVER decouples")
    print("    → ν-sheet at (1, 1) is α-safe at any (ε, s)")
    print("  • (1, 2) mode (electron, also ν₃ in R49 Family A): decouples at sε = 1")
    print("    → e-sheet must avoid sε = 1.0 exactly")
    print("    → ν-sheet using ν₃ also constrained (note for Track 6+)")
    print("  • (1, 3) mode (proton): decouples at sε ≈ 0.382 or 2.618")
    print("    → p-sheet must avoid these two specific products")
    print()


# ── Main ───────────────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("R60 Track 5 Part 2 — α-decoupling locus")
    print("=" * 72)
    print()
    print("Analytical result:")
    print("  For mode (n_t, n_r) on a single sheet at the R59 F59 architecture,")
    print("  α_Coulomb = 0 ⟺  n_r/n_t = (sε) + 1/(sε)")
    print("  ⟺  n_t · u² − n_r · u + n_t = 0  with u = sε")
    print("  ⟺  u = (n_r ± √(n_r² − 4 n_t²)) / (2 n_t)")
    print()
    print("  Real roots exist iff n_r² ≥ 4 n_t².")
    print()

    smoke_locus_check()
    verify_locus_numerical()
    mode_summary()

    print("=" * 72)
    print("Track 5 Part 2 complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
