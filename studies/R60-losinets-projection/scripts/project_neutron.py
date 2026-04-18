"""R60 — Project the model-E neutron compound mode (0, −4, −1, 2, 0, −3)
onto 3D radial charge density ρ(r) via all M × P = 12 variants.
Verify the sign-reversed-core criterion (Losinets: neutron Q_core = −e/2,
Q_mantle = +e/2).

Run from repo root:
  python studies/R60-losinets-projection/scripts/project_neutron.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from common import (
    NEUTRON_MODE, M_NEUTRON,
    R_CORE_TARGET, R_MANTLE_TARGET, RATIO_TARGET, RATIO_WINDOW,
    run_all_variants, criteria_pass,
    build_circumferences, build_metric, mode_energy, SIGMA_CROSS, S_E, S_NU, S_P,
)


def main():
    print("=" * 78)
    print("R60 Neutron — Losinets Hofstadter projection (sign-reversed core)")
    print("=" * 78)

    L, (Lre, Lrnu, Lrp) = build_circumferences()
    from common import build_metric, SIGMA_CROSS, S_E, S_NU, S_P
    Gt, Gti = build_metric(L, S_E, S_NU, S_P, SIGMA_CROSS)
    E_n = mode_energy(NEUTRON_MODE, L, Gti)
    print(f"  E(neutron compound {NEUTRON_MODE}) = {E_n:.3f} MeV "
          f"(target {M_NEUTRON}, Δ/m = {(E_n - M_NEUTRON) / M_NEUTRON * 100:+.3f}%)")

    results, _, _ = run_all_variants(NEUTRON_MODE, label='neutron')

    print()
    print("Results table (neutron):")
    header = (f"  {'M':>4s} {'P':>4s}  {'n_scales':>8s}  {'r_in':>7s}  {'r_out':>7s}  "
              f"{'ratio':>7s}  {'sgn_in':>7s}  {'sgn_out':>7s}  c4")
    print(header)
    print("  " + "─" * (len(header) - 2))

    c4_any = False
    for r in results:
        if 'error' in r:
            print(f"  {r['M']:>4s} {r['P']:>4s}  error: {r['error']}")
            continue
        two = r['two_scale']
        if two is None:
            print(f"  {r['M']:>4s} {r['P']:>4s}  {r['n_scales']:>8d}  "
                  f"{'—':>7s}  {'—':>7s}  {'—':>7s}")
            continue
        r_in, r_out, ratio = two
        # Get signs from the original peaks (scales list holds sign as 3rd element)
        # The two chosen may not be the same elements — look up signs in scales.
        scales = r['scales']
        sign_in = next((s[2] for s in scales if abs(s[0] - r_in) < 1e-6), 0)
        sign_out = next((s[2] for s in scales if abs(s[0] - r_out) < 1e-6), 0)
        c4 = (sign_in * sign_out < 0)
        mark = '✓' if c4 else '✗'
        print(f"  {r['M']:>4s} {r['P']:>4s}  {r['n_scales']:>8d}  "
              f"{r_in:>7.3f}  {r_out:>7.3f}  {ratio:>7.3f}  "
              f"{sign_in:>+7.1f}  {sign_out:>+7.1f}  {mark}")
        if c4:
            c4_any = True

    print()
    if c4_any:
        print("Sign-reversed-core structure (c4) observed in ≥1 variant.")
    else:
        print("No variant produced sign-reversed core for the neutron.")

    # Save
    out_path = os.path.join(os.path.dirname(__file__), '..', 'neutron_results.npz')
    save = {}
    for r in results:
        if 'error' in r:
            continue
        key = f"{r['M']}_{r['P']}".replace('-', '')
        save[key + '_r'] = r['r_grid']
        save[key + '_rho'] = r['rho']
    np.savez(out_path, **save)
    print(f"Saved numerics to {out_path}")

    return results


if __name__ == '__main__':
    main()
