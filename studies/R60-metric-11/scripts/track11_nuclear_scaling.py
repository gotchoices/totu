"""
R60 Track 11: Nuclear scaling audit.

Test R29 / model-E's nuclear scaling law (n_5 = A, n_6 = 3A, with
n_et = A − Z for charge Z) on the Track 9 augmented baseline.

Nuclei tested:
  d (A=2,  Z=1, target ~1875.613 MeV)
  ⁴He      (A=4,  Z=2, target ~3727.380 MeV)
  ¹²C      (A=12, Z=6, target ~11177.932 MeV)
  ⁵⁶Fe     (A=56, Z=26, target ~52089.8 MeV)

Primary tuple: (A−Z, 0, 0, 0, A, 3A).  Secondary: scan n_er and
n_νt, n_νr to see if decorations improve accuracy.

Additionally: verify that α_Coulomb for a Z-charged nucleus is
Z² × α, per the α/α = (n_et − n_pt + n_νt)² = Z² pattern.
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
from track7b_resolve import build_aug_metric
from track9_modelE_extreme_e import *
from track10_hadron_inventory import track9_params


# Observed nuclear masses (MeV) — from NIST / PDG
NUCLEAR_TARGETS = [
    # (label, A, Z, target_mass_MeV)
    ("d (²H)",     2,   1,  1875.6128),
    ("⁴He",        4,   2,  3727.379),
    ("¹²C",       12,   6, 11177.929),
    ("⁵⁶Fe",      56,  26, 52089.77),
]


def main():
    print("=" * 88)
    print("R60 Track 11 — Nuclear scaling audit")
    print("=" * 88)
    print(f"  Baseline: Track 9 (model-E extreme e-sheet)")
    print(f"  Scaling rule: n_5 = A, n_6 = 3A, n_et = A−Z")
    print(f"  Predicted α pattern: α_Coulomb = Z² × α (since α_sum = −Z)")
    print()

    p = track9_params()
    G = build_aug_metric(p)
    L = L_vector_from_params(p)

    if not signature_ok(G):
        print("  WARNING: baseline signature broken")
        return

    # Phase 1: primary tuple per nucleus
    print("─" * 88)
    print("Phase 1 — primary tuple (A−Z, 0, 0, 0, A, 3A)")
    print("─" * 88)
    print(f"  {'nucleus':<10s}  {'tuple':<28s}  {'Q_check':>7s}  "
          f"{'predicted':>14s}  {'target':>14s}  {'Δ':>9s}  "
          f"{'α/α':>10s}  {'Z²':>5s}")

    primary_results = []
    for label, A, Z, target in NUCLEAR_TARGETS:
        n_et = A - Z
        n6 = (n_et, 0, 0, 0, A, 3 * A)
        n11 = mode_6_to_11(n6)
        Q = -n6[0] + n6[4]
        E_pred = mode_energy(G, L, n11)
        a_ratio = alpha_coulomb(G, n11) / ALPHA
        rel = (E_pred - target) / target
        tuple_str = str(n6).replace(" ", "")
        print(f"  {label:<10s}  {tuple_str:<28s}  {Q:>+7d}  "
              f"{E_pred:>14.4f}  {target:>14.4f}  {rel:>+9.4%}  "
              f"{a_ratio:>10.4f}  {Z*Z:>5d}")
        primary_results.append((label, A, Z, target, n6, E_pred, rel, a_ratio))
    print()

    # Phase 2: check α pattern
    print("─" * 88)
    print("Phase 2 — α_Coulomb / (Z² · α) ratio check")
    print("─" * 88)
    print(f"  If α_Coulomb = Z² × α exactly, this ratio is 1.0 for every nucleus.")
    print()
    print(f"  {'nucleus':<10s}  {'Z':>3s}  {'α/α':>12s}  {'Z²':>6s}  "
          f"{'α/(Z²α)':>12s}")
    for label, A, Z, target, n6, E_pred, rel, a_ratio in primary_results:
        ratio = a_ratio / (Z * Z)
        print(f"  {label:<10s}  {Z:>3d}  {a_ratio:>12.6f}  {Z*Z:>6d}  "
              f"{ratio:>12.6f}")
    print()

    # Phase 3: try minor n_er / n_νr / n_νt decorations for improved fit
    print("─" * 88)
    print("Phase 3 — small decorations (n_er, n_νt, n_νr ∈ [−3, 3])")
    print("         preserving α = Z² α and (Q, spin) structure")
    print("─" * 88)

    for label, A, Z, target, n6_pri, E_pri, rel_pri, a_pri in primary_results:
        n_et = A - Z
        # α_sum for α = Z²α: n_et − n_pt + n_νt = −Z
        # n_et = A−Z, n_pt = A, so n_νt = −Z + n_pt − n_et = −Z + A − (A−Z) = 0
        # So n_νt must stay 0 to maintain α = Z²α.
        # We can vary n_er and n_νr freely (don't enter α_sum or charge)
        best = None
        for n_er in range(-3, 4):
            for n_nur in range(-3, 4):
                n6 = (n_et, n_er, 0, n_nur, A, 3 * A)
                n11 = mode_6_to_11(n6)
                E = mode_energy(G, L, n11)
                rel = abs(E - target) / target
                if best is None or rel < best[0]:
                    best = (rel, n6, E)
        rel, n6, E = best
        tuple_str = str(n6).replace(" ", "")
        sign_ch = "+" if E > target else "-"
        print(f"  {label:<10s}  best: {tuple_str:<28s}  E = {E:>14.4f}  "
              f"Δ = {sign_ch}{rel:>8.4%}")
    print()

    # Phase 4: summary vs model-E
    print("=" * 88)
    print("Phase 4 — Summary: R60 vs model-E nuclear accuracy")
    print("=" * 88)
    print()
    model_e_deltas = {
        "d (²H)":   "0.05%",
        "⁴He":     "0.69%",
        "¹²C":     "0.76%",
        "⁵⁶Fe":    "1.05%",
    }
    print(f"  {'nucleus':<10s}  {'A':>3s}  {'Z':>3s}  "
          f"{'target (MeV)':>14s}  {'R60 Δ':>10s}  {'Model-E Δ':>10s}  α/α")
    for label, A, Z, target, n6, E_pred, rel, a_ratio in primary_results:
        print(f"  {label:<10s}  {A:>3d}  {Z:>3d}  "
              f"{target:>14.3f}  {rel:>+10.4%}  "
              f"{model_e_deltas.get(label, '?'):>10s}  "
              f"{a_ratio:.2f}")
    print()

    print("=" * 88)
    print("Track 11 complete.")
    print("=" * 88)


if __name__ == "__main__":
    main()
