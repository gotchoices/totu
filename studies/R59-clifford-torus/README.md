# R59: A self-consistent metric with time

**Status:** Complete — see [findings.md](findings.md) for outcomes
**Background:** [background.md](background.md)
**Metric reference:** [metric-terms.md](metric-terms.md)
**Review:** [review.md](review.md)
**Type:** theoretical + compute
**Depends on:** R55 (ℵ-mediated coupling), R54 (particle inventory),
  R53 (generations),
  [sim-impedance](../../grid/sim-impedance/) (charge from bending, Tracks 8–12),
  GRID (lattice substrate)

---

## Goal

Find a single metric that simultaneously:

1. **Predicts the known particle spectrum** (model-E already
   does this with the flat 6D Ma metric + internal shears)
2. **Models the Ma-St coupling correctly** at strength α = 1/137
   (R55 partially achieved this with ℵ mediation, 3.6% gap)

The key new element: **add the time dimension to the metric.**
Model-E and R55 used a purely spatial metric (6 Ma + 3 S, or
+1 ℵ). Without time, the only coupling mechanism available was
the 3D bending of the torus surface (R19, sim-impedance) or
ℵ-mediation (R55). Adding time opens the Kaluza-Klein coupling
mechanism: off-diagonal metric entries between Ma and t produce
the electromagnetic potential directly — in principle.

## Strategy

1. Start with the model-E flat Ma metric (which gives the
   correct particle spectrum)
2. Add time to the metric, making it (6 Ma + 3 S + 1 t = 10D),
   or 11D if ℵ is included
3. Introduce Ma-t off-diagonal entries (the KK coupling)
4. Determine whether these entries can be set to produce
   α = 1/137 universally — for electron, proton, and all
   charged modes
5. Check that the particle spectrum is not disrupted

If a single Ma-t entry (or a small number of entries) sets α
without disturbing the particle spectrum, we have a self-
consistent metric. If ℵ is needed, it adds one row/column. If
it's not needed, the metric is simpler.

## The coupling question (open)

Whether the coupling goes through ℵ (R55 approach), through
direct Ma-t entries (KK approach), or both, is an open question
at framing time. This study tests the time-based approach. If
it works without ℵ, that's the simpler solution. If ℵ is still
needed, the time dimension may still improve the 3.6%
universality gap from R55.

## EM as spacetime geometry (hypothesis)

A secondary question: if the Ma-t coupling produces the
electromagnetic field in St, does the resulting force reproduce
the Coulomb law via geodesic deviation? Specifically:

- Opposite Ma windings → fields cancel between charges →
  geodesics converge → **attraction**
- Same Ma windings → fields reinforce →
  geodesics diverge → **repulsion**

This would geometrize EM the same way Einstein geometrized
gravity. It is a hypothesis to be tested, not an assertion.

---

## Note on the flat metric (Clifford torus)

Model-E's particle spectrum uses a flat 2-torus metric for
each sheet. This is intrinsically the Clifford torus — no
bending, no self-intersection, any aspect ratio valid.

Model-E's charge and α mechanisms (R19, R48, sim-impedance)
use 3D embedding with bending. This study proposes to
replace those with the KK mechanism (Ma-t coupling), which
works on the flat metric directly. If successful, the 3D
embedding becomes a visualization aid, not physics.

See [background.md](background.md) for detailed discussion
of the Clifford torus, the 3D embedding problems, and the
relationship to model-E.

---

## What changes from model-E's 3D embedding

Model-E's particle spectrum uses a flat metric, but its charge
and coupling mechanisms use 3D embedding. R59 proposes to move
everything to the intrinsic flat geometry + KK coupling. The
table compares the two approaches.

| Feature | 3D visualization | Intrinsic (Clifford) | Type of change |
|---------|-----------------|---------------------|----------------|
| Extrinsic curvature | Nonzero (inner/outer) | Zero (flat) | Artifact removed |
| Self-intersection | Fails when a > R | Any aspect ratio valid | Artifact removed |
| Tube-ring mixing | cos(θ₁) factor | Zero | Artifact removed |
| Metric saturation | e-sheet at PD limit | No saturation | Artifact removed |
| EM from curvature | Not available | Hypothesis: Ma-St coupling → Coulomb | **New physics (R59)** |
| Time in metric | Absent | Included via KK | **New physics (R59)** |

---

## Open questions

1. **Does the Clifford embedding need ℵ?** R55 Track 3 used ℵ
   to mediate Ma-S coupling (3.6% universality gap). If the
   time dimension provides the coupling via KK reduction, ℵ
   may be redundant — or it may be the microscopic mechanism
   that the time-based coupling implements at the lattice
   scale. To be determined.

2. **Which circle couples to time?** If the torus embeds in
   spacetime, one circle is spatial and one involves time. Is
   it the tube (charge direction) or the ring (mass/frequency
   direction)? The KK picture suggests the tube couples to t
   (producing the electric potential g₅₀). But the ring might
   also couple (producing the magnetic potential).

3. **Where does α appear?** In KK theory (compact momentum
   model), α comes from the ratio of the compact dimension's
   size to the Planck length. Whether this carries over to
   MaSt (standing-wave model) is unknown. α might come from
   a Ma-t off-diagonal entry, from the ℵ-t entry, or from a
   different mechanism entirely. A single entry setting α
   would be the cleanest result.

---

## Tracks

### Track 1: Direct Ma-t coupling on model-E

Extend the model-E 6D Ma metric to 10D (6 Ma + 3 S + 1 t).
Introduce Ma-t off-diagonal entries. Tune σ so that a
mass-shell "α_eff" matches observed α. Check universality
across electron, proton, and other modes. Verify the particle
spectrum is not disrupted.

**Preliminary step:** verify that the model-E 6D Ma metric
(flat, with internal shears) produces the correct particle
spectrum before any coupling is added. This is a sanity
check, not a derivation — the flat metric is known to work.

### Track 1b: ℵ-mediated time coupling (11D)

Route the coupling through ℵ instead of directly: Ma ↔ ℵ ↔ t
chain on an 11D metric. Compare to Track 1's direct Ma-t
architecture. Test whether ℵ mediation improves the
universality gap or the mass-direction physics.

### Track 1c: Minimal single sheet

Strip the metric to a single electron sheet + ℵ + S + t. Test
both coupling architectures (D1 = direct ring-t, D2 =
ℵ-mediated) on this minimal system. Check whether the coupling
entries conflict with the particle-spectrum entries (tubes and
internal shear). Verify that generation structure is preserved.

### Track 1d: Two sheets (electron + proton)

Add the proton sheet to the minimal system. Test whether
cross-sheet coupling interferes or whether the two sheets
operate independently. Measure universality on the two-sheet
system and compare to single-sheet and full model-E results.

### Track 1e: Root-selection diagnostics

Investigate the sign-direction concern raised during Track 1
(apparent mass decrease under coupling). Three diagnostics:
(a) which quadratic root is "the particle" under a consistent
charge-sign definition, (b) whether the standard Coulomb
self-energy matches the mass-shell shift in magnitude, and
(c) whether flipping the metric signature convention changes
the sign.

### Track 3: Shear architecture test bed

Systematic test bed over a catalog of shear architectures. For
each, build the full N×N metric, check signature + spectrum
preservation, and extract α_eff via three complementary
measures: (a) mass-shell shift, (b) inverse-metric gauge, (c)
spatial coefficient.

Architectures: internal cross shear, Ma-S direct, ℵ-mediated
to S, ℵ-mediated to t, direct Ma-tube ↔ t, direct Ma-ring ↔ t
(at σ = α and σ = √α each).

No tuning — each architecture's α_eff is determined by its
input shears and model-E's geometry.

### Track 3b: Spatial field solve — the Coulomb test

Compute the spatial field δg_{Ma,t}(r) directly by solving
Poisson's equation in S for a localized source. Extract the
1/r coefficient at r ≫ L_Ma and compare to α × (source charge).
This is the definitive test that distinguishes mass-shell
α_eff from the Coulomb coupling.

Covers multiple architectures: direct Ma-t, ring-based
ℵ-mediation, tube-based ℵ-mediation on model-E, tube-based
ℵ-mediation on a shearless clean metric, and a mixed
architecture (tubes via ℵ + rings direct).

### Track 3c: Precision tune on the clean-metric tube-ℵ-t architecture

Track 3b F42 reported tube-based ℵ mediation on a shearless Ma
metric giving "α_Coulomb ≈ 0.68α at (σ_ta, σ_at, g_ℵℵ) = (√α, 1, 1)"
with exact structural universality. Track 3c performs a precision
parameter sweep to find what values actually give α_Coulomb = α
and whether those values take a natural form.

Approach:
1. Fix the architecture (clean Ma + tube↔ℵ, ℵ↔t, symmetric
   signs for e/p).
2. Sweep (σ_ta, σ_at, g_ℵℵ) systematically.
3. Find the combination(s) that give α_Coulomb = α to ≤ 1 %.
4. Analyze: does the tuned point take a simple expression
   (pure √α, small integer ratios, etc.) or require arbitrary
   numerical values?

Acceptance criteria:
- α_Coulomb = α to within 1 % across electron and proton
- Metric signature preserved
- Structural universality (α_e / α_p = 1.000) maintained

See findings.md §Track 3c for outcome.

### Track 3d: Direct tube↔t on a clean metric (no ℵ)

R59 has not tested the simplest possible architecture for α
coupling: direct tube↔t off-diagonal on a clean (shearless) Ma
metric, with no ℵ dimension. Track 3a/3b tested ring↔t direct on
model-E (failed spatially) and tube↔ℵ↔t (universality real, α
magnitude needs fine-tuning). The pure tube↔t direct case on a
clean metric was skipped.

Question this track resolves: **is ℵ in the coupling loop, or out?**

If direct tube↔t on a clean metric gives α_Coulomb = α at a
natural σ value, ℵ is not needed for the coupling and the
architecture simplifies. If it fails (signature breaks, or the
required σ is unnatural), ℵ stays in the loop.

Approach:
1. Build 10D metric: clean Ma identity + flat S + Lorentzian t.
2. Add tube↔t entries with ±σ for e/p (no ring entries, no ℵ).
3. Sweep σ; identify where α_Coulomb = α.
4. Compare the required σ to natural candidates: √α, √(4πα), 1/(2π),
   and to the σ found in Track 3c's ℵ-mediated case.

Acceptance criteria:
- Signature preserved
- Structural universality α_e/α_p = 1.000 (expected since both
  tube windings = ±1)
- α_Coulomb = α at a value that is or is not naturally expressible

### Track 3e: Solve for the natural ℵ scale

If ℵ stays in the loop (Track 3d shows direct tube↔t doesn't
work cleanly), Track 3c's α_Coulomb scaling problem can be
inverted: instead of *tuning* σ_ta to hit α at fixed g(ℵ,ℵ) = 1,
*fix* σ_ta at a natural value (√α) and *solve* for the g(ℵ,ℵ)
and σ_at that produce α_Coulomb = α.

This treats g(ℵ,ℵ) as a derived quantity — the diagonal of the
ℵ dimension that we have been assuming is 1. If a natural σ_ta
combined with some specific g(ℵ,ℵ) gives observed α, that
specific g(ℵ,ℵ) is the implied scale of the ℵ dimension. It
might be natural (something like α, 1/(2π), L_P/L_Compton²) or
arbitrary.

Approach:
1. Fix σ_ta = √α (natural value).
2. 2D scan (σ_at, g_aa) to find (g_aa, σ_at) combinations
   producing α_Coulomb = α.
3. Identify the simplest combination.
4. Interpret: what does that g(ℵ,ℵ) value imply about L_ℵ?

Acceptance criteria:
- α_Coulomb = α to within 1 %
- Universality preserved (automatic on clean metric)
- The derived g(ℵ,ℵ) is reported regardless of whether it looks
  natural

### Track 4: Parameter synthesis and metric-terms.md

Synthesis track. Enumerate all metric coefficients R59 has
considered (across all 7 prior tracks).  Identify:

- Which entries are CONSTRAINED by model-E's particle spectrum
  (and thus not available for α coupling without disrupting
  the spectrum)
- Which entries are FREE (available without constraint)
- Which entries R59 has placed values at, and what those values
  were
- Where conflicts arise between α coupling and spectrum
  preservation

Output a single reference document (metric-terms.md) listing
each metric coefficient, its role, its current value (if any),
and its constraint status. Use compressed notation where
appropriate (e.g., S as a single block, Ma as one block per
sheet) to keep the document readable.

The output answers: "What knobs do we have, where, and what's
already used?"

### Track 3g: Natural-form parameter scan

Track 3f F54 found α_Coulomb = 0.977α at the simple combination
(k = 0.10, σ_at = 0.5, g_aa = 1, σ_ta = √α).  Section 4 of the
same script tested several natural-form candidates, with results
in the 0.5–0.8α range but none exact.  Pre-model-E α derivations
(R19) used parameters expressed in terms of α, π, and small
integers — suggesting a natural-form expression for the R59
architecture's tuning may exist.

This track does a focused search over natural-form combinations
of the architecture's three knobs (k, σ_at, g_aa) at fixed
σ_ta = √α, looking for combinations that hit α_Coulomb = α
exactly.

Approach:
1. Define a candidate list of "natural" values: 1, 1/2, 1/π,
   1/(2π), 1/(4π), √α, α, α × π, α × 4π, 4πα, π, 4π, √(4πα),
   etc.
2. Test all combinations (k, σ_at, g_aa) from this list
   against α_Coulomb = α.
3. Report combinations matching to within 1%.
4. Test fine-tuning around any near-matches to see if they
   sharpen.

Acceptance criteria:
- A combination matches α_Coulomb = α to within 0.1%
- Each knob has a "natural" closed-form expression
- Universality and ν neutrality preserved

Outcome possibilities:
- Clean natural-form match found: R60 starts with this as the
  exact target.  α is *derived* from geometry, not tuned.
- No exact natural-form match: R60 starts with F54's approximate
  target (k ≈ 0.1) and treats the residual ~3% as a refinement
  problem.

### Track 3f: Diagonal scaling — does Ma diagonal choice matter?

R59 Tracks 3b–3e found that the tube↔ℵ↔t architecture gives
exact universality but does NOT naturally produce α — getting
α requires fine-tuning σ_ta or g_aa near the PD boundary. All
those tests held the Ma diagonals fixed at the dimensionless
identity value (1) inherited from the model-E normalization.

The Ma diagonal values themselves come from a normalization
choice (divide by L_i × L_j), not from physics.  The
"physical" diagonals are L_i² in fm² — set by the L vector
chosen to match particle masses.  Skepticism is warranted:
those values may not be the "right" ones for α coupling.

This track asks: **with the tube↔ℵ↔t architecture at natural σ
values, can we produce α_Coulomb = α by scaling the Ma diagonals
alone?**

Approach:
1. Use the clean (no-internal-shear) Ma metric.
2. Couple e-tube and p-tube to ℵ at σ_ta = ±√α (natural).
3. Leave ν-tube uncoupled (neutrinos are charge-neutral, so
   no tube↔ℵ entry for the ν-sheet).
4. Treat each sheet's diagonal block as a free scaling factor:
   k_e, k_p, k_ν.
5. Treat g_aa and σ_at as free knobs.
6. Search the parameter space for combinations that produce:
   - α_Coulomb(electron) = α (within 1%)
   - α_Coulomb(proton) = α (universality, automatic)
   - α_Coulomb(neutrino mode) ≈ 0 (charge neutrality preserved)
   - Metric signature OK

Acceptance criteria:
- α_e = α to 1%, α_p = α to 1%, α_ν < 0.01α
- Diagonal scaling values that are "reasonable" (not extreme;
  not requiring near-singular limits)
- Configuration documented for R60 follow-up

Three possible interpretations of the result:
- If a natural diagonal scaling produces α: F44–F46's "tuning
  is unnatural" conclusion is reversed — the unnatural tuning
  was a consequence of fixed bad diagonals, not the architecture
  itself.  R60 has a clean target: find (ε, s) values that
  produce these diagonals AND match the spectrum.
- If only an arbitrary scaling works: confirms F44–F46.  R60
  needs a different α mechanism.
- If no scaling works: tube↔ℵ↔t cannot produce α regardless of
  diagonal freedom.  Architectural dead end.

---

## Visualization

The metric has 10+ dimensions. Visualization requires
dimensional compression: reduce S from 3D to 2D, showing
the compact or time dimension as height, color, or animation.
Based on the approach in viz/geodesic-curvature.

Relevant for illustrating geodesic convergence/divergence
if R59 reaches that point. Not needed for the core
mathematical/computational work.

**Rule:** derive analytically or compute numerically first;
visualize to confirm and communicate.

---

## Mathematical approach

New concepts needed (derived from scratch where used):

- **Lorentzian signature:** how time differs from space in the
  metric (−dt² vs +dx²) and what this means for geodesics
- **KK reduction:** how a higher-dimensional metric with compact
  dimensions produces gravity + gauge field in St. Standard
  KK assumes compact momentum; we must check what changes for
  standing waves
- **Linearized gravity:** metric perturbations from a source
  → geodesic deviation → force

---

## Files

| File | Purpose |
|------|---------|
| [background.md](background.md) | Detailed motivation and context |
| README.md | This framing document |
| [findings.md](findings.md) | Results, summary, and interpretations |
| [metric-terms.md](metric-terms.md) | Reference: every metric coefficient, value, and constraint |
| [review.md](review.md) | Review notes on framing and execution |
| [scripts/](scripts/) | Computation scripts (per track) |
