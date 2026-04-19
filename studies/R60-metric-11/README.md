# R60: Metric-11 — particle spectrum on R59's α-derivable 11D architecture

**Status:** Framed — Track 1 ready
**Type:** theoretical + compute
**Depends on:** R59 (tube↔ℵ↔t architecture, F54 + F59), R53 (generations),
  R49 (neutrinos), R54 (compound modes), model-E

---

## Objectives

R59 closed with a viable 11D architecture for α coupling
(tube↔ℵ↔t) that produces α_Coulomb = α (within 60 ppm) at the
natural-form parameter point:

- σ_ta = √α (e-tube to ℵ at +√α; p-tube to ℵ at −√α)
- σ_at = 4πα (single ℵ to t entry)
- g_aa = 1 (ℵ diagonal)
- k = 1/(8π) ≈ 0.040 (Ma sheet diagonal scale, k_e = k_p)

Universality (α_e/α_p = 1.000) and ν neutrality (α_ν = 0) are
structural properties of the architecture, not tuning choices.

But the metric requires Ma diagonals at k = 1/(8π) — far smaller
than the model-E normalization of 1.  Model-E's internal shears
(especially s_e = 2.004) actively block this architecture.

R60 asks: can a metric configuration be found that simultaneously:

1. Implements R59's α architecture (k = 1/(8π), σ_ta = √α,
   σ_at = 4πα, g_aa = 1)
2. Reproduces the model-E particle spectrum (electron, proton,
   neutron, three lepton generations, neutrino mass eigenstates,
   hadron inventory)
3. Identifies which model-E mechanisms survive and which need
   replacement

If yes, R60 produces a successor candidate (potentially "model-F"
— though the model designation is deferred until viability is
established).  If no, R60 documents specifically which constraint
blocks it — narrowing the search for an alternative α mechanism.

The directory is named "metric-11" because the 11D structure
(adding ℵ to model-E's 9D Ma+S+t) is what's being explored;
whether this becomes model-F depends on R60's outcome.

---

## Execution plan

Tracks are added one at a time.  Only the currently-executing
track is numbered; candidates for "next track" live in the pool
below as lettered items and get numbered when chosen.  This keeps
the plan responsive to what each track actually reveals.

### Track 1 — Solver infrastructure (framed)

**Goal.**  Build and validate the 11D metric + joint-fit toolkit
that later tracks will use to search for particles one at a time.
No physics conclusions in this track — only tested machinery.

**Strategy.**

Implement four primitives and a thin fitting wrapper, each with
a smoke test against a known result.  Keep the API small; grow
it only when a later track needs something.

**Tactics.**

1. **Metric builder.**  `build_metric_11(params)` returns the
   11×11 array using the R59 index ordering ℵ, p_t, p_r, e_t,
   e_r, ν_t, ν_r, S_x, S_y, S_z, t.  Incorporates per-sheet
   in-sheet shear via B = diag(L)(I + S), per-sheet diagonal
   scaling k, tube↔ℵ entries with sign pattern (+, −, 0) for
   (e, p, ν), and the ℵ↔t entry.

2. **Signature check.**  `signature_ok(G)` — exactly one negative
   eigenvalue (the t direction).  Rules out knob combinations
   that break Lorentzian structure.

3. **Mode energy.**  `mode_energy(G, n_11)` for an 11-vector mode
   with zeros in the S and t slots.  Same quadratic form that
   R59 and model-E use, generalized to 11D.

4. **α_Coulomb extractor.**  `alpha_coulomb(G, n_11)` reproduces
   R59 track3g's formula:
   Q = (ñ · G⁻¹[:, t]) × (−G⁻¹[t, t]), then α = Q² / (4π).

5. **Joint fitter.**  `solve(params_free, params_fixed, targets)
   → (params, residuals, jacobian_info)` using
   `scipy.optimize.least_squares`.  Targets are a generic list of
   residual functions so later tracks can supply their own
   (mass residual, α residual, ratio residual).  This track does
   not hard-code the model-E target list.

**Smoke tests (infrastructure only).**

| # | Test | Expected outcome |
|---|------|-----------------|
| T1 | `build_metric_11` with all α knobs = 0 and model-E Ma params reproduces model-E's 6×6 mode energies | m_e, m_p agree with [lib/metric.py:model_E()](../lib/metric.py) to < 10⁻¹⁰ relative |
| T2 | `alpha_coulomb` on the R59 F59 clean metric (k = 1/(8π), g_aa = 1, σ_at = 4πα, σ_ta = √α) | α_Coulomb = α to < 100 ppm (matches R59 F59) |
| T3 | `signature_ok` rejects the F41 failure cases (model-E Ma + any tube↔ℵ entry) | returns False as expected |
| T4 | `solve` fits L_ring_e to a target m_e, all else fixed | converges to the same value as the closed-form expression L = 2πℏc μ / m_e |

**Deliverables.**

- `scripts/track1_solver.py` — primitives + `solve` wrapper + the
  four smoke tests above, runnable as `python track1_solver.py`.
- findings.md entries F1–F4 recording smoke-test results.

**Acceptance criteria.**

- All four smoke tests pass at the tolerances listed.
- The API is small enough to document in a few lines; later
  tracks import from this script (not copy-paste).

**Prototyping note.**  Lives in
[scripts/track1_solver.py](scripts/) only.  Promotion to `lib/`
is deferred until 2–3 later tracks have imported from it with
no changes — that's when the API is stable enough to share.

---

### Track 2 — Electron sheet viability map

**Goal.**  Characterize the electron sheet by itself, as a 2D
parameter problem in (ε_e, s_e).  Report:

1. The locus where the electron (1, 2) can be calibrated to m_e
   (trivial: any (ε_e, s_e) with L_ring_e free).
2. The region where (1, 2) is the lightest charged e-sheet mode —
   i.e., where the (1, 1) ghost sits above (1, 2).
3. The region where the R59 F59 α knobs (k_e = 1/(8π), σ_ta = √α
   on e-tube, g_aa = 1, σ_at = 4πα) preserve Lorentzian signature.
4. The overlap of (2) and (3), if any.

Stop here.  Muon and tau are compound in model-E (muon = e+ν,
tau = e+ν+p) and need the other sheets — they cannot be tested
before Tracks 3 (ν-sheet) and 4 (p-sheet) are built.

**Background.**  Track 1 T3 showed that R53 Solution D
(ε_e = 397.074, s_e = 2.004200) breaks signature under the R59
F59 α knobs.  It is unknown whether (a) a nearby (ε_e, s_e) works,
(b) the viable region is elsewhere entirely, or (c) no region
exists.  Track 2 answers this without committing to any
generation-ratio hypothesis.

**Strategy.**  Two independent constraints evaluated on the same
(ε_e, s_e) grid:

- **Ghost-order constraint.**  At each (ε_e, s_e), compute the
  single-sheet mode energies μ(1, 1, ε, s) = √(1/ε² + (1 − s)²)
  and μ(1, 2, ε, s) = √(1/ε² + (2 − s)²).  Ghost-order favorable
  iff μ(1, 1) ≥ μ(1, 2).  (Equivalently: |1 − s| ≥ |2 − s|,
  i.e., s ≥ 1.5.  Independent of ε.  Worth confirming by direct
  computation anyway.)
- **Signature constraint.**  Build the full 11D metric with only
  the electron sheet as the active material block (set ν and p
  sheets to identity placeholders, uncoupled) and the R59 F59 α
  knobs on.  Signature OK iff exactly one negative eigenvalue
  (the t direction).

The overlap of these two regions is the viable zone for Track 2's
purposes.  Track 2 does **not** test mass ratios, ghost
suppression beyond simple ordering, or compound modes.

**Tactics.**

1. Scan (ε_e, s_e) on a 2D grid: ε_e ∈ [0.1, 1000] log-spaced,
   s_e ∈ [−3, 3] linear.  At each point evaluate:
   (i) μ(1, 1) vs μ(1, 2) on the bare single sheet (fast, closed form).
   (ii) signature of the 11D metric with R59 F59 α knobs on.
   (iii) smallest-eigenvalue margin (how close to the signature
        cliff) at the passing points.
2. Plot the two regions and their overlap.  Mark the R53 Solution
   D point (397.074, 2.004200) and the R53 Solution B point
   (~330, ~3.00) for reference.
3. Report the overlap region in a form useful for Track 3:
   bounded box + a handful of representative (ε_e, s_e) points,
   with signature margin at each.

**Smoke cross-checks before the scan.**

- At (397.074, 2.004200) with α off: μ(1, 2) < μ(1, 1) (ghost OK
  per R53).
- At (397.074, 2.004200) with α on: signature fails (reproduces
  Track 1 T3).

**Deliverables.**

- `scripts/track2_electron_sheet.py` — grid scan + overlap report.
- findings.md F5 (ghost-order region), F6 (signature-OK region),
  F7 (overlap and representative points).
- No plot required unless the overlap is non-obvious; a clear
  textual description of the boundary is enough if it's a simple
  inequality in (ε_e, s_e).

**Acceptance criteria.**

- Ghost-order region and signature-OK region both reported over
  the full scan range.
- Overlap region identified (empty, bounded, or open).
- At least three representative (ε_e, s_e) points from the
  overlap (if nonempty) with signature margin listed, so Track 3
  has candidates to build on.

**Possible outcomes.**

- **Overlap nonempty.**  Track 3 (ν-sheet) proceeds against one
  of the candidate points.  We don't commit to a specific
  (ε_e, s_e) yet — just pick a point with comfortable margin and
  continue.
- **Overlap empty.**  R59 F59 α knobs are incompatible with a
  ghost-ordered e-sheet.  R60 revisits whether the α knobs can
  be relaxed (e.g., smaller σ_ta, different sign pattern) or
  whether a different α architecture is needed.  This is the
  model-F-existence question answered sharply at the first gate.

---

### Track 3 — Proton sheet viability map

**Goal.**  Same idea as Track 2 but for the proton sheet.
Characterize the (ε_p, s_p) range under which the R59 F59 α
architecture remains signature-OK with the proton sheet active
alongside an already-fixed electron sheet.  Calibrate L_ring_p
from m_p inside that range.  Constrain ranges where no single
preferred value is yet identified.

The proton in model-E is effectively a pure single-sheet (1, 3)
mode (its ν content is decorative; cross-sheet σ₄₅, σ₄₆ are
neutron knobs and don't move the proton).  Three quarks are
"ringings" of the n_pr = 3 ring symmetry — emergent, not separate
modes.  So the proton sheet can be characterized by its own
(ε_p, s_p) without invoking the ν or e sheets.

**Use model-E as a guide, not a pin.**  Model-E's (ε_p = 0.55,
s_p = 0.162) gives s · ε ≈ 0.089 — well inside the 3/√2 ≈ 2.12
Track 2 boundary, so almost certainly inside the joint
e+p signature region too.  Track 3 starts there as a smoke
check, then maps the actual range.

**Note on s_p being free.**  In model-E, s_p was fixed by R19
(`solve_shear_for_alpha(0.55, 1, 3) = 0.162`) — i.e., s_p was
the value that made R19 give α at that ε_p.  In R60 the α
mechanism has moved to Ma↔ℵ↔t coupling (R59 F59), so the R19
constraint is gone.  s_p is now genuinely free until pinned by
something else (compound modes, neutron, hadron near-misses —
all later tracks).

**Strategy.**

1. Fix the electron sheet at a representative Track 2 candidate.
   Recommended: (ε_e = 1, s_e = 3/2) — the analytic corner of
   the Track 2 overlap.  L_ring_e calibrated to m_e.
2. Scan (ε_p, s_p) over a 2D grid with the same span as Track 2.
3. At each (ε_p, s_p):
   (i)   Compute L_ring_p so that E(0,0,0,0,1,3) = m_p exactly
         (closed form, always achievable).
   (ii)  Build the full 11D metric with e+p sheets active, ν
         identity placeholder, R59 F59 α knobs on with sign_p
         = −1 on p-tube.
   (iii) Check signature.
   (iv)  Compute α_Coulomb on the proton mode (0,0,0,0,1,3) —
         universality demands α_p / α_e ≈ 1 by R59 F45.
4. Report Region C (signature-OK, p-sheet alone) and Region D
   (signature-OK with e-sheet active at the chosen point).
   Compare; characterize whether adding the p-sheet meaningfully
   tightens the signature region or not.

**Tactics.**

- Boundary refinement by bisection in ε_p along several s_p
  lines, parallel to Track 2's analysis.  Look for an analogous
  s · ε boundary; it may differ because the joint e+p
  configuration places more demand on ℵ.
- Smoke check at model-E (0.55, 0.162): expect signature OK,
  α_p / α_e ≈ 1 to 60 ppm, mass exact by construction.
- Compare Region D against several different e-sheet anchors
  (e.g., also (0.1, 1.5)) to see if the e-sheet choice
  materially changes the p-sheet viable range.

**Smoke cross-check before scan.**

- Model-E (ε_p, s_p) = (0.55, 0.162) with e-sheet at (1, 3/2):
  signature OK, α_p / α_e ≈ 1.

**Deliverables.**

- `scripts/track3_proton_sheet.py` — scan + boundary refinement +
  candidate report.
- findings.md F11 (smoke), F12 (Region C: p-sheet alone), F13
  (Region D: joint e+p), F14 (interpretation, candidate range,
  comparison to model-E).

**Acceptance criteria.**

- Region D characterized over the scan range with a clear
  bounded form (analytical inequality if it falls out, otherwise
  a numerical region with representative points).
- α_Coulomb universality verified on the joint metric: α_p / α_e
  within 1% across the viable region.
- At least three representative (ε_p, s_p) points reported,
  including one near model-E and one with maximum signature
  margin.

**Scope.**

- Only ε_p and s_p are varied; L_ring_p is derived from m_p.
- Ghost-ordering on p-sheet is **not** a Track 3 constraint
  (matches the Track 2 convention; (1,1) ghost suppression is
  handled by other mechanisms — waveguide, irreducibility, R47
  Track 7 gcd argument).
- No quark mass-ratio test (quarks are ringings of n_pr = 3,
  not separate modes; no R60 lever for them).
- No compound modes (neutron, mesons) — those are later tracks.

**Possible outcomes.**

- **Region D is wide.**  Proton sheet poses no architectural
  constraint; model-E's (0.55, 0.162) is comfortably inside.
  Carry forward and proceed to Track 4 (ν-sheet).
- **Region D is narrow but nonempty.**  Constrains the proton
  geometry but lets us pick a comfortable point.  Carry forward.
- **Region D excludes model-E.**  Proton sheet has a different
  viable range than model-E used.  Document and carry forward
  with a new working (ε_p, s_p).
- **Region D is empty.**  Joint e+p with R59 F59 α is
  structurally infeasible.  Major problem; revisit α
  architecture or e-sheet choice.

---

### Track 4 — Per-sheet diagonal compensation for α universality

**Goal.**  Test whether allowing the per-sheet diagonal scale to
differ between sheets (k_e ≠ k_p) can recover both α universality
(α_e = α_p = α) and α magnitude (= observed α) on a metric with
internal shears active.  Track 3 showed that R59 F59's identical-k
assumption is fragile under shear — this track checks whether the
fragility is the assumption or the architecture.

**Background.**  R59 F59 found that on a *shearless* clean Ma
metric, `k_e = k_p = 1/(8π)` with σ_ta = √α and σ_at = 4πα gives
α_Coulomb = α to 60 ppm with α_e = α_p exactly.  R59 F57
established that universality requires `k_e = k_p` *on that
metric*.  Track 3 showed that with shears on (s_e ≥ 3/2 from
ghost order, s_p free) both universality and magnitude break
even at identical k.  Working hypothesis: identical k was never
the real symmetry — what's required is *whatever per-sheet k
makes that sheet's α extraction land on observed α*.  In the
shearless case, that happens to be 1/(8π) for both sheets; with
shears, k_e ≠ k_p.

**Strategy.**

For fixed (ε_e, s_e, ε_p, s_p), solve for the four-knob vector
(L_ring_e, k_e, L_ring_p, k_p) such that:

| Target | Source |
|--------|--------|
| E(electron mode) = m_e        | mass calibration |
| E(proton mode)   = m_p        | mass calibration |
| α_Coulomb(electron) = α       | α magnitude (e-sheet) |
| α_Coulomb(proton)   = α       | α magnitude (p-sheet) |

Universality (α_e = α_p) follows automatically when both α
targets are met.

The solve is a 4×4 nonlinear system with `scipy.optimize.least_squares`
on the Track 1 solver.  Run in two modes for diagnostic value:

1. **Per-sheet independent.**  Two 2×2 solves: (L_ring_e, k_e)
   against (m_e, α_e), then (L_ring_p, k_p) against (m_p, α_p),
   each with the *other* sheet's α coupling turned off (sign = 0).
   Gives "what each sheet wants in isolation."
2. **Joint.**  One 4×4 solve with both sheets active.  The
   "right" answer because in the joint metric each sheet's α
   extraction depends on the other sheet (via the shared ℵ).
   Compare to (1) to quantify cross-sheet contamination.

**Tactics.**

1. **Smoke at shearless clean.**  At (ε_e, s_e, ε_p, s_p) =
   (1, 0, 1, 0), the solver should converge to k_e = k_p = 1/(8π)
   with both α targets met (R59 F59 reproduction).  Sanity that
   the joint solve recovers known-good values.
2. **Smoke at Track 3 best point.**  At (ε_e=0.1, s_e=1.5,
   ε_p=0.55, s_p=0.162), Track 3 found α_p/α_e = 1.05 already.
   Joint solver should pull this to exactly 1 with mild k
   adjustments.
3. **Stress at Track 3 worst point.**  At (ε_e=1.0, s_e=1.5,
   ε_p=0.55, s_p=0.162), Track 3 reported α_p/α_e = 8.78.
   Solver either converges with very different k_e, k_p, or
   fails — either outcome is informative.
4. **Pathology check.**  At (ε_e=0.5, s_e=2.0, ε_p=0.55,
   s_p=0.162), Track 3 reported α_e ≈ 0 (sign-flip cancellation).
   The α_e target may have no real-k solution; document the
   failure mode.
5. **Map k_e/k_p as a function of (ε, s).**  For a small grid of
   (ε_e, s_e) and (ε_p, s_p) pairs inside the Track 3 viable
   region, run the joint solve and tabulate the resulting k_e
   and k_p.  Look for patterns (e.g., does k_x scale with
   (ε_x · s_x) in a clean way?  Does the ratio k_e/k_p depend
   only on the difference between sheets?).

**Smoke cross-checks before search.**

- Build the shearless clean metric with the R59 F59 knobs, run
  `alpha_coulomb` — should give 1.000061×α (matches Track 1 T2).
- Initial guess for joint solve: k_e = k_p = 1/(8π) and
  L_ring_x derived from m_x at that k.  At a viable point, the
  solver should improve from this seed.

**Deliverables.**

- `scripts/track4_diagonal_compensation.py` — independent + joint
  solves at the four representative points above, plus the (ε, s)
  map.
- findings.md F17 (smoke at clean), F18 (per-sheet vs joint
  diagnostic), F19 (results across representative points), F20
  (k_e/k_p patterns and what they imply).

**Acceptance criteria.**

- The joint solve converges at the shearless clean point to
  R59 F59's k = 1/(8π) within solver tolerance.
- At least one (ε, s) pair inside Track 3's viable region yields
  α_e = α_p = α to ≤ 1% with a real, signature-OK metric.
- The solver's failure modes (where they occur) are clearly
  characterized: sign-flip pathology, no-real-k region,
  signature breach, etc.

**Possible outcomes.**

- **Clean convergence everywhere.**  Per-sheet k *is* a function
  of that sheet's (ε, s) — α universality is recovered at the
  cost of an extra knob per sheet (no longer assumed identical).
  R59 F59 generalizes cleanly; model-F program is alive.
  Promote pool item **f** (analytical derivation of k(ε, s)).
- **Convergence in some regions, failure in others.**  R59 F59
  is *partially* generalizable.  Model-F is constrained to the
  regions where Track 4 succeeds.  Map them.
- **No convergence anywhere with shears.**  R59 F59's natural
  α-knob set is irretrievably shear-incompatible.  R60 must
  either accept approximate universality (path a in Track 3
  decision) or pivot to a different α architecture (pool item g).

---

### Track 5 — Proton on shearless electron + α-decoupling locus

**Goal.**  Two complementary pieces, run together because they
inform each other:

1. **Numerical: confirm Q1.**  Show that with the electron sheet
   left shearless (s_e = 0), the proton sheet at any reasonable
   (ε_p, s_p) inside Track 4's working region can be calibrated
   to m_p with α_p = α via per-sheet diagonal compensation k_p.
   The Track 4 Smoke 1 (clean) and Smoke 2 (T3 best) points
   already suggest this works; Track 5 maps the proton viable
   region against a fixed shearless-e baseline.

2. **Analytical: derive the α-decoupling locus.**  Track 4 F19
   discovered that at s_e = n_r/n_t for the electron's reference
   mode (specifically s_e = 2 for the (1, 2) electron), the α
   extraction Q_e cancels to zero independent of k_e.  Derive
   the closed-form condition Q_e = 0 in (ε, s) so we know which
   curves to avoid in *every* later (ε, s) scan.  This is the
   pool-item-f analytical complement to the numerical work.

The two pieces share infrastructure (Track 1 solver) and
context, so combining them keeps the analysis coherent.

**Strategy.**

*Part 1 (numerical).*

Fix the electron sheet at (ε_e = 1, s_e = 0).  This sits inside
Track 4's confirmed-working region (Smoke 1 reproduces R59 F59
exactly there).  Vary the proton sheet (ε_p, s_p) over a 2D grid
spanning Track 3's Region D.  At each grid point:

- Run Track 4's joint solver over (L_ring_e, k_e, L_ring_p, k_p)
  against (m_e, m_p, α_e=α, α_p=α).
- Record convergence, signature, residuals, k values.
- Map the proton viable region under shearless e-sheet.

If the viable region is wide and includes natural starting
points (e.g., model-E's (0.55, 0.162) or analytically nice
choices like (1.0, 0.0) or (0.5, 0.5)), Q1 is confirmed and we
have a clean baseline for Track 6 (ν-sheet).

*Part 2 (analytical).*

Compute Q_e symbolically for the electron mode (1, 2) on the
e-sheet alone (other sheets uncoupled, sign_e = +1).  The
expression

    Q_e = (n_e_tube/L_e_tube · G⁻¹[e_t, t]) +
          (n_e_ring/L_e_ring · G⁻¹[e_r, t])

depends on the inverse metric block.  With the 2×2 sheet block
`k·[[1, sε], [sε, 1+(sε)²]]`, the e-tube and e-ring entries of
G⁻¹[:, t] propagate through the (e-tube ↔ ℵ ↔ t) chain.  Find
the (ε, s) curve where the two terms cancel.

Hypothesis (from F19 evidence): the curve is `s = n_r/n_t = 2`
for the (1, 2) mode, independent of ε — but we should derive
this rather than assume.  Generalize for arbitrary (n_t, n_r).

If derivable, the result tells us:
- Which (ε, s) curves to avoid for *each* sheet (e-sheet, p-sheet,
  ν-sheet) given that sheet's reference mode.
- Whether the locus is exactly s = n_r/n_t or has corrections.
- How "wide" the pathology is (sharp curve vs broad band).

**Tactics.**

- Part 1: extend [scripts/track4_diagonal_compensation.py]
  with a (ε_p, s_p) grid scan at fixed shearless e.  ~15×15 grid
  should suffice.
- Part 2: write `scripts/track5_decoupling_locus.py` that does
  the symbolic derivation either by hand-derived closed form
  or via `sympy` for the 11D inverse metric.  Cross-check
  numerically against the actual Q_e from `alpha_coulomb`.

**Smoke cross-checks.**

- Part 1: at (ε_e=1, s_e=0, ε_p=1, s_p=0), reproduce Track 4
  Smoke 1 (k_e=k_p=1/(8π), all targets exact).
- Part 2: at (ε=0.5, s=2.0) the derived Q_e should equal zero
  (matches Track 4 F19); at (ε=1, s=0) it should be nonzero.

**Deliverables.**

- `scripts/track5_proton_shearless_e.py` — Part 1 grid scan
- `scripts/track5_decoupling_locus.py` — Part 2 derivation
- findings F22 (Part 1 results), F23 (Part 2 derivation), F24
  (combined interpretation: viable proton region + pathological
  curves)

**Acceptance criteria.**

- Part 1: viable region for (ε_p, s_p) under shearless e is
  characterized; at least three concrete candidate proton
  configurations identified.
- Part 2: closed-form expression for the Q_e = 0 locus on a
  single sheet with reference mode (n_t, n_r), validated against
  numerical Q_e from the Track 1 extractor.

**Possible outcomes.**

- **Wide proton region + clean locus formula.**  Best case.  R60
  has a simple rule for choosing (ε, s) per sheet ("stay off
  s = n_r/n_t for the reference mode"), and the proton has many
  options.  Proceed to Track 6 confidently.
- **Narrow proton region or messy locus.**  Constraints tighter
  than expected; we need to be more careful about (ε_p, s_p)
  choice.  Report and proceed.
- **Empty proton region.**  Surprising; would indicate the
  shearless-e + compensated-p approach is itself blocked.
  Pivot needed.

---

### Track 6 — Add the ν-sheet (joint e+p+ν solver)

**Goal.**  Add the ν-sheet on the same architectural footing as
e and p, then joint-solve for all six free knobs (per-sheet
L_ring and k) against six targets (three masses, three α's).
Confirm a working e+p+ν configuration exists.  This is the first
all-three-sheets test of R60's architecture.

**Background.**

- **ν architectural coupling.**  Earlier tracks set `sign_nu = 0`
  (ν-tube uncoupled from ℵ), giving α_ν = 0 by construction.
  That was a simplification, not a physics statement — R55 had
  α_ν ≈ 0.92α via inherited geometry, and R61's neutrino
  taxonomy treats the ν-sheet as architecturally coupled
  with charge-zero arising from topology (Q_charge = −n_e_tube +
  n_p_tube = 0 for pure ν modes, regardless of the ν-tube↔ℵ
  coupling magnitude).  Track 6 turns the architecture on:
  `sign_nu = +1` (same convention as the electron, per R55).
- **(1, 1) immunity.**  Track 5 F22 showed (1, 1) modes never
  decouple — fortunate, because R61's top ν candidates all use
  (1, 1) for ν₁ and ν₂.  No per-mode pathology to dodge for the
  light eigenstates.
- **Wide k ranges expected.**  Sheet ring scales: L_p ~ fm,
  L_e ~ 10⁴ × L_p, L_ν ~ 10⁴ × L_e, L_ℵ possibly ~10⁻¹⁸ × L_p.
  In any normalization that respects this, the per-sheet
  diagonal scales (k) and the ℵ diagonal (g_aa) span many orders
  of magnitude.  R59 F59's `k = 1/(8π), g_aa = 1` was *one*
  self-consistent natural-form choice; other configurations
  involving very different k values are physically reasonable.
  Solver bounds should be wide.

**Strategy.**

Use Track 4's joint solver, extended to three sheets.  Hold the
α-architecture global knobs at R59 F59 natural-form values for
the first attempt, with `sign_nu = +1`.  Free knobs and targets:

| Free knob | Bound (loose) |
|-----------|---------------|
| L_ring_e | (10⁻³, 10⁹) fm |
| L_ring_p | (10⁻³, 10⁹) fm |
| L_ring_ν | (10⁻³, 10⁹) fm |
| k_e | (10⁻⁶, 10⁶) |
| k_p | (10⁻⁶, 10⁶) |
| k_ν | (10⁻⁶, 10⁶) |

| Target | Source |
|--------|--------|
| E(electron mode) = m_e | input |
| E(proton mode) = m_p | input |
| E(ν₁ mode) = m_ν₁ | derived from Δm²₂₁ |
| α_Coulomb(electron) = α | architecture |
| α_Coulomb(proton) = α | architecture |
| α_Coulomb(ν₁) = α | architecture (R55-consistent) |

Six knobs, six targets — square system.  ε and s for each sheet
are *inputs*, chosen from Track 5 baseline (e, p) and R61 (ν).

**Sheet inputs.**

| Sheet | (ε, s) | Mode | Source |
|-------|--------|------|--------|
| e | (1, 0) | (1, 2) | Track 5 baseline |
| p | (1, 0) | (1, 3) | Track 5 baseline |
| ν | (2, 0.022) | (1, 1) for ν₁ | R61 top candidate (`+1,+1)(-1,+1)(+1,+2)`) |

The ν candidate has s_ν · ε_ν = 0.044 — far from any decoupling
locus and well within any reasonable signature budget.  ν₂ at
(−1, 1) and ν₃ at (1, 2) inherit the same (ε_ν, s_ν).

**ν₁ mass target.**  Take m_ν₁ = 32.1 meV from R61 candidate 1
(calibrated to Δm²₂₁ = 7.53 × 10⁻⁵ eV²).  Δm²₃₁/Δm²₂₁ = 33.6
should follow automatically from (ε_ν=2, s_ν=0.022) — verify as
a passive check, don't target.

**Tactics.**

1. **Phase 1: natural-form g_aa.**  Solve at g_aa = 1, R59 F59
   defaults for σ_ta = √α, σ_at = 4πα.  Wide k bounds.
2. **Phase 1.5: rescan against other R61 ν candidates.**  If
   Phase 1 succeeds, also try R61 candidates 2, 3, 4 to see
   how robust the result is across ν geometry choices.
3. **Phase 2 (only if Phase 1 fails for all R61 candidates).**
   Free g_aa as a 7th knob, add a soft target (signature margin
   ≥ some value) or accept a slight Phase 1 residual to make
   the system square.  Document any g_aa deviation from 1 as a
   "natural-form cost."
4. **Cross-checks.**  At any successful configuration: confirm
   ν₂ and ν₃ masses come out at predicted values (no separate
   targeting needed — they share (ε_ν, s_ν)), and confirm
   Δm²₃₁/Δm²₂₁ ≈ 33.6.

**Smoke check before scan.**

Build the metric with Track 5 baseline + R61 #1 ν, R59 F59 α
knobs, sign_nu = +1.  Confirm signature OK, all three sheets
contribute to the inverse metric, no obvious numerical
breakage.  Report initial (uncalibrated) α_ν to see if it's in
the right ballpark.

**Deliverables.**

- `scripts/track6_three_sheet_solve.py` — joint solver, smoke
  + Phase 1 + Phase 1.5; Phase 2 wired but only invoked if
  Phase 1 fails.
- findings.md F27 (smoke + Phase 1 result), F28 (R61 candidate
  rescan), F29 (Phase 2 if needed), F30 (interpretation +
  candidate config for Track 7).

**Acceptance criteria.**

- Joint solver converges on at least one R61 ν candidate with
  all six targets met to ≤ 1% (mass) and 1% (α universality).
- Signature OK at the converged configuration.
- ν₂, ν₃ masses and the Δm² ratio cross-check correctly.
- A specific (L_e, k_e, L_p, k_p, L_ν, k_ν) configuration is
  identified as the working baseline for Track 7 (compound modes).

**Possible outcomes.**

- **Phase 1 succeeds.**  R60 has a clean three-sheet baseline
  at full natural-form values.  Architecture is fully validated;
  proceed to Track 7 with confidence.
- **Phase 1.5 differentiates ν candidates.**  Some R61
  candidates work, others don't.  Identifies the most viable ν
  geometry — feeds back into R61.
- **Phase 2 needed.**  We have to deviate from g_aa = 1 to make
  it work.  Documents the cost.  Still likely viable, but
  slightly less elegant.
- **Phase 2 also fails.**  ν-sheet inclusion at full α coupling
  is structurally blocked.  Reconsider sign_nu choice or revisit
  the ν architectural coupling assumption.

---

### Track 7 — Ring↔ℵ structural cancellation test

**Goal.**  Test the conjecture (post-Track 6 dialog) that adding
ring↔ℵ entries with the structural prescription
σ_ra = sε · σ_ta on each sheet cancels the shear-induced α
mode-dependence, restoring universality across all (n_t, n_r)
modes on a sheared sheet.

**Background.**  Track 6 found that on sheared sheets, different
modes get different α values via an indirect ring-to-t leak
(ring ↔ tube via shear, tube ↔ ℵ via σ_ta, ℵ ↔ t via σ_at).
Algebraic derivation suggests the ring↔ℵ entry σ_ra at value
sε · σ_ta exactly cancels the leak, leaving Q ∝ n_t (mode-
independent).  R59 ruled out ring-based ℵ mediation as a
*replacement* for tube coupling (F39, F43) but did NOT test
ring↔ℵ as a *supplement* with this specific structural relation.

**Strategy.**  Use the Track 6 F28 baseline (R61 #1 ν, e/p
shearless, k_e = k_p = 4.73 × 10⁻², k_ν = 4.53 × 10⁻²).
Compute σ_ra per sheet, build the augmented metric, compare α
extraction for ν₁/ν₂/ν₃ between base and augmented.

**Tactics.**

- σ_ra prescription: σ_ra_x = (s × ε)_x × sign_x × σ_ta
  - σ_ra_e = 0 (e shearless)
  - σ_ra_p = 0 (p shearless)
  - σ_ra_ν = 0.044 × √α ≈ 3.76 × 10⁻³ (the ν-sheet shear
    is what produces mode-dependence in the first place)
- Build augmented 11D metric with these new ring↔ℵ entries
- Verify signature still OK
- Compute α for electron, proton, ν₁, ν₂, ν₃; report base vs
  augmented values

**Acceptance criteria.**

- Augmented metric: signature OK preserved
- α_ν₁ / α_ν₂ / α_ν₃ all equal each other to ≤ 0.1%
  (Track 6 had spread 0.91× to 1.19× of α — i.e., 28%)
- α_e and α_p unchanged (their σ_ra = 0)

**Possible outcomes.**

- **Universality restored.**  Architectural fix works.
  Mode-dependence problem retired.  R60's program proceeds
  with the augmented architecture.
- **Universality partially restored.**  First-order cancellation
  works but residual cross-sheet effects remain.  Refine.
- **Universality not restored.**  Derivation had a wrinkle.
  Re-examine.

---

### Track 14 — Analytical derivation of k = 1.1803/(8π)

**Goal.**  Derive the single-k value that the joint solver
finds across all tested geometries.  Is k = 1.1803/(8π) a fixed
point determined by the solver's target set, or an artifact of
the initial guess?  If a fixed point, does it have a closed-form
expression?

**Strategy.**

Phase 1 — **Empirical.**  Rerun the joint solve with different
initial k values (k_init = 0.5/(8π), 1/(8π), 2/(8π), etc.).  If
solver always converges to the same k, it's a fixed point.  If
it depends on init, it's an artifact.

Phase 2 — **Symbolic (sympy).**  With σ_ra = (sε)·σ_ta active,
the α extraction Q = n_t · σ_ta at structural cancellation.  The
full formula α_Coulomb = Q²/(4π) · (−G⁻¹[t,t])² gives an implicit
equation in k at the targeted α_Coulomb = α.  Solve for k
symbolically.

Phase 3 — **Natural form match.**  Given the solved k value (a
numeric constant), search for a closed-form expression involving
α, π, and small integers.

**Acceptance.**

- Phase 1 establishes whether k is a true fixed point
- Phase 2 produces a closed-form or explicit formula for k
- Phase 3 either finds a clean natural-form expression or
  documents that it doesn't exist

---

### Track 13a — R60-native α-universal inventory on Track 12 baseline

**Goal.**  Ten of model-E's 18 compound tuples have α ≠ α on
Track 12's metric (α_sum ∈ {±2, ±3, ±4}).  For each, search for
an α-universal alternative (α_sum = ±1) within |n_i| ≤ 6 and
report mass accuracy.  Produces a clean "model-F canonical
inventory" ready for the model-F writeup.

**Strategy.**  α-filtered brute force per target, enforcing
α_sum² = 1 and correct Q and spin.  Report top-3 per target.

**Acceptance.**  Every non-pion compound gets an α-universal
tuple within reasonable accuracy (say ≤ 5%).  Pion remains a
known failure (out of scope).

---

### Track 13b — ν-candidate sweep

**Goal.**  Test R61 candidates #1–5 on Track 12 architecture.
For each: does the joint solve converge?  What inventory
accuracy does it give?  Nuclear scaling?  Any candidate
meaningfully better or worse for specific hadrons?

**Strategy.**  For each R61 candidate:
- Run Track 12-style joint solve with that (ε_ν, s_ν) and
  ν-triplet
- Compute inventory accuracy (summary numbers only)
- Rank candidates by composite

**Outcome.**  Either one candidate clearly wins (pick it for
model-F) or multiple are viable (model-F documents them all).

---

### Track 12 — Proton sheet alignment with model-E

**Goal.**  Replace Track 9's magic-shear p-sheet (ε_p = 0.4,
s_p = 3.0) with model-E's proton geometry (ε_p = 0.55,
s_p = 0.162) and re-run the joint solve + inventory audits.
Hypothesis: model-E's p-sheet values are better-tuned for the
hadron inventory and nuclear scaling; reverting to them should
tighten Tracks 10 and 11 accuracies toward model-E's numbers.

**Strategy.**

Phase 1 — joint re-solve with the model-E p-sheet.  Same six
free knobs (L, k per sheet), same six targets.  Check:
- Signature holds (s_p · ε_p = 0.089, well under any bound)
- α universality preserved
- Single-k symmetry preserved (solver should again find
  k_e = k_p = k_ν)

Phase 2 — inventory re-evaluation.  Plug model-E's compound
tuples into the new metric.  Many should now match their
model-E accuracy since the p-sheet is the same.

Phase 3 — nuclear re-audit.  d, ⁴He, ¹²C, ⁵⁶Fe on the new
metric.

**Expected outcomes.**

- **Clean alignment.**  Track 10 accuracy improves to near
  model-E levels for the tuples that failed before; nuclear
  scaling tightens to ≤ 1.1% like model-E.  R60 now matches
  model-E across the full inventory and nuclei, with α
  universality as a structural bonus.
- **Partial alignment.**  Some things improve, some don't.
  Track 12 identifies which hadron/nuclear fits are sensitive
  to p-sheet geometry specifically.
- **Regression.**  p-sheet change breaks something we previously
  had working (unlikely given the structural architecture holds,
  but possible).

---

### Track 11 — Nuclear scaling audit

**Goal.**  Test R29 / model-E's nuclear scaling law (n_5 = A,
n_6 = 3A, with n_et = A − Z for charge Z) on the Track 9 augmented
baseline.  Model-E matched d (0.05%), ⁴He (0.69%), ¹²C (0.76%),
⁵⁶Fe (1.05%) with this scaling.  Does R60 inherit the result?

**Strategy.**

For each nucleus (d, ⁴He, ¹²C, ⁵⁶Fe):
- Construct tuple (A − Z, 0, 0, 0, A, 3A)
- Compute predicted mass on Track 9 metric
- Compute α_Coulomb — for Z-charged nuclei, should naturally be
  Z² × α (since α_sum = −Z by construction)
- Compare to observed nuclear mass

Secondary: vary n_er and n_νr within small range (|n| ≤ 5) to
see if small decorations improve accuracy.

**Expected.**  If nuclear scaling works, this is another major
validation of R60's architecture.  Nuclear masses are independent
of particle-inventory fits (different quantum-number regime, very
different scale).  Success here means the single scaling law
covers ~60 stable nuclei from hydrogen to iron.

---

### Track 10 — Broader hadron inventory on Track 9 baseline

**Goal.**  Having reproduced muon, tau, neutron on the Track 9
extreme-e baseline (Track 9 F54, F55), test R60's coverage of
model-E's broader inventory: Λ, η′, Σ, Ξ, Ξ⁰, φ, ρ, K, η, π.
Two questions: (a) do model-E's tuples evaluate well on Track 9
metric? (b) when they don't, does α-filtered brute force find
an R60-native alternative close to observed?

**Strategy.**

Phase 1 — verbatim: plug each model-E tuple into the Track 9
metric, tabulate E_predicted vs observed and α_Coulomb vs α.
Group by whether tuple matches.

Phase 2 — α-filtered brute-force search for non-matching targets,
enforcing α_sum = (n_et − n_pt + n_νt) with |α_sum| = 1 for
unit charge and |α_sum| = 0 for Q = 0 (checking quantization
pattern on Q=0 hadrons).

Phase 3 — tabulate R60 vs model-E accuracy across the full
inventory.  Flag near-misses and apparent failures.

**Acceptance.**

- All model-E tuples evaluated on Track 9 baseline
- α_Coulomb reported per mode
- For each target, either the model-E tuple matches (within
  model-E's own accuracy ± small residual) or a Track 9 native
  tuple is found

**Possible outcomes.**

- **Most model-E tuples survive.**  R60's architecture plus
  extreme-e revival gives back model-E's spectrum cleanly.
  Major win.
- **Split result.**  Some survive, some need R60-native tuples.
  Document where and why (probably p-sheet geometry difference).
- **Few survive.**  Track 9's p-sheet magic shear is too
  different from model-E's; hadrons need a p-sheet re-tune.

---

### Track 8 — Compound mode search (μ, τ, neutron)

**Goal.**  With the Track 7d magic-shear baseline established
(all three sheets calibrated, α universal across sheets and
modes, ghost ordering on e and p), search for compound modes
— 6-tuples spanning multiple sheets — whose energies match
observed muon, tau, and neutron masses.  First pass: no
cross-sheet σ.  Second pass only if needed.

**Background.**

Model-E's inventory listed the compounds:

| Particle | Observed (MeV) | Model-E 6-tuple | Model-E accuracy |
|----------|---------------:|:----------------|:-----------------|
| muon (μ⁻) | 105.658 | (1, 1, −2, −2, 0, 0) | 0.83% |
| tau (τ⁻) | 1776.86 | (3, −6, 2, −2, 2, 3) | 0.05% |
| neutron (n) | 939.565 | (0, −4, −1, 2, 0, −3) | 0.07% |

Ordering: `(n_et, n_er, n_νt, n_νr, n_pt, n_pr)`.

Each mode satisfies MaSt constraints:
- **Charge:** `Q = −n_et + n_pt`  (=−1, −1, 0 above ✓)
- **Spin-½:** odd total tube-winding parity on at least one sheet
- **Reality:** metric eigenvalue must be positive (mode is physical)

Model-E used these specific 6-tuples with R19-era α (not the R59
F59 architecture we have now).  Whether they land at observed
masses on the Track 7d R60 metric is an open question — the metric
has changed (magic shear geometry, ring↔ℵ entries, single-k
symmetry, different L values).  Track 8 tests this empirically.

**Strategy.**

Three phases, gated on results:

**Phase 1 — direct check of model-E tuples.**  Take each
model-E compound 6-tuple verbatim; compute its mass on the Track
7d baseline.  If residuals < 5%, compound modes "survive the
transition" and we have a good story.  If > 5%, Phase 2.

**Phase 2 — search for alternative 6-tuples.**  For each target
(μ, τ, n), do a bounded brute-force search over 6-tuples `|n_i|
≤ N_max` satisfying the (Q, spin) constraints.  Report the
closest-mass candidates and document the best match.  Compare
to model-E: same mode, different, or no clean match?

**Phase 3 — α audit on compound modes.**  For each compound
mode that matches a target mass, compute α_Coulomb.  Track 7
only verified α universality for simple single-sheet modes;
compound modes span multiple sheets and might have
mode-dependent α.  Report.

If Phase 3 shows compound modes have α ≠ α universally, this
tells us whether pool item **h** (cross-sheet α cancellation
prescription) is needed or whether we accept mode-dependent α
on compounds as a feature.

**Tactics.**

- Enumerate 6-tuples with `|n_i| ≤ 10` (~2M candidates, tractable)
- Apply Q and spin filters before computing mass (fast reject)
- Compute `mode_energy` on the Track 7d metric for filtered
  candidates
- Rank by `|E_predicted − E_target| / E_target`
- Report top-10 per target particle
- Compute α_Coulomb for the top-1 match; flag if not at α

**Smoke cross-checks before scan.**

- Confirm model-E's tuples load correctly and give the expected
  charge/spin assignments on our code
- Confirm Track 7d's stable particles (e, p, ν₁, ν₂, ν₃) still
  give exact masses + α = α

**Deliverables.**

- `scripts/track8_compound_modes.py` — Phase 1 + Phase 2 search
  + Phase 3 α audit
- findings-8.md — results per target particle, best match summary
- Updated candidate baseline for Track 9 (if compound results
  indicate pool item h is needed)

**Acceptance criteria.**

- Phase 1 completes: three model-E compound tuples evaluated on
  Track 7d metric; residuals reported
- Phase 2 completes: alternative 6-tuple candidates found within
  5% of each target, or documented as not achievable at current
  metric
- Phase 3 completes: α status of each matched compound mode
  reported (universal at α, or mode-dependent with specific
  deviation)

**Possible outcomes.**

- **Best case.**  Model-E tuples land within 1% on Track 7d, α
  universal across compounds.  R60 architecture is validated end
  to end — the model-E spectrum transfers cleanly.  Promote to
  model-F candidate.
- **Mixed.**  Some compounds match, others need different
  6-tuples.  Catalog the differences; R60 inventory is slightly
  different from model-E but equally justified.
- **α mode-dependence on compounds.**  Compounds have α ≠ α.
  Pool item **h** becomes the natural next track.  Decide
  between "derive cancellation prescription" and "accept
  mode-dependent compound α" based on severity.
- **No compound matches close enough.**  Major issue — would
  indicate the Track 7d geometry is wrong, or that compound
  modes in MaSt need a richer mechanism (e.g. cross-sheet σ is
  not just a correction but is load-bearing).  Significant
  replanning.

---

### Track 7d — Magic-shear baseline re-solve (ghost ordering)

**Goal.**  Replace Track 7b's shearless (ε=1, s=0) baseline for
the e and p sheets with magic-shear geometries that make each
sheet's target mode the *lightest* charged mode on that sheet
— restoring ghost ordering as a built-in structural feature.
Verify that Track 7b's α universality survives the change.

**Background.**  At Track 7b's (ε=1, s=0) baseline, the mode
(1, 1) on each charged sheet is lighter than the target mode
((1, 2) electron, (1, 3) proton) — violating ghost ordering.
We deferred this to "other mechanisms" but it raises the
diagnostic complexity of Track 8.  "Magic shear" — setting
`s_x = n_r / n_t` for each sheet's target — makes the target
mode have ring energy `(n_r − s·n_t)² = 0` and thus minimal
μ = 1/ε, lighter than all other (1, *) modes on the same sheet.

**Sheet configuration.**

| Sheet | Target mode | Magic shear | Proposed (ε, s) | sε | Decoupling check |
|-------|:-----------:|:-----------:|:---------------:|:--:|:----------------:|
| e | (1, 2) | s_e = 2 | (0.4, 2.0) | 0.8 | off sε = 1 locus ✓ |
| p | (1, 3) | s_p = 3 | (0.4, 3.0) | 1.2 | off sε ∈ {0.382, 2.618} ✓ |
| ν | (1, 1) target | s_ν from R49 Δm² | (2.0, 0.022) | 0.044 | (1,1) never decouples ✓ |

Joint signature budget check: `Σ(sε)² = 0.64 + 1.44 + 0.002 =
2.08` < predicted 5/2 three-tube bound.

**Strategy.**

- Fix the (ε, s) values above.  Free knobs remain (L_e, k_e,
  L_p, k_p, L_ν, k_ν) as in Track 7b.
- Architecture: ring↔ℵ structural σ_ra entries active (Track 7
  prescription).
- Targets: same six (masses + α universality) as Track 7b.
- Verify after convergence:
  1. All targets met to floating-point precision
  2. Ghost ordering confirmed on each sheet (compute
     μ(1,1), μ(1,2), μ(1,3) per sheet at final values)
  3. α universality across modes preserved (α_ν₂, α_ν₃ = α)
  4. Signature OK (joint three-tube bound respected)

**Deliverables.**

- `scripts/track7d_magic_shear.py` — re-solve + verification +
  ghost-ordering audit on each sheet
- findings-7.md §F42–F44 entries
- Updated baseline numbers for Track 8

**Possible outcomes.**

- **All targets met + ghost ordering + universality preserved.**
  Magic-shear baseline works.  Track 8 has a cleaner starting
  configuration.
- **Signature violation.**  Budget too tight at these (ε, s)
  values.  Shrink ε further.
- **α universality breaks.**  Structural fix doesn't survive
  the geometry change.  Needs investigation (likely ν
  mode-symmetry interaction we didn't anticipate).
- **Ghost ordering fails.**  Unexpected — magic shear is
  algebraically guaranteed to make target mode lightest.
  Sanity check.

---

### Track 7c — Inter-sheet shear compatibility check (post-Track 7b)

**Goal.**  Quick sanity check: does activating Ma cross-sheet σ
entries (R54's σ₄₅ = −0.18 and σ₄₆ = +0.10, or analogs) break
Track 7b's clean α universality?

**Strategy.**  Take the Track 7b baseline metric (α universal to
floating point across all three sheets).  Add cross-sheet σ
entries at (a) small values (0.01), (b) R54's historical values
(±0.18, ±0.10), (c) several intermediate values.  At each
configuration, compute α_e, α_p, α_ν₁/₂/₃ and check signature.
Optionally re-solve (L, k) to absorb any shift.

**Acceptance.**  If α universality survives activation of
cross-sheet σ (within tolerance reachable by re-solve), we have
a usable free knob for compound-mode fine-tuning.  If it breaks,
we need to extend the structural prescription to cover the
cross-sheet case (a natural follow-up — likely σ_cross ↔ ℵ
entries by analogy with σ_ra).

---

### Track 7b — Re-solve on the augmented metric (magnitude lock)

**Goal.**  Track 7 demonstrated that adding σ_ra entries collapses
the ν-mode spread from 28% to 0% — but the converged value drifted
to 1.0885α (not exactly α) because we used Track 6's k values
unchanged on a metric that had changed.  Track 7b re-solves the
joint system on the augmented metric to bring the magnitude back
to α exactly while preserving the structural universality.

**Strategy.**  Same six free knobs as Track 6 (L_e, k_e, L_p, k_p,
L_ν, k_ν), same six targets (three masses + α_e = α_p = α_ν₁ = α),
but with the metric builder modified to include the structural
σ_ra entries.  The σ_ra values are *not* free knobs — they're
derived from σ_ra_x = (sε)_x · σ_ta on each sheet.

**Acceptance criteria.**

- Joint solve converges with all six targets met to ≤ 1e-6.
- α_ν₂ and α_ν₃ (untargeted) come out within 1e-6 of α — i.e.,
  Track 7's structural universality is preserved at the new
  k values.
- Δm²₃₁/Δm²₂₁ ≈ 33.6 cross-check still holds.
- Final k values are the "natural-form" baseline for the
  augmented architecture, ready for Track 8 (compound modes).

---

## Next-track pool

Candidates after Track 7b.  Sequence decided as we go.

**a.** (absorbed into Track 2)

**b. Smallest-shear neutrino solution.**  Same exercise for s_ν
from R49's Δm²₃₁/Δm²₂₁ = 33.6.  R26 Family A uses s_ν = 0.022
(already small, probably compatible), but confirm across
neutrino families and identify any constraints on ε_ν.

**c. Joint metric search.**  With s_e and s_ν bounds known from
Tracks a/b, run the Track 1 solver over (ε, s, σ_cross) to find
a single 11D metric satisfying all targets.  This is the "does
model-F exist?" computation.

**d. Re-derived particle inventory.**  Given a viable joint
solution, re-solve for mode tuples across the model-E 18/20
particle inventory on the new metric.  Check that neutron compound
still works (0.07%), hadron near-misses still near, and Q = −n₁ +
n₅ still integer-valued.

**e. Survival audit of model-E results.**  Systematically check
each model-E prediction on the R60 metric: charge formula, neutron
compound mode, nuclear scaling (n₅ = A, n₆ = 3A), three neutrino
eigenstates, shell structure (R56), energy routing (R57).  Any
prediction that survives at the same accuracy is carried into
model-F; any that degrades flags a conceptual cost.

**f. Analytical derivation of α match.**  Verify that α_Coulomb
= α at (k = 1/(8π), g_aa = 1, σ_at = 4πα, σ_ta = √α) is an exact
algebraic identity, not a numerical coincidence.  Derive the
inverse-metric expression in closed form and check the 60 ppm
residual is a floating-point artifact.  If true, α is *derived*.

**g. Fallback — alternative α architecture.**  If Track c shows
the tube↔ℵ↔t architecture cannot coexist with the model-E
spectrum, investigate an alternative α mechanism compatible with
the preserved spectrum (extended R19, moduli potential, GRID
lattice scale).  Only relevant if c fails.

**h. Cross-sheet α cancellation structural prescription.**
Extend the Track 7 ring↔ℵ σ_ra = (sε)·σ_ta cancellation to
cross-sheet σ entries.  Derive (analytically or numerically)
the counter-entry relationship that cancels cross-sheet
shear-induced α leakage on the joint metric.  Prerequisite
for compound-mode search using cross-sheet σ as free knobs.

**Counting argument (Track 7d dialog):** each cross-sheet edge
creates α leakage on *both* sheets it connects.  To cancel
leakage on all three sheets simultaneously requires **all three
edges of the triangle** (e↔p, e↔ν, p↔ν) active at specific
derived values — a "3-phase" / circular arrangement.  Linear
chains (only two edges) are structurally underdetermined.
Model-E used only the p↔ν edge; it sacrificed α universality to
get neutron placement right.  Under R59 F59's universality
requirement, partial triangles are incompatible; either full
triangle with prescription, or zero cross-sheet σ.

**i. Alternative ghost-suppression mechanisms** (raised
post-Track 7c).  If we don't use magic shear on every sheet,
we need other filters for the (1, 1) and (1, 2) ghosts.
Candidates: (a) R46-style waveguide cutoff at specific ε; (b)
R61-style Majorana-pair cancellation (requires ±n_tube
partners for existence); (c) "too heavy" energy-routing
argument (R56/R57 — spatial separation cheaper than Ma
stacking).  Document as fallback in case magic-shear geometry
becomes unworkable elsewhere.

**j. ν-sheet ghost audit.**  At R61 #1 (ε=2, s=0.022), mode
(1, 0) is lighter than (1, 1) by μ calculation.  Investigate
whether (1, 0) modes are filtered in R49/R61 taxonomy
(candidate: modes with n_ring=0 may be structurally excluded
or absorbed into dark-mode classification).  Required before
claiming ν₁ is the lightest on that sheet.

**z. Closeout.**  After the chosen pool items execute: if
viability holds, promote to model-F candidate with a migration
document from model-E.  If not, document the specific blocking
constraint so future work can target it directly.

---

## Files

| File | Purpose |
|------|---------|
| README.md | This framing document |
| scripts/ | Computation scripts (per track) |
| findings.md | Results (after computation) |
