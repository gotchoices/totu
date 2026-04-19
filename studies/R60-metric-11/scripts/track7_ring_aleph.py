"""
R60 Track 7: Ring↔ℵ structural cancellation test.

Conjecture (post-Track 6 dialog): adding ring↔ℵ entries with
the structural prescription σ_ra = (s·ε) × σ_ta on each sheet
cancels the shear-induced α mode-dependence discovered in
Track 6 (F28).  After cancellation, Q ∝ n_t for all (n_t, n_r)
modes — universality restored across modes on a sheared sheet.

Test:
  Take Track 6 F28 baseline (R61 #1 ν geometry, e+p shearless).
  Compute σ_ra per sheet using prescription.
  Build augmented 11D metric.
  Compare α extraction (ν₁, ν₂, ν₃, electron, proton) base vs aug.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok, num_negative_eigs,
    alpha_coulomb, mode_6_to_11,
    L_vector_from_params, mode_energy,
    ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI, M_E_MEV, M_P_MEV,
    I_ALEPH, I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING,
    I_NU_TUBE, I_NU_RING, I_T,
)


def add_ring_aleph_entries(G: np.ndarray, params: Params) -> np.ndarray:
    """Augment G with ring↔ℵ entries: σ_ra_x = (sε)_x × sign_x × σ_ta."""
    G_aug = G.copy()
    sigma_ta = params.sigma_ta

    pairs = [
        ((params.eps_e * params.s_e) * params.sign_e * sigma_ta, I_E_RING),
        ((params.eps_p * params.s_p) * params.sign_p * sigma_ta, I_P_RING),
        ((params.eps_nu * params.s_nu) * params.sign_nu * sigma_ta, I_NU_RING),
    ]
    for sigma_ra, ring_idx in pairs:
        if sigma_ra != 0.0:
            G_aug[I_ALEPH, ring_idx] += sigma_ra
            G_aug[ring_idx, I_ALEPH] += sigma_ra

    return G_aug


def main():
    # Track 6 F28 baseline configuration
    eps_e, s_e = 1.0, 0.0
    eps_p, s_p = 1.0, 0.0
    eps_nu, s_nu = 2.0, 0.022
    triplet = [(+1, +1), (-1, +1), (+1, +2)]

    # k and L from Track 6 F28
    k_e = 4.729397e-2
    k_p = 4.729397e-2
    k_nu = 4.530460e-2

    p = Params(
        eps_e=eps_e, s_e=s_e,
        eps_p=eps_p, s_p=s_p,
        eps_nu=eps_nu, s_nu=s_nu,
        k_e=k_e, k_p=k_p, k_nu=k_nu,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=2.4948e+04,
        L_ring_p=1.9215e+01,
        L_ring_nu=1.9932e+11,
    )

    # Build metrics
    G_base = build_metric_11(p)
    G_aug = add_ring_aleph_entries(G_base, p)

    # σ_ra values for reporting
    sigma_ra_e  = (p.eps_e  * p.s_e)  * p.sign_e  * p.sigma_ta
    sigma_ra_p  = (p.eps_p  * p.s_p)  * p.sign_p  * p.sigma_ta
    sigma_ra_nu = (p.eps_nu * p.s_nu) * p.sign_nu * p.sigma_ta

    print("=" * 72)
    print("R60 Track 7 — Ring↔ℵ structural cancellation test")
    print("=" * 72)
    print(f"  Track 6 F28 baseline:")
    print(f"    e:  ε={eps_e}, s={s_e}, k={k_e:.4e}, L={p.L_ring_e:.3e} fm")
    print(f"    p:  ε={eps_p}, s={s_p}, k={k_p:.4e}, L={p.L_ring_p:.3e} fm")
    print(f"    ν:  ε={eps_nu}, s={s_nu}, k={k_nu:.4e}, "
          f"L={p.L_ring_nu:.3e} fm")
    print()
    print(f"  Structural prescription: σ_ra = (s·ε) × sign × σ_ta")
    print(f"    σ_ra_e  = {sigma_ra_e:+.6e}  (sε = {p.eps_e*p.s_e:.3f})")
    print(f"    σ_ra_p  = {sigma_ra_p:+.6e}  (sε = {p.eps_p*p.s_p:.3f})")
    print(f"    σ_ra_ν  = {sigma_ra_nu:+.6e}  (sε = {p.eps_nu*p.s_nu:.3f})")
    print()

    print("─" * 72)
    print("Signature check")
    print("─" * 72)
    sig_base = signature_ok(G_base)
    sig_aug = signature_ok(G_aug)
    print(f"  Base metric:      signature OK = {sig_base}, "
          f"neg eigs = {num_negative_eigs(G_base)}")
    print(f"  Augmented metric: signature OK = {sig_aug}, "
          f"neg eigs = {num_negative_eigs(G_aug)}")
    print()
    if not sig_aug:
        print("  WARNING: augmented signature broken — test invalidated.")
        return

    print("─" * 72)
    print("α_Coulomb comparison: base vs augmented")
    print("─" * 72)
    n_e_mode  = mode_6_to_11((1, 2, 0, 0, 0, 0))
    n_p_mode  = mode_6_to_11((0, 0, 0, 0, 1, 3))
    n_nu1     = mode_6_to_11((0, 0, +1, +1, 0, 0))
    n_nu2     = mode_6_to_11((0, 0, -1, +1, 0, 0))
    n_nu3     = mode_6_to_11((0, 0, +1, +2, 0, 0))

    print(f"  {'mode':>14s}  {'α_base/α':>12s}  {'α_aug/α':>12s}  "
          f"{'change':>10s}")
    rows = [
        ("electron (1,2)", n_e_mode),
        ("proton (1,3)",    n_p_mode),
        ("ν₁ (+1,+1)",       n_nu1),
        ("ν₂ (-1,+1)",       n_nu2),
        ("ν₃ (+1,+2)",       n_nu3),
    ]
    for label, n_mode in rows:
        a_base = alpha_coulomb(G_base, n_mode) / ALPHA
        a_aug = alpha_coulomb(G_aug, n_mode) / ALPHA
        chg = (a_aug - a_base) / a_base if a_base != 0 else float("inf")
        print(f"  {label:>14s}  {a_base:>12.6f}  {a_aug:>12.6f}  "
              f"{chg:>+10.4f}")
    print()

    print("─" * 72)
    print("ν-sheet mode universality check")
    print("─" * 72)
    a_nu1_base = alpha_coulomb(G_base, n_nu1) / ALPHA
    a_nu2_base = alpha_coulomb(G_base, n_nu2) / ALPHA
    a_nu3_base = alpha_coulomb(G_base, n_nu3) / ALPHA
    a_nu1_aug = alpha_coulomb(G_aug, n_nu1) / ALPHA
    a_nu2_aug = alpha_coulomb(G_aug, n_nu2) / ALPHA
    a_nu3_aug = alpha_coulomb(G_aug, n_nu3) / ALPHA

    spread_base = max(abs(a_nu1_base - a_nu2_base),
                      abs(a_nu1_base - a_nu3_base),
                      abs(a_nu2_base - a_nu3_base))
    spread_aug = max(abs(a_nu1_aug - a_nu2_aug),
                     abs(a_nu1_aug - a_nu3_aug),
                     abs(a_nu2_aug - a_nu3_aug))

    print(f"  Base spread:      max(|α_νᵢ - α_νⱼ|/α) = {spread_base:.6f}  "
          f"({spread_base*100:.2f}% of α)")
    print(f"  Augmented spread: max(|α_νᵢ - α_νⱼ|/α) = {spread_aug:.6f}  "
          f"({spread_aug*100:.4f}% of α)")
    if spread_aug < 1e-3:
        print(f"  → Universality RESTORED (spread < 0.1%)")
    elif spread_aug < spread_base / 10:
        print(f"  → Universality much improved ({spread_base/spread_aug:.1f}× tighter)")
    elif spread_aug < spread_base:
        print(f"  → Improvement ({spread_base/spread_aug:.2f}× tighter)")
    else:
        print(f"  → No improvement or worse")
    print()

    print("─" * 72)
    print("Mass impact (using mode_energy formula on Ma block only)")
    print("─" * 72)
    L = L_vector_from_params(p)
    print(f"  {'mode':>14s}  {'E_base':>16s}  {'E_aug':>16s}  {'rel shift':>12s}")
    for label, n_mode in rows:
        E_base = mode_energy(G_base, L, n_mode)
        E_aug  = mode_energy(G_aug, L, n_mode)
        rel = (E_aug - E_base) / E_base if E_base > 0 else 0
        print(f"  {label:>14s}  {E_base:>16.10e}  {E_aug:>16.10e}  "
              f"{rel:>+12.4e}")
    print()
    print("  (Note: mode_energy uses only the Ma sub-block; ring↔ℵ entries")
    print("   sit outside Ma so they don't enter this approximation.")
    print("   A full Schur-corrected mass would shift slightly.)")
    print()

    print("=" * 72)
    print("Track 7 complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
