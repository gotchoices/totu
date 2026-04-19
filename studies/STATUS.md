# Studies Registry

See [`../STATUS.md`](../STATUS.md) for electron objectives and project snapshot.  
See [`../qa/`](../qa/) for open physics questions and detailed problem analysis.

---

## Active

### R15. Forward charge calculation — deriving α
**Study:** [`R15-forward-charge/`](R15-forward-charge/)
**Questions:** [Q18](../qa/Q18-deriving-alpha.md), Q34 Path 7  **Type:** compute  **Depends on:** R7, R13

R7 computed U_Coulomb = α × m_e c² and called it a failure. R8 "fixed" it by
shrinking the torus, requiring R8-multi-winding (68,137). R13 showed R8-multi-winding
breaks WvM charge (monopole = 0, exactly). This revives (1,2) at Compton scale —
the only model where charge works. R15 runs R7's calculation *forward*: input
energy m_e c² and (1,2) topology, compute the far-field Coulomb flux, read off
charge Q, and check whether Q²/(4πε₀ℏc) ≈ 1/137. If so, α is derived from
energy and topology alone.

**Open sub-problem:** the formula α(r,s) produces a one-parameter family of
solutions — every r > ~2 has a self-consistent s.  Nothing currently selects r.
R44 attempted to pin r_e via the anomalous magnetic moment but produced a
negative result (charge-mass separation is order 1, not order α).  Pinning
r_e remains open — candidate routes: Casimir/vacuum energy, tau mass
constraint, or energy-partition g − 2.

### R30. Minimal material geometry — is a material sheet necessary?
**Study:** [`R30-minimal-geometry/`](R30-minimal-geometry/)
**Questions:** Q34, Q16  **Type:** theoretical + compute  **Depends on:** R19, R26, R27

Each material sheet represents a curve, not an area.  The persistent r-degeneracy
(r_e free, r_ν ≥ 3.2, only r_p pinned) and 20× ghost-mode over-prediction
suggest possible over-parameterization.  Can a circle reproduce particle
properties?  Is the charge mechanism irreducibly 2D?  What about Klein bottle
identification?  Hierarchical compactification?  Non-uniform circle?  5 tracks.

### R44. Anomalous magnetic moment from torus geometry  **Done — negative result**
**Study:** [`R44-g-minus-2/`](R44-g-minus-2/)
**Questions:** Q53, Q34  **Type:** compute  **Depends on:** R19, R8, R40

Tested whether R19 charge-mass separation produces g − 2 ≈ α/(2π).
Track 1 computed σ(θ₁,θ₂) and its magnetic moment on the embedded
torus.  **Result:** The charge density is an oscillating cos()
pattern, not a small perturbation.  The correction μ_actual/μ_uniform − 1
is of order −1.6 to −2.4 (wrong sign, ~1400× too large).  Charge-mass
separation from shear is ruled out as the g − 2 mechanism.
Tracks 2–4 cancelled (see findings F4–F7).

### R45. Magnetic moments from cross-sheet coupling  **On hold**
**Study:** [`R45-magnetic-moments/`](R45-magnetic-moments/)
**Questions:** Q53, Q34  **Type:** compute  **Depends on:** R19, R27, R28, R33, R44

### R46. Electron filter — aperture effects on a toroidal cavity  **Framing**
**Study:** [`R46-electron-filter/`](R46-electron-filter/)
**Questions:** Q100, Q53, Q94  **Type:** compute / grid simulation  **Depends on:** R44, R33, R40

**Track 1 (geodesic tilting): DONE — negative result.**  The magnetic
moment on a static flat torus is a topological invariant: L = ℏn
depends on winding numbers, not on the metric.  Cross-shear changes
velocity but not winding numbers → g = 4 independent of σ_ep.  The
naive current-loop formula gives g ≈ 1092 (unphysical, dominated by
L² amplification from the Ma_e sheet).  Tracks 2 and 4 are blocked
by the same topological argument.

**Track 3 (self-consistent dressed particles) remains the primary
path forward.**  The dressed proton is a composite of the bare
(0,0,0,0,1,2) mode plus cross-sheet excitations carrying DIFFERENT
winding numbers.  The total angular momentum of the composite is not
simply ℏn₆ — it includes contributions from excitations with their
own winding numbers.  This is a different physics from geodesic tilting.
6 tracks (1 done, 2 blocked, 3 viable).  **HIGH VALUE — Track 3.**

### R47. Proton geometry — mode, slots, and anomalous moment  **Track 7**
**Study:** [`R47-proton-filter/`](R47-proton-filter/)
**Questions:** Q90, Q53  **Type:** compute / interactive  **Depends on:** R46

Tracks 0–2: Torus Lab tool infrastructure (complete, still valid).
**Tracks 1, 3: Null** — (1,3) hypothesis abandoned (spin ⅓ ≠ ½).
**Track 4:** Spindle torus (ε > 1) for anomalous moment — ceiling
at g ≈ 4 vs target 5.586.  Current-loop g matches at ε = 0.252.
**Track 7 (active):** (1,2) vs (3,6) comparison against quark
phenomenology.  **(3,6) wins 8 of 11 criteria.**  SU(6) moments
μ_p = 3.000 μ_N (+7.4%), μ_n = −2.000 μ_N (+4.5%), constituent
mass m_p/3 = 313 MeV, and geometric confinement all follow from
the mode topology.  Key surprise: WvM charge integral is exactly
zero for n₁ = 3 — charge must come from (1,2) strand sub-structure.
Composite waveguide cutoff question flagged for eigenmode study.

### R56. Electron shell structure  **Active — Tracks 1–6 complete**
**Study:** [`R56-electron-shells/`](R56-electron-shells/)
**Type:** compute + theoretical  **Depends on:** R53, model-E

Shell structure as a lowest-energy routing problem: the Ma
torus at each Bohr radius has finite angular mode capacity
(n² from the closure condition l(l+1) < n²).  When full,
the next electron routes to S (next shell) because separation
is ~2.5× cheaper than promoting to the next harmonic.  Shell
capacities 2n² reproduced exactly with the factor of 2 from
tube winding topology.  Ghost mode suppression follows from
the same routing: higher harmonics exist but are energetically
uncompetitive with spatial separation.  Classical packing
(Tracks 1–4) failed; mode capacity (Track 6) succeeded.
Prior work: LaFave (2014) Thomson problem correspondence.

### R58. Phonon material search for neutrino frequency matching  **Active — Track 1 complete**
**Study:** [`R58-phonon-material-search/`](R58-phonon-material-search/)
**Type:** compute  **Depends on:** R49, L05, Q119

Systematic search for materials whose optical phonon frequencies
match MaSt-predicted neutrino frequencies (all 4 families, 12
targets).  Sub-1% matches found for 8 of 12 frequencies.  Best:
BaS at 7.45 THz (Family D ν₂, 0.0%), DCl at 13.99 THz (Family D
ν₃, 0.0%), CaSe at 7.36 THz (Family A ν₂, 0.1%).  These materials
could serve as precision resonant filters in L05, converting
optical beats into real phonon oscillations at neutrino frequencies.
Tracks 2–4 (deuterides, molecular vibrations, DFT validation) pending.

### R57. Energy routing between Ma and S  **Complete — Tracks 1–5**
**Study:** [`R57-energy-routing/`](R57-energy-routing/)
**Type:** theoretical + compute  **Depends on:** R56, R54, R49, model-E

Generalized routing engine: given input energy and a starting
mode configuration, predict whether energy accumulates in Ma
(dark modes, higher harmonics) or forges new particles in S.
Key application: proton-to-neutron transition via Ma pathway
(mode rearrangement) vs S pathway (Coulomb barrier).  If the
Ma route is cheaper, it provides a theoretical mechanism for
LENR/cold fusion: dark mode accumulation on the ν-sheet builds
to the 1.3 MeV p→n threshold without spatial collision.
Companion to L04 (THz neutrino experiment) and L02 (threshold
nuclear loading).

### R59. Self-consistent metric with time  **Complete**
**Study:** [`R59-clifford-torus/`](R59-clifford-torus/)
**Type:** theoretical + compute + visualization
**Depends on:** R55, R54, R53, sim-impedance, GRID

Tested whether adding time to the Ma metric produces α via
Kaluza–Klein coupling on 10D/11D architectures.  Ten tracks
completed.  Negative on the original claim (direct Ma-t on
model-E, ring-based ℵ mediation, direct Ma-t on a clean metric
all fail to reach α at the spatial level).  Positive on a spinout
architecture: **tube↔ℵ↔t on a clean Ma metric** gives exact
structural universality (α_e = α_p by |n_tube| = 1) and reaches
α at a natural-form parameter point (k = 1/(8π), g_aa = 1,
σ_at = 4πα, σ_ta = √α) within 60 ppm (F59).  Model-E's internal
shears (s_e = 2.004) saturate the e-tube and block this
architecture on model-E geometry (F41) — R60 is scoped to find
whether a modified spectrum mechanism can coexist with it.

### R60. Metric-11 — particle spectrum on R59's α-derivable 11D architecture  **Complete — Tracks 1–14; model-F promoted**
**Study:** [`R60-metric-11/`](R60-metric-11/)
**Type:** theoretical + compute
**Depends on:** R59, R53, R49, R54, R61, model-E

Can a metric configuration be found that simultaneously implements
R59's α architecture and reproduces the model-E particle spectrum?

Tracks 1–4 built solver infrastructure (F1–F4), mapped the
e-sheet (F5–F10) and p-sheet (F11–F16) viability regions, and
discovered that per-sheet diagonal compensation (k_e ≠ k_p)
rescues α universality+magnitude in 66% of (ε, s) configurations
(F17–F21).  Track 5 derived the α-decoupling locus in closed
form: `Q = 0 ⟺ n_r/n_t = sε + 1/(sε)` (F22); (1,1) modes never
decouple, (1,2) modes decouple at sε = 1, (1,3) modes at
sε ≈ 0.382 or 2.618.  Track 5 Part 1 confirmed wide proton
viability under shearless electron (F23–F26).

Track 6 added the ν-sheet on equal footing (sign_nu = +1, σ_ta
coupling, free k_ν).  **Joint e+p+ν solver converges cleanly at
g_aa = 1 with α_e = α_p = α_ν₁ = α universality** for three of
four R61 ν-sheet candidates (F27–F31).  k values cluster within
20% of R59 F59 natural value for charged sheets; per-sheet L
scales span 10+ orders of magnitude (L_p = 19 fm, L_ν = 2×10¹¹
fm) consistent with mass hierarchy.  **R60's full architecture
is now validated** as compatible with the model-E three-sheet
foundation.

Track 7 added ring↔ℵ structural cancellation σ_ra = (sε)·σ_ta
per sheet.  Mode-dependence on ν collapsed from 28% to 0%.
Tracks 7b–7d re-solved with the fix across shearless/magic-shear
geometries — all produced the same emergent single-k symmetry
k = 0.04696 = 1.1803/(8π).  Track 7c found most cross-sheet σ
entries break α universality (pool item **h**).

Track 8 found compound α exactly quantized:
`α/α = (n_et − n_pt + n_νt)²`.  On the Track 7d baseline,
tau and neutron land cleanly but muon is blocked by mass desert.

**Tracks 8b + 9 revival:** confirmed σ_ra lifts Track 2's
signature bound (tested up to sε = 2000), then re-solved with
e-sheet at model-E extreme values (ε=397, s=2.004).  Single-k
symmetry survives even sε ≈ 800.  **Muon at model-E's tuple
(1,1,−2,−2,0,0) lands at 104.78 MeV — 0.83% off, identical to
model-E's own accuracy.**  Tau and neutron at alternate tuples
within 0.2%.  All α universal, ν predictions intact, Δm² ratio
= 33.59.  R53's generation resonance mechanism working on R60's
augmented architecture.

Recommended next: Track 10 — broader hadron inventory (Σ, Λ,
Ξ, Ω, K, π, η, ρ, φ) on this baseline.

### R55. α consistency — Ma-S coupling derivation  **Tracks 1,3 done; Track 4 paused**
**Study:** [`R55-alpha-consistency/`](R55-alpha-consistency/)
**Questions:** Q115, Q116, Q102  **Type:** theoretical + compute  **Depends on:** R54, R19, R48, GRID

Track 1: Direct Ma-S coupling (Schur complement) gives
mode-dependent α — fails universality (30%+ spread on e-sheet).
Track 3: ℵ-mediated 10×10 metric with ring-only Ma-ℵ coupling
achieves near-universal α (3.6% e-p gap), nonzero ν coupling,
and 0.4% spectrum shift.  The coupling direction (which side
carries α) is symmetric in the metric.  Track 4 (self-consistent
parameter re-derivation) paused — preliminary scans show
adjusting scale preserves generations.

### R54. Compound modes on the full T⁶  **Active — Tracks 1–3 complete**
**Study:** [`R54-compound-modes/`](R54-compound-modes/)
**Questions:** Q115, Q116  **Type:** compute / theoretical  **Depends on:** R53, R50, R49

Full particle inventory on the 6D torus with individual cross
entries (not scalar σ_ep).  **Results: 18 of 20 spin-correct modes
(2 resonances: Δ⁺, Ω⁻ as excited-state overtones).**  Stable particles (proton,
electron) are exact eigenmodes.  17 of 18 unstable particles
within 2%.  Pions at 23–25% off — large miss consistent with
short lifetime.  Pion spin-charge constraint solved via
multi-sheet tube windings (e+ν compound gives spin 0 with Q = ±1).
Neutron is an e+ν+p 6D knot at 0.07% off, whose decay decomposes
the knot into electron + neutrino + proton.

### R53. Three generations from in-sheet shear  **Active — Tracks 1, 4 complete; 5–7 pending**
**Study:** [`R53-three-generations/`](R53-three-generations/)
**Questions:** Q115  **Type:** compute / theoretical  **Depends on:** R50, R49, R19

Tests whether the three charged lepton masses (e, μ, τ) emerge
from three low-order modes on the electron sheet when in-sheet
shear s_e is freed from the α = 1/137 constraint and treated as
a generation-structure parameter (paralleling the neutrino sheet's
s₃₄ = 0.022 which gives three ν mass eigenstates).  Track 1
solves for (ε_e, s_e) from mass ratios; Track 2 counts ghosts;
Track 3 checks α; Track 4 applies the method to the proton sheet
for quarks.  Motivated by R50 Track 11's finding that (1, 506)
matches the muon at 0.049% but creates ~500 ghost modes —
suggesting the muon is a low-order mode at a different shear,
not a high harmonic at the current shear.

### R51. Hydrogen as compound torus mode  **Active — Track 1c complete**
**Study:** [`R51-hydrogen-mode/`](R51-hydrogen-mode/)
**Questions:** Q16  **Type:** compute / theoretical  **Depends on:** R29, R50

Tests whether atoms (starting with hydrogen) are pure compound
eigenmodes of the three tori — no spatial electron-nucleus
relation, no Bohr model.  "Adding an electron" means adding
energy quanta to Ma_e; shell filling is mode saturation
overflowing into dark Ma_ν modes.

- **Track 1**: σ_ep coupling crosses 13.6 eV only at σ_ep ≈ 0
  (effectively zero coupling); at particle-fitted σ_ep ≈ −0.28,
  ΔE_add balloons to ~261 keV.
- **Track 1a**: Systematically closed the σ_ep pathway.  Shears
  are O(0.1) not O(α), Schur complement shifts are MeV/keV
  scale, structural barrier from proton MeV scale.  Identified
  σ_eν as the remaining plausible path (F14).
- **Track 1b**: σ_eν pathway also fails.  The eν cross-term
  is ~10⁻⁵ eV at small neutrino quantum numbers — six orders
  of magnitude too small.  Root cause: both electron and
  neutrino sheets are large (L ~ 10³–10¹⁰ fm), making their
  n/L products doubly suppressed.
- **Track 1c**: Multi-mode picture (separate nuclear and
  electron modes coupled through shared neutrino quantum
  numbers) also fails.  Neutrino mode degeneracies are
  uniformly 2 (no shell structure).  Anti-correlated ν
  numbers give correct sign for binding but only −0.004 eV
  (3,400× too small).  All bilinear metric pathways closed.
  Two-tier physics (R29) appears structurally necessary.

### R50. Filtered multi-sheet mode search  **Active — Track 8 complete**
**Study:** [`R50-filtered-particle-search/`](R50-filtered-particle-search/)
**Questions:** Q16  **Type:** compute  **Depends on:** R29, R46, R47, R49

Joint 6D search on the **coupled** three-sheet metric (not
independent per-sheet catalogs).  Builds `lib/ma_model_d.py`
(R46–R49 filters, no hard-coded legacy pinning).  Nuclei
reprised from R29 Track 3 / F16 as richer mode combinations
under the new rules.  Philosophy: one system, near-misses
for unstable states, neutron not a calibration target.
Dual proton hypothesis: (1,3) leading, (3,6) alternative.
Track 6 dropped per-sheet waveguide filter and found that
(1,3) achieves 0.9 MeV neutron gap via a non-propagating
mode — the compound structure sustains modes that are
evanescent on isolated tori.  Track 7 swept σ_ep across the
full particle spectrum: both hypotheses optimize at σ_ep ≈ −0.28;
(3,6) fits the spectrum better (trimmed mean 0.89% vs 2.35%)
but (1,3) fits the physics better (universal charge formula,
nuclear scaling).  σ_ep remains a free parameter.
**Track 8** ran a viability sweep over the full inventory across
all four sign branches and a σ_eν grid: 16 of 20 particles
viable (≤ 5%), 9 excellent (≤ 1%), tau viable at 0.656% on a
purely ν+p mode.  **Muon NOT viable** (97.98% off, mass desert
real and structural across every branch); π±/K± topologically
forbidden as single 6-tuples; π⁰ also fails (84% off).  Negative
result on the muon motivates building a compound back-reaction
engine in a future study.
Parameter strategy: defaults with provenance, sweep before pin,
keep free variables free (model-D.md §Parameter strategy).

### R49. Neutrino sheet — filtering, oscillation, and mode spectrum  **On hold — Tracks 1–2a complete**
**Study:** [`R49-neutrino-filter/`](R49-neutrino-filter/)
**Questions:** Q85, Q94, Q99  **Type:** compute / theoretical  **Depends on:** R24, R25, R26, R46, R47

Neutrino sheet characterization.  Completed tracks:
- **Track 1**: ε broadly viable (0.1–5+), 3 solution families,
  not uniquely constrained by oscillation data alone
- **Track 1a**: Extra modes can't hide — sharp selection required
- **Track 1b**: Waveguide cutoff sets floor but doesn't select
  exactly 3; Assignment A near floor at ε ≈ 2–5
- **Track 2a**: Modes reach m_e at N ≈ 17.5M; Compton window
  (6.6 μm) encompasses ~10¹³ atoms in condensed matter
- **Q105**: Assignment A implies Majorana neutrinos via
  C-conjugate mixing; predicts 0νββ at |m_ββ| ≈ 10–30 meV

Remaining tracks (2–6) on hold pending weak coupling model.

### R52. Anomalous moment from torus self-field  **Framed — ready to compute**
**Study:** [`R52-self-field-moment/`](R52-self-field-moment/)
**Questions:** Q53, Q103  **Type:** compute  **Depends on:** R44, R45, R46, R47, R33

Computes the Coulomb self-potential of a charged mode embedded as a
torus knot in 3D and uses it to perturbatively correct the magnetic
moment.  Tests the hypothesis that the **sign** of the anomaly is
determined by mode phase structure: single-phase (1,2) → additive
(g > 2), three-phase (1,3) → subtractive (μ < 3μ_N).  Five tracks:
bare moment verification, self-potential computation, electron
correction (target: +α/2π), proton correction (target: −7%), and
analytical sign rule.  Uses existing `lib/embedded.py` infrastructure.

### R33. Ghost mode selection — why most Ma modes are dark  **Paused**
**Study:** [`R33-ghost-selection/`](R33-ghost-selection/)
**Questions:** Q77, Q34  **Type:** compute + theoretical  **Depends on:** R19, R27, R28, R31, R32

8 tracks (2 complete, 1 dead, 5 deferred).  15 findings.  The n₁ = ±1
selection rule (F1) kills 88% of modes.  The spin-statistics filter (F3,
spin = n₁/n₂) kills most of the rest.  Result: ~860 ghosts reduced to 4
per charged sheet — the (1,±1) spin-1 bosons and (1,±2) spin-½ fermions.
The (1,1) boson at half the electron mass is the critical remaining
tension: unobserved but charged with valid spin.  Track 8 (wave-optics)
found ω⁴ radiation suppression gives it ~1/16× the electron's radiation
efficiency (F10), but this is model-dependent (F14).  Track 7 (r_e scan)
is dead — the charge integral cannot pin r_e (F8).  Remaining: Track 6
(spin derivation) could change the ghost landscape entirely; Tracks 2–5
are cleanup.  Neutrino-sheet ghosts are a feature, not a bug (Q85 §8).

---

## Backlog

Ordered roughly by priority. Items get an R-number when promoted to Active.

### Flat space → curved appearance  *(Q2)*
The material space is intrinsically flat (photon sees Cartesian space), but
embedded in 3+1D with toroidal geometry.  The photon's fields project into 3D
through this embedding, producing the Coulomb-like potential.  This is now
understood as the correct physical picture (R12 F14 revised).  The explicit
field projection calculation is R13 Track 3.

### Quadrupole correction  *(Q10, depends on R6)*
The (1,2) orbit has ~2.5% field anisotropy at the rotation horizon (quantified in
S2 F5). A full charge calculation including this anisotropy may shift q/e by a few
percent. Low priority until the charge mechanism itself is settled (R13).

### Precession of torus axis  *(Q19)*
What drives axis precession, and does precession restore approximate spherical
symmetry for the electron's external field? Natural consequence of equations of
motion, or requires an external torque?

### Orbit precession and volume-filling  *(Q23)*
Does a precessing (1,2) orbit reproduce WvM's volume-filling energy flow pattern
(Fig. 2)? This would strengthen the connection between the material-dimension model
and the original WvM paper's visual picture.

### Photon absorption and excited electrons  *(Q28)*
In this model the electron IS a photon on Ma_e. When a QM electron "absorbs a photon"
and jumps to a higher level, what happens in material-dimension language? Candidate
pictures: extra energy loads into the material space as a higher harmonic; or the
material geometry reshapes to accommodate it. If periodic boundary conditions impose
discrete allowed energy increments, this should reproduce atomic spectral lines —
a strong test of the framework. See [`../qa/Q28-photon-absorption.md`](../qa/Q28-photon-absorption.md).

### String theory parallels  *(Q24, Q25)*
A string is a 1D object vibrating on material geometry; our photon is a 1D wave on
a closed geodesic. Both produce particle properties from winding and harmonics.
How deep is the analogy? Is the material-sheet model a special case of string compactification
on a torus, and does string theory's machinery (modular invariance, T-duality) apply
or constrain our model?

### KK gauge coupling on the sheared torus — resolve the Yukawa tension  *(R29 F11–F13, depends on R19)*
**Computable.**  R29 showed naive KK Yukawa corrections are 10³–10⁶×
too large for hydrogen spectroscopy.  Five resolutions proposed
(R29 F13); the most promising (Resolution B) is that massive KK
gauge modes couple with suppressed strength on the sheared torus.
**Computation:** compute the overlap integral of the electron mode
profile with each KK gauge mode on the sheared Ma_e metric, sum
the Yukawa series with the correct (non-uniform) coupling
constants, and compare to measured hydrogen 1S–2S and Lamb shift.
The r_e value that matches spectroscopy pins r_e independently
of the g−2 route.  Would also clarify whether the Yukawa tension
is a genuine problem or an artifact of the naive coupling assumption.

### W barrier height from mode reconfiguration dynamics  *(R43 F7, Q96)*
**Partially computable.**  R43 confirmed the W is a transient
cross-sheet reconfiguration, not an eigenmode.  The W mass
(80.4 GeV) is the energy
threshold for cross-sheet transitions — a barrier height in the
mode landscape.  **Computation:** model the energy cost of
continuously deforming a neutron eigenmode (1,2,0,0,1,2) into
separate proton + electron + neutrino eigenmodes on the Ma metric,
tracking the maximum energy along the reconfiguration path.
The saddle point energy should equal M_W.  Requires a path-integral
or variational approach on the 6D metric — harder than eigenvalue
problems but well-defined.

---

## Done

Studies in chronological order of completion. Key result only — see each study's
`findings.md` for the full record.

| # | Study | Key result |
|---|-------|------------|
| 1 | **S1. Toroid series** [`S1-toroid-series/`](S1-toroid-series/) | Null result. The 9% charge deficit is an artifact of geometric approximations, not a real target. |
| 2 | **S2. Toroid geometry** [`S2-toroid-geometry/`](S2-toroid-geometry/) | a/R = 1/√(πα) ≈ 6.60 gives q = e in WvM's formula. Key algebraic result, but not self-consistent (see R6). |
| 3 | **S3. Knot zoo** [`S3-knot-zoo/`](S3-knot-zoo/) | Only (1,2) produces nonzero charge. Fractional charges (e/3, 2e/3) map to specific a/R multiples. Material dimension hypothesis proposed. |
| 4 | **R1. KK charge comparison** [`R1-kk-charge/`](R1-kk-charge/) | KK gravitational charge is ~10⁻²² × e at Compton scale — ruled out. WvM mechanism is structurally different. 6D decomposition documented for reference. |
| 5 | **R2. Electron from geometry** [`R2-electron-compact/`](R2-electron-compact/) | Photon of energy m_e c² on (1,2) geodesic on Ma_e gives q = e, s = ½, g ≈ 2.0023 with zero free continuous parameters. Framework sound; numerics use S2's r = 6.60 (later revised by R6). |
| — | **R4. B-field / magnetic dipole** *(retired)* | *Not started. Answered within R2: magnetic moment is the net axial projection of B on Ma_e. No separate study needed.* |
| — | **R3. Dual visualizer** *(not a study — see [`viz/dual-torus.html`](../viz/dual-torus.html))* | Interactive 3D torus + 2D flat rectangle with synchronized photon animation. Not a research study; reclassified as a visualization tool. |
| — | **R5. Flat space → curved appearance** *(retired)* | *Not started. Subsumed by R13: deriving the 4D effective field from flat Ma via KK decomposition directly answers this question.* |
| 7 | **R6. Guided-wave field profile** [`R6-field-profile/`](R6-field-profile/) | S2's r = 6.60 is not self-consistent. Self-consistent solution: r ≈ 4.29, R ≈ 8.2 × 10⁻¹⁴ m. All profile shapes give q = e; actual profile requires solving the wave equation on Ma_e. |
| 8 | **R7. Charge from torus geometry** [`R7-torus-capacitance/`](R7-torus-capacitance/) | Coulomb field energy is ~α × target for all aspect ratios at Compton scale. WvM energy-balance approach overestimates by ~1/α. "Magic ratios" from S2/R6 were artifacts. Correct charge mechanism remains open. |
| — | **R9. Precession causes** *(number retired)* | *Number pre-assigned but study never started. Question lives on in backlog as "Precession of torus axis (Q19)".* |
| — | **R10. Precessing orbit / volume-filling** *(number retired)* | *Number pre-assigned but study never started. Question lives on in backlog as "Orbit precession and volume-filling (Q23)".* |
| 9 | **R11. Prime resonance** [`R11-prime-resonance/`](R11-prime-resonance/) | Eight tracks: no mechanism selects q = 137 from energy cost or primality. q ~ 1/α is partly tautological (follows from using e as input). Real free parameter is r (aspect ratio), not q. → R12. |
| 10 | **R12. Self-consistent fields** [`R12-self-consistent-fields/`](R12-self-consistent-fields/) | Flat Ma_e has no eigenmodes at ω_C (spectral gap ~137×). Curved geodesics give q ≈ 193 — photon sees flat space internally. Flat-for-mass / embedded-for-charge is the correct two-domain picture (not an inconsistency). Track 3 (propagation self-consistency) trivially satisfied on flat Ma_e. |
| 11 | **R13. Charge from the embedding** [`R13-kk-charge-t3/`](R13-kk-charge-t3/) | Electron is winding mode (not KK). Multi-winding (68,137) breaks WvM charge mechanism: p = 68 ≠ 1 destroys commensurability, E oscillates 67× relative to surface normal, monopole = 0 (exact). The α problem ≡ the charge mechanism problem: α ≈ 1/137 forces a tradeoff between correct Coulomb energy (R8-multi-winding) and correct charge (p = 1). → Q34. |
| 12 | **R8. Multi-winding electron** [`R8-multi-winding/`](R8-multi-winding/) | (68,137) on sheared Ma_e at r_e scale: mass ✓, spin ½ exact ✓, g = 2 ✓, R/r_e = 0.989 ✓. **Charge mechanism invalidated by R13** — R8-multi-winding breaks WvM commensurability (Q = 0). Spin/g-factor results carry over to any (1,2)-local model. q was never selected; the premise (U_Coulomb = m_e c²/2) was the wrong target (see R15). |
| 13 | **R17. Radiation pressure** [`R17-radiation-pressure/`](R17-radiation-pressure/) | Centrifugal force from confined photon's curved 3D path cannot determine α. Track 4: tube deformation preserves φ-symmetry → charge = 0. Track 5: F ⊥ v (no clumping), σ_φ = const (breathing conservative), force is a consequence of confinement. Positive: force decomposition quantified; confirms model self-consistency. |
| 14 | **R18. Torus stiffness** [`R18-torus-stiffness/`](R18-torus-stiffness/) | Geometric deformation cannot produce charge. Track 1: backwards stiffness κ = ε₀E₀²/(2R), α-independent at linear order. Track 2: Coulomb cost exceeds photon energy saving by 96×. Symmetric torus is stable. Charge integral of cos(θ+2φ) vanishes on any smooth torus. |
| 15 | **R14. Universal geometry** [`R14-universal-geometry/`](R14-universal-geometry/) | Three-photon linking model for hadrons ruled out. Charge depends on mode numbers, not spatial arrangement (F18). All redistribution mechanisms fail. Positive: spin quantization protects electron (F10); uncharged modes can add mass (F8). |
| 16 | **R20. Harmonic proton** [`R20-harmonic-proton/`](R20-harmonic-proton/) | Proton/neutron as fundamental + uncharged harmonics on Ma_e. 5 tracks, 21 findings. Harmonics exactly uncharged (F1), decay energetics match (F9), stability explained (F10), muon/tau = "hot electrons" (F17), neutrino excluded from the electron sheet (F14). Descriptive model complete; predictivity requires embedding curvature (→ R21). |
| 17 | **R16. Harmonic charge** [`R16-harmonic-charge/`](R16-harmonic-charge/) | Paused indefinitely.  R18 showed axisymmetric curvature cannot mix modes into charge — needs φ-symmetry breaking.  Superseded by R19 (shear provides the symmetry breaking).  Analytical complement to R15 never materialized. |
| 18 | **R19. Shear-induced charge** [`R19-shear-charge/`](R19-shear-charge/) | Shear breaks φ-symmetry → first mechanism producing charge from delocalized wave.  α(r,s) formula derived (Tracks 1–3).  Quark program (Tracks 4–6) ruled out: single-photon quarks from shear definitively excluded (F24, F33).  3D integral predicts electron is lightest charged particle (F31).  Free parameter r remains open (→ R15).  **Track 8 (reopened):** KK convention reconciliation — α formula re-derived under correct KK Compton constraint (F35–F43).  KK is the rigorous wave-equation result; WvM was a classical approximation.  Same charge physics, updated s(r) curve. |
| 19 | **R21. Quarks from embedding curvature** [`R21-embedding-quarks/`](R21-embedding-quarks/) | Curvature concentrates modes, lifts ±n₁ degeneracy (T1).  Charge ratios continuous, not quantized — single-torus quarks insufficient (T2).  Parity selection rule: all harmonics must be sin-like; cos-like electron is unique charged mode (T5 F12).  Selects R20 harmonic spectrum. |
| 20 | **R22. Mode coupling** [`R22-mode-coupling/`](R22-mode-coupling/) | Spectral S-L solver: curvature makes harmonics heavier (δ/n ≈ 0.26 ε²), proton mass decreases slightly (ΔM ≈ −53 m_e at r=3).  Correction monotonic in r — does not select r (F4).  θ₂ symmetry preserved by backreaction (F5) — phonon neutrino definitively ruled out.  Tracks 2–3 deferred: R22-mode-coupling matrix cannot select spectrum without nonlinear dynamics. |
| 21 | **R23. Neutrino from harmonic beating** [`R23-neutrino-beating/`](R23-neutrino-beating/) | Δm² ratio 33.6 achievable by many triplets — not selective (T1).  θ₂-momentum conservation blocks phonon mechanism (T2).  R22 F5 closes last rescue path (backreaction preserves θ₂).  Single-sheet neutrino ruled out.  Neutrino mechanism remains open. |
| 22 | **R24. Torus dynamics** [`R24-torus-dynamics/`](R24-torus-dynamics/) | 3-torus neutrinos: modes (0,0,n₃) uncharged, mass ratio 33.63 from integers alone (0.03σ), Σm = 72 meV, system over-determined → r predicted (T1 F1–F7).  Wave dynamics: defocusing nonlinearity does not select modes (T2 F8–F12).  r-selection via dynamics pre-empted (T3).  Critical open: spin of (0,0,n₃) → R25. |
| 23 | **R25. Neutrino spin** [`R25-neutrino-spin/`](R25-neutrino-spin/) | Charge-spin linkage (F4): both charge (n₁ = ±1) and spin-½ (n₁ odd) are controlled by tube winding n₁.  "Uncharged" and "fermion" are mutually exclusive — WvM cannot produce neutrinos.  3-torus kinematic success (R24 T1) blocked at spin gate.  PMNS path to r-selection closed.  Neutrino mechanism remains the central open problem. |
| 24 | **R26. Three tori — Ma** [`R26-neutrino-t4/`](R26-neutrino-t4/) | Ma = the three material sheets (electron, neutrino, proton).  Neutrino mass ratio Δm²₃₁/Δm²₂₁ = 33.6 from shear s₃₄ = 0.022 (exact, r-independent).  Charge-neutral neutron mode (0,−2,+1,0,0,+2) reproduces m_n at σ_ep = −0.091 (R27 F15–F18; supersedes the R26 candidate (1,2,0,0,1,2) at |σ_ep| ≈ 0.038).  Parameter census: 21 total, 15 free (3 aspect ratios + 12 cross-shears) — under-determined.  Casimir–mass tension (F73): vacuum energy wants maximal coupling, mass spectrum wants minimal — first candidate for a self-selecting principle.  75 findings across 4 tracks. |
| 25 | **R27. Ma oscillation patterns** [`R27-bound-states/`](R27-bound-states/) | Discovery engine finds Ma modes matching particles.  7 tracks, 54 findings.  Neutron and muon pin r_p = 8.906 and σ_ep = −0.0906 — zero free parameters at MeV scale.  Parameter-free predictions: kaon (1.2%), eta (0.6%), eta prime (0.3%), phi (0.8%).  Lifetime-gap correlation r = −0.84 supports off-resonance hypothesis.  Tau 5.6% high (structural gap). |
| 26 | **R28. Ma spectrum refinement** [`R28-particle-spectrum/`](R28-particle-spectrum/) | 4 tracks, 22 findings.  ~48 energy bands below 2 GeV, ~900 modes vs ~40 known particles — consistent with off-resonance hypothesis.  Strange baryon sign flips resolved at n_max=15.  W/Z/Higgs match trivially at high energy; Ma non-predictive above ~2 GeV.  Predictive horizon established. |
| 27 | **R29. Atoms and nuclei** [`R29-atoms-and-nuclei/`](R29-atoms-and-nuclei/) | 4 tracks, 27 findings.  Coulomb potential derived from Ma × S (α = 1/137, H E₁ = −13.6 eV).  Nuclei ARE Ma modes: scaling law n₅ = A, n₆ = 2A matches d→⁵⁶Fe to < 1%.  Deuteron 0.02% error.  Nuclear spins predicted (9/11).  Two-tier physics: Ma (MeV) / S (eV). |
| 28 | **R31. Origin of α** [`R31-alpha-derivation/`](R31-alpha-derivation/) | 6 tracks, 24 findings.  Hydrogen NOT a Ma mode (spectrum 2,830× too coarse).  Casimir energy cannot select α.  Naive KK Yukawa 10³–10⁶× too large for Lamb shift.  α remains an input; deriving it requires a moduli potential not yet in the model. |
| 29 | **R32. Running of α** [`R32-alpha-running/`](R32-alpha-running/) | 4 tracks.  Naive KK running catastrophic (157,000× SM), confirming ~10⁵ ghost suppression.  Volume dilution gives α_bare ≈ 1/5.  "Why α = 1/137?" reduces to "why s ≈ 0.01?" — shear currently reverse-engineered from α. |
| 30 | **R34. Midpoint coupling** [`R34-midpoint-coupling/`](R34-midpoint-coupling/) | 4 tracks.  Weighted gauge partition gives 1/80 = (137+24)/2 to 99.8%.  Tests bidirectional Kramers-Kronig dispersion from geometric base coupling.  Ma modes as absorption resonances modulate α upward (IR → 137) and downward (UV → 24). |
| 31 | **R35. Threshold detection** [`R35-threshold-coupling/`](R35-threshold-coupling/) | 4 tracks, 34 findings.  Threshold "continuity" is mode-hopping on ν-sheet's dense ladder.  Cd-109 Re/Rc = 33 reproduced via SCA.  Storage 10–324 bits/cell, write ~70 ps/hop, read ~3 ps.  Writing REQUIRES metabolic energy (ATP). |
| 32 | **R36. Geometric tilt** [`R36-geometric-tilt/`](R36-geometric-tilt/) | Drops KK.  Ma_e plane tilted relative to S by angle θ; α = f(θ).  EM emerges from S-projection of material-dimension momentum.  α may be a free "designer's choice" parameter. |
| 33 | **R37. Membrane mechanics** [`R37-membrane-mechanics/`](R37-membrane-mechanics/) | 12 findings.  Gravity "derivation" tautological.  KEY: constrained energy minimisation gives r ≈ 0.50 (first mechanism preferring a specific r region), decisively ruling out thin-torus geometries (r = 6.6 is 91% worse).  Anisotropic correction requires moduli potential. |
| 34 | **R38. Fourth generation** [`R38-fourth-generation/`](R38-fourth-generation/) | 5 tracks, 10 findings.  MaSt does NOT predict exactly three generations (~14,000 levels below 10 GeV).  Three generations accommodated not predicted.  Resonance capture hypothesis viable (Q ≈ 30 excludes 4th gen) but underdetermined. |
| 35 | **R39. Near-field phase** [`R39-near-field-phase/`](R39-near-field-phase/) | 6 tracks, 9 findings.  Proton's extended charge reduces Coulomb barrier by 74% at 1 fm.  Phase modulation adds ~3–14%.  Anti-phase cancellation falsified for (1,2).  No EM attraction at any orientation.  Nuclear binding requires non-EM mechanism. |
| 36 | **R40. Dynamic torus** [`R40-dynamic-torus/`](R40-dynamic-torus/) | Phase 1: GR bulk stiffness gives 10⁻⁴⁰ deformation.  Phase 2: α-impedance model — wall is (1−α) contour, 136/137 confined.  Elastic 1/k² wall response provides low-pass filter (40× suppression per n₁ step).  Dynamic Ma is perturbative (∝ α²); static model is correct zeroth order. |
| 37 | **R41. Dynamic model (full)** [`R41-dynamic-model/`](R41-dynamic-model/) | 7 tracks, 43 findings.  Refactored `lib/ma_model.py`.  Dynamic model is a CONCEPTUAL advance (elliptical cross-section, 92% mode elimination, geometric generation hierarchy) but NOT quantitative (corrections 100× smaller than structural errors).  Reproduces static to 7 sig figs.  125 unit tests pass. |
| 38 | **R42. Dark matter from ghost modes** [`R42-dark-matter/`](R42-dark-matter/) | 6 tracks, 14 findings.  Ghost modes exactly charge-symmetric (F1–F3).  DM/visible mass ratio spans 2.4–12.4 under physical filters; Planck 5.36 in the middle.  Several filters within 20% of 5.4.  Hypothesis viable; next step is projection integral W(n). |
| 39 | **R43. Weinberg angle** [`R43-weinberg-angle/`](R43-weinberg-angle/) | 4 tracks, 10 findings.  sin²θ_W matches 3/13 to −0.19% of MS-bar value.  2/9 predicts M_W = 80.420 GeV (+0.051%).  However, 3/13 is NOT derivable from Ma metric trace (F10) — at unified coupling the structural ratio is 3/15 = 1/5.  Unexplained numerical match, not a derivation.  W/Z are transient cross-sheet reconfigurations, not eigenmodes (F7). |
