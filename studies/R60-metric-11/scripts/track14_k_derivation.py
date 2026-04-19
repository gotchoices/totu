"""
R60 Track 14: Analytical derivation of k = 1.1803/(8π).

Phase 1: Empirical — is k a fixed point of the solver or an
         initial-point artifact?
Phase 2: Symbolic — solve for k at α_Coulomb = α using sympy.
Phase 3: Natural-form search — does k have a closed-form expression?
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import sympy as sp

from track1_solver import (
    Params, build_metric_11, signature_ok,
    alpha_coulomb, mode_6_to_11, derive_L_ring,
    L_vector_from_params, mode_energy, solve, Target,
    ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI, M_E_MEV, M_P_MEV,
)
from track4_diagonal_compensation import K_NATURAL
from track7b_resolve import (
    build_aug_metric, solve_joint_aug, n_e, n_p, n_nu1, n_nu2, n_nu3,
)


# ═════════════════════════════════════════════════════════════════════
#  Phase 1: Empirical
# ═════════════════════════════════════════════════════════════════════

def phase1_empirical():
    print("=" * 72)
    print("Phase 1 — Is k a fixed point of the solver?")
    print("=" * 72)
    print()
    print("  Sweep initial k across orders of magnitude, check what the")
    print("  solver converges to.  If always the same k, it's a fixed point.")
    print()

    # Model-F baseline geometry
    eps_e, s_e = 397.074, 2.004200
    eps_p, s_p = 0.55, 0.162037
    eps_nu, s_nu = 2.0, 0.022
    m_nu1_MeV = 32.1e-9

    test_k_inits = [
        K_NATURAL * 0.1,
        K_NATURAL * 0.5,
        K_NATURAL * 1.0,
        K_NATURAL * 2.0,
        K_NATURAL * 5.0,
        K_NATURAL * 10.0,
    ]

    print(f"  R59 F59 natural k = 1/(8π) = {K_NATURAL:.6e}")
    print()
    print(f"  {'k_init':>14s}  {'k_init/K_NAT':>14s}  {'k_final':>14s}  "
          f"{'k_final/K_NAT':>14s}  {'converged?'}")
    print(f"  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*12}")
    for k_init in test_k_inits:
        rj = solve_joint_aug(eps_e, s_e, eps_p, s_p, eps_nu, s_nu,
                              m_nu1_MeV, k_init=k_init)
        k_final = rj.params.k_e
        converged = rj.success and rj.cost < 1e-6
        print(f"  {k_init:>14.6e}  {k_init/K_NATURAL:>14.4f}  "
              f"{k_final:>14.6e}  {k_final/K_NATURAL:>14.4f}  "
              f"{'YES' if converged else 'no'}")
    print()


# ═════════════════════════════════════════════════════════════════════
#  Phase 2: Symbolic derivation
# ═════════════════════════════════════════════════════════════════════

def phase2_symbolic():
    print("=" * 72)
    print("Phase 2 — Symbolic derivation of k at α_Coulomb = α")
    print("=" * 72)
    print()

    # Symbols
    k, alpha_s, u = sp.symbols('k alpha u', positive=True, real=True)
    # We use alpha_s to avoid collision; it represents observed α (1/137).

    # R59 F59 natural forms (parameters derived from α)
    sigma_ta_sq = alpha_s            # σ_ta² = α
    sigma_at_sq = (4 * sp.pi * alpha_s) ** 2  # σ_at² = 16π²α²
    g_aa = 1
    sigma_ra_over_sigma_ta = u       # σ_ra = u · σ_ta (structural)

    print("  Setup:  σ_ta² = α,  σ_at² = 16π²α²,  g_aa = 1")
    print("          σ_ra  = u · σ_ta  (structural cancellation, Track 7)")
    print("          u = sε (shear · aspect ratio)")
    print()

    # 4×4 sub-metric for (tube, ring, ℵ, t):
    #   [[k,    k u,          σ_ta,   0 ],
    #    [k u,  k(1 + u²),   u σ_ta,  0 ],
    #    [σ_ta, u σ_ta,       g,      σ_at],
    #    [0,    0,            σ_at,  -1 ]]
    #
    # With σ_ra = u·σ_ta (symbolic)
    sigma_ta = sp.sqrt(alpha_s)
    sigma_at = 4 * sp.pi * alpha_s

    A = sp.Matrix([
        [k,       k*u,            sigma_ta,     0],
        [k*u,     k*(1 + u**2),   u*sigma_ta,   0],
        [sigma_ta, u*sigma_ta,    g_aa,         sigma_at],
        [0,       0,              sigma_at,     -1],
    ])

    print("  4×4 sub-metric A(k, u):")
    sp.pprint(A, use_unicode=True)
    print()

    det_A = sp.simplify(A.det())
    print(f"  det(A) = {det_A}")
    print()

    # Compute A⁻¹[t, t]
    Ainv = A.inv()
    Ainv_tt = sp.simplify(Ainv[3, 3])
    print(f"  A⁻¹[t, t] = {Ainv_tt}")
    print()

    # Compute Q for mode (n_t = 1, n_r = 0) on this single sheet
    #   Q = (n_t · A⁻¹[tube, t] + n_r · A⁻¹[ring, t]) · (−A⁻¹[t, t])
    # For unit-tube charge-carrying mode (n_t = 1), with σ_ra structural,
    # the ring contribution cancels the leakage — Q = σ_ta · (−A⁻¹[t, t]) · F(k, u)
    # Let's derive F(k, u) by computing the full thing.

    # For (n_t, n_r) = (1, 0): Q = A⁻¹[tube, t] · (−A⁻¹[t, t])
    #   (no ring contribution for n_r = 0)
    Ainv_tube_t = sp.simplify(Ainv[0, 3])
    print(f"  A⁻¹[tube, t] = {Ainv_tube_t}")
    print()

    # For (1, 0) mode: Q = Ainv_tube_t · (−Ainv_tt)
    # Actually for general mode (n_t, n_r), we sum both contributions.
    # With σ_ra structural prescription, the sum simplifies.

    # Let's compute Q_general(n_t, n_r):
    n_t, n_r = sp.symbols('n_t n_r', integer=True)
    Ainv_ring_t = sp.simplify(Ainv[1, 3])
    print(f"  A⁻¹[ring, t] = {Ainv_ring_t}")
    print()

    Q_general = (n_t * Ainv_tube_t + n_r * Ainv_ring_t) * (-Ainv_tt)
    Q_general = sp.simplify(Q_general)
    print(f"  Q_general(n_t, n_r) = {Q_general}")
    print()

    # For the electron mode (1, 2):
    Q_electron = sp.simplify(Q_general.subs([(n_t, 1), (n_r, 2)]))
    print(f"  Q_electron (n_t=1, n_r=2) = {Q_electron}")
    print()

    # α_Coulomb = Q² / (4π)
    alpha_coulomb_expr = sp.simplify(Q_electron**2 / (4 * sp.pi))
    print(f"  α_Coulomb(electron) = {alpha_coulomb_expr}")
    print()

    # Set α_Coulomb = α and solve for k:
    equation = sp.Eq(alpha_coulomb_expr, alpha_s)
    print(f"  Equation: α_Coulomb = α  →")
    sp.pprint(equation, use_unicode=True)
    print()

    # Substitute numeric α to solve
    alpha_val = 1 / 137.036
    # Also substitute u = model-F's e-sheet u = 2.004200 × 397.074 = 795.816
    u_val = 2.004200 * 397.074
    eq_numeric = equation.subs([(alpha_s, alpha_val), (u, u_val)])
    print(f"  Numeric substitution (α = 1/137.036, u = sε_e ≈ {u_val:.2f}):")
    print(f"    equation: {eq_numeric}")
    print()

    try:
        solutions = sp.solve(eq_numeric, k)
        print(f"  Solutions for k: {solutions}")
        print()
        for sol in solutions:
            sol_num = float(sol)
            print(f"    k = {sol_num:.6e}  = {sol_num/K_NATURAL:.6f} × 1/(8π)")
    except Exception as e:
        print(f"  sympy.solve failed: {e}")
        print("  Trying nsolve with initial guess k = 0.047:")
        try:
            sol = sp.nsolve(eq_numeric.lhs - eq_numeric.rhs, k, 0.047)
            sol_num = float(sol)
            print(f"    k = {sol_num:.6e}  = {sol_num/K_NATURAL:.6f} × 1/(8π)")
        except Exception as e2:
            print(f"    nsolve failed: {e2}")
    print()

    # Also solve for mode-independent case (u = 0, shearless)
    eq_shearless = equation.subs([(alpha_s, alpha_val), (u, 0)])
    print(f"  Shearless limit (u = 0):")
    print(f"    equation: {eq_shearless}")
    try:
        sols = sp.solve(eq_shearless, k)
        print(f"    Solutions for k: {sols}")
        for sol in sols:
            try:
                sol_num = float(sol)
                print(f"      k = {sol_num:.6e}  = {sol_num/K_NATURAL:.6f} × 1/(8π)")
            except:
                print(f"      k = {sol}")
    except Exception as e:
        print(f"    sympy.solve failed: {e}")
        try:
            sol = sp.nsolve(eq_shearless.lhs - eq_shearless.rhs, k, 0.04)
            print(f"    k ≈ {float(sol):.6e}  = {float(sol)/K_NATURAL:.6f} × 1/(8π)")
        except Exception as e2:
            print(f"    nsolve failed: {e2}")
    print()


# ═════════════════════════════════════════════════════════════════════
#  Phase 3: Natural-form search
# ═════════════════════════════════════════════════════════════════════

def phase3_natural_form():
    print("=" * 72)
    print("Phase 3 — Search for natural-form expression of k")
    print("=" * 72)
    print()

    # Empirical k from solver at model-F baseline
    k_empirical = 4.696442e-02
    k_ratio = k_empirical * EIGHT_PI  # = 1.18030... if k = 1.1803/(8π)
    print(f"  k (solver) = {k_empirical:.10e}")
    print(f"  k × 8π     = {k_ratio:.10f}")
    print(f"  k × 8π × 2 = {k_ratio * 2:.10f}  (= 2.360608)")
    print(f"  k × 8π / α = {k_ratio / ALPHA:.4f}  (= 161.7)")
    print(f"  k × 8π × α = {k_ratio * ALPHA:.6e}")
    print()

    # Candidate natural forms for the k × 8π factor (= 1.1803...)
    candidates = {
        "1": 1,
        "1 + α": 1 + ALPHA,
        "1 + 16π²α²": 1 + 16 * PI**2 * ALPHA**2,
        "1 + 4πα": 1 + 4 * PI * ALPHA,
        "(1 + 4πα)²": (1 + 4 * PI * ALPHA) ** 2,
        "1 + 4πα + 16π²α²": 1 + 4*PI*ALPHA + 16*PI**2*ALPHA**2,
        "√(1 + 4πα)": math.sqrt(1 + 4*PI*ALPHA),
        "1/cos(4πα)": 1 / math.cos(4*PI*ALPHA) if abs(4*PI*ALPHA) < 1.5 else math.nan,
        "(2π+1)/(2π)": (2*PI + 1) / (2*PI),
        "e^(2α)": math.exp(2 * ALPHA),
        "1 + 2α·π": 1 + 2 * ALPHA * PI,
        "(1−α)⁻¹": 1 / (1 - ALPHA),
        "(1 + α)² / (1 − α)": (1 + ALPHA)**2 / (1 - ALPHA),
        "√(4π/(3α·π²))": math.sqrt(4*PI / (3 * ALPHA * PI**2)) if False else math.nan,
        "(8π α + 1) / (8π α)": (8*PI*ALPHA + 1) / (8*PI*ALPHA),
    }

    print(f"  Target: k × 8π = {k_ratio:.10f}")
    print(f"  {'candidate':<30s}  {'value':>14s}  {'|rel err|':>12s}")
    for label, val in candidates.items():
        if math.isnan(val):
            continue
        rel = abs(val - k_ratio) / k_ratio
        marker = "  ← MATCH" if rel < 1e-5 else ""
        print(f"  {label:<30s}  {val:>14.10f}  {rel:>12.4e}{marker}")
    print()


# ═════════════════════════════════════════════════════════════════════
#  Main
# ═════════════════════════════════════════════════════════════════════

def main():
    print("=" * 72)
    print("R60 Track 14 — Analytical derivation of k = 1.1803/(8π)")
    print("=" * 72)
    print()

    phase1_empirical()
    phase2_symbolic()
    phase3_natural_form()

    print("=" * 72)
    print("Track 14 complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
