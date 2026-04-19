"""
R60 Track 8b: Extreme-geometry e-sheet signature sanity check.

Hypothesis (from post-Track 8 dialog): with σ_ra = (sε)·σ_ta
active, the Track 2 bound `(sε)² ≤ 9/2` is lifted — signature
becomes independent of the in-sheet shear magnitude.

Derivation gave:
    det(A) = k · (σ_ta² − k·(g + σ_at²))
at the σ_ra-augmented 4×4 subspace — no u = sε dependence.

Test: build the 11D metric with e-sheet at model-E extreme values
(ε_e = 397.074, s_e = 2.004200, sε ≈ 795), σ_ra augmentation
active, p and ν sheets at Track 7d values.  Check:
  - signature OK?
  - α_e at (1, 2) electron mode = α?
  - α_p, α_ν still = α?
  - ν₂, ν₃ still = α (structural universality)?
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok, num_negative_eigs,
    alpha_coulomb, mode_6_to_11, mu_sheet, derive_L_ring,
    L_vector_from_params, mode_energy,
    ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI, M_E_MEV, M_P_MEV,
    I_ALEPH, I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING,
    I_NU_TUBE, I_NU_RING, I_T,
)
from track7b_resolve import build_aug_metric, n_e, n_p, n_nu1, n_nu2, n_nu3


def test_config(eps_e, s_e, k_e, label):
    """Build metric with model-E e-sheet at given (ε, s, k), Track 7d p/ν,
    σ_ra augmented.  Report signature and α values."""
    # L_ring_e calibrated to m_e at this geometry
    L_ring_e = derive_L_ring(M_E_MEV, 1, 2, eps_e, s_e, k_e)

    p = Params(
        eps_e=eps_e, s_e=s_e,
        eps_p=0.4, s_p=3.0,
        eps_nu=2.0, s_nu=0.022,
        k_e=k_e, k_p=4.696442e-02, k_nu=4.696442e-02,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=L_ring_e,
        L_ring_p=1.5244e+01,
        L_ring_nu=1.9577e+11,
    )
    G = build_aug_metric(p)
    L = L_vector_from_params(p)

    sig = signature_ok(G)
    nneg = num_negative_eigs(G)
    eigs = np.linalg.eigvalsh(G)
    min_pos = float(eigs[eigs > 0].min()) if (eigs > 0).any() else 0.0

    print(f"── {label} ──")
    print(f"  (ε_e, s_e) = ({eps_e}, {s_e}),  sε = {eps_e*s_e:.2f},  "
          f"k_e = {k_e:.3e}")
    print(f"  σ_ra_e (derived) = {eps_e*s_e*p.sign_e*p.sigma_ta:+.4e}")
    print(f"  L_ring_e (from m_e) = {L_ring_e:.4e} fm")
    print(f"  signature OK = {sig}, neg eigs = {nneg}, "
          f"min pos eig = {min_pos:.3e}")
    if sig:
        E_e   = mode_energy(G, L, n_e())
        E_p   = mode_energy(G, L, n_p())
        E_nu1 = mode_energy(G, L, n_nu1())
        a_e   = alpha_coulomb(G, n_e())   / ALPHA
        a_p   = alpha_coulomb(G, n_p())   / ALPHA
        a_nu1 = alpha_coulomb(G, n_nu1()) / ALPHA
        a_nu2 = alpha_coulomb(G, n_nu2()) / ALPHA
        a_nu3 = alpha_coulomb(G, n_nu3()) / ALPHA
        print(f"  E_e = {E_e:.6f} MeV (target {M_E_MEV})  rel = {(E_e-M_E_MEV)/M_E_MEV:+.2e}")
        print(f"  E_p = {E_p:.4f} MeV  rel = {(E_p-M_P_MEV)/M_P_MEV:+.2e}")
        print(f"  E_ν₁ = {E_nu1*1e9:.4f} meV")
        print(f"  α_e/α  = {a_e:.8f}")
        print(f"  α_p/α  = {a_p:.8f}")
        print(f"  α_ν₁/α = {a_nu1:.8f}")
        print(f"  α_ν₂/α = {a_nu2:.8f}")
        print(f"  α_ν₃/α = {a_nu3:.8f}")
    print()
    return sig


def main():
    print("=" * 72)
    print("R60 Track 8b — Extreme-geometry e-sheet signature sanity")
    print("=" * 72)
    print()
    print("  Hypothesis: σ_ra = (sε)·σ_ta lifts the Track 2 signature bound.")
    print("  Test by increasing e-sheet sε through Track 2 cliff (2.12)")
    print("  and up to model-E values (~795).")
    print()

    # Reference: Track 7d (sε = 0.8)
    test_config(0.4, 2.0, 4.696e-02, "Track 7d reference (sε = 0.8)")

    # Just above Track 2 bound — this would have failed at Track 2
    test_config(1.5, 1.5, 4.696e-02, "sε = 2.25 (just past Track 2 cliff)")

    # Larger
    test_config(5.0, 2.0, 4.696e-02, "sε = 10")

    # Approaching model-E
    test_config(50.0, 2.0, 4.696e-02, "sε = 100")

    # Model-E extreme
    test_config(397.074, 2.004200, 4.696e-02, "sε ≈ 795 (model-E extreme)")

    # Even more extreme as a stress test
    test_config(1000.0, 2.0, 4.696e-02, "sε = 2000 (stress)")

    print("=" * 72)
    print("Track 8b complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
