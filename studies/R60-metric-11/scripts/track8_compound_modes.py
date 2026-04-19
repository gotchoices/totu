"""
R60 Track 8: Compound mode search for muon, tau, neutron.

On the Track 7d magic-shear baseline (all three sheets calibrated,
α universal across sheets and modes, ghost ordering on e and p),
search for compound 6-tuples matching observed masses:
  muon μ⁻    : 105.658 MeV, charge -1, spin ½
  tau  τ⁻    : 1776.86 MeV, charge -1, spin ½
  neutron n  : 939.565 MeV, charge  0, spin ½

Three phases:
  Phase 1 — evaluate model-E's compound tuples verbatim
  Phase 2 — brute-force alternative 6-tuple search (|n_i| ≤ 10)
  Phase 3 — α audit on top matches

Mode conventions (R54):
  Charge  Q = -n_et + n_pt
  Spin ½  iff total tube-winding parity is odd
    (count of sheets with odd n_tube)
"""

import sys, os, math
from itertools import product as iproduct

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
from track7b_resolve import build_aug_metric


# ── Track 7d baseline (from findings-7 F42) ───────────────────────────

def track7d_params() -> Params:
    return Params(
        eps_e=0.4, s_e=2.0,
        eps_p=0.4, s_p=3.0,
        eps_nu=2.0, s_nu=0.022,
        k_e=4.696442e-02, k_p=4.696442e-02, k_nu=4.696442e-02,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=2.7990e+04,
        L_ring_p=1.5244e+01,
        L_ring_nu=1.9577e+11,
    )


# ── Mode properties ────────────────────────────────────────────────────

def mode_charge(n6: tuple) -> int:
    """Q = -n_et + n_pt per R54."""
    return -n6[0] + n6[4]


def mode_spin_half(n6: tuple) -> bool:
    """Spin-½ iff the count of sheets with odd n_tube is odd."""
    odd_count = sum(1 for nt in (n6[0], n6[2], n6[4]) if nt % 2 != 0)
    return odd_count % 2 == 1


def mode_sheets_active(n6: tuple) -> str:
    """Return which sheets the mode touches."""
    active = []
    if n6[0] != 0 or n6[1] != 0:  active.append("e")
    if n6[2] != 0 or n6[3] != 0:  active.append("ν")
    if n6[4] != 0 or n6[5] != 0:  active.append("p")
    return "+".join(active) if active else "empty"


# ── Targets ────────────────────────────────────────────────────────────

TARGETS = [
    ("muon",    105.658,   -1),
    ("tau",    1776.860,   -1),
    ("neutron", 939.565,    0),
]

# Model-E compound tuples for Phase 1
MODEL_E_TUPLES = {
    "muon":    (1,  1, -2, -2,  0,  0),
    "tau":     (3, -6,  2, -2,  2,  3),
    "neutron": (0, -4, -1,  2,  0, -3),
}


# ── Phase 1: model-E tuples ────────────────────────────────────────────

def phase1_evaluate(G: np.ndarray, L: np.ndarray):
    print("=" * 72)
    print("Phase 1 — evaluate model-E compound tuples verbatim")
    print("=" * 72)
    print()
    print(f"  {'particle':<10s}  {'6-tuple':<32s}  "
          f"{'Q':>3s} {'s½':>3s}  {'E_predicted':>14s}  {'E_target':>14s}  "
          f"{'Δ':>9s}  α/α")

    for label, target_mass, target_Q in TARGETS:
        n6 = MODEL_E_TUPLES[label]
        Q = mode_charge(n6)
        s_half = mode_spin_half(n6)
        n11 = mode_6_to_11(n6)

        E_pred = mode_energy(G, L, n11)
        a = alpha_coulomb(G, n11) / ALPHA
        rel = (E_pred - target_mass) / target_mass
        tuple_str = str(n6)
        print(f"  {label:<10s}  {tuple_str:<32s}  "
              f"{Q:>+3d} {'½' if s_half else 'X':>3s}  "
              f"{E_pred:>14.4f}  {target_mass:>14.4f}  "
              f"{rel:>+9.4f}  {a:.4f}")
    print()


# ── Phase 2: bounded brute-force 6-tuple search ────────────────────────

def phase2_search(G: np.ndarray, L: np.ndarray, n_max: int = 6,
                    top_k: int = 10):
    print("=" * 72)
    print(f"Phase 2 — bounded search, |n_i| ≤ {n_max}, top {top_k} per target")
    print("=" * 72)
    print()

    # Precompute ranges and targets lookup
    target_by_Q = {}
    for label, mass, Q in TARGETS:
        target_by_Q.setdefault(Q, []).append((label, mass))

    # Track best candidates per target
    # Use running sorted list; insertion sort by relative residual
    best = {label: [] for label, _, _ in TARGETS}

    rng = range(-n_max, n_max + 1)
    total = (2 * n_max + 1) ** 6
    filtered_Q = 0
    filtered_spin = 0
    evaluated = 0
    reported = 0

    for n6 in iproduct(rng, repeat=6):
        # Exclude trivial mode
        if all(ni == 0 for ni in n6):
            continue

        Q = -n6[0] + n6[4]
        if Q not in target_by_Q:
            continue
        filtered_Q += 1

        # Spin filter
        odd_count = (n6[0] % 2 != 0) + (n6[2] % 2 != 0) + (n6[4] % 2 != 0)
        if odd_count % 2 != 1:
            continue
        filtered_spin += 1

        n11 = mode_6_to_11(n6)
        E_pred = mode_energy(G, L, n11)
        evaluated += 1

        for label, target_mass in target_by_Q[Q]:
            rel = abs(E_pred - target_mass) / target_mass
            # Keep top_k sorted
            lst = best[label]
            if len(lst) < top_k or rel < lst[-1][0]:
                lst.append((rel, n6, E_pred))
                lst.sort(key=lambda x: x[0])
                if len(lst) > top_k:
                    lst.pop()
                reported += 1

    print(f"  Enumerated: {total}; Q-filtered: {filtered_Q}; "
          f"spin-filtered: {filtered_spin}; evaluated: {evaluated}")
    print()

    for label, target_mass, target_Q in TARGETS:
        print(f"  Top {top_k} for {label}  (target {target_mass} MeV, Q={target_Q:+d}):")
        print(f"    {'rank':>4s}  {'6-tuple':<32s}  {'E':>14s}  {'Δ':>10s}  sheets")
        for i, (rel, n6, E) in enumerate(best[label]):
            sign = "+" if E > target_mass else "-"
            tuple_str = str(n6)
            sheets = mode_sheets_active(n6)
            print(f"    {i+1:>4d}  {tuple_str:<32s}  {E:>14.4f}  "
                  f"{sign}{rel:>9.4%}  {sheets}")
        print()

    return best


# ── Phase 3: α audit on top matches ────────────────────────────────────

def phase3_alpha_audit(G: np.ndarray, L: np.ndarray, best: dict):
    print("=" * 72)
    print("Phase 3 — α_Coulomb audit on top-3 compound matches per target")
    print("=" * 72)
    print()
    print(f"  {'particle':<10s}  {'rank':>4s}  {'6-tuple':<32s}  "
          f"{'E':>12s}  {'α/α':>10s}")
    any_nonuniv = False
    for label, _, _ in TARGETS:
        for i, (rel, n6, E) in enumerate(best[label][:3]):
            n11 = mode_6_to_11(n6)
            a = alpha_coulomb(G, n11) / ALPHA
            tuple_str = str(n6)
            mark = "" if abs(a - 1) < 1e-3 else "  ← non-universal"
            if abs(a - 1) >= 1e-3:
                any_nonuniv = True
            print(f"  {label:<10s}  {i+1:>4d}  {tuple_str:<32s}  "
                  f"{E:>12.4f}  {a:>10.6f}{mark}")
    print()
    if any_nonuniv:
        print("  → Mode-dependent α on some compound modes.")
        print("    Pool item h (cross-sheet cancellation prescription) or")
        print("    accept-as-feature decision needed before Track 9.")
    else:
        print("  → α universal across all top compound matches.")
        print("    R60 architecture validated end-to-end.")
    print()


# ── Phase 4: α-filtered search ─────────────────────────────────────────

def phase4_search_alpha_filtered(G: np.ndarray, L: np.ndarray,
                                   n_max: int = 6, top_k: int = 10):
    """Re-search with the additional constraint (n_et - n_pt + n_νt) = ±1,
    which (empirically from Phase 3) enforces α_Coulomb = α exactly."""
    print("=" * 72)
    print(f"Phase 4 — α-filtered search  (n_et − n_pt + n_νt = ±1)")
    print("=" * 72)
    print()
    print("  This filter enforces α_Coulomb = α on every candidate.")
    print("  Conjecture (from Phase 3): α/α = (n_et − n_pt + n_νt)².")
    print()

    target_by_Q = {}
    for label, mass, Q in TARGETS:
        target_by_Q.setdefault(Q, []).append((label, mass))

    best = {label: [] for label, _, _ in TARGETS}

    rng = range(-n_max, n_max + 1)
    evaluated = 0

    for n6 in iproduct(rng, repeat=6):
        if all(ni == 0 for ni in n6):
            continue

        Q = -n6[0] + n6[4]
        if Q not in target_by_Q:
            continue

        # α = 1 filter: (n_et - n_pt + n_νt)² = 1
        alpha_sum = n6[0] - n6[4] + n6[2]
        if alpha_sum * alpha_sum != 1:
            continue

        # Spin filter
        odd_count = (n6[0] % 2 != 0) + (n6[2] % 2 != 0) + (n6[4] % 2 != 0)
        if odd_count % 2 != 1:
            continue

        n11 = mode_6_to_11(n6)
        E_pred = mode_energy(G, L, n11)
        evaluated += 1

        for label, target_mass in target_by_Q[Q]:
            rel = abs(E_pred - target_mass) / target_mass
            lst = best[label]
            if len(lst) < top_k or rel < lst[-1][0]:
                lst.append((rel, n6, E_pred))
                lst.sort(key=lambda x: x[0])
                if len(lst) > top_k:
                    lst.pop()

    print(f"  Evaluated (after α + Q + spin filters): {evaluated}")
    print()

    for label, target_mass, target_Q in TARGETS:
        print(f"  Top {top_k} α=α for {label}  (target {target_mass} MeV):")
        print(f"    {'rank':>4s}  {'6-tuple':<32s}  {'E':>14s}  {'Δ':>10s}  α/α  sheets")
        for i, (rel, n6, E) in enumerate(best[label][:top_k]):
            n11 = mode_6_to_11(n6)
            a = alpha_coulomb(G, n11) / ALPHA
            sign = "+" if E > target_mass else "-"
            tuple_str = str(n6)
            sheets = mode_sheets_active(n6)
            print(f"    {i+1:>4d}  {tuple_str:<32s}  {E:>14.4f}  "
                  f"{sign}{rel:>9.4%}  {a:.4f}  {sheets}")
        print()


# ── Main ───────────────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("R60 Track 8 — Compound mode search")
    print("=" * 72)
    print(f"  Baseline: Track 7d (magic shear, ring↔ℵ augmented)")
    print(f"  Targets: muon, tau, neutron")
    print()

    p = track7d_params()
    G = build_aug_metric(p)
    L = L_vector_from_params(p)

    if not signature_ok(G):
        print("  WARNING: baseline signature broken; aborting.")
        return
    print(f"  Signature OK, neg eigs = {num_negative_eigs(G)}")
    print()

    # Smoke: verify stable particles still exact
    print("  Smoke: stable particles on baseline metric:")
    for label, n6, target in [
        ("electron", (1, 2, 0, 0, 0, 0), M_E_MEV),
        ("proton",   (0, 0, 0, 0, 1, 3), M_P_MEV),
        ("ν₁",       (0, 0, 1, 1, 0, 0), 32.1e-9),
    ]:
        E = mode_energy(G, L, mode_6_to_11(n6))
        a = alpha_coulomb(G, mode_6_to_11(n6)) / ALPHA
        if target > 1:
            E_str = f"{E:.6f} MeV"
            tgt_str = f"{target} MeV"
        else:
            E_str = f"{E*1e9:.4f} meV"
            tgt_str = f"{target*1e9} meV"
        print(f"    {label:<10s}  E = {E_str:<20s}  target {tgt_str:<20s}  α/α = {a:.6f}")
    print()

    phase1_evaluate(G, L)
    best = phase2_search(G, L, n_max=6, top_k=10)
    phase3_alpha_audit(G, L, best)
    phase4_search_alpha_filtered(G, L, n_max=6, top_k=10)

    print("=" * 72)
    print("Track 8 complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
