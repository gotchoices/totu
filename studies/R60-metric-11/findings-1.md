# R60 Track 1: Solver infrastructure

**Scope.**  Build and validate the primitives every later track needs:
a parametric 11D metric builder, signature check, mode-energy computation,
α_Coulomb extractor, and a thin `scipy.optimize.least_squares`-based
joint fitter.  No physics conclusions — only tested machinery.

Script: [scripts/track1_solver.py](scripts/track1_solver.py).  Run via
`.venv/bin/python studies/R60-metric-11/scripts/track1_solver.py`.

### Review of variables

- **11D metric** — the 11-index layout is (ℵ, p_t, p_r, e_t, e_r, ν_t,
  ν_r, S_x, S_y, S_z, t).  Time index `I_T = 10` carries the Lorentzian
  −1 diagonal; the three S indices are Euclidean +1; the ℵ diagonal is
  `g_aa` (default 1); the 6-index Ma slice `MA_SLICE = [1..6]` holds the
  three 2×2 sheet blocks.
- **Sheet block (dimensionless)** — for a sheet with aspect ratio ε,
  shear s, and diagonal scale k, the 2×2 dimensionless block is
  `k · [[1, s·ε], [s·ε, 1 + (s·ε)²]]`.  Derived from
  `G_phys = B^T B` with `B = diag(L_tube, L_ring)(I + [[0, s], [0, 0]])`
  then normalized by `L_i L_j`.
- **k (diagonal scale)** — R59 F53 found α_Coulomb scales roughly as 1/k²
  at fixed σ_ta.  The model-E normalization is k = 1; the R59 F59
  natural-form α match requires k = 1/(8π) ≈ 0.040 on the charged sheets.
- **σ_ta** — tube↔ℵ off-diagonal magnitude.  Signed per sheet: +1 for e,
  −1 for p, 0 for ν (charge neutrality).  Natural value √α (R59 F59).
- **σ_at** — ℵ↔t off-diagonal.  Natural value 4πα (R59 F59).
- **α_Coulomb extraction** — `Q = (ñ_Ma · G⁻¹[Ma, t]) × (−G⁻¹[t, t])`,
  then `α = Q² / (4π)`.  This is the R59 track3g formula; it reports the
  effective Coulomb coupling that would be felt in S by a static mode.

### F1. T1 — 11D reproduces model-E masses when α knobs are off

Build the 11D metric with model-E Ma parameters (R53 Solution D on e,
R54 on p, R49 Family A on ν), all α-coupling knobs set to zero, k = 1
on every sheet.  Compute mode energies of the electron (1, 2, 0, 0, 0, 0)
and proton (0, 0, 0, 0, 1, 3) on the Ma subspace.

| Quantity | Expected | Computed | Relative error |
|----------|----------|----------|----------------|
| E(electron) | 0.5109989461 MeV | 0.5109989461 MeV | 1.7 × 10⁻¹¹ |
| E(proton)   | 938.272 MeV      | 938.272 MeV      | 1.2 × 10⁻¹⁶ |
| signature_ok | True (1 neg eig) | True | — |

**Interpretation.**  The 11D embedding does not disturb model-E's mass
predictions when the new dimensions (ℵ, t, S) are decoupled from Ma.
The sheet block formula `k · [[1, sε], [sε, 1 + (sε)²]]` reproduces
model-E's `μ_sheet = √((n_t/ε)² + (n_r − s·n_t)²)` exactly.

**What this means.**  The Ma-mass arm of every later track will reduce
to the model-E computation when the α knobs are off, and perturbatively
shift as they are turned on.  Any mass-prediction disagreement with
model-E will come from α coupling, not from the 11D wrapping.

### F2. T2 — R59 F59 natural-form point gives α_Coulomb = α to 60 ppm

Build the clean metric R59 Track 3g used (shearless Ma, k = 1/(8π) on
charged sheets, g_aa = 1, σ_ta = √α with signs +/−/0, σ_at = 4πα),
compute α_Coulomb for the electron and proton reference modes.

| Quantity | Value | Ratio to α |
|----------|-------|------------|
| α_e      | 0.007297798 | 1.000061 |
| α_p      | 0.007297798 | 1.000061 |
| α_e / α_p | 1.000000000 | — |
| α_ν      | 0 (exact)   | 0 |

**Interpretation.**  The α extractor reproduces R59 F59 at 60 ppm —
matching the R59 headline result to the reported precision.  Universality
is exact to floating point (α_e = α_p to 10+ digits), consistent with
R59 F45 (structural universality from |n_tube| = 1).  ν is exactly
neutral because sign_nu = 0 zeros the ν-tube↔ℵ entry.

**What this means.**  The α arm of every later track starts from a
validated extractor and a known reference point.  Any deviation from
60 ppm in future fits is signal about the geometry, not about the tool.

### F3. T3 — F41 signature rejection on shear-saturated e-tube

Build the model-E metric plus tube↔ℵ coupling at σ_ta = √α and σ_at = 4πα.
Expect signature failure (R59 F41: model-E's s_e = 2.004 saturates the
e-tube against any additional tube coupling).

| Configuration | Neg eigs | signature_ok |
|---------------|---------:|:-------------|
| Model-E Ma + σ_ta = √α, σ_at = 4πα | 2 | False |
| Model-E Ma + σ_ta = σ_at = 0.01    | 2 | False |

**Interpretation.**  Any tube↔ℵ coupling — even at σ = 0.01 — pushes a
second eigenvalue negative on model-E geometry.  This is R59 F41
exactly: the shear-saturated e-tube will not tolerate additional ℵ
coupling on top of the in-sheet shear.

**What this means for R60.**  R60 cannot run the R59 F59 α architecture
directly on model-E.  Either (i) find a smaller s_e that preserves the
lepton-generation ratios (pool item **a**), or (ii) move α to a
different architecture (pool item **g**).  This track confirms the
obstruction computationally; it does not yet point to a resolution.

### F4. T4 — Single-knob solve of L_ring_e converges cleanly

Start from model-E Ma geometry but with L_ring_e = 1000 fm (deliberately
bad initial guess, two orders of magnitude off).  One residual (m_e
fractional error), one free knob (L_ring_e), bounds [1, 10⁶] fm.

| Quantity | Closed-form | Solver result | Relative error |
|----------|-------------|---------------|----------------|
| L_ring_e | 11.88209756 fm | 11.88209756 fm | 1.6 × 10⁻¹⁰ |
| residual(m_e) | 0 | −1.4 × 10⁻¹⁰ | — |

scipy.optimize.least_squares converged to the analytical
`L_ring = 2π ℏc · μ / m · √k⁻¹` value at floating-point precision,
reaching `gtol` termination.

**Interpretation.**  The fitter wraps scipy correctly, responds to a
poor initial guess, and hits the analytical answer to floating-point
precision on a target with a known closed form.

**What this means.**  The solver can be trusted for well-posed
single-knob fits.  Multi-knob fits will be tested once later tracks
start using them against particle targets.

### Sanity (not part of acceptance): electron at α-on

An auxiliary run confirms the solver works end-to-end with α coupling
active: clean Ma (s=0), k_e = k_p = 1/(8π), σ_ta = √α, σ_at = 4πα,
eps_e fixed at 1.5, fit L_ring_e against m_e.

| Quantity | Value |
|----------|-------|
| L_ring_e (fit) | 25643.36 fm |
| E_e (at fit)   | 0.5109989462 MeV (target 0.5109989461) |
| α_e / α       | 1.00006 |

Not a physics claim.  Only shows the pipeline composes: α extraction,
mass computation, and fitting all work together inside one Params
construction.  The eps_e = 1.5 choice is arbitrary; a physics run
would vary it too.

## Track 1 status

Complete.  All four smoke tests pass.  The 11D metric builder,
signature check, mode-energy formula, α_Coulomb extractor, and
least-squares fitter are validated against known reference points
(model-E masses, R59 F59, R59 F41).

### What's ready for next tracks

- `build_metric_11(params) → 11×11 array`
- `signature_ok(G) → bool`
- `mode_energy(G, L, n11) → float MeV`
- `alpha_coulomb(G, n11) → float`
- `solve(params0, free, targets) → SolveResult`
- `Params` dataclass with model-E defaults and R59 α-knob fields

All importable from
[scripts/track1_solver.py](scripts/track1_solver.py).

### What's not yet built

- Coupled mass shift from α-on: the mode energy currently uses the Ma
  subspace in isolation.  R59 F13 reported ~1.3% shift when ℵ coupling
  turns on; this back-reaction must be modeled before any α-on mass
  target is interpreted physically.  Deferred until a later track
  actually needs it — most "find a particle at α-off, then check mass
  shift at α-on" tracks can use the current primitive.
- Cross-sheet σ (R54 neutron-region entries σ₄₅, σ₄₆) is supported by
  the Params interface but not yet exercised by a smoke test.
- No ν-sheet mass calibration yet — L_ring_ν is a 1 fm placeholder.
  Later tracks that touch neutrino physics will need to add that.

### Decision point

Next track pool items (a, b, c, d, e, f, g) in
[README.md](README.md) are unchanged.  Recommendation: pick **a**
(smallest-s_e resonance solution) next — it directly targets the F3
obstruction.  If a low-|s_e| solution that preserves m_μ/m_e and
m_τ/m_e exists, F3 is unblocked and Tracks c–e become straightforward.
If it doesn't, we pivot to **g** (alternative α architecture).


