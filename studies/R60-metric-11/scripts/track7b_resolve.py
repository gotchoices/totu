"""
R60 Track 7b: Re-solve joint system on the ring↔ℵ augmented metric.

Track 7 demonstrated structural ν-mode universality (spread 0.0000%)
but with α magnitude shifted to 1.0885α (because Track 6's k values
were used on a metric that had changed).  Track 7b re-solves the
joint system on the augmented metric to bring magnitude back to α
exactly.

Architecture:
  - tube↔ℵ at ±√α (sign per sheet)
  - ring↔ℵ at σ_ra = (sε)_x · sign_x · σ_ta  (NEW, structural)
  - ℵ↔t at 4πα
  - g_aa = 1

Free knobs: (L_e, k_e, L_p, k_p, L_ν, k_ν)
Targets:    (m_e, m_p, m_ν₁, α_e=α, α_p=α, α_ν₁=α)

Cross-checks (no separate target — should fall out):
  α_ν₂, α_ν₃ also = α (Track 7 structural prediction)
  Δm²₃₁/Δm²₂₁ ≈ 33.6
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


def add_ring_aleph(G: np.ndarray, p: Params) -> np.ndarray:
    """Add structural ring↔ℵ entries: σ_ra = (sε)·sign·σ_ta per sheet."""
    G_aug = G.copy()
    pairs = [
        ((p.eps_e * p.s_e) * p.sign_e * p.sigma_ta, I_E_RING),
        ((p.eps_p * p.s_p) * p.sign_p * p.sigma_ta, I_P_RING),
        ((p.eps_nu * p.s_nu) * p.sign_nu * p.sigma_ta, I_NU_RING),
    ]
    for sigma_ra, ring_idx in pairs:
        if sigma_ra != 0.0:
            G_aug[I_ALEPH, ring_idx] += sigma_ra
            G_aug[ring_idx, I_ALEPH] += sigma_ra
    return G_aug


def build_aug_metric(p: Params) -> np.ndarray:
    """Wrap build_metric_11 with the structural σ_ra augmentation."""
    return add_ring_aleph(build_metric_11(p), p)


# ── Mode shorthands ────────────────────────────────────────────────────

def n_e():    return mode_6_to_11((1, 2, 0, 0, 0, 0))
def n_p():    return mode_6_to_11((0, 0, 0, 0, 1, 3))
def n_nu1():  return mode_6_to_11((0, 0, +1, +1, 0, 0))
def n_nu2():  return mode_6_to_11((0, 0, -1, +1, 0, 0))
def n_nu3():  return mode_6_to_11((0, 0, +1, +2, 0, 0))


# ── Joint solver on augmented metric ───────────────────────────────────

def solve_joint_aug(eps_e, s_e, eps_p, s_p, eps_nu, s_nu, m_nu1_MeV,
                     k_init=K_NATURAL):
    L_e_init  = derive_L_ring(M_E_MEV,  1, 2, eps_e,  s_e,  k_init)
    L_p_init  = derive_L_ring(M_P_MEV,  1, 3, eps_p,  s_p,  k_init)
    L_nu_init = derive_L_ring(m_nu1_MeV, 1, 1, eps_nu, s_nu, k_init)

    p0 = Params(
        eps_e=eps_e, s_e=s_e,
        eps_p=eps_p, s_p=s_p,
        eps_nu=eps_nu, s_nu=s_nu,
        k_e=k_init, k_p=k_init, k_nu=k_init,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=L_e_init, L_ring_p=L_p_init, L_ring_nu=L_nu_init,
    )

    PENALTY = 100.0

    def res_me(p):
        G = build_aug_metric(p)
        L = L_vector_from_params(p)
        if not signature_ok(G):
            return PENALTY
        return (mode_energy(G, L, n_e()) - M_E_MEV) / M_E_MEV

    def res_mp(p):
        G = build_aug_metric(p)
        L = L_vector_from_params(p)
        if not signature_ok(G):
            return PENALTY
        return (mode_energy(G, L, n_p()) - M_P_MEV) / M_P_MEV

    def res_mnu1(p):
        G = build_aug_metric(p)
        L = L_vector_from_params(p)
        if not signature_ok(G):
            return PENALTY
        return (mode_energy(G, L, n_nu1()) - m_nu1_MeV) / m_nu1_MeV

    def res_ae(p):
        G = build_aug_metric(p)
        if not signature_ok(G):
            return PENALTY
        return (alpha_coulomb(G, n_e()) - ALPHA) / ALPHA

    def res_ap(p):
        G = build_aug_metric(p)
        if not signature_ok(G):
            return PENALTY
        return (alpha_coulomb(G, n_p()) - ALPHA) / ALPHA

    def res_anu(p):
        G = build_aug_metric(p)
        if not signature_ok(G):
            return PENALTY
        return (alpha_coulomb(G, n_nu1()) - ALPHA) / ALPHA

    targets = [
        Target("m_e",   res_me),
        Target("m_p",   res_mp),
        Target("m_ν1",  res_mnu1),
        Target("α_e",   res_ae),
        Target("α_p",   res_ap),
        Target("α_ν1",  res_anu),
    ]

    return solve(
        p0,
        free=["L_ring_e", "k_e", "L_ring_p", "k_p", "L_ring_nu", "k_nu"],
        targets=targets,
        bounds={
            "L_ring_e":  (1e-3, 1e9),
            "k_e":       (1e-6, 1e6),
            "L_ring_p":  (1e-3, 1e9),
            "k_p":       (1e-6, 1e6),
            "L_ring_nu": (1e-3, 1e15),
            "k_nu":      (1e-6, 1e6),
        },
        xtol=1e-12, ftol=1e-12,
    )


def main():
    eps_e, s_e   = 1.0, 0.0
    eps_p, s_p   = 1.0, 0.0
    eps_nu, s_nu = 2.0, 0.022     # R61 candidate #1
    m_nu1_meV    = 32.1
    m_nu1_MeV    = m_nu1_meV * 1e-9

    print("=" * 72)
    print("R60 Track 7b — Re-solve on ring↔ℵ augmented metric")
    print("=" * 72)
    print(f"  Architecture: tube↔ℵ + structural ring↔ℵ "
          f"(σ_ra = sε·σ_ta) + ℵ↔t")
    print(f"  Sheets: e=({eps_e},{s_e}), p=({eps_p},{s_p}), "
          f"ν=({eps_nu},{s_nu})")
    print(f"  Free knobs:  L_x, k_x for x ∈ {{e, p, ν}}  (6 knobs)")
    print(f"  Targets:     m_x and α_x = α for x ∈ {{e, p, ν₁}}  (6 targets)")
    print()

    rj = solve_joint_aug(eps_e, s_e, eps_p, s_p, eps_nu, s_nu, m_nu1_MeV)

    print("─" * 72)
    print("Solver result")
    print("─" * 72)
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
        print("  WARNING: signature broken")
        return

    L = L_vector_from_params(rj.params)
    E_e   = mode_energy(G, L, n_e())
    E_p   = mode_energy(G, L, n_p())
    E_nu1 = mode_energy(G, L, n_nu1())
    E_nu2 = mode_energy(G, L, n_nu2())
    E_nu3 = mode_energy(G, L, n_nu3())

    a_e   = alpha_coulomb(G, n_e())   / ALPHA
    a_p   = alpha_coulomb(G, n_p())   / ALPHA
    a_nu1 = alpha_coulomb(G, n_nu1()) / ALPHA
    a_nu2 = alpha_coulomb(G, n_nu2()) / ALPHA
    a_nu3 = alpha_coulomb(G, n_nu3()) / ALPHA

    print()
    print("─" * 72)
    print("Targeted modes (mass + α)")
    print("─" * 72)
    print(f"  E(e)   = {E_e:.10f} MeV    (target {M_E_MEV})")
    print(f"  E(p)   = {E_p:.6f} MeV     (target {M_P_MEV})")
    print(f"  E(ν₁)  = {E_nu1*1e9:.6f} meV  (target {m_nu1_meV})")
    print(f"  α_e/α  = {a_e:.10f}")
    print(f"  α_p/α  = {a_p:.10f}")
    print(f"  α_ν₁/α = {a_nu1:.10f}")
    print()

    print("─" * 72)
    print("Cross-check: untargeted ν modes — Track 7 predicts α_ν = α exactly")
    print("─" * 72)
    print(f"  α_ν₂/α = {a_nu2:.10f}  (R61 #1 mode (-1,+1))")
    print(f"  α_ν₃/α = {a_nu3:.10f}  (R61 #1 mode (+1,+2))")
    print(f"  E(ν₂)  = {E_nu2*1e9:.6f} meV  (R61: 33.3)")
    print(f"  E(ν₃)  = {E_nu3*1e9:.6f} meV  (R61: 59.7)")
    spread = max(abs(a_nu1-a_nu2), abs(a_nu1-a_nu3), abs(a_nu2-a_nu3))
    print(f"  ν-mode α spread (max |αᵢ-αⱼ|/α) = {spread:.2e}")
    if spread < 1e-6:
        print(f"    → Track 7 prediction confirmed: structural universality "
              f"survives the re-solve")
    else:
        print(f"    → spread is {spread:.2e}, indicating residual "
              f"cross-sheet effects")
    print()

    # Δm² ratio
    dm2_21 = E_nu2**2 - E_nu1**2
    dm2_31 = E_nu3**2 - E_nu1**2
    if dm2_21 > 0:
        ratio = dm2_31 / dm2_21
        print(f"  Δm²₃₁/Δm²₂₁ = {ratio:.6f}  (R49 target: 33.6)")
    print()

    print("=" * 72)
    print("Track 7b complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
