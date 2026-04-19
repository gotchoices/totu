# R61: Neutrino-sheet tuning — paired-mode zoo and Δm² comb

**Status:** Tracks 1–4 complete — charge-neutrality-scored shortlist available
**Type:** compute + analytical
**Depends on:** R49 (ν-sheet families, ε_ν/s_ν sweep, Majorana F16),
  R26 (Assignment A derivation), R57 (dark/active ratio 440:1),
  R60 next-track b (smallest-shear ν solution)

---

## Objectives

R49 identified the neutrino sheet as structurally the simplest of the
three Ma sheets (F26): the three mass eigenstates are the three lowest
spin-½ modes of an unfiltered torus at ε_ν = 5, s_ν = 0.022, matching
Δm²₃₁/Δm²₂₁ = 33.6 with one free parameter.  R49 F16 also noted that
±n_ring modes are C-conjugates, i.e. WvM-realized Majorana neutrinos.

R61 picks up a structural observation that R49 made in passing but did
not systematize: at any (ε_ν, s_ν) that produces the 33.6 ratio, **many
triplets beyond Family A reproduce the same ratio**, and **every
fermion-candidate mode (|n_r| ≥ 1) has a ±n_r partner at near-degenerate
mass**.  This suggests a different reading of the neutrino sheet — not
"three specific modes selected from a ghost-filled spectrum," but "a
zoo of near-degenerate ±paired triplets all producing the observed
ratio, of which three are 'loud' under some selection rule and the rest
are sterile (R57's 440:1)."

R61 asks:

1. Does a region of (ε_ν, s_ν) exist where the zoo of 33.6-ratio,
   all-paired, spin-½ triplets is populous AND the observed triplet
   sits cleanly among its lowest members?
2. What *comb* of Δm² features (predicted by the integer n_tube
   transition structure) does each (ε_ν, s_ν, E₀) calibration imply?
   Do reported oscillation anomalies (LSND, DANSS, reactor) land on
   the comb or miss it?
3. What selection rule — waveguide cutoff, cross-sheet coupling,
   energetic threshold, production matrix element — picks three
   "loud" triplets out of the zoo?
4. Under the pair-mandatory reading, does the Majorana superposition
   give zero net winding / zero charge under whichever charge
   mechanism (tube-winding per R48, ring-winding per Taxonomy) is
   taken as canonical?

If a clean zoo region exists and the comb lines up with any reported
anomaly, R61 delivers a testable re-reading of neutrino physics.  If
no selection rule cleanly isolates Family A from the zoo, R61
documents the gap and flags what the selection mechanism would need
to be.

Note on project-level framing: R61 ignores cosmological Σm and N_eff
bounds per user direction — only steady-state laboratory oscillation
constraints apply.

---

## Execution plan

Tracks are added one at a time.  Only the currently-executing track
is numbered; candidates for "next track" live in the pool below as
lettered items and get numbered when chosen.

### Track 1 — Zoo enumerator and comb predictor (complete)

See [findings.md §Track 1](findings.md#track-1-zoo-enumerator-pair-filter-triplet-finder-δm²-comb)
for F1–F4 and the reference sweep results.

**Known correction carried into Track 2:** Track 1 used the Taxonomy
form `(n_r·ε)² + (n_t − n_r·s)²` with tuple (n_ring, n_tube).  R49
uses `(n_tube/ε)² + (n_ring − n_tube·s)²` with tuple (n_tube, n_ring).
The 33.6 ratio check is unaffected for same-n_tube triplets, but
absolute µ² values and mixed-n_tube zoo counts differ.  Track 2
adopts R49's convention as canonical and re-verifies Track 1's
smoke tests under it.

### Track 2 — Candidate ranking and best-fit selection (complete)

See [findings.md §Track 2](findings.md#track-2-candidate-ranking-and-best-fit-selection)
for F5–F12, smoke-test results (T5–T8), and the full shortlist.

**Headline:** best candidate at ε_ν = 2.0, s_ν = 0.022 with Family
A modes (1,1)(−1,1)(1,2), composite score 0.762.  Same mode-set as
R49 Assignment A but at smaller ε — preferred by Track 2's scoring
(better spin-½ quality: 0.45 vs 0.36).  R49's ε = 5.0 scores 0.700
and remains a strong alternative under different priorities
(sterile-count minimization).

**Supplemental framing (kept for reference)**: this was the Track 2
plan before execution.

### Track 3 — Sterile-count scoring and consensus shortlist (complete)

See [findings.md §Track 3](findings.md#track-3-sterile-count-scoring-and-consensus-shortlist)
for F13–F16, smoke-test results (T9–T12), and the consensus shortlist.

**Headline:** **ε_ν = 2.0, s_ν = 0.022, Family A modes (1,1)(−1,1)(1,2)**
is top-1 under all three weight schedules (equal, sterile-heavy,
balanced).  Same mode-set as R49 Assignment A but at smaller ε,
preferred on spin quality (0.89 vs 0.56) AND sterile count (4 vs
15 for the identical triplet).  R49's ε=5 remains the alternative
if cosmological Σm bound is binding.

Consensus shortlist (top-5 under every schedule) = 4 candidates,
3 of them at ε_ν = 2.0.

**Supplemental framing (kept for reference)**: this was the Track
3 plan before execution.

**Goal.**  Extend Track 2's scorer with a sterile-count criterion
(R49's preferred selection handle) and re-rank.  Produce a
consensus shortlist of candidates that score top under *multiple*
weight schedules, so the selection is robust to which criterion
the user cares about most (spin-½ quality vs mode sparsity).

**Strategy.**

Add one primitive (`sterile_count`) and one scoring criterion.
Run under three weight schedules: (a) Track 2's equal-weight
baseline (sterile weight = 0), (b) sterile-count dominant
(weight 0.4, others 0.15 each), (c) balanced (all six at ~0.167).
A candidate appearing in the top-3 under all three schedules is a
"consensus" candidate — the one we would recommend regardless of
weight preference.

**Tactics.**

1. **Sterile count primitive.**
   `sterile_count(triplet, paired_modes) → int`: number of paired
   fermion modes with µ² in [µ²_a, µ²_c] that aren't in the triplet.
   Validates against R49 F4: at (ε=5, s=0.022), Family A's count
   should be ≈ 26 (R49's reported value).

2. **Scoring criterion.**  `sterile_score = 1 − min(1, count/100)`.
   Linear from 100 sterile modes (score 0) to 0 sterile (score 1).
   The 100 cap matches R49's "hundreds at small ε" observation.
   A triplet with R49's 26 scores 0.74.

3. **Six-criterion composite.**  Default weights redistribute from
   Track 2's equal-weight {0.2, 0.2, 0.2, 0.2, 0.2} to
   {0.167, 0.167, 0.167, 0.167, 0.167, 0.167} when sterile is
   included.  Alternative schedules load sterile more or less.

4. **Three-schedule sweep.**  For each (ε, s) in Track 2's grid,
   score every paired-fermion 33.6-triplet under three weight
   schedules.  Pick best triplet per (ε, s) per schedule.
   Deduplicate by mode-set within each schedule.  Intersect the
   top-5 lists → consensus shortlist.

5. **Tradeoff plot.**  Scatter: sterile-count vs composite score
   (under equal-weight baseline), with top candidates labeled.
   Visualizes the Pareto frontier.

**Smoke tests.**

| # | Test | Expected |
|---|------|----------|
| T9  | `sterile_count` for Family A triplet at (ε=5, s=0.022) | ≈ 26 (matches R49 F4) |
| T10 | Under sterile-heavy weights, best candidate ε shifts toward 5 (R49's choice) | top-1 ε increases relative to Track 2 |
| T11 | Under equal-weight baseline (sterile weight = 0), ranking matches Track 2 | top-1 = (ε=2, s=0.022) Family A |
| T12 | Consensus intersection across 3 schedules non-empty and includes Family A or a Family A variant | robustness confirmed |

**Deliverables.**

- `scripts/track3_sterile_scoring.py` — sterile primitive, six-criterion
  scorer, three-schedule sweep, consensus intersection, tradeoff plot.
- `outputs/track3_shortlist_equal.md` — ranked top-10 under equal weights.
- `outputs/track3_shortlist_sterile_heavy.md` — ranked top-10 under sterile-heavy weights.
- `outputs/track3_shortlist_balanced.md` — ranked top-10 under balanced weights.
- `outputs/track3_consensus.md` — intersection of top-5 across three schedules.
- `outputs/track3_tradeoff.png` — scatter of sterile-count vs composite score.
- `findings.md` F13–F16: smoke tests, per-schedule top-1 candidates, consensus list, Pareto observations.

**Acceptance criteria.**

- All four smoke tests pass.
- Consensus shortlist has ≥ 1 entry (ideally 2–3) — candidates
  robust to weight choice.
- If consensus is empty, explicitly flag the selection as
  weight-dependent and report both Track 2's optimum and R49's
  as co-equal candidates with their respective justifications.

---

**Goal.**  For each (ε_ν, s_ν) in the zoo parameter space,
identify the best paired-fermion 33.6-triplet under a composite
score and produce a ranked shortlist of best-candidate (ε_ν, s_ν)
points.  This is the direct path to selecting one or more *best*
ν-sheet size/shape/shear settings.

**Strategy.**

Build on Track 1's enumerator and comb primitives.  Add a spin-½
function (R49's finite-ε formula), a per-triplet composite scorer,
and a ranker.  Keep scoring transparent — each criterion contributes
a sub-score; the final is a weighted sum with explicit weights;
rank stability under weight perturbations is reported alongside the
shortlist.  No hidden tuning.

**Tactics.**

1. **Convention alignment.**  Adopt R49's form as canonical:
   `mu2(n_tube, n_ring, eps, s) = (n_tube/eps)² + (n_ring − n_tube·s)²`.
   Refactor Track 1's primitives under this convention.  Re-run T1
   against R49's published Family A masses (m₁ = 29.2, m₃ = 58.2
   meV at E₀ = 29.25 meV).

2. **Spin-½ function.**  Port R49's finite-ε formula
   `L_z/ℏ = 2π²q²(2 + ε²) / I²(p, q, ε)` where
   `I(p, q, ε) = ∫₀²π √(p²ε² + q²(1 + ε cos(pt))²) dt` and (p, q)
   map to (n_tube, n_ring).  Validate against R49 F14 ((0,1) gives
   spin 1) and R49 F7 ((1,2) at ε = 5 gives ≈ 0.37).

3. **Per-triplet scoring.**  For each paired 33.6-triplet at
   (ε_ν, s_ν), compute five sub-scores:

   | Criterion | Quantity | Direction |
   |-----------|----------|-----------|
   | Ratio exactness | \|ratio − 33.6\| / 33.6 | minimize |
   | Pair cleanliness | max over three pairs of splitting/mean-µ² | minimize |
   | Mode simplicity | Σ (\|n_tube\| + \|n_ring\|) across triplet | minimize |
   | Spin quality | Σ \|L_z/ℏ − 0.5\| across triplet | minimize |
   | Lowest-triplet bonus | is this the lightest paired triplet at (ε, s)? | boolean |

   Normalize each continuous criterion to [0, 1] within the sweep;
   combine with explicit weights (default equal) to a composite
   score.  Weights are a knob — sensitivity to ±50% perturbations
   is reported.

4. **Best-triplet-per-geometry and ranking.**  For each (ε_ν, s_ν),
   pick the triplet with highest composite score.  Then rank
   (ε_ν, s_ν) points by their best-triplet score.  Produce a
   shortlist of top 5–10 candidates.

5. **Per-candidate detail report.**  For each shortlisted
   (ε_ν, s_ν), emit: the distinguished triplet, all five sub-scores,
   absolute masses (calibrated so Δm²₂₁ = 7.53×10⁻⁵ eV²), the
   predicted Δm² comb (via Track 1's `delta_m2_comb`), and the
   individual L_z/ℏ for each mode in the triplet.

**Smoke tests.**

| # | Test | Expected outcome |
|---|------|-----------------|
| T5 | R49 formula + E₀ = 29.25 meV on Family A reproduces m₁ = 29.2, m₂ = 30.5, m₃ = 58.2 meV | < 0.1% relative error |
| T6 | `spin_Lz_over_hbar(0, 1, any ε)` = 1.0 | matches R49 F14 (pure-ring mode is spin 1) |
| T7 | `spin_Lz_over_hbar(1, 2, 5.0)` ≈ 0.37 | matches R49 F7 (Family A marginal spin) |
| T8 | Ranking at (ε=5.0, s=0.022) places Family A (1,1)(−1,1)(1,2) in top 3 under equal-weight scoring | Family A surfaces as a distinguished triplet |

**Deliverables.**

- `scripts/track2_candidates.py` — spin function, scorer, ranker,
  shortlist writer.  Imports Track 1's enumerator, pair filter,
  triplet finder, and comb predictor (after convention alignment).
- `outputs/track2_shortlist.md` — ranked table of top candidates
  with per-criterion scores.
- `outputs/track2_score_heatmap.png` — best-triplet composite
  score across (ε_ν, s_ν).
- `outputs/track2_top_candidates/` — one markdown file per top-5
  candidate with triplet identity, masses, comb, spins.
- `findings.md` F5–F8: smoke-test results, shortlist, weight-
  sensitivity audit, comparison of top candidates to R49's Family
  A/B/C assignments.

**Acceptance criteria.**

- All four smoke tests pass.
- Shortlist contains either Family A or a structurally similar
  near-Family-A triplet (sanity check that the ranker surfaces a
  known-good option).
- Top-5 candidates differ meaningfully in at least one criterion
  (not all clones of one region).
- Weight-sensitivity audit: ranking of the top candidate is stable
  under ±50% weight perturbations, or the instability is flagged
  explicitly as "no unique best."

**Prototyping note.**  Scripts stay local to R61.  Track 1's
primitives are re-exported from `track2_candidates.py` under the
aligned convention; Track 1's old script is kept for
reproducibility of the original zoo-density map but not used in
Track 2's computation path.

---


**Goal.**  Build a self-contained toolkit that (a) enumerates
±n_r-paired fermion modes on Ma_ν, (b) finds all triplets matching
the 33.6 ratio, (c) outputs the predicted Δm² comb from n_tube
transitions under a given E₀ calibration.  No selection rules yet —
this track establishes the raw spectrum and its measurable
consequences.  Later tracks impose filters.

**Strategy.**

One script, five primitives, four tests.  Keep the API small and
scriptable so later tracks import rather than copy-paste.  No
dependency on `lib/` — everything stays local to R61 until stable.

**Tactics.**

1. **Mode enumerator.**  `enumerate_modes(eps, s, nr_max, nt_max)`
   returns a list of `(n_r, n_t, mu2)` tuples for all integer modes
   with |n_r| ≤ nr_max, 0 ≤ n_t ≤ nt_max, using

       mu2(n_r, n_t) = (n_r · eps)² + (n_t − n_r · s)²

2. **Pair filter.**  `paired_fermion_modes(modes, eps, s, delta)`
   keeps modes with |n_r| ≥ 1 whose ±n_r partner exists in the list
   with µ² splitting below `delta` (dimensionless tolerance on
   splitting/mean).  Excludes n_r = 0 (spin 1) and any splittings
   too large to support Majorana mixing.

3. **Triplet finder.**  `find_ratio_triplets(modes, target, tol)`
   returns all triplets (a, b, c) with µ_a² < µ_b² < µ_c² satisfying
   (µ_c² − µ_a²) / (µ_b² − µ_a²) within `tol` of `target`.  Each
   triplet is reported with its three modes and the exact ratio.

4. **Comb predictor.**  `delta_m2_comb(eps, s, E0_sq, max_dn)`
   computes the cluster of Δm² values from n_tube transitions
   (a, b) with 1 ≤ a < b ≤ max_dn, averaged over low n_r.  Returns
   a list of (n_t_from, n_t_to, Δm²_mean, Δm²_spread).  These are
   predictions — positions fixed by integer structure once (eps, s,
   E0_sq) are set.

5. **Zoo density sweep.**  `zoo_sweep(eps_grid, s_grid, delta, tol,
   ratio_target)` returns a 2D array of counts: at each (eps, s),
   how many 33.6-matching paired-fermion triplets exist.  Identifies
   the populous regions.

**Smoke tests (infrastructure only).**

| # | Test | Expected outcome |
|---|------|-----------------|
| T1 | `enumerate_modes(5.0, 0.022, 3, 5)` reproduces R49 Family A µ² values | (1,1) = 25.957, (−1,1) = 26.045, (1,2) = 28.913 to < 10⁻⁶ |
| T2 | `paired_fermion_modes` at Family A parameters includes (±1,1), (±1,2), (±2,1), excludes all (0, n_t) | list contents match expected |
| T3 | `find_ratio_triplets` at Family A reproduces Family A triplet AND at least 10 other 33.6-matching triplets | ≥ 11 triplets returned, Family A (1,1)(−1,1)(1,2) present |
| T4 | `delta_m2_comb` at (5.0, 0.022, E₀² calibrated to Δm²₃₁ = 2.53×10⁻³ eV²) | n_t: 1→2 cluster at 2.53×10⁻³ eV²; 1→3 cluster at ≈ 6.77×10⁻³ eV² |

**Deliverables.**

- `scripts/track1_zoo.py` — primitives + smoke tests + a reference
  zoo sweep over (ε_ν ∈ [1, 10], s_ν ∈ [0.005, 0.1]) with a
  heatmap output.
- `findings.md` entries F1–F4 recording smoke-test results and an
  initial characterization of the zoo-density map.

**Acceptance criteria.**

- All four smoke tests pass at stated tolerances.
- Zoo sweep output contains a usable density map and a printed
  table of (eps, s, triplet_count) for the top 10 densest points.
- API is small enough to document in the findings (five functions).

**Prototyping note.**  Script and helpers stay inside
[scripts/track1_zoo.py](scripts/) for R61.  Promotion to `lib/` is
deferred until at least two later tracks import the primitives
unchanged.

---

## Next-track pool

Candidates for the next track after Track 1.  Sequence decided from
Track 1's outcome.  Entries are sketches; the chosen one is
elaborated to full-track detail when promoted.

**a. ~~Zoo-region characterization~~** — folded into Track 2.

**b. Comb vs anomalies.**  Compare the Δm² combs from the Track 2
shortlist against reported sterile-neutrino and oscillation anomalies
(LSND at Δm² ≈ 1 eV², DANSS, reactor antineutrino anomaly,
MicroBooNE).  Identify which (if any) anomalies land on a predicted
cluster for any of the top candidates.

**c. ~~Selection rule candidates~~** — partially folded into Track 2
(spin-½ quality as a scoring criterion).  Remaining work: apply
the R49 waveguide cutoff, energetic cutoff, and cross-sheet
coupling filters as additional scoring criteria or as hard
constraints that pre-filter the zoo before ranking.

**d. Charge cancellation proof.**  Under each candidate charge
mechanism — tube-winding (R48 CP synchronization), ring-winding
(Taxonomy Q = −n₁ + n₅ generalized to ν-sheet), shear-induced (R19)
— verify quantitatively that the ±n_r Majorana superposition gives
zero net charge.  Required for the "pair-cancels-charge" argument
to be more than narrative.

**e. Small-ε waveguide regime.**  Re-examine R49 Family B (ε = 0.1)
with the zoo lens.  Under a softer cutoff than R49's literal formula
(e.g. evanescence-based, frequency-based), does Family B's
all-paired triplet (±1,2), (±2,2), (±10,1) survive as the
distinguished triplet?

**f. R60 handoff.**  When R60 settles on a ν-sheet geometry via
its track (b), re-run R61's zoo analysis on that geometry.  Provides
the paired-mode structure inside the R60 metric, whatever it turns
out to be.

**g. Production coupling.**  Derive (or bound) the β-decay matrix
element for each zoo triplet — which triplets can be populated by
standard weak processes, and which are genuinely sterile.  This
is the most physically motivated selection candidate but requires
a weak-coupling model, which MaSt does not currently have in
derivable form.

**z. Closeout.**  If a selection rule from track (c) or (e)
isolates a distinguished triplet consistent with observation:
document the refined Family A (or Family A′) assignment and any
testable comb predictions.  If no rule works, document the gap as
the precise blocking constraint so future work can target it.

---

### Track 4 — Charge-neutrality scoring and harmonic flagging (complete)

See [findings.md §Track 4](findings.md#track-4-charge-neutrality-scoring-and-harmonic-flagging)
for F17–F20, smoke-test results (T13–T16), and the re-scored
shortlist.

**Scoring changes from Track 3:**
1. **Charge neutrality** replaces pair cleanliness.  Per-mode:
   uncharged via (a) \|n_tube\|=1 AND ±partner within delta
   (Majorana) or (b) \|n_tube\|≥2 (inherently uncharged per R48
   CP synchronization).  Triplet score = average.
2. **Charged-extras count** replaces sterile count.  Counts
   only modes in window that *would* carry charge (\|n_tube\|=1 and
   partner unpaired).  Dark extras aren't penalized, per user
   guidance: more dark modes is fine, possibly beneficial
   (threshold / storage capacity).
3. **Harmonic flag** (new).  If any two triplet members share
   signed reduced form (e.g., (−2,2) reduces to (−1,1) matching
   another member), score = 0.  Harmonics are flagged as
   redundant particle identities, not filtered from enumeration.

---

## Files

| File | Purpose |
|------|---------|
| README.md | This framing document |
| scripts/ | Computation scripts (per track, local to R61) |
| findings.md | Results (after computation) |
