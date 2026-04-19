"""
R60 Track 12: Proton sheet alignment with model-E.

Replace Track 9's magic-shear p-sheet (ε=0.4, s=3.0) with
model-E's values (ε=0.55, s=0.162) and re-run the joint solve,
inventory, and nuclear scaling audits.

Hypothesis: model-E's p-sheet was tuned for hadron and nuclear
mass fits; reverting should improve Tracks 10 and 11 accuracies.
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
)
from track4_diagonal_compensation import K_NATURAL
from track7b_resolve import (
    build_aug_metric, solve_joint_aug, n_e, n_p, n_nu1, n_nu2, n_nu3,
)
from track10_hadron_inventory import MODEL_E_INVENTORY, mode_charge, mode_alpha_sum
from track11_nuclear_scaling import NUCLEAR_TARGETS


def main():
    # Model-E p-sheet geometry (pe=0.55, s=0.162037)
    # From R19 formula in model-E context, or from R54/Track 3
    eps_e, s_e   = 397.074, 2.004200
    eps_p, s_p   = 0.55, 0.162037
    eps_nu, s_nu = 2.0, 0.022
    m_nu1_MeV    = 32.1e-9

    print("=" * 88)
    print("R60 Track 12 — Proton sheet alignment with model-E")
    print("=" * 88)
    print(f"  e-sheet: (ε={eps_e}, s={s_e})  model-E R53 Solution D")
    print(f"  p-sheet: (ε={eps_p}, s={s_p})  model-E values")
    print(f"           sε = {eps_p*s_p:.4f}, decoupling loci at 0.382 and 2.618")
    print(f"  ν-sheet: (ε={eps_nu}, s={s_nu})  R61 #1")
    print()

    # ── Phase 1: joint re-solve ──
    print("─" * 88)
    print("Phase 1 — joint re-solve with model-E p-sheet")
    print("─" * 88)
    rj = solve_joint_aug(eps_e, s_e, eps_p, s_p, eps_nu, s_nu, m_nu1_MeV)
    print(f"  converged = {rj.success}")
    print(f"  message   = {rj.message[:60]}")
    print(f"  cost      = {rj.cost:.4e}")
    print()
    print(f"  k_e = {rj.params.k_e:.6e}  ({rj.params.k_e/K_NATURAL:.4f}× R59 F59)")
    print(f"  k_p = {rj.params.k_p:.6e}  ({rj.params.k_p/K_NATURAL:.4f}× R59 F59)")
    print(f"  k_ν = {rj.params.k_nu:.6e}  ({rj.params.k_nu/K_NATURAL:.4f}× R59 F59)")
    print(f"  single-k? k_e/k_p = {rj.params.k_e/rj.params.k_p:.8f}  "
          f"k_p/k_ν = {rj.params.k_p/rj.params.k_nu:.8f}")
    print()
    print(f"  L_ring_e = {rj.params.L_ring_e:.4e} fm")
    print(f"  L_ring_p = {rj.params.L_ring_p:.4e} fm")
    print(f"  L_ring_ν = {rj.params.L_ring_nu:.4e} fm")
    print()

    G = build_aug_metric(rj.params)
    sig = signature_ok(G)
    print(f"  signature_ok = {sig}, neg eigs = {num_negative_eigs(G)}")
    if not sig:
        print("  WARNING: signature broken; halting.")
        return
    L = L_vector_from_params(rj.params)

    # Verify all targets
    a_e   = alpha_coulomb(G, n_e())   / ALPHA
    a_p   = alpha_coulomb(G, n_p())   / ALPHA
    a_nu1 = alpha_coulomb(G, n_nu1()) / ALPHA
    a_nu2 = alpha_coulomb(G, n_nu2()) / ALPHA
    a_nu3 = alpha_coulomb(G, n_nu3()) / ALPHA
    E_nu2 = mode_energy(G, L, n_nu2())
    E_nu3 = mode_energy(G, L, n_nu3())
    E_nu1 = mode_energy(G, L, n_nu1())
    dm2_21 = E_nu2**2 - E_nu1**2
    dm2_31 = E_nu3**2 - E_nu1**2
    print(f"  α_e/α = {a_e:.8f}   α_p/α = {a_p:.8f}   α_ν₁/α = {a_nu1:.8f}")
    print(f"  α_ν₂/α = {a_nu2:.8f}  α_ν₃/α = {a_nu3:.8f}")
    if dm2_21 > 0:
        print(f"  Δm²₃₁/Δm²₂₁ = {dm2_31/dm2_21:.4f}  (R49 target: 33.6)")
    print()

    # ── Phase 2: hadron inventory ──
    print("=" * 88)
    print("Phase 2 — model-E compound tuples on new (model-E p) metric")
    print("=" * 88)
    print()
    print(f"  {'particle':<10s}  {'tuple':<28s}  {'Q':>3s}  "
          f"{'α_sum':>6s}  {'predicted':>12s}  {'target':>10s}  "
          f"{'R60 Δ':>9s}  {'α/α':>8s}  {'M-E Δ'}")

    clean = 0
    mass_ok = 0
    poor = 0
    for label, target, Q, tup, me_delta in MODEL_E_INVENTORY:
        n11 = mode_6_to_11(tup)
        E_pred = mode_energy(G, L, n11)
        a_ratio = alpha_coulomb(G, n11) / ALPHA
        rel = (E_pred - target) / target if target > 0 else float("inf")
        tuple_str = str(tup).replace(" ", "")
        Q_c = mode_charge(tup)
        α_sum = mode_alpha_sum(tup)
        print(f"  {label:<10s}  {tuple_str:<28s}  {Q_c:>+3d}  "
              f"{α_sum:>+6d}  {E_pred:>12.4f}  {target:>10.4f}  "
              f"{rel:>+9.4f}  {a_ratio:>8.4f}  {me_delta}")
        if me_delta == "input":
            clean += 1
        elif abs(a_ratio - 1) < 1e-3 and abs(rel) < 0.025:
            clean += 1
        elif abs(a_ratio - 1) < 1e-3 and abs(rel) < 0.10:
            mass_ok += 1
        else:
            poor += 1
    print()
    print(f"  Summary: clean ≤ 2.5%: {clean},  mass off 2.5–10%: {mass_ok},  poor ≥ 10% or α ≠ 1: {poor}")
    print()

    # ── Phase 3: nuclear scaling ──
    print("=" * 88)
    print("Phase 3 — nuclear scaling on model-E p-sheet")
    print("=" * 88)
    print()
    print(f"  {'nucleus':<10s}  {'A':>3s}  {'Z':>3s}  "
          f"{'target':>12s}  {'primary Δ':>12s}  "
          f"{'decorated Δ':>14s}  α/α")

    for label, A, Z, target in NUCLEAR_TARGETS:
        n_et = A - Z
        n6_pri = (n_et, 0, 0, 0, A, 3 * A)
        n11 = mode_6_to_11(n6_pri)
        E_pri = mode_energy(G, L, n11)
        a_ratio = alpha_coulomb(G, n11) / ALPHA
        rel_pri = (E_pri - target) / target

        # Decorated search
        best_dec = None
        for n_er in range(-3, 4):
            for n_nur in range(-3, 4):
                n6 = (n_et, n_er, 0, n_nur, A, 3 * A)
                n11_d = mode_6_to_11(n6)
                E_d = mode_energy(G, L, n11_d)
                rel_d = abs(E_d - target) / target
                if best_dec is None or rel_d < best_dec[0]:
                    best_dec = (rel_d, n6, E_d)
        rel_dec, n6_dec, E_dec = best_dec
        sign_ch = "+" if E_dec > target else "-"

        print(f"  {label:<10s}  {A:>3d}  {Z:>3d}  "
              f"{target:>12.3f}  {rel_pri:>+11.4%}  "
              f"{sign_ch}{rel_dec:>13.4%}  {a_ratio:.2f}")
    print()

    print("=" * 88)
    print("Track 12 complete.")
    print("=" * 88)


if __name__ == "__main__":
    main()
