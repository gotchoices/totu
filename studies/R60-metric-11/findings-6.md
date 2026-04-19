# R60 Track 6: Joint e+p+ν solver

**Scope.**  Add the ν-sheet on the same architectural footing as
e and p (sign_nu = +1, full σ_ta coupling).  Joint solve for six
free knobs (L_x, k_x for each sheet) against six targets (three
masses, three α_x = α).  Test against R61's top-4 candidate ν
geometries.

Script: [scripts/track6_three_sheet_solve.py](scripts/track6_three_sheet_solve.py).

### Review of variables

- **sign_nu = +1**: same convention as electron (R55-consistent).
  Activates the ν-tube↔ℵ entry at +√α.
- **Wide k bounds (10⁻⁶ to 10⁶)**: per the user observation that
  physical sheet ring scales span L_p ~ fm to L_ν ~ μm to mm,
  per-sheet diagonal scales should be allowed to span similarly
  wide ranges without being treated as "unnatural."
- **R61 candidates**: top-ranked ν-sheet geometries from R61's
  taxonomy, each specifying (ε_ν, s_ν) and a triplet of mode
  assignments for ν₁, ν₂, ν₃.

### F27. Smoke check — three-sheet metric is well-posed at defaults

Built the 11D metric with Track 5 baseline (e: ε=1, s=0; p: ε=1,
s=0) plus R61 #1 ν-sheet (ε=2, s=0.022) at uncalibrated R59 F59
defaults (k = 1/(8π) for all three sheets):

- **Signature OK** — exactly one negative eigenvalue (the t
  direction).  No structural breakage from adding the ν-sheet.
- Masses come out at targets by construction (L_ring derived
  from each mass at uniform k = 1/(8π)).
- α_e/α = α_p/α = 1.943 — universality between e and p exact,
  but magnitude inflated by ~94% above target.  This is
  expected because k = 1/(8π) was tuned for two-sheet e+p, not
  three-sheet.
- α_ν₁/α = 1.78 — close to e/p value, signaling that the
  three-sheet system needs joint retuning (not a structural
  problem).
- L_ring scales: L_ring_e = 27,200 fm, L_ring_p = 21 fm,
  L_ring_ν = 2.1 × 10¹¹ fm = 0.21 mm.  Span of ~10¹⁰ fm
  between proton and neutrino — consistent with the user's
  physical-scale intuition.

### F28. Phase 1 — R61 #1 converges cleanly with universal α = α

Joint solve at R61 candidate #1: triplet `(+1,+1)(-1,+1)(+1,+2)`,
ε_ν = 2.0, s_ν = 0.022, m_ν₁ = 32.1 meV.  Wide k bounds, g_aa = 1
(R59 F59 fixed).

| Quantity | Value | Target / Reference |
|----------|-------|---------------------|
| k_e | 4.73 × 10⁻² | 1.19× R59 F59 |
| k_p | 4.73 × 10⁻² | 1.19× R59 F59 |
| k_ν | 4.53 × 10⁻² | 1.14× R59 F59 |
| L_ring_e | 24,948 fm | derived |
| L_ring_p | 19.2 fm | derived |
| L_ring_ν | 1.99 × 10¹¹ fm | derived |
| E(electron) | 0.5109989461 MeV | exact |
| E(proton)   | 938.272 MeV | exact |
| E(ν₁)       | 32.100 meV | exact (target) |
| E(ν₂)       | 33.250 meV | predicted (R61: 33.3) |
| E(ν₃)       | 59.624 meV | predicted (R61: 59.7) |
| Δm²₃₁/Δm²₂₁ | 33.59 | passive check vs R49 33.6 ✓ |
| α_e/α       | 1.000000 | target ✓ |
| α_p/α       | 1.000000 | target ✓ |
| α_ν₁/α      | 1.000000 | target ✓ |
| α_ν₂/α      | 1.192 | predicted (not targeted) |
| α_ν₃/α      | 0.910 | predicted (not targeted) |
| Cost (½‖r‖²) | 1.18 × 10⁻²⁶ | residual at floating-point limit |

**Headline:** the architecture works.  All three sheets sit on a
single 11D metric with α universality across the targeted modes
and signature preserved.  k values cluster at ~1.19× R59 F59 for
the charged sheets and 1.14× for the neutrino — small,
consistent shift from the natural-form value.  The Δm² ratio
matches R49 to 4 digits without being targeted.

**Note on ν₂, ν₃ α deviations.**  α_ν₂ = 1.19α and α_ν₃ = 0.91α
— neither equals α despite ν₁ being targeted to α.  The reason:
α_Coulomb depends on the specific mode's (n_t, n_r), not just
the sheet's (ε, s, k).  Different ν modes on the *same* sheet
get different α values.  This is a structural feature, not a
bug.  Whether it conflicts with R61's "Majorana cancellation"
mechanism (which expects ν₁/ν₂ to behave as a charge-conjugate
pair) is a Track 7 / R61-feedback question.

### F29. Phase 1.5 — three of four R61 candidates converge cleanly

| Candidate | (ε_ν, s_ν) | k_e/k_p (× nat) | k_ν (× nat) | α_ν₁/α | converged? |
|-----------|------------|----------------:|------------:|-------:|:----------:|
| #1 `(+1,+1)(-1,+1)(+1,+2)` | (2.0, 0.022) | 1.19 | 1.14 | 1.000 | YES |
| #2 `(+1,+1)(-2,+1)(+1,+2)` | (8.5, 0.0078) | 1.19 | 1.12 | 1.000 | YES |
| #3 `(+2,+1)(-1,+1)(-1,+2)` | (10.0, 0.0207) | 1.09 | 1.26 | 3.42 | partial |
| #4 `(+1,+1)(+2,+1)(+1,+4)` | (2.5, 0.0193) | 1.19 | 1.13 | 1.000 | YES |

R61 #1, #2, #4 all converge with the full α_e = α_p = α_ν₁ = α
universality and Δm² ratio cross-checking against R49.  The k
values cluster around 1.19× R59 F59 for the charged sheets and
1.13–1.14× for the neutrino — robust across very different ν
geometries.

R61 #3 fails because its ν₁ mode is `(+2, +1)` (n_t = 2, not 1).
The α extraction formula scales differently with `n_t`, so the
"α_ν₁ = α" target sits in a harder-to-reach region of
parameter space.  This is consistent with the R59 F45/F45
universality result: structural universality holds for
|n_tube| = 1; modes with |n_tube| = 2 (or higher) couple
differently and may need different k to hit α exactly.

**Practical implication for R61 feedback:** ν candidates with
all three modes at |n_tube| = 1 (i.e., #1, #4) integrate
cleanly into R60.  Candidates using even-tube modes (R61's
"R48 dark" mechanism for charge neutrality, like #3's ν₁ at
(2, 1)) need either different k handling or a different α
target structure.  R61's "dark" interpretation may need
extension to address how α should be set for these modes.

### F30. Per-sheet L scales span 10 orders of magnitude

The converged R61 #1 configuration:

| Sheet | L_ring (fm) | L_ring (m) |
|-------|-------------|------------|
| Proton | 19.2 | 1.92 × 10⁻¹⁴ m |
| Electron | 24,948 | 2.49 × 10⁻¹¹ m (~ Compton scale) |
| Neutrino | 1.99 × 10¹¹ | 2.0 × 10⁻⁴ m (~ 0.2 mm) |

L_e/L_p ≈ 1,300; L_ν/L_e ≈ 8 × 10⁶.  The proton-to-electron
ratio is below the user's "10⁴" rule of thumb (because the
e-sheet here is shearless and not at the model-E generation
resonance — the electron's μ value is ~1, not ~0.005).  The
electron-to-neutrino ratio is much larger than 10⁴ because the
ν is at meV scale (~10⁹ smaller than electron in mass), giving
L_ν proportionally larger.

**The wide L spread is physically sensible** — it tracks the
mass hierarchy m_p > m_e > m_ν₁.  Importantly, the *k* values
(per-sheet diagonal scales) stay close together (within 5%
across all three sheets), so the metric does not require
per-sheet normalization tricks to make the joint solver work.
**The wide-k-bounds policy paid off**: the solver was free to
explore but landed on naturally close k values for this
geometry, validating the R59 F59 architecture as approximately
correct (to ~20%) without needing global-normalization
re-derivation.

### F31. Track 6 status and next steps

**Completed.**

- Joint e+p+ν solver works at R59 F59 architecture (g_aa = 1)
  with no Phase 2 fallback needed.
- Three of four R61 ν-sheet candidates produce clean
  configurations with all six targets met.
- α universality (α_e = α_p = α_ν₁ = α) is achievable across
  all three sheets when the targeted ν mode has |n_tube| = 1.
- ν₂, ν₃ masses and the Δm² ratio cross-check correctly without
  being targeted.
- Per-sheet diagonal scales (k) cluster within ~20% of R59 F59
  natural value for charged sheets — the natural-form story
  survives in the three-sheet setting.
- Per-sheet L scales naturally span 10+ orders of magnitude as
  expected from the mass hierarchy.

**Working baseline for Track 7.**  R61 #1 configuration:

| Knob | Value |
|------|-------|
| (ε_e, s_e) | (1, 0) |
| (ε_p, s_p) | (1, 0) |
| (ε_ν, s_ν) | (2, 0.022) |
| ν triplet | (+1,+1) (-1,+1) (+1,+2) |
| k_e = k_p | 4.73 × 10⁻² |
| k_ν | 4.53 × 10⁻² |
| L_ring_e | 24,948 fm |
| L_ring_p | 19.2 fm |
| L_ring_ν | 1.99 × 10¹¹ fm |
| g_aa | 1.0 (default) |
| σ_ta | √α (default) |
| σ_at | 4πα (default) |

**Notes for Track 7 (compound modes — μ, τ, neutron, hadrons).**

- Use the F31 baseline configuration as the starting metric.
- Compound modes will combine windings across sheets (e.g.,
  muon as e+ν compound per model-E inventory).
- Compound mode α_Coulomb may be species-dependent — the F28
  observation about α_ν₂ ≠ α_ν₁ shows this happens even within
  the same sheet for different (n_t, n_r).  Track 7 should
  document this carefully and not assume universality across
  compound modes.
- The R61 "Majorana pair cancellation" interpretation
  (ν₁ + ν₂ → 0 net charge when both excited) is testable on
  this baseline — Track 7 or a side study could verify.
- R61 candidate #3 (and other |n_tube|=2 ν configurations)
  may need separate treatment; flag back to R61 if their
  taxonomy wants to retain those candidates.

### Decision point

Track 6 is a clean positive result.  R60's full architecture
(11D, R59 F59 α, three sheets, per-sheet diagonal scales) is
validated as compatible with the model-E spectrum's three-sheet
foundation.

Recommend proceeding to **Track 7 — compound mode search** for
muon, tau, neutron, and hadrons.  Use F31 baseline as input.
Test whether model-E's compound modes (e.g., muon =
(1, 1, −2, −2, 0, 0)) land on observed masses on the new metric,
or whether Track 7 finds different compound modes.  Either
outcome is informative.


