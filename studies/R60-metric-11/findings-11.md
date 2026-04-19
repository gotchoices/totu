# R60 Track 11: Nuclear scaling audit

**Scope.**  Test R29 / model-E's nuclear scaling law
(n_5 = A, n_6 = 3A, n_et = A − Z) on the Track 9 baseline against
observed masses of d, ⁴He, ¹²C, and ⁵⁶Fe.  Verify both mass
predictions and α_Coulomb behavior for multi-charge nuclei.

Script: [scripts/track11_nuclear_scaling.py](scripts/track11_nuclear_scaling.py).

## F63. Nuclear scaling works on R60, with α ∝ Z² as expected

Primary tuple `(A − Z, 0, 0, 0, A, 3A)` evaluated on the Track 9
metric:

| Nucleus | A | Z | Target (MeV) | R60 predicted | Δ | α/α | Z² check |
|---------|--:|--:|-------------:|--------------:|--:|----:|:--------:|
| d (²H) | 2 | 1 | 1875.613 | 1888.136 | +0.67% | 1.0000 | 1 ✓ |
| ⁴He | 4 | 2 | 3727.379 | 3776.272 | +1.31% | 4.0000 | 4 ✓ |
| ¹²C | 12 | 6 | 11177.929 | 11328.816 | +1.35% | 35.999998 | 36 ✓ |
| ⁵⁶Fe | 56 | 26 | 52089.770 | 52915.766 | +1.59% | 675.999967 | 676 ✓ |

**α_Coulomb / (Z² α) = 1.000000 to 6 decimal places for every
tested nucleus.**  The compound-α quantization rule
`α/α = (n_et − n_pt + n_νt)²` gives exactly `Z²` for the nuclear
scaling tuple (since α_sum = (A−Z) − A + 0 = −Z).  This is
structurally the Coulomb self-energy scaling that physics
requires: a Z-charged nucleus has self-energy ∝ Z²α, and R60's
geometry delivers that for free.

## F64. Decoration improves deuterium to model-E accuracy

Scanning n_er and n_νr within ±3 (neither affects Q, spin, or
α_sum), the best decorations found:

| Nucleus | Primary Δ | Decorated tuple | Decorated Δ |
|---------|:---------:|:----------------|:-----------:|
| d | +0.67% | (1, 2, 0, −3, 2, 6) | **+0.05%** (matches model-E exactly) |
| ⁴He | +1.31% | (2, 3, 0, −3, 4, 12) | +0.73% |
| ¹²C | +1.35% | (6, 3, 0, −3, 12, 36) | +1.08% |
| ⁵⁶Fe | +1.59% | (30, 3, 0, −3, 56, 168) | +1.52% |

Decoration improvement scales roughly with how much ring-sheet
correction helps the specific A, Z combination.  Deuterium gets
the cleanest boost, matching model-E's 0.05% exactly.

## F65. R60 nuclear accuracy is comparable to model-E, 1–2× worse

Summary vs model-E:

| Nucleus | R60 (decorated) | Model-E | Ratio |
|---------|:---------------:|:-------:|:-----:|
| d | 0.05% | 0.05% | 1× |
| ⁴He | 0.73% | 0.69% | 1.06× |
| ¹²C | 1.08% | 0.76% | 1.42× |
| ⁵⁶Fe | 1.52% | 1.05% | 1.45× |

All R60 errors are within model-E's "≤ 1.1%" claim to within a
factor of 1.5.  The slight worsening likely comes from R60's
p-sheet being at magic shear (ε = 0.4, s = 3) rather than
model-E's original (ε = 0.55, s = 0.162).  Track 12 could test
whether reverting to model-E's p-geometry tightens the nuclear
fit.

## F66. The α = Z² result is structurally important

The compound-α rule `α/α = (α_sum)²` with α_sum = −Z for nuclei
isn't coincidence — it's the correct generalization of α
universality from |Q|=1 particles to |Q|=Z nuclei.  In
standard physics:

- Single unit charge: Coulomb self-energy ∝ α
- Z-charged nucleus: self-energy ∝ Z²α

This is exactly what our α formula delivers.  The same mechanism
that gives α universality across individual charged particles
gives the correct Z² scaling across nuclei.  **Without this
being an input, R60's α architecture naturally reproduces
nuclear Coulomb physics.**

This also means: pool item **h** (cross-sheet σ prescription)
that might someday be needed for compound-mode fine-tuning is
NOT needed for nuclear scaling — the plain architecture already
does this part right.

## Status

**Nuclear scaling is validated on the R60 architecture.**  Four
nuclei from H to Fe, spanning a factor of ~27 in mass, all
reproduced within 1.6% with the α = Z²α pattern exact.  This
was one of model-E's strongest results; R60 inherits it with
α universality as a structural feature.

## Decision point

R60's core architecture is now extensively validated:
- α universal across sheets (Track 4)
- α universal across modes within a sheet (Track 7)
- Muon at model-E's tuple (Track 9)
- 16 of 18 hadrons within 2.5% (Track 10)
- Nuclear scaling at α = Z²α (Track 11)

**Ready to promote to model-F.**  Natural next steps:

- **(a) Write model-F document** (models/model-F.md) — synthesize the architecture, results, and positioning vs model-E.  Formalize the promotion.
- **(b) Revisit p-sheet alignment with model-E** — use (ε_p, s_p) = (0.55, 0.162) instead of (0.4, 3.0) to see if tau, neutron, Λ, Σ, Ξ match model-E's tuples more closely.  Potentially a big improvement to Tracks 10 and 11 accuracies.
- **(c) Analytical derivation of k = 1.1803/(8π)** — the persistent single-k value across all tested geometries remains unexplained.  Pool item.
- **(d) Pion follow-up study (R62)** — focused effort on MaSt pion mass desert. Out of R60 scope.

Recommendation: (a) and (b) together.  Write up model-F in
parallel with p-sheet alignment test — they inform each other.
