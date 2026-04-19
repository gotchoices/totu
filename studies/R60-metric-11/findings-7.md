# R60 Track 7: Ring↔ℵ structural cancellation test

**Scope.**  Test the algebraic conjecture (post-Track 6 dialog)
that adding ring↔ℵ entries with the structural prescription
σ_ra = (s × ε) × sign × σ_ta on each sheet cancels the
shear-induced α mode-dependence found in Track 6 F28.

Script: [scripts/track7_ring_aleph.py](scripts/track7_ring_aleph.py).

### Background

Track 6 F28 reported that with the ν-sheet at (ε=2, s=0.022) and
the joint solver tuning k_ν to make α_ν₁ = α exactly, the other
two ν modes did not get α: ν₂ landed at 1.192α and ν₃ at 0.910α
— a 28% spread across modes on the *same* sheet.  Algebraic
analysis attributed this to an indirect ring-to-time leakage
chain: shear couples ring to tube, the tube couples to ℵ, ℵ
couples to t.  The leakage strength depends on (n_t, n_r), so
different modes get different α even on the same sheet.

The conjectured fix: add a *direct* ring↔ℵ entry σ_ra at the
specific value σ_ra = (s · ε) · σ_ta.  Algebraically this
cancels the indirect leak, leaving Q ∝ n_t for all modes —
mode-independent.

R59 had ruled out ring-based ℵ mediation as a *replacement* for
tube coupling (F39) and direct ring↔t added on top of tube↔ℵ↔t
(F43).  But ring↔ℵ as a *structural supplement* with the
specific (sε)-tracking value was not in R59's tested
architectures.

### F32. Structural fix restores ν-mode universality to floating point

Took Track 6 F28 baseline (k_e = k_p = 4.73 × 10⁻², k_ν = 4.53 ×
10⁻², all L's from F28).  Added σ_ra entries:

| Sheet | s · ε | σ_ra value |
|-------|------:|-----------:|
| e | 0 | 0 |
| p | 0 | 0 |
| ν | 0.044 | +3.76 × 10⁻³ |

(Only ν gets a nonzero entry because e and p are shearless in
this baseline.)  Built the augmented 11D metric.

Comparison:

| Mode | α_base/α | α_aug/α |
|------|---------:|--------:|
| electron (1, 2) | 1.000 | 0.9989 |
| proton   (1, 3) | 1.000 | 0.9989 |
| ν₁ (+1, +1) | 1.000 | 1.0885 |
| ν₂ (−1, +1) | 1.192 | 1.0885 |
| ν₃ (+1, +2) | 0.910 | 1.0885 |
| **ν-mode spread** | **28.2 %** | **0.0000 %** |

Signature OK in both cases (one negative eigenvalue, the t
direction).

### F33. Interpretation

**The conjecture holds at floating-point precision.**  The σ_ra =
(s·ε) · σ_ta prescription cancels the n_r-dependent term in the
α extraction *exactly*, not approximately.  All three ν modes —
including ν₃ at (1, 2) which had the largest deviation in the
base case — collapse to the same α.

The remaining issue is the **overall magnitude shift**: the
single value all three ν modes converge to is 1.0885α, not
α exactly, and the e/p modes shift slightly to 0.9989α.  The
metric changed (new entries added) and we didn't re-solve the
free knobs (k_e, k_p, k_ν).  A fresh joint solve on the
augmented metric would adjust the k values and shift everyone
back to exactly α.  The structural cancellation persists under
re-tuning (it's coordinate-independent), so the magnitude fix
is a separate, easily-handled problem.

**This solves the mode-dependence problem identified in Track 6.**
R60's α universality story is restored — not just across
sheets, but across modes within a sheet.  R59 F45's "structural
universality" extends to the sheared case, provided the
ring↔ℵ entry is set to its structurally-determined value.

### F34. Status and what's resolved

R60 now has:

1. **R59 F59 architecture** with three sheets, all coupled via
   tube↔ℵ↔t.
2. **Per-sheet diagonal compensation k_x** (Track 4) that
   adjusts to make each sheet's lead mode hit α exactly.
3. **Per-sheet ring↔ℵ entry σ_ra_x** (Track 7) at structural
   value (sε)_x · σ_ta_x that cancels mode-dependence on
   sheared sheets.

Together these give: α_e = α_p = α_ν = α (across sheets, by
universality of |n_tube|=1 + per-sheet k tuning) and α independent
of (n_t, n_r) within each sheet (by the σ_ra cancellation).
Both axes of universality are now achieved.

Per-sheet "natural" values for the augmented architecture (at
the Track 6/7 baseline geometry, post-resolve — not yet
explicitly computed):

| Knob | Value |
|------|-------|
| σ_ta_x | sign × √α (per sheet) |
| σ_at | 4πα |
| g_aa | 1 |
| k_x | tunable per sheet, ~5% of unity for charged sheets at moderate shears |
| **σ_ra_x** | **(sε)_x · σ_ta_x  (NEW, derived)** |

### Caveats and open questions

- **Mass impact not verified.**  The mode_energy formula in
  Track 1 uses only the Ma sub-block; ring↔ℵ entries sit
  outside Ma so they don't enter that approximation.  A full
  Schur-corrected mass calculation would shift masses slightly.
  Likely small (the σ_ra values are small) but should be
  verified.
- **No re-solve done.**  Track 7 used Track 6's k and L values
  unchanged.  A clean joint solve on the augmented metric would
  give the post-fix natural-form k values and show the magnitude
  shift collapses.  Easy follow-up.
- **Cross-sheet effects.**  My derivation was for a single
  sheet in isolation.  On the joint e+p+ν metric, the σ_ra
  cancellation might have small cross-sheet residuals.  The
  numerical result here (spread 0.0000%) suggests cross-sheet
  effects are also cancelled or extremely small.  Notable.
- **Generalizes to sheared e and p.**  The Track 6/7 baseline
  has e and p shearless.  If we ever turn on shear there
  (e.g., for ghost suppression or compound mode placement), the
  σ_ra prescription should still apply: σ_ra_e = (s·ε)_e · σ_ta_e
  cancels the e-sheet's leak.  Worth testing once we add
  e-sheet shear.
- **Compound modes.**  Compound modes span multiple sheets;
  their α extraction involves contributions from each sheet.
  The single-sheet structural fix should work per sheet, so
  compound mode α should also be mode-independent on the
  augmented metric.  Track 8 (compound mode search) will test.

### Decision point

**The mode-dependence concern flagged in the Open Question
section above is now resolved structurally.**  The three
candidate next-step tracks I outlined (7a, 7b, 7c) are
superseded by Track 7's actual result.  The original "Track 7d"
(compound mode search for μ, τ, neutron, hadrons) becomes the
natural next step.

Recommend: re-solve the joint system on the augmented metric
(quick post-fix calibration), then proceed to compound mode
search.

---

## Track 7b: Re-solve on the ring↔ℵ augmented metric

**Scope.**  Track 7 demonstrated structural ν-mode universality
(spread 0.0000%) but with α magnitude shifted to 1.0885α because
Track 6's k values were used unchanged on a metric that had
changed.  Track 7b runs the full joint solver on the augmented
metric to bring magnitude back to α exactly while preserving the
structural cancellation.

Script: [scripts/track7b_resolve.py](scripts/track7b_resolve.py).

### F35. Re-solve converges with all six targets at floating-point precision

Joint solver on the augmented metric (tube↔ℵ + structural
ring↔ℵ + ℵ↔t).  6 free knobs (L_x, k_x per sheet), 6 targets
(m_x, α_x = α for x ∈ {e, p, ν₁}).  Same Track 6 sheet inputs
(R61 #1: e/p shearless, ν at ε=2, s=0.022).

| Knob | Value |
|------|-------|
| k_e  | 4.696442 × 10⁻²  (1.1803× R59 F59) |
| k_p  | 4.696442 × 10⁻²  (1.1803× R59 F59) |
| k_ν  | 4.696442 × 10⁻²  (1.1803× R59 F59) |
| L_ring_e | 25,035 fm |
| L_ring_p | 19.28 fm |
| L_ring_ν | 1.96 × 10¹¹ fm |

| Target | Value | Precision |
|--------|-------|-----------|
| E_e | 0.5109989461 MeV | 10⁻¹⁵ |
| E_p | 938.272 MeV | 10⁻¹⁴ |
| E_ν₁ | 32.100 meV | 10⁻¹⁴ |
| α_e / α | 1.0000000000 | 10⁻¹⁵ |
| α_p / α | 1.0000000000 | 10⁻¹⁵ |
| α_ν₁ / α | 1.0000000000 | 10⁻¹⁴ |
| Signature | OK | one neg eig (the t direction) |

### F36. Track 7's structural prediction is confirmed at floating-point exactness

ν₂ and ν₃ were not targeted in the solve.  Track 7 predicted
that, regardless of the converged (L, k) values, the structural
σ_ra cancellation would make all three ν modes give the same α.

| Mode | α_x / α |
|------|---------|
| ν₁ (+1, +1) — targeted | 1.0000000000 |
| ν₂ (−1, +1) — *not targeted* | 1.0000000000 |
| ν₃ (+1, +2) — *not targeted* | 1.0000000000 |
| **ν-mode α spread** | **0.00e+00** |

The cancellation is a property of the augmented metric structure,
not of any specific operating point.  Track 7's algebraic
derivation is fully validated.

### F37. The augmented architecture has a single-k symmetry

A striking observation from F35: the joint solver — with three
*independent* per-sheet k knobs — converged on **k_e = k_p = k_ν**
to floating-point precision.  Track 6's solver had given values
within ~5% of each other (~1.19× nat for charged sheets, 1.14× for
ν).  The augmented metric pins them to one common value (1.1803×
R59 F59 = 0.04696).

This suggests that adding the ring↔ℵ entries restores a deeper
symmetry between sheets.  In the un-augmented (Track 6) metric,
the per-sheet k differed because shear-induced ring leakage was
species-dependent (different n_r per sheet).  With the
cancellation, that asymmetry is gone, and one global k handles
all three sheets.

**Practical consequence:** the model has *one* diagonal-scale
parameter, not three.  k = 1.1803 × 1/(8π) = 4.696 × 10⁻² is the
new candidate "natural" value for the augmented architecture.
Whether this value has a clean closed form (analogous to R59
F59's 1/(8π)) is open; numerically 1.1803 is suggestive but
hasn't been pattern-matched yet.  Worth analytical follow-up.

### F38 (cross-checks). Δm² ratio and ν masses fall out automatically

| Quantity | Value | R49/R61 reference |
|----------|-------|-------------------|
| E(ν₂) | 33.250 meV | R61 #1: 33.3 |
| E(ν₃) | 59.624 meV | R61 #1: 59.7 |
| Δm²₃₁ / Δm²₂₁ | 33.5909 | R49 target: 33.6 |

The Δm² ratio matches to 4 digits without being targeted —
consistent with R49's mechanism (the ratio is a function of
(ε_ν, s_ν) alone).  R61 candidate #1's ν₂ and ν₃ masses are
also reproduced, confirming the R61 taxonomy is internally
consistent with our metric.

### Status

R60 architecture is now FULLY validated as compatible with the
model-E three-sheet foundation:

- α universal across sheets ✓ (Track 4)
- α universal across modes within a sheet ✓ (Track 7 + 7b)
- Three-sheet metric works with one global k ✓ (Track 7b F37)
- All masses calibrated correctly ✓
- Δm² ratio cross-checks ✓

**Working baseline for Track 8 (compound modes):**

| Knob | Value |
|------|-------|
| (ε_e, s_e) | (1, 0) |
| (ε_p, s_p) | (1, 0) |
| (ε_ν, s_ν) | (2, 0.022) |
| ν triplet | R61 #1: (+1,+1)(-1,+1)(+1,+2) |
| k (all sheets) | 4.696 × 10⁻² (1.1803/(8π)) |
| L_ring_e | 25,035 fm |
| L_ring_p | 19.28 fm |
| L_ring_ν | 1.96 × 10¹¹ fm |
| g_aa | 1 |
| σ_ta | √α (signs +1, −1, +1 for e, p, ν) |
| σ_at | 4πα |
| **σ_ra (NEW)** | **(sε)·σ_ta per sheet (derived, not free)** |

### Open follow-ups

- Analytical derivation of the natural-form value k = 1.1803/(8π).
  R59 F59 found k = 1/(8π); the augmented architecture wants
  k = 1.1803/(8π).  Pattern? Analytical identity? (Cheap analysis.)
- Mass impact of σ_ra entries via Schur correction.  Track 7b's
  joint solve uses mode_energy on the Ma sub-block only; a
  full Schur calculation would shift masses by O(σ_ra²) ≈ 10⁻⁵.
  Likely small enough to ignore but worth a check.
- Test the augmented architecture with non-shearless e or p
  sheets.  The σ_ra prescription should generalize cleanly, but
  Track 7 only verified for ν having shear and e/p shearless.

### Decision point

**The Track 7+7b ring↔ℵ structural fix is a real architectural
advance.**  R60's α universality is now established on both axes
(across sheets AND across modes).  The compound-mode question
(Track 8) is the next natural step — this is the original "Track
7d" from the now-superseded Open Question section.

Recommend proceeding to Track 8 (compound modes — μ, τ, neutron,
hadrons) on this baseline.

---

## Track 7c: Inter-sheet shear compatibility check

**Scope.**  Quick sanity test: can we activate Ma cross-sheet σ
entries on top of Track 7b's baseline without breaking α
universality?  Eight configurations tested.

Script: [scripts/track7c_cross_sheet.py](scripts/track7c_cross_sheet.py).

### F39. Most cross-sheet σ entries break signature or α universality

Test baseline: Track 7b metric (all α targets at exactly α with
ring↔ℵ structural fix active).  Add one or more Ma cross-sheet
σ entries at various magnitudes, measure response.

| Configuration | Signature | α universal? | α magnitude |
|---------------|:---------:|:------------:|:-----------:|
| Baseline (no cross) | OK | yes | 1.000 |
| σ_{pt, νr} = 0.01 | OK | **no** — ν spread 1.51× | broken |
| σ_{pt, νr} = 0.10 | **broken** | no | broken |
| σ_{pt, νr} = −0.18 (R54) | **broken** | no | broken |
| σ_{pr, νr} = +0.10 (R54) | **broken** | preserved | 1.000 |
| R54 pair (both ν₄₅, ν₄₆) | **broken** | no | broken |
| σ_{et, νr} = 0.05 | **broken** | no | broken (5.45×) |
| σ_{et, νt} = 0.05 | **broken** | no | broken |
| σ_{er, νr} = 0.05 | **broken** | preserved | 1.000 |

**Every tested cross-sheet activation either breaks signature or
breaks α universality (or both).**  Two entries (ring-ring
crosses σ_{pr,νr} and σ_{er,νr}) preserve α exactly but still
break signature.

### F40. Interpretation: Track 7's fix does not extend freely to cross-sheet entries

The ring↔ℵ structural prescription `σ_ra = (sε) · σ_ta`
cancels the *in-sheet* shear leakage.  It does not automatically
cancel *cross-sheet* leakage.

Mechanism: cross-sheet entries (e.g., σ_{p_t, ν_r}) couple a
tube on one sheet to a ring on another.  Through the shared ℵ,
this creates new indirect α-coupling chains (p_t → ν_r → ν_t
via ν-sheet shear → ℵ via σ_ta_ν → t) that are NOT cancelled by
the per-sheet σ_ra.

**Consequence:** compound-mode fine-tuning via cross-sheet σ
entries is not a free knob on the Track 7b architecture.  Two
options for Track 8:

1. **Extend the structural prescription** to include compensating
   entries that cancel cross-sheet leakage, analogous to the
   σ_ra = sε·σ_ta rule but for inter-sheet cases.  Algebra TBD.
2. **Accept mode-dependent α on compound modes.**  Make α
   universality a target *only* for single-sheet reference modes
   (electron, proton, ν₁).  Compound modes (muon, tau, neutron)
   would naturally have species-dependent α — consistent with
   physical reality if the R61 charge-topology interpretation is
   right (charge is winding, α is a coupling strength that can
   vary).

**Signature breakage** on ring-ring crosses is a separate
concern — those entries preserve α but push an eigenvalue
negative.  Probably fixable by allowing k values to re-adjust
when cross entries activate (Track 7b-style re-solve); not done
here because our Params/solver infrastructure doesn't yet
support free cross-sheet σ.

### F41. Status and implications for Track 8

**What's clear:** Ma cross-sheet σ entries are not a clean free
knob.  Compound-mode search (Track 8) needs to either derive
compensating entries (option 1 above) or accept mode-dependent
compound α (option 2).

**What's not yet tested:**

- Cross-sheet entries combined with re-solve of (L, k).  The
  solver infrastructure needs to be extended to include σ_cross
  as free knobs with appropriate bounds.  A meaningful Track 7c
  extension; deferred.
- Cross-sheet entries involving ℵ (e.g., σ_{p_t, ν_t via ℵ})
  — candidate for the "extended structural prescription" path.
- Whether specific cross-sheet values emerge naturally from
  compound-mode targeting (vs being tuned ad hoc).

### Decision point

Track 8 scope needs to choose between options 1 (extend
prescription) and 2 (accept mode-dependent compound α) before
coding.  User dialog required.

**Also surfaced by Track 7c:** our Track 7b baseline uses
*shearless* e and p sheets (ε=1, s=0), which means
neither sheet has proper ghost-ordering on its own — (1, 1) is
lighter than (1, 2) on the e-sheet and (1, 1), (1, 2) are both
lighter than (1, 3) on the p-sheet.  We deferred ghost
suppression to "other mechanisms."  Before compound-mode search
(which has 6× more degrees of freedom and is much harder to
diagnose), it's worth revisiting whether we should activate
"magic shear" (s_e ≈ 2, s_p ≈ 3) to get proper ghost ordering
built into each sheet's geometry.  User-facing analysis pending.

---

## Track 7d: Magic-shear baseline re-solve

**Scope.**  Replace Track 7b's shearless baseline on e and p
with magic-shear geometries that give each sheet's target mode
the lightest μ on that sheet.  Verify Track 7b's α universality
survives the geometry change.

Script: [scripts/track7d_magic_shear.py](scripts/track7d_magic_shear.py).

### F42. Joint solve converges cleanly at magic-shear baseline

Sheet inputs:
- e: (ε=0.4, s=2.0), sε = 0.8 — magic shear for target (1, 2)
- p: (ε=0.4, s=3.0), sε = 1.2 — magic shear for target (1, 3)
- ν: (ε=2.0, s=0.022) R61 #1 unchanged

Joint signature budget: `Σ(sε)² = 0.64 + 1.44 + 0.002 = 2.082`
< predicted 5/2 three-tube bound.  Under budget with ~0.4
headroom.

Solver result:

| Quantity | Value | Notes |
|----------|-------|-------|
| Convergence | OK (gtol, cost 10⁻²⁶) | — |
| k_e = k_p = k_ν | 4.696442 × 10⁻² | Same single-k value as Track 7b F37 |
| L_ring_e | 27,990 fm | (shifted from Track 7b's 25,035 — accounts for ε, s change) |
| L_ring_p | 15.24 fm | (shifted from Track 7b's 19.28) |
| L_ring_ν | 1.96 × 10¹¹ fm | unchanged |
| σ_ra_e (derived) | +6.83 × 10⁻² | much bigger than Track 7b (was 0 at s_e = 0) |
| σ_ra_p (derived) | −1.03 × 10⁻¹ | ditto |
| σ_ra_ν (derived) | +3.76 × 10⁻³ | unchanged |
| Signature | OK (1 neg eig) | ✓ |

**The emergent single-k symmetry survives the geometry change.**
Even with very different (ε, s) on each sheet, k_e = k_p = k_ν
to floating-point precision.  Same value 1.1803/(8π) as Track 7b.

### F43. α universality survives magic shear — on all three sheets and all tested modes

All six targets met to floating-point precision (residuals at
10⁻¹⁴).  Untargeted ν₂ and ν₃ modes also give α to floating-point:

| Mode | α/α (targeted?) |
|------|----------------|
| electron (1, 2) | 1.0000000000 (target) |
| proton (1, 3) | 1.0000000000 (target) |
| ν₁ (+1, +1) | 1.0000000000 (target) |
| ν₂ (−1, +1) | 1.0000000000 (not targeted) |
| ν₃ (+1, +2) | 1.0000000000 (not targeted) |

ν-mode spread: **0.00e+00**.  Track 7's structural fix works
cleanly across the geometry change.  Δm²₃₁/Δm²₂₁ = 33.59
matches R49's 33.6 as before.

### F44. Ghost ordering achieved on e and p — not on ν

At the converged (L, k, σ_ra) values, full-metric mode energies
for (1, n_r) charged modes:

**e-sheet (target n_r = 2):**

| n_r | E | ratio to electron |
|----:|--:|------------------:|
| 0 | 0.654 MeV | 1.28 |
| 1 | 0.550 MeV | 1.08 |
| **2** | **0.511 MeV** | **1.00 ← target / lightest ✓** |
| 3 | 0.550 MeV | 1.08 |
| 4 | 0.654 MeV | 1.28 |

**p-sheet (target n_r = 3):**

| n_r | E | ratio to proton |
|----:|--:|----------------:|
| 0 | 1465.6 MeV | 1.56 |
| 1 | 1201.6 MeV | 1.28 |
| 2 | 1010.5 MeV | 1.08 |
| **3** | **938.27 MeV** | **1.00 ← target / lightest ✓** |
| 4 | 1010.5 MeV | 1.08 |

**Ghost ordering achieved on e and p sheets.**  The magic shear
makes the target mode the lightest single-sheet charged mode on
each, with its neighbors (n_r ± 1) the next closest (~1.08×
target), and the gap grows fast as n_r departs further.

**ν-sheet (target n_r = 1):**

| n_r | E | ratio to ν₁ |
|----:|--:|------------:|
| **0** | **14.63 meV** | **0.456 ← LIGHTEST** |
| 1 | 32.10 meV | 1.00 (target) |
| 2 | 59.62 meV | 1.86 (= ν₃) |

The (1, 0) ν-sheet mode is ~46% of ν₁'s mass — a lighter spin-½
charged-neutral ghost that we do not observe.  Same as noted
in pool item **j**.  The magic-shear ordering doesn't apply on
the ν-sheet because (a) R61's Δm²-tuned s_ν = 0.022 is far from
the magic value s_ν = 1 for (1, 1), and (b) the R61 taxonomy
expects filter mechanisms (Majorana-pair cancellation, dark
even-tube modes) to handle ν ghosts, not in-sheet ordering.

### F45. Status and implications for Track 8

**What Track 7d establishes:**

1. **Magic-shear baseline is viable** for e and p.  All targets
   hit, signature OK, ghost ordering ✓, k-symmetry preserved,
   α universal.
2. **σ_ra values grow with sε** (now 0.07 and 0.10 on e and p)
   but still small enough to preserve signature.
3. **ν-sheet ghost (1, 0) persists** and must be handled via
   R61 filter mechanisms (pool item **j** — defer to R61
   dialogue).

**Working baseline for Track 8:**

| Knob | Value |
|------|-------|
| (ε_e, s_e) | (0.4, 2.0) |
| (ε_p, s_p) | (0.4, 3.0) |
| (ε_ν, s_ν) | (2.0, 0.022) |
| ν triplet | R61 #1: (+1,+1)(−1,+1)(+1,+2) |
| k (all sheets) | 4.696 × 10⁻² = 1.1803/(8π) |
| L_ring_e | 27,990 fm |
| L_ring_p | 15.24 fm |
| L_ring_ν | 1.96 × 10¹¹ fm |
| g_aa | 1 |
| σ_ta | √α (signs +1, −1, +1) |
| σ_ra | (sε)·σ_ta per sheet (derived) |
| σ_at | 4πα |

All in-sheet architecture now "done."  Track 8 proceeds on this
baseline.  **Cross-sheet σ entries stay at zero for the first
Track 8 pass** — compound modes (μ, τ, neutron, hadrons) are
6-tuples on the existing joint metric, so their masses are
already determined by the joint inverse without needing σ_cross.
Pool item **h** (cross-sheet structural prescription) is a
follow-up only if Track 8's first pass needs fine-tuning.

### Decision point

Track 7d clean.  Ready for Track 8 (compound mode search) on
the magic-shear baseline above.

---

## Appendix: the mode-dependent α question (now resolved)

The following analysis was generated post-Track 6 when the α
mode-dependence problem first surfaced.  It outlined the
problem, the load-bearing roles of shear, and candidate
resolution paths.  Tracks 7 and 7b resolved the question via
the ring↔ℵ structural cancellation.  Kept below as a record
of the reasoning path.

### What we found

Track 6 surfaced that α_Coulomb is **mode-dependent** on any
sheared sheet under R59 F59.  The closed-form formula is

    Q(n_t, n_r) ∝ n_t · (1 + u²) − n_r · u   with u = s · ε.

At u = 0 (shearless), Q ∝ n_t — so all |n_tube|=1 modes get
identical Q regardless of n_r.  At u ≠ 0, the n_r·u term breaks
this and different (n_t, n_r) on the same sheet get different α.

In our Track 6 baseline this only manifested on the ν-sheet
(s_ν = 0.022), where ν₁ at α target gave ν₂ at 1.19α and ν₃ at
0.91α.  e and p sheets are shearless in the baseline so didn't
exhibit mode-dependence.

### Why this matters

Standard physics has α as a universal constant (1/137 for every
charged particle).  If the model predicts different α for
different particles on the same sheet, it is not faithful to
observation — at least not without reinterpreting what α
*means* in MaSt.

### Two candidate resolutions

**(a) Reinterpret α as a mode-dependent coupling strength
modulated by topological charge.**  Integer EM charge in MaSt
is topological (Q_charge = −n_e_tube + n_p_tube).  Our extracted
"α_Coulomb = Q²/(4π)" might be a per-mode coupling parameter
(weak-interaction analog?), not the universal EM coupling.  The
electron's value happens to equal observed α; other modes have
related-but-different values.  Physical support: neutrinos *do*
have different scattering rates per flavor.  But: the standard
model treats α as universal across charged leptons, and any MaSt
reinterpretation needs a compensating story for charged modes
(which we didn't test because e and p stayed shearless).

**(b) Eliminate sheared sheets entirely.**  If no sheet has
internal shear, mode-dependence vanishes everywhere and α is
strictly universal across |n_tube|=1 modes.  But this requires
finding non-shear mechanisms for everything shear currently does.

### What shear currently does in MaSt (load-bearing)

Per user assessment plus review of model-D/E/R49:

1. **Neutrino oscillation matching.**  R26's `s_ν ≈ 0.022` gives
   `Δm²₃₁/Δm²₂₁ = 33.6` exactly via `(3−2s)/(4s)`.  Without
   shear, all (n_t, n_r) modes on a shearless sheet have masses
   determined only by μ = √((n_t/ε)² + n_r²) — a fixed
   geometric pattern.  Whether *any* shearless ν-sheet
   geometry gives the right mass triplet 32.1/33.3/59.7 meV is
   open and unlikely without auxiliary mechanism.
2. **Generation structure (R53).**  Already retired in R60
   (Track 4 F19 incompatibility with R59 F59 α).  Replaced by
   compound modes per model-E inventory.
3. **Ghost suppression on charged sheets.**  Multiple
   alternatives exist (R46 waveguide cutoff, R47 gcd
   irreducibility, R56 mode routing, R61 (1,1) filter on
   ν-sheet).  Not strictly shear-dependent.

### Compound mass splitting — what it would look like

In the current single-sheet picture, ν₁/ν₂/ν₃ are three
different (n_t, n_r) on the same (ε_ν, s_ν, L_ring_ν) sheet.
Mass differences come entirely from the geometric formula at
nonzero shear.

In a compound picture, ν₁/ν₂/ν₃ would each be a 6-tuple
spanning multiple sheets:

| Eigenstate | Possible compound mode (illustrative) |
|------------|---------------------------------------|
| ν₁ | `(0, 0, 1, 1, 0, 0)` — pure ν-sheet (1, 1) |
| ν₂ | `(1, 0, 1, 1, 0, 0)` — ν₁ + small e-sheet (1, 0) leak |
| ν₃ | `(0, 0, 1, 1, 1, 0)` — ν₁ + small p-sheet (1, 0) leak |

Each compound mode's mass comes from `E² ∝ ñ G̃⁻¹ ñ` summing
across all touched sheets.  Cross-sheet σ entries (which were
zeroed in the R60 baseline) provide the inter-sheet coupling.
Different compounds get different masses **even on shearless
sheets**, because their cross-sheet contributions differ.

### Possible next-step tracks (deferred — R60 paused for analysis)

If R60 resumes after the analysis dialog the user has planned,
candidate tracks to investigate this question:

**Track 7a — mode-dependence audit.**  Catalog α_Coulomb for a
representative set of (n_t, n_r) modes on each sheet at the
Track 6 baseline.  Quantify how big the deviation gets across
the modes we'd want to label as ν₁/ν₂/ν₃ and across compound
modes that might represent muon/tau/neutron.  Outcome: a sharp
characterization of how serious the mode-dependence problem is
across the whole spectrum.

**Track 7b — shearless ν compound mass splitting attempt.**
Set s_ν = 0.  Search compound 6-tuples (e + ν, p + ν, e + ν + p
combinations) whose energies could be assigned to ν₁/ν₂/ν₃.
Use cross-sheet σ entries (currently zeroed) as the splitting
mechanism.  Test whether *any* configuration produces
m_ν₂/m_ν₁ and m_ν₃/m_ν₁ ratios consistent with observed
oscillation data (Δm²₃₁/Δm²₂₁ = 33.6).  If yes: shear can be
dropped from ν-sheet, mode-dependence vanishes, R60 program
strengthens.  If no: shear is genuinely required for ν
oscillations and we must address mode-dependence on its own
terms.

**Track 7c — α reinterpretation feasibility.**  Take the
mode-dependence as physical and ask what it would predict.
Compute α_e for the electron (1, 2) on the *currently
shearless* e-sheet (always equals α — no test).  Then add a
small s_e and recompute α for the (1, 1) ghost mode and (1, 3)
hypothetical mode to see how mode-dependence behaves on the
e-sheet.  Compare to standard QED predictions for any related
observable.  Outcome: indicates whether the mode-dependent α
could survive as a physical prediction or is incompatible with
known data.

**Track 7d (the original "Track 7" before this question
arose) — compound mode search for μ, τ, neutron, hadrons.**
Resume the F31 baseline and search for compound modes matching
the model-E inventory.  Defer α universality concerns; just
check whether mass spectrum reproduces.  Could be useful as
parallel work even if 7a–c are still in question.

### Status

R60 paused at end of Track 6 for further analysis dialog with
user.  No commitment to which (if any) of the above tracks to
pursue; depends on outcome of analysis.
