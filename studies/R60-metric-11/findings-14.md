# R60 Track 14: Analytical derivation of k — partial result

**Scope.**  Pool item f: derive the single-k value that the joint
solver finds across all tested geometries.  Three phases:
(1) empirical — is k a fixed point?  (2) symbolic — derive it
with sympy.  (3) natural-form search — closed form?

Script: [scripts/track14_k_derivation.py](scripts/track14_k_derivation.py).

## F78. Phase 1 confirms k = 1.1803/(8π) is a true fixed point

Sweep of initial k values for the joint solver:

| k_init / K_NAT | k_final / K_NAT | converged? |
|---:|---:|:---:|
| 0.1 | 0.1 (unchanged) | no |
| 0.5 | 0.5 (unchanged) | no |
| 1.0 | **1.1803** | YES |
| 2.0 | **1.1803** | YES |
| 5.0 | **1.1803** | YES |
| 10.0 | **1.1803** | YES |

For any initial value at or above K_NATURAL = 1/(8π), the solver
converges to k = 1.1803/(8π) identically.  Below K_NATURAL the
solver fails to converge (likely signature cliff blocks the
descent path).  **k is structurally determined**, not an
artifact of initial conditions.

## F79. Phase 2 — single-sheet derivation clean; multi-sheet not closed

Using sympy on the 4×4 sub-metric for one sheet (tube, ring, ℵ, t)
with σ_ra = u · σ_ta active, I derived:

- `det(A) = k · (α − k(1 + 16π²α²))`  (independent of u)
- `A⁻¹[t, t] = (α − k) / (k(1 + 16π²α²) − α)`
- `A⁻¹[tube, t] = −4π α^(3/2) / (k(1 + 16π²α²) − α)`
- `A⁻¹[ring, t] = 0`  (structural cancellation confirmed)
- **`α_Coulomb(electron, 1-sheet) = 4π α³ (α − k)² / (k(1 + 16π²α²) − α)⁴`**

Setting `α_Coulomb = α` yields an implicit equation in k.
sympy's `solve()` returned an empty solution set for the numeric
substitution, indicating that no closed-form solution exists for
the single-sheet equation in the parameter range around
k ≈ 0.047.

Numerical check: at k = 0.04696 (the empirical multi-sheet
value), the single-sheet α_Coulomb evaluates to 0.41 × α, not
α.  **The multi-sheet and single-sheet systems are not equivalent
at this k.**

The full multi-sheet derivation requires the 11×11 inverse metric
analytically with multiple σ_ra entries contributing through
ℵ.  sympy algebra at that scale didn't produce a clean closed
form in my attempts.  Deferred.

## F80. Phase 3 — no clean natural-form expression found

Search over natural-form candidates for `k × 8π = 1.1803`:

| Candidate | Value | Rel err |
|-----------|------:|--------:|
| 1 | 1.0000 | 15.3% |
| 1 + α | 1.0073 | 14.7% |
| 1 + 16π²α² | 1.0084 | 14.6% |
| 1 + 4πα | 1.0917 | 7.5% |
| **(1 + 4πα)²** | 1.1918 | **0.97%** (best simple form) |
| 1 + 4πα + 16π²α² | 1.1001 | 6.8% |
| (2π+1)/(2π) | 1.1592 | 1.8% |
| e^(2α) | 1.0147 | 14.0% |
| (1+α)²/(1−α) | 1.0221 | 13.4% |
| 1 + 2πα | 1.0459 | 11.4% |

**Best match** is `(1 + 4πα)² ≈ 1.19181`, off by 0.97%.
Suggestive but not clean.  **No closed-form candidate matches
to < 0.1%.**

A private check of `1 + (5π²/2)·α = 1.18009` is 0.02% off — but
with no physics motivation for that specific combination, this
is likely numerical coincidence on my single candidate.

## F81. Status and honest assessment

**What Track 14 resolved:**

- k = 1.1803/(8π) is structurally pinned by the joint solver, not
  an initial-condition artifact.  Empirically confirmed.
- The single-sheet α_Coulomb equation has a clean analytical form
  (F79).  Structural σ_ra cancellation makes A⁻¹[ring, t] = 0
  exactly — useful machinery.
- σ_ra = u·σ_ta does make det(A) u-independent (Track 8b F51
  confirmation via analytical form).

**What Track 14 did not resolve:**

- The multi-sheet derivation that actually produces k = 1.1803/(8π)
  requires more sympy algebra than this track delivered, or a
  cleverer reduction.
- No closed-form expression for 1.1803 was found in the tested
  natural-form candidates.
- The difference between R59 F59 clean (k = 1/(8π)) and R60 with
  ν-shear (k = 1.1803/(8π)) is clearly driven by the ν-sheet's
  contribution, but the exact mechanism isn't derived here.

**Net:** Pool item f is now *partially* resolved.  The fixed-point
nature of k is confirmed, the single-sheet analytics are derived,
but the full closed-form expression remains open.

## Decision point

Two reasonable follow-ups, neither of which is in R60's critical
path:

- **More sympy work** on the multi-sheet system.  Probably
  feasible but requires setting up the 11×11 carefully and using
  assumptions to simplify.  Several hours of algebra.
- **Finer natural-form search** with more candidates, including
  products/sums involving n_νt = 1, s_ν = 0.022, or trigonometric
  functions.  Might find the expression empirically even without
  derivation.

Neither is load-bearing for model-F.  The structural fact "k is
a fixed point, approximately 1.18/(8π), close to (1+4πα)²/(8π)"
is enough for model-F's documentation.

---

**Recommendation:** leave pool item f as "partially resolved;
full derivation deferred to future analytical work" in model-F
documentation.  Don't claim k is derived in closed form.
