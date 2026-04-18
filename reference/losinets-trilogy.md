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
| **Compound particles** | — | Two-zone Hill vortex (nucleons); ring assemblies (hyperons, partial) | Multi-winding T⁶ modes across e-, ν-, p-sheets |
| **Charge mechanism** | Topological phase winding on the lattice; e = √(4πα) | Circulation invariant Q = ρ₀·r₀·Γ (K–V units); SI via R | Tube-winding integer, Q = −n₁ + n₅ from Ma–S coupling sign |
| **Single dial** | α (dimensionless) | R = τ_KV = η₀/G = ν₀/c² (time) | α (dimensionless, inherited from GRID) |

The three frameworks are **not** competitors but cover different slices of a single architecture. They agree strongly on concepts (charge from winding, photon as ring-like, Coulomb gauge as a consequence not an assumption), and disagree or fail to connect on substrate microstructure, free-photon internal structure, and spin sector. Both the agreements and the disagreements are structural, not cosmetic.

---

## Genuine three-way meshing

**1. Charge as a winding invariant.** GRID derives it from U(1) phase periodicity; Losinets from Kelvin's circulation theorem; MaSt from tube-winding integers. Three independent routes to the same statement — charge is topological, not a material property of a point particle.

**2. Coulomb gauge without assumption.** GRID gets it from local gauge invariance (A4). Losinets gets it from incompressibility (∇·u = 0 ⇒ ∇·A = 0 when A = Ru). MaSt simply inherits Maxwell. The mechanical version (Losinets) is the most transparent; the gauge-theoretic version (GRID) is the deepest.

**3. Mass = confined-photon frequency.** MaSt's white-paper argument *m = hf/c² for the confined-photon circulation frequency* is stated verbally. Losinets's eq. 15, E_n = n·ℏω from Γ_n = n·h/m_vac, **derives** the same relation from a specific mechanical model — modulo the interpretation of what "n" and "ω" are. MaSt's mass formula is the statement that a confined photon's energy is its eigenfrequency; Losinets's E_n = n·ℏω is the statement that a ring of fixed ρ supports a ladder of circulation quanta. These are related but not identical statements, and conflating them obscures the difference.

**4. A single coupling dial.** Each framework has exactly one free electromagnetic input: α (GRID, MaSt) or R = τ_KV (Losinets). R has units of time and is measurable in principle from the fluid properties; α is dimensionless. If both descriptions are valid at different scales, there should be a relation of the form α = f(R·m_P·c²/ℏ) or similar, relating the mechanical relaxation time to the dimensionless coupling via the Planck scale. Neither paper writes this down.

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

One candidate mechanism: spin-½ in MaSt may be a pair property (two half-windings around a ring equals one full trip), and the "photon" that gets wrapped is not a single Losinets ring but a more complex object that pairs circulation with a reference phase. This is not what the trilogy's papers say — it's a conjecture to be developed, not imported from Losinets.

**T4. Nucleon in 3D vs. T⁶.** Losinets's nucleon is a **spatially** extended vortex with two 3D zones (r_c = 0.25 fm, r_m = 1.3 fm). MaSt's proton is a 6D standing wave (0, 0, −2, 2, 1, 3) whose amplitude is defined on the compact torus, not on 3D space. To compare them quantitatively one must **project** the T⁶ mode onto a 3D radial charge density. This projection has not been done. Without it, coincidences of length scale (see below) are suggestive but not verified.

---

## Cross-check targets (the punch list)

### C1. Hofstadter two-scale structure (strongest concrete target)

Losinets derives r_m/r_c ≈ 5.2 parameter-free from equal-charge + Hill two-zone structure. MaSt's p-sheet has L₅ = 2.45 fm (tube circumference) and L₆ = 4.45 fm (ring circumference). Neither ratio nor the individual scales alone reproduce r_c = 0.25 fm and r_m = 1.3 fm directly. But after a projection of the proton mode (0, 0, −2, 2, 1, 3) onto a 3D radial charge density, one should ask:

- Does the projection exhibit two characteristic scales?
- Is the ratio close to 5?
- Do the absolute scales match 0.25 fm and 1.3 fm?

A yes on all three would be a substantive three-way agreement between Losinets (two zones from equal-charge ansatz), MaSt (two scales from T⁶ projection), and Hofstadter (two scales measured directly). A clear no on any one of them falsifies the equivalence at the compound-particle layer.

**Status (R60, 2026-04):** tested — **fails at the kinematic level**. All twelve (density × projection) combinations produce two scales, but the ratios cluster in [1.3, 1.8] near the raw p-sheet ratio L₆/L₅ ≈ 1.82, never reaching 4.0. Only Fourier-form-factor projections deliver an outer scale near 1.3 fm (matching r_m), but the partnering inner scale sits at ~0.95 fm rather than ~0.25 fm, so the ratio is wrong. The result points to the Hofstadter mantle being dynamical (self-field / K–V elastic wake) rather than part of the T⁶ eigenmode amplitude, and constrains R55: a purely local Ma-S rescaling of the p-sheet cannot generate the 5.2 ratio; a second physical-space scale must enter. Full report: [R60 findings](../studies/R60-losinets-projection/findings.md).

### C2. m_vac from MaSt geometry

If Losinets's free-photon ring radius ρ(ω) equals a MaSt confinement scale at the particle's natural frequency, m_vac is no longer free. The literal identification (previous versions of this note):

- ω_e = m_e c²/ℏ ≈ 7.76 × 10²⁰ rad/s,
- ρ = L₂/(2π) ≈ 1.89 fm (taking L₂ = 11.9 fm as the e-sheet ring circumference),
- m_vac = ℏ/(ω·ρ²) ≈ **3.8 × 10⁻²⁶ kg ≈ 21 GeV/c²**.

(An earlier version of this note gave ~200 GeV/c², which was arithmetically wrong.)

**This 21 GeV number is a number, not a derivation.** The identification assumes:

- the relevant ω for a confined mode is the Compton frequency (it may differ by 2π or by a wrapping factor),
- the relevant ρ for a confined mode is a 3D ring radius equal to L₂/(2π), even though L₂ is a length of a compact dimension, not a 3D vortex ring radius (T4 above),
- n = 1 is the right quantum number.

Each assumption is questionable. The correct attitude: if **some** careful identification of ρ and ω yields an order-of-magnitude stable value of m_vac from MaSt's geometry alone, with no adjustable factor, that would close one of Losinets's main open questions. The 21 GeV result does not yet qualify — but it is in a physically reasonable range (not 10⁻²⁰ eV, not 10¹⁹ GeV), which suggests the exercise is worth finishing.

### C3. Near-field E_z structure for confined modes

Losinets predicts free-photon near-field E_z ∝ sin(b)·exp(−|r|/r₀). A MaSt confined mode is a superposition of such photons on the compact geometry. Naively:

- **Neutrino modes** (pure ν-sheet, no Ma–S coupling, Q = 0): no net near-field E_z. Consistent with observed electric neutrality.
- **Scalar charged modes** (pions, with both e- and ν-tube windings to achieve spin 0 + Q ≠ 0): potentially maximal near-field E_z.
- **Proton (compound mode across three sheets)**: complex near-field with structure tied to form-factor behaviour at large Q².

These predictions are **analogies, not derivations**. Whether a MaSt confined mode actually inherits the Losinets (a, b) → E_z structure depends on how the compactification projects polarisation onto winding — which, per T3, is not a trivial map. Listing these as "predictions" without derivation would be overselling. Listing them as motivated targets for a projection calculation is fair.

### C4. α from R

GRID has α as its one dimensionless EM input. Losinets has R = ν₀/c² as his one time-scale EM input. A candidate bridge:

> α = R · (some Planck-scale frequency) / (some geometric factor)

This is the cleanest question raised by the two-framework pair: can α be read off as the ratio of two mechanical times (K–V relaxation / Planck light-crossing)? Not addressed by any of the three papers but hard to avoid once the layer map is taken seriously.

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
