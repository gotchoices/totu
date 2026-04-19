"""
R60 Track 7d: Magic-shear baseline re-solve.

Replace Track 7b's shearless (ε=1, s=0) baseline on e and p
sheets with magic-shear values that make each sheet's target
mode the LIGHTEST charged mode on that sheet.

Magic shear: s = n_r / n_t for the target mode
  e-sheet: target (1, 2) → s_e = 2
  p-sheet: target (1, 3) → s_p = 3
  ν-sheet: keep R61 #1 values (s_ν = 0.022)

Proposed (ε, s) values keeping sε within joint signature budget:
  e: (0.4, 2.0) → sε = 0.8
  p: (0.4, 3.0) → sε = 1.2
  ν: (2.0, 0.022) → sε = 0.044
  Sum of squares: 2.08 < 5/2 predicted three-tube bound.

Re-solve same six free knobs (L_x, k_x per sheet) against same
six targets (three masses + α_e = α_p = α_ν₁ = α), using the
ring↔ℵ structural augmentation.

Cross-check beyond targets:
  - Ghost ordering: on each sheet, target mode should be lightest
  - α universality: α_ν₂ and α_ν₃ should equal α (Track 7 fix)
  - Decoupling locus avoided (done at framing time)
  - Signature OK
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok, num_negative_eigs,
    alpha_coulomb, mode_6_to_11, derive_L_ring,
    L_vector_from_params, mode_energy, solve, Target,
    ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI, M_E_MEV, M_P_MEV,
    I_ALEPH, I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING,
    I_NU_TUBE, I_NU_RING, I_T, mu_sheet,
)
from track4_diagonal_compensation import K_NATURAL
from track7b_resolve import (
    add_ring_aleph, build_aug_metric, solve_joint_aug,
    n_e, n_p, n_nu1, n_nu2, n_nu3,
)


def report_ghost_ordering(eps, s, label, n_t=1, max_nr=5):
    """Print single-sheet mode energies to show ghost ordering."""
    print(f"  {label} sheet (ε={eps}, s={s}):")
    print(f"    {'mode':>8s}  {'μ':>8s}  {'note':<s}")
    modes = [(n_t, n_r) for n_r in range(0, max_nr + 1)]
    mus = []
    for n_r in range(0, max_nr + 1):
        mu = mu_sheet(n_t, n_r, eps, s)
        mus.append((n_r, mu))
    mus.sort(key=lambda x: x[1])
    lightest = mus[0][0]
    for n_r, mu in sorted(mus, key=lambda x: x[0]):
        tag = "← LIGHTEST" if n_r == lightest else ""
        print(f"    ({n_t},{n_r:>2d})  {mu:>8.4f}  {tag}")
    return lightest


def main():
    # Magic-shear baseline
    eps_e, s_e = 0.4, 2.0
    eps_p, s_p = 0.4, 3.0
    eps_nu, s_nu = 2.0, 0.022
    m_nu1_MeV = 32.1e-9

    print("=" * 72)
    print("R60 Track 7d — Magic-shear baseline re-solve")
    print("=" * 72)
    print(f"  Architecture: tube↔ℵ + structural ring↔ℵ (σ_ra = sε·σ_ta) + ℵ↔t")
    print(f"  Sheet inputs:")
    print(f"    e: (ε={eps_e}, s={s_e}) magic shear for (1,2), sε={eps_e*s_e}")
    print(f"    p: (ε={eps_p}, s={s_p}) magic shear for (1,3), sε={eps_p*s_p}")
    print(f"    ν: (ε={eps_nu}, s={s_nu}) R61 #1, sε={eps_nu*s_nu}")
    print(f"  Joint signature budget: Σ(sε)² = {(eps_e*s_e)**2+(eps_p*s_p)**2+(eps_nu*s_nu)**2:.4f} < 2.5 (3-tube bound)")
    print()

    # ── Pre-solve ghost ordering (on bare single-sheet μ) ──
    print("─" * 72)
    print("Pre-solve ghost ordering (single-sheet μ values)")
    print("─" * 72)
    e_lightest = report_ghost_ordering(eps_e, s_e, "e")
    p_lightest = report_ghost_ordering(eps_p, s_p, "p")
    nu_lightest = report_ghost_ordering(eps_nu, s_nu, "ν")
    print()
    print(f"  e-sheet lightest (n_r): {e_lightest}  (target: 2 for electron)")
    print(f"  p-sheet lightest (n_r): {p_lightest}  (target: 3 for proton)")
    print(f"  ν-sheet lightest (n_r): {nu_lightest}  (target: 1 for ν₁)")
    print()

    # ── Joint solve ──
    print("─" * 72)
    print("Joint solve (6 knobs, 6 targets, ring↔ℵ augmented metric)")
    print("─" * 72)
    rj = solve_joint_aug(eps_e, s_e, eps_p, s_p, eps_nu, s_nu, m_nu1_MeV)
    print(f"  converged = {rj.success}")
    print(f"  message   = {rj.message[:60]}")
    print(f"  cost      = {rj.cost:.4e}")
    print()
    print(f"  k_e       = {rj.params.k_e:.6e}  "
          f"({rj.params.k_e/K_NATURAL:.4f}× R59 F59)")
    print(f"  k_p       = {rj.params.k_p:.6e}  "
          f"({rj.params.k_p/K_NATURAL:.4f}× R59 F59)")
    print(f"  k_ν       = {rj.params.k_nu:.6e}  "
          f"({rj.params.k_nu/K_NATURAL:.4f}× R59 F59)")
    print(f"  L_ring_e  = {rj.params.L_ring_e:.4e} fm")
    print(f"  L_ring_p  = {rj.params.L_ring_p:.4e} fm")
    print(f"  L_ring_ν  = {rj.params.L_ring_nu:.4e} fm")
    print()
    sigma_ra_e  = (rj.params.eps_e  * rj.params.s_e)  * rj.params.sign_e  * rj.params.sigma_ta
    sigma_ra_p  = (rj.params.eps_p  * rj.params.s_p)  * rj.params.sign_p  * rj.params.sigma_ta
    sigma_ra_nu = (rj.params.eps_nu * rj.params.s_nu) * rj.params.sign_nu * rj.params.sigma_ta
    print(f"  σ_ra_e (derived) = {sigma_ra_e:+.6e}")
    print(f"  σ_ra_p (derived) = {sigma_ra_p:+.6e}")
    print(f"  σ_ra_ν (derived) = {sigma_ra_nu:+.6e}")
    print()
    print(f"  residuals = {rj.residuals}")
    print()

    G = build_aug_metric(rj.params)
    sig = signature_ok(G)
    print(f"  signature_ok = {sig}, neg eigs = {num_negative_eigs(G)}")
    if not sig:
        print("  WARNING: signature broken; halting further analysis.")
        return

    L = L_vector_from_params(rj.params)

    # ── Target verification ──
    print()
    print("─" * 72)
    print("Target verification")
    print("─" * 72)
    E_e   = mode_energy(G, L, n_e())
    E_p   = mode_energy(G, L, n_p())
    E_nu1 = mode_energy(G, L, n_nu1())
    a_e   = alpha_coulomb(G, n_e())   / ALPHA
    a_p   = alpha_coulomb(G, n_p())   / ALPHA
    a_nu1 = alpha_coulomb(G, n_nu1()) / ALPHA
    print(f"  E_e   = {E_e:.10f} MeV (target {M_E_MEV})")
    print(f"  E_p   = {E_p:.6f} MeV (target {M_P_MEV})")
    print(f"  E_ν₁  = {E_nu1*1e9:.6f} meV (target 32.1)")
    print(f"  α_e/α  = {a_e:.10f}")
    print(f"  α_p/α  = {a_p:.10f}")
    print(f"  α_ν₁/α = {a_nu1:.10f}")

    # ── Universality cross-check ──
    print()
    print("─" * 72)
    print("Universality cross-check (untargeted ν₂, ν₃ should = α)")
    print("─" * 72)
    a_nu2 = alpha_coulomb(G, n_nu2()) / ALPHA
    a_nu3 = alpha_coulomb(G, n_nu3()) / ALPHA
    E_nu2 = mode_energy(G, L, n_nu2())
    E_nu3 = mode_energy(G, L, n_nu3())
    print(f"  α_ν₂/α = {a_nu2:.10f}  (R61 mode (-1, +1))")
    print(f"  α_ν₃/α = {a_nu3:.10f}  (R61 mode (+1, +2))")
    print(f"  E_ν₂  = {E_nu2*1e9:.6f} meV")
    print(f"  E_ν₃  = {E_nu3*1e9:.6f} meV")
    spread = max(abs(a_nu1-a_nu2), abs(a_nu1-a_nu3), abs(a_nu2-a_nu3))
    print(f"  ν-mode spread = {spread:.2e}")
    if spread < 1e-6:
        print(f"    → universality preserved under magic-shear baseline ✓")
    else:
        print(f"    → spread nonzero — investigate")
    dm2_21 = E_nu2**2 - E_nu1**2
    dm2_31 = E_nu3**2 - E_nu1**2
    if dm2_21 > 0:
        print(f"  Δm²₃₁/Δm²₂₁ = {dm2_31/dm2_21:.4f}  (R49 target: 33.6)")
    print()

    # ── Ghost ordering AT THE CONVERGED POINT (with joint metric) ──
    print("─" * 72)
    print("Ghost ordering at converged point (full-metric mode energies)")
    print("─" * 72)
    # Compute actual E for (1, n_r) on each sheet at final L, k
    def compute_ghost_E(sheet, max_nr=5):
        """Return list of (n_r, E_MeV) for charged single-sheet modes."""
        results = []
        for n_r in range(0, max_nr + 1):
            if sheet == "e":
                n6 = (1, n_r, 0, 0, 0, 0)
            elif sheet == "p":
                n6 = (0, 0, 0, 0, 1, n_r)
            elif sheet == "ν":
                n6 = (0, 0, 1, n_r, 0, 0)
            n11 = mode_6_to_11(n6)
            E = mode_energy(G, L, n11)
            results.append((n_r, E))
        return results

    for sheet_name, target_nr, target_mass, units in [
        ("e", 2, M_E_MEV, "MeV"),
        ("p", 3, M_P_MEV, "MeV"),
        ("ν", 1, 32.1e-9, "meV"),
    ]:
        print(f"\n  {sheet_name}-sheet (target mode n_r = {target_nr}):")
        results = compute_ghost_E(sheet_name)
        min_E = min(r[1] for r in results)
        lightest_nr = [nr for nr, E in results if E == min_E][0]
        ordered = "✓" if lightest_nr == target_nr else "✗"
        print(f"    {'n_r':>4s}  {'E':>16s}  {'ratio to target':>18s}")
        for n_r, E in results:
            ratio = E / target_mass
            if units == "meV":
                E_disp = f"{E*1e9:.4f} meV"
            else:
                E_disp = f"{E:.6f} {units}"
            marker = " ← target" if n_r == target_nr else (
                " ← LIGHTEST" if E == min_E else "")
            print(f"    ({n_r:>2d})  {E_disp:>16s}  {ratio:>18.6f}{marker}")
        print(f"    Ghost ordering {ordered}: lightest is n_r={lightest_nr}, target is n_r={target_nr}")

    print()
    print("=" * 72)
    print("Track 7d complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
