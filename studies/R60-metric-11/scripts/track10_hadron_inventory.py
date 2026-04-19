"""
R60 Track 10: Broader hadron inventory on Track 9 baseline.

On the Track 9 extreme-e baseline (model-E e-sheet, Track 7d p-sheet
magic shear, R61 #1 ν-sheet), evaluate model-E's full 20-particle
compound inventory.  For each:
  Phase 1: E_predicted from model-E tuple, vs observed, with α
  Phase 2: if model-E tuple fails (α ≠ α or mass > 10% off),
           α-filtered brute force for a Track 9-native tuple
  Phase 3: summary comparison R60 vs model-E
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
from track7b_resolve import build_aug_metric


# Model-E inventory — particle, observed mass (MeV), Q, tuple
MODEL_E_INVENTORY = [
    # (label, observed_MeV, Q, model-E tuple, model-E Δm/m)
    ("electron",  0.511,      -1, (1, 2, 0, 0, 0, 0),     "input"),
    ("muon",      105.658,    -1, (1, 1, -2, -2, 0, 0),   "0.83%"),
    ("tau",       1776.860,   -1, (3, -6, 2, -2, 2, 3),   "0.05%"),
    ("proton",    938.272,    +1, (0, 0, -2, 2, 1, 3),    "input"),
    ("neutron",   939.565,     0, (0, -4, -1, 2, 0, -3),  "0.07%"),
    ("Λ",         1115.683,    0, (-1, 2, -1, 2, -1, 3),  "0.00%"),
    ("η′",        957.78,      0, (-1, -7, 2, -2, -1, 2), "0.00%"),
    ("Σ⁻",        1197.449,   -1, (-1, 2, -2, 2, -2, -2), "0.01%"),
    ("Σ⁺",        1189.37,    +1, (-2, 3, 2, -2, -1, -3), "0.02%"),
    ("Ξ⁻",        1321.71,    -1, (-1, 5, -2, 2, -2, 1),  "0.03%"),
    ("φ",         1019.461,    0, (-1, 4, 2, -2, -1, 2),  "0.06%"),
    ("Ξ⁰",        1314.86,     0, (-1, 8, -3, 3, -1, 2),  "0.19%"),
    ("ρ",         775.26,      0, (-1, 5, -2, 2, 0, 1),   "0.97%"),
    ("K⁰",        497.611,     0, (0, -4, -2, 2, 0, 1),   "1.04%"),
    ("K±",        493.677,    -1, (-1, -6, -2, 2, 0, 1),  "1.77%"),
    ("η",         547.862,     0, (-1, -4, -2, 2, -1, 0), "1.84%"),
    ("π⁰",        134.977,     0, (0, -1, -2, -2, 0, 0),  "22.7%"),
    ("π±",        139.570,    -1, (-1, -1, -3, -3, 0, 0), "24.9%"),
]

# Track 9 baseline
def track9_params() -> Params:
    return Params(
        eps_e=397.074, s_e=2.004200,
        eps_p=0.4, s_p=3.0,
        eps_nu=2.0, s_nu=0.022,
        k_e=4.696442e-02, k_p=4.696442e-02, k_nu=4.696442e-02,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=5.4829e+01,
        L_ring_p=1.5244e+01,
        L_ring_nu=1.9577e+11,
    )


def mode_charge(n6: tuple) -> int:
    return -n6[0] + n6[4]


def mode_alpha_sum(n6: tuple) -> int:
    """α/α = (n_et − n_pt + n_νt)² — this returns the signed sum."""
    return n6[0] - n6[4] + n6[2]


def mode_spin_half(n6: tuple) -> bool:
    odd_count = sum(1 for nt in (n6[0], n6[2], n6[4]) if nt % 2 != 0)
    return odd_count % 2 == 1


def mode_sheets_active(n6: tuple) -> str:
    active = []
    if n6[0] != 0 or n6[1] != 0:  active.append("e")
    if n6[2] != 0 or n6[3] != 0:  active.append("ν")
    if n6[4] != 0 or n6[5] != 0:  active.append("p")
    return "+".join(active) if active else "empty"


# ── Phase 1 ────────────────────────────────────────────────────────────

def phase1(G, L):
    print("=" * 88)
    print("Phase 1 — model-E tuples on Track 9 metric (verbatim)")
    print("=" * 88)
    print()
    hdr = (f"  {'particle':<10s}  {'tuple':<28s}  {'Q':>3s}  "
           f"{'α_sum':>5s}  {'predicted':>12s}  {'target':>10s}  "
           f"{'Δ':>9s}  {'α/α':>8s}  {'M-E Δ'}")
    print(hdr)
    results = []
    for label, target, Q, tup, me_delta in MODEL_E_INVENTORY:
        Q_check = mode_charge(tup)
        alpha_sum = mode_alpha_sum(tup)
        n11 = mode_6_to_11(tup)
        E_pred = mode_energy(G, L, n11)
        a_ratio = alpha_coulomb(G, n11) / ALPHA
        rel = (E_pred - target) / target if target > 0 else float("inf")
        tuple_str = str(tup).replace(" ", "")
        print(f"  {label:<10s}  {tuple_str:<28s}  {Q_check:>+3d}  "
              f"{alpha_sum:>+5d}  {E_pred:>12.4f}  {target:>10.4f}  "
              f"{rel:>+9.4f}  {a_ratio:>8.4f}  {me_delta}")
        results.append((label, target, Q, tup, E_pred, rel, a_ratio, alpha_sum, me_delta))
    print()
    return results


# ── Phase 2 ────────────────────────────────────────────────────────────

def phase2_for_target(G, L, target_mass, target_Q, n_max=6, top_k=5,
                       require_alpha_one=True):
    """α-filtered brute force for one target."""
    best = []
    rng = range(-n_max, n_max + 1)

    for n6 in iproduct(rng, repeat=6):
        if all(ni == 0 for ni in n6):
            continue
        Q = -n6[0] + n6[4]
        if Q != target_Q:
            continue
        alpha_sum = n6[0] - n6[4] + n6[2]
        if require_alpha_one:
            # For unit-charge: α=α requires |α_sum|=1
            # For Q=0: any α_sum gives a value; we search for α_sum²=0 (perfect zero coupling)
            #   or α_sum²=1 (α=α, treating as weak-coupling analog)
            if target_Q == 0:
                # Prefer |α_sum|≤1 (either uncoupled or α=α)
                if abs(alpha_sum) > 1:
                    continue
            else:
                if alpha_sum * alpha_sum != 1:
                    continue
        # Spin filter
        odd_count = (n6[0] % 2 != 0) + (n6[2] % 2 != 0) + (n6[4] % 2 != 0)
        if odd_count % 2 != 1 and abs(target_Q) == 1:
            continue  # unit-charged particles are spin-½

        n11 = mode_6_to_11(n6)
        E_pred = mode_energy(G, L, n11)
        rel = abs(E_pred - target_mass) / target_mass

        if len(best) < top_k or rel < best[-1][0]:
            best.append((rel, n6, E_pred, alpha_sum))
            best.sort(key=lambda x: x[0])
            if len(best) > top_k:
                best.pop()
    return best


def phase2(G, L, results):
    print("=" * 88)
    print("Phase 2 — α-filtered brute-force search for targets where")
    print("         model-E tuple has α ≠ α or mass error > 5%")
    print("=" * 88)
    print()

    phase2_results = {}
    for label, target, Q, me_tup, E_pred, rel, a_ratio, alpha_sum, me_delta in results:
        # Skip inputs and clean wins
        if me_delta == "input":
            continue
        alpha_ok = abs(a_ratio - 1) < 1e-3
        mass_ok = abs(rel) < 0.05
        if alpha_ok and mass_ok:
            continue  # already good
        # Search
        best = phase2_for_target(G, L, target, Q, n_max=6, top_k=3)
        phase2_results[label] = (target, Q, best)

    for label, (target, Q, best) in phase2_results.items():
        print(f"  {label}  (target {target} MeV, Q={Q:+d}):")
        if not best:
            print(f"    (no α-compliant match within |n_i| ≤ 6)")
            continue
        for i, (rel, n6, E, alpha_sum) in enumerate(best):
            sign_ch = "+" if E > target else "-"
            tuple_str = str(n6).replace(" ", "")
            sheets = mode_sheets_active(n6)
            print(f"    {i+1}: {tuple_str:<28s}  "
                  f"E = {E:>10.4f}  Δ = {sign_ch}{rel:>8.4%}  "
                  f"α_sum = {alpha_sum:+d}  ({sheets})")
        print()
    return phase2_results


# ── Phase 3 ────────────────────────────────────────────────────────────

def phase3(results, phase2_results):
    print("=" * 88)
    print("Phase 3 — R60 vs model-E inventory summary")
    print("=" * 88)
    print()
    print(f"  {'particle':<10s}  {'target':>10s}  {'M-E Δ':>8s}  "
          f"{'R60 M-E-tuple Δ':>16s}  {'R60 α/α':>8s}  "
          f"{'R60 native':>14s}  {'R60 native Δ':>14s}")

    clean_match = 0
    needs_retune = 0
    native_ok = 0
    still_bad = 0

    for label, target, Q, me_tup, E_pred, rel, a_ratio, alpha_sum, me_delta in results:
        is_input = me_delta == "input"
        alpha_ok = abs(a_ratio - 1) < 1e-3
        mass_ok = abs(rel) < 0.05

        r60_native_tag = "—"
        r60_native_delta = "—"

        if label in phase2_results:
            _, _, best = phase2_results[label]
            if best:
                r60_native_tag = str(best[0][1]).replace(" ", "")
                r60_native_delta = f"{(best[0][2] - target)/target:+.4%}"
                if abs(best[0][0]) < 0.05:
                    native_ok += 1
                else:
                    still_bad += 1
            else:
                still_bad += 1

        if is_input:
            status = "input"
            clean_match += 1
        elif alpha_ok and mass_ok:
            status = f"{rel:+.4%}"
            clean_match += 1
        elif alpha_ok and not mass_ok:
            status = f"{rel:+.4%} (mass off)"
            needs_retune += 1
        elif not alpha_ok and mass_ok:
            status = f"α={a_ratio:.2f}"
            needs_retune += 1
        else:
            status = f"{rel:+.4%} α={a_ratio:.2f}"
            needs_retune += 1

        print(f"  {label:<10s}  {target:>10.3f}  {me_delta:>8s}  "
              f"{status:>16s}  {a_ratio:>8.4f}  "
              f"{r60_native_tag:>14s}  {r60_native_delta:>14s}")

    print()
    print(f"  Clean (input or M-E tuple matches): {clean_match}")
    print(f"  M-E tuple needs retune, R60 native found:  {native_ok}")
    print(f"  Still poor:                         {still_bad}")
    print()


# ── Main ───────────────────────────────────────────────────────────────

def main():
    print("=" * 88)
    print("R60 Track 10 — Broader hadron inventory on Track 9 baseline")
    print("=" * 88)
    print(f"  Baseline: e=(397.074, 2.004200), p=(0.4, 3.0), ν=(2.0, 0.022)")
    print(f"  Architecture: ring↔ℵ augmented; k single-symm ≈ 0.04696")
    print()

    p = track9_params()
    G = build_aug_metric(p)
    L = L_vector_from_params(p)

    if not signature_ok(G):
        print("  WARNING: signature broken")
        return

    results = phase1(G, L)
    phase2_results = phase2(G, L, results)
    phase3(results, phase2_results)

    print("=" * 88)
    print("Track 10 complete.")
    print("=" * 88)


if __name__ == "__main__":
    main()
