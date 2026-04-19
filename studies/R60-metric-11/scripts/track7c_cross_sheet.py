"""
R60 Track 7c: Inter-sheet shear compatibility check.

Quick sanity test: can we activate Ma cross-sheet σ entries
without breaking Track 7b's α universality?

Tests cross-sheet entries (σ at Ma[i,j] for i,j in different
sheets):
  - σ_pt_νr  (index 1-6): R54's σ₄₅ analog (neutron region)
  - σ_pr_νr  (index 2-6): R54's σ₄₆ analog (neutron region)
  - σ_et_νr, σ_er_νr: electron–neutrino cross (model-E muon site)

For each activation magnitude, report:
  - signature OK?
  - α_e, α_p, α_ν₁ (should stay at α)
  - α_ν₂, α_ν₃ (should stay at α per Track 7)
  - mass shifts for the targeted modes

Then a re-solve attempt to absorb any shift.
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
    I_NU_TUBE, I_NU_RING, I_T,
)
from track4_diagonal_compensation import K_NATURAL
from track7b_resolve import add_ring_aleph, solve_joint_aug, n_e, n_p, n_nu1, n_nu2, n_nu3


def build_aug_with_cross(p: Params, cross_sigmas: dict) -> np.ndarray:
    """Build the ring↔ℵ augmented metric, then add cross-sheet σ entries.
    cross_sigmas maps (i, j) → σ value, with i, j in the Ma slice 1..6."""
    G = build_metric_11(p)
    G = add_ring_aleph(G, p)
    for (i, j), sigma in cross_sigmas.items():
        G[i, j] += sigma
        G[j, i] += sigma
    return G


def track7b_baseline() -> Params:
    """The Track 7b converged configuration (F35)."""
    return Params(
        eps_e=1.0, s_e=0.0,
        eps_p=1.0, s_p=0.0,
        eps_nu=2.0, s_nu=0.022,
        k_e=4.696442e-02, k_p=4.696442e-02, k_nu=4.696442e-02,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=2.5035e+04,
        L_ring_p=1.9282e+01,
        L_ring_nu=1.9577e+11,
    )


def report_alpha(G, label):
    """Print α for each target mode."""
    a_e   = alpha_coulomb(G, n_e())   / ALPHA
    a_p   = alpha_coulomb(G, n_p())   / ALPHA
    a_nu1 = alpha_coulomb(G, n_nu1()) / ALPHA
    a_nu2 = alpha_coulomb(G, n_nu2()) / ALPHA
    a_nu3 = alpha_coulomb(G, n_nu3()) / ALPHA
    sig = signature_ok(G)
    print(f"  {label}")
    print(f"    signature_ok: {sig}")
    print(f"    α_e   = {a_e:.8f}")
    print(f"    α_p   = {a_p:.8f}")
    print(f"    α_ν₁  = {a_nu1:.8f}")
    print(f"    α_ν₂  = {a_nu2:.8f}")
    print(f"    α_ν₃  = {a_nu3:.8f}")
    spread = max(abs(a_nu1-a_nu2), abs(a_nu1-a_nu3), abs(a_nu2-a_nu3))
    dev = max(abs(a_e-1), abs(a_p-1), abs(a_nu1-1))
    print(f"    ν spread: {spread:.2e}   deviation from α: {dev:.2e}")
    return sig, a_e, a_p, a_nu1, a_nu2, a_nu3


def main():
    print("=" * 72)
    print("R60 Track 7c — Inter-sheet shear compatibility check")
    print("=" * 72)

    p = track7b_baseline()

    # Baseline α (no cross-sheet entries)
    print("\n── Baseline (no cross-sheet σ) ──")
    G0 = build_aug_with_cross(p, {})
    report_alpha(G0, "Track 7b baseline + ring↔ℵ")

    # Test configurations — various cross-sheet activations
    # Index ordering: 1=p_t, 2=p_r, 3=e_t, 4=e_r, 5=ν_t, 6=ν_r
    test_configs = [
        ("σ_{pt, νr} = 0.01 (small, R54-adjacent)",  {(I_P_TUBE, I_NU_RING): 0.01}),
        ("σ_{pt, νr} = 0.10",                         {(I_P_TUBE, I_NU_RING): 0.10}),
        ("σ_{pt, νr} = -0.18 (R54 σ₄₅ value)",       {(I_P_TUBE, I_NU_RING): -0.18}),
        ("σ_{pr, νr} = +0.10 (R54 σ₄₆ value)",       {(I_P_RING, I_NU_RING): +0.10}),
        ("R54 pair: σ_{pt,νr}=-0.18 + σ_{pr,νr}=+0.10",
         {(I_P_TUBE, I_NU_RING): -0.18, (I_P_RING, I_NU_RING): +0.10}),
        ("σ_{et, νr} = 0.05 (e-ν compound region)",  {(I_E_TUBE, I_NU_RING): 0.05}),
        ("σ_{et, νt} = 0.05 (e-ν tube-tube)",        {(I_E_TUBE, I_NU_TUBE): 0.05}),
        ("σ_{er, νr} = 0.05 (e-ν ring-ring)",        {(I_E_RING, I_NU_RING): 0.05}),
    ]

    results = []
    for label, cross_sigmas in test_configs:
        print(f"\n── {label} ──")
        G = build_aug_with_cross(p, cross_sigmas)
        result = report_alpha(G, "")
        results.append((label, result, cross_sigmas))

    # Summary table
    print("\n" + "=" * 72)
    print("Summary: which cross-sheet activations preserve α universality?")
    print("=" * 72)
    print(f"  {'config':<50s}  {'ν spread':>12s}  {'α dev':>10s}  OK?")
    for label, (sig, ae, ap, anu1, anu2, anu3), _ in results:
        spread = max(abs(anu1-anu2), abs(anu1-anu3), abs(anu2-anu3))
        dev = max(abs(ae-1), abs(ap-1), abs(anu1-1))
        ok = sig and dev < 1e-3 and spread < 1e-3
        tag = "YES" if ok else ("partial" if sig and dev < 0.05 else "no")
        print(f"  {label:<50s}  {spread:>12.2e}  {dev:>10.2e}  {tag}")

    # One re-solve attempt on the R54-pair configuration
    print("\n" + "=" * 72)
    print("Re-solve attempt: R54 pair σ_{pt,νr}=-0.18 + σ_{pr,νr}=+0.10")
    print("=" * 72)
    print("Can the joint solver recover α targets with these entries present?")

    # Note: our solve() infrastructure doesn't directly support cross-sheet
    # σ yet, so we just report the baseline shift. A full re-solve would
    # require extending Params + build_metric_11 to accept cross_sigmas.

    cross_r54 = {(I_P_TUBE, I_NU_RING): -0.18, (I_P_RING, I_NU_RING): +0.10}
    G_r54 = build_aug_with_cross(p, cross_r54)
    L = L_vector_from_params(p)

    if signature_ok(G_r54):
        E_e = mode_energy(G_r54, L, n_e())
        E_p = mode_energy(G_r54, L, n_p())
        E_nu1 = mode_energy(G_r54, L, n_nu1())
        print(f"  Masses at Track 7b (L, k) without re-solve:")
        print(f"    E_e   = {E_e:.6f} (target {M_E_MEV})  Δ = {(E_e - M_E_MEV)/M_E_MEV*100:+.4f}%")
        print(f"    E_p   = {E_p:.4f} (target {M_P_MEV})  Δ = {(E_p - M_P_MEV)/M_P_MEV*100:+.4f}%")
        print(f"    E_ν₁  = {E_nu1*1e9:.6f} meV (target 32.1)  "
              f"Δ = {(E_nu1 - 32.1e-9)/32.1e-9*100:+.4f}%")
        print()
        print("  (Full re-solve with cross-sheet σ as free knobs is a Track 8")
        print("   infrastructure task — not done here.)")

    print()
    print("=" * 72)
    print("Track 7c complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
