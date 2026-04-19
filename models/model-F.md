# Model: model-F (11D α-derivable architecture) ⟵ ACTIVE

**Status:** Active — R60 complete, ready for observational cross-checks
**Code:** [`studies/R60-metric-11/scripts/track1_solver.py`](../studies/R60-metric-11/scripts/track1_solver.py) (primitives) plus R60 tracks
**Study range:** R59 (architecture discovery), R60 (spectrum validation)
**Supersedes:** [model-E](model-E.md)

---

## TL;DR

Model-F is model-E's T⁶ spectrum architecture sitting on an 11D
metric (T⁶ × S³ × t × ℵ) with a geometric mechanism for
α coupling that makes α **structurally universal** across every
charged particle, every mode, every compound, and every
Z-charged nucleus (α_Coulomb = Z² α exactly).  The coupling
architecture is a Kaluza–Klein–style chain: `tube ↔ ℵ ↔ t`
with σ_ta = √α, σ_at = 4πα, g_aa = 1, plus a structurally-
derived `ring ↔ ℵ` entry σ_ra = (sε)·σ_ta (R60 Track 7) that
cancels shear-induced mode dependence.

**What is derived from geometry:**
- The connection between Ma-sheet windings and spacetime
  coupling (the tube↔ℵ↔t chain)
- The relationship σ_ra = (sε)·σ_ta from shear algebra (Track 7)
- α universality across sheets, modes, and compound modes
  (structural, not tuned)
- α_Coulomb = Z² × α for Z-charged nuclei (structural,
  floating-point exact)
- The single-k symmetry k_e = k_p = k_ν = 1.1803/(8π) emergent
  across every tested configuration

**What remains an input:**
- The *value* of α = 1/137.036 itself — it enters through
  σ_ta = √α and σ_at = 4πα.  Model-F explains how α *couples*
  to spacetime but does not explain why the coupling strength
  has that particular value.

| Measured inputs | Derived |
|----------------:|---------|
| m_e, m_p, Δm²₂₁ | all particle masses, full inventory |
| α = 1/137 | α-coupling mechanism, universality, Z² scaling |
| **4 inputs total** | same as model-E (no reduction) |

**Headline numbers:** R60 reproduces 16 of 18 model-E compound
particles within 1.6%, beats model-E on several (Ξ⁰ 19×, η 8×),
reproduces nuclear scaling at 0.05–1.5%, gives α_Coulomb = Z² α
exactly for every Z-charged nucleus, and does all this with α
structurally universal — something model-E did not have.

---

## Quick facts

### Dimensions and indices

Ordering: `ℵ, p_t, p_r, e_t, e_r, ν_t, ν_r, S_x, S_y, S_z, t`
(11D, R59 convention).

### Baseline configuration (Track 12 / 13a)

| Parameter | Value | Source |
|-----------|-------|--------|
| ε_e | 397.074 | R53 Solution D (inherited from model-E) |
| s_e | 2.004200 | R53 Solution D |
| ε_p | 0.55 | Model-E |
| s_p | 0.162037 | Model-E (R19-derived, preserved) |
| ε_ν | 2.0 (R61 #1) or 5.0 (R49 Family A) | Both viable |
| s_ν | 0.022 | R49 oscillation data |
| k_e = k_p = k_ν | 4.696 × 10⁻² = 1.1803/(8π) | **Emergent single-k symmetry** |
| g_aa | 1 | R59 F59 natural |
| σ_ta | √α (signs: e = +1, p = −1, ν = +1) | R59 F59 natural |
| σ_at | 4πα | R59 F59 natural |
| σ_ra | **(sε) · σ_ta per sheet** | **Track 7 structural prescription** |
| L_ring_e | 54.83 fm | derived from m_e |
| L_ring_p | 20.55 fm | derived from m_p |
| L_ring_ν | 1.96 × 10¹¹ fm | derived from m_ν₁ |

### Parameter count

| Category | Count | Examples |
|----------|------:|---------|
| **Measured dimensional scales** | **3** | m_e, m_p, Δm²₂₁ |
| **Measured dimensionless** | **1** | α (enters via σ_ta = √α; value not derived) |
| **Geometric inputs from prior studies** | 6 | ε, s per sheet (R53, R49, R61) |
| **Structural (derived)** | 4 | σ_ra_e, σ_ra_p, σ_ra_ν, k (single-value) |
| **Fixed at natural form** | 2 | σ_at = 4πα, g_aa = 1 |

**What structural gives us despite α still being input:**
Model-F makes α *universal* across every charged mode and
*exactly* Z² α for Z-charged nuclei — these are structural
predictions of the architecture once α is specified.  Model-E
specified α via R19's formula and got per-mode coupling
that varied with geometry; model-F gets structural universality
for free.

---

## Assumptions

1. **GRID** — discrete causal lattice with internal phase.  Gives
   Maxwell's equations, gravity, charge quantization.  Charge is
   topological (GRID axiom A3: one tube winding = one unit).

2. **One flat six-torus (T⁶)** in six compact material dimensions.
   Each "sheet" is a 2-torus.  Particles are standing
   electromagnetic waves on T⁶.  Inherited from model-E.

3. **ℵ dimension** — a sub-Planck internal edge dimension below
   the Ma scale (GRID).  Participates as a mediator in the α
   coupling chain but does not itself carry particle winding.
   Introduced in R55, formalized in R59.

4. **The 11×11 metric** has specific structural roles:
   - In-sheet shears (tube↔ring) → generation structure, shear
     resonance, compound-mode placement
   - Tube↔ℵ couplings → σ_ta mediates α delivery from each sheet
     to time
   - Ring↔ℵ couplings → σ_ra = (sε)·σ_ta cancels shear-induced
     mode dependence (derived, not free)
   - ℵ↔t coupling → σ_at delivers α to spacetime (single global
     parameter)
   - Cross-sheet entries → reserved for compound-mode
     fine-tuning (not used in model-F baseline)

5. **Charge is topological**, formula `Q = −n_et + n_pt`.  Mode
   winding determines integer charge.

6. **α coupling is quantized per mode**: `α_Coulomb = (α_sum)² × α`
   where `α_sum = n_et − n_pt + n_νt`.  For unit-charge particles
   (|Q| = 1), α = α iff |α_sum| = 1.  For Z-charged nuclei,
   α = Z² × α exactly — reproducing the expected nuclear Coulomb
   self-energy scaling.

---

## Headline results

### Architecture-level

- **α-coupling mechanism is geometric** — the tube↔ℵ↔t
  Kaluza–Klein–style chain delivers α-strength coupling from
  Ma-sheet windings to spacetime.  The *structure* of the
  coupling is derived; the *value* of α itself is still input
  (via σ_ta = √α).
- **α universality structural** across sheets, across modes
  within a sheet (via σ_ra cancellation), and across compound
  modes (via α-sum rule).  Every mode with `|α_sum| = 1` gets
  the same α — a structural prediction, not a tuning.
- **Single-k symmetry** emergent: k_e = k_p = k_ν = 1.1803/(8π)
  to floating-point precision across every tested geometry (6+
  configurations).  Suggests a hidden symmetry worth analytical
  follow-up.
- **α_Coulomb = Z² × α** for any Z-charged nucleus — physically
  correct Coulomb self-energy scaling, emerges from the metric
  structure given the same α input, not imposed separately.
- **Pion mass desert** inherited from model-E — MaSt structural
  limitation, not an R60 regression.

### Inventory

- **Stable particles exact:** electron, proton, neutrino mass
  eigenstates all calibrated to observed values.
- **Muon recovered at model-E tuple** (1, 1, −2, −2, 0, 0) with
  model-E's own 0.83% accuracy.
- **Tau, neutron, hyperons** — R60 finds α-universal
  6-tuples within 0.01–1.6% of observed.
- **14 of 16 non-pion particles** tabulated with α universal.
- **π⁰ and π±** stuck at ~105 MeV (~23% off observed), same
  failure as model-E.

### Nuclear scaling

- d (0.05%), ⁴He (0.73%), ¹²C (1.08%), ⁵⁶Fe (1.52%) with
  decorations.  `n₅ = A, n₆ = 3A` scaling law inherited from
  R29 / model-E.
- **α_Coulomb for nuclei is exactly Z² × α** (tested Z = 1, 2, 6,
  26 — matches to floating-point precision).

### Three generations

Inherited intact from model-E / R53 Solution D:
- electron (1, 2) at shear cancellation point
- muon (1, 1) on e-sheet (compound with small ν decoration)
- tau at compound mode (2, −6, −2, *, 1, 5)

Mass ratios algebraically determined by (ε_e, s_e) with zero
free parameters.  R53 generation resonance mechanism preserved.

---

## Particle inventory

Ordering in 6-tuples: `(n_et, n_er, n_νt, n_νr, n_pt, n_pr)`.
α/α values given for the R60-native tuples (with α-sum shown).

| Particle | Obs (MeV) | R60 tuple | α_sum | α/α | Δm/m |
|----------|----------:|:----------|:-----:|:---:|:----:|
| ν₁ | 3.21 × 10⁻⁸ | (0, 0, 1, 1, 0, 0) | +1 | 1 | input/derived |
| ν₂ | 3.33 × 10⁻⁸ | (0, 0, −1, 1, 0, 0) | −1 | 1 | derived (0.03%) |
| ν₃ | 5.96 × 10⁻⁸ | (0, 0, 1, 2, 0, 0) | +1 | 1 | derived (2.5%) |
| electron | 0.511 | (1, 2, 0, 0, 0, 0) | +1 | 1 | input |
| proton | 938.272 | (0, 0, 0, 0, 1, 3) | +1 | 1 | input |
| neutron | 939.565 | (−1, −2, −1, *, −1, −3) | −1 | 1 | 0.14% |
| muon | 105.658 | (1, 1, −2, *, 0, 0) | −1 | 1 | 0.83% |
| tau | 1776.86 | (2, −6, −2, *, 1, 5) | −1 | 1 | 0.06% |
| Λ | 1115.68 | (−2, −4, −1, *, −2, −2) | −1 | 1 | 0.09% |
| Σ⁺ | 1189.37 | (−1, 2, 0, *, 0, −4) | +1 | 1 | 0.00% |
| Σ⁻ | 1197.45 | (3, 1, −2, *, 2, −1) | −1 | 1 | 0.01% |
| Ξ⁰ | 1314.86 | (−1, 6, −1, *, −1, 3) | −1 | 1 | 0.01% |
| Ξ⁻ | 1321.71 | (−1, −6, −2, *, −2, −3) | −1 | 1 | 0.19% |
| η′ | 957.78 | (−1, −4, 0, *, −1, −3) | 0 | 0 | 0.35% |
| η | 547.86 | (−1, −4, 0, *, −1, 0) | 0 | 0 | 0.24% |
| φ | 1019.46 | (−1, −3, 0, *, −1, 3) | 0 | 0 | 0.12% |
| ρ | 775.26 | (−1, −5, 0, *, −1, −2) | 0 | 0 | 1.21% |
| K⁰ | 497.61 | (0, −4, 0, *, 0, −1) | 0 | 0 | 0.82% |
| K± | 493.68 | (1, 6, −2, *, 0, −1) | −1 | 1 | 1.55% |
| π⁰ | 134.98 | (0, −1, 0, *, 0, 0) | 0 | 0 | **22.7% (stuck)** |
| π± | 139.57 | (1, 1, −2, *, 0, 0) | −1 | 1 | **24.9% (stuck)** |

(Asterisk: n_νr is degenerate at current L_ν.  Any small value works.)

**Split of Q = 0 compounds into α = 0 (structurally neutral) and
α = α (weak-coupling analog):**

- α = 0 (structurally neutral): η, η′, φ, ρ, K⁰, π⁰
- α = α: Λ, Σ⁻, neutron, Ξ⁰, Ξ⁻

This is a new model-F prediction; comparison to observed weak
interaction cross-sections for these particles is a follow-up.

### Nuclear scaling

Scaling law `n₅ = A, n₆ = 3A, n_et = A − Z` with small
decoration on (n_er, n_νr):

| Nucleus | A | Z | R60 Δm/m | α/α = Z² |
|---------|--:|--:|:--------:|:--------:|
| d | 2 | 1 | 0.05% | 1 |
| ⁴He | 4 | 2 | 0.73% | 4 |
| ¹²C | 12 | 6 | 1.08% | 36 |
| ⁵⁶Fe | 56 | 26 | 1.52% | 676 |

The α_Coulomb = Z² α pattern is *exact* (tested to Z = 26,
match to floating-point precision).

---

## Architecture details

### The σ_ra structural fix

The key R60 discovery (Track 7): with in-sheet shear `s` on a
sheet, the ring inherits an indirect coupling to the t direction
via the (ring → tube → ℵ → t) chain, breaking α universality
across modes on the sheet.  The fix: add a direct ring↔ℵ entry
at value `σ_ra = (s · ε) · σ_ta`.  This cancels the indirect leak
exactly, restoring α universality.

Derivation: in the 4×4 (tube, ring, ℵ, t) sub-metric with σ_ra
active, `det(A) = k · (σ_ta² − k·(g_aa + σ_at²))` — completely
independent of `u = sε`.  Signature stays intact at arbitrarily
large sε (verified up to sε = 2000, Track 8b).

σ_ra is **derived from existing geometry**, not free.  It's not
a new knob.

### The single-k symmetry

In 6 different geometric configurations (all shearless, magic
shear on e+p, extreme e + magic p, extreme e + model-E p, etc.),
the joint solver with three independent per-sheet k knobs lands
at k_e = k_p = k_ν = 1.1803/(8π) to floating-point precision.

**R60 Track 14 confirmed k is a structural fixed point** — the
solver converges to the same k from any initial value at or above
K_NATURAL = 1/(8π).  Track 14 also derived the single-sheet
α_Coulomb equation in closed form using sympy, but the full
multi-sheet derivation that would explain *why* k = 1.1803/(8π)
specifically is not closed (best near-natural form found:
(1+4πα)² = 1.19181, off by 0.97%).

So: **k is structurally determined (empirically confirmed); the
closed-form expression for its specific value remains open.**
One global k suffices for model-F in practice.

### α quantization for compound modes

Compound modes span multiple sheets.  For a mode
`(n_et, n_er, n_νt, n_νr, n_pt, n_pr)`:

    α_Coulomb = (n_et − n_pt + n_νt)² × α

Exact, verified across every test case.  Two direct consequences:

1. **α universality** requires `|n_et − n_pt + n_νt| = 1` — the
   R60 selection rule for unit-α coupling.
2. **Nuclear Z² scaling** emerges naturally: for a Z-nucleus with
   `n_et = A − Z`, `n_pt = A`, `n_νt = 0`, we get α_sum = −Z,
   hence α_Coulomb = Z² α.

### ν-sheet optionality

R60 Track 13b found that the ν candidate choice has **negligible
effect** on hadron inventory and nuclear scaling (ν contributes
~10⁻¹⁰ of compound masses at our L_ν).  Multiple R61 candidates
are viable.

The two cleanest:

| Candidate | (ε_ν, s_ν) | ν triplet | Δm²₃₁/Δm²₂₁ |
|-----------|:----------:|:---------:|:-----------:|
| **R61 #1 (recommended)** | (2.0, 0.022) | (+1,+1)(−1,+1)(+1,+2) | 33.591 |
| R49 Family A (model-E's choice) | (5.0, 0.022) | (+1,+1)(−1,+1)(+1,+2) | 33.591 |

Both give full ν α universality (α_ν₁ = α_ν₂ = α_ν₃ = α) and
match the R49 oscillation target (33.6) to 0.03%.  R61 #1 has
slightly more compact geometry.  R49 Family A matches model-E
exactly.  Either is fine.

---

## Open questions

### Unresolved

- **Pion mass desert.**  π⁰ and π± land at ~105 MeV (same slot
  as muon) instead of observed 135–140 MeV.  Identical failure
  to model-E.  Likely needs chiral dynamics or paired-mode
  physics beyond R60.  Candidate for follow-up study R62.
- **Single-k symmetry analytical derivation.**  R60 Track 14
  confirmed the value is a structural fixed point (empirical)
  and derived the single-sheet α_Coulomb equation analytically.
  The full multi-sheet derivation that would give k in closed
  form is not yet completed.  Best near-natural-form candidate:
  (1+4πα)² = 1.19181 (0.97% off the observed 1.18034).
- **ν-sheet (1, 0) ghost.**  At R61 #1 geometry, the (1, 0) ν
  mode is lighter than (1, 1).  Per R61's own taxonomy, filtered
  by pair-cancellation or dark-mode mechanisms.  External to R60
  architecture.

### Working assumptions

- ν-sheet architecturally coupled at σ_ta = √α with sign
  convention.  Neutral charge comes from topology (Q = −n_et +
  n_pt = 0 for pure ν modes), not from zeroing σ_ta.  R60 Track 6
  validates this.
- Single-k symmetry is structural; one k value works for all
  sheets.

---

## Parameter count (detailed)

**Measured (from experiment):**
- m_e, m_p, Δm²₂₁ — 3 dimensional scales
- α = 1/137.036 — 1 dimensionless coupling (value is input;
  enters as σ_ta = √α.  Model-F does not derive this number.)

**Structural (fixed by R60 architecture, not tunable):**
- σ_ra = (sε)·σ_ta per sheet — Track 7 derivation
- k = 1.1803/(8π) — single-k symmetry across all sheets
- Sign convention for σ_ta per sheet: +1 for e, −1 for p, +1 for ν
- α_Coulomb for a mode (n_et, n_er, n_νt, n_νr, n_pt, n_pr):
  equals (n_et − n_pt + n_νt)² × α exactly — the α-sum rule
- Nuclear α_Coulomb = Z² × α (consequence of the α-sum rule
  when α_sum = −Z)

**Fixed at R59 F59 "natural form" once α is chosen:**
- σ_ta = √α (the α-delivery coupling magnitude)
- σ_at = 4πα (ℵ → t coupling)
- g_aa = 1 (ℵ diagonal)

**Inherited from prior studies (physics-determined):**
- ε_e, s_e from R53 Solution D (lepton generation ratios exact)
- ε_p, s_p from model-E / R19 formula
- ε_ν, s_ν from R49 oscillation data

**What R60 actually derives.**  Not the value of α — it's input.
What *is* derived:
- The geometric mechanism by which Ma windings couple to
  spacetime (the tube↔ℵ↔t chain)
- The structural relationship σ_ra = (sε)·σ_ta that cancels
  shear-induced mode-dependence
- The α-sum rule for compound modes and its specialization to
  Z² α for nuclei
- The single-k symmetry
- α universality across all charged particles from the tube-
  winding structure

Track 5 F22 closed-form: `Q_Coulomb = 0 ⟺ n_r/n_t = sε + 1/(sε)`,
identifying which (ε, s) values structurally neutralize α for a
given mode.  This is a derived geometric fact.

---

## Comparison to model-E

| Property | Model-E | Model-F |
|----------|:-------:|:-------:|
| Metric dimensionality | 9D (T⁶ + S + t, no ℵ in metric) | **11D (T⁶ + ℵ + S + t)** |
| α *value* | Input (via R19 shear formula) | Input (via σ_ta = √α, σ_at = 4πα) — same |
| α *coupling mechanism* | R19 formula relates α to shear; per-sheet | **Geometric chain tube↔ℵ↔t; structural** |
| α universality | Not structural (per-mode coupling varies) | **Structural — same α for every charged particle** |
| Muon | (1, 1, −2, −2, 0, 0), 0.83% | Same tuple, 0.83%, α = α |
| Tau | (3, −6, 2, −2, 2, 3), 0.05% | (2, −6, −2, *, 1, 5), 0.06%, α = α |
| Neutron | (0, −4, −1, 2, 0, −3), 0.07% | (−1, −2, −1, *, −1, −3), 0.14%, α = α |
| Λ | 0.00% | 0.09% |
| Ξ⁰ | 0.19% | **0.01%** (19× better) |
| η | 1.84% | **0.24%** (8× better) |
| Nuclear scaling | ≤ 1.1% | ≤ 1.5% (1–2× worse in absolute terms) |
| **α_Coulomb for nuclei** | N/A (α not extracted per-particle) | **= Z² × α, exact structural** |
| Measured inputs | 4 (m_e, m_p, Δm²₂₁, α) | 4 (same — value of α still input) |
| Pion failure | 22.7% / 24.9% | 22.7% / 24.9% (same) |

**Net:** model-F has the same spectrum accuracy as model-E and
the same 4 measured inputs (including α itself), but trades
model-E's per-mode α-coupling (which varied with geometry) for a
structural α universality that holds across every charged mode,
every compound, and every Z-nucleus (as Z²α).  The coupling
*mechanism* is now geometric; the coupling *value* remains
observational input.

---

## Studies

| Study | Focus | Status |
|-------|-------|--------|
| R59 | Architecture discovery (σ_ta = √α, σ_at = 4πα, g_aa = 1, tube↔ℵ↔t chain) | Complete |
| R60 | Metric-11 — spectrum validation + σ_ra structural fix + single-k symmetry + inventory audit | Complete (Tracks 1–14) |
| R61 | Neutrino sheet candidates | Complete (taxonomy used here) |
| R62 (future) | Pion mass resolution study | Proposed, not started |

---

## References

- [R60 findings index](../studies/R60-metric-11/findings.md)
- [R60 README](../studies/R60-metric-11/README.md) — track framings
- [R60 metric-terms](../studies/R60-metric-11/metric-terms.md) — parameter reference
- [R59 findings](../studies/R59-clifford-torus/findings.md) — architecture discovery
- [R61 candidates](../studies/R61-neutrino-tuning/findings.md) — ν-sheet options
- Predecessor: [model-E](model-E.md)
