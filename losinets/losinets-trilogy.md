# Losinets trilogy — notes and connection to MaSt/GRID

Three 2026 papers by Dmitry Losinets form a coherent programme: a continuum-mechanical substrate (Kelvin–Voigt medium), a free-photon model as a vortex ring in that substrate, and a compound-particle (baryon) model built from the same vortex primitives. Read together they map onto MaSt and GRID at three different layers of the same architecture — but the fit is not clean, and several apparent correspondences are speculative rather than derived.

Source PDFs (kept in `reference/`):

- `losinets_EfD.pdf` — *Maxwell's Equations from Vortex Mechanics: A Kelvin–Voigt Analogy.* Substrate.
- `losinets_photon.pdf` — *Vortex Photon Model: Program for Experimental Verification.* Free photon.
- `losinets_baryon.pdf` — *Baryon Magnetic Moments in a Two-Zone Kelvin–Voigt Vortex Model.* Composite particles.

---

## Background: what each paper actually proves

### EfD — Maxwell from vortex mechanics

Losinets establishes a **formal mathematical isomorphism** (not an ontological claim) between Maxwell's equations and the linearised dynamics of a specific mechanical medium: a dilute assembly of compact Hill-type vortex rings in an **incompressible Kelvin–Voigt viscoelastic fluid**. The K–V constitutive law

> σ = 2G E(d) + 2η₀ D(u)

combines an elastic response (shear modulus G) with Newtonian viscosity (η₀). G arises from two contributions of comparable magnitude — Hill-vortex shape stability plus the collective Tkachenko back-reaction — giving the scaling

> G ≈ 0.234 Γ²/r₀²

where Γ is the circulation of a single ring and r₀ its core radius. Wave speed and relaxation time follow:

> c = √(G/ρ₀),    R ≡ τ_KV = η₀/G = ν₀/c²

Key derivations (exact, not assumed):

- **Damped shear-wave equation** for A = R·u, with u the solenoidal velocity field.
- **Coulomb gauge** ∇·A = 0 from incompressibility alone.
- **All four Maxwell equations** follow; in the far field (δ → 0) the viscous "current" vanishes and the exact source-free vacuum equations are recovered.
- **Electric charge** is the mass-normalised circulation invariant

  > Q = ρ₀·r₀·Γ

  conserved by Kelvin's theorem. R converts K–V units to SI.

**Free parameters / open items:**

- Circulation quantisation Γ = n·h/m_vac is **imported** from the Onsager–Feynman superfluid analogue. The effective medium particle mass **m_vac** (units: kg, **not** a density) is not derived.
- The shape-mode prefactor G_shape = 27Γ²/(175 r₀²) is a pressure-jump lower bound.
- The framework is non-relativistic and non-quantum; no attempt at Lorentz covariance.
- Explicitly: "no ontological claim is made that electromagnetism is mechanical."

### Photon — the free photon as a vortex ring

A free photon is modelled as a **propagating compact vortex ring** in the K–V medium, with:

- ring (major) radius ρ,
- core radius r₀,
- circulation Γ,
- orientation angles (a, b) on the Poincaré sphere (a = azimuth, b = tilt).

From the superfluid quantisation Γ = n·h/m_vac and the circulation integral Γ = 2π·ρ²·ω, setting n = 1 gives

> ω(ρ) = ℏ/(m_vac · ρ²),    i.e.    ρ(ω) = √(ℏ / (m_vac·ω))

Higher-frequency photons correspond to smaller vortex rings (ρ ∝ ω^(−½)). Multi-quantum modes at fixed ring geometry give E_n = n·ℏω, reproducing Planck–Einstein.

The transverse Jones formalism emerges exactly from the ring trajectory (a, b → Jones vector). The third Stokes parameter is S₃ = cos b.

**Falsifiable prediction.** For a tilted ring (b ≠ 0) the z-component of the fluid-element trajectory is non-zero,

> r_z = ρ·sin(b)·sin(ωt + φ)

producing a **near-field longitudinal E_z component** confined to |r − r_vortex| ≲ r₀ with |g|² ∝ sin²(b). Circular polarisation (b = 0): no near-field E_z. Linear (b = π/2): maximal near-field E_z. Standard QED predicts zero near-field E_z for a free photon in vacuum; PINEM can resolve this at sub-wavelength impact parameter (target r₀ ≈ λ̄ = λ/(2π); 80–250 nm for visible light).

**Free parameters / open items:**

- m_vac is explicitly flagged: "A complete quantitative check — computing the K–V elastic energy of the ring and verifying E_ring = ℏω — would fix m_vac in terms of c, G, and ν₀, and remains an open problem." (§2.4.)
- r₀ is pinned only by order-of-magnitude argument λ̄ ≲ r₀ ≲ λ/2.
- The model is spin-1 throughout — there is no mechanism in the paper that produces a spin-½ object from a free photon ring.

### Baryon — two-zone nucleon

Each nucleon is a **single** Hill-type vortex with two hydrodynamically distinct zones:

- inner **core** (rotational, vorticity ≠ 0), radius r_c ≈ 0.25 fm,
- outer **mantle** (irrotational but carrying circulation and K–V elastic energy), outer radius r_m ≈ 1.3 fm.

Both zone radii are taken from Hofstadter-era electron-scattering data (1960s; precision ≈ 20–25%).

The K–V charge formula Q = ρ₀·r₀·Γ and the magnetic moment of a rotating zone

> μ = ρ₀·V·ω·(ω·r₀)   (V = core volume)

with

> ω = Γ/(2π·r₀²)

give μ ∝ ρ₀·Γ²/r₀ per zone. The **equal-charge condition** (proton: Q_c + Q_m = +e; neutron: −Q_c + Q_m = 0) forces |Q_c| = |Q_m| = e/2, i.e. r_c·ω_c = r_m·ω_m. Then

> **|μ_c| / |μ_m| = r_m / r_c ≈ 5.2**

— a parameter-free relation between the magnetic-moment ratio and the geometric size ratio. Using the measured μ_p = +2.79 μ_N and μ_n = −1.91 μ_N with the additive rules μ_p = μ_c + μ_m and μ_n = −μ_c + μ_m gives μ_c = 2.35 μ_N, μ_m = 0.44 μ_N, so μ_c/μ_m = 5.34 — consistent with r_m/r_c = 5.2 ± 1.2. The proton→neutron transition is a reversal of the core-zone circulation only.

**Hyperon extensions fail in a structured pattern:**

| Baryon | S | Outcome | Diagnostic |
|---|---|---|---|
| p, n | 0 | exact | two zones, r_m/r_c ≈ 5.2 |
| Λ | −1 | underdetermined | predicts μ_c/μ_m = r_m/r_c (eq. 14) |
| Σ± | −1 | quantitatively inconsistent | Δ = μ_Σ+ + μ_Σ− = +1.30 μ_N ≠ 0 |
| Ξ | −2 | no physical solution | likely 3-zone or linked loops |

Losinets reads the failure ladder as diagnostic: each unit of strangeness introduces a structural complication the minimal two-zone equal-charge ansatz cannot absorb.

**Free parameters / open items:**

- Half-integer spin is not derived. The Onsager–Feynman quantisation of Γ discretises charge; the corresponding quantisation of angular momentum L = ρ₀·Γ·r₀² in units of ℏ/2 is flagged as an open problem.
- Stability of the two-zone profile against redistribution of circulation between core and mantle is not analysed.
- r_c and r_m are empirical inputs, not predictions.

---

## Layer map (corrected)

| Layer | GRID | Losinets | MaSt |
|---|---|---|---|
| **Substrate** | Discrete 4D causal Planck lattice with U(1) phase; axioms give Maxwell, G, charge quantisation; α as input | Continuum incompressible K–V vacuum (ρ₀, η₀, G); vortex-ring medium gives Maxwell exactly | Assumed smooth 5-manifold M⁴ × M_a; Maxwell + α taken as inputs |
| **Free photon** | Propagating link-state disturbance (gauge field) | Vortex ring with finite ρ(ω), core r₀, continuous polarisation (a, b) | Plane-wave excitation of the ambient EM field (no intrinsic size) |
| **Confined photon** | — | — (not addressed) | Photon wrapped on M_a as a T⁶ standing wave; mass = eigenfrequency |
| **Compound particles** | — | Irrotational mantle at ~1.3 fm as K-V elastic wake of the charged core (hypothesis, R61) | Rotational core from T⁶ eigenmode amplitude at ~0.4 fm (R60 result; complementary to Losinets mantle, not equivalent to his two-zone picture) |
| **Charge mechanism** | Topological phase winding on the lattice; e = √(4πα) | Circulation invariant Q = ρ₀·r₀·Γ (K–V units); SI via R | Tube-winding integer, Q = −n₁ + n₅ from Ma–S coupling sign |
| **Single dial** | α (dimensionless) | R = τ_KV = η₀/G = ν₀/c² (time) | α (dimensionless, inherited from GRID) |

(The three single dials sit on **orthogonal axes** of the joint K–V parameter space — α is fixed by (ρ₀, r₀, m_vac), R is the viscoelastic relaxation time, and they do not reduce to each other unless Losinets's photon §2.4 ring-energy closure is solved. See C4 below and [`losinets/alpha-vs-R.md`](../losinets/alpha-vs-R.md).)

The three frameworks are **not** competitors but cover different slices of a single architecture. They agree strongly on concepts (charge from winding, photon as ring-like, Coulomb gauge as a consequence not an assumption), and disagree or fail to connect on substrate microstructure, free-photon internal structure, and spin sector. Both the agreements and the disagreements are structural, not cosmetic.

---

## Genuine three-way meshing

**1. Charge as a winding invariant.** GRID derives it from U(1) phase periodicity; Losinets from Kelvin's circulation theorem; MaSt from tube-winding integers. Three independent routes to the same statement — charge is topological, not a material property of a point particle.

**2. Coulomb gauge without assumption.** GRID gets it from local gauge invariance (A4). Losinets gets it from incompressibility (∇·u = 0 ⇒ ∇·A = 0 when A = Ru). MaSt simply inherits Maxwell. The mechanical version (Losinets) is the most transparent; the gauge-theoretic version (GRID) is the deepest.

**3. Mass = confined-photon frequency.** MaSt's white-paper argument *m = hf/c² for the confined-photon circulation frequency* is stated verbally. Losinets's eq. 15, E_n = n·ℏω from Γ_n = n·h/m_vac, **derives** the same relation from a specific mechanical model — modulo the interpretation of what "n" and "ω" are. MaSt's mass formula is the statement that a confined photon's energy is its eigenfrequency; Losinets's E_n = n·ℏω is the statement that a ring of fixed ρ supports a ladder of circulation quanta. These are related but not identical statements, and conflating them obscures the difference.

**4. One dial per framework, on orthogonal axes.** Each framework has exactly one free electromagnetic input: α (GRID, MaSt) or R = τ_KV (Losinets). R has units of time and is measurable in principle from the fluid properties; α is dimensionless. The hopeful "α = f(R · m_P·c²/ℏ)" form does not survive the algebra: substituting Losinets's K–V identifications into α = e²/(4πε₀ℏc) yields **α = π·ρ₀·r₀²·ℏ / (m_vac²·c)** and **R drops out**. The two dials are logically independent inputs to the K–V parameter space, not two names for the same number. A conditional bridge exists only if Losinets's photon §2.4 open problem (m_vac from the ring-energy closure) is solved. Full derivation, dimensional audits, and a corrected Planck-scale estimate R ≈ t_P (the trilogy's earlier μ₀/G_shear guess was a unit error) live in [`losinets/alpha-vs-R.md`](../losinets/alpha-vs-R.md). See also C4 below.

---

## Real tensions (not soluble by hand-waving)

**T1. Discrete lattice vs. continuous medium.** GRID is manifestly discrete (Planck-scale cells). Losinets is manifestly continuous and incompressible. They can only both be right if the K–V description is the long-wavelength effective theory of the discrete lattice. Concretely this would mean:

- ρ₀ (K–V mass density) ↔ some coarse-grained lattice inertia,
- ν₀ (viscosity) ↔ lattice UV dissipation as modes approach the Nyquist cutoff,
- c_KV = √(G/ρ₀) **must equal** GRID's propagation speed from axiom A1,
- the K–V shear modulus G ≈ Γ²/r₀² should emerge from lattice stiffness.

None of these identifications is derived. Until they are, the layer-map picture is a programme, not a result.

**T2. Free photon as ring vs. plane wave.** Losinets's free photon has finite internal structure: ring radius ρ ∝ ω^(−½), core r₀ ≈ λ̄, non-zero near-field E_z for tilted polarisation. A plane wave in MaSt/Maxwell has none of these. The two descriptions cannot both be correct unless one is a limit of the other — and if the ring picture is fundamental, then **MaSt is using an incomplete photon** wherever it treats the free photon as a primitive.

This matters practically: the PINEM near-field test isn't just a probe of Losinets's model, it's a test of whether MaSt's primitive photon is the full story. A positive result refutes plane-wave QED; a negative result refutes Losinets at the stated scale; either outcome constrains MaSt.

**T3. Spin sector.** Losinets's free photon is manifestly spin-1: the Jones 2-vector, Poincaré sphere parameterisation (a, b), and circular/linear polarisation are all statements about a spin-1 particle. MaSt's spin-½ emerges from **odd tube-winding parity** in a **confined** mode. A free photon cannot spontaneously become spin-½ under wrapping — the angular momentum content is fixed by the underlying field's representation of the Lorentz group, not by geometry. Any mapping between Losinets (a, b) angles and MaSt tube-winding parity is crossing a spin-sector boundary and needs a mechanism, not just a diagram.

**Status (R63, 2026-04): none of three candidate mechanisms closes Losinets's §2.2 open problem cleanly.** See [`studies/R63-losinets-spin-half/findings.md`](../studies/R63-losinets-spin-half/findings.md). Verdict one-liner: **M1 (half-wrap/double cover) survives the compound-mode inventory for all 5 rows; M2 (paired-circulation projection — the earlier conjecture in this section) fails at the π± row; M3 (embedding-parity label) matches by relabelling but does not derive ℏ/2 for L.**

Phase A also uncovered a structural problem the original open-problem statement did not flag: under Losinets's own EfD closures (G = 0.234 Γ²/r₀², ρ₀ = G/c²), the formula L = ρ₀ Γ r₀² reduces algebraically to L = 0.234 Γ³/c² — r₀ drops out — and has units of linear momentum (kg·m/s), not angular momentum. Under every natural length-scale completion, L·ℓ lands 10¹⁷–10²² below ℏ. The gap is structural, not a factor of 2; any closure must first build an object whose circulation quantum is of order h/m_vac *per single traversal* carrying an extra length factor. The §2.2 quantisation problem and the §2.4 ring-energy problem (C2 / R62) are linked — closing one without the other does not close the spin story.

**Candidate M1 (the surviving direction)**, phrased in K-V variables for continuity with Losinets's baryon-paper §2.2: *Consider a Hill-type ring Hopf-linked to a reference ring with odd linking number. The phase accumulated along the primary ring per full circuit does not return to its initial value; closure of the joint state requires two circuits of the primary. The Onsager-Feynman quantum per single circuit is then Γ₁ = h/(2 m_vac) rather than h/m_vac, and the primary's angular momentum contribution per traversal is halved. This is the K-V realisation of the "double cover" that the standard half-integer-spin arithmetic invokes.* The K-V elastic-and-kinetic derivation of the halved phase for a linked ring pair is not in the trilogy and would need to be done; without it, T3 remains open and the conjecture is a programme, not a result.

**T4. Nucleon in 3D vs. T⁶.** Losinets's nucleon is a **spatially** extended vortex with two 3D zones (r_c = 0.25 fm, r_m = 1.3 fm). MaSt's proton is a 6D standing wave (0, 0, −2, 2, 1, 3) whose amplitude is defined on the compact torus, not on 3D space. To compare them quantitatively one must **project** the T⁶ mode onto a 3D radial charge density. This projection has not been done. Without it, coincidences of length scale (see below) are suggestive but not verified.

---

## Cross-check targets (the punch list)

### C1. Hofstadter two-scale structure — kinematic projection (resolved by R60)

R60 projected the proton mode (0, 0, −2, 2, 1, 3) onto 3D radial charge density under twelve (density × projection) combinations. Result: best ratio 1.77, all physically plausible variants clustered in [1.3, 1.8]; inner scale bottoms at 0.39 fm, never reaches 0.25 fm. The kinematic equivalence **fails**. Root cause: only two physical scales enter the Hofstadter window — L₅ = 2.45 fm and L₆ = 4.45 fm — and no integer-winding geometric operation on them bridges the factor-of-3 gap from 1.82 to 5.2.

See `studies/R60-losinets-projection/findings.md`.

### C1′. Dynamical mantle as K-V elastic wake (R61, partial pass)

R60's Interpretation 2 — tested quantitatively in R61. The Hill-vortex exterior stream function in the lab frame (fluid at rest at infinity) is ψ = A sin²θ/r with A = Ur₀³/2, giving axisymmetric dipole velocities u ∝ 1/r³ and kinetic-energy density |u|² ∝ 1/r⁶ (not 1/r⁴ as an initial estimate assumed — that is the 2-D dipole scaling). Inverting w(r_mantle)/w(r_core) = η gives r_mantle = r_core · η^(−1/6).

Result: for r_core = 0.40 fm (the R60/MaSt inner-scale peak) and η = 10⁻³ (a −30 dB "end-of-near-field" threshold), r_mantle = 1.26 fm — within 3% of Losinets's Hofstadter-based mantle radius 1.30 fm. The match is real but conditional on a threshold choice the K-V framework does not fix. A striking *unrelated* numerical coincidence also falls out: α^(−1/3) ≈ 5.156 matches Losinets's empirical r_m/r_c ≈ 5.2 within 1%, and 0.25 fm × α^(−1/3) = 1.289 fm matches 1.30 fm within 1% — flagged for follow-up because it would require α (absent from Losinets's framework) to set a geometric ratio.

**Net verdict**: partial pass. The three frameworks are *consistent* with each other at the compound-particle layer — MaSt supplies r_core ≈ 0.4 fm, Losinets's K-V exterior supplies the 1/r⁶ decay, and a physically defensible threshold η = 10⁻³ lands at 1.26 fm. Proton/neutron mantle equivalence is automatic (|u|² ∝ A² is invariant under A → −A). But 1.3 fm is not *derived* from Losinets's equations alone without input — either r_core, η, m_π, or α.

Deliverable framing for Losinets: "MaSt supplies r_core ≈ 0.4 fm from the T⁶ proton eigenmode; your Hill-vortex exterior decays to 10⁻³ of its surface |u|² at r ≈ 1.26 fm — within 3% of the Hofstadter mantle."

See `studies/R61-losinets-mantle-wake/findings.md`.

**Status (R60, 2026-04):** tested — **fails at the kinematic level**. All twelve (density × projection) combinations produce two scales, but the ratios cluster in [1.3, 1.8] near the raw p-sheet ratio L₆/L₅ ≈ 1.82, never reaching 4.0. Only Fourier-form-factor projections deliver an outer scale near 1.3 fm (matching r_m), but the partnering inner scale sits at ~0.95 fm rather than ~0.25 fm, so the ratio is wrong. The result points to the Hofstadter mantle being dynamical (self-field / K–V elastic wake) rather than part of the T⁶ eigenmode amplitude, and constrains R55: a purely local Ma-S rescaling of the p-sheet cannot generate the 5.2 ratio; a second physical-space scale must enter. Full report: [R60 findings](../studies/R60-losinets-projection/findings.md).

### C2. m_vac from MaSt geometry (tested by R62 — does not stabilise)

Tested in [`studies/R62-losinets-mvac/findings.md`](../studies/R62-losinets-mvac/findings.md) across four
(ρ, ω) identifications drawn from MaSt L-values and particle Compton
frequencies with ρ = L/(2π), n = 1. Verdict: **no identification yields
an order-of-magnitude stable m_vac across particles**. The e-sheet-ring
× electron baseline reproduces 21 GeV/c² (I-1), but the p-sheet-ring ×
proton identification (I-3) gives 83 MeV/c² — 257× lighter — and the
ν-sheet-ring × ν₃ identification (I-4) gives 15 meV/c², twelve orders
below baseline and incoherent (lighter than the particle it would
support). The I-1/I-3 disagreement is **geometry-driven**: MaSt
L-values are eigenmode scales, not free-photon ring scales, so
(L₆/L₂)² · (m_p/m_e) = 257× rather than 1 as universality would
require. The 21 GeV number is a per-particle identification, not a
prediction. Exploratory closure through the classical thin-core
kinetic energy (R62 I-5) does not cancel m_vac but introduces r₀ as a
second free parameter — consistent with Losinets's §2.4 statement that
a proper K-V *elastic* energy derivation remains open.

### C3. Near-field E_z structure for confined modes

Losinets predicts free-photon near-field E_z ∝ sin(b)·exp(−|r|/r₀). A MaSt confined mode is a superposition of such photons on the compact geometry. Naively:

- **Neutrino modes** (pure ν-sheet, no Ma–S coupling, Q = 0): no net near-field E_z. Consistent with observed electric neutrality.
- **Scalar charged modes** (pions, with both e- and ν-tube windings to achieve spin 0 + Q ≠ 0): potentially maximal near-field E_z.
- **Proton (compound mode across three sheets)**: complex near-field with structure tied to form-factor behaviour at large Q².

These predictions are **analogies, not derivations**. Whether a MaSt confined mode actually inherits the Losinets (a, b) → E_z structure depends on how the compactification projects polarisation onto winding — which, per T3, is not a trivial map. Listing these as "predictions" without derivation would be overselling. Listing them as motivated targets for a projection calculation is fair.

### C4. α from R — derived; α and R are orthogonal in K–V space

**Status (2026-04): worked.** Full derivation in [`losinets/alpha-vs-R.md`](../losinets/alpha-vs-R.md).

The candidate bridge originally written here — α = R · (some Planck-scale frequency) — does not exist within Losinets's own correspondence table. Substituting the EfD §7.4 identifications **e ↔ Q = ρ₀·r₀·Γ**, **ε₀ ↔ ρ₀**, and the Onsager–Feynman quantisation **Γ = h/m_vac** into the SI definition α = e²/(4πε₀ℏc) gives the unconditional result

> **α = π·ρ₀·r₀²·ℏ / (m_vac²·c)**

— in which R does not appear at all. R = η₀/G is the viscoelastic relaxation time and the SI-unit conversion that makes A = R·u carry units V·s·m⁻¹; it sets dissipation and the source term in the in-medium Maxwell equations (EfD §4.6) but cancels from the dimensionless coupling ratio. **α and R live on orthogonal axes of the K–V parameter space.** A Planck-scale plug into the boxed formula gives α ~ O(1), confirming dimensional self-consistency but also showing that pinning α to 1/137 still requires choosing two of (ρ₀, r₀, m_vac) from outside Losinets's framework.

**Conditional escape.** Losinets photon §2.4 flags a complete K–V elastic-energy calculation of the ring (E_ring = ℏω) as an open problem. *If* solved, it would fix m_vac as a function of (ρ₀, c, ν₀); dimensional analysis then forces m_vac = κ·ρ₀·c³·R³ for some dimensionless κ, and α ∝ r₀² / (ρ₀·c⁷·R⁶). This is a parametric two-knob relation, not the clean one-knob bridge originally hoped for, and it is contingent on the §2.4 closure.

**The trilogy's "≈ 1.5 × 10⁻¹²⁶ s" guess was a unit error, not a result.** The naive substitution μ₀/G_shear has units of m²/A², not seconds — the K–V identification "μ₀ ↔ 1/G" lives entirely within the *mechanical-units* column of EfD Table 1 and does not survive an SI cross-substitution. The dimensionally correct Planck-scale estimate (G_shear = c⁴/(8πG_N), ρ₀ = G_shear/c², η₀ ≈ ρ₀·c·L_P) yields **R ≈ t_P ≈ 5.4 × 10⁻⁴⁴ s** — a falsifiable GRID prediction for the K–V relaxation time, 80 orders of magnitude away from the spurious earlier number.

**Consequence for the layer map.** Both frameworks remain "one-dial-per-framework", but the dials are not two names for the same number. The "single dial" row of the layer-map table now reads "one dial per framework, on independent axes" rather than "the same dial in different units". The substrate-equivalence picture (T1) is not refuted; it just does not collapse the parameter count.

### C5. g-factor and composite-mode magnetic moments

From Losinets's baryon eq. 9, μ ∝ ρ₀·Γ²·r₀. For an elementary ring Γ is fixed at h/m_vac, so μ-variation between particles comes from r₀ and ρ, not Γ. For composite particles with multiple windings, the combination rule (Σ Γᵢ)² versus Σ Γᵢ² is a derivation to do, not assume. The MaSt Q114 g-factor problem should be revisited with this constraint; the Losinets derivation narrows the space of legitimate g-factor formulas.

### C6. Hyperon failure pattern

Losinets's three-way ladder (Λ underdetermined, Σ inconsistent, Ξ impossible) is a diagnostic of strangeness-induced structural complication. MaSt's hyperon near-misses (Λ 0.00%, Σ⁻ 0.01%, Σ⁺ 0.02%, Ξ⁻ 0.03%, Ξ⁰ 0.19%) do not show an obviously matching ladder. Do the Losinets inconsistency metrics (sum rule deviation, 3-zone vs 2-zone required) correlate with MaSt's cross-sheet shear requirements? A correlation here would be a non-trivial cross-check; its absence would be informative too.

---

## What this note is not

It is not a proof that the three frameworks describe the same physics. It is a map of where they agree, where they disagree, and where the most productive cross-derivations sit. In particular:

- The polarisation-to-winding correspondence proposed in earlier versions of this note was overstated; per T3 it crosses a spin-sector boundary and requires a mechanism, not a table.
- The m_vac back-of-envelope is a sanity check, not a derivation; the earlier ~200 GeV number was arithmetically wrong, and the corrected ~21 GeV number is still an identification-dependent estimate, not a prediction.
- The rm/rc = 5.2 Hofstadter agreement is the single strongest candidate for a three-way quantitative cross-check; it requires a MaSt compound-mode projection calculation that has not yet been done.

---

## Relation to existing project docs

- `reference/WvM-summary.md` — WvM's (1,2) knot is a discretised electron mode; Losinets gives the continuous free-ring primitive that MaSt/WvM discretise, subject to the T2/T3 tensions.
- `qa/Q26-hadrons-photon-knots.md`, `qa/Q114` (g-factor) — the composite-mode magnetic moment combination rule (C5) constrains the g-factor work.
- `grid/foundations.md`, `primers/alpha-in-grid.md` — the GRID–Losinets substrate reconciliation (T1, C4) sits here.
- `papers/little-balls.md`, `papers/universe-as-mode.md` — the "what is a particle" thread Losinets makes mechanically concrete at the free-photon layer but only phenomenologically at the baryon layer.
- `models/model-E.md` — the proton mode (0, 0, −2, 2, 1, 3) whose 3D projection is the target of C1.
