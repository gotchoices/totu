# GRID Foundations

The axioms, notation, and free parameters of the Geometric Relational
Interaction Domain.

## Notation and conventions

| Symbol | Meaning | Value (natural units) |
|--------|---------|----------------------|
| L | Lattice grain size (= Planck length) | 1 |
| c | Propagation speed (one cell per time step) | 1 |
| ℏ | Reduced Planck constant | 1 |
| k | Boltzmann constant | 1 |
| ζ | Resolution — bits per Planck cell | 1/4 |
| α | Fine-structure constant | ≈ 1/137.036 |

"Natural units" throughout GRID means c = ℏ = k = 1, with L = 1
defining the length scale.  The Planck length is the grain size,
not a derived quantity.

**Convention:** all GRID derivations work in natural units.  SI
conversions are deferred to the end and clearly marked when they
appear.

---

## The axioms

Six statements.  The first four define the lattice structure.  The
fifth sets the information content.  The sixth sets the interaction
strength.

### A1. Four-dimensional causal lattice

Space is a regular array of identical cells in four dimensions.
Each cell has a characteristic size L (the grain size).

Disturbances propagate from cell to cell at one cell per time step.
This propagation speed, in the continuum limit, is the speed of
light c.

*This axiom gives us: dimensionality (4), a length scale (L),
and a speed (c = L/τ where τ is the time step).*

### A2. Lorentzian signature (1,3)

Of the four lattice dimensions, exactly one is **timelike** — it
carries a causal ordering.  Information flows forward along this
dimension only.  The remaining three dimensions are spatial and
have no preferred direction.

In the continuum limit, the metric signature is (−, +, +, +).
The minus sign on the time component is not put in by hand — it
is the statement that the causal dimension behaves differently
from the spatial ones.

*This axiom gives us: the distinction between time and space,
the light-cone structure, and the impossibility of backward
signaling.*

### A3. Periodic internal phase

Each cell carries an internal degree of freedom: a **phase**
θ ∈ [0, 2π).  This is the simplest possible compact continuous
variable — a point on a circle.

The phase is not directly observable.  Only **phase differences**
between neighboring cells have physical meaning.

**Phase oscillates freely.**  Time always advances (A2), but
the phase at each cell can increase or decrease on any given
tick.  This back-and-forth oscillation is the wave content of
the lattice — without it, there are no oscillating fields and
no wave propagation.  The time derivative of phase (θ̇) is
the electric field in the temporal gauge; its oscillation
between positive and negative values produces the alternating
E and B of an electromagnetic wave.  When phase accumulates
past 2π and wraps, this topological carry is the microscopic
mechanism of charge quantization.

*This axiom gives us: U(1) symmetry (the circle group), and the
seed from which electromagnetic gauge structure will grow.*

### A4. Local gauge invariance

The physics is unchanged under arbitrary local relabeling of the
phase:

<!-- θ(x) → θ(x) + χ(x) for any smooth function χ -->
$$
\theta(x) \;\to\; \theta(x) + \chi(x)
$$

for any smooth function χ(x).  Since only phase differences
matter (A3), a *uniform* shift is trivially irrelevant.  Gauge
invariance extends this to *non-uniform* shifts: even if I
relabel each cell's phase by a different amount, the physics
must remain the same — provided I simultaneously adjust the
**connection** between cells to compensate.

This compensating connection, in the continuum limit, is the
electromagnetic four-potential A_μ.  It is part of the grid's
state, stored on the **links** between cells (not on the cells
themselves).  A_μ is not a new parameter — it is dynamic memory
on each link, determined by the equations of motion.  Its
existence is *forced* by gauge invariance; its dynamics produce
the electromagnetic field.  A propagating disturbance in the
link states is a photon
(see [maxwell.md](maxwell.md) for the full derivation).

*This axiom gives us: the gauge field A_μ, from which the
electromagnetic field tensor F_μν is constructed.*

### A5. Information resolution ζ = 1/4

Each cell contributes ζ = 1/4 bit to the collective information
content of the lattice.  Equivalently: it takes 1/ζ = 4 cells to
encode one bit of physical information.

**Geometric origin:** ζ follows from the face count of the
simplicial cells adjacent to a causal horizon.  A horizon is
a 2D surface in 3D space.  The 3D cells touching the horizon
are tetrahedra (3-simplices).  Each tetrahedron has 4
face-sharing neighbors.

In the "cell = its edges" model (Model B in
[lattice-geometry.md](lattice-geometry.md)), the cell carries
no separate internal state — its information is entirely
encoded in the standing-wave modes on its boundary edges.
There is no "self" to count, only the 4 neighbors:

- 4 face-sharing neighbors → 4 contributors per bit
- **ζ = 1/4**

This matches the Bekenstein-Hawking factor.  The 1/4 is not
imported from black hole physics but derived from the
dimensionality (3D tetrahedra) and packing (simplicial) of the
cells adjacent to the horizon.  (See also
[compact-dimensions.md](compact-dimensions.md) for the compact
dimension perspective.)

A causal horizon of area A (measured in Planck units, L = 1)
carries entropy:

<!-- S = ζ · A = A/4 -->
$$
S = \zeta \cdot A = \frac{A}{4}
$$

No single cell holds a complete bit.  The bit is a collective
property of a patch of ~4 cells — like a pixel requiring a
2×2 sub-pixel grid to resolve.  This is an anti-aliasing
constraint: no excitation can have spatial frequency higher
than 1/(4L).

The resolution ζ directly determines the gravitational constant:

<!-- G = 1/(4ζ) = 1 in natural units -->
$$
G = \frac{1}{4\zeta} = 1 \quad \text{(natural units)}
$$

This is derived, not postulated — see [gravity.md](gravity.md).

*This axiom gives us: the entropy bound, the Planck area, the
gravitational constant, and the UV cutoff of the lattice.*

### A6. Electromagnetic coupling α ≈ 1/137

The energy cost of a minimal topological defect (a vortex — a
region where the collective phase winds through a full 2π) relative
to the natural lattice energy scale is set by a single dimensionless
number: the fine-structure constant α.

In the lattice action, α appears as the inverse of the coupling
constant κ:

<!-- κ = 1/(4πα) ≈ 1722 -->
$$
\kappa = \frac{1}{4\pi\alpha} \approx 1722
$$

so the electromagnetic Lagrangian density is:

<!-- L = −(1/4) κ F_μν F^μν = −1/(16πα) F_μν F^μν -->
$$
\mathcal{L} = -\frac{1}{4}\,\kappa\, F_{\mu\nu}F^{\mu\nu}
             = -\frac{1}{16\pi\alpha}\, F_{\mu\nu}F^{\mu\nu}
$$

From α, all electromagnetic quantities follow:

| Quantity | Expression | Natural units |
|----------|------------|---------------|
| Elementary charge e | √(4πα) | ≈ 0.3028 |
| Permittivity ε₀ | 1 | 1 |
| Permeability μ₀ | 1 | 1 |
| Impedance Z₀ | √(μ₀/ε₀) | 1 |

In SI units, ε₀ and μ₀ acquire their familiar values through the
unit conversions c, ℏ, and the definition of the ampere.  Their
apparent independence is an artifact of SI — they encode the same
single parameter α.

*This axiom gives us: the strength of electromagnetism, the value
of the elementary charge, and (through the lattice action) the
dynamics that produce Maxwell's equations.*

---

## The ℵ-line (aleph line)

Each edge of the lattice carries a 1D compact internal
dimension — a sub-Planck degree of freedom orthogonal to
the 2D spatial grid.  This is the **ℵ-line** (aleph line).

| Property | Value |
|----------|-------|
| Dimensionality | 1D (compact, periodic) |
| Length | L_compact (particle-dependent; for an electron, ≈ 10¹⁹ L_P) |
| Lowest mode | Phase θ / gauge connection A_μ (axiom A3) |
| Higher modes | Standing waves that carry entropy and internal state |
| Visibility to grid | **None** — the hexagonal cell acts as a low-pass filter (width 1.822 L_P < Nyquist 2 L_P) |

The ℵ-line is where particle identity lives.  The grid
(spatial lattice) handles propagation and curvature; the
ℵ-line handles mass, charge, and internal quantum numbers.
The hexagonal cell geometrically filters the ℵ-line from
the grid scale — the Planck length is the resolution of
the grid, not of nature.

The ℵ-line is distinct from MaSt's compact dimensions (the
2D Ma sheets where particles reside as standing waves).  The
Ma sheets are higher-level structures built from many grid
edges; the ℵ-line is the internal dimension of each
individual edge.

A helpful mental model: each edge is a zig-zag truss whose
end-to-end length is 1 L_P (rigid) but whose internal path
length is L_compact (much longer).  Longitudinal standing
waves on the truss are the ℵ-line modes.  See
[INBOX.md](INBOX.md), "The truss model for internal strings."

---

## What the axioms produce

| Emergent structure | From which axioms | Where derived |
|--------------------|-------------------|---------------|
| Maxwell's equations | A1–A4, A6 | [maxwell.md](maxwell.md) |
| Charge quantization | A3 (phase periodicity) | [maxwell.md](maxwell.md) |
| Gravitational constant G | A1, A5 | [gravity.md](gravity.md) |
| Einstein field equations | A1, A2, A5 | [gravity.md](gravity.md) |
| Spacetime stiffness c⁴/(8πG) | A1, A2, A5 | [stiffness.md](stiffness.md) |
| Arrow of time | A2, A5 | [gravity.md](gravity.md) |
| Speed of light | A1 (lattice propagation) | Given by construction |
| E and B field decomposition | A2 (signature splits F_μν) | [maxwell.md](maxwell.md) |
| ε₀ = μ₀ = 1 (natural units) | A1, A6 | [maxwell.md](maxwell.md) |

---

## What the axioms do NOT produce

These require additional structure beyond the minimal lattice:

- **The value of α** — the coupling is a measured input, not
  derived.  GRID takes α ≈ 1/137.036 as given.  This is the
  sole free parameter of the framework.

- **Non-abelian gauge groups** — the U(1) symmetry of axiom A3
  gives electromagnetism.  The SU(2) × SU(3) structure of the
  weak and strong forces requires richer internal degrees of
  freedom.  This is outside GRID's scope (and largely handled by
  MaSt's compact geometry).

- **Particle masses** — these are MaSt's domain.  GRID provides
  the field equations; MaSt provides the compact geometry that
  confines photons into massive particles.

---

## Open questions at the foundations level

**Q1. Does the tensor window size matter?**

A smooth tensor field (10 independent components, each requiring
meaningful precision) cannot live in a single cell that holds only
ζ = 1/4 bit.  The tensor description is a **sliding window** over
many cells — roughly ~4000 cells (~8 Planck lengths across) by
a naive estimate.  This window size may follow from ζ alone, or
it may be derivable from macro-scale observables, or it may be
an independent parameter.  We leave this aside unless the Maxwell
or G derivations require it.

**Q2. Are ζ and α related?**

Both are treated as independent inputs.  It is conceivable that
they are connected by a consistency condition (e.g. a Nyquist-like
constraint matching resolution to signal bandwidth), which would
reduce the free parameters to one.  This is noted but not assumed.

**Q2b. Are α and Losinets's R related?**

Losinets's K–V continuum theory has one electromagnetic input,
the relaxation time R = η₀/G = ν₀/c² (units: seconds).  GRID's
α (dimensionless) and Losinets's R (a time) are the natural
candidates for a one-dial-to-one-dial bridge.

**Short answer: no, unless Losinets's photon §2.4 open problem is
solved.**  Direct algebra using the EfD §7.4 K–V correspondence
gives α = π·ρ₀·r₀²·ℏ / (m_vac²·c), in which R does not appear at
all — α depends on the substrate parameters (ρ₀, r₀, m_vac) and
universal constants.  R lives on an orthogonal axis of the K–V
parameter space; it sets dissipation and the SI-unit conversion
A = R·u, but cancels from the dimensionless coupling.

A conditional bridge α ∝ r₀² / (ρ₀·R⁶·c⁷) emerges *if* the
Losinets ring-energy closure (m_vac in terms of c, G, ν₀) is
ever solved, but introduces r₀ as a second knob.  See
[`alpha-vs-R.md`](alpha-vs-R.md) for the full derivation,
dimensional audits, and a corrected Planck-scale estimate
R ≈ t_P (the trilogy's earlier "≈ 1.5 × 10⁻¹²⁶ s" guess was
a unit-mixing error).

**Q3. Does the lattice require 4 dimensions?**

Axiom A1 asserts 4D.  Could a self-consistent causal lattice with
holographic entropy exist in other dimensions?  If 4 is the unique
consistent choice, one axiom becomes a theorem.

**Q4. Is the (1,3) signature derivable?**

If the causal structure (forward-only information flow) is the
fundamental input, does exactly one timelike dimension follow?
Some approaches to quantum gravity (Euclidean quantum gravity)
suggest the signature emerges from a phase transition.
