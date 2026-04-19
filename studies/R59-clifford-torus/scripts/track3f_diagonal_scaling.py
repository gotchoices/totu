"""
R59 Track 3f: Does scaling Ma sheet diagonals make α emerge naturally?

Tracks 3b–3e found that tube↔ℵ↔t gives exact universality but the
α magnitude requires unnatural fine-tuning of σ_ta or g_aa near the
PD boundary.  All those tests held the Ma diagonals fixed at the
dimensionless identity (1) inherited from the model-E normalization.

The Ma diagonals are not derived from physics — they're calibrated
to particle masses.  Their values may simply be the wrong "scale"
for the architecture to produce α naturally.

This track tests: with the architecture at natural σ values, can
we produce α_Coulomb = α by scaling the Ma sheet diagonals?

Architecture:
  - 11D: clean Ma block + ℵ + S + Lorentzian t
  - Each sheet diagonal block scaled by k_e, k_p, k_ν
  - tube↔ℵ entries: +√α for e-tube, −√α for p-tube
    (ν-tube NOT coupled — neutrinos are electrically neutral)
  - ℵ↔t entry: σ_at (free)
  - g(ℵ,ℵ): g_aa (free)

Targets:
  - α_Coulomb(electron) = α
  - α_Coulomb(proton) = α (= α_e by structural universality)
  - α_Coulomb(neutrino) ≈ 0 (charge neutrality)

Knobs (5):
  k_e, k_p, k_ν, g_aa, σ_at

Goal: find a (preferably "natural-looking") configuration of the
knobs that hits all three targets.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from itertools import product

ALPHA = 1.0 / 137.036
SQRT_ALPHA = math.sqrt(ALPHA)

# Mode definitions (from model-E)
MODE_E = (1, 2, 0, 0, 0, 0)
MODE_P = (0, 0, -2, 2, 1, 3)
MODE_NU = (0, 0, 1, 1, 0, 0)  # ν₁ — has ν-sheet windings only

# New ordering: ℵ=0, p_t=1, p_r=2, e_t=3, e_r=4, ν_t=5, ν_r=6, S=7-9, t=10
# But for backward compatibility with mode tuples, we map 6-tuple modes
# (in OLD order: e_t, e_r, ν_t, ν_r, p_t, p_r) onto rows of the new metric.

# Old → new index mapping for Ma rows:
OLD_TO_NEW = {0: 3, 1: 4, 2: 5, 3: 6, 4: 1, 5: 2}

I_ALEPH = 0
I_P_TUBE = 1
I_P_RING = 2
I_E_TUBE = 3
I_E_RING = 4
I_NU_TUBE = 5
I_NU_RING = 6
I_T = 10


def build_metric(k_e, k_p, k_nu, g_aa, sigma_at, sigma_ta=SQRT_ALPHA):
    """
    Build the 11D metric in NEW ordering with sheet-diagonal scaling.

    Architecture:
      - ℵ at index 0 with diagonal g_aa
      - p-sheet (1, 2): diagonal k_p, no internal shear (clean)
      - e-sheet (3, 4): diagonal k_e, no internal shear
      - ν-sheet (5, 6): diagonal k_nu, no internal shear
      - S (7-9): identity
      - t (10): -1
      - Off-diagonals:
          (0, 1) = -sigma_ta  (p-tube ↔ ℵ, paired)
          (0, 3) = +sigma_ta  (e-tube ↔ ℵ)
          (0, 5) = 0          (ν-tube NOT coupled)
          (0, 10) = sigma_at  (ℵ ↔ t)
    """
    G = np.zeros((11, 11))
    G[0, 0] = g_aa
    G[1, 1] = k_p   # p_t
    G[2, 2] = k_p   # p_r
    G[3, 3] = k_e   # e_t
    G[4, 4] = k_e   # e_r
    G[5, 5] = k_nu  # ν_t
    G[6, 6] = k_nu  # ν_r
    G[7, 7] = G[8, 8] = G[9, 9] = 1.0  # S
    G[I_T, I_T] = -1.0

    # tube↔ℵ
    G[I_ALEPH, I_E_TUBE] = +sigma_ta
    G[I_E_TUBE, I_ALEPH] = +sigma_ta
    G[I_ALEPH, I_P_TUBE] = -sigma_ta
    G[I_P_TUBE, I_ALEPH] = -sigma_ta
    # ν-tube NOT coupled

    # ℵ↔t
    G[I_ALEPH, I_T] = sigma_at
    G[I_T, I_ALEPH] = sigma_at

    return G


def map_mode_to_new(n_old):
    """Map a 6-tuple mode (OLD ordering: e_t,e_r,ν_t,ν_r,p_t,p_r) to
    a winding vector in NEW ordering (slots 1-6 in 11D)."""
    n_new = np.zeros(11)
    for old_i, n in enumerate(n_old):
        new_i = OLD_TO_NEW[old_i]
        n_new[new_i] = n
    return n_new


def compute_alpha_coulomb(G, n_new):
    """Q = (n · g^{Ma,t}) × (-g^{tt}); α = Q²/(4π)."""
    try:
        G_inv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return float('nan'), float('nan')
    # Ma rows are 1-6 in the new ordering
    Q = float((n_new[1:7] @ G_inv[1:7, I_T]) * (-G_inv[I_T, I_T]))
    alpha = Q * Q / (4 * math.pi)
    return Q, alpha


def check_signature(G):
    eigs = np.linalg.eigvalsh(G)
    n_neg = int(np.sum(eigs < 0))
    return (n_neg == 1), n_neg


def evaluate(k_e, k_p, k_nu, g_aa, sigma_at, sigma_ta=SQRT_ALPHA):
    """Evaluate one configuration; return (sig_ok, α_e/α, α_p/α, α_ν/α)."""
    G = build_metric(k_e, k_p, k_nu, g_aa, sigma_at, sigma_ta)
    sig_ok, _ = check_signature(G)
    if not sig_ok:
        return False, np.nan, np.nan, np.nan
    n_e = map_mode_to_new(MODE_E)
    n_p = map_mode_to_new(MODE_P)
    n_nu = map_mode_to_new(MODE_NU)
    _, alpha_e = compute_alpha_coulomb(G, n_e)
    _, alpha_p = compute_alpha_coulomb(G, n_p)
    _, alpha_nu = compute_alpha_coulomb(G, n_nu)
    return True, alpha_e/ALPHA, alpha_p/ALPHA, alpha_nu/ALPHA


def main():
    print('=' * 80)
    print('R59 Track 3f — Does scaling Ma diagonals produce α naturally?')
    print('=' * 80)
    print()
    print(f'  α = {ALPHA:.10f}')
    print(f'  √α = {SQRT_ALPHA:.10f}')
    print()
    print('  Architecture: clean Ma + ℵ + S + t, tube↔ℵ at ±√α, ℵ↔t = σ_at')
    print('  Knobs: k_e, k_p, k_ν (Ma diagonal scales), g_aa, σ_at')
    print('  Targets: α_e = α_p = α (charged), α_ν ≈ 0 (neutral)')
    print()

    # ── Section 0: Reference baseline (all diagonals = 1) ──
    print('─' * 80)
    print('  Section 0: Baseline (k_e = k_p = k_ν = g_aa = 1, σ_at = 1)')
    print('─' * 80)
    print()
    sig_ok, ae, ap, an = evaluate(1.0, 1.0, 1.0, 1.0, 1.0)
    print(f'  sig OK: {sig_ok}')
    print(f'  α_e/α = {ae:.6f}')
    print(f'  α_p/α = {ap:.6f}')
    print(f'  α_ν/α = {an:.6f}')
    print(f'  Universality (α_e/α_p): {ae/ap if ap else "—"}')
    print()

    # ── Section 1: Vary k_e and k_p uniformly (k_e = k_p = k) ──
    print('─' * 80)
    print('  Section 1: Vary k_e = k_p = k (uniform charged-sheet scale)')
    print('─' * 80)
    print('  k_ν = 1, g_aa = 1, σ_at = 1')
    print()
    print(f'  {"k":>10s}  {"sig":>4s}  {"α_e/α":>10s}  {"α_p/α":>10s}  '
          f'{"α_ν/α":>10s}')
    print(f'  {"-"*10}  {"-"*4}  {"-"*10}  {"-"*10}  {"-"*10}')
    for k in [0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 10.0, 100.0]:
        sig_ok, ae, ap, an = evaluate(k, k, 1.0, 1.0, 1.0)
        sig_str = 'YES' if sig_ok else 'no'
        if sig_ok:
            print(f'  {k:10.4f}  {sig_str:>4s}  {ae:10.4e}  '
                  f'{ap:10.4e}  {an:10.4e}')
        else:
            print(f'  {k:10.4f}  {sig_str:>4s}  {"—":>10s}  '
                  f'{"—":>10s}  {"—":>10s}')

    # ── Section 2: Vary k_e and k_p independently (find ratio that helps) ──
    print()
    print('─' * 80)
    print('  Section 2: Independent k_e and k_p (does asymmetric scaling help?)')
    print('─' * 80)
    print('  k_ν = 1, g_aa = 1, σ_at = 1')
    print()
    print(f'  {"k_e":>8s}  {"k_p":>8s}  {"sig":>4s}  {"α_e/α":>10s}  '
          f'{"α_p/α":>10s}  {"α_e/α_p":>10s}')
    print(f'  {"-"*8}  {"-"*8}  {"-"*4}  {"-"*10}  '
          f'{"-"*10}  {"-"*10}')
    for k_e in [0.01, 0.1, 1.0, 10.0]:
        for k_p in [0.01, 0.1, 1.0, 10.0]:
            sig_ok, ae, ap, an = evaluate(k_e, k_p, 1.0, 1.0, 1.0)
            if sig_ok:
                ratio = ae/ap if ap else float('nan')
                print(f'  {k_e:8.4f}  {k_p:8.4f}  {"YES":>4s}  '
                      f'{ae:10.4e}  {ap:10.4e}  {ratio:10.4f}')
            else:
                print(f'  {k_e:8.4f}  {k_p:8.4f}  {"no":>4s}  '
                      f'{"—":>10s}  {"—":>10s}  {"—":>10s}')

    # ── Section 3: 4D scan to find α_e/α = 1 with universality ──
    print()
    print('─' * 80)
    print('  Section 3: 4D scan — search for α_Coulomb = α with universality')
    print('─' * 80)
    print()

    matches = []
    k_grid = [0.01, 0.05, 0.1, 0.5, 1.0]
    g_grid = [0.01, 0.1, 1.0, 10.0]
    sat_grid = [0.01, 0.1, 0.5, 1.0, 5.0, 10.0]

    print(f'  Searching k_e × k_p × g_aa × σ_at grid')
    print(f'  ({len(k_grid)} × {len(k_grid)} × {len(g_grid)} × {len(sat_grid)} '
          f'= {len(k_grid)**2 * len(g_grid) * len(sat_grid)} configs)...')

    for k_e, k_p, g_aa, sat in product(k_grid, k_grid, g_grid, sat_grid):
        sig_ok, ae, ap, an = evaluate(k_e, k_p, 1.0, g_aa, sat)
        if not sig_ok:
            continue
        if abs(ae - 1.0) < 0.05:  # within 5% of α
            uni_ok = abs(ae/ap - 1.0) < 0.01
            nu_ok = abs(an) < 0.05
            matches.append({
                'k_e': k_e, 'k_p': k_p, 'g_aa': g_aa, 'sat': sat,
                'ae': ae, 'ap': ap, 'an': an,
                'uni_ok': uni_ok, 'nu_ok': nu_ok,
            })

    print(f'  Found {len(matches)} configs with α_e/α within 5%.')
    print()
    if matches:
        print(f'  {"k_e":>8s}  {"k_p":>8s}  {"g_aa":>8s}  {"σ_at":>8s}  '
              f'{"α_e/α":>10s}  {"α_p/α":>10s}  {"α_ν/α":>10s}  {"uni":>4s}  '
              f'{"ν=0":>4s}')
        print(f'  {"-"*8}  {"-"*8}  {"-"*8}  {"-"*8}  '
              f'{"-"*10}  {"-"*10}  {"-"*10}  {"-"*4}  {"-"*4}')
        # Sort by closest to α and most natural
        matches.sort(key=lambda m: abs(m['ae'] - 1.0))
        for m in matches[:20]:
            uni = 'YES' if m['uni_ok'] else 'no'
            nu = 'YES' if m['nu_ok'] else 'no'
            print(f'  {m["k_e"]:8.4f}  {m["k_p"]:8.4f}  {m["g_aa"]:8.4f}  '
                  f'{m["sat"]:8.4f}  {m["ae"]:10.4f}  {m["ap"]:10.4f}  '
                  f'{m["an"]:10.4e}  {uni:>4s}  {nu:>4s}')

    # ── Section 4: Test natural candidate combinations ──
    print()
    print('─' * 80)
    print('  Section 4: Hand-picked natural candidates')
    print('─' * 80)
    print()
    candidates = [
        ('all 1', 1.0, 1.0, 1.0, 1.0, 1.0),
        ('k = α', ALPHA, ALPHA, ALPHA, 1.0, 1.0),
        ('k = √α', SQRT_ALPHA, SQRT_ALPHA, SQRT_ALPHA, 1.0, 1.0),
        ('k = 4πα', 4*math.pi*ALPHA, 4*math.pi*ALPHA, 4*math.pi*ALPHA, 1.0, 1.0),
        ('k = α, g_aa = α', ALPHA, ALPHA, ALPHA, ALPHA, 1.0),
        ('k = α, σ_at = α', ALPHA, ALPHA, ALPHA, 1.0, ALPHA),
        ('k = α, σ_at = 1/α', ALPHA, ALPHA, ALPHA, 1.0, 1/ALPHA),
        ('k_charged = α, k_ν = 1', ALPHA, ALPHA, 1.0, 1.0, 1.0),
        ('k_charged = √α, k_ν = 1', SQRT_ALPHA, SQRT_ALPHA, 1.0, 1.0, 1.0),
        ('all = 1/(4π)', 1/(4*math.pi), 1/(4*math.pi), 1/(4*math.pi), 1.0, 1.0),
        ('k = 1, g_aa = α, σ_at = 1/√α',
         1.0, 1.0, 1.0, ALPHA, 1/SQRT_ALPHA),
    ]
    print(f'  {"Description":>30s}  {"α_e/α":>10s}  {"α_p/α":>10s}  '
          f'{"α_ν/α":>10s}  {"uni":>4s}')
    print(f'  {"-"*30}  {"-"*10}  {"-"*10}  {"-"*10}  {"-"*4}')
    for name, ke, kp, kn, gaa, sat in candidates:
        sig_ok, ae, ap, an = evaluate(ke, kp, kn, gaa, sat)
        if sig_ok:
            uni = 'YES' if abs(ae/ap - 1.0) < 0.01 else 'no'
            print(f'  {name:>30s}  {ae:10.4f}  {ap:10.4f}  '
                  f'{an:10.4e}  {uni:>4s}')
        else:
            print(f'  {name:>30s}  {"no sig":>10s}  {"":>10s}  '
                  f'{"":>10s}  {"":>4s}')

    # ── Summary ──
    print()
    print('=' * 80)
    print('  SUMMARY')
    print('=' * 80)
    print()
    print('  Question: can sheet-diagonal scaling produce α_Coulomb = α at')
    print('  natural σ values?')
    print()
    print('  Section 0: baseline gives α_e/α = some value; report below.')
    print('  Section 3: comprehensive scan results.')
    print('  Section 4: tests of "natural" combinations.')
    print()
    print('  Universality (α_e/α_p = 1.000) should be exact at every')
    print('  signature-OK point — confirms F45 structural result.')
    print()
    print('  ν-sheet (uncoupled tube) should give α_ν ≈ 0 — confirms')
    print('  charge-neutrality.')
    print()
    print('Track 3f complete.')


if __name__ == '__main__':
    main()
