"""
R59 Track 4: Metric synthesis — what knobs do we have, where, and what's used?

This script enumerates every metric coefficient R59 has considered
across Tracks 1–3e, and reports for each:

- Whether it is constrained by model-E (used for the particle
  spectrum)
- Whether R59 has assigned a value to it (and what value)
- Whether it conflicts with any other use

Output goes to stdout (this script) and to metric-terms.md (a
companion reference document written separately).

The "metric" we are talking about is the full extension R59
considered:

  10 dimensions (no ℵ): 6 Ma + 3 S + 1 t
  11 dimensions (with ℵ): 6 Ma + 3 S + 1 t + 1 ℵ

The 6 Ma dimensions decompose as 3 sheets × 2 (tube, ring):

  Index 0: e-tube       (electron sheet, tube circle)
  Index 1: e-ring       (electron sheet, ring circle)
  Index 2: ν-tube       (neutrino sheet, tube circle)
  Index 3: ν-ring       (neutrino sheet, ring circle)
  Index 4: p-tube       (proton sheet, tube circle)
  Index 5: p-ring       (proton sheet, ring circle)
  Index 6-8: S          (3D space, x/y/z)
  Index 9: t            (time)
  Index 10: ℵ           (sub-Planck dimension, optional)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np

from lib.metric import Metric
from lib.ma_model_d import (
    ALPHA, M_E_MEV, M_P_MEV, _TWO_PI_HC,
    solve_shear_for_alpha,
)

SQRT_ALPHA = math.sqrt(ALPHA)


def print_section(title):
    print()
    print('─' * 80)
    print(f'  {title}')
    print('─' * 80)
    print()


def main():
    print('=' * 80)
    print('R59 Track 4 — Metric synthesis: knobs, values, and constraints')
    print('=' * 80)

    # ── Section 1: model-E baseline ──
    print_section('Section 1: Model-E baseline values (the "consumed" knobs)')
    m = Metric.model_E()
    print(f'  Model-E aspect ratios (ε):')
    print(f'    ε_e = {m.eps[0]:.4f}     (electron sheet)')
    print(f'    ε_ν = {m.eps[1]:.4f}     (neutrino sheet)')
    print(f'    ε_p = {m.eps[2]:.4f}     (proton sheet, derived from α via R19)')
    print()
    print(f'  Internal shears (s) — set within each 2x2 sheet block:')
    print(f'    s_e = {m.shears[0]:.6f}   (e-tube ↔ e-ring, indices 0↔1)')
    print(f'    s_ν = {m.shears[1]:.6f}   (ν-tube ↔ ν-ring, indices 2↔3)')
    print(f'    s_p = {m.shears[2]:.6f}   (p-tube ↔ p-ring, indices 4↔5)')
    print()
    print(f'  Cross-sheet shears (model-E defaults):')
    print(f'    σ(3,4) = -0.18  (ν-ring ↔ p-tube)')
    print(f'    σ(3,5) = +0.10  (ν-ring ↔ p-ring)')
    print(f'  Other Ma-Ma off-diagonals: zero by default in model-E')
    print()
    print(f'  Ring circumferences (fm, derived):')
    print(f'    L_ring_e = {m.L_ring[0]:.4f}')
    print(f'    L_ring_ν = {m.L_ring[1]:.4e}')
    print(f'    L_ring_p = {m.L_ring[2]:.4f}')
    print()
    print(f'  These knobs are "consumed" — they are tuned to match observed')
    print(f'  particle masses and generation structure.  Changing them')
    print(f'  alters the particle spectrum.')

    # ── Section 2: R59 architecture knobs (S, t, ℵ blocks) ──
    print_section('Section 2: R59 architecture knobs (S, t, ℵ)')
    print('  S block (indices 6–8): identity (+1) — flat 3D space.')
    print('    Diagonal: g(S_x, S_x) = g(S_y, S_y) = g(S_z, S_z) = +1')
    print('    Off-diagonals within S: zero.  Always assumed.')
    print()
    print('  t (index 9): Lorentzian.')
    print('    Diagonal: g(t, t) = -1 (mostly-plus convention)')
    print('    F25 confirmed signature convention does not affect physics.')
    print()
    print('  ℵ (index 10, optional): Euclidean.')
    print('    Diagonal: g(ℵ, ℵ) = ASSUMED 1 throughout R59.')
    print('    F52 showed: no natural value of g(ℵ,ℵ) makes α emerge')
    print('    naturally at σ_ta = √α.  Treated as free parameter.')
    print()
    print('  S↔t off-diagonals (F40): kept zero — would introduce frame-')
    print('    dragging structure, not relevant to static Coulomb.')

    # ── Section 3: R59 coupling entries tested ──
    print_section('Section 3: Off-diagonal entries R59 tested for α coupling')

    print('  Direct Ma↔t (10D, no ℵ):')
    print('    Tested at: ring (Track 1, Arch 7) — preserved spectrum but')
    print('               failed spatial test (F35)')
    print('    Tested at: tube (Track 3 Arch 5/6) — broke spectrum on')
    print('               model-E')
    print('    Tested at: tube (Track 3d) — works on clean metric but caps')
    print('               at α_e/α ≈ 0.57 (F48)')
    print()
    print('  Ma↔ℵ + ℵ↔t (11D, ℵ in loop):')
    print('    Tested at: ring (Track 1b, Track 3b Part 5) — failed spatial')
    print('    Tested at: tube on model-E (Track 3b Part 6) — broke signature')
    print('    Tested at: tube on clean metric (Track 3b Part 7) — universal')
    print('               to floating-point precision; α matchable but only')
    print('               at non-natural values (F44, F50)')
    print()
    print('  Ma↔S direct (10D):')
    print('    Tested at: tube (Track 3 Arch 2) — broke signature')
    print('    Tested at: ring — not specifically tested but Arch-2 family')
    print('               failure suggests it would also fail')
    print()
    print('  Ma↔ℵ + ℵ↔S (11D, ℵ to S not t):')
    print('    Tested at: tube (Track 3 Arch 3) — broke signature on model-E')
    print('               on clean metric: not separately tested')
    print()
    print('  Mixed (tube↔ℵ + ring↔t):')
    print('    Tested (Track 3b Part 8, F43) — destroys universality')

    # ── Section 4: Constraint analysis ──
    print_section('Section 4: Constraint analysis — what is actually used?')
    print('  Entries USED by model-E (consumed):')
    print('    Diagonal Ma blocks (6 entries via L vector and ε ratios)')
    print('    Internal shears: s_e, s_ν, s_p (3 entries)')
    print('    Cross-sheet shears: σ(3,4), σ(3,5) (2 entries)')
    print('    Total: 11 model-E entries are "consumed"')
    print()
    print('  Entries R59 PROPOSED for α coupling:')
    print('    Direct Ma↔t (rings): 2 entries (Arch 7) — failed spatial')
    print('    Tube↔ℵ + ℵ↔t: 3 entries (2 tube↔ℵ + 1 ℵ↔t) — works')
    print('      on clean metric, fails on model-E (signature)')
    print('    g(ℵ,ℵ): 1 free entry — not derived')
    print()
    print('  CONFLICT — model-E\'s s_e blocks tube-based ℵ coupling on')
    print('    model-E (F41).  On a clean metric the architecture works')
    print('    but loses the particle spectrum.')

    # ── Section 5: What model-F would need to resolve ──
    print_section('Section 5: Open knobs for R60 / model-F')
    print('  Knobs available without disturbing the universality mechanism:')
    print('    - Aspect ratios ε_e, ε_ν, ε_p (could be tuned for spectrum)')
    print('    - Cross-sheet shears σ(i,j) for i,j on rings or in')
    print('      ring-only positions')
    print('    - ℵ scale g(ℵ,ℵ) — currently free, no natural derivation')
    print()
    print('  Knobs that conflict with tube-ℵ coupling:')
    print('    - Internal shears s_e, s_ν, s_p — saturate the tube row,')
    print('      blocking additional tube↔ℵ couplings')
    print('    - Any Ma↔Ma entry involving the tube of a sheet')
    print()
    print('  Open question for R60: can the particle spectrum be')
    print('  reproduced without internal shears?  If not, model-F needs')
    print('  a different α architecture than tube↔ℵ↔t.')

    print()
    print('=' * 80)
    print('  Track 4 complete.  See metric-terms.md for the full reference.')
    print('=' * 80)


if __name__ == '__main__':
    main()
