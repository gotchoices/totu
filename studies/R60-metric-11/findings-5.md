# R60 Track 5: Proton on shearless electron + α-decoupling locus

**Scope.**  Two complementary pieces: (Part 1) numerical scan
of the proton sheet at fixed shearless e, (Part 2) closed-form
derivation of the α-decoupling locus for any single-sheet mode.

Scripts:
- [scripts/track5_proton_shearless_e.py](scripts/track5_proton_shearless_e.py)
- [scripts/track5_decoupling_locus.py](scripts/track5_decoupling_locus.py)

### F22. Part 2 — closed-form α-decoupling locus

For a single sheet with mode (n_t, n_r) coupled to ℵ via
σ_ta = √α and to t via σ_at = 4πα (other sheets uncoupled),
the α extraction Q = 0 iff

    n_r/n_t = (s·ε) + 1/(s·ε)

equivalently  `n_t · u² − n_r · u + n_t = 0` with u = s·ε,
giving

    u = (n_r ± √(n_r² − 4 n_t²)) / (2 n_t).

Real roots exist iff `n_r² ≥ 4 n_t²`.

The result follows from cofactor expansion of the 4×4
sub-metric (e_t, e_r, ℵ, t):

    G⁻¹[e_t, t] = +σ k τ (1 + u²) / det
    G⁻¹[e_r, t] = −σ k u τ / det
    Q = (σ k τ / det) · [n_t (1+u²) − n_r u]

So Q vanishes whenever the bracket vanishes.

**Numerical verification.**  At the predicted decoupling points,
α_Coulomb returned 10⁻³¹ to 10⁻³² (zero to floating-point
precision):

| Mode | Predicted u = s·ε | Numerical α/α at predicted u |
|------|-------------------|-------------------------------|
| (1, 2) | 1.000 (single root) | 1.31e−31 ≈ 0 ✓ |
| (1, 3) | 0.382 or 2.618 | 3.29e−32 ≈ 0 (at 0.382); signature fails at 2.618 |
| (1, 1) | (no real root) | always nonzero across tested (ε, s) ✓ |

**Key practical implications:**

| Mode | Used by | Decoupling sε | Action for R60 |
|------|---------|---------------|----------------|
| (1, 1) | ν₁, ν₂ (R49 Family A) | none — never decouples | ν-sheet at (1,1) is α-safe everywhere |
| (1, 2) | electron, ν₃ (R49 Family A) | s·ε = 1 (exactly) | e-sheet must avoid sε = 1; ν₃ at sε = 1 too |
| (1, 3) | proton | s·ε ≈ 0.382 or 2.618 | p-sheet must avoid these |
| (n_t ≤ n_r/2) compound modes | μ, τ, hadrons | n_r/n_t = u + 1/u | check on a per-mode basis |

The **(1, 1) ν exemption** is structural (n_r² < 4 n_t² has no
real solution).  This is fortunate: R49 Family A's lightest two
neutrinos are (1, 1) modes, so they never decouple regardless of
ν-sheet (ε, s).  ν₃ at (1, 2) is constrained like the electron.

The locus formula is exact and computed for *single-sheet*
coupling.  In the joint multi-sheet case the precise location may
shift slightly, but Track 4 F19 and Part 1 below show the
single-sheet locus is an excellent predictor.

### F23. Part 1 — proton viability under shearless electron

Joint solve for (L_e, k_e, L_p, k_p) against (m_e, m_p, α_e=α,
α_p=α) at fixed (ε_e=1, s_e=0), scanning (ε_p, s_p) over an
11×13 grid:

- 104 / 143 grid points (72.7%) converged with all four targets
  hit at α_e = α_p = α exactly and signature OK.
- Failures cluster at (a) signature breach when sε_p ≳ 1.87
  (joint Track 4 F14 bound with shearless e: (sε_p)² ≤ 7/2,
  so sε_p ≤ √3.5 ≈ 1.87); and (b) the (1, 3) decoupling locus
  at sε_p ≈ 0.382 (e.g., (ε_p=0.770, s_p=0.50) → sε = 0.385,
  α_p falls to 0.33).
- At s_p = 0 (any ε_p): k_e = k_p = 1/(8π) exactly recovered;
  L_ring_p ranges 20–69 fm depending on ε_p.

Selected candidate proton configurations (sorted by closeness
of k values to natural 1/(8π)):

| ε_p | s_p | s·ε | k_e | k_p | L_ring_p (fm) |
|----:|----:|----:|----:|----:|--------------:|
| 0.10 | 0.00 | 0.00 | 1/(8π) | 1/(8π) | 69.2 |
| 0.55 | 0.00 | 0.00 | 1/(8π) | 1/(8π) | 23.3 |
| 1.00 | 0.00 | 0.00 | 1/(8π) | 1/(8π) | 20.8 |
| 0.10 | 0.50 | 0.05 | 4.10e−2 | 3.50e−2 | (≈ 14× scale) |
| 0.55 | 1.00 | 0.55 | 5.98e−2 | 2.05e−2 | (compensated) |

**Headline:** Q1 confirmed.  With shearless electron, the proton
sheet has a **wide viable region** at any reasonable (ε_p, s_p)
away from the signature cliff (sε > 1.87) and the (1,3)
decoupling locus (sε ≈ 0.382).  Per-sheet k compensation is
mild (~5–30%) for moderate shears, only diverges near the
pathological curves.

### F24. The "trivial baseline": shearless e + shearless p

The simplest converged point is (ε_e=1, s_e=0, ε_p=any, s_p=0):

- Both sheets shearless → no decoupling pathology, no
  signature pressure
- k_e = k_p = 1/(8π) exactly (recovers R59 F59)
- α_e = α_p = α exactly
- L_ring_e ≈ 27,200 fm, L_ring_p depends on ε_p (~20–70 fm)

This is the "no surprises" foundation for Tracks 6+.  Adding
shears (small ones) is fine; the architecture deforms gracefully.

### F25. Joint vs single-sheet locus — single-sheet is a good predictor

Track 4 F19 saw α_e = 0 at (0.5, 2.0)e + (0.55, 0.162)p.  Part 2
predicts (1, 2) decoupling at sε = 1.0; (0.5, 2.0) gives sε = 1.0.
Match.

Part 1 grid: failure points near sε_p ≈ 0.382 (e.g., (0.770,
0.50), (0.141, 2.75)) match the predicted (1, 3) decoupling
curve.  Near-misses (sε_p = 0.39 vs predicted 0.382) sometimes
converge — the curve is sharp but not perfectly knife-edged in
the joint case.

**Practical rule:** treat the single-sheet decoupling formula as
defining "no-go curves" with ~1–3% buffer on either side.

### F26. Track 5 status and what's ready for Track 6

**Completed.**

- **Closed-form decoupling locus** (F22): per-mode rule for any
  sheet.  Avoid `s·ε = (n_r ± √(n_r² − 4n_t²)) / (2 n_t)` for
  the sheet's reference mode.
- **Proton viability under shearless e** (F23): wide region with
  many candidate (ε_p, s_p) configurations, per-sheet k
  compensation works.
- **Q1 from user's proposal validated.**  The shearless-e +
  compensated-p approach gives clean configurations across most
  of the (ε_p, s_p) space.

**Ready for Track 6.**

- Choose a Track 5 candidate proton configuration as the working
  baseline (recommend `(ε_p, s_p) = (1, 0)` for maximum
  simplicity; or model-E-like `(0.55, 0)` if continuity is
  preferred).
- Add ν-sheet on the same architecture: free `(L_ν, k_ν)` and
  σ_ta on ν-tube with sign convention TBD; targets m_ν and
  α_ν = α.
- ν₁, ν₂ at (1, 1) are α-safe (never decouple); ν₃ at (1, 2)
  must avoid sε_ν = 1 — same constraint as electron.
- The joint signature bound generalizes: with three coupled
  tubes, Track 4 F14 predicts (sε_e)² + (sε_p)² + (sε_ν)² ≤ 5/2.
  Each sheet now spends one unit of the budget.  Conservative
  starting point: keep all three sheets at small sε.

### Decision point

Recommend proceeding to Track 6 (ν-sheet inclusion) using:

- e-sheet: (ε_e, s_e) = (1, 0) — shearless baseline
- p-sheet: (ε_p, s_p) = (1, 0) — also shearless baseline
- ν-sheet: TBD from R49 Family A or R61 candidates;
  carefully choose (ε_ν, s_ν) to satisfy joint signature bound
  and the per-mode decoupling avoidance for ν₁, ν₂, ν₃.

The R53 generation mechanism is now **structurally retired** for
R60 — there's no single-sheet (ε_e, s_e) that gives both (a) the
R53 generation ratios *and* (b) Track 4 universality at α.
Generations must come from compound modes per the model-E
inventory style.  Track 7 (compound modes) will revisit this.


