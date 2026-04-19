# R60 Track 4: Per-sheet diagonal compensation for α universality

**Scope.**  Test whether allowing per-sheet `k_e ≠ k_p` (instead
of R59 F59's identical assumption) recovers both α universality
(α_e = α_p = α) and α magnitude (= observed α) on a metric with
internal shears active.  Free knobs: (L_ring_e, k_e, L_ring_p,
k_p).  Targets: (E_e=m_e, E_p=m_p, α_e=α, α_p=α).  Joint solve
via `scipy.optimize.least_squares` on the Track 1 solver; per-sheet
solves run in parallel as diagnostic.

Script: [scripts/track4_diagonal_compensation.py](scripts/track4_diagonal_compensation.py).

### F17. Smoke 1 — joint solver recovers R59 F59 on shearless clean

At (ε_e, s_e, ε_p, s_p) = (1, 0, 1, 0) the joint 4×4 solve
recovers `k_e = k_p = 3.978951e-2 ≈ 1/(8π)` to floating-point
precision, with all residuals at 10⁻¹⁴.  α_e/α = α_p/α = 1.000
exactly, masses exact.  Confirms the solver is well-posed and
finds the known answer without prompting.

### F18. Smoke 2 (Track 3 best) — per-sheet compensation works cleanly

At (ε_e, s_e, ε_p, s_p) = (0.1, 1.5, 0.55, 0.162037) — Track 3's
best universality point (1.05 ratio at uniform k):

| Quantity | Per-sheet solve | Joint solve | R59 F59 ref |
|----------|----------------|-------------|-------------|
| k_e | 2.572e-2 (0.646× nat) | **3.277e-2 (0.824× nat)** | 3.979e-2 |
| k_p | 2.607e-2 (0.655× nat) | **3.359e-2 (0.844× nat)** | 3.979e-2 |
| k_e / k_p | 0.987 | **0.976** | 1.0 |
| α_e/α at solve | 1.000000 | 1.000000 | — |
| α_p/α at solve | 1.000000 | 1.000000 | — |
| Universality | exact | exact | — |
| Sig OK | yes | yes (margin 2.6e-3) | — |

**Three observations:**

1. **Per-sheet diagonal compensation works.**  The user's
   hypothesis is confirmed at this point: tuning k per-sheet to
   compensate for shear-induced α distortion gives α_e = α_p = α
   exactly with signature preserved.

2. **The joint solve gives different k values than the
   independent per-sheet solves.**  Independent solves push k
   ~35% below natural; joint solve only ~17% below.  The
   difference is the cross-sheet contamination — each sheet's
   α extraction depends on the joint inverse metric, so the
   "right" k for each sheet depends on the other sheet too.
   Joint solve is the correct one to trust.

3. **k_e/k_p stays close to 1 at this point.**  R59 F59's
   identical-k assumption is approximately preserved (0.976
   ratio).  This isn't always the case — F20 shows it can vary
   wildly elsewhere.

### F19. Stress + pathology — two distinct failure modes

**Stress (Track 3 worst, ε_e=1.0, s_e=1.5, ε_p=0.55, s_p=0.162):**
Joint solve fails — converges at residual 100 (signature penalty)
because no (k_e, k_p) restores α magnitude without breaking
signature.  At this point `s_e · ε_e = 1.5` puts the e-sheet near
Track 2's hyperbolic boundary; the joint signature budget (F14)
collapses too tight for k retuning.  **Failure mode: signature
breach.**

**Pathology (ε_e=0.5, s_e=2.0, ε_p=0.55, s_p=0.162):**  Joint
solve "converges" but with α_e/α = 0 stuck at zero, residual −1.
Per-sheet e-only solve confirms α_e = 0 at *any* k_e — there is
no k that restores it.

**Mechanism:** the electron mode (1, 2) at `s_e = 2 = n_r/n_t` is
exactly on the shear cancellation point.  R53's argument was that
this makes the electron the lightest charged mode (μ → 1/ε
because the ring detuning vanishes).  We now find that **the same
condition makes Q_e = 0** — the e-tube and shear-induced e-ring
contributions to G⁻¹[:, t] cancel for the (1, 2) mode.

So the mechanism that produces R53's electron lightness is **the
same mechanism that decouples the electron from S** under the
R59 F59 architecture.  Profound and probably general:
*generation resonance ↔ electromagnetic decoupling on the same
sheet.*

This is a structural finding worth its own follow-up — flagged
as a candidate for a focused study (perhaps "R53/R59
incompatibility theorem"); deferred for now.

**Failure mode: structural sign-flip cancellation.**  No k can
rescue.

### F20. Grid map — per-sheet k is NOT a function of own (ε, s) alone

3×3×3×3 grid scan (81 points) over (ε_e, s_e) ∈ {0.1, 0.5, 1.0} ×
{1.5, 2.0, 2.5} and (ε_p, s_p) ∈ {0.1, 0.55, 1.0} × {0.1, 0.5,
1.0}.  **54 of 81 points (66%) converge cleanly** with α_e = α_p
= α exact and signature OK.

**Failure clusters:**

- All `(ε_e=1.0, s_e=2.0)` and `(ε_e=1.0, s_e=2.5)` — signature
  breaks (`s_e · ε_e ≥ 2.0`, near or over Track 2 boundary).
- All `(ε_e=0.5, s_e=2.0)` — α_e = 0 cancellation (the F19
  pathology generalized to ε_e = 0.5).

**k_e dependence on cross-sheet parameters.**  For (ε_e=0.1,
s_e=1.5) at fixed e-anchor across 9 different (ε_p, s_p)
combinations: k_e values range 3.10e-2 to 5.16e-2 — **54%
spread**.  The joint k_e is *not* a clean function of (ε_e, s_e)
alone; it depends meaningfully on the other sheet via shared ℵ.

Same pattern for k_p, with even larger spread (~200% across
e-anchors at fixed (ε_p, s_p)).

**Implication.**  R59 F59's `k = 1/(8π)` was a *global* natural
constant on a clean metric.  In R60 with shears, k is a
*per-configuration* derived value with no clean closed form in
terms of one sheet's (ε, s) alone.  The per-sheet compensation
mechanism works — but the values aren't elegantly determined.

### F21. Net of Track 4 — partial rescue, real but not clean

**What's positive:**

- **Per-sheet diagonal compensation rescues α universality and
  magnitude in 66% of tested (ε, s) configurations.**  R59 F59's
  α architecture is more general than its clean-metric demonstration
  suggested — it can absorb shears via per-sheet k retuning.
- **Track 3's best point (0.1, 1.5)e + (0.55, 0.162)p is fully
  rescued.**  Joint solve gives an exact, signature-OK
  configuration with both α targets met and k_e/k_p close to 1.
- **R59 F59 reproduces exactly at the shearless reference.**

**What's negative:**

- **k is no longer a single global constant.**  Each
  configuration has its own per-sheet k values, and they depend
  on the joint geometry (54% spread for k_e at fixed (ε_e, s_e)
  across different p-sheets).  The "natural-form" elegance of
  R59 F59's `1/(8π)` is lost in the joint setting.
- **A structural pathology exists at the R53 generation
  resonance.**  Whenever `s · ε = n_r/n_t · ε` for the
  reference mode, that sheet's α_Coulomb cancels to zero and no
  k can restore it.  Likely general: **the R53 generation
  mechanism and the R59 α architecture are partially
  incompatible at the resonant point itself.**
- **Joint signature constraint (F14) bounds the viable region.**
  At `s · ε ≈ 2`, signature breaks even with k retuning.

**What this means for R60.**

- The viable (ε, s) region for model-F is narrower than Track 2/3
  suggested: it must avoid both the Track 2 signature cliff AND
  the R53-resonance α-decoupling pathology.  At minimum: stay
  *off* the strict resonance `s_e = n_r/n_t` (probably want
  `s_e` modestly above 3/2 but not equal to 2 or other integer
  ratios).
- The model-F architecture has now been validated as **viable in
  principle** at one or more configurations.  Pool item **c**
  (joint metric search across all targets) becomes much more
  tractable knowing that the α machinery rescues at most points.
- The "elegance" of R59 F59's natural-form values (k = 1/(8π))
  is downgraded from "exact constant" to "approximate at small
  shears, varies by tens of percent at moderate shears."  Still
  natural-form-ish at typical points, but not algebraic.

**Recommendation for next steps.**

The user's per-sheet hypothesis is confirmed in spirit.  Three
options:

1. **Proceed to Track 5 (ν-sheet)** with the rescue mechanism in
   hand.  Join all three sheets and solve for (k_e, k_p, k_ν,
   L_e, L_p, L_ν) against a wider target set.  Practical, builds
   on the working machinery.
2. **Pool item f (analytical derivation)** of the cancellation
   condition `Q_e = 0 at s_e = 2 with (1,2) mode`.  If derivable,
   it tells us exactly which (ε, s) curves to avoid — a
   structural map of the pathology.  Cheap, high-leverage.
3. **Investigate R53/R59 incompatibility** as a focused study.
   The discovery in F19 that generation resonance and α
   decoupling coincide is too important to leave as a footnote;
   it may have implications for whether the R53 picture survives
   in any α-coupled architecture.  Probably warrants its own
   study (R61 or sub-track).

I'd recommend **2 → 1**.  Get the analytical map of the
α-decoupling locus first (cheap), then proceed to ν-sheet with
known no-go regions marked.


