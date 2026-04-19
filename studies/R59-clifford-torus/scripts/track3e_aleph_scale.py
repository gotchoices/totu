"""
R59 Track 3e: Solve for the natural ℵ scale.

Track 3d showed that direct tube↔t on a clean metric (no ℵ) cannot
reach observed α — the coupling ceiling is ~0.57α.  ℵ stays in
the coupling loop.

Track 3c showed that with σ_ta = √α and σ_at = 1, g(ℵ,ℵ) = 1, the
result is only 0.005α.  The "α match" requires σ_ta ≈ 0.785 near
the PD boundary.

This track inverts the question: what if we FIX σ_ta = √α as the
natural value, and SOLVE for the g(ℵ,ℵ) and σ_at that produce
α_Coulomb = α?  The diagonal g(ℵ,ℵ) was assumed = 1 throughout
R59 but never derived.  Treating it as a derived quantity:

- If a natural (g, σ_at) combination produces observed α at
  σ_ta = √α, then g(ℵ,ℵ) is a derived constant of MaSt and we've
  learned its value.
- If the combination is arbitrary, we've at least pinned the
  numerical relationship needed.

Architecture: 11D, clean Ma identity, tube↔ℵ + ℵ↔t.

  σ_ta = √α   (FIXED at natural value)
  σ_at = ?     (variable)
  g(ℵ,ℵ) = ?   (variable)

For each combination, compute α_Coulomb and find the match.

Then ask: does the matching point take a natural form?  Candidates
for g(ℵ,ℵ):
  - 1   (assumed throughout R59)
  - α   (one factor of α from the underlying coupling)
  - α²  (two factors)
  - 1/(4π)
  - 4π × α
  - (L_P / L_Compton)²  ≈ 4 × 10⁻⁴⁰  (standard KK relation)
  - α/(4π)
  - whatever the data gives
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np

ALPHA = 1.0 / 137.036
SQRT_ALPHA = math.sqrt(ALPHA)
FOUR_PI_ALPHA = 4 * math.pi * ALPHA
SQRT_4PI_ALPHA = math.sqrt(FOUR_PI_ALPHA)

MODE_E = (1, 2, 0, 0, 0, 0)
MODE_P = (0, 0, -2, 2, 1, 3)

I_E_TUBE = 0
I_P_TUBE = 4
I_T = 9
I_ALEPH = 10


def build_metric(sigma_ta, sigma_at, g_aa):
    """11D, clean Ma + ℵ + tube↔ℵ + ℵ↔t."""
    G = np.zeros((11, 11))
    for i in range(6):
        G[i, i] = 1.0
    G[6, 6] = G[7, 7] = G[8, 8] = 1.0
    G[9, 9] = -1.0
    G[I_ALEPH, I_ALEPH] = g_aa
    G[I_E_TUBE, I_ALEPH] = +sigma_ta
    G[I_ALEPH, I_E_TUBE] = +sigma_ta
    G[I_P_TUBE, I_ALEPH] = -sigma_ta
    G[I_ALEPH, I_P_TUBE] = -sigma_ta
    G[I_ALEPH, I_T] = sigma_at
    G[I_T, I_ALEPH] = sigma_at
    return G


def compute_Q(G, n6):
    try:
        G_inv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return float('nan')
    n_tilde = np.zeros(G.shape[0])
    n_tilde[:6] = np.asarray(n6, dtype=float)
    return float((n_tilde[:6] @ G_inv[:6, I_T]) * (-G_inv[I_T, I_T]))


def alpha_coulomb(G, n6):
    Q = compute_Q(G, n6)
    return Q * Q / (4 * math.pi)


def check_signature(G):
    eigs = np.linalg.eigvalsh(G)
    n_neg = int(np.sum(eigs < 0))
    return n_neg, (n_neg == 1)


def main():
    print('=' * 80)
    print('R59 Track 3e — Solve for the natural ℵ scale')
    print('=' * 80)
    print()
    print(f'  α = {ALPHA:.10f}')
    print(f'  √α = {SQRT_ALPHA:.10f}')
    print(f'  4πα = {FOUR_PI_ALPHA:.10f}')
    print()
    print('  Architecture: 11D clean Ma + tube↔ℵ + ℵ↔t')
    print('  Fixed: σ_ta = √α  (natural)')
    print('  Variable: σ_at, g(ℵ,ℵ)')
    print()
    print('  Goal: find (σ_at, g_aa) such that α_Coulomb = α at σ_ta = √α.')
    print()

    # ── Section 1: 1D scan in σ_at at g_aa = 1 ──
    print('─' * 80)
    print('  Section 1: Vary σ_at at g_aa = 1 (find σ_at that hits α)')
    print('─' * 80)
    print()
    print(f'  {"σ_at":>10s}  {"sig":>4s}  {"α_e/α":>11s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*10}  {"-"*4}  {"-"*11}  {"-"*10}')

    sigma_at_grid = np.concatenate([
        np.array([0.1, 0.5, 1.0, 2.0, 5.0]),
        np.linspace(10, 30, 21),
        np.array([50, 100]),
    ])
    best_sigma_at = None
    for s_at in sigma_at_grid:
        G = build_metric(SQRT_ALPHA, s_at, 1.0)
        _, sig_ok = check_signature(G)
        if not sig_ok:
            print(f'  {s_at:10.4f}  {"no":>4s}  {"—":>11s}  {"—":>10s}')
            continue
        ae = alpha_coulomb(G, MODE_E)
        ap = alpha_coulomb(G, MODE_P)
        ratio_e = ae / ALPHA
        ratio_ep = ae / ap if ap != 0 else float('nan')
        marker = '   ← α match' if abs(ratio_e - 1.0) < 0.005 else ''
        if abs(ratio_e - 1.0) < 0.005:
            if best_sigma_at is None or abs(ratio_e - 1.0) < abs(best_sigma_at['ratio'] - 1.0):
                best_sigma_at = {'s_at': s_at, 'ratio': ratio_e}
        print(f'  {s_at:10.4f}  {"YES":>4s}  {ratio_e:11.4e}  '
              f'{ratio_ep:10.6f}{marker}')

    if best_sigma_at:
        print()
        print(f'  Best σ_at = {best_sigma_at["s_at"]:.4f}, '
              f'α_e/α = {best_sigma_at["ratio"]:.4f}')

    # ── Section 2: 1D scan in g_aa at σ_at = 1 ──
    print()
    print('─' * 80)
    print('  Section 2: Vary g_aa at σ_at = 1 (find g_aa that hits α)')
    print('─' * 80)
    print()
    print(f'  {"g_aa":>14s}  {"sig":>4s}  {"α_e/α":>11s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*14}  {"-"*4}  {"-"*11}  {"-"*10}')

    g_aa_grid = np.concatenate([
        np.array([1e-4, 1e-3]),
        np.logspace(-3, -1, 13),
        np.array([0.15, 0.2, 0.3, 0.5, 1.0]),
    ])
    best_g_aa = None
    for g_aa in g_aa_grid:
        G = build_metric(SQRT_ALPHA, 1.0, g_aa)
        _, sig_ok = check_signature(G)
        if not sig_ok:
            print(f'  {g_aa:14.6e}  {"no":>4s}  {"—":>11s}  {"—":>10s}')
            continue
        ae = alpha_coulomb(G, MODE_E)
        ap = alpha_coulomb(G, MODE_P)
        ratio_e = ae / ALPHA
        ratio_ep = ae / ap if ap != 0 else float('nan')
        marker = '   ← α match' if abs(ratio_e - 1.0) < 0.005 else ''
        if abs(ratio_e - 1.0) < 0.005:
            if best_g_aa is None or abs(ratio_e - 1.0) < abs(best_g_aa['ratio'] - 1.0):
                best_g_aa = {'g_aa': g_aa, 'ratio': ratio_e}
        print(f'  {g_aa:14.6e}  {"YES":>4s}  {ratio_e:11.4e}  '
              f'{ratio_ep:10.6f}{marker}')

    if best_g_aa:
        print()
        print(f'  Best g_aa = {best_g_aa["g_aa"]:.6e}, '
              f'α_e/α = {best_g_aa["ratio"]:.4f}')

    # ── Section 3: Fine-tune to find the exact match ──
    print()
    print('─' * 80)
    print('  Section 3: Bisect to find exact g_aa for α_Coulomb = α (σ_at = 1)')
    print('─' * 80)
    print()

    # Bisection in log(g_aa)
    def alpha_e_at(log_g_aa):
        g = math.exp(log_g_aa)
        G = build_metric(SQRT_ALPHA, 1.0, g)
        _, sig_ok = check_signature(G)
        if not sig_ok:
            return float('inf')
        return alpha_coulomb(G, MODE_E) / ALPHA

    # From section 2: small g_aa amplifies, large g_aa suppresses.
    # Find a bracket.
    log_lo, log_hi = math.log(1e-4), math.log(1.0)
    val_lo = alpha_e_at(log_lo)
    val_hi = alpha_e_at(log_hi)
    print(f'  Bracket: g_aa ∈ [{math.exp(log_lo):.2e}, {math.exp(log_hi):.2f}]')
    print(f'    α_e/α at bracket ends: {val_lo:.4e}, {val_hi:.4e}')

    if (val_lo - 1) * (val_hi - 1) < 0:
        # Bracketed
        for _ in range(50):
            log_mid = (log_lo + log_hi) / 2
            val_mid = alpha_e_at(log_mid)
            if abs(val_mid - 1) < 1e-6:
                break
            if (val_lo - 1) * (val_mid - 1) < 0:
                log_hi, val_hi = log_mid, val_mid
            else:
                log_lo, val_lo = log_mid, val_mid
        g_aa_match = math.exp(log_mid)
        print(f'  Bisection converged: g_aa = {g_aa_match:.10f}')
        print(f'    α_e/α = {val_mid:.8f}')
        print()
        print(f'  Compare g_aa to natural candidates:')
        print(f'    g_aa = {g_aa_match:.6e}')
        print(f'    α   = {ALPHA:.6e}    ratio: {g_aa_match/ALPHA:.6f}')
        print(f'    α²  = {ALPHA**2:.6e}    ratio: {g_aa_match/ALPHA**2:.6f}')
        print(f'    α/(4π) = {ALPHA/(4*math.pi):.6e}    '
              f'ratio: {g_aa_match/(ALPHA/(4*math.pi)):.6f}')
        print(f'    1/(4π) = {1/(4*math.pi):.6e}    '
              f'ratio: {g_aa_match/(1/(4*math.pi)):.6f}')
        print(f'    4πα = {FOUR_PI_ALPHA:.6e}    '
              f'ratio: {g_aa_match/FOUR_PI_ALPHA:.6f}')
        print(f'    1/(4π·α) = {1/FOUR_PI_ALPHA:.6e}    '
              f'ratio: {g_aa_match/(1/FOUR_PI_ALPHA):.6f}')
    else:
        print('  Could not bracket — both endpoints on same side of α.')

    # ── Section 4: 2D scan to map the α=α contour ──
    print()
    print('─' * 80)
    print('  Section 4: Map the α_Coulomb = α contour in (σ_at, g_aa) space')
    print('─' * 80)
    print()
    print('  For σ_ta = √α (fixed), find all (σ_at, g_aa) combinations')
    print('  giving α_Coulomb = α to within 1%.')
    print()

    contour = []
    for log_g in np.linspace(-6, 0, 30):
        g = math.exp(log_g)
        # For each g, scan σ_at to find where α_e/α = 1
        for s_at in np.logspace(-2, 2, 50):
            G = build_metric(SQRT_ALPHA, s_at, g)
            _, sig_ok = check_signature(G)
            if not sig_ok:
                continue
            ratio = alpha_coulomb(G, MODE_E) / ALPHA
            if abs(ratio - 1.0) < 0.01:
                contour.append({'g_aa': g, 's_at': s_at, 'ratio': ratio})
                break  # first match per g

    print(f'  Found {len(contour)} contour points.  Sample:')
    print()
    print(f'  {"g_aa":>12s}  {"σ_at":>10s}  {"α_e/α":>10s}  '
          f'{"σ_at × √g_aa":>14s}')
    print(f'  {"-"*12}  {"-"*10}  {"-"*10}  {"-"*14}')
    for c in contour[::max(1, len(contour)//12)]:
        product = c['s_at'] * math.sqrt(c['g_aa'])
        print(f'  {c["g_aa"]:12.4e}  {c["s_at"]:10.4f}  '
              f'{c["ratio"]:10.6f}  {product:14.6f}')

    if contour:
        print()
        print('  Pattern check: does σ_at × √g_aa stay constant along the contour?')
        products = [c['s_at'] * math.sqrt(c['g_aa']) for c in contour]
        print(f'    σ_at × √g_aa: min = {min(products):.4f}, '
              f'max = {max(products):.4f}, mean = {np.mean(products):.4f}')
        print(f'    Compare to: √(4π) = {math.sqrt(4*math.pi):.4f}, '
              f'1/√α = {1/SQRT_ALPHA:.4f}')

    # ── Summary ──
    print()
    print('=' * 80)
    print('  SUMMARY')
    print('=' * 80)
    print()
    print('  Question: at fixed σ_ta = √α, what (σ_at, g_aa) gives α_Coulomb = α?')
    print()
    print('  Section 3 reports the bisected g_aa value (with σ_at = 1).')
    print('  Section 4 maps the contour and tests for a hidden constant.')
    print()
    print('  Interpretation:')
    print('    - If g_aa takes a natural value: ℵ has a definite scale we have')
    print('      now derived.  Worth carrying to R60.')
    print('    - If σ_at × √g_aa = constant along the contour: only one')
    print('      degree of freedom is real; the system is over-parameterized.')
    print('    - If everything looks arbitrary: tube↔ℵ↔t can be tuned to α')
    print('      but the tuning requires unmotivated values.')
    print()
    print('Track 3e complete.')


if __name__ == '__main__':
    main()
