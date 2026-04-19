"""
R59 Track 3g: Natural-form parameter scan for exact α_Coulomb = α.

Track 3f F54 found α_Coulomb = 0.977α at simple values
(k = 0.10, σ_at = 0.5, g_aa = 1, σ_ta = √α).

This track does a focused search over natural-form combinations
of the three knobs (k, σ_at, g_aa) at σ_ta = √α (fixed natural)
to find combinations that hit α exactly.

Architecture: 11D clean Ma + ℵ + S + t.  Tube↔ℵ at ±√α.
ν-tube uncoupled.  Sheets share scale: k_e = k_p = k.

Goal: find a natural-form (k, σ_at, g_aa) giving α_Coulomb = α
to within 1% (or 0.1% for "exact").
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from itertools import product

ALPHA = 1.0 / 137.036
SQRT_ALPHA = math.sqrt(ALPHA)
PI = math.pi
TWO_PI = 2 * PI
FOUR_PI = 4 * PI

MODE_E = (1, 2, 0, 0, 0, 0)
MODE_P = (0, 0, -2, 2, 1, 3)
MODE_NU = (0, 0, 1, 1, 0, 0)

# New ordering: ℵ=0, p_t=1, p_r=2, e_t=3, e_r=4, ν_t=5, ν_r=6, S=7-9, t=10
OLD_TO_NEW = {0: 3, 1: 4, 2: 5, 3: 6, 4: 1, 5: 2}
I_ALEPH, I_P_TUBE, I_E_TUBE, I_T = 0, 1, 3, 10


def build_metric(k, g_aa, sigma_at, sigma_ta=SQRT_ALPHA):
    """Clean Ma + tube↔ℵ + ℵ↔t with sheet scale k (k_e = k_p = k_ν = k for simplicity).

    Actually we set k_ν = 1 since ν isn't coupled and to match Track 3f.
    """
    G = np.zeros((11, 11))
    G[0, 0] = g_aa
    G[1, 1] = G[2, 2] = k     # p-sheet
    G[3, 3] = G[4, 4] = k     # e-sheet
    G[5, 5] = G[6, 6] = 1.0   # ν-sheet uncoupled, identity
    G[7, 7] = G[8, 8] = G[9, 9] = 1.0
    G[I_T, I_T] = -1.0
    G[I_ALEPH, I_E_TUBE] = +sigma_ta
    G[I_E_TUBE, I_ALEPH] = +sigma_ta
    G[I_ALEPH, I_P_TUBE] = -sigma_ta
    G[I_P_TUBE, I_ALEPH] = -sigma_ta
    G[I_ALEPH, I_T] = sigma_at
    G[I_T, I_ALEPH] = sigma_at
    return G


def map_mode(n_old):
    n = np.zeros(11)
    for i, v in enumerate(n_old):
        n[OLD_TO_NEW[i]] = v
    return n


def alpha_coulomb(G, n_new):
    try:
        G_inv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return float('nan')
    Q = float((n_new[1:7] @ G_inv[1:7, I_T]) * (-G_inv[I_T, I_T]))
    return Q * Q / (4 * PI)


def signature_ok(G):
    return int(np.sum(np.linalg.eigvalsh(G) < 0)) == 1


def evaluate(k, g_aa, sigma_at):
    G = build_metric(k, g_aa, sigma_at)
    if not signature_ok(G):
        return None
    ae = alpha_coulomb(G, map_mode(MODE_E))
    ap = alpha_coulomb(G, map_mode(MODE_P))
    an = alpha_coulomb(G, map_mode(MODE_NU))
    return {'ae': ae, 'ap': ap, 'an': an,
            'ratio_e': ae/ALPHA, 'ratio_ep': ae/ap if ap else float('nan')}


# Natural-form candidate values
NATURAL_VALUES = {
    'α':       ALPHA,
    'α/π':     ALPHA / PI,
    'α/(4π)':  ALPHA / FOUR_PI,
    '4πα':     FOUR_PI * ALPHA,
    'πα':      PI * ALPHA,
    '√α':      SQRT_ALPHA,
    '√(4πα)':  math.sqrt(FOUR_PI * ALPHA),
    '√(α/π)':  math.sqrt(ALPHA / PI),
    '√(α/(4π))': math.sqrt(ALPHA / FOUR_PI),
    '1/(8π)':  1/(8*PI),
    '1/(4π)':  1/FOUR_PI,
    '1/(2π)':  1/TWO_PI,
    '1/π':     1/PI,
    '1/3':     1/3,
    '1/2':     0.5,
    '2/3':     2/3,
    '1':       1.0,
    '4/3':     4/3,
    'π/4':     PI/4,
    'π/2':     PI/2,
    '1/√(4π)': 1/math.sqrt(FOUR_PI),
    '1/√π':    1/math.sqrt(PI),
}


def main():
    print('=' * 80)
    print('R59 Track 3g — Natural-form parameter scan')
    print('=' * 80)
    print()
    print(f'  α = {ALPHA:.10f}')
    print(f'  √α = {SQRT_ALPHA:.10f}')
    print(f'  1/(4π) = {1/FOUR_PI:.10f}')
    print()
    print('  Architecture: clean Ma (k_e = k_p = k), σ_ta = √α (fixed)')
    print('  Search: combinations of (k, g_aa, σ_at) from natural-form candidates')
    print('  Targets: α_Coulomb = α (±1%), universality automatic, α_ν = 0 automatic')
    print()
    print('  Natural-form candidates:')
    for name, val in sorted(NATURAL_VALUES.items(), key=lambda kv: kv[1]):
        print(f'    {name:>14s} = {val:.6e}')
    print()

    # ── Search all combinations ──
    print('─' * 80)
    print('  Section 1: Full natural-form combination scan')
    print('─' * 80)
    print()

    matches_strict = []  # within 0.1%
    matches_loose = []   # within 1%
    matches_5pct = []    # within 5%

    for (k_name, k), (g_name, g), (s_name, s) in product(
            NATURAL_VALUES.items(), repeat=3):
        result = evaluate(k, g, s)
        if result is None:
            continue
        ratio = result['ratio_e']
        if math.isnan(ratio):
            continue
        record = {
            'k': (k_name, k), 'g_aa': (g_name, g), 'σ_at': (s_name, s),
            'ratio_e': ratio, 'an': result['an'],
        }
        if abs(ratio - 1.0) < 0.001:
            matches_strict.append(record)
        if abs(ratio - 1.0) < 0.01:
            matches_loose.append(record)
        if abs(ratio - 1.0) < 0.05:
            matches_5pct.append(record)

    n_combos = len(NATURAL_VALUES) ** 3
    print(f'  Tested {n_combos} combinations.')
    print(f'    Within 5% of α:   {len(matches_5pct)}')
    print(f'    Within 1% of α:   {len(matches_loose)}')
    print(f'    Within 0.1% of α: {len(matches_strict)}')
    print()

    # ── Report best matches ──
    if matches_strict:
        print('  STRICT matches (within 0.1%):')
        print(f'  {"k":>16s}  {"g_aa":>16s}  {"σ_at":>16s}  '
              f'{"α_e/α":>10s}  {"α_ν":>10s}')
        print(f'  {"-"*16}  {"-"*16}  {"-"*16}  {"-"*10}  {"-"*10}')
        for m in sorted(matches_strict, key=lambda x: abs(x['ratio_e'] - 1.0)):
            print(f'  {m["k"][0]:>16s}  {m["g_aa"][0]:>16s}  {m["σ_at"][0]:>16s}  '
                  f'{m["ratio_e"]:10.6f}  {abs(m["an"]):10.4e}')
        print()

    print('  LOOSE matches (within 1%, sorted by closeness):')
    print(f'  {"k":>16s}  {"g_aa":>16s}  {"σ_at":>16s}  '
          f'{"α_e/α":>10s}')
    print(f'  {"-"*16}  {"-"*16}  {"-"*16}  {"-"*10}')
    for m in sorted(matches_loose, key=lambda x: abs(x['ratio_e'] - 1.0))[:30]:
        print(f'  {m["k"][0]:>16s}  {m["g_aa"][0]:>16s}  {m["σ_at"][0]:>16s}  '
              f'{m["ratio_e"]:10.6f}')

    # ── Best 30 from 5% bracket (sorted by closeness) ──
    print()
    print('  Top 30 from 5% bracket (sorted by closeness):')
    print(f'  {"k":>16s}  {"g_aa":>16s}  {"σ_at":>16s}  '
          f'{"α_e/α":>10s}')
    print(f'  {"-"*16}  {"-"*16}  {"-"*16}  {"-"*10}')
    for m in sorted(matches_5pct, key=lambda x: abs(x['ratio_e'] - 1.0))[:30]:
        print(f'  {m["k"][0]:>16s}  {m["g_aa"][0]:>16s}  {m["σ_at"][0]:>16s}  '
              f'{m["ratio_e"]:10.6f}')

    # ── Section 2: Refine around the best matches ──
    print()
    print('─' * 80)
    print('  Section 2: Fine-tuning around best matches')
    print('─' * 80)
    print()
    print('  For top matches, scan a small region around each knob to find exact match.')
    print()

    best_to_refine = sorted(matches_5pct, key=lambda x: abs(x['ratio_e'] - 1.0))[:5]
    if not best_to_refine:
        best_to_refine = []
        # Fall back: scan a wide grid
        for k in [0.05, 0.075, 0.08, 0.085, 0.09, 0.1, 0.12, 0.15]:
            for g in [0.5, 1.0, 2.0]:
                for s in [0.3, 0.5, 0.7, 1.0]:
                    r = evaluate(k, g, s)
                    if r and not math.isnan(r['ratio_e']):
                        best_to_refine.append({
                            'k': (f'{k:.3f}', k),
                            'g_aa': (f'{g:.2f}', g),
                            'σ_at': (f'{s:.2f}', s),
                            'ratio_e': r['ratio_e'],
                            'an': r['an'],
                        })
        best_to_refine = sorted(best_to_refine, key=lambda x: abs(x['ratio_e'] - 1.0))[:5]

    for base in best_to_refine[:5]:
        k0, g0, s0 = base['k'][1], base['g_aa'][1], base['σ_at'][1]
        print(f'  Anchor: ({base["k"][0]}, {base["g_aa"][0]}, {base["σ_at"][0]}) '
              f'= ({k0:.4f}, {g0:.4f}, {s0:.4f}), α_e/α = {base["ratio_e"]:.4f}')
        # Scan k around k0
        best_local = base
        for dk in np.linspace(-0.2, 0.2, 41):
            k_test = k0 * (1 + dk)
            if k_test <= 0:
                continue
            r = evaluate(k_test, g0, s0)
            if r and not math.isnan(r['ratio_e']) and abs(r['ratio_e'] - 1.0) < abs(best_local['ratio_e'] - 1.0):
                best_local = {'k': (f'k×{1+dk:.3f}', k_test),
                              'g_aa': base['g_aa'], 'σ_at': base['σ_at'],
                              'ratio_e': r['ratio_e'], 'an': r['an']}
        print(f'    after k-scan: k = {best_local["k"][1]:.6f}, '
              f'α_e/α = {best_local["ratio_e"]:.6f}')

    # ── Summary ──
    print()
    print('=' * 80)
    print('  SUMMARY')
    print('=' * 80)
    print()
    print(f'  Total combinations tested: {n_combos}')
    print(f'  Strict matches (0.1%): {len(matches_strict)}')
    print(f'  Loose matches (1%):    {len(matches_loose)}')
    print(f'  5% matches:            {len(matches_5pct)}')
    print()
    if matches_strict:
        print('  CLEAN NATURAL-FORM MATCH FOUND.')
        m = matches_strict[0]
        print(f'    Best: k = {m["k"][0]}, g_aa = {m["g_aa"][0]}, σ_at = {m["σ_at"][0]}')
        print(f'    α_e/α = {m["ratio_e"]:.8f}')
    elif matches_loose:
        print('  Loose natural-form matches exist (within 1%)')
        print('  but no strict (0.1%) match.  R60 may start with these as targets')
        print('  for further refinement.')
    else:
        print('  No natural-form combination matches α to better than 5%.')
        print('  R60 should start with F54 numerical target (k ≈ 0.1, σ_at ≈ 0.5).')
    print()
    print('Track 3g complete.')


if __name__ == '__main__':
    main()
