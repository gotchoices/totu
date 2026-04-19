"""
R60 Track 13a: R60-native α-universal inventory on Track 12 baseline.

For each particle where model-E's tuple has α ≠ α on Track 12
metric, search the α-filtered space (|α_sum| = 1 for charged,
either |α_sum| ≤ 1 for Q=0) for a better tuple.
Report the best α-universal match per particle.
"""

import sys, os, math
from itertools import product as iproduct

sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok,
    alpha_coulomb, mode_6_to_11,
    L_vector_from_params, mode_energy,
    ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI, M_E_MEV, M_P_MEV,
)
from track4_diagonal_compensation import K_NATURAL
from track7b_resolve import build_aug_metric
from track10_hadron_inventory import (
    MODEL_E_INVENTORY, mode_charge, mode_alpha_sum,
    mode_spin_half, mode_sheets_active,
)


def track12_baseline() -> Params:
    """Track 12 converged configuration (F67)."""
    return Params(
        eps_e=397.074, s_e=2.004200,
        eps_p=0.55, s_p=0.162037,
        eps_nu=2.0, s_nu=0.022,
        k_e=4.696442e-02, k_p=4.696442e-02, k_nu=4.696442e-02,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=5.4829e+01,
        L_ring_p=2.0551e+01,
        L_ring_nu=1.9577e+11,
    )


def search_for_target(G, L, target_mass, target_Q,
                       n_max=6, top_k=3, spin_half=True):
    """α-filtered brute force for one target."""
    best = []
    rng = range(-n_max, n_max + 1)

    for n6 in iproduct(rng, repeat=6):
        if all(ni == 0 for ni in n6):
            continue
        Q = -n6[0] + n6[4]
        if Q != target_Q:
            continue

        # α-sum: for unit charge, |α_sum| = 1
        # For Q=0, |α_sum| ≤ 1 (either 0 = structurally neutral or 1 = weak coupling)
        alpha_sum = n6[0] - n6[4] + n6[2]
        if target_Q == 0:
            if abs(alpha_sum) > 1:
                continue
        else:
            if alpha_sum * alpha_sum != 1:
                continue

        # Spin filter
        odd_count = (n6[0] % 2 != 0) + (n6[2] % 2 != 0) + (n6[4] % 2 != 0)
        if spin_half and odd_count % 2 != 1:
            continue
        if not spin_half and odd_count % 2 != 0:
            continue

        n11 = mode_6_to_11(n6)
        E_pred = mode_energy(G, L, n11)
        rel = abs(E_pred - target_mass) / target_mass

        if len(best) < top_k or rel < best[-1][0]:
            best.append((rel, n6, E_pred, alpha_sum))
            best.sort(key=lambda x: x[0])
            if len(best) > top_k:
                best.pop()
    return best


# Spin assignments for model-E inventory
# Baryons: spin-½; mesons: spin-0 (pions, kaons, eta) or spin-1 (ρ, φ)
SPIN_ASSIGNMENTS = {
    "electron": True,  "muon": True,  "tau": True,
    "proton":   True,  "neutron": True,
    "Λ": True,  "Σ⁻": True,  "Σ⁺": True,  "Ξ⁻": True,  "Ξ⁰": True,
    # Mesons: spin 0 or 1. For search, allow either.
    # We'll try spin-0 first.
    "η′": False,  "η": False,  "K⁰": False,  "K±": False,
    "φ": False,  "ρ": False,  "π⁰": False,  "π±": False,
}


def main():
    print("=" * 88)
    print("R60 Track 13a — R60-native α-universal inventory on Track 12 baseline")
    print("=" * 88)
    p = track12_baseline()
    G = build_aug_metric(p)
    L = L_vector_from_params(p)
    if not signature_ok(G):
        print("  WARNING: signature broken")
        return

    print()
    print(f"  {'particle':<10s}  {'M-E tuple α_sum':>16s}  {'M-E Δ':>9s}  "
          f"{'R60 native':<28s}  {'R60 Δ':>9s}  {'α/α':>6s}")

    better = 0
    same_or_worse = 0
    skipped = 0

    for label, target, Q, me_tup, me_delta in MODEL_E_INVENTORY:
        α_sum_me = mode_alpha_sum(me_tup)

        # Skip inputs
        if me_delta == "input":
            skipped += 1
            continue

        # Get model-E tuple's current accuracy for comparison
        n11_me = mode_6_to_11(me_tup)
        E_me = mode_energy(G, L, n11_me)
        a_me = alpha_coulomb(G, n11_me) / ALPHA
        rel_me = (E_me - target) / target

        # Spin: use known assignment
        spin_half = SPIN_ASSIGNMENTS.get(label, True)

        # Search
        best = search_for_target(G, L, target, Q, spin_half=spin_half)

        # Fall back to spin-1 search for ρ, φ (they're spin-1 vector mesons)
        # Try without spin constraint if the strict search fails
        if label in ("ρ", "φ") or not best:
            # Try opposite spin
            best2 = search_for_target(G, L, target, Q, spin_half=(not spin_half))
            if best2:
                if not best or best2[0][0] < best[0][0]:
                    best = best2

        if not best:
            print(f"  {label:<10s}  {α_sum_me:>+16d}  "
                  f"{rel_me*100:>+8.4f}%  (no α-universal match)     "
                  f"{'—':>9s}  {'—':>6s}")
            same_or_worse += 1
            continue

        rel, n6, E, α_sum = best[0]
        sign_ch = "+" if E > target else "-"
        tuple_str = str(n6).replace(" ", "")

        # Is it better than model-E?
        if abs(rel) < abs(rel_me):
            tag = "better"
            better += 1
        else:
            tag = "same/worse"
            same_or_worse += 1

        n11 = mode_6_to_11(n6)
        a_native = alpha_coulomb(G, n11) / ALPHA

        print(f"  {label:<10s}  {α_sum_me:>+16d}  "
              f"{rel_me*100:>+8.4f}%  {tuple_str:<28s}  "
              f"{sign_ch}{rel*100:>7.4f}%  {a_native:>6.3f}")

    print()
    print(f"  Summary: better than model-E tuple on R60: {better},  "
          f"same or worse: {same_or_worse},  skipped (inputs): {skipped}")
    print()

    # Alternative: do the search with BOTH spin-0 and spin-1 allowed for mesons
    print("=" * 88)
    print("Meson re-search with both spin parities allowed")
    print("=" * 88)
    print()
    meson_labels = ("η′", "η", "K⁰", "K±", "φ", "ρ", "π⁰", "π±")
    for label, target, Q, me_tup, me_delta in MODEL_E_INVENTORY:
        if label not in meson_labels:
            continue
        best_any = []
        for sh in (True, False):
            b = search_for_target(G, L, target, Q, spin_half=sh, top_k=3)
            for rel, n6, E, α_sum in b:
                best_any.append((rel, n6, E, α_sum, sh))
        best_any.sort(key=lambda x: x[0])
        print(f"  {label:<10s}  target = {target} MeV  (model-E Δ = {me_delta})")
        for i, (rel, n6, E, α_sum, sh) in enumerate(best_any[:3]):
            sign_ch = "+" if E > target else "-"
            sp_str = "J=½" if sh else "J=0/1"
            tuple_str = str(n6).replace(" ", "")
            print(f"    {i+1}: {tuple_str:<28s}  E = {E:>10.4f}  "
                  f"Δ = {sign_ch}{rel*100:>7.4f}%  α_sum = {α_sum:+d}  ({sp_str})")
        print()

    print("=" * 88)
    print("Track 13a complete.")
    print("=" * 88)


if __name__ == "__main__":
    main()
