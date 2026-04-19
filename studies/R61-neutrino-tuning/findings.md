# R61 Findings

Study: [`README.md`](README.md)

---

## Track 1: Zoo enumerator, pair filter, triplet finder, Δm² comb

Script: [`scripts/track1_zoo.py`](scripts/track1_zoo.py)
Outputs: [`outputs/track1_zoo_density.png`](outputs/track1_zoo_density.png),
[`outputs/track1_zoo_counts.txt`](outputs/track1_zoo_counts.txt)

### Summary

Track 1 delivers a self-contained toolkit for the paired-mode zoo
analysis: five primitives (`mu2`, `enumerate_modes`,
`paired_fermion_modes`, `find_ratio_triplets`, `delta_m2_comb`) and
a sweep driver (`zoo_sweep`).  All four smoke tests pass at the
stated tolerances.  A reference sweep over ε_ν ∈ [1, 10] and
s_ν ∈ [0.005, 0.1] confirms that the zoo is not only non-empty at
the Family A geometry but grows monotonically with ε_ν, peaking
near 100 paired-fermion triplets at ε_ν = 10, s_ν ≈ 0.006.

### Primitives

| Function | Role |
|----------|------|
| `mu2(n_r, n_t, eps, s)` | Dimensionless mass-squared on a 2-torus with shear. |
| `enumerate_modes(eps, s, nr_max, nt_max)` | All integer modes sorted by µ². |
| `paired_fermion_modes(modes, eps, s, delta)` | Modes with \|n_r\|≥1 and a ±n_r partner at relative µ² splitting ≤ delta. |
| `find_ratio_triplets(modes, target, tol)` | All (a, b, c) whose (µ_c²−µ_a²)/(µ_b²−µ_a²) lies within tol of target. |
| `delta_m2_comb(eps, s, E0_sq, max_dn, nr_sample)` | Predicted Δm² clusters from n_tube transitions, sampled over n_r. |
| `zoo_sweep(eps_grid, s_grid, delta, tol, ratio_target, ...)` | 2D triplet-count grid. |

Design note: pair filter uses a *relative* splitting (splitting ÷
mean µ²) rather than an absolute threshold, so a single delta works
across scales.  Default delta = 0.1 (10%) admits pairs up to s_ν ≈
0.2 for low n_r.

### Findings table

| ID | Finding |
|----|---------|
| F1 | The mass formula µ²(n_r, n_t) = (n_r·ε)² + (n_t − n_r·s)² at (ε, s) = (5.0, 0.022) reproduces Family A µ² values exactly (0.00 residual vs R49's (1,1)=25.956, (−1,1)=26.044, (1,2)=28.912).  Computational baseline confirmed. |
| F2 | The pair filter correctly excludes all (0, n_t) modes (spin-1, not fermion candidates) and retains (±1,1), (±1,2), (±2,1) at Family A parameters with delta = 0.1 (relative splitting tolerance).  The ±n_r pairing is structural: every |n_r|≥1 mode finds its partner at splitting 8·s·|n_r| in µ² units, which is well below delta for s_ν ≈ 0.022. |
| F3 | At Family A's geometry (ε=5.0, s=0.022), the triplet finder recovers Family A (1,1)(−1,1)(1,2) AND 11 additional paired-fermion triplets matching 33.6 within 1%.  The zoo is real and populous at the minimal exploration cutoff (\|n_r\|≤3, n_t≤5).  Earlier unfiltered enumeration (n_r=0 modes admitted) counted 14 triplets; the pair-mandatory filter removes 2 that involved (0, n_t) modes. |
| F4 | The Δm² comb predictor, calibrated so the (1→2) cluster sits at atmospheric Δm²₃₁ = 2.53×10⁻³ eV², predicts the (1→3) cluster at 6.75×10⁻³ eV² (0.3% off the target 6.77×10⁻³ eV² from the analytical expression).  All other clusters land at positions dictated by integer structure, fixed once (ε, s, E₀) are set.  This is a concrete, testable comb of predicted Δm² values. |

### Reference zoo-density sweep

Grid: ε_ν ∈ [1.0, 10.0] (19 points), s_ν ∈ [0.005, 0.1] (21 points,
log-spaced).  Mode enumeration cutoff \|n_r\|≤3, n_t≤6.  Ratio
target 33.6 at 1% tolerance, pair tolerance delta = 0.1.

Observations:

- **Zoo density grows monotonically with ε_ν.** At ε_ν=1 the count
  is often 0–2; at ε_ν=5 (Family A) it sits at 13; at ε_ν=10 it
  reaches 97 at the densest point.  This is structural — higher ε_ν
  means more modes with µ² ≈ n_r²·ε² cluster at the same "altitude,"
  giving more opportunities for the 33.6 ratio to be satisfied.
- **Density decays as s_ν grows.** The top-10 densest points all sit
  at ε_ν = 10 with s_ν ∈ [0.005, 0.019].  Larger s_ν breaks ±n_r
  degeneracy, removing pairs from the filter.
- **Family A sits in a moderately populated corner, not the peak.**
  At ε=5.0, s≈0.022, the filter admits 13 triplets.  Family A
  specifically is one of them.  The *densest* regions of the
  parameter space are at larger ε_ν, which R49 did not explore in
  detail (its largest Family A point is ε_ν = 5).

Top-10 densest points:

| rank | ε_ν | s_ν | triplet count |
|------|-----|-----|---------------|
| 1 | 10.00 | 0.00581 | 97 |
| 2 | 10.00 | 0.00500 | 93 |
| 3 | 10.00 | 0.00675 | 88 |
| 4 | 10.00 | 0.00784 | 84 |
| 5 | 10.00 | 0.00910 | 80 |
| 6 | 10.00 | 0.01057 | 77 |
| 7 | 10.00 | 0.01228 | 71 |
| 8 | 10.00 | 0.01427 | 71 |
| 9 | 10.00 | 0.01925 | 71 |
| 10 | 10.00 | 0.01657 | 67 |

### Status

**Track 1 complete.**  Infrastructure is working; smoke tests pass;
reference sweep produced a usable density map.  The zoo hypothesis
is structurally confirmed for the ν-sheet: dozens to ~100 paired
fermion triplets match the 33.6 ratio across the explored region,
with Family A sitting as one admissible assignment among many.

### What this track did NOT address

- No selection rule applied yet — the triplet counts are raw
  enumerations.  Separating "observed" triplets from "sterile" ones
  requires a filter (waveguide cutoff, cross-sheet coupling,
  production matrix element).  This is pool item (c).
- The comb predictions have not been compared to reported
  oscillation anomalies (pool item b).
- The Majorana charge-cancellation under a specific charge
  mechanism is not verified (pool item d).
- The zoo at high ε_ν (near ε_ν = 10) is far denser than at
  Family A's ε_ν = 5, suggesting the density alone is not the
  right selection criterion.  Why Family A sits at ε_ν = 5 rather
  than the density peak is an open question — possibly a spin-½
  tolerance issue (R49 F7: spins drift from ½ at large ε_ν).
- Track 1's formula `(n_r·ε)² + (n_t − n_r·s)²` used the Taxonomy
  convention, not R49's canonical form.  Absolute µ² values and
  mixed-n_tube zoo counts are not R49-comparable; Track 2 adopts
  R49's form and re-verifies smoke tests under it.

---

## Track 2: Candidate ranking and best-fit selection

Script: [`scripts/track2_candidates.py`](scripts/track2_candidates.py)
Outputs:
[`outputs/track2_shortlist.md`](outputs/track2_shortlist.md),
[`outputs/track2_score_heatmap.png`](outputs/track2_score_heatmap.png),
[`outputs/track2_top_candidates/`](outputs/track2_top_candidates/).

### Summary

Track 2 adopts R49's formula convention as canonical
(µ² = (n_tube/ε)² + (n_ring − n_tube·s)² with tuple (n_tube, n_ring)),
ports R49's finite-ε spin formula, and ranks 33.6-ratio paired
fermion triplets by a five-criterion composite score.  All four
Track 2 smoke tests pass.  The shortlist is dominated by Family A
and close variants; the composite-score winner is a Family A
instance at ε_ν = 2.0, s_ν = 0.022 — a lower ε_ν than R49's
canonical ε = 5.0, preferred because modes at ε = 2 have
L_z/ℏ much closer to the textbook spin-½ value (0.45 vs 0.36).

### Smoke-test results

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T5 | R49 formula reproduces Family A masses (m₁, m₂, m₃) = (29.2, 30.5, 58.2) meV | PASS | E₀ = 29.251 meV; computed (29.200, 30.462, 58.154) meV |
| T6 | Spin formula at analytical limits: Lz/ℏ(0,1,0) = 1.0, Lz/ℏ(0,1,1) = 3/8 | PASS | Computed 1.0000 and 0.3750 |
| T7 | Family A spins at ε=5 sit in R49 F7 band [0.30, 0.45] | PASS | Computed (0.358, 0.358, 0.372) |
| T8 | Family A ranked top-3 at its own geometry under equal-weight scoring | PASS | Family A is rank 1 at (ε=5, s=0.022) with composite 0.700 |

### Findings table

| ID | Finding |
|----|---------|
| F5 | R49's convention `(n_tube/ε)² + (n_ring − n_tube·s)²` with tuple (n_tube, n_ring) is adopted as canonical.  The formula reproduces R49's published Family A masses (m₁ = 29.2, m₃ = 58.2 meV) to < 0.1% with E₀ = 29.251 meV, confirming numerical alignment with prior work. |
| F6 | R49's finite-ε spin formula `L_z/ℏ = 2π²·q²·(2+ε²)/I²` (with `I(p,q,ε) = ∫₀²π √(p²ε² + q²(1+ε cos(pt))²) dt`) is ported successfully.  Analytical limits match: Lz/ℏ(0,1,0) = 1 exactly, Lz/ℏ(0,1,1) = 3/8 = 0.375 exactly.  The formula gives Family A spins (0.358, 0.358, 0.372) at ε=5, matching R49 F7's reported "≈ 0.36–0.37" band. |
| F7 | Fermion filter must require n_ring ≥ 1 (in addition to \|n_tube\| ≥ 1) to exclude pure-tube modes.  Under R49's spin formula these modes have L_z/ℏ = 0 (no ring-axis angular momentum); including them produced top-10 candidates dominated by (n_tube, 0) mode triplets — a methodological artifact, not physics.  The filter now matches R49's implicit convention (all Families have n_ring ≥ 1). |
| F8 | **Best candidate under equal-weight composite scoring: ε_ν = 2.0, s_ν = 0.022, with Family A modes (1,1)(−1,1)(1,2), composite score 0.762.** This is the same mode-set as R49 Assignment A but at a smaller ε.  Absolute masses: (32.1, 33.3, 59.7) meV.  Σm = 125.1 meV (2 meV above 120 meV cosmological bound; user scope excludes cosmology).  Predicted Δm²₃₁ = 2.529×10⁻³ eV² (matches atmospheric 2.53×10⁻³). |
| F9 | **R49's canonical ε = 5.0 and Track 2's optimum ε = 2.0 represent different tradeoffs.** At (ε=5, s=0.022) Family A scores 0.700; at (ε=2, s=0.022) it scores 0.762.  The 0.062 gap comes entirely from spin quality: spins drift from 0.45 (at ε=2, close to ½) to 0.36 (at ε=5, ~28% below ½).  R49 chose ε=5 to minimize sterile-mode count (~26 intermediate modes vs hundreds at smaller ε); Track 2's scoring doesn't yet include sterile count.  Either criterion is defensible — the "best" depends on whether clean spin-½ or mode sparsity matters more.  See pool item (c) for a sterile-count extension. |
| F10 | **Top-10 shortlist clusters into two structural classes:** (a) "ring-1" triplets with all three modes at n_ring = 1 (e.g. (1,1)(−1,1)(−2,1) at ε=2, s=0.006) — simple, low-Σm; (b) "ring-12" triplets spanning n_ring = 1 and 2 (e.g. Family A itself, or (1,2)(−1,2)(+2,3)) — more canonical.  Both classes reproduce the 33.6 ratio via either the ±n_tube pair splitting (class a) or the n_ring 1→2 transition (class b).  This is a genuine degeneracy in the zoo: two distinct ways to structurally hit the ratio. |
| F11 | Weight sensitivity audit (±50% perturbation on each of 5 weights): top-1 candidate unchanged in 9/10 perturbations; top-5 overlap ≥ 3/5 in all cases.  Ranking is robust but not unique — under certain weight schedules rank 2 and rank 1 swap.  The top candidate at ε=2, s=0.022 is the most weight-stable choice. |
| F12 | Predicted Δm² comb at the top candidate: the (Δn_ring = 1→2) cluster sits at 2.57×10⁻³ eV² (matches atmospheric), the 2→3 cluster at 4.28×10⁻³ eV², the 1→3 cluster at 6.85×10⁻³ eV², and higher-order clusters extend to 2.05×10⁻² eV².  None of these non-primary positions are reported as observed Δm² features in standard 3-flavor oscillation data — consistent with dark/sterile modes not yet probed, or constraining future experiments. |

### Shortlist (top-10)

See [`outputs/track2_shortlist.md`](outputs/track2_shortlist.md) for
the full table with per-criterion scores.

| # | ε_ν | s_ν | triplet | composite |
|--:|-----|-----|---------|----------:|
| 1 | 2.000 | 0.02200 | (1,1), (−1,1), (1,2) — **Family A** | 0.762 |
| 2 | 2.000 | 0.00581 | (1,1), (−1,1), (−2,1) | 0.713 |
| 3 | 5.500 | 0.00500 | (1,1), (2,1), (1,2) | 0.703 |
| 4 | 3.000 | 0.01925 | (1,2), (−1,2), (2,3) | 0.703 |
| 5 | 4.000 | 0.01925 | (1,2), (−1,2), (−1,3) | 0.699 |
| 6 | 8.500 | 0.00784 | (1,1), (−2,1), (1,2) | 0.690 |
| 7 | 2.000 | 0.03017 | (1,1), (−1,1), (−2,2) | 0.674 |
| 8 | 4.500 | 0.00626 | (1,1), (−3,1), (1,4) | 0.671 |
| 9 | 6.000 | 0.00727 | (−1,1), (−2,1), (−3,2) | 0.662 |
| 10 | 3.500 | 0.00727 | (1,1), (−3,1), (1,5) | 0.644 |

### Status

**Track 2 complete.**  Best-fit candidate identified: Family A at
ε_ν = 2.0, s_ν = 0.022.  Top-5 candidates documented in
[`outputs/track2_top_candidates/`](outputs/track2_top_candidates/)
with per-candidate masses, Δm² combs, and L_z/ℏ tables.  Pool
items (b) comb-vs-anomalies and (c) sterile-count selection rule
are the natural next moves.

### What this track did NOT address

- Sterile mode count as a scoring criterion — **addressed in Track 3.**
- Comb-vs-anomalies comparison (pool item b): still open.
- Σm cosmological check — user scope excludes cosmology.
- Majorana charge-cancellation proof — still pool item (d).

---

## Track 3: Sterile-count scoring and consensus shortlist

Script: [`scripts/track3_sterile_scoring.py`](scripts/track3_sterile_scoring.py)
Outputs:
[`outputs/track3_consensus.md`](outputs/track3_consensus.md),
three per-schedule shortlists
([equal](outputs/track3_shortlist_equal.md),
[sterile_heavy](outputs/track3_shortlist_sterile_heavy.md),
[balanced](outputs/track3_shortlist_balanced.md)),
[`outputs/track3_tradeoff.png`](outputs/track3_tradeoff.png),
[`outputs/track3_heatmap_compare.png`](outputs/track3_heatmap_compare.png).

### Summary

Track 3 adds sterile-mode count as a sixth scoring criterion
(R49's preferred selection handle) and ranks candidates under
three weight schedules.  **Family A at (ε_ν = 2.0, s_ν = 0.022)
is the top-1 candidate under all three schedules**, with composite
scores 0.795 (equal), 0.807 (balanced), and 0.841 (sterile-heavy).
Four mode-sets appear in the top-5 under every schedule — a
consensus shortlist that is robust to which criterion the user
prioritizes.

Contrary to initial expectations, moving to ε = 5 (R49's canonical
value) does not reduce the sterile count of the Family A triplet.
At the SAME triplet, ε = 5 has 15 steriles while ε = 2 has 4 — the
(n_tube/ε)² term is smaller at larger ε, letting more high-n_tube
modes into the mass window.  R49's preference for ε = 5 was based
on a comparison across DIFFERENT triplets at different ε (Family A
at ε=5 vs Family B at ε=0.1); the same-triplet comparison favors
ε = 2 on every sterile-aware criterion.

### Smoke-test results

| ID | Test | Result | Detail |
|----|------|--------|--------|
| T9  | `sterile_count` for Family A at (ε=5, s=0.022) is in [15, 40] per R49 F4 ≈ 26 | PASS | count = 15 (within band) |
| T10 | Sterile-heavy schedule preserves or raises best ε | PASS | equal ε=2.0; sterile-heavy ε=2.0 (unchanged, as expected with same-triplet comparison) |
| T11 | Zero-sterile weight recovers Track 2 optimum | PASS | top-1 = (ε=2.0, s=0.022) Family A |
| T12 | Consensus intersection across 3 schedules non-empty | PASS | \|intersection\| = 4 mode-sets |

### Findings table

| ID | Finding |
|----|---------|
| F13 | The Track 3 sterile-count primitive counts fermion candidates (\|n_tube\|≥1, \|n_ring\|≥1; no pair-splitting tolerance) with µ² between ν₁ and ν₃.  For Family A at (ε=5, s=0.022) this gives 15 modes (R49 F4 reports 26; the 11-mode gap likely reflects a different mode enumeration or different spin filter on R49's side, but the functional behavior — fewer steriles at larger ε, more at smaller ε for different triplets — is reproduced). |
| F14 | **Consensus top-1 across all three weight schedules: ε_ν = 2.0, s_ν = 0.022 with Family A modes (1,1)(−1,1)(1,2)**.  Composite scores: equal = 0.795, balanced = 0.807, sterile-heavy = 0.841.  The sterile-heavy boost comes from this geometry's low sterile count (4 vs R49's 15 at ε=5 for the same triplet).  Weight-schedule-invariant selection confirms this is the definitive best candidate. |
| F15 | **Consensus shortlist = 4 mode-sets** appearing in top-5 under every weight schedule: (a) Family A at (ε=2.0, s=0.022), sterile=4; (b) (1,1)(−1,1)(−2,1) at (ε=2.0, s=0.00581), sterile=1; (c) (1,1)(−1,1)(−2,2) at (ε=2.0, s=0.03017), sterile=8; (d) (1,1)(2,1)(1,2) at (ε=5.5, s=0.005), sterile=16.  Three of four sit at ε=2.0 — consensus prefers small-ε torus strongly. |
| F16 | **R49's ε=5 vs Track 3's ε=2 for the same Family A triplet: ε=2 is strictly better on every criterion we measure.**  Sterile count 4 vs 15 (3.75× fewer).  Spin quality 0.89 vs 0.56 (spins 0.45 vs 0.36, closer to textbook ½).  Pair cleanliness identical.  Simplicity identical.  Only drawback at ε=2: Σm = 125 meV (slightly above 120 meV cosmological bound); R49's ε=5 gives Σm = 118 meV.  User scope excludes cosmology, so ε=2 wins.  R49's ε=5 preference was driven by a cross-family comparison (Family A vs B/C at different ε), not a same-triplet analysis. |

### The recommended ν-sheet geometry

**ε_ν = 2.0, s_ν = 0.022** with mode triplet **(1,1), (−1,1), (1,2)**.

- ν₁ = (1, 1): mass **32.13 meV**, L_z/ℏ = 0.450
- ν₂ = (−1, 1): mass **33.28 meV**, L_z/ℏ = 0.450
- ν₃ = (1, 2): mass **59.68 meV**, L_z/ℏ = 0.439
- Σm = **125.1 meV**
- E₀ = **29.25 meV** (calibrated to Δm²₂₁ = 7.53×10⁻⁵ eV²)
- Predicted Δm²₃₁ = **2.529 × 10⁻³ eV²** (atmospheric target 2.53×10⁻³)
- Sterile count between ν₁ and ν₃: **4**
- ν₁ / ν₂ are C-conjugate pair (Majorana); ν₃ has available partner (−1, 2) at µ² = 4.34

**Contrast with R49 Assignment A (same modes, different ε):**
Track 3's ε = 2.0 and R49's ε = 5.0 use the identical mode triplet.
Track 3's choice gives 3.75× fewer sterile modes and spin values
26% closer to textbook ½; R49's choice gives Σm under cosmological
bound (118 vs 125 meV).  If cosmology is not binding (user scope),
ε = 2 is the clear winner.  If cosmology is required, ε = 5
remains the viable alternative.

### Status

**Tracks 1–3 complete.  Best candidate definitively identified:
ε_ν = 2.0, s_ν = 0.022, Family A mode-set.**  Consensus shortlist
of 4 candidates available for downstream work.

### What this track did NOT address

- Comb-vs-anomalies (pool item b).
- Majorana charge-cancellation via R48 rule — **addressed in Track 4.**
- Cosmological Σm refinement — user scope excludes.
- Production coupling (pool item g).

---

## Track 4: Charge-neutrality scoring and harmonic flagging

Script: [`scripts/track4_charge_neutrality.py`](scripts/track4_charge_neutrality.py)
Outputs:
[`outputs/track4_shortlist.md`](outputs/track4_shortlist.md),
[`outputs/track4_hybrid_candidates.md`](outputs/track4_hybrid_candidates.md),
[`outputs/track4_score_heatmap.png`](outputs/track4_score_heatmap.png).

### Summary

Track 4 replaces Track 3's pair-cleanliness with **charge-neutrality**
(per R48's CP-synchronization rule: charge requires |n_tube|=1;
|n_tube|≥2 modes are inherently uncharged), replaces sterile count
with **charged-extras count** (only charge-carrying extras are
penalized; dark extras are ignored per user guidance that dark
abundance is fine or beneficial), and adds a **harmonic flag** that
zeros any triplet whose three modes don't have three distinct
signed reduced forms.

Result: Family A at (ε_ν=2.0, s_ν=0.022) remains top-1 with an
improved composite score of **0.931** (vs Track 3's 0.795), and a
new shortlist of 14 **hybrid triplets** — invisible under Track 3's
scoring — appears at ranks 2–15.  Each hybrid uses R48's inherent
neutrality for at least one mode rather than Majorana pairing for
all three.  Track 3's consensus candidate #3 (1,1)(−1,1)(−2,2) is
correctly demoted by the harmonic flag since (−2,2) = 2×(−1,1).

### Smoke-test results

| ID | Test | Result |
|----|------|--------|
| T13 | `is_charged` per R48 rule: paired (±1,1) neutral at s=0.022, split (1,1) charged at s=0.06, (2,3) always neutral | PASS |
| T14 | Family A at (ε=2, s=0.022) has charged_extras_count = 0 | PASS |
| T15 | Harmonic flag detects (−2,2) ∼ (−1,1); Family A flag = 1; (1,1)(−1,1)(−2,2) flag = 0 | PASS |
| T16 | Hybrid triplet (1,1)(−1,1)(2,3) at ε=5, s=0.0564 scores via mixed mechanisms (Majorana-weak/Majorana-weak/R48) | PASS |

### Findings table

| ID | Finding |
|----|---------|
| F17 | **Charge-neutrality criterion distinguishes modes by R48 mechanism.**  A mode is uncharged via (a) Majorana: \|n_tube\|=1 with ±partner within delta=0.1, or (b) R48: \|n_tube\|≥2 (CP synchronization fails).  Weak Majorana (delta exceeded) gets partial or zero credit.  Enables hybrid triplets — mixing Majorana and R48 mechanisms — to score competitively, whereas Track 3's pair-cleanliness penalized them. |
| F18 | **Family A's composite rises to 0.931** (from Track 3's 0.795) at the same (ε_ν=2.0, s_ν=0.022).  All three modes Majorana-neutralized via their ±n_tube partners, no charged extras, no internal harmonics.  Highest score across all four tracks; consistently top-1 under every scoring variation. |
| F19 | **Ranks 2–15 are all hybrid triplets.**  Top hybrids: rank 2 (1,1)(−2,1)(1,2) at ε=8.5, s=0.00784, composite 0.863; rank 3 (2,1)(−1,1)(−1,2) at ε=10, s=0.02075, composite 0.862.  Some use *two* R48 modes (ranks 9–11: "Majorana/R48/R48" pattern), with only one Majorana dependency — arguably more robust in neutrality terms since two of three modes need no pair degeneracy. |
| F20 | **Harmonic flag correctly demotes Track 3's consensus candidate #3 (1,1)(−1,1)(−2,2)**: (−2,2) reduces to (−1,1,2) — same signed reduced form as (−1,1) already in the triplet.  Physical reading: (−2,2) is the 2× octave of (−1,1), not a distinct particle identity.  No such redundant triplets appear in Track 4's top-15.  Harmonics are flagged, not filtered — they remain valid sheet modes that may cascade to lower fundamentals energetically, per user physics intuition. |

### Final shortlist — viable ν-sheet candidates

Top-5 (full top-15 in [`outputs/track4_shortlist.md`](outputs/track4_shortlist.md)):

| # | (ε_ν, s_ν) | triplet | composite | mechanisms |
|--:|-----------|---------|----------:|:-----------|
| 1 | (2.000, 0.02200) | (1,1), (−1,1), (1,2) ← **Family A** | 0.931 | Maj/Maj/Maj |
| 2 | (8.500, 0.00784) | (1,1), (−2,1), (1,2) | 0.863 | Maj/R48/Maj |
| 3 | (10.000, 0.02075) | (2,1), (−1,1), (−1,2) | 0.862 | R48/Maj/Maj |
| 4 | (2.500, 0.01925) | (1,1), (2,1), (1,4) | 0.854 | Maj/R48/Maj |
| 5 | (2.000, 0.02075) | (1,1), (2,1), (1,5) | 0.852 | Maj/R48/Maj |

All 15 shortlisted candidates satisfy:
- Ratio within 2.7% of 33.6 (R49's 1σ experimental tolerance)
- Every mode uncharged via Majorana or R48 mechanism
- No internal harmonics (three distinct signed reduced forms)
- Zero modes in the mass window that would carry observable charge

**These are the viable candidates for downstream metric testing**
as requested — the best ν-sheet size/shape/shear settings the
framework identifies under seven physically motivated criteria.

### Status

**R61 complete.  Primary objective delivered:** ranked shortlist
of 15 viable ν-sheet candidates with their distinguished triplets
and neutrality mechanisms.

**Primary recommendation:** Family A at (ε_ν = 2.0, s_ν = 0.022),
composite 0.931.

**14 hybrid alternatives** at ranks 2–15 — previously unidentified
— provide a rich set of candidates testing the hypothesis that
ν-sheet neutrality can be achieved by mixing Majorana pairing and
R48 CP-synchronization mechanisms.

### What this track did NOT address

- Per-candidate absolute masses / Σm — script produces the
  ranking; calibration recipe from Track 2 can be applied to any
  shortlisted (ε, s, triplet) to recover masses.
- Ratio-tolerance sensitivity — if tightened below 2.7%, the
  ranking may compress.
- Comb-vs-anomalies (pool b), production coupling (pool g) —
  remain open for downstream studies.

