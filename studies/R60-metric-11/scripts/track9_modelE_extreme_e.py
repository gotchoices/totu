"""
R60 Track 9: Full joint re-solve with model-E extreme e-sheet.

Track 8b confirmed that σ_ra = (sε)·σ_ta lifts the Track 2
signature bound entirely — arbitrarily large sε is geometrically
feasible.  Track 9 exploits this by re-solving the joint
e + p + ν system with:

  e-sheet at model-E extreme values (ε=397.074, s=2.004200)
           → (1, 2) is anomalously light, generation resonance
  p-sheet at Track 7d magic shear    (ε=0.4, s=3.0)
           → (1, 3) is lightest p-sheet mode, ghost ordered
  ν-sheet at R61 #1                  (ε=2.0, s=0.022)
           → Δm²₃₁/Δm²₂₁ = 33.6 matches R49

Free knobs: (L_e, k_e, L_p, k_p, L_ν, k_ν).  NOT forcing
single-k symmetry — if solver finds different values per
sheet, so be it.

Targets: (m_e, m_p, m_ν₁, α_e=α, α_p=α, α_ν₁=α).

After convergence, re-run the compound mode search (Phase 1
model-E tuples verbatim, Phase 4 α-filtered brute force) to
see if μ, τ, n now land as low-order compounds.
"""

import sys, os, math
from itertools import product as iproduct

sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok, num_negative_eigs,
    alpha_coulomb, mode_6_to_11, derive_L_ring,
    L_vector_from_params, mode_energy,
    ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI, M_E_MEV, M_P_MEV,
    I_ALEPH, I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING,
    I_NU_TUBE, I_NU_RING, I_T,
)
from track4_diagonal_compensation import K_NATURAL
from track7b_resolve import (
    build_aug_metric, solve_joint_aug, n_e, n_p, n_nu1, n_nu2, n_nu3,
)
from track8_compound_modes import TARGETS, MODEL_E_TUPLES, mode_sheets_active


def main():
    # Model-E extreme e-sheet + Track 7d magic p + R61 #1 ν
    eps_e, s_e   = 397.074, 2.004200
    eps_p, s_p   = 0.4, 3.0
    eps_nu, s_nu = 2.0, 0.022
    m_nu1_MeV    = 32.1e-9

    print("=" * 72)
    print("R60 Track 9 — Full re-solve with model-E extreme e-sheet")
    print("=" * 72)
    print(f"  e-sheet: (ε={eps_e}, s={s_e})  sε = {eps_e*s_e:.3f}")
    print(f"  p-sheet: (ε={eps_p}, s={s_p})  sε = {eps_p*s_p:.3f}")
    print(f"  ν-sheet: (ε={eps_nu}, s={s_nu})  sε = {eps_nu*s_nu:.3f}")
    print()
    print(f"  Free knobs: L_x, k_x per sheet.")
    print(f"  Architecture: ring↔ℵ structural σ_ra active per sheet.")
    print()

    # ── Joint solve ──────────────────────────────────────────────────
    print("─" * 72)
    print("Joint 6-knob solve")
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
    print(f"  k_e/k_p   = {rj.params.k_e/rj.params.k_p:.6f}")
    print(f"  k_e/k_ν   = {rj.params.k_e/rj.params.k_nu:.6f}")
    print()
    print(f"  L_ring_e  = {rj.params.L_ring_e:.4e} fm")
    print(f"  L_ring_p  = {rj.params.L_ring_p:.4e} fm")
    print(f"  L_ring_ν  = {rj.params.L_ring_nu:.4e} fm")
    print()
    sigma_ra_e  = (rj.params.eps_e  * rj.params.s_e)  * rj.params.sign_e  * rj.params.sigma_ta
    sigma_ra_p  = (rj.params.eps_p  * rj.params.s_p)  * rj.params.sign_p  * rj.params.sigma_ta
    sigma_ra_nu = (rj.params.eps_nu * rj.params.s_nu) * rj.params.sign_nu * rj.params.sigma_ta
    print(f"  σ_ra_e = {sigma_ra_e:+.4e}")
    print(f"  σ_ra_p = {sigma_ra_p:+.4e}")
    print(f"  σ_ra_ν = {sigma_ra_nu:+.4e}")
    print()

    G = build_aug_metric(rj.params)
    sig = signature_ok(G)
    print(f"  signature_ok = {sig}, neg eigs = {num_negative_eigs(G)}")
    if not sig:
        print("  WARNING: signature broken; halting.")
        return

    L = L_vector_from_params(rj.params)

    # ── Target verification ─────────────────────────────────────────
    print()
    print("─" * 72)
    print("Target verification")
    print("─" * 72)
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
    print(f"  E_e   = {E_e:.10f} MeV (target {M_E_MEV})")
    print(f"  E_p   = {E_p:.6f} MeV (target {M_P_MEV})")
    print(f"  E_ν₁  = {E_nu1*1e9:.6f} meV (target 32.1)")
    print(f"  E_ν₂  = {E_nu2*1e9:.6f} meV")
    print(f"  E_ν₃  = {E_nu3*1e9:.6f} meV")
    dm2_21 = E_nu2**2 - E_nu1**2
    dm2_31 = E_nu3**2 - E_nu1**2
    if dm2_21 > 0:
        print(f"  Δm²₃₁/Δm²₂₁ = {dm2_31/dm2_21:.4f}  (R49 target: 33.6)")
    print(f"  α_e/α  = {a_e:.10f}")
    print(f"  α_p/α  = {a_p:.10f}")
    print(f"  α_ν₁/α = {a_nu1:.10f}")
    print(f"  α_ν₂/α = {a_nu2:.10f}")
    print(f"  α_ν₃/α = {a_nu3:.10f}")
    print()

    # ── Phase 1: model-E compound tuples on the new metric ───────────
    print("─" * 72)
    print("Compound mode check: model-E tuples on the new metric")
    print("─" * 72)
    print(f"  {'particle':<10s}  {'6-tuple':<32s}  "
          f"{'E_predicted':>14s}  {'E_target':>14s}  "
          f"{'Δ':>9s}  α/α")
    for label, target_mass, target_Q in TARGETS:
        n6 = MODEL_E_TUPLES[label]
        n11 = mode_6_to_11(n6)
        E_pred = mode_energy(G, L, n11)
        a = alpha_coulomb(G, n11) / ALPHA
        rel = (E_pred - target_mass) / target_mass
        tuple_str = str(n6)
        print(f"  {label:<10s}  {tuple_str:<32s}  "
              f"{E_pred:>14.4f}  {target_mass:>14.4f}  "
              f"{rel:>+9.4f}  {a:.4f}")
    print()

    # ── Phase 4: α-filtered brute force on new metric ────────────────
    print("─" * 72)
    print("α-filtered search (|n_i| ≤ 6, n_et−n_pt+n_νt = ±1)")
    print("─" * 72)

    target_by_Q = {}
    for label, mass, Q in TARGETS:
        target_by_Q.setdefault(Q, []).append((label, mass))

    best = {label: [] for label, _, _ in TARGETS}
    top_k = 5
    n_max = 6

    rng = range(-n_max, n_max + 1)
    for n6 in iproduct(rng, repeat=6):
        if all(ni == 0 for ni in n6):
            continue
        Q = -n6[0] + n6[4]
        if Q not in target_by_Q:
            continue
        alpha_sum = n6[0] - n6[4] + n6[2]
        if alpha_sum * alpha_sum != 1:
            continue
        odd_count = (n6[0] % 2 != 0) + (n6[2] % 2 != 0) + (n6[4] % 2 != 0)
        if odd_count % 2 != 1:
            continue

        n11 = mode_6_to_11(n6)
        E_pred = mode_energy(G, L, n11)

        for label, target_mass in target_by_Q[Q]:
            rel = abs(E_pred - target_mass) / target_mass
            lst = best[label]
            if len(lst) < top_k or rel < lst[-1][0]:
                lst.append((rel, n6, E_pred))
                lst.sort(key=lambda x: x[0])
                if len(lst) > top_k:
                    lst.pop()

    for label, target_mass, target_Q in TARGETS:
        print(f"\n  Top {top_k} α=α for {label}  (target {target_mass} MeV):")
        print(f"    {'rank':>4s}  {'6-tuple':<32s}  {'E':>14s}  {'Δ':>10s}  sheets")
        for i, (rel, n6, E) in enumerate(best[label][:top_k]):
            sign = "+" if E > target_mass else "-"
            tuple_str = str(n6)
            sheets = mode_sheets_active(n6)
            print(f"    {i+1:>4d}  {tuple_str:<32s}  {E:>14.4f}  "
                  f"{sign}{rel:>9.4%}  {sheets}")
    print()

    print("=" * 72)
    print("Track 9 complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
