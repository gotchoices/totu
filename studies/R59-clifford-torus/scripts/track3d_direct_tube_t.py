"""
R59 Track 3d: Direct tube↔t on a clean metric (no ℵ).

The simplest possible architecture for α coupling: a single direct
off-diagonal between Ma_tube and t.  No ℵ.  No internal shears.
Tested on a "clean" metric where Ma is identity.

Question: is ℵ in the coupling loop or out?

If direct tube↔t at a natural σ value (e.g., √α, √(4πα), 1/(2π))
produces α_Coulomb = α, then ℵ is not needed for the coupling.
The architecture simplifies to 10D = 6 Ma + 3 S + 1 t with no
extra dimension.

If it doesn't (signature breaks, or required σ is unnatural), ℵ
stays in the loop as Track 3b/3c assumed.

Architecture: 10D metric
  - Ma:  identity (no shears, no cross entries)
  - S:   identity
  - t:   Lorentzian (-1)
  - Ma_e-tube ↔ t = +σ
  - Ma_p-tube ↔ t = -σ  (opposite sign for opposite charge)

For a mode with tube winding n_tube at rest in S:
  Q ≈ n_tube × σ × (-g^{tt}) = n_tube × σ
  α_Coulomb = Q²/(4π) = n_tube² × σ² / (4π)

For unit charge (|n_tube| = 1) to give α_Coulomb = α:
  σ² = 4πα
  σ = √(4πα) ≈ 0.303

That is a natural value (√(4π) × √α).  Whether the metric
remains positive-definite at σ ≈ 0.303 is the test.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np

ALPHA = 1.0 / 137.036
SQRT_ALPHA = math.sqrt(ALPHA)
SQRT_4PI_ALPHA = math.sqrt(4 * math.pi * ALPHA)

MODE_E = (1, 2, 0, 0, 0, 0)
MODE_P = (0, 0, -2, 2, 1, 3)

I_E_TUBE = 0
I_P_TUBE = 4
I_T = 9


def build_clean_metric_no_aleph(sigma):
    """10D metric: clean Ma + flat S + Lorentzian t.
    Tube↔t entries: ±σ for e/p."""
    G = np.zeros((10, 10))
    for i in range(6):
        G[i, i] = 1.0
    G[6, 6] = G[7, 7] = G[8, 8] = 1.0
    G[9, 9] = -1.0
    G[I_E_TUBE, I_T] = +sigma
    G[I_T, I_E_TUBE] = +sigma
    G[I_P_TUBE, I_T] = -sigma
    G[I_T, I_P_TUBE] = -sigma
    return G


def compute_Q_and_alpha(G, n6):
    """Extract source charge Q and α_Coulomb = Q²/(4π)."""
    try:
        G_inv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return float('nan'), float('nan')
    n_tilde = np.zeros(G.shape[0])
    n_tilde[:6] = np.asarray(n6, dtype=float)
    Q = float((n_tilde[:6] @ G_inv[:6, I_T]) * (-G_inv[I_T, I_T]))
    alpha = Q * Q / (4 * math.pi)
    return Q, alpha


def check_signature(G):
    eigs = np.linalg.eigvalsh(G)
    n_neg = int(np.sum(eigs < 0))
    return n_neg, (n_neg == 1), eigs


def main():
    print('=' * 80)
    print('R59 Track 3d — Direct tube↔t on a clean metric (no ℵ)')
    print('=' * 80)
    print()
    print(f'  α = {ALPHA:.10f}')
    print(f'  √α = {SQRT_ALPHA:.10f}')
    print(f'  √(4πα) = {SQRT_4PI_ALPHA:.10f}  ← predicted "natural" σ')
    print()
    print('  Architecture: 10D, no ℵ.  Clean Ma identity, tube↔t direct.')
    print('  Theory: α_Coulomb = σ²/(4π).  For α = 1/137, σ = √(4πα) ≈ 0.303.')
    print()

    # ── Section 1: Sweep σ around the predicted value ──
    print('─' * 80)
    print('  Section 1: Sweep σ to map α_Coulomb(σ)')
    print('─' * 80)
    print()
    print(f'  {"σ":>10s}  {"sig":>4s}  {"min eig":>11s}  {"Q_e":>14s}  '
          f'{"α_e/α":>11s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*10}  {"-"*4}  {"-"*11}  {"-"*14}  '
          f'{"-"*11}  {"-"*10}')

    # Span from 0 well past √(4πα), looking for where signature breaks
    sigma_values = np.concatenate([
        np.array([0.001, 0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.28]),
        np.linspace(0.29, 0.31, 11),
        np.array([0.32, 0.4, 0.5, 0.7, 0.9, 0.99, 1.0, 1.01, 1.1]),
    ])

    best = None
    for sigma in sigma_values:
        G = build_clean_metric_no_aleph(sigma)
        n_neg, sig_ok, eigs = check_signature(G)
        sig_str = 'YES' if sig_ok else 'no'
        if not sig_ok:
            print(f'  {sigma:10.4f}  {sig_str:>4s}  {eigs.min():11.4e}  '
                  f'{"—":>14s}  {"—":>11s}  {"—":>10s}')
            continue
        Q_e, alpha_e = compute_Q_and_alpha(G, MODE_E)
        Q_p, alpha_p = compute_Q_and_alpha(G, MODE_P)
        ratio_e = alpha_e / ALPHA
        ratio_ep = alpha_e / alpha_p if alpha_p != 0 else float('nan')
        marker = ''
        if abs(ratio_e - 1.0) < 0.005:
            marker = '   ← α match'
            if best is None or abs(ratio_e - 1.0) < abs(best['ratio_e'] - 1.0):
                best = {'sigma': sigma, 'ratio_e': ratio_e, 'Q_e': Q_e}
        print(f'  {sigma:10.4f}  {sig_str:>4s}  {eigs.min():11.4e}  '
              f'{Q_e:+14.6e}  {ratio_e:11.4e}  '
              f'{ratio_ep:10.6f}{marker}')

    print()
    if best:
        print(f'  Closest to α match: σ = {best["sigma"]:.4f}, '
              f'α_e/α = {best["ratio_e"]:.4f}')
        print(f'  σ / √(4πα) = {best["sigma"] / SQRT_4PI_ALPHA:.6f}')

    # ── Section 2: Test natural candidates explicitly ──
    print()
    print('─' * 80)
    print('  Section 2: Natural σ candidates')
    print('─' * 80)
    print()
    print(f'  {"Name":>20s}  {"σ value":>11s}  {"sig":>4s}  '
          f'{"α_e/α":>11s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*20}  {"-"*11}  {"-"*4}  '
          f'{"-"*11}  {"-"*10}')

    candidates = [
        ('√α', SQRT_ALPHA),
        ('α', ALPHA),
        ('√(4πα) [predicted]', SQRT_4PI_ALPHA),
        ('1/(2π)', 1/(2*math.pi)),
        ('1/π', 1/math.pi),
        ('1/√(2π)', 1/math.sqrt(2*math.pi)),
        ('1/2', 0.5),
        ('1', 1.0),
    ]
    for name, sigma in candidates:
        G = build_clean_metric_no_aleph(sigma)
        n_neg, sig_ok, eigs = check_signature(G)
        if not sig_ok:
            print(f'  {name:>20s}  {sigma:11.6f}  {"no":>4s}  '
                  f'{"—":>11s}  {"—":>10s}')
            continue
        Q_e, alpha_e = compute_Q_and_alpha(G, MODE_E)
        Q_p, alpha_p = compute_Q_and_alpha(G, MODE_P)
        ratio_e = alpha_e / ALPHA
        ratio_ep = alpha_e / alpha_p if alpha_p != 0 else float('nan')
        print(f'  {name:>20s}  {sigma:11.6f}  {"YES":>4s}  '
              f'{ratio_e:11.4e}  {ratio_ep:10.6f}')

    # ── Section 3: Find the signature boundary ──
    print()
    print('─' * 80)
    print('  Section 3: Where does signature break?')
    print('─' * 80)
    print()
    print('  Fine sweep near the boundary identified in Section 1.')
    print()
    print(f'  {"σ":>10s}  {"sig":>4s}  {"min eig":>11s}  '
          f'{"Q_e":>14s}  {"α_e/α":>11s}')
    print(f'  {"-"*10}  {"-"*4}  {"-"*11}  '
          f'{"-"*14}  {"-"*11}')
    for sigma in np.linspace(0.95, 1.05, 21):
        G = build_clean_metric_no_aleph(sigma)
        n_neg, sig_ok, eigs = check_signature(G)
        sig_str = 'YES' if sig_ok else 'no'
        if sig_ok:
            Q_e, alpha_e = compute_Q_and_alpha(G, MODE_E)
            print(f'  {sigma:10.4f}  {sig_str:>4s}  {eigs.min():11.4e}  '
                  f'{Q_e:+14.6e}  {alpha_e/ALPHA:11.4e}')
        else:
            print(f'  {sigma:10.4f}  {sig_str:>4s}  {eigs.min():11.4e}  '
                  f'{"—":>14s}  {"—":>11s}')

    # ── Summary ──
    print()
    print('=' * 80)
    print('  SUMMARY')
    print('=' * 80)
    print()
    print('  Theory predicts σ = √(4πα) ≈ 0.303 should give exact α.')
    print('  Test: does the metric remain physical at that σ?')
    print()
    print('  Implications:')
    print('    - If signature OK and α_e/α = 1 at σ = √(4πα): ℵ is OUT.')
    print('      Direct tube↔t at a natural value gives observed α.')
    print('    - If signature breaks before σ = √(4πα): ℵ stays IN.')
    print('      Direct architecture cannot reach α; mediation needed.')
    print('    - If signature OK but α_e/α ≠ 1: extraction may be wrong;')
    print('      revisit the Q formula.')
    print()
    print('Track 3d complete.')


if __name__ == '__main__':
    main()
