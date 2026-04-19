"""
R60 Track 13b: ν-candidate sweep across R61 top-5.

For each R61 neutrino candidate:
  - Run joint solve with Track 12 architecture (model-E e + p)
  - Check convergence
  - Measure inventory accuracy (Phase 2 from Track 10/12)
  - Measure nuclear scaling (Phase 3 from Track 11)
  - Score composite

Report ranking across candidates to identify ν viable options.
"""

import sys, os, math
from itertools import product as iproduct

sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok,
    alpha_coulomb, mode_6_to_11, derive_L_ring,
    L_vector_from_params, mode_energy,
    ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI, M_E_MEV, M_P_MEV,
)
from track4_diagonal_compensation import K_NATURAL
from track7b_resolve import build_aug_metric, solve_joint_aug, n_e, n_p, n_nu1, n_nu2, n_nu3
from track10_hadron_inventory import MODEL_E_INVENTORY, mode_charge, mode_alpha_sum
from track11_nuclear_scaling import NUCLEAR_TARGETS
from track6_three_sheet_solve import R61_CANDIDATES, meV_to_MeV


def evaluate_candidate(candidate_idx, label, eps_nu, s_nu, triplet, m_nu1_meV):
    """Full Track-12-style evaluation for one ν candidate.  Returns dict."""
    m_nu1_MeV = meV_to_MeV(m_nu1_meV)

    # Model-E e and p
    eps_e, s_e = 397.074, 2.004200
    eps_p, s_p = 0.55, 0.162037

    print(f"\n── Candidate R61-#{candidate_idx}: {label} ──")
    print(f"  ε_ν = {eps_nu}, s_ν = {s_nu}, triplet {triplet}")

    result = {
        "idx": candidate_idx,
        "label": label,
        "eps_nu": eps_nu, "s_nu": s_nu, "triplet": triplet,
        "m_nu1_meV": m_nu1_meV,
    }

    # Joint solve (using ν1 mode from triplet)
    n6_nu1 = triplet[0]  # (nt, nr)

    # We need to pass these as the ν1 reference mode to the solver,
    # but solve_joint_aug uses (1, 1) by default; we'll just pass
    # through and verify ν masses post-hoc
    try:
        rj = solve_joint_aug(
            eps_e, s_e, eps_p, s_p, eps_nu, s_nu, m_nu1_MeV,
        )
    except Exception as e:
        print(f"  solver error: {e}")
        result["converged"] = False
        return result

    result["converged"] = rj.success
    result["cost"] = rj.cost

    G = build_aug_metric(rj.params)
    sig = signature_ok(G)
    result["signature"] = sig
    if not sig:
        print(f"  signature broken; skipping rest")
        return result

    L = L_vector_from_params(rj.params)

    # Check ν1 mass using the candidate's ν1 mode
    n11_nu1 = mode_6_to_11((0, 0, triplet[0][0], triplet[0][1], 0, 0))
    n11_nu2 = mode_6_to_11((0, 0, triplet[1][0], triplet[1][1], 0, 0))
    n11_nu3 = mode_6_to_11((0, 0, triplet[2][0], triplet[2][1], 0, 0))

    E_nu1 = mode_energy(G, L, n11_nu1)
    E_nu2 = mode_energy(G, L, n11_nu2)
    E_nu3 = mode_energy(G, L, n11_nu3)
    dm2_21 = E_nu2**2 - E_nu1**2
    dm2_31 = E_nu3**2 - E_nu1**2
    ratio = dm2_31 / dm2_21 if dm2_21 > 0 else float("nan")

    # Check α universality on the candidate's modes
    a_nu1 = alpha_coulomb(G, n11_nu1) / ALPHA
    a_nu2 = alpha_coulomb(G, n11_nu2) / ALPHA
    a_nu3 = alpha_coulomb(G, n11_nu3) / ALPHA

    result["E_nu1_meV"] = E_nu1 * 1e9
    result["E_nu2_meV"] = E_nu2 * 1e9
    result["E_nu3_meV"] = E_nu3 * 1e9
    result["dm2_ratio"] = ratio
    result["alpha_nu1"] = a_nu1
    result["alpha_nu2"] = a_nu2
    result["alpha_nu3"] = a_nu3

    print(f"  solve ok (cost {rj.cost:.2e}, k = {rj.params.k_e:.4e})")
    print(f"  m_ν₁ = {E_nu1*1e9:.4f} meV (target {m_nu1_meV})")
    print(f"  m_ν₂ = {E_nu2*1e9:.4f} meV")
    print(f"  m_ν₃ = {E_nu3*1e9:.4f} meV")
    print(f"  Δm²₃₁/Δm²₂₁ = {ratio:.4f}  (R49 target: 33.6)")
    print(f"  α_ν₁ = {a_nu1:.6f}, α_ν₂ = {a_nu2:.6f}, α_ν₃ = {a_nu3:.6f}")

    # Inventory accuracy: plug each model-E tuple, count how many within 2% and α = 1
    n_good = 0
    n_total = 0
    total_abs_rel = 0.0
    for p_label, target, Q, me_tup, me_delta in MODEL_E_INVENTORY:
        if me_delta == "input":
            continue
        n11 = mode_6_to_11(me_tup)
        E_pred = mode_energy(G, L, n11)
        a = alpha_coulomb(G, n11) / ALPHA
        rel = (E_pred - target) / target
        n_total += 1
        if abs(rel) < 0.02 and abs(a - 1) < 1e-3:
            n_good += 1
        total_abs_rel += abs(rel)
    result["n_good_me_tuples"] = n_good
    result["n_total_me_tuples"] = n_total
    result["mean_abs_rel"] = total_abs_rel / n_total if n_total > 0 else 0
    print(f"  model-E tuples passing (α=1 and Δ<2%): {n_good} / {n_total}  "
          f"(mean |Δ| = {result['mean_abs_rel']*100:.2f}%)")

    # Nuclear scaling accuracy
    nuc_abs_rel = []
    for nuc_label, A, Z, target in NUCLEAR_TARGETS:
        n_et = A - Z
        # Use decorated search
        best = None
        for n_er in range(-3, 4):
            for n_nur in range(-3, 4):
                n6 = (n_et, n_er, 0, n_nur, A, 3 * A)
                n11 = mode_6_to_11(n6)
                E = mode_energy(G, L, n11)
                rel = abs(E - target) / target
                if best is None or rel < best:
                    best = rel
        nuc_abs_rel.append(best)
    result["nuc_mean"] = float(np.mean(nuc_abs_rel))
    result["nuc_max"] = float(max(nuc_abs_rel))
    print(f"  nuclear scaling: mean |Δ| = {result['nuc_mean']*100:.2f}%, "
          f"max = {result['nuc_max']*100:.2f}%")

    return result


def main():
    print("=" * 88)
    print("R60 Track 13b — ν-candidate sweep across R61 top-5")
    print("=" * 88)
    print(f"  Architecture: model-E e + p, Track 12 baseline")
    print(f"  Sweep each R61 candidate's (ε_ν, s_ν, triplet), compare quality")
    print()

    # Sweep top-5 R61 candidates
    # R61_CANDIDATES is from track6_three_sheet_solve; extend with more
    # Model-E R49 Family A is close to R61 #1; let's also include #1-4 and R49
    extended_candidates = [
        (1, "R61 #1", 2.00, 0.0220, [(+1,+1), (-1,+1), (+1,+2)], 32.1),
        (2, "R61 #2", 8.50, 0.0078, [(+1,+1), (-2,+1), (+1,+2)], 29.1),
        (3, "R61 #3", 10.00, 0.0207, [(+2,+1), (-1,+1), (-1,+2)], 27.8),
        (4, "R61 #4", 2.50, 0.0193, [(+1,+1), (+2,+1), (+1,+4)], 13.8),
        # R49 Family A (model-E)
        (0, "R49 Family A (model-E)", 5.0, 0.022, [(+1,+1), (-1,+1), (+1,+2)], 29.2),
    ]

    all_results = []
    for idx, label, eps_nu, s_nu, triplet, m_nu1 in extended_candidates:
        r = evaluate_candidate(idx, label, eps_nu, s_nu, triplet, m_nu1)
        all_results.append(r)

    # Summary table
    print()
    print("=" * 88)
    print("Summary ranking")
    print("=" * 88)
    print(f"\n  {'candidate':<24s}  {'(ε_ν, s_ν)':<14s}  "
          f"{'Δm²ratio':>9s}  "
          f"{'α_ν₁/α':>8s}  {'α_ν₂/α':>8s}  {'α_ν₃/α':>8s}  "
          f"{'M-E inv':>8s}  {'inv<|Δ|>':>9s}  {'nuc<|Δ|>':>9s}")
    # Rank by composite: n_good + low mean relative error
    def score(r):
        if not r.get("signature", False):
            return 1e9
        return -r["n_good_me_tuples"] + r["mean_abs_rel"] + r["nuc_mean"]

    all_results.sort(key=score)
    for r in all_results:
        if not r.get("signature", False):
            print(f"  {r['label']:<24s}  signature broken or solve failed")
            continue
        e_s = f"({r['eps_nu']:.2f}, {r['s_nu']:.4f})"
        print(f"  {r['label']:<24s}  {e_s:<14s}  "
              f"{r['dm2_ratio']:>9.4f}  "
              f"{r['alpha_nu1']:>8.4f}  {r['alpha_nu2']:>8.4f}  "
              f"{r['alpha_nu3']:>8.4f}  "
              f"{r['n_good_me_tuples']:>3d}/{r['n_total_me_tuples']:<4d}  "
              f"{r['mean_abs_rel']*100:>8.3f}%  "
              f"{r['nuc_mean']*100:>8.3f}%")
    print()

    print("=" * 88)
    print("Track 13b complete.")
    print("=" * 88)


if __name__ == "__main__":
    main()
