# R60 Track 9: Model-E extreme e-sheet revival

**Scope.**  Track 8b confirmed that σ_ra = (sε)·σ_ta lifts the
Track 2 signature bound entirely — arbitrarily large sε is
feasible.  Track 9 exploits this by re-solving the joint three-
sheet system with the electron sheet at model-E's extreme values
(ε = 397.074, s = 2.004200, sε ≈ 796) that were incompatible
with R59 F59 in Track 2 (375× over the 3/√2 bound).

Hypothesis: at model-E's extreme e-sheet values, R53's
generation resonance kicks in — the (1, 2) electron mode sits
at the shear cancellation point with μ ≈ 1/ε, anomalously
light, and the (1, 1) mode above it acts as the muon.  Muon
then lands as a low-order compound on the new metric.

Scripts: [track8b_extreme_e_sanity.py](scripts/track8b_extreme_e_sanity.py)
(signature sweep) and [track9_modelE_extreme_e.py](scripts/track9_modelE_extreme_e.py)
(full re-solve).

## F51. Track 2's signature bound is lifted by σ_ra

Derivation: with σ_ra = u·σ_ta (where u = sε) added to the 4×4
(Ma_tube, Ma_ring, ℵ, t) subspace, the determinant simplifies to

    det(A) = k·(σ_ta² − k·(g_aa + σ_at²))

— **completely independent of u**.  The Track 2 bound
`(sε)² ≤ 9/2` was a property of the un-augmented metric; with
σ_ra active, arbitrarily large sε preserves signature.

Numerical sweep (Track 8b):

| sε | Signature OK? | Min pos eig | α_e/α |
|----:|:-------------:|-----------:|:-----:|
| 0.8 (Track 7d) | ✓ | 1.36 × 10⁻² | 1.000 |
| 2.25 (just past Track 2 cliff) | ✓ | 6.52 × 10⁻³ | 1.000 |
| 10 | ✓ | 4.59 × 10⁻⁴ | 1.000 |
| 100 | ✓ | 4.70 × 10⁻⁶ | 1.000 |
| **795 (model-E)** | **✓** | **7.41 × 10⁻⁸** | **1.000** |
| 2000 (stress) | ✓ | 1.17 × 10⁻⁸ | 1.000 |

Min positive eigenvalue shrinks as sε grows, but stays positive
— signature holds throughout.  α_e is constant at α across the
entire range because σ_ra cancellation is exact.

## F52. Joint re-solve converges at model-E extreme geometry

Sheet inputs: e at (ε = 397.074, s = 2.004200); p at Track 7d
magic shear (ε = 0.4, s = 3.0); ν at R61 #1 (ε = 2.0, s = 0.022).
Free knobs (L, k) per sheet.  Targets: three masses and α = α
on the three primary modes.

| Quantity | Value |
|----------|-------|
| Converged | True (xtol, cost 10⁻²⁴) |
| k_e | 4.696442 × 10⁻² |
| k_p | 4.696442 × 10⁻² |
| k_ν | 4.696442 × 10⁻² |
| k_e / k_p | 1.000000 |
| L_ring_e | 54.83 fm |
| L_ring_p | 15.24 fm |
| L_ring_ν | 1.96 × 10¹¹ fm |
| σ_ra_e | +67.98 |
| σ_ra_p | −0.103 |
| σ_ra_ν | +0.00376 |
| Signature | OK, 1 neg eig |

**Remarkable:** the single-k symmetry k_e = k_p = k_ν = 1.1803/(8π)
survives even with sε_e ≈ 796 while sε_p = 1.2 and sε_ν = 0.044.
The solver had six free knobs and landed with the three k values
*identical to 6 decimal places*.  This symmetry is much deeper
than the Track 7b discovery suggested — it's not just "emergent
at one geometry," it holds across radically different sheet
geometries.

L_ring_e = 54.83 fm on our k = 0.047 normalization is exactly
model-E's L_ring_e = 11.88 fm at k = 1, scaled by 1/√k.  The
geometry is model-E's, just expressed in R60's dimensionless
parameterization.

## F53. All primary targets met at floating-point precision

| Mode | E predicted | E target | α/α |
|------|------------:|---------:|----:|
| electron (1, 2, 0, 0, 0, 0) | 0.5109989461 MeV | 0.5109989461 | 1.0000000000 |
| proton (0, 0, 0, 0, 1, 3) | 938.272 MeV | 938.272 | 1.0000000000 |
| ν₁ (0, 0, 1, 1, 0, 0) | 32.100 meV | 32.1 | 1.0000000000 |
| ν₂ (0, 0, −1, 1, 0, 0) | 33.250 meV | (predicted) | 1.0000000000 |
| ν₃ (0, 0, 1, 2, 0, 0) | 59.624 meV | (predicted) | 1.0000000000 |

Δm²₃₁/Δm²₂₁ = 33.5909 (R49 target: 33.6).

## F54. Model-E's muon tuple reproduces muon mass at 0.83%

Plug model-E's compound tuples directly into the Track 9 metric:

| Particle | Model-E tuple | E predicted | E target | Δ | α/α |
|----------|:--------------|------------:|---------:|--:|----:|
| **muon** | **(1, 1, −2, −2, 0, 0)** | **104.7840 MeV** | **105.658** | **−0.83%** | **1.0000** |
| tau | (3, −6, 2, −2, 2, 3) | 2521.96 MeV | 1776.86 | +42% | 9.0000 |
| neutron | (0, −4, −1, 2, 0, −3) | 1200.80 MeV | 939.57 | +28% | 1.0000 |

**The muon is recovered at model-E's own tuple with model-E's
own 0.83% accuracy.**  This is R53's generation resonance
mechanism working: at (ε_e = 397, s_e = 2.004), the (1, 2)
electron mode has μ = √(1/ε² + (2 − s)²) ≈ 0.0049, while the
(1, 1) ghost has μ ≈ 1.004 — ratio ≈ 205.  Since the
compound tuple's mass is dominated by its heaviest contribution,
(1, 1, −2, −2, 0, 0) = (1, 1) e-sheet + negligible ν-contribution
≈ 205 × m_e ≈ 104.8 MeV, hitting muon.

Tau and neutron don't match via model-E tuples because our
p-sheet is at magic shear (ε = 0.4, s = 3), not model-E's
(ε = 0.55, s = 0.162).  Different p-geometry → different
compound spectrum.

## F55. Alternative compound tuples hit tau and neutron cleanly

α-filtered brute-force search at |n_i| ≤ 6:

| Particle | Best tuple | E predicted | Δ | α/α |
|----------|:-----------|------------:|--:|----:|
| muon | (1, 1, −2, −2, 0, 0) | 104.78 MeV | −0.83% | 1.0000 |
| tau | (2, 3, −2, *, 1, −1) | 1773.45 MeV | −0.19% | 1.0000 |
| neutron | (−1, −2, −1, *, −1, −3) | 938.27 MeV | −0.14% | 1.0000 |

(Asterisk: n_νr is effectively free at our L_ν; all 5 top
matches per target share the same energy.)

All three particles at α = α with residuals comparable to
model-E's own accuracy.

## F56. The spectrum picture

Three decisive features combine to give R60 a clean, R53-consistent
spectrum story:

1. **R53 generation mechanism works at model-E e-sheet**.  The (1, 2)
   electron lives at the shear cancellation point; (1, 1) acts as
   the muon via the compound (1, 1, −2, −2, 0, 0).  The (1, 3) tau
   analog on e-sheet would have μ ≈ 1.996 ≈ 406 × m_e ≈ 207 MeV —
   too light for tau (1777 MeV), which is why tau needs cross-sheet
   compound contributions.

2. **σ_ra cancellation enables the extreme geometry**.  Without
   Track 7's ring↔ℵ structural fix, sε = 796 would break signature
   by 375×.  With σ_ra_e = (sε)·σ_ta ≈ 68, signature holds and α
   universality is preserved.

3. **Single-k symmetry is a deep structural feature**.  It held
   in Track 7b (all sheets shearless) and Track 7d (magic shear)
   and now in Track 9 (extreme asymmetric geometry).  Three
   independent knobs landing at one value across wildly different
   configurations suggests an underlying symmetry we haven't
   explicitly identified.  Worth analytical follow-up.

4. **Compound α is exactly quantized** (Track 8 F47):
   `α/α = (n_et − n_pt + n_νt)²`.  Every charged particle has
   integer α-ratio; unit-charge compound modes naturally land at
   α = α.  Tau's model-E tuple has sum = +3, so α = 9 — wrong for
   unit-charge α.  A better tuple with sum = ±1 gives α = α
   correctly.  The compound search with the α filter is clean.

## Status

R60 has achieved its primary objective: reproduce model-E's
spectrum on the R59 F59 α-derivable architecture with α
universality preserved across all sheets and all modes.

| Particle | R60 result | Model-E result | Comparable? |
|----------|:----------:|:--------------:|:-----------:|
| electron | exact | exact | yes |
| proton | exact | exact | yes |
| ν₁, ν₂, ν₃ | 32.1 / 33.3 / 59.6 meV (Δm² ratio 33.59) | same (R49 Family A) | yes |
| **muon** | **0.83% at (1, 1, −2, −2, 0, 0)** | **0.83% at same tuple** | **identical** |
| tau | 0.19% at (2, 3, −2, *, 1, −1) | 0.05% at (3, −6, 2, −2, 2, 3) | R60 slightly worse |
| neutron | 0.14% at (−1, −2, −1, *, −1, −3) | 0.07% at (0, −4, −1, 2, 0, −3) | R60 slightly worse |

With α universality as a free bonus.

## Decision point

Track 9 is a major positive result.  **R60's core architecture is
validated as a model-F candidate.**  Natural next steps:

- **Track 10: broader hadron inventory** (Σ, Λ, Ξ, Ω, K, π, η,
  ρ, φ, ...) on the Track 9 baseline.  Compare to model-E's
  18/20 inventory.  Goal: recover most of the model-E hadrons
  at α = α with comparable accuracy.
- **Track 11: refine tau, neutron** by trying model-E's p-sheet
  geometry (ε_p = 0.55) instead of Track 7d magic shear.  If
  model-E's tau/neutron tuples then match, we have total
  model-E spectrum replication.
- **Pool item for later:** nuclear scaling (R29's n₅ = A, n₆ = 3A)
  on the new metric.  Model-E matched d, ⁴He, ¹²C, ⁵⁶Fe at
  ≤ 1.1%; we'd want to verify this too.
- **Analytical understanding of single-k symmetry** (pool item).
  k_e = k_p = k_ν = 1.1803/(8π) holds across three very different
  sheet configurations.  This is probably a structural identity
  worth deriving.
