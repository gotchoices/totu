# R60 Track 3: Proton sheet viability map

**Scope.**  Same idea as Track 2 but for the proton sheet.
Characterize the (ε_p, s_p) range where R59 F59 α is signature-OK
with the proton sheet active alongside the e-sheet.  Test multiple
e-sheet anchors to see if the e-sheet choice changes the p-region.
Verify R59 F45 universality (α_p / α_e ≈ 1) on the joint metric.
L_ring_p derived from m_p (closed form); free knobs only ε_p, s_p.

Script: [scripts/track3_proton_sheet.py](scripts/track3_proton_sheet.py).

### Review of variables

- **Region C** — p-sheet alone, e-sheet uncoupled (sign_e = 0).
  Analogue of Region B from Track 2 but for the proton.
- **Region D** — joint e+p signature-OK with both sheets active
  at R59 F59 α knobs (sign_e = +1, sign_p = −1, |σ_ta| = √α
  on both tubes).  Depends on the chosen e-sheet anchor.
- **R59 F45 universality** — claim that α_e / α_p = 1 is
  structural at k_e = k_p = 1/(8π) for any |n_tube| = 1 mode.
  Demonstrated in R59 on a *shearless* clean Ma metric.  Track 3
  tests whether it survives nonzero internal shears.

### F11. Smoke check reveals immediate universality breakdown

Joint metric with e-sheet at (ε_e=1, s_e=3/2) and p-sheet at
model-E (ε_p=0.55, s_p=0.162037), R59 F59 α knobs on:

| Quantity | Value | Ratio to α |
|----------|-------|------------|
| α_e | 3.45 × 10⁻³ | 0.473 |
| α_p | 3.03 × 10⁻² | 4.154 |
| α_p / α_e | 8.78 | (R59 F45 said 1.0) |

Signature OK, masses exact by L_ring derivation.  But
**universality is broken by nearly an order of magnitude, and α
magnitude on each sheet is far from observed**.  R59 F59's
"structural universality" was a property of the shearless clean
Ma metric.  As soon as nonzero internal shears (s_e ≥ 3/2 from
Track 2 ghost order; s_p arbitrary) are introduced, both
universality and α magnitude break.

This is a **major negative finding** for the R60 program.  See
F15 for the mechanism and F16 for implications.

### F12. Region C (p-sheet alone) is identical in form to Region B

Boundary refinement on the p-sheet-only configuration
(sign_e = sign_nu = 0, sign_p = −1) reproduces the Track 2
hyperbolic bound exactly:

| s_p | ε_p_max at cliff | s_p · ε_p |
|----:|:--------:|:------:|
| 0.50 | 4.2419 | 2.1209 |
| 1.00 | 2.1209 | 2.1209 |
| 1.50 | 1.4140 | 2.1209 |
| 2.00 | 1.0605 | 2.1209 |
| 2.50 | 0.8484 | 2.1209 |
| 3.00 | 0.7070 | 2.1209 |

**Region C boundary**: `s_p · ε_p ≤ 3/√2 ≈ 2.121`.

Identical to Region B (Track 2 e-sheet alone).  The single-sheet
signature bound is sheet-symmetric — depends only on |σ_ta|, not
on which tube it's on.  Region C covers 32.4% of the scan grid
(same as Region B).

### F13. Region D (joint e+p) is anchor-dependent and tighter

Joint signature scans for four representative e-sheet anchors:

| e-anchor | (s_e ε_e) | s_p · ε_p bound | Region D pts | Model-E p (0.55, 0.162) included? |
|----------|-----------|-----------------|-------------:|:---------------------------------:|
| (1.0, 1.5) corner-1.0   | 1.5  | **1.1173** | 1897 (25.7%) | yes (margin 2.6e-3) |
| (1.4, 1.5) corner-edge  | 2.1  | **0.0**    | 0 (0.0%)     | **no** |
| (0.1, 1.5) high-margin  | 0.15 | **1.8644** | 2293 (31.1%) | yes (margin 2.4e-2) |
| (0.5, 2.0) mid-shear    | 1.0  | **1.5806** | 2161 (29.3%) | yes (margin 8.1e-3) |

**Two structural findings:**

(a) **The joint bound is consistently lower than 2.121**, and it
varies sharply with the e-anchor.  The "corner-edge" anchor
(near the Track 2 signature boundary) collapses Region D to
empty.  Choosing the e-anchor near Track 2's hyperbola eats all
the margin.

(b) **The model-E p-sheet (0.55, 0.162) is included in 3 of 4
e-anchors** with various margins.  The architecture *does*
admit model-E's proton geometry — but only when the e-sheet sits
comfortably inside Track 2's overlap, not at its edge.

### F14. The joint signature bound has an exact algebraic form

Combining the four e-anchor measurements with the single-sheet
result (Region C boundary = 2.121² = 9/2):

| (s_e ε_e)² | (s_p · ε_p)²_max | Sum |
|------------|------------------|-----|
| 0.0000  | 9/2  = 4.500 | 4.500 |
| 0.0225  | 1.864² = 3.475 | 3.498 |
| 1.0000  | 1.581² = 2.499 | 3.499 |
| 2.2500  | 1.117² = 1.249 | 3.499 |
| 4.4100  | (infeasible)   | — |

When *both* tubes carry σ_ta, the joint signature bound is

    (s_e · ε_e)² + (s_p · ε_p)² ≤ **7/2**

(consistent to 4 digits across the four anchors tested).  The
single-active-tube bound is 9/2; adding a second active tube
costs exactly **1**.  Likely an exact algebraic identity arising
from the specific R59 F59 knob set (k = 1/(8π), σ_ta = √α,
σ_at = 4πα, g_aa = 1).  Derivation deferred to pool item **f**.

The "1" budget per tube has a natural interpretation: each
σ_ta = √α coupling pulls one unit of "negative-eigenvalue
budget" from the Lorentzian t direction.  At zero coupling, the
9/2 bound is the full budget; each additional active tube spends
one unit.

For three coupled tubes (e + p + ν, if we ever turn on
sign_nu = ±1) the predicted bound would be (s_e ε_e)² + (s_p
ε_p)² + (s_ν ε_ν)² ≤ 5/2.  In R59 F59 the ν-tube is uncoupled,
so this remains a prediction to test only if/when ν coupling is
considered.

### F15. α universality and α magnitude both fail under shears

Universality and magnitude reported across (e-anchor) × (p-candidate)
combinations on the joint metric:

| e-anchor | p-candidate | α_e/α | α_p/α | α_p/α_e |
|----------|-------------|------:|------:|--------:|
| (1.0, 1.5) | model-E (0.55, 0.162)  | 0.473 |  4.154 | 8.78 |
| (1.0, 1.5) | high-margin (0.1, 0.1) | 0.468 |  7.043 | 15.06 |
| (0.1, 1.5) | model-E (0.55, 0.162)  | 0.531 |  0.558 | 1.05 |
| (0.1, 1.5) | (1.0, 1.5)             | 4.045 | 12.107 | 2.99 |
| (0.1, 1.5) | high-margin (0.1, 0.1) | 0.529 |  0.953 | 1.80 |
| (0.5, 2.0) | model-E (0.55, 0.162)  | ~0    |  1.071 | huge (numerical) |

**Three observations:**

1. **R59 F45 universality breaks immediately** when shears are on.
   Best ratio observed (0.1, 1.5)e + (0.55, 0.162)p gives
   α_p / α_e = 1.05 — better than 8.78 but still *not* structural.
2. **α magnitude is wrong** on every test point.  α_e ranges from
   0.47×α to 4.05×α; α_p from 0.56×α to 12.1×α.  Neither is
   close to R59 F59's clean-metric value of 1.000061×α.
3. **Mechanism: ring-mediated indirect t coupling.**  R59 F45
   universality required the only Ma-t coupling to come through
   tube↔ℵ entries.  With shear `s·ε ≠ 0`, the ring inherits
   indirect t coupling via the sheet block's `(ring, tube)`
   off-diagonal `s·ε` (R59 F43 noted this in a different
   context).  The ring contribution scales with `n_ring / L_ring`,
   which differs between sheets (electron `n_er = 2`, proton
   `n_pr = 3`, with different L's), so the ring leakage is
   species-dependent.  Universality dies.

The (0.5, 2.0)e + model-E p case shows α_e numerically zero —
likely the shear-induced ring leakage cancels the tube
contribution exactly at this geometry.  Catastrophic for the
electron's α extraction; symptomatic of the bigger problem.

### F16. Track 3 status and what this means for R60

Track 3 passes its **stated** acceptance: Region D is nonempty for
3 of 4 e-anchors, model-E's p-sheet is included in 3 of 4, the
joint bound is characterized analytically (F14).  But the
**physically more important** finding is F15: the R59 F59
architecture's α universality and magnitude do **not** survive
internal shears.  This was an unstated assumption of R60 and is
now refuted.

**What R60 has learned through Track 3:**

1. The R59 F59 architecture works only on a *shearless* Ma metric.
2. Particle spectrum requires shears (electron generations, ghost
   ordering, proton mode placement).
3. **These two conditions are incompatible.**  Either α universality
   and magnitude are sacrificed (Track 3's actual result), or
   shears are sacrificed (no spectrum).

**What's still possible:**

- **Re-tune the α knobs in the presence of shears.**  R59 F59's
  natural-form values (k = 1/(8π), σ_ta = √α, σ_at = 4πα) were
  found by scanning a *shearless* metric.  In R60, with shears,
  a different combination might restore universality and
  magnitude.  Searching for it is a new track (call it
  pool item **h** — shear-aware α tuning).
- **Re-derive the joint-bound identity** (F14) analytically.
  A clean derivation might suggest a per-sheet renormalization
  that restores universality.  Pool item **f**.
- **Try smaller shears.**  At low (s ε), F15 shows universality
  drifting back toward 1.  The high-margin anchor (0.1, 1.5)e
  + model-E p gave α_p/α_e = 1.05, only 5% off.  Maybe a
  parameter region exists where shears are large enough for
  ghost order but small enough that R59 F59 universality
  approximately survives.

**What's likely dead:**

- **R59 F59's claim of *structural* universality does not extend
  to the model-E spectrum.**  At best we can recover *approximate*
  universality at small (s ε); structural exactness is gone.
- **The natural-form value σ_ta = √α may not give α magnitude
  on shears.**  σ_ta will need to be tuned per shear configuration
  if α magnitude is required.

### Status

Complete.  Scope deliverables met.  But the architectural surprise
in F11/F15 is significant enough that R60 needs a strategy
decision before Track 4 (ν-sheet).  Pause here.

### Decision point

Three paths forward, in order of cost:

**(a) Accept approximate universality and continue.**  At small
(s ε) anchors, α_p/α_e is within ~5% of 1.  If we can find a
spectrum-compatible region where this holds for all charged
particles, the model-F program is intact (with weaker α claims).
Next: Track 4 = ν-sheet on the same lines, then a wider survey.

**(b) Pivot to shear-aware α retuning.**  Pool item **h**: scan
the α-knobs (k, σ_ta, σ_at, g_aa) in the presence of model-E-like
shears, looking for a configuration where α_e = α_p = α holds
even with shears on.  If found, R60 has a new natural-form
target.  If not, we know R59 F59 is irretrievably
shear-incompatible.

**(c) Pivot to analytical derivation first.**  Pool item **f**:
derive (i) the joint signature bound (s_e ε_e)² + (s_p ε_p)² ≤
7/2 in closed form, and (ii) the universality-breaking formula.
Could reveal whether (b) has any chance of succeeding before we
spend search effort on it.

I'd argue for **(c) → (b) → (a)**: cheap analytical work first,
then targeted search informed by it, then either continue or
adapt.  But this is a strategic call — your decision.


