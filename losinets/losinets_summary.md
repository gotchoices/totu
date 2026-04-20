# Losinets × MaSt × GRID — programme summary

Status: complete through R63 (studies R60–R63) and the α↔R derivation (`losinets/alpha-vs-R.md`). This document consolidates what was tested, what was found, and what the findings mean for the three-framework architecture and for a potential collaboration with Losinets.

Companion: `losinets/losinets-trilogy.md` (layer map and punch list; this document supersedes most of its interpretive content with the completed results).

---

## Executive summary

**Top-line.** Naive unification between MaSt, GRID, and the Losinets trilogy fails at every layer where it was directly tested. In its place a layered complementarity picture emerges, in which the three frameworks describe different objects at different scales and the translations between layers are regime changes, not identities. The failures are informative: they sharpen where each framework does original work and where the cross-framework derivations actually live.

**What was tested (five items, all resolved):**

| # | Claim | Verdict | Headline number |
|---|---|---|---|
| R60 | MaSt proton T⁶ eigenmode projects onto Losinets's two-zone charge density | **fails** kinematically | best ratio 1.77 (target 5.2) |
| R61 | Losinets's mantle ≈ 1.3 fm is the K-V elastic wake of the MaSt eigenmode core ≈ 0.4 fm | **partial pass** | r_mantle = 1.26 fm at η = 10⁻³ (±3%) |
| R62 | MaSt L's fix Losinets's m_vac via Γ = h/m_vac closure | **fails** | 25 decades spread across 4 identifications |
| R63 | MaSt's odd-tube-winding → spin-½ rule can be stated in K-V language | **none cleanly closes** | L = ρ₀Γr₀² has wrong units and is 10²⁰ off ℏ |
| R-α | α derives from R = τ_KV | **orthogonal axes** | α = π·ρ₀·r₀²·ℏ/(m_vac²·c); R drops out |

**One bonus finding.** The Planck-scale K-V estimate gives **R ≈ t_P ≈ 5.4 × 10⁻⁴⁴ s** — a concrete falsifiable cross-framework prediction if GRID's discrete lattice is the coarse-graining of Losinets's K-V continuum.

**One suggestive coincidence.** α^(−1/3) ≈ 5.156 lands within 1% of Losinets's empirical r_m/r_c ≈ 5.2. Not derived by any framework; flagged for future work.

**The emergent picture.** Each framework occupies a distinct layer:

- **GRID** — discrete 4D causal Planck lattice. Substrate microstructure.
- **Losinets EfD** — continuum K-V viscoelastic medium. The long-wavelength limit of GRID if R = t_P is realised.
- **Losinets photon** — 3D vortex-ring primitive with internal structure (ρ, r₀, (a, b)).
- **MaSt** — topological standing-wave eigenmodes on a compact 6-torus. Gives particle spectrum.
- **Losinets baryon** — K-V mechanical response of the medium around a charged core. Gives nucleon mantle.

These layers are **not** three descriptions of the same physics. They are three descriptions of **three different things** that meet at specific interfaces. Where they meet the match can be quantitative (R61, R-α at Planck); where they don't meet the mismatch is geometric and diagnosable (R60, R62, R63).

**The offer to Losinets** is not equivalence but complementarity. See §6 for the specific framing.

---

## 1. Technical background

### 1.1 Losinets EfD — Maxwell from K-V vortex mechanics

Losinets establishes a **formal mathematical isomorphism** (not an ontological claim) between Maxwell's equations and the linearised dynamics of a dilute assembly of compact Hill-type vortex rings in an **incompressible Kelvin–Voigt viscoelastic fluid**. The core structure:

**Constitutive law.**

> σ = 2G E(d) + 2η₀ D(u)

combines an elastic response (shear modulus G, stress from displacement d) with Newtonian viscosity (η₀, stress from strain rate from velocity u).

**Shear modulus scaling** (from Hill-vortex shape stability + Tkachenko back-reaction):

> G ≈ 0.234 Γ²/r₀²

for a single vortex ring of circulation Γ and core radius r₀.

**Wave speed and relaxation time.**

> c = √(G/ρ₀)     R ≡ τ_KV = η₀/G = ν₀/c²

(ν₀ = η₀/ρ₀ is the kinematic viscosity.)

**Derived results (exact, not assumed):**

- Damped shear-wave equation for A = R·u, with u the solenoidal velocity field.
- Coulomb gauge ∇·A = 0 from incompressibility alone.
- All four Maxwell equations; in the far field the viscous correction vanishes.
- **Electric charge as circulation invariant:**

  > Q = ρ₀·r₀·Γ   (K-V units; SI via R)

  conserved by Kelvin's theorem.

**Free parameters / openly flagged:**

- Γ = n·h/m_vac is **imported** from Onsager–Feynman superfluid analogy. The effective medium particle mass **m_vac** (a mass, not a density) is not derived — §2.4 explicitly asks for a closure via E_ring = ℏω using K-V elastic energy.
- Spin quantisation (L = ρ₀·Γ·r₀² in units of ℏ/2): flagged open in baryon §2.2.
- Framework is non-relativistic and non-quantum; no Lorentz covariance.
- Explicitly: "no ontological claim is made that electromagnetism is mechanical."

### 1.2 Losinets photon — free photon as a vortex ring

A free photon is a **propagating compact vortex ring** in the K-V medium, with:

- ring (major) radius ρ,
- core radius r₀ ≈ λ̄ = λ/(2π),
- circulation Γ,
- orientation angles (a, b) on the Poincaré sphere.

**Ring-radius / frequency relation.** From Γ = 2π·ρ²·ω and Γ = h/m_vac at n = 1:

> ω(ρ) = ℏ/(m_vac · ρ²)     i.e.     ρ(ω) = √(ℏ/(m_vac·ω))

Higher-frequency photons correspond to smaller rings (ρ ∝ ω^(−½)). Multi-quantum modes give E_n = n·ℏω, reproducing Planck–Einstein.

**Jones formalism exact.** The ring trajectory's xy-projection gives the transverse Jones 2-vector; S₃ = cos b.

**Falsifiable prediction.** For tilted rings (b ≠ 0), the z-coordinate of a fluid element on the ring is non-zero, producing a **near-field longitudinal E_z** confined to |r − r_vortex| ≲ r₀ with |g|² ∝ sin²b. PINEM can resolve this at sub-wavelength impact parameter. Standard QED predicts zero.

**The photon is spin-1.** Jones 2-vector, Poincaré sphere, circular/linear polarisation are all spin-1 statements. Nothing in the free-photon paper generates a spin-½ object.

### 1.3 Losinets baryon — two-zone nucleon

A nucleon is a **single** Hill-type vortex with two hydrodynamically distinct zones:

- inner **core** (rotational, vorticity ≠ 0), radius r_c ≈ 0.25 fm,
- outer **mantle** (irrotational but carrying circulation and K-V elastic energy), outer radius r_m ≈ 1.3 fm.

Both radii are from 1960s Hofstadter electron-scattering data; neither is derived.

**Equal-charge condition** (Q_c = Q_m = e/2 from proton = +e, neutron = 0 under core-reversal) gives r_c·ω_c = r_m·ω_m. With μ ∝ ρ₀·Γ²/r₀ per zone:

> |μ_c|/|μ_m| = r_m/r_c ≈ 5.2

A parameter-free relation matching experiment (μ_c = 2.35 μ_N, μ_m = 0.44 μ_N from nucleon data gives μ_c/μ_m = 5.34, consistent with r_m/r_c = 5.2 ± 1.2).

**Hyperon extensions fail in a structured ladder** (Λ underdetermined, Σ inconsistent, Ξ no physical solution) — Losinets reads the failure pattern as diagnostic of strangeness-induced complication.

### 1.4 GRID — discrete Planck-scale substrate

Six axioms: 4D causal lattice (A1), Lorentzian signature (A2), periodic internal phase (A3), local gauge invariance (A4), information resolution ζ = 1/4 (A5), EM coupling α (A6). From these:

- Maxwell's equations from phase dynamics on links.
- Gravitational constant G = 1/(4ζ) in natural units.
- Charge quantisation from phase periodicity.
- Elementary charge e = √(4πα) in natural units.

α is the sole free EM input; ζ follows from tetrahedral simplicial packing near a causal horizon. MaSt inherits Maxwell + α from GRID.

### 1.5 MaSt — standing-wave particle spectrum

Particles are **standing EM waves on a compact T⁶ × S³ × t × phase** manifold. Each mode is labelled by six integers (n₁, …, n₆). Mass = eigenfrequency; charge = topological tube-winding (Q = −n₁ + n₅); spin-½ from odd tube-winding parity.

Key geometry (model-E):

- e-sheet (dims 1–2): L_tube = 4717 fm, L_ring = 11.9 fm, ε_e = 397.
- ν-sheet (dims 3–4): L_tube ≈ 2.1 × 10¹¹ fm, L_ring ≈ 4.2 × 10¹⁰ fm, ε_ν = 5.
- p-sheet (dims 5–6): L_tube = 2.45 fm, L_ring = 4.45 fm, ε_p = 0.55.

Proton mode: (0, 0, −2, 2, 1, 3), exact eigenmode at 938.272 MeV. Neutron: (0, −4, −1, 2, 0, −3), near-miss at 0.07% (consistent with 880 s decay).

4 dimensionless inputs (α, m_μ/m_e, m_τ/m_e, Δm²-ratio) + 3 scales (m_e, m_p, Δm²₂₁) reproduce 18 of 20 surveyed particles spin-correct, nuclear scaling to ≤ 1.1%, three lepton generations from shear resonance, neutrino oscillation exact.

---

## 2. The five tested claims

### 2.1 R60 — Hofstadter kinematic projection (failed)

**Claim.** Projecting the MaSt proton mode (0, 0, −2, 2, 1, 3) onto 3D radial charge density reproduces Losinets's two-zone structure (r_c = 0.25 fm, r_m = 1.3 fm, r_m/r_c = 5.2).

**Method.** Twelve (density × projection) combinations: three charge-density prescriptions (standing wave M-A, kinetic/gradient M-B, charge-weighted M-C) × four projections (embedding-sum Gaussians P-1, node-wavelet packets P-2, hydrogen-like basis via Monte-Carlo T⁶ sampling P-3, Fourier form factor P-4).

**Result.** C1 (two peaks): met in every variant. C2 (ratio in [4, 6.4]): **failed**; best 1.77, variants clustered at [1.3, 1.8]. C3 (absolute scales): **failed**; inner never below 0.39 fm, outer hits 1.33 fm in only two variants. C4 (neutron sign-reversed core): one variant gives the right sign pattern but wrong magnitudes.

**Root cause.** Only two physical scales enter the Hofstadter radial window: L₅ = 2.45 fm and L₆ = 4.45 fm, ratio 1.82. The ν-sheet at ~10¹⁰ fm is invisible on the grid. No integer-winding geometric operation on two scales produces a ratio of 5.2 without a free parameter.

**Reading (R60 Interpretation 2).** The MaSt T⁶ eigenmode gives the **rotational core** (~0.4 fm); the 1.3 fm mantle is not in the eigenmode amplitude — it must be the K-V elastic response of the surrounding medium. This directly tracks Losinets's own core-vs-mantle distinction (rotational vs irrotational-but-circulating) and reframes the cross-check as R61.

### 2.2 R61 — K-V wake around eigenmode core (partial pass)

**Claim.** Losinets's mantle at 1.3 fm is the K-V elastic wake of the MaSt eigenmode core at ~0.4 fm in the surrounding viscoelastic medium.

**Method.** Hill-vortex exterior stream function (EfD Appendix F, lab frame, no uniform flow): ψ_ext(r, θ) = A·sin²θ/r with A = U·r₀³/2. Angular-averaged energy density ⟨|u|²⟩ = 2A²/r⁶. Wake threshold operational definition: r_mantle where ⟨|u|²⟩(r_mantle)/⟨|u|²⟩(r_core) = η.

**Result.** The Hill exterior has no intrinsic length. Five candidate sources for r_mantle ≈ 1.3 fm were evaluated:

| Candidate | r_mantle | vs 1.30 fm | parameter-free? |
|---|---:|---:|:---:|
| K-V viscous length ν₀/c | — | — | no (needs m_vac) |
| Hill exterior pure decay | — | — | n/a (no length) |
| Charged pion Compton ℏ/(m_π c) | 1.414 fm | +9% | yes |
| α^(−1/3) · r_c (r_c = 0.25 fm) | 1.289 fm | −1% | yes |
| η = 10⁻³ threshold on r_core = 0.40 fm | 1.260 fm | −3% | needs η |

**Formula.** With 1/r⁶ decay, r_mantle = r_core · η^(−1/6). The ticket's original η^(−1/4) formula (2-D dipole) was wrong for the axisymmetric 3-D Hill exterior; the corrected exponent makes r_mantle less sensitive to the choice of η (one decade of η shifts r_mantle by 47%).

**Pass/fail summary.** Task A (closed-form exterior): met. Task B (≥ 1 candidate within 20% parameter-free): met (pion Compton +9%; α^(−1/3)·r_c −1%). Task C (single η gives 1.3 fm for both r_core values): **partial** — η = 10⁻³ works for r_core = 0.4 fm; r_core = 0.25 fm needs η ≈ 5 × 10⁻⁵. Task D (proton/neutron mantle equivalence): met trivially (|u|² independent of sgn Γ, as Losinets's construction requires).

**Net verdict.** The hypothesis R60-Interpretation-2 survives quantitatively: a K-V wake of a nucleon-sized core lands at a Hofstadter-compatible mantle scale under physically reasonable assumptions and is identically consistent with Losinets's proton↔neutron core-reversal convention. But 1.3 fm drops out only with an input the K-V framework does not fix internally — either η ≈ 10⁻³, m_π, or α via α^(−1/3).

**The α^(−1/3) coincidence.** α^(−1/3) = 5.156 lands within 1% of Losinets's empirical r_m/r_c = 5.2. Neither framework produces α as a 3-D geometric exponent (α is absent from Losinets's K-V; it enters MaSt via Ma-S coupling, not via a dimensional ratio). Flagged as either noise or a hint of a deeper structural bridge.

### 2.3 R62 — m_vac across particles (failed)

**Claim.** Some consistent identification of (ρ, ω) between a MaSt confined mode and a Losinets free-photon ring yields a universal m_vac.

**Method.** Four identifications, ρ = L/(2π):

| # | Identification | ρ | ω | m_vac |
|---|---|---:|---:|---:|
| I-1 | e-sheet ring × electron | 1.894 fm | 7.76 × 10²⁰ rad/s | **21.2 GeV/c²** |
| I-2 | e-sheet tube × electron | 750.7 fm | 7.76 × 10²⁰ rad/s | 135 keV/c² |
| I-3 | p-sheet ring × proton | 0.708 fm | 1.43 × 10²⁴ rad/s | 82.7 MeV/c² |
| I-4 | ν-sheet ring × ν₃ | 6.69 × 10⁹ fm | 8.84 × 10¹³ rad/s | 15 meV/c² |

**Result.** I-1 and I-3 — the two charged-particle ring identifications, the natural place to look for consistency — disagree by **257×**. The full four-way spread is 25 orders of magnitude. No convergence.

**Decomposition.** m_vac^(I-1)/m_vac^(I-3) = (ρ_p/ρ_e)² · (ω_p/ω_e) = (L₆/L₂)² · (m_p/m_e) = (0.374)² · 1836 = 257. Geometry-driven: MaSt L's are fitted to eigenmode mass spectra (L₂/L₆ = 2.67), not Compton ladders (m_p/m_e = 1836). For I-1 ≡ I-3 to hold, p-sheet ring ρ would need to shrink by √(m_e/m_p) ≈ 1/43, far below L₅ = 2.45 fm.

**I-4 as category-mismatch marker.** An m_vac of 15 meV/c² — below the neutrino mass it would quantise — is physically incoherent. The ν-sheet length is a compactification radius of an internal dimension, not a 3D vortex-ring radius. The 10¹² factor in I-4/I-1 records the category mismatch honestly.

**I-5 (exploratory).** Substituting ρ_m = G/c² into the classical thin-core kinetic energy and setting E_ring = ℏω gives m_vac³ ∝ ρ³[ln(8ρ/r₀) − 7/4]/(r₀²·c²) — a one-parameter family (m_vac, r₀), not a number. Indicative scan at ρ = 1.89 fm gives m_vac ≈ 1–20 keV/c² across r₀ = 2–0.1 fm — 6 orders below I-1. This reproduces Losinets's own §2.4 disclaimer that the classical kinetic form is a lower bound; the full K-V elastic-energy closure is still needed.

**Net verdict.** MaSt does not fix m_vac. The failure is geometry-driven: MaSt L's are particle eigenmode scales, not free-photon ring scales; these are different physical quantities and identifying them across the free-vs-confined regime enforces no universality. Closing m_vac from Losinets's K-V alone requires the §2.4 elastic-energy derivation Losinets himself flagged.

### 2.4 R63 — spin-½ mechanism (none cleanly closes)

**Claim.** MaSt's "odd tube-winding → spin-½" rule can be translated into Losinets's K-V language in a way that closes the baryon §2.2 open problem on quantisation of L = ρ₀·Γ·r₀² in units of ℏ/2.

**Phase A — dimensional/scale audit of L.** Substituting Losinets's own closures G = 0.234 Γ²/r₀² and ρ₀ = G/c² into L gives:

> L = ρ₀·Γ·r₀² = 0.234·Γ³/c²

**r₀ cancels identically.** The formula has SI units kg·m/s (linear momentum, not angular momentum). It requires multiplication by a length ℓ to be comparable to ℏ. Every natural ℓ (ρ, 2πρ, λ̄_e, ℏ/(m_vac·c)) gives L·ℓ between 10⁻²⁴ ℏ and 10⁻²⁰ ℏ — 20+ orders of magnitude off. For L·ρ to reach exactly ℏ, m_vac would need to shrink from 21 GeV to ~1.3 keV (a factor 10⁷).

**Consequence.** Spin-½ in a MaSt confined mode cannot be recovered by a refined *quantisation* of Losinets's bare L expression. The mismatch is structural (dimensional + scale), not a factor-of-2.

**Phase B — three candidate mechanisms:**

| Mechanism | e⁻ | π± | p | n | Σ⁻ | Closes §2.2? |
|---|---|---|---|---|---|---|
| **M1** half-wrap / double cover (Hopf-linked rings) | ✓ | ✓ (with {0,1} ambiguity shared by MaSt) | ✓ | ✓ | ✓ | Conditionally — if K-V Hopf-linking phase derivation is supplied |
| **M2** paired circulation + reference phase | ✓ | **✗ ambiguous** | ✓ | ✓ | ✓ | No — composition rule not K-V-derivable |
| **M3** embedding parity label (not from Γ) | ✓ | ✓ | ✓ | ✓ | ✓ | No — relabels, does not derive ℏ/2 for L |

**M1 wins the inventory** and matches MaSt's compound rule including the parity of odd tube-windings for multi-sheet modes. The double-cover identification (two traversals of the primary ring to close a joint phase with a Hopf-linked partner) supplies the ℏ/2-per-single-traversal quantum structurally. But the Hopf-linking phase derivation is **not** in Losinets's trilogy and would be new K-V work.

**M2 fails at π±.** Two odd-winding projections compose to {spin-0, spin-1} with no K-V-native rule selecting the spin-0 scalar pion. This falsifies the earlier trilogy-note §T3 paired-circulation conjecture.

**M3 is the minimal reframe.** Spin-½ is a parity label on the compactification sector; L keeps its ℏ quantisation; Losinets's §2.2 problem as stated has no solution and the correct K-V statement is that spin-½ is not a property of L. Honest but does not derive ℏ/2.

**Net verdict.** §2.2 stays open. R63 narrows the solution space to the M1 direction. A genuine K-V derivation of half-integer spin requires (a) a Hopf-linked pair construction with odd linking number and (b) a K-V phase-integral derivation of the angular-momentum functional whose ground state has ℏ value — which is the same §2.4 elastic-energy closure R62 flagged for m_vac. **The m_vac and spin-½ open problems are the same problem.**

### 2.5 R-α — α and R on orthogonal axes (resolved)

**Claim.** Can GRID's fine-structure constant α be derived from Losinets's K-V relaxation time R via Planck-scale quantities?

**Method.** Substitute Losinets's correspondence-table identifications into α = e²/(4πε₀ℏc).

- Q = ρ₀·r₀·Γ (EfD eq. 29)
- ε₀ = ρ₀ (EfD §7.4)
- Γ = 2πℏ/m_vac (Γ = h/m_vac with h = 2πℏ)

**Result.** α = ρ₀·r₀²·Γ²/(4πℏc) = ρ₀·r₀²·(2πℏ)²/(m_vac²·4πℏc):

> **α = π · ρ₀ · r₀² · ℏ / (m_vac² · c)**

R = η₀/G **does not appear**. R controls dissipation and K-V-to-SI conversion but cancels from the dimensionless coupling. α and R live on orthogonal axes of Losinets's K-V parameter space.

**Conditional outcome.** If the photon §2.4 closure fixes m_vac = κ·ρ₀·c³·R³ (unique dimensional form), then α ∝ r₀²/(ρ₀·c⁷·R⁶). Two-knob, contingent on an open derivation. Recorded but not relied on.

**Bonus result — R at the Planck scale.** The original trilogy-note estimate R ≈ 1.5 × 10⁻¹²⁶ s was a unit-mixing error (μ₀/G_shear gives m²/A², not seconds). Dimensionally correct with G_shear = c⁴/(8πG_N), ρ₀ = G_shear/c², η₀ ≈ ρ₀·c·L_P:

> **R ≈ t_P ≈ 5.4 × 10⁻⁴⁴ s**

This is a concrete falsifiable prediction: if GRID's discrete 4D causal lattice is the coarse-graining of Losinets's K-V continuum, R equals the Planck time. The cleanest cross-framework prediction of the programme.

---

## 3. The emergent layer picture

The three frameworks describe **different objects at different scales**, and the translations between them are regime changes, not identities.

| Layer | What lives here | Framework | Cross-framework statement |
|---|---|---|---|
| Substrate (Planck) | Discrete 4D causal lattice | GRID | Losinets's R = t_P if the K-V continuum is the coarse-graining |
| Continuum (K-V) | Viscoelastic vacuum with vortex rings | Losinets EfD | R = ν₀/c² is the one dimensionful dial; Coulomb gauge from incompressibility |
| Free photon | 3D vortex ring ρ(ω), r₀, (a, b) **or** plane-wave primitive | Losinets photon **vs** MaSt/Maxwell | PINEM near-field E_z test decides between them |
| Confined mode | T⁶ standing wave — rotational core ~0.4 fm | MaSt | Eigenmode amplitude |
| Surrounding field | K-V elastic wake ~1.3 fm mantle | Losinets baryon | Irrotational response to the charged core |

**Where the layers meet cleanly:**

- Substrate ↔ K-V: R = t_P is a clean cross-framework prediction.
- Confined mode ↔ K-V wake: MaSt core + Losinets mantle = Hofstadter two-scale structure under η = 10⁻³ threshold (R61).
- Charge topology: Q = ρ₀·r₀·Γ (Losinets) ↔ tube winding (MaSt) ↔ e = √(4πα) (GRID). Three consistent formulations of the same topological invariant.

**Where the layers don't meet (without auxiliary input):**

- Free-photon primitive: different objects (ring vs plane wave). PINEM resolves.
- m_vac: not fixed by MaSt's L's; needs Losinets's own §2.4 closure.
- Spin-½: MaSt's topological rule is richer than Losinets's framework can currently express; needs a Hopf-linked K-V phase derivation.
- α from R: algebraically orthogonal. α depends on (ρ₀, r₀, m_vac), not on R.

---

## 4. Open problems

Ordered by which are likely to yield to further work:

**4.1 The §2.4 / §2.2 joint closure.** Losinets's photon §2.4 (m_vac from E_ring = ℏω using K-V elastic energy) and baryon §2.2 (L quantisation in ℏ/2) are the same problem — both require a full K-V derivation of the ring-energy and angular-momentum functionals including elastic storage, not just classical kinetic terms. If solved, R62's I-5 closes to a number and R63's M1 mechanism gains its K-V phase derivation. This is the single highest-leverage open item.

**4.2 α^(−1/3) ≈ r_m/r_c.** The numerical coincidence α^(−1/3) = 5.156 vs Losinets's empirical 5.2 is either noise or a structural hint that the compound-particle core/mantle ratio is set by the EM coupling itself. Investigating whether GRID's α has geometric consequences in MaSt's Ma-S coupling that would produce this ratio is a standalone question worth framing.

**4.3 Free-photon primitive reconciliation.** Losinets's ring (finite ρ, r₀, near-field E_z) and MaSt's plane wave are not the same object. PINEM near-field test is falsifiable experiment; either result has strong consequences for the layer picture.

**4.4 Hyperon failure pattern cross-check.** Losinets's three-way strangeness ladder (Λ underdetermined, Σ inconsistent, Ξ impossible) vs MaSt's hyperon near-miss pattern (Λ 0.00%, Σ⁻ 0.01%, Σ⁺ 0.02%, Ξ⁻ 0.03%, Ξ⁰ 0.19%) — do these correlate structurally? Not tested. Could be a tractable next ticket.

**4.5 K-V continuum as GRID coarse-graining.** R = t_P is a prediction; whether the K-V dynamics are literally the long-wavelength limit of GRID's discrete lattice is a harder structural question requiring a renormalisation-style derivation. Worth framing eventually.

---

## 5. Relation to Losinets's own open problems

Losinets's trilogy flags three open items explicitly. Their status after R60–R63 + R-α:

| Losinets open problem | Status | Our contribution |
|---|---|---|
| m_vac from E_ring = ℏω (photon §2.4) | still open | R62 shows MaSt doesn't fix it; the full K-V elastic-energy derivation is still needed |
| L = ρ₀·Γ·r₀² quantised in ℏ/2 (baryon §2.2) | still open | R63 shows it's the same problem as §2.4; MaSt's odd-tube-winding rule can be reframed as Hopf-linked K-V rings pending the phase derivation |
| Derivation of G_shape prefactor (EfD §2.1) | unchanged | Not addressed; Losinets's own pressure-jump lower bound G_shape ≥ 27Γ²/(175r₀²) stands |

**Our added items:**

- R ≈ t_P at Planck scale — GRID-level prediction testable via superfluid analogues.
- α^(−1/3) ≈ r_m/r_c numerical coincidence — worth explaining or dismissing.
- Hyperon pattern cross-check — not run.

---

## 6. Collaboration with Losinets

The question of how to approach Losinets — what to lead with, what to ask, in what form, with what specific offers — is developed separately in `losinets/losinets_proposition.md`. That document builds on the findings here and frames the communication; this one stays analytical.

---

## 7. References

**Source papers:**

- `losinets/losinets_EfD.pdf` / `.txt` — Maxwell from vortex mechanics (K-V substrate).
- `losinets/losinets_photon.pdf` / `.txt` — Free photon as vortex ring.
- `losinets/losinets_baryon.pdf` / `.txt` — Two-zone nucleon.

**Studies:**

- `studies/R60-losinets-projection/findings.md` — Hofstadter kinematic projection (failed).
- `studies/R61-losinets-mantle-wake/findings.md` — K-V wake around eigenmode core (partial pass).
- `studies/R62-losinets-mvac/findings.md` — m_vac universality (failed).
- `studies/R63-losinets-spin-half/findings.md` — Spin-½ mechanism (none cleanly closes).
- `losinets/alpha-vs-R.md` — α ↔ R derivation (orthogonal; R = t_P Planck prediction).

**Framework docs:**

- `papers/white-paper.md`, `models/model-E.md` — MaSt.
- `grid/foundations.md`, `grid/maxwell.md` — GRID.
- `losinets/losinets-trilogy.md` — earlier layer-map and punch list (superseded by this document for interpretive content; still current for framing).

**Tickets (all complete):**

- `tickets/complete/4-losinets-hofstadter-projection.md`
- `tickets/complete/4-losinets-mantle-as-kv-wake.md`
- `tickets/complete/4-losinets-mvac-identifications.md`
- `tickets/complete/3-losinets-spin-half-mechanism.md`
- `tickets/complete/3-losinets-R-alpha-bridge.md`
