# Alpha in GRID

How the fine-structure constant α fits into the GRID lattice
model — what it controls, what it doesn't, and why it is the
sole free parameter of the framework.  Assumes familiarity with
basic physics (forces, fields, waves) but not with the GRID
axioms or lattice gauge theory.

---

## 1. What is α?

The **fine-structure constant** α ≈ 1/137.036 is a dimensionless
number that measures the strength of the electromagnetic
interaction.  It governs how strongly charged particles (electrons,
protons) interact with photons.

"Dimensionless" means it has no units — it is a pure ratio.  You
get the same number regardless of whether you measure in meters,
inches, or Planck lengths.  This makes it a candidate for a truly
fundamental constant, unlike quantities like c or ℏ that depend on
your choice of units.

A few ways to think about what α measures:

- **Coupling strength:** if two electrons interact by exchanging
  a photon, the probability of that exchange is proportional to α.
  Since α ≈ 1/137 is small, electromagnetic interactions are
  relatively weak — photons are exchanged sparingly.

- **Energy ratio:** α is the ratio of the electrostatic energy
  between two charges separated by one Compton wavelength to the
  rest energy mc² of the particle.  It measures "how much does
  charge energy matter compared to mass energy?"

- **Defect energy fraction:** in the GRID lattice (see below),
  a charged particle is a topological defect — a region where
  the phase winds through a full 2π cycle.  The defect's total
  energy is the standing wave (mc²), but only a fraction α of
  that energy leaks into the surrounding lattice as Coulomb
  field.  The rest stays internal as mass.  Alpha is the
  energy tax that the ambient lattice levies on the defect.


## 2. What is GRID?

**GRID** (Geometric Relational Interaction Domain) is a theoretical
framework that derives both Maxwell's equations (electromagnetism)
and Einstein's field equations (gravity) from a single discrete
lattice at the Planck scale.  It sits beneath a companion framework
called **MaSt** (Material Space), which takes the field equations
GRID derives and uses them to build particles, masses, and charges
from confined photons on compact geometry.

The relationship:

```
GRID (substrate layer)
    Inputs:  ζ = 1/4, α ≈ 1/137
    Outputs: Maxwell's equations, G, Λ
              │
              ▼
MaSt (architecture layer)
    Inputs:  Maxwell + α (from GRID)
    Outputs: particle spectrum, masses, charges, forces
```

GRID provides the rules of the game.  MaSt plays the game.

GRID rests on **six axioms** — minimal assumptions about the
lattice:

| # | Axiom | What it says |
|---|-------|--------------|
| A1 | 4D causal lattice | Space is a regular array of cells; disturbances travel at one cell per tick (= speed of light) |
| A2 | Lorentzian signature | One dimension is time (forward only); three are space |
| A3 | Periodic phase | Each cell carries a phase θ ∈ [0, 2π) — a point on a circle |
| A4 | Local gauge invariance | Relabeling any cell's phase by an arbitrary amount doesn't change the physics, provided you adjust the connections between cells to compensate |
| A5 | Resolution ζ = 1/4 | Each cell contributes 1/4 bit to the collective information of the lattice |
| A6 | Coupling α ≈ 1/137 | The strength of the electromagnetic interaction |

A few terms that may be unfamiliar:

- **Phase** (θ): think of each cell as a tiny clock hand that
  points in a direction on a circle.  The physical content is
  not where any one clock hand points, but the *difference*
  between neighboring clock hands.

- **Gauge invariance** (A4): you can reset all the clock hands
  by different amounts at every cell, and the physics doesn't
  change — as long as you keep track of the offsets on the
  connections between cells.  This bookkeeping requirement
  *forces* the lattice to carry connection variables on its
  links, which turn out to be the electromagnetic potential A_μ.

- **Resolution** (ζ): how much information each cell contributes.
  At ζ = 1/4, it takes 4 cells to encode one bit of physical
  information.  This is an information-density limit, like an
  anti-aliasing constraint in digital imaging.


## 3. Where α enters

Of the six axioms, **Axiom A6 is the only one that contains α**.
It enters the physics at a single point: the **action** — the
quantity that the lattice extremizes to determine how fields evolve.

The electromagnetic action in natural units is:

<!-- S = −(1/4) ∫ F_μν F^μν d⁴x + e ∫ j^μ A_μ d⁴x -->
$$
S = -\frac{1}{4}\int F_{\mu\nu}F^{\mu\nu}\,d^4x
    \;+\; e\int j^\mu A_\mu\,d^4x
$$

The first term describes the energy stored in the electromagnetic
field (E and B).  It has no free parameters — its form is uniquely
fixed by the axioms (gauge invariance + Lorentz invariance +
locality).

The second term couples the field to charged matter.  The coupling
constant is the **elementary charge**:

<!-- e = √(4πα) ≈ 0.303 -->
$$
e = \sqrt{4\pi\alpha} \approx 0.303 \quad\text{(natural units)}
$$

This is the only place α appears.  It sets how strongly the
phase field (matter) couples to the connection field
(electromagnetism).  Everything else in the Maxwell derivation —
the field tensor F_μν, the E/B decomposition, charge quantization,
charge conservation, all four Maxwell equations — follows from
geometry and topology alone.

**What α controls in the lattice picture:**

| Quantity | How it depends on α |
|----------|---------------------|
| Elementary charge e | e = √(4πα) |
| Coupling constant κ | κ = 1/(4πα) ≈ 1722 |
| Photon-matter interaction strength | Proportional to α |
| Defect field energy (Coulomb) | Fraction α of the wave's total energy mc² |
| ε₀ and μ₀ (SI units) | Emerge from α + unit conversions |

In natural units, ε₀ = μ₀ = 1 and the vacuum impedance Z₀ = 1.
The SI values of ε₀ and μ₀ — which look like two independent
constants in textbooks — are both just α in different unit
disguises.  There was always only one electromagnetic constant.


## 4. What α does NOT control

This is equally important.  GRID derives gravity from a completely
separate subset of axioms, and **α plays no role in the gravity
derivation**.

The two derivations use disjoint inputs:

| | Electromagnetism | Gravity |
|--|------------------|---------|
| **Axioms used** | A1, A2, A3, A4, **A6 (α)** | A1, A2, **A5 (ζ)** |
| **Free parameter** | α ≈ 1/137 | ζ = 1/4 |
| **Mechanism** | Dynamics — gauge symmetry of phases | Thermodynamics — entropy of horizons |
| **What emerges** | Maxwell's equations, E, B, charge | Einstein's equations, G, Λ |

The gravity derivation follows Jacobson (1995): if every causal
horizon on the lattice carries entropy proportional to its area
(set by ζ), then applying basic thermodynamics (heat = temperature
× entropy change) to energy flowing through the horizon forces
the geometry to obey Einstein's field equations.  Newton's
gravitational constant falls out as:

<!-- G = 1/(4ζ) = 1 in natural units -->
$$
G = \frac{1}{4\zeta} = 1 \quad\text{(natural units)}
$$

No α anywhere.  Gravity and electromagnetism share the lattice
(A1) and the causal structure (A2), but they draw on completely
different features of it:

- **EM** uses the internal structure: phases on cells, connections
  on links, gauge symmetry.
- **Gravity** uses the information-theoretic structure: how many
  bits the lattice encodes per unit area.

This clean separation explains the **hierarchy problem** — why
gravity is so much weaker than electromagnetism.  α ≈ 1/137 is
a moderate coupling (link phases interact at every tick), while
gravity is a collective statistical effect requiring ~10⁶⁰ cells'
worth of area to become significant.  EM is a local phase
interaction; gravity is an emergent thermodynamic phenomenon.


## 5. The status of ζ versus α

GRID has two constants: ζ and α.  Their epistemic status is
different.

**ζ = 1/4** may be derivable from geometry.  The lattice geometry
investigation proposes that the cells adjacent to a causal horizon
are tetrahedra (3-simplices in 3D space).  Each tetrahedron has
4 face-sharing neighbors.  Under a counting scheme where the cell
carries no separate internal state — its information is entirely
in its boundary relationships (the "cell IS its edges" model) —
each cell contributes 1 bit per 4 neighbors, giving ζ = 1/4.

If this geometric argument holds, **ζ is derived, not free**, and
α becomes the sole free parameter of the entire framework.

**α ≈ 1/137** is measured, not derived.  GRID takes it as input.
The compact-dimensions investigation tested whether wrapping a
2D triangular lattice into a torus (like rolling graphene into
a nanotube) could constrain α through discrete geometry.  The
result: α is achievable for a wide range of wrappings.  The
lattice provides the menu of possible values, but does not
select which one nature chose.

The honest conclusion:

> α is a designer's choice within the available discrete steps.
> The lattice permits it.  Something else — energy minimization,
> topology, or a principle we haven't identified — selects it.


## 6. Can α be derived?

Several attempts have been made, both within GRID and elsewhere.

**Within GRID (compact-dimensions study):** a 2D triangular
lattice wrapped into a torus is described by four integers
(n₁, m₁, n₂, m₂), analogous to the chiral vectors of carbon
nanotubes.  These integers determine the torus geometry —
aspect ratio and shear — which in MaSt's framework determines α.
Computational enumeration found:

- α = 1/137 first appears at the **3-cell torus** (6 triangles,
  1.5 bits) — the smallest torus that supports weak coupling at
  all.  Below 3 cells, only strong coupling (α > 1) is possible.

- The 1/137 and 1/128 (Z-mass energy scale) matches share the
  **same tube direction** (−2,−1), differing only in ring length.
  This is consistent with the "running" of α (its variation with
  energy scale) being a geometric effect — the same structure
  probed at different resolutions.

- But the solution space is dense.  With wrapping integers on the
  order of 10²² (realistic for the electron sheet), the achievable
  α values are spaced ~10⁻⁴⁴ apart — effectively continuous.
  Any value is achievable.

**In standard physics:** α has resisted derivation for a century.
Eddington famously tried (and failed) to show α = 1/136 from
pure numerology.  The Standard Model takes α as a measured input —
one of about 19 free parameters.  If GRID + MaSt reduces that
count to **one**, that would be remarkable progress even without
explaining the one.

**Open question Q2** in GRID's foundations asks whether ζ and α
might be related — perhaps through a Nyquist-like consistency
condition matching the lattice resolution to the signal bandwidth.
If such a relation existed, the free-parameter count would drop
to zero.  This is noted but not assumed.

**Losinets does not provide a route either.**  The companion K–V
continuum framework (see `reference/losinets-trilogy.md`) has one
dimensional EM input — a viscoelastic relaxation time R = η₀/G —
and an obvious question is whether α = f(R · ω_Planck) for some
clean dimensionless combination.  Working the algebra through
Losinets's own EfD §7.4 correspondence table gives the
unconditional result α = π·ρ₀·r₀²·ℏ / (m_vac²·c), in which **R
does not appear**.  α and R sit on orthogonal axes of the K–V
parameter space; reducing them to one knob requires solving an
open Losinets problem (the ring-energy closure that would fix
m_vac), and even then introduces r₀ as a second knob.  Full
derivation, dimensional audits, and a corrected Planck-scale
estimate R ≈ t_P are in [`../grid/alpha-vs-R.md`](../grid/alpha-vs-R.md).
**Take-away:** Losinets's substrate equivalence with GRID does
not collapse the free-parameter count — α remains the sole
measured input on the GRID/MaSt side, independent of R.


## 7. Alpha as impedance mismatch: the bridge from GRID to MaSt

The discussion so far has treated α as an abstract coupling
constant — a number in an equation.  This section gives it a
physical picture by connecting the GRID substrate to the MaSt
particle model.

### Particles as topological defects

In MaSt, a particle is not a point.  It is a **photon confined
to a 2D sheet** (a triangular lattice) that is wrapped into a
torus and embedded in the 3D spatial lattice.  The electron, for
example, is a circularly polarized standing wave circulating on
a torus whose minor radius is at the Compton scale (~10⁻¹³ m).

This torus is a **topological defect** in the 3D lattice.  The
phase of the standing wave winds through a full 2π cycle as it
goes once through the tube of the torus.  From the perspective
of the ambient 3D lattice, that 2π winding cannot be smoothed
away — it is a permanent twist in the phase field.  Gauss's law
detects this twist as electric charge.  The winding number (how
many times the phase wraps) is the charge quantum number: +1
for a positron, −1 for an electron, 0 for a neutrino.

The torus also carries a second independent winding — twice
around the ring — which produces the magnetic moment.  The
ratio of tube windings (1) to ring windings (2) gives the
particle's spin: 1/2.

So a single confined photon on a torus, through topology alone,
generates charge, magnetic moment, and spin.  No additional
properties need to be attached to the particle.

### Two grids, one junction

Now consider what happens at the boundary where the 2D sheet
meets the 3D ambient lattice.  These are **two different grid
fabrics** with different structures:

| Property | 2D sheet (Ma) | 3D ambient (S) |
|----------|---------------|-----------------|
| Lattice type | Triangular | Tetrahedral |
| Neighbors per cell | 3 | 4 |
| Resolution ζ | 1/4 | 1/4 (or 1/5) |
| What it carries | Standing wave (particle mass) | Coulomb field, gravitational field |

The standing wave on the sheet carries the particle's full
rest energy mc².  But the 3D lattice doesn't see all of that
energy.  It sees only what **couples through the junction**
between the two grids — and what couples through is the
topological winding, which appears as a static electric field.

This is an **impedance mismatch**.  When a wave encounters a
boundary between two media of different structure, only a
fraction of the energy transmits; the rest stays internal.
The same principle applies here: the 2D sheet and the 3D
lattice are two different media, and the winding on the sheet
projects into the ambient lattice with a coupling efficiency
that is less than unity.

### The exact energy ratio

The numbers bear this out precisely.  For a particle of mass m:

- **Internal energy** (on the sheet): E_wave = mc², the full
  rest energy of the standing wave.  This is the Compton energy,
  related to the Compton wavelength by E = ℏc/ƛ_C.

- **External energy** (in the 3D Coulomb field, evaluated at
  the Compton scale): E_Coulomb = e²/(4πε₀ƛ_C) = α mc².

The ratio is exact:

<!-- E_Coulomb / E_wave = α -->
$$
\frac{E_{\text{Coulomb}}}{E_{\text{wave}}} = \alpha
$$

Only a fraction α ≈ 1/137 of the wave's energy appears in the
ambient lattice as Coulomb field energy.  The remaining 136/137
stays on the sheet — circulating as the standing wave that
constitutes the particle's mass, invisible to the 3D lattice
except through its gravitational effect.

This is what α *is* in the GRID + MaSt picture: **the
transmission coefficient at the junction between the 2D
material sheet and the 3D spatial lattice**.  It measures how
efficiently a topological winding on the sheet couples energy
into the ambient grid.

### Why this matters

In standard physics, α is a measured constant with no known
origin — it appears in the Lagrangian and that's that.  The
impedance-mismatch picture changes the question:

- **Old framing:** "Why does α have the value 1/137?  Where
  does this number come from?"

- **New framing:** "Two lattices of different dimensionality
  and structure interface at a junction.  What is the geometric
  transmission coefficient?"

Alpha is not an independent property of the particle.  It is
**inherited from the substrate** — a consequence of how the
2D sheet and the 3D lattice couple at their boundary.  The
electron doesn't "have" a coupling constant; it lives on a
sheet whose geometry determines how its internal winding
projects into ambient space.

GRID does not yet predict the value of α from this picture.
The junction geometry depends on the lattice structures, the
embedding, and possibly the wrapping integers of the torus —
all of which are under investigation.  But the conceptual
shift is significant: α stops being a mysterious free
parameter of nature and becomes a **geometric property of
the interface between two grid fabrics**.


## 8. What α controls downstream (via MaSt)

GRID derives the field equations.  MaSt takes those equations plus
α and builds particles from confined photons on compact geometry.
In MaSt, α's influence cascades:

- **Elementary charge** e = √(4πα) — the charge carried by an
  electron or proton.

- **Particle masses** — standing-wave modes on compact torus
  geometry, whose energy levels depend on α through the charge
  mechanism.

- **The strong force** — hypothesized as unscreened internal EM
  at the overlap range of proton-scale geometry (Q95).  If
  correct, strong coupling is not a separate force but EM at
  short range, governed by α.

- **The Weinberg angle** — the mixing parameter of the electroweak
  force.  MaSt finds sin²θ_W ≈ 3/13, matching experiment to
  −0.19% (R43), though the origin of this match is not yet
  derived from the geometry.

- **Dark matter candidates** — ghost modes (Ma eigenstates without
  EM coupling) reinterpreted as charge-neutral dark matter,
  with a mass-weighted ratio that brackets the observed dark/
  visible ratio of 5.36 (R42, Q94).

The entire observable universe of particles, forces, and structure
traces back through MaSt to α.  GRID provides the stage; α sets
the lighting.


## 9. Summary

| Question | Answer |
|----------|--------|
| What is α? | The dimensionless electromagnetic coupling constant, ≈ 1/137 |
| Where does it enter GRID? | Axiom A6 — the energy cost of a topological defect |
| What does it control? | All of electromagnetism: charge, coupling strength, ε₀, μ₀ |
| What doesn't it control? | Gravity — which uses ζ, not α |
| Is it derived? | No — it is the sole measured input |
| Could it be derived? | Open question — the lattice permits many values; a selection principle is unknown |
| Why does it matter? | It is the single free parameter of the GRID + MaSt framework; everything observable traces back to it |

The GRID framework derives Maxwell's equations, Einstein's field
equations, Newton's gravitational constant G, the cosmological
constant Λ, charge quantization, and charge conservation — all
from geometry.  The only thing it cannot derive is why α has the
value it does.

If ζ is confirmed as a geometric consequence of the lattice
packing, then α is the **one number** that separates a complete
geometric theory of physics from a set of empty lattice axioms.
Everything else is structure.  Alpha is the setting.
