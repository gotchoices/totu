# What Losinets offers MaSt — and how to explore it

**Purpose.** The flip side of `losinets_proposition.md`. That doc asked what MaSt can offer Losinets; this one asks what MaSt can **take from** Losinets's trilogy, and lays out a concrete exploration plan for each candidate.

**Audience.** Internal — MaSt/GRID developers. Not for external communication. Focus is tactical: which offers have the highest leverage for MaSt's own open problems, and how to pursue them.

**Status.** Draft. Builds on R60–R63, the α↔R derivation, `losinets_summary.md`, and `losinets_proposition.md`. No new studies required to read this document; all specific claims reference work already done.

---

## Executive summary

Losinets's three papers offer MaSt **seven concrete technical inputs** and **four methodological habits**. The technical offers break down by layer:

| Layer | Offer | Leverage for MaSt | Status |
|---|---|---|---|
| Substrate | K-V continuum as long-wavelength limit of GRID | Supplies a physical interpretation of the lattice; gives R = t_P as prediction | R-α done; pending a coarse-graining derivation |
| Substrate | Coulomb gauge from incompressibility | Simplifies gauge-fixing in some MaSt derivations | Drop-in, not yet used |
| Photon | Photon internal structure (ρ, r₀, (a, b)) | Challenges MaSt's primitive free-photon assumption | Experimental test exists (PINEM) |
| Photon | Jones formalism from ring geometry | Gives MaSt a pre-confinement polarisation picture | Underused; worth formalising |
| Compound | Two-zone Hill vortex (core + K-V mantle) | Physical interpretation of MaSt T⁶ eigenmodes + field response | R60/R61 done; extends to all compound modes |
| Compound | Magnetic moment formula μ = ρ₀·V·ω·(ω·r₀) | Candidate answer to the Q114 g-factor problem | Not yet attempted |
| Coupling | α = π·ρ₀·r₀²·ℏ/(m_vac²·c) | Candidate derivation of α via Ma-S coupling geometry | R-α done; pins (ρ₀, r₀, m_vac) not fixed |

The methodological offers are style transfer: explicit scope limitation, negative-result-as-diagnostic, experimental-proposal-as-core-deliverable, and pedagogical clarity as a design criterion. All four improve MaSt's self-presentation without requiring any technical change.

**Highest-leverage single item:** the two-zone compound-mode picture (Offer 5 below). It converts MaSt's T⁶ eigenmodes from "standing wave amplitudes" into "rotational cores with K-V elastic wakes," gives MaSt a physical picture of compound particles that matches Losinets's own language, and provides a systematic path to form-factor predictions for every compound mode. R61 shows the machinery works; extending it to hyperons and nuclei is a multi-study programme.

---

## 1. Technical offers

### Offer 1 — K-V continuum as coarse-graining of GRID

**What Losinets has.** An explicit incompressible K-V continuum (ρ₀, η₀, G) with wave speed c = √(G/ρ₀), relaxation time R = η₀/G, and full derivation of Maxwell's equations from its linearised dynamics. Charge is the circulation invariant Q = ρ₀·r₀·Γ. The framework is non-relativistic but otherwise complete.

**What MaSt gains by adopting it.**

- A **physical picture** of the substrate on which MaSt's standing waves live. GRID's discrete lattice is abstract; Losinets's K-V medium is mechanically concrete.
- A **cross-framework prediction**, R ≈ t_P (from `losinets/alpha-vs-R.md`). If GRID is the coarse-graining of Losinets's continuum, R is fixed. This is the cleanest substrate-layer test available.
- A **mass-density scale** ρ₀ and **viscosity** ν₀ that GRID does not currently expose. These are measurable in principle via superfluid-vortex analogues.

**How to explore.**

- **Derive the K-V continuum as the long-wavelength limit of GRID's discrete phase dynamics.** Start from axioms A1–A4, take the continuum limit with appropriate anti-aliasing from ζ = 1/4, identify the coefficients of the emergent elastic and viscous terms. This is a renormalisation-style calculation — 2–4 weeks of focused work.
- **Check the R = t_P prediction at least parametrically.** If ρ₀ and η₀ both follow from lattice parameters with only ℏ, c, L_P, and ζ as inputs, the algebra should close. If it doesn't close — if there's a free dimensionless factor — that is itself the answer: R and t_P differ by a computable factor.

**Related study to run.** `R64-grid-to-kv-continuum` (not yet created). Deliverable: a note deriving Losinets's K-V constitutive law from GRID's phase-on-lattice dynamics, with explicit identification of ρ₀, η₀, G in terms of lattice parameters.

### Offer 2 — Coulomb gauge from incompressibility

**What Losinets has.** ∇·A = 0 as an **identity**, not a gauge choice. It follows directly from A = R·u and incompressibility ∇·u = 0 (EfD §4.5). No gauge-fixing Lagrange multiplier, no Faddeev–Popov machinery.

**What MaSt gains.** In MaSt's derivations where gauge fixing appears (the 9×9 metric construction, the projection from T⁶ modes onto observed polarisation states), Losinets's derivation gives an alternative motivation that is physical rather than formal. This does not change any quantitative result, but it cleans up the story.

**How to explore.**

- Identify where MaSt currently invokes Coulomb gauge. Check whether any step can be restated as "Coulomb gauge holds identically because the Ma sheets are incompressible in their metric sense."
- If yes, rewrite the relevant derivations with the Losinets-style motivation as an aside.

**Related study.** Low-leverage; a documentation pass, not a study. Worth doing once the main physics results are stable.

### Offer 3 — Photon internal structure as a challenge to the MaSt free-photon primitive

**What Losinets has.** A **spin-1 vortex ring** with concrete ring radius ρ(ω) = √(ℏ/(m_vac·ω)), core radius r₀ ≈ λ̄, Poincaré-sphere orientation (a, b), and a falsifiable near-field E_z ∝ sin b detectable by PINEM.

**What MaSt gains — two scenarios depending on experiment.**

- **If PINEM finds no near-field E_z** (standard QED wins): MaSt's plane-wave free-photon primitive is safe. This is a defensive result.
- **If PINEM finds near-field E_z** (Losinets wins): MaSt's free-photon primitive is **incomplete**. The free photon is not a plane wave but has internal structure — and MaSt's confined photon is then confining something richer than it currently models. The mass-from-confined-photon argument becomes more mechanically concrete (MaSt confines a Losinets ring, not a Maxwell plane wave) but also requires MaSt to adopt ring kinematics.

**Why this is interesting for MaSt regardless of the experimental outcome.** MaSt's "photon" is a primitive; it is not derived from anything. Losinets provides a candidate mechanical content for that primitive. Even if the mechanical content turns out to be different from what Losinets proposes, the framing of *what a photon is in MaSt* can be sharpened by taking Losinets's proposal seriously.

**How to explore.**

- **Compute the MaSt prediction for near-field E_z on confined modes.** If MaSt's confined photons inherit structure from a Losinets ring, the (a, b) parameters project onto Ma winding under compactification. The computation is: for each MaSt particle mode, what is the implied near-field E_z signature? See tickets that this would correspond to — `R65-confined-mode-nearfield-Ez` or similar.
- **Re-derive MaSt's mass-from-confinement argument with a ring photon.** The white-paper argument uses v²(circulation) + v²(spatial) = c² for a plane-wave photon. With a ring photon, the argument picks up a geometric prefactor from ring orbital motion. Does the m = hf/c² relation survive? Is there a ring-specific correction at higher orders?

**Related study.** `R65-photon-primitive-ring-content` — recompute MaSt's free-photon content with Losinets's ring structure; check whether any MaSt results depend on the plane-wave assumption.

### Offer 4 — Jones formalism from ring geometry

**What Losinets has.** The transverse far-field of a vortex ring is **exactly** the Jones 2-vector of a classical photon — derived geometrically from the ring trajectory. The third Stokes parameter is S₃ = cos b. The mapping (a, b) → (Jx, Jy) is explicit and two-to-one.

**What MaSt gains.** MaSt's confined photon is confining an object whose pre-confinement polarisation is the Jones 2-vector. If the confinement is a wrapping on a compact dimension, the *polarisation* that survives is a specific geometric restriction on (a, b). This gives MaSt a cleaner statement of *what becomes spin* under confinement.

The R63 study already explored three candidate mechanisms (M1 half-wrap, M2 paired circulation, M3 embedding parity) for translating MaSt's odd-tube-winding rule into K-V language. Offer 4 is the other direction: use Losinets's Jones-from-ring to restate MaSt's polarisation content in pre-confinement terms.

**How to explore.**

- For each MaSt particle mode, identify the (a, b) values consistent with its tube-winding parity and ring-winding count. If this map is consistent across the particle inventory, Losinets has provided MaSt with a geometric definition of polarisation that MaSt currently lacks.
- Check whether the map is unique: a tube-winding parity of 1 with ring-winding n_ring could correspond to a specific sub-region of the Poincaré sphere, or to all of it.

**Related study.** `R66-polarisation-to-winding-map` — the non-speculative version of what the earlier trilogy-note §T3 section floated. R63's M2 failure tells us the naïve "(a, b) maps directly onto tube/ring winding" is wrong; a better map needs to account for the spin-1 vs spin-½ sector boundary.

### Offer 5 — Two-zone structure for compound modes

**What Losinets has.** A **physical picture** of compound particles as Hill vortices with two zones: a rotational inner core and an irrotational-but-circulating outer mantle. R61 showed that with MaSt supplying the core (~0.4 fm eigenmode amplitude) and Losinets supplying the mantle (K-V elastic wake, ~1.3 fm), the Hofstadter two-scale structure drops out within 3%.

**What MaSt gains.** A physical interpretation of every MaSt compound mode. Currently a MaSt particle mode is described by six integers (n₁, …, n₆) and an eigenfrequency. With Offer 5, each mode gets:

- a **core scale** from the eigenmode amplitude projection (R60-style calculation),
- a **mantle scale** from the K-V wake around that core (R61-style calculation),
- a **charge-density profile** from the sum of both,
- a **magnetic-moment structure** from the peripheral velocity of each zone (see Offer 6),
- **form-factor predictions** for electron-scattering experiments.

This is a substantial upgrade. Every near-miss in model-E's particle inventory currently has only a mass gap reported. With Offer 5, every near-miss gains a full form-factor prediction that can be compared to experimental data at Jefferson Lab and elsewhere.

**How to explore.**

- **Extend R60/R61 methodology to the neutron.** Confirm that the K-V wake picture reproduces the neutron's known charge-density profile (core-negative, mantle-positive, net zero). This is a direct test of the method on a particle where the structure is experimentally well-measured.
- **Extend to hyperons.** Losinets's hyperon paper flagged a failure ladder (Λ underdetermined, Σ inconsistent, Ξ impossible). Does MaSt's hyperon near-miss pattern correlate with this ladder when the eigenmodes are run through the core + K-V-wake machinery? This is R64's natural continuation: `R67-hyperon-two-zone-structure`.
- **Extend to nuclei.** MaSt's nuclear scaling (n₅ = A, n₆ = 3A) gives a compound mode for each nucleus. Running these through the core + mantle machinery gives predicted nuclear charge-density profiles that can be compared to electron-scattering data. `R68-nuclear-wake-profiles`.
- **Extend to mesons.** Losinets's baryon paper notes mesons (ρ, φ, K) as a future target. MaSt has eigenmodes for these; combining them with K-V wake thinking gives meson form factors.

**Leverage assessment.** This is the single highest-leverage offer. It converts one result (R61) into a programme spanning ~4 studies that produce quantitative form-factor predictions across the full MaSt particle inventory. Every one of those predictions is independently testable.

### Offer 6 — Magnetic-moment formula

**What Losinets has.** μ = ρ₀·V·ω·(ω·r₀) for a rotating zone of volume V with peripheral velocity ω·r₀, giving μ ∝ ρ₀·Γ²/r₀ per zone. For nucleons with two zones, the equal-charge condition gives |μ_c|/|μ_m| = r_m/r_c ≈ 5.2.

**What MaSt gains.** A candidate formula for computing magnetic moments from MaSt geometry. The MaSt Q114 g-factor problem (g_bare for the electron differs from the measured g ≈ 2 by a significant factor) is currently open. Losinets's formula, applied to a MaSt confined mode understood as a (core + mantle) Hill vortex, gives a specific prediction.

**Constraint.** For an elementary mode (single photon at Γ = h/m_vac), μ varies only with r₀ and ρ. For a compound mode with multiple windings, the combination rule (Σ Γᵢ² vs (Σ Γᵢ)²) matters and is not derived. R63 identified this as an open issue.

**How to explore.**

- **Compute μ for the MaSt electron mode** (single odd tube winding, single ring winding) using Losinets's formula with r_c from R60's projection and m_vac from R62 I-1 (21 GeV). Does the result match the observed electron magnetic moment μ_e = 1.001159·μ_B?
- **If yes**, the Q114 problem is solved in principle and the remaining work is deriving the composition rule for compound modes.
- **If no**, the discrepancy tells us either (a) m_vac is wrong (bears on R62), (b) r_c from the R60 projection is not the right object for Losinets's formula, or (c) a non-trivial correction from the compactification (spin-½ via M1 Hopf-linking) is needed.

**Related study.** `R69-magnetic-moment-from-vortex-formula` — apply Losinets's formula to MaSt modes, use Hofstadter-style projection for r_c and m_vac from R62. Pass/fail on the electron g-factor.

### Offer 7 — α from K-V parameters

**What Losinets has (after R-α derivation).** α = π·ρ₀·r₀²·ℏ/(m_vac²·c). This expresses α in terms of K-V substrate parameters. R and the Coulomb-vs-Lorenz gauge choice are irrelevant; m_vac and r₀ carry the weight.

**What MaSt gains.** A candidate **derivation of α** via Ma-S coupling. R55 (framed but not computed) asks what the Ma-S coupling entries in the 9×9 metric produce as α. Losinets's formula says: if Ma-S coupling determines an effective (ρ₀, r₀, m_vac) at the compactification scale, α follows.

**Constraint.** Three K-V parameters (ρ₀, r₀, m_vac) appear in the formula; MaSt would need to identify all three from Ma-S geometry. R62 showed MaSt's L-values don't pin m_vac uniformly. A cleaner approach may be needed.

**How to explore.**

- **Parametrise the formula in MaSt-native variables.** If Ma-S coupling entries σ_eS and σ_pS (with |σ_eS| = |σ_pS| ∝ α) correspond to specific K-V parameters, what are the correspondences?
- **Check the α^(−1/3) coincidence.** Losinets's empirical r_m/r_c = 5.2 matches α^(−1/3) = 5.156 within 1%. If this ratio emerges from a K-V wake calculation around an MaSt core with Ma-S coupling, we have a candidate mechanism for α in terms of geometric wake expansion. R61 flagged this; not yet run down.
- **Close R55.** The working assumption in model-E is that α follows from Ma-S coupling; the quantitative formula is pending. Losinets's formula is a candidate starting point.

**Related study.** `R70-alpha-from-ma-s-and-kv` — attempt to derive α from Ma-S entries using Losinets's formula, with the α^(−1/3) coincidence as a consistency check.

---

## 2. Methodological offers

### Habit 1 — Explicit scope limitation

**What Losinets does.** Every paper includes an explicit scope statement. EfD: "No ontological claim is made that electromagnetism is mechanical." Photon: "Does not refute QED… is falsifiable." Baryon: "Phenomenological… does not claim to be fundamental."

**What MaSt should borrow.** The MaSt white paper and model-E card lean toward stronger claims. This is partially warranted (MaSt makes many quantitative predictions that match experiment) but also exposes MaSt to over-interpretation. Adding Losinets-style scope statements — "this is a phenomenological model; the Standard Model's parameters are measured not explained, and so are ours from a different geometric input" — would improve the framing without weakening the content.

**How to adopt.** A documentation pass on the white paper. One paragraph per major claim clarifying what is derived from what. Low effort, high rhetorical benefit.

### Habit 2 — Negative result as diagnostic

**What Losinets does.** The baryon paper's hyperon section is a model. Losinets runs his equal-charge ansatz on Λ, Σ, Ξ and reports: Λ underdetermined, Σ inconsistent, Ξ impossible. Instead of hiding the failures, he reads them structurally: each unit of strangeness introduces a complication the minimal ansatz cannot absorb.

**What MaSt should borrow.** MaSt's near-miss pattern across the particle inventory is currently presented as "18 of 20 spin-correct modes." The gaps carry information that is not being extracted. Specifically:

- The Δ⁺ and Ω⁻ "forbidden" modes are interpreted as resonances, but their gap sizes carry dynamical content.
- The pion near-misses (22% for π⁰, 25% for π±) are the largest in the inventory. Losinets-style diagnostic reading: what does the gap size tell us about pion internal structure?
- Hyperon near-misses (Λ 0.00%, Σ⁻ 0.01%, Σ⁺ 0.02%, Ξ⁻ 0.03%, Ξ⁰ 0.19%) show a strangeness-dependent increase. Does this correlate with Losinets's Λ → Σ → Ξ ladder?

**How to adopt.** A study: `R71-maSt-gap-diagnostics` — read the near-miss gap pattern across the MaSt inventory using Losinets's failure-as-diagnostic framework. Test for strangeness, charge, and spin correlations.

### Habit 3 — Experimental proposals as first-class deliverables

**What Losinets does.** Every paper ends with a numbered list of experiments: specific setups, specific observables, specific expected signals, specific control experiments. The photon paper lists PINEM near-field E_z scanning and ion-trap angular-momentum measurement in experiment-design detail.

**What MaSt has.** Some: Σm_ν = 116–120 meV, 0νββ at |m_ββ| ~ 10–30 meV, Ma_ν ring at ~42 μm. But these are mentioned in passing rather than developed into experiment proposals.

**What MaSt should borrow.** Develop each prediction into a **full experimental proposal** with setup, expected signal, control, and quantitative discrimination from competing theories. The neutrino mass sum, the short-range gravity test at ~42 μm, and the L05 optical beat absorption are the three that need promoting to first-class deliverables.

**How to adopt.** One document per prediction: `experiments/mast-cosmological-neutrino-sum.md`, `experiments/mast-short-range-gravity-42um.md`, `experiments/mast-L05-optical-beat.md`. Each structured like Losinets's §3 of the photon paper.

### Habit 4 — Pedagogical value as design criterion

**What Losinets does.** The baryon paper explicitly notes educational applications. The two-zone Hill-vortex picture is constructed to be visualisable. This is not ornament — it is a deliberate design goal.

**What MaSt has.** The T⁶ × S³ × t manifold is not obviously visualisable. The 6-integer mode labels are abstract. The 9×9 metric is opaque. MaSt's white-paper §1 does include the "confined photon on a torus" metaphor, but it competes for attention with the later technical machinery.

**What MaSt should borrow.** A commitment to a visualisable picture as a first-class deliverable, separate from the technical derivations. The "matter from light" metaphor is promising; it could be developed more systematically, perhaps with explicit diagrams, maybe with the help of Offer 5 (compound modes as core + K-V mantle) which is easier to draw than a 6-torus standing wave.

**How to adopt.** Already partially in hand via the primers. Continue the primer series with an explicit "visualising MaSt particles" document that uses Losinets's core + mantle picture as the visual anchor.

---

## 3. How to prioritise

Given limited attention, which offers to pursue first?

**Priority 1 — Offer 5 (two-zone compound modes).** Highest leverage: produces quantitative form-factor predictions across the full MaSt inventory, each independently testable. R61 has already done the nucleon; the hyperon and nuclear extensions are natural follow-ons. Delivers publishable results every 2–3 studies.

**Priority 2 — Offer 6 (magnetic moment formula).** Directly addresses Q114, which has been open. One focused study (R69). Pass/fail on the electron g-factor gives a clear signal whether this is the right direction.

**Priority 3 — Offer 1 (K-V continuum as GRID coarse-graining).** High leverage at the substrate layer. The R = t_P prediction from `losinets/alpha-vs-R.md` is already in hand; the missing piece is a derivation showing the continuum limit actually produces a K-V response. If successful, the three-framework architecture gains a substantive lower-bound theorem: GRID at large scales **is** Losinets's K-V.

**Priority 4 — Offer 7 (α from K-V via Ma-S).** Closes R55 if it lands. Depends on having a way to identify ρ₀, r₀, m_vac from Ma-S parameters, which is itself open.

**Priority 5 — Offer 3 (photon internal structure).** Waiting on experimental input (PINEM). Meanwhile: run R65 to check whether MaSt's results depend on the plane-wave primitive.

**Priorities 6–7.** Offers 2 (Coulomb gauge) and 4 (Jones from ring) are lower-leverage cleanups. Worth doing but only after the above.

**Methodological items.** Habit 2 (gap diagnostics) can be done in parallel with any of the above; Habits 1, 3, 4 are documentation passes best bundled with the next white-paper revision.

---

## 4. What MaSt has to change to adopt these offers

None of these offers requires MaSt to abandon its existing results. The adoptions are additive:

- **Offer 5** adds a physical interpretation layer on top of the existing T⁶ mode spectrum. Particle masses stay the same; each mode gains a charge-density profile.
- **Offer 6** proposes a computation of magnetic moments using Losinets's formula with MaSt-derived inputs. If it fails for the electron, MaSt loses nothing. If it succeeds, MaSt gains a g-factor mechanism.
- **Offer 1** re-casts GRID as the microstructure of a K-V continuum. The GRID axioms are unchanged; only their interpretation is expanded.
- **Offer 7** sits on top of R55, which was already framed as pending.

The methodological offers (scope discipline, diagnostic gaps, experimental proposals, visualisability) are also additive and do not conflict with anything.

**One potential tension:** Losinets's K-V framework is explicitly non-relativistic. If MaSt adopts it as the substrate description, some work is needed to show the Lorentz covariance of MaSt's results is preserved at the relevant scale. This is an engineering problem, not a fundamental conflict.

---

## 5. Summary

Losinets offers MaSt a physical substrate, a compound-particle interpretation, a g-factor mechanism candidate, a route to α, and four methodological habits. The highest-leverage single adoption is the two-zone core + K-V-wake picture for compound particles, which R60/R61 have already shown works quantitatively for the nucleon and which extends naturally to hyperons, nuclei, and mesons.

The adoption plan, ordered:

1. Extend R60/R61 methodology across the MaSt compound-mode inventory (hyperons → nuclei → mesons).
2. Apply Losinets's magnetic-moment formula to MaSt's electron mode and test against the measured g-factor.
3. Derive the K-V continuum limit of GRID and check R ≈ t_P holds.
4. Close R55 using Losinets's α formula with MaSt Ma-S inputs.
5. Run the gap-diagnostic study (R71) to read MaSt's near-miss pattern structurally.
6. In parallel, adopt Losinets's methodological habits in the next MaSt documentation revision.

Each of items 1–4 is a single focused study (≈1–2 weeks of work each). Items 5–6 are lighter-weight. The full programme is ~2–4 months of sustained effort and produces roughly five new studies plus a documentation pass.

Expected result: a version of MaSt that has physical interpretations for every compound particle, magnetic-moment predictions to compare with experiment, a mechanically concrete substrate picture, and presentational discipline matching Losinets's own. Nothing in MaSt's current content needs to be withdrawn.

---

## 6. References

**Source materials:**

- `losinets/losinets_EfD.txt` — K-V substrate paper (Offers 1, 2, 7).
- `losinets/losinets_photon.txt` — Photon paper (Offers 3, 4).
- `losinets/losinets_baryon.txt` — Baryon paper (Offers 5, 6).

**Completed cross-framework work (the results this document builds on):**

- `studies/R60-losinets-projection/findings.md` — Hofstadter kinematic projection.
- `studies/R61-losinets-mantle-wake/findings.md` — K-V wake around eigenmode core.
- `studies/R62-losinets-mvac/findings.md` — m_vac universality.
- `studies/R63-losinets-spin-half/findings.md` — Spin-½ mechanism candidates.
- `losinets/alpha-vs-R.md` — α ↔ R derivation and R = t_P prediction.

**Companion documents:**

- `losinets/losinets_summary.md` — analytical consolidation of all findings.
- `losinets/losinets_proposition.md` — what MaSt can offer Losinets (the other direction).
- `losinets/losinets-trilogy.md` — earlier layer map and punch list.

**MaSt anchors:**

- `papers/white-paper.md` — the standing-wave particle-spectrum model.
- `models/model-E.md` — active model card.
- `qa/Q114` — g-factor problem (Offer 6 addresses this).
- `studies/R55-ma-s-coupling` — α from Ma-S (Offer 7 addresses this).
