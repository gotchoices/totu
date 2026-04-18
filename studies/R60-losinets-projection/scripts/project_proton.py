"""R60 — Project the model-E proton compound mode (0, 0, −2, 2, 1, 3)
onto 3D radial charge density ρ(r) via all M × P = 12 variants.
Check against Losinets's two-zone Hofstadter prediction r_m/r_c ≈ 5.2.

Run from repo root:
  python studies/R60-losinets-projection/scripts/project_proton.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from common import (
    PROTON_MODE, M_PROTON, M_NEUTRON,
    R_CORE_TARGET, R_MANTLE_TARGET, RATIO_TARGET, RATIO_WINDOW,
    run_all_variants, criteria_pass,
    build_circumferences, build_metric, mode_energy, SIGMA_CROSS, S_E, S_NU, S_P,
)


def verify_geometry():
    L, (Lre, Lrnu, Lrp) = build_circumferences()
    Gt, Gti = build_metric(L, S_E, S_NU, S_P, SIGMA_CROSS)
    E_p = mode_energy(PROTON_MODE, L, Gti)
    print(f"Geometry check (model-E, σ_45=−0.18, σ_46=+0.10):")
    print(f"  L_tube_e  = {L[0]:.3e} fm   L_ring_e  = {L[1]:.3e} fm")
    print(f"  L_tube_nu = {L[2]:.3e} fm   L_ring_nu = {L[3]:.3e} fm")
    print(f"  L_tube_p  = {L[4]:.3f} fm        L_ring_p  = {L[5]:.3f} fm")
    print(f"  E(proton  compound {PROTON_MODE})  = {E_p:.3f} MeV "
          f"(target {M_PROTON})  Δ = {E_p - M_PROTON:+.3e} MeV")
    assert abs(E_p - M_PROTON) < 0.01, "Proton energy off — geometry mismatch"
    return L, Gti, E_p


def main():
    print("=" * 78)
    print("R60 Proton — Losinets Hofstadter projection")
    print("=" * 78)
    verify_geometry()

    results, L, Gti = run_all_variants(PROTON_MODE, label='proton')

    print()
    print("Results table (proton):")
    header = f"  {'M':>4s} {'P':>4s}  {'n_scales':>8s}  {'r_in':>7s}  {'r_out':>7s}  {'ratio':>7s}  {'c1':>3s} {'c2':>3s} {'c3':>3s}"
    print(header)
    print("  " + "─" * (len(header) - 2))

    any_pass = False
    winners = []
    for r in results:
        if 'error' in r:
            print(f"  {r['M']:>4s} {r['P']:>4s}  error: {r['error']}")
            continue
        two = r['two_scale']
        if two is None:
            print(f"  {r['M']:>4s} {r['P']:>4s}  {r['n_scales']:>8d}  "
                  f"{'—':>7s}  {'—':>7s}  {'—':>7s}  {'—':>3s} {'—':>3s} {'—':>3s}")
            continue
        r_in, r_out, ratio = two
        crit = criteria_pass(r_in, r_out, mode='proton')
        y = lambda b: '✓' if b else '✗'
        print(f"  {r['M']:>4s} {r['P']:>4s}  {r['n_scales']:>8d}  "
              f"{r_in:>7.3f}  {r_out:>7.3f}  {ratio:>7.3f}  "
              f"{y(crit['c1']):>3s} {y(crit['c2']):>3s} {y(crit['c3']):>3s}")
        if crit['c1'] and crit['c2'] and crit['c3']:
            any_pass = True
            winners.append((r['M'], r['P'], r_in, r_out, ratio))

    print()
    print(f"Targets:  r_c ≈ {R_CORE_TARGET} fm,  r_m ≈ {R_MANTLE_TARGET} fm,  "
          f"ratio ≈ {RATIO_TARGET} (window [{RATIO_WINDOW[0]}, {RATIO_WINDOW[1]}])")
    if any_pass:
        print(f"\nPASS — proton criteria 1–3 met by:")
        for w in winners:
            print(f"  {w[0]} × {w[1]}:  r_in={w[2]:.3f} fm, r_out={w[3]:.3f} fm, "
                  f"ratio={w[4]:.2f}")
    else:
        print("\nFAIL — no (M, P) combination hits all three proton criteria.")

    # Save numerical results
    out_path = os.path.join(os.path.dirname(__file__), '..', 'proton_results.npz')
    save = {}
    for r in results:
        if 'error' in r:
            continue
        key = f"{r['M']}_{r['P']}".replace('-', '')
        save[key + '_r'] = r['r_grid']
        save[key + '_rho'] = r['rho']
    np.savez(out_path, **save)
    print(f"\nSaved numerics to {out_path}")

    return results


if __name__ == '__main__':
    main()
