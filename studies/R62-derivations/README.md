# R62: Derivations

**Status:** Tracks 1–4 complete; Track 5 framed (Program 1)
**Type:** theoretical (analytical, no scripts required)
**Depends on:** [primers/kaluza-klein.md](../../primers/kaluza-klein.md)
  (KK derivation of Lorentz force from 5D metric), R59 (Clifford
  torus / flat 2-torus geometry), model-E (target particle
  inventory for verification)

---

## Scope

R62 is a home for analytical derivations within MaSt — proofs,
constructions, and "from first principles" extensions of well-
known results. Each derivation is a **program** with its own
sequence of tracks. New programs can be added over time; tracks
within each program are added one at a time using the same
add-as-needed convention as R59/R60/R61.

**Program 1 (active): Electron from light.** Generalize Kaluza-
Klein theory from a 1D compact dimension to a 2-torus, replace
the test particle with a photon, and derive the electron's mass,
charge, spin, and magnetic moment as outputs of the same
geometric machinery.

Future programs (any number) will be added as new sections below
when needed.

---

## Program 1 — Electron from light

### Objectives

Kaluza-Klein theory (KK), in its original 1921–1926 form, derived
electromagnetism as the projection of a 5D metric into 4D
spacetime. The derivation is exact and well-respected. But KK
treated its "object" — the test particle moving along a 5D
geodesic — as a particle with prescribed mass m. KK derived
**charge** as the compact-direction momentum, but **mass, spin,
and magnetic moment** were inputs, not outputs.

Program 1 asks: **can we replace KK's massive test particle with
a photon (a null trajectory in higher dimensions), generalize the
compact direction from 1D to a 2-torus, and derive the electron's
mass, charge, spin, and magnetic moment as outputs of the same
geometric machinery?**

The conceptual move is short to state but consequential:

> **A photon's compact-direction momentum becomes 4D rest mass.**

Mathematically: if the (4+N)D momentum is null, p^A p_A = 0, then
the projected 4D momentum satisfies

<!-- p^μ p_μ = -|p_compact|² → m² c⁴ = |p_compact|² c² -->
$$
p^\mu p_\mu = -|p_{\text{compact}}|^2
\quad\Rightarrow\quad
m^2 c^4 = |p_{\text{compact}}|^2\,c^2
$$

A confined photon has rest mass equal to its compact momentum
times c. KK's result that "charge = compact momentum" generalizes
to "(charge, mass, …) = (compact momenta on different windings)."

This aligns directly with MaSt's existing structure. Each MaSt
sheet is a 2-torus with two windings (n_tube, n_ring). If the
photon's compact momentum is shared between these two windings,
**one winding could give charge and the other could give mass** —
both derived from a single null-trajectory ansatz, not postulated
separately.

### The "1D + 1D = 2D" framing

A clean way to motivate the photon-on-a-2-torus picture is to
notice that two independent textbook results, each living in one
compact dimension, give two of the four electron quantum numbers:

| Compact geometry | Object | Derived quantity | Source |
|---|---|---|---|
| 1D linear cavity | Standing-wave photon | **Rest mass** m = nh/(Lc) | Special relativity (Track 1A) |
| 1D circle (compact direction) on top of 4D | Geodesic with compact momentum | **Electric charge** q = p_compact / k | KK (primer Appendix A) |

Each of these uses **one** compact dimension and derives **one**
property. A 2-torus (two compact dimensions woven together) is
the natural place to ask:

- Can both derivations run side-by-side, with one winding giving
  mass and the other giving charge?
- Does the cross-coupling between the two windings (the off-
  diagonal entry of the 2×2 internal metric — what MaSt already
  calls **shear**) introduce a *third* derived quantity (spin /
  intrinsic angular momentum)?

Program 1 attempts both. Track 1 establishes the foundational
1D-linear half (mass from confinement). Pool item **a** does the
KK 2-torus construction. Pool item **b** runs the mass derivation
on the 2-torus. Pool item **d** runs the charge derivation on the
2-torus. Pool item **f** asks whether the cross-coupling produces
spin.

### Quantum-number assignment (the program in four lines)

The cleanest way to state Program 1's hypothesis is to read off
which feature of the 2-torus is responsible for which observed
quantity:

| Geometric feature | Derived quantity | Mechanism |
|-------------------|------------------|-----------|
| **Ring winding** (n_ring) | **Rest mass** | Standing-wave photon along the ring (Track 1B → MaSt μ formula via pool c) |
| **Tube winding** (n_tube) | **Electric charge** | KK compact-direction momentum on the Ma–St-coupled axis (pool d) |
| **Cross-coupling** (s and ε together) | **Spin** | Holonomy / parity of windings on the sheared 2-torus (pool f, hypothesis) |
| **Charge + spin** | **Magnetic moment** | Automatic via Lorentz covariance (E and B come as a matched set in F_μν); Dirac analog gives g = 2 (pool g, trivial corollary) |

A few notes on this assignment:

1. **The mass-from-ring assignment is electron-specific.** The
   MaSt mass formula has *both* windings contributing
   (μ² = (n_t/ε)² + (n_r − n_t s)²). For the electron-like
   geometry (large ε, "long ring, short tube") the ring term
   dominates and "ring creates mass" is essentially exact. For
   the proton-like geometry (small ε, "short ring, long tube")
   the tube term dominates instead. Program 1 is framed around
   the electron, so the table reads naturally; the proton case
   is recovered as a parameter limit, not a separate mechanism.
2. **The tube-as-charge assignment is universal.** MaSt's charge
   formula Q = −n_1 + n_5 uses only tube windings on the e and
   p sheets, with no dependence on aspect ratio or shear. This
   is the cleanest of the four lines and the most directly tied
   to KK's original derivation.
3. **The ratio-as-spin assignment is the program's central
   hypothesis** (pool item f). Standard physics derives spin from
   spinor representations of the Lorentz group; this program
   instead looks for spin as a topological / holonomy property
   of a sheared 2-torus. If it works, the parity of n_tube
   (MaSt's empirical spin rule) is recovered as a Berry-phase
   condition.
4. **The "moment follows from charge" line is essentially free
   once the prior three lines are in place.** Maxwell's equations
   show that charge and angular momentum *must* couple via the
   field tensor F_μν — E and B always come as a matched set
   under Lorentz transformations. So the magnetic moment is not
   an independent thing to derive; it's a corollary. The Dirac
   equation analog on the 2-torus should give g = 2 for free,
   with anomalous corrections (g − 2) potentially derivable from
   higher-mode contributions to the standing wave (a stretch
   goal, not a Program 1 commitment).

### What KK derived (and what it didn't)

The primer covers the full derivation. For framing purposes:

| Quantity | KK derived? | How |
|----------|:-----------:|-----|
| EM potential A_μ | Yes | Off-diagonal metric g_μ5 |
| Electric charge | Yes | Momentum in compact dimension |
| Charge quantization | Yes | Periodicity of compact dimension |
| Charge conservation | Yes | Noether's theorem on translation symmetry |
| Lorentz force | Yes | Geodesic equation in 5D |
| Maxwell's equations | Yes | Einstein equations applied to off-diagonal block |
| **Mass values** | **No** | Test particle had prescribed m |
| **Spin** | **No** | Test particle was scalar |
| **Magnetic moment** | **No** | No spin → no magnetic moment |
| **Internal structure** | **No** | Particle treated as point |

Program 1's targets are precisely the four "no" rows.

### Why a photon, not a massive particle

KK's test particle was a massive particle moving along a timelike
geodesic in 5D. Its 5D 4-momentum satisfied p^A p_A = -m_5² c²
with m_5 the 5D rest mass — already a postulated quantity.

If we instead postulate a **photon** (null trajectory) in higher
dimensions:

<!-- p^A p_A = 0 -->
$$
p^A p_A = 0
$$

then there is no rest mass to begin with. The 4D rest mass arises
purely from the projection: when momentum exists in the compact
directions, the apparent 4D 4-momentum has timelike norm
p^μ p_μ = −|p_compact|² × c². Rest mass becomes a *derived*
quantity, equal to compact momentum / c.

This is the central methodological move of Program 1. It is not
novel in cosmology (it appears in Wesson's "induced matter
theory" / "space-time-matter program"), but it has not, to our
knowledge, been combined with a 2-torus compactification and used
to derive the full electron quantum-number profile from a single
geometric ansatz.

### The Klein scale issue (acknowledged up front)

Klein's original derivation predicts compact-dimension momenta on
the order of the Planck scale, giving particle masses of ~10¹⁹
GeV — wildly different from the electron mass. This is the
well-known "mass hierarchy problem" of traditional KK.

MaSt avoids this by treating the compact dimensions as **larger**
than KK's Planckian compactification (sheet circumferences in the
fm range, set empirically by particle masses rather than by the
KK requirement R = ℏ/(ec)) and the standing-wave momenta as
**small integers** rather than excitation modes of a Planck-scale
spectrum.

This is a model choice, not a derived result. Program 1 will
state it explicitly in the appropriate track and treat it as the
starting geometric scale, without trying to derive it from first
principles in this study.

### Scope: analytical only

Program 1 is a derivation program. All work is symbolic /
analytical; no numerical scripts are needed for the core path.
Tracks produce mathematical derivations in markdown (with TeX
equations following the project notation convention from
CLAUDE.md), not computational results.

If a later track wants to verify a derivation against existing
numerical results (e.g., compare to model-E's particle masses),
it may use scripts for that single verification, but the
derivation itself stays in markdown.

### Execution plan

Tracks are added one at a time. Only the currently-executing
track is numbered; candidates for "next track" live in the pool
below as lettered items and get numbered when chosen. This keeps
the plan responsive to what each derivation actually establishes.

#### Track 1 — Mass from a confined photon

**Goal.** Establish, from special relativity alone, that a
photon confined to a finite spatial region has rest mass and
inertia in the cavity rest frame. Two complementary
constructions are run, both giving the same mass formula but
each isolating a different aspect:

| Part | Confinement | What it isolates |
|------|-------------|------------------|
| **A — Linear** | Two mirrors a distance L apart | Rest mass + **translational inertia** (resistance to acceleration) |
| **B — Circular** | Photon orbiting a 1D ring of circumference L | Rest mass + **rotational inertia** (resistance to torque, gyroscopic stability) |

Both parts produce m = nh/(Lc) for the lowest n. Part B
additionally produces a quantized angular momentum L_z = nℏ
which previews — but does not yet derive — the spin tracks
later in the program.

This is the foundational lemma for every subsequent track in
Program 1. With it in hand we can take "standing-wave photon =
rest-mass particle with inertia" as established and focus
later tracks on the genuinely new geometric content (compact
windings, cross-couplings, etc.).

##### Part A — Linear cavity (light clock)

**Strategy.**

Use Einstein's light-clock setup, but at rest:

- Two perfectly reflecting mirrors a distance L apart, normal
  to the z-axis, both at rest in frame F.
- A photon bounces between them along z, with wavelength λ
  such that 2L = nλ for some positive integer n (standing-
  wave condition).
- The photon has 4-momentum p^μ = (E/c, 0, 0, ±p_z) with
  E = p_z c (massless particle).
- Build the time-averaged stress-energy of the bouncing photon
  and compute its rest-frame energy density and total energy.
- Show that the **total** time-averaged 4-momentum of the
  confined-photon system is (E_total/c, 0, 0, 0) — i.e.,
  timelike, with vanishing spatial momentum because the +p_z
  and −p_z contributions cancel.
- Apply the rest-mass identity m² c⁴ = E_total² − |**p**|² c²:
  with |**p**| = 0, the system has rest mass m = E_total/c².
- For a single photon in steady-state confinement, this gives
  m = hf/c² = h/(λc) — the Compton relation read in the
  opposite direction (mass from frequency, not the other way
  around).

**The inertia argument (status quo is least costly).**

Beyond the bookkeeping above, Part A makes inertia explicit:

1. The standing-wave configuration is a *stationary* solution
   of the wave equation in the cavity. Its energy is constant
   in time — it is the least-action / least-cost steady state
   for the given boundary conditions.
2. Accelerating the cavity (pushing one mirror) changes the
   boundary conditions while the photon is mid-flight,
   Doppler-shifting the photon on each subsequent reflection
   and pumping work into or out of the cavity.
3. The work required to change the cavity's velocity by Δv is
   exactly (m c²) × γ corrections — i.e., the system resists
   acceleration with the same coefficient (m) that appears in
   the rest-mass identity.
4. Therefore the same m that came out of the energy bookkeeping
   *is* the inertial mass: it both describes the rest energy
   *and* quantifies the resistance to acceleration. Inertia
   is not a separate postulate — it follows from the standing-
   wave being the minimum-energy state for fixed boundary
   conditions.

**Tactics.**

1. **Setup.** State the geometry (two mirrors at z = 0 and
   z = L, photon bouncing in z with reflections that conserve
   energy and reverse z-momentum). State the standing-wave
   boundary condition 2L = nλ.

2. **4-momentum bookkeeping.** Write down the photon's 4-momentum
   on each leg of its bounce. Show that the time-averaged
   spatial momentum is zero (because each leg of duration L/c
   contributes equal and opposite p_z).

3. **Rest mass identification.** Apply
   m² c⁴ = E² − |**p**|² c² to the time-averaged 4-momentum.
   Show m = E/c².

4. **Wavelength connection.** Use E = hf = hc/λ for the
   photon. Get m = h/(λc). For the lowest standing-wave mode
   (n = 1, λ = 2L), this gives m = h/(2Lc) — the rest mass
   is set by the cavity length.

5. **Inertia argument.** Push one mirror. Show via Doppler
   bookkeeping that the work done equals (1/2) m v² + O(v⁴),
   recovering Newtonian inertia at low v and the relativistic
   form at all v. This proves the m from step 3 is the
   inertial mass, not just an energy label.

6. **Bridge to compact dimensions.** Note that the argument
   doesn't depend on the cavity being made of mirrors. Any
   mechanism that confines a photon to a finite spatial region
   produces the same result. In particular: if the photon is
   confined to a **compact direction** (a circle of
   circumference L, no mirrors needed — periodicity does the
   confining), the standing-wave condition is L = nλ, and the
   rest mass becomes m = nh/(Lc). This is the bridge to KK.

##### Part B — Circular cavity (spinning photon on a 1D ring)

**Strategy.**

Replace the two mirrors with a circular 1D ring of
circumference L. The photon now orbits the ring instead of
bouncing between mirrors:

- The photon's 4-momentum is tangent to the ring, with
  magnitude E/c. Its spatial momentum points along the
  azimuthal direction φ.
- Standing-wave condition (single-valuedness around the ring):
  L = nλ for positive integer n.
- The photon now carries **angular momentum**
  L_z = r × p = (L / 2π) × (E/c) = nℏ at the n-th mode.
- The total energy is the same as Part A (E = nhc/L), so the
  rest mass is the same: m = E/c² = nh/(Lc).
- But unlike Part A, the spatial momentum **does not cancel**
  in time-average: it traces a closed circle. The time-averaged
  *linear* momentum vanishes (the ring is symmetric), so the
  rest-mass identity still gives m = E/c². But the angular
  momentum about the ring axis is nonzero and quantized.

**Why this matters.**

1. **Same mass, with intrinsic angular momentum.** Part A's
   linear cavity gives mass alone. Part B's ring gives mass
   *plus* a quantized angular momentum. This is the first
   place in the program where a "spin-like" quantity appears
   from pure geometry — without postulating a spinor field,
   without invoking Pauli matrices, just from confining a
   photon to a 1D loop.

2. **Rotational inertia / gyroscopic stability.** A spinning
   confined photon resists changes to its rotation axis the
   same way a spinning top does. Tilting the ring requires
   work proportional to the angular momentum × tilt rate.
   The system has *rotational* inertia in addition to
   *translational* inertia. Both are derived from the same
   E = mc² + the orbital geometry.

3. **Holds its position.** A free spinning top in vacuum
   maintains its orientation in space — that's gyroscopic
   stability. A spinning-photon system would similarly
   maintain its orientation. This is suggestive (not
   conclusive) of why elementary particles have well-defined
   spin axes that don't dephase under small perturbations.

4. **Foreshadow but do not commit.** Part B does *not* claim
   to derive the topological spin rule (odd tube windings →
   spin ½) or to identify L_z = nℏ with the electron's spin.
   Those derivations belong in pool item **f** (spin from
   the 2×2 torus metric), where the cross-coupling between
   tube and ring windings becomes available. Part B simply
   establishes that "confined-photon angular momentum" is a
   well-defined geometric quantity, ready to be used.

**Tactics.**

1. **Setup.** Photon orbiting a ring of radius r = L/(2π),
   tangent 4-momentum, single-valuedness boundary condition
   L = nλ.

2. **Momentum bookkeeping.** Show the time-averaged linear
   momentum is zero (symmetry); the total angular momentum
   is L_z = nℏ.

3. **Rest mass.** Same calculation as Part A: m = nh/(Lc).

4. **Gyroscopic-inertia argument.** Apply a torque to tilt
   the ring axis. Show via standard rigid-body / classical
   mechanics that the work required is proportional to
   L_z × (tilt rate)² × t, recovering the moment-of-inertia
   law. Spin angular momentum and gyroscopic resistance
   come out of the same calculation.

5. **Note the key difference from Part A.** Linear cavity
   gives mass + linear inertia. Ring cavity gives mass +
   linear inertia + angular momentum + rotational inertia.
   The ring has *one more* output for *zero* extra postulates
   — geometry alone delivers it.

##### Combined deliverable

- `track1.md` — full derivation written out with TeX equations,
  containing both Part A and Part B, including the 4-momentum
  bookkeeping, the rest-mass identity, the inertia arguments,
  the angular momentum quantization on the ring, and the
  bridge to compact-dimension confinement (Part A step 6).
- `findings.md` entries:
  - F1: "A photon confined to a linear cavity of length L by a
    standing-wave boundary condition has rest mass
    m = nh/(Lc) and inertia identical to a Newtonian point
    mass at the rest-frame energy. Inertia follows from the
    standing-wave being the minimum-cost steady state."
  - F2: "A photon orbiting a circular 1D ring of circumference
    L has rest mass m = nh/(Lc) (same as F1) plus a quantized
    angular momentum L_z = nℏ and rotational inertia
    proportional to L_z. The system exhibits gyroscopic
    stability — it 'holds its position' under small
    perturbations, like a spinning top."
  - F3 (interpretive): "1D linear confinement → mass.
    1D circular confinement → mass + intrinsic angular
    momentum. This sets up the program's main move: combine
    both confinements on a 2-torus and add KK's compact-
    direction charge derivation to get all three (mass,
    angular momentum, charge) from one geometric setup."

**Acceptance criteria.**

- The Part A derivation uses only special relativity and the
  standing-wave boundary condition. No QM, no GR, no KK.
- The Part B derivation uses only special relativity, the
  standing-wave boundary condition, and elementary classical
  rotational mechanics.
- The result m = nh/(Lc) is shown to follow exactly (not as
  an approximation) in both parts.
- Part A's bridge to compact dimensions (step 6) is stated
  explicitly enough that subsequent tracks can invoke "Track
  1 lemma" without re-deriving.
- Part B's angular momentum quantization L_z = nℏ is shown
  to follow from the single-valuedness boundary condition,
  not assumed.

**Possible outcomes.**

- **Clean derivations.** Both parts succeed; the program has
  a solid foundational lemma. Pool items b/c can take
  "standing-wave photon = rest-mass particle with inertia"
  as established. Pool item f has a concrete classical
  precedent for "geometric angular momentum" to point back
  to.
- **Subtlety encountered.** If something doesn't go through
  cleanly (e.g., the "rest mass" of a single photon is zero
  by Lorentz invariance, even when confined — only the
  cavity-photon system as a whole has rest mass), document
  the subtlety carefully. This actually clarifies what KK is
  doing: KK's "mass = compact momentum" is a property of the
  *projected particle*, not a Lorentz-invariant intrinsic
  mass.
- **Part B alone is questionable.** Part B's gyroscopic
  argument relies on the photon being well-localized to the
  ring. If quantum delocalization makes that picture
  problematic, Part B may need to be reframed as a
  semi-classical limit. Document and proceed with Part A as
  the rigorous result; treat Part B as motivational.

**Why this is the right first track.** Even if every later
pool item in this program fails, Track 1 alone is a concise
statement of why "photon confined to a compact dimension" is
a legitimate model for a massive particle. It removes the
most common objection to the photon-on-torus picture
("photons are massless") by showing that the objection
conflates intrinsic Lorentz-invariant mass (zero for a free
photon) with the rest-frame energy of a bound system
(nonzero for a confined photon). It also establishes inertia
as a *consequence* of the standing-wave being the minimum-
cost steady state, not as a separate postulate.

**Status.** Complete.  See [derivation-1.md](derivation-1.md)
for the full step-by-step proof; lemma F1–F3 stated at the end.

---

#### Track 2 — Kaluza-Klein on a 2-torus (promoted from pool item **a**)

**Goal.** Generalize the primer's Appendix A derivation from one
compact dimension (a circle) to two compact dimensions (a
2-torus). Identify all the new off-diagonal metric entries —
the eight spacetime↔compact entries g_μ4 and g_μ5 (giving a
U(1)×U(1) gauge structure with two potentials A_μ and B_μ) and
the one compact↔compact entry g_45 (the internal shear with no
analog in 5D KK). Re-derive the Christoffel symbols, the 6D
geodesic equation, and the projection to 4D. Catalog which
results generalize cleanly from 5D KK and which are
structurally new on the 2-torus.

The test particle in this track remains a **massive** particle
moving along a 6D timelike geodesic, exactly as in the primer.
Replacing it with a photon (null trajectory) is the next pool
item; this track does the geometric/algebraic groundwork so
that move can be made cleanly.

**Strategy.** Mirror the primer's Appendix A structure step by
step, with one compact dimension replaced by a 2-torus. The
6×6 metric splits into three blocks:

- A 4×4 spacetime block g_μν.
- A 2×2 internal block g_ab with a, b ∈ {4, 5}, containing
  the two compact diagonals g_44, g_55 and one off-diagonal
  entry g_45 (the shear).
- A 4×2 mixed block g_μa containing the two gauge potentials.

Apply the cylinder condition (∂_4 = ∂_5 = 0 on all metric
components), compute the inverse metric, derive Christoffel
symbols organized by index type, write the 6D geodesic
equation, and project to 4D. The 5D KK case must be recovered
as the limit g_55 → 0 (or by setting the second compact
direction to a single point).

**Tactics.**

1. **Setup.** Coordinates, ranges, the 6×6 metric ansatz with
   explicit identifications of A_μ, B_μ, and the shear s.
2. **Inverse metric.** Block-matrix inversion. The 2×2 internal
   block with off-diagonal g_45 must be inverted in closed
   form; this is where the shear first contributes
   nontrivially.
3. **Cylinder condition.** State and apply ∂_4 = ∂_5 = 0 on
   all metric components.
4. **Christoffel symbols.** Compute, organized by index
   structure:
   - Pure spacetime Γ^μ_νρ — like 4D GR plus A·A and B·B
     corrections.
   - Mixed Γ with one compact index — these are where the
     field strengths F^A_μν and F^B_μν live.
   - Mixed Γ with two compact indices — these contain the
     shear contributions.
5. **6D geodesic.** Write down d²x^A/dτ² + Γ^A_BC ẋ^B ẋ^C = 0
   for the massive test particle.
6. **Conserved compact momenta.** Cylinder condition + Killing
   directions in x_4 and x_5 → two conserved quantities,
   identified as charges Q_A and Q_B.
7. **4D projection.** Project the spacetime components of the
   geodesic. Recover the Lorentz force from each U(1)
   independently, plus a shear-induced cross-term coupling
   the two charges.
8. **Interpretation of the shear.** Show that g_45 ≠ 0 mixes
   the two charges at the geodesic level; specifically, an
   eigenstate of pure-x_4 momentum carries nonzero x_5
   covariant momentum proportional to s. Connect this to the
   MaSt mass formula μ² = (n_t/ε)² + (n_r − s n_t)² in
   advance of pool item c.

**Deliverable.** `derivation-2.md` — full step-by-step
derivation following the format of derivation-1.md, with each
step's purpose annotated and key results boxed.

**Acceptance criteria.**

- Each step uses only differential geometry + the cylinder
  condition. No KK results are *assumed*; the 5D KK case is
  derivable as a limit.
- The two U(1) potentials A_μ and B_μ are explicitly
  identified, and shown to give independent Maxwell-like
  fields when the shear is zero.
- The shear g_45 is shown to produce a *specific*, named
  coupling term in the 4D projection — distinct from anything
  appearing in 5D KK.
- The 5D KK limit (drop the second compact direction)
  reproduces the primer Appendix A result exactly.
- The "compact momentum = charge" identification from the
  primer extends naturally to two charges (one per U(1)).

**Possible outcomes.**

- **Clean generalization.** Everything from 5D KK extends
  term-by-term; the shear contributes one well-defined extra
  coupling. Pool items b, d, f have a solid metric structure
  to build on.
- **Inverse-metric subtleties.** The 2×2 internal block with
  off-diagonal g_45 has a nontrivial inverse; if this
  introduces unexpected complications (e.g., singularities
  when |s| approaches a critical value), document them as
  constraints on viable shear values.
- **Shear interpretation surprise.** The g_45 term might
  produce something other than naive "two-charge mixing" —
  e.g., an effective topological coupling or a Berry-phase-
  like correction. If so, flag it as a candidate spin
  precursor for pool item f.

**Status.** Complete.  See [derivation-2.md](derivation-2.md);
lemma F4–F6 stated at the end.

---

#### Track 3 — Photon on a 2-torus: 4D mass from compact momentum (promoted from pool item **b**)

**Goal.**  Replace Track 2's massive test particle with a null
trajectory (a photon) in the same 6D geometry.  Apply Track 1's
lemma — that a confined photon system has rest mass equal to
its energy divided by c² — to read off the 4D rest mass as the
magnitude (in the internal metric) of the conserved 6D compact
momentum vector (P_4, P_5).  In the canonical case (no shear,
equal-radii 2-torus) the result is the **Pythagorean mass
formula** m c = (h/L) √(n_4² + n_5²); the general case is a
quadratic form m²c² = h^ab P_a P_b that is the seed of MaSt's
mass formula.

**Strategy.**  The 6D null condition G_AB k^A k^B = 0 splits
into a 4D part g_μν k^μ k^ν and a compact part g_ab w^a w^b.
The 4D part is exactly the 4D mass-shell relation
g_μν p^μ p^ν = −m²c² when read with p^μ = ℏ k^μ (the projected
4-momentum of the particle as seen by a 4D observer).  So the
projected rest mass squared is the compact-direction quadratic
form g_ab w^a w^b — and using Track 2's conservation laws
P_a = g_ab w^b, this becomes h^ab P_a P_b.  The Track 1 lemma
provides the conceptual bridge: just as a photon between
mirrors has rest mass = E/c² in the rest frame of the mirrors,
a photon constrained to the 2-torus has rest mass = (compact
energy)/c² in the rest frame of the 4D observer.

**Tactics.**

1. State the 6D null condition for a photon: G_AB k^A k^B = 0.
2. Confirm conservation of P_4 and P_5 still holds for null
   trajectories (Killing's theorem applies regardless of
   timelike vs null character).
3. Decompose the null condition into spacetime + compact +
   mixed parts using the metric ansatz from Track 2.
4. Identify the spacetime part with the 4D mass shell
   g_μν p^μ p^ν = −m²c²; read off m²c² = g_ab w^a w^b.
5. Convert the kinetic w^a to conserved P_a using
   w^a = h^ab P_b: m²c² = h^ab P_a P_b (the **general mass
   formula**).
6. Specialize to the canonical case (g_ab = δ_ab, no shear):
   recover the Pythagorean mass m²c² = P_4² + P_5².
7. Apply standing-wave quantization (P_a = n_a h/L_a from
   derivation-2 D.4): get the discrete mass spectrum
   m = (h/Lc)√(n_4² + n_5²).
8. Apply Track 1's Lorentz-boost argument to confirm the
   projected rest mass behaves inertially — same as the
   linear-cavity and 1D-ring cases, with the cavity now being
   the 2-torus.
9. Note the connection to the MaSt mass formula
   μ² = (n_t/ε)² + (n_r − s n_t)² in the general (sheared,
   asymmetric-radii) case, deferring the full identification
   to the next pool item.
10. Discuss interpretation: the projected particle is
    simultaneously massive and electrically charged in 4D,
    even though its 6D form is a null trajectory — exactly the
    "electron from light" picture this program is testing.

**Deliverable.**  `derivation-3.md` — full step-by-step
derivation in the same format as derivations 1 and 2.

**Acceptance criteria.**

- The 6D null condition is stated explicitly and decomposed
  cleanly.
- The mass formula m²c² = h^ab P_a P_b follows from the
  decomposition with no additional assumptions beyond what
  Tracks 1 and 2 established.
- The Pythagorean special case is shown to follow exactly (not
  as an approximation) when g_ab = δ_ab.
- The standing-wave quantization gives a discrete mass
  spectrum on the 2-torus, with explicit formula.
- The inertial-mass argument from Track 1 is confirmed to
  apply unchanged in the 2-torus case.
- The "preview of MaSt formula" subsection states what is
  derived now and what is deferred to pool item c, with no
  hand-waving across the boundary.

**Possible outcomes.**

- **Clean derivation.**  The mass formula falls out of one
  identity (decomposition of G_AB k^A k^B = 0), Pythagorean is
  a one-line corollary, and the MaSt connection is structural.
  Pool items c, d, f all proceed with the mass formula in
  hand.
- **Sign/normalization subtleties.**  The exact relationship
  between the conserved Killing momentum and the operationally
  defined "electric charge" might require a unit choice that
  affects the prefactor in m²c² = h^ab P_a P_b.  Document any
  such choice transparently.
- **The "photon-on-torus = electron" claim is robust.**  This
  derivation should make the central claim of Program 1 hold
  up to scrutiny: the 4D projection of a 6D null trajectory
  with nonzero compact momentum is a 4D massive charged
  particle, not a 4D photon.

**Status.** Complete.  See [derivation-3.md](derivation-3.md);
lemma F7–F10 stated at the end.

---

#### Track 4 — Recovery of the MaSt mass formula (promoted from pool item **c**)

**Goal.**  Derive MaSt's empirically-found mass formula

<!-- μ² = (n_t/ε)² + (n_r − s n_t)² -->
$$
\mu^{2} \;=\; (n_{t}/\varepsilon)^{2}
        \;+\; (n_{r} - s\,n_{t})^{2}
$$

from the photon-on-2-torus mass formula m²c² = h^ab P_a P_b
(F7) by choosing an explicit parametrization of the 2×2
internal metric in terms of the aspect ratio ε and shear s.
This closes the loop that started in Track 1 (confined photon
gives rest mass), passed through Track 2 (KK on a 2-torus
gives the metric structure), and Track 3 (photon-on-torus gives
the structural mass formula), by reducing it to the exact form
that model-D / model-E currently postulate.

This is the central deliverable: the **MaSt mass formula is no
longer a postulate** — it is a derived consequence of GR with
two compact dimensions plus the Planck–Einstein relation.

**Strategy.**  The general mass formula h^ab P_a P_b expands
to a quadratic form in (P_4, P_5) with coefficients set by
g_44, g_55, g_45.  MaSt's formula has the same structure but
written in (n_t, n_r) with parameters (ε, s).  Find the
parametrization of g_ab in terms of (ε, s) that matches MaSt's
formula identically, term by term, then verify by completing
the square (or equivalently by direct substitution).  Identify
which compact direction is "tube" and which is "ring" in the
process.

**Tactics.**

1. State the two formulas side by side: F7's general
   (h^ab P_a P_b) and MaSt's empirical (μ²).
2. Apply standing-wave quantization (P_4 = n_4 h/L_4, etc.) to
   convert F7 into a function of integer quantum numbers.
3. Choose the natural parametrization: declare the "tube" to
   be the smaller compact direction and the "ring" to be the
   larger; introduce ε ≡ L_ring/L_tube as the aspect ratio.
   Write g_44, g_55, g_45 in terms of (ε, s).
4. Substitute into m²c² = h^ab P_a P_b and simplify.
5. Show the result is exactly MaSt's μ² = (n_t/ε)² +
   (n_r − s n_t)² up to a unit prefactor that fixes the
   overall mass scale (the Compton scale of the sheet).
6. Identify what the shear s "geometrically is" in this
   picture: it is the off-diagonal entry of the 2×2 internal
   metric, normalized to be dimensionless.  This was sketched
   in Track 2; here it is pinned down operationally as the
   specific number that appears in MaSt's formula.
7. Tabulate the lowest few mass eigenvalues for an example
   (ε, s) — e.g., the electron-sheet values from R49 — to
   verify the formula reproduces the known particle inventory
   in the right order.

**Deliverable.**  `derivation-4.md` — full step-by-step
derivation in the same format as derivations 1–3.

**Acceptance criteria.**

- The parametrization g_ab(ε, s) is stated explicitly and
  motivated geometrically (not pulled from MaSt by reverse
  engineering).
- The substitution into m²c² = h^ab P_a P_b yields MaSt's
  formula identically — every coefficient and every cross-term
  matches.
- The unit prefactor (the overall mass scale of the sheet) is
  identified with a clear physical interpretation (e.g., the
  Compton momentum of the tube circumference).
- The "tube" / "ring" naming is fixed by a stated convention
  (smaller / larger compact direction), not by reverse-
  engineering from charge identification.
- A worked numerical example confirms the formula reproduces
  R49's mass spectra.

**Possible outcomes.**

- **Exact match.**  MaSt's formula falls out cleanly from a
  natural parametrization.  Model-D / model-E's mass-formula
  postulate is now derived from first principles.  This is the
  expected outcome.
- **Match up to a normalization choice.**  The formula matches
  in form but with a different overall prefactor than MaSt's
  empirical fit.  Document the choice and note that the
  prefactor is degenerate with the choice of length unit
  (i.e., what we call L_tube).
- **Form mismatch.**  The natural parametrization gives a
  quadratic form that does not reduce to MaSt's exact (n_r −
  s n_t)² combination — it might yield (n_r − s n_t)² /(1−s²)
  or some other variant.  This would mean MaSt's formula is
  *almost* but not exactly KK on a 2-torus, and we would need
  to characterize the discrepancy.  Either way, the result is
  informative.

**Status.** Complete.  See [derivation-4.md](derivation-4.md);
lemma F11–F13 stated at the end.  **Outcome: exact match.**
The parametrization g_44 = ε², g_55 = 1/ε² + s², g_45 = ε s
(with det g = 1, and the convention 4 = tube, 5 = ring,
L_5 = ε L_4) reduces F7 identically to MaSt's formula.  An
unexpected by-product: MaSt's "shear" parameter s is *not*
the same as derivation-2's dimensionless shear s_geom; they
are related by s_geom = ε s / √(1 + ε² s²), which means
s_geom is automatically bounded |s_geom| < 1 for any real
(ε, s) — the positivity constraint of derivation-2 is
manifest in this parametrization.

---

#### Track 5 — Charge identification (promoted from pool item **d**)

**Goal.**  Show that the conserved Killing momentum P_4 of F4
(the one in the *tube* direction, by Track 4's convention) is
the **electric charge** Q of the projected 4D particle, when
the convention

<!-- g_μ4 ≠ 0 (tube couples to spacetime),  g_μ5 = 0 (ring does not) -->
$$
g_{\mu 4} \neq 0 \;\;\text{(tube couples to spacetime)},
\qquad
g_{\mu 5} = 0 \;\;\text{(ring does not)}
$$

is adopted.  Show that with standing-wave quantization, Q is
automatically integer-quantized in units of an elementary charge
e set by the tube period.  Generalize to MaSt's three-sheet
T⁶ setup to recover the empirical universal charge formula

<!-- Q = -n_1 + n_5  (electron-sheet tube minus proton-sheet tube; neutrino tube neutral) -->
$$
Q \;=\; -n_{1} + n_{5}
$$

where n_1 = electron-sheet tube winding, n_3 = neutrino-sheet
tube winding (does not appear because σ_νS = 0), n_5 =
proton-sheet tube winding.

This is the **charge counterpart** of Track 4 (mass): together,
the two derivations give the full mass-and-charge picture of
the electron-from-light hypothesis on a single sheet, and the
extension across MaSt's three sheets is just bookkeeping with
sign conventions.

**Strategy.**

1. Start from F4–F6: U(1)×U(1) gauge structure on a 2-torus,
   two conserved compact momenta P_4 and P_5.
2. Adopt the **tube-couples convention**: g_μ4 ≠ 0, g_μ5 = 0.
   This zeros the second gauge potential (B_μ = 0 from F4) and
   leaves only one physical gauge field A_μ ∝ g_μ4.
3. Note that P_5 remains conserved by Killing's theorem
   (independent of whether g_μ5 = 0), but P_5 is now
   "decoupled from spacetime" — it contributes to mass (via the
   F11 quadratic form) but not to any 4D Lorentz force.  P_5
   is a *dark conservation law*: real, but invisible.
4. Identify Q with P_4.  Apply the F4 D.4 standing-wave
   quantization to get Q = e × n_t with e the elementary
   charge unit (set by the tube period L_t).
5. Generalize to T⁶ = T² × T² × T² (three 2-tori, one per
   MaSt sheet, no cross-shears for now).  Each sheet has its
   own (P_tube, P_ring) and its own per-sheet Ma–S coupling
   sign σ_e, σ_ν, σ_p.
6. Apply MaSt's empirical sign assignments: σ_νS = 0 (neutrino
   neutral), σ_eS = −1 (in normalized units), σ_pS = +1.
   This gives Q = −n_1 + n_5 with n_3 absent.

**Tactics.**

1. Recap F4 D.2 (Killing momenta) and F4 E.2 (Lorentz force
   from g_μa).
2. Set g_μ5 = 0 explicitly; show A_μ from F4's expansion
   reduces to a single gauge potential built from g_μ4 alone.
3. Show that the Lorentz-force term of F5 reduces from
   Q_A F^Aμ_ν + Q_B F^Bμ_ν to Q F^μ_ν (single force, single
   charge).
4. Apply F4 D.4 (standing-wave quantization) to get
   Q = (units factor) × n_t.
5. Identify the units factor as the elementary charge e.
   Discuss how its value relates to the GRID coupling
   constant α.
6. Assemble the three-sheet picture: one (P_tube)_sheet per
   sheet, summed with sign σ_sheet.  Verify: with σ_e = -1,
   σ_ν = 0, σ_p = +1, get Q = -n_1 + n_5.
7. Discuss matter/antimatter as sign(n_t) and particle
   identity as which sheet's tube is excited.

**Deliverable.**  `derivation-5.md` — full step-by-step in the
same format as derivations 1–4.

**Acceptance criteria.**

- The tube-couples convention is stated explicitly with its
  motivation (basis choice + empirical input that there is no
  second EM force).
- The reduction U(1)×U(1) → U(1) is shown algebraically.
- The Killing momentum P_4 → Q identification is unambiguous.
- The standing-wave quantization Q = e × n_t is derived, not
  postulated.
- The generalization to MaSt's Q = -n_1 + n_5 is mechanical
  given the sign conventions, with σ_e, σ_ν, σ_p called out
  as one-time choices (not derived).
- The neutrino's neutrality is shown to follow from σ_νS = 0,
  not from some intrinsic property of the neutrino sheet.

**Possible outcomes.**

- **Clean derivation.**  Q falls out of P_4 with no additional
  postulates beyond the tube-couples convention and the
  per-sheet Ma–S coupling signs.  The expected result.
- **Sign ambiguities.**  The signs (σ_e < 0, σ_p > 0) might
  not be derivable from the geometry alone — they may be
  inherited from MaSt as empirical inputs.  Document this
  transparently.
- **Charge unit determination.**  The elementary charge e
  might or might not be derivable from L_t and the other
  metric parameters.  If derivable, this connects to GRID's
  derivation of α.  If not, document e as an additional
  parameter (the overall coupling strength of the surviving
  U(1)).

---

### Next-track pool

Candidates after Track 1. Sequence decided as we go. Each
entry is a sketch; the chosen one is elaborated to full-track
detail when promoted.

**a. ~~KK derivation on a 2-torus.~~** Promoted to Track 2;
see derivation-2.md.

**b. ~~Photon-on-torus: 4D mass from compact momentum.~~**
Promoted to Track 3; see derivation-3.md.

**c. ~~Recovery of the MaSt mass formula.~~** Promoted to
Track 4; see derivation-4.md.

**d. ~~Charge identification: tube as the charge-carrying
winding.~~** Promoted to Track 5; see derivation-5.md.

**e. Lorentz force on the standing-wave state.**
Generalize the primer's Appendix A geodesic projection to the
case where the test particle is a standing-wave eigenstate
(not a free particle moving along a single geodesic). Show
that the Lorentz force still emerges, with the charge q =
compact momentum in the charge-carrying direction, and the
mass m = total compact momentum (per pool item c). This is the
cleanest demonstration that mass, charge, and the Lorentz
force coupling all come from the same geometric source.

**f. Spin from the 2×2 internal torus metric (the cross-coupling
hypothesis).**
Build the 2×2 metric of the torus alone, apply KK's derivation
rules, and see whether spin "falls out" as a consistency
requirement. The rough idea: the torus has an off-diagonal entry
(the shear s), which by KK's analogy is a U(1) gauge potential
**internal to the torus**. The holonomy of parallel transport
around the two cycles of the torus produces a phase that depends
on the **ratio** of the windings (n_tube and n_ring) and the
metric coupling between them (s and ε together).

Working hypothesis: for windings where the holonomy phase
accumulates to π × (odd integer) over a full transport cycle,
the wavefunction picks up a sign on a 2π rotation — the
defining property of a spin-½ object. The parity-of-n_tube
rule that MaSt currently postulates would then be the
algebraic statement of this condition.

Track 1 Part B (spinning photon on a 1D ring) provides
classical precedent for "geometric angular momentum" that this
track builds on: a single-loop standing wave gives integer
L_z = nℏ; cross-coupling two loops via shear opens the door to
half-integer values via the holonomy phase.

This pool item is the highest-risk highest-reward item.
Standard physics derives spin from spinor representations of
the Lorentz group, which is technical. The cross-coupling idea
bypasses that route by looking for a topological / metric
origin of spin. It may work; it may not. Either way, the
result is informative.

**g. Magnetic moment as a corollary of charge + spin.**
Once charge (pool d) and spin (pool f) are derived from the
same 2-torus geometry, the magnetic moment is essentially
automatic. The reason is structural, not technical: in 4D
Minkowski space E and B are unified into a single antisymmetric
tensor F_μν, and they always come as a matched set under
Lorentz transformations. A particle with charge **and** angular
momentum *must* couple to B with a moment proportional to its
spin — there is no Lagrangian consistent with Lorentz
covariance that allows charge + spin without a magnetic moment.

The work in this pool item is therefore mostly bookkeeping:
take the standing-wave eigenstate from pool b/d/f, apply a
weak external EM field, and read off the moment coefficient.
The Dirac-equation analog on the 2-torus should yield g = 2 at
the lowest order with no free parameters. Anomalous corrections
(g − 2) might be derivable from higher-mode contributions to
the standing wave (a stretch goal — connects to R44).

This pool item is *trivial-to-medium* if f succeeds, and
unaddressable if f does not. Its difficulty is gated entirely
by f.

**h. Cross-shears between two 2-tori (4D internal).**
Extend the geometry from one 2-torus to two 2-tori with
cross-shears between them. Show that compound modes (modes
spanning both tori) emerge as eigenstates of the joint metric.
This is the analytical version of what R54 did numerically.
Predicts that the structural results (which compound modes
exist, how cross-shears mediate inter-sheet couplings) follow
from the metric algebra.

**i. Full 6D MaSt with three 2-tori and all cross-shears.**
The final extension: three 2-tori (electron, neutrino, proton
sheets) with all 12 cross-shear entries. Show that the
resulting 4 + 6D structure recovers the full MaSt particle
inventory. This is mostly bookkeeping once tracks a–h are in
place, but it is the deliverable that proves the program
reaches all the way to the existing model-E predictions.

**j. Klein quantization at non-Planck scales.**
Address (or formally postpone) the mass hierarchy issue.
Document why MaSt's compact dimensions are sized to give ~MeV
particles rather than ~GeV (Planck) particles, what
mathematical changes this entails relative to traditional KK,
and what is still open about the choice. Likely outcome:
documented as an inherited constraint, not solved here.

**z. Closeout for Program 1.** Synthesize the tracks. If mass
+ charge + Lorentz force are derived (a–e succeed), promote
the result to a primer appendix or its own primer ("MaSt as
photon-on-torus"). If spin also is derived (f succeeds), this
becomes a substantial theoretical contribution. If spin is
not derived, document the specific blocking constraint and
flag the topological-spin rule as still postulated. Either
way, summarize what model-E now inherits as derived versus
postulated.

---

### Notes on structure (Program 1)

The tracks form a natural dependency tree:

```
                          Track 1 (light clock + ring)
                                      │
                                      ▼
                              a (KK on 2-torus)
                                      │
                      ┌───────────────┼───────────────┐
                      ▼               ▼               ▼
                  b (mass)         d (charge)      f (spin?)
                      │               │               │
                      ▼               │               ▼
                  c (μ formula)       │           g (mag mom)
                      │               │               │
                      └───────┬───────┘               │
                              ▼                       │
                      e (Lorentz force)               │
                              │                       │
                              └───────┬───────────────┘
                                      ▼
                         h (two 2-tori + cross-shears)
                                      │
                                      ▼
                         i (full 6D MaSt; matches R54)
                                      │
                                      ▼
                                z (closeout)
```

Tracks b, d, f are independent given track a, so they can be
ordered as we go. Track e depends on b and d. Track g depends
on f. Tracks h and i are sequential consolidation steps that
integrate everything earlier.

The user's two specific suggestions map to:
- **Light-clock + spinning-photon argument** → Track 1
  (framed in detail above)
- **Spin from 2×2 torus metric** → Pool item f (sketched;
  framed in detail when promoted)

The user's "1D + 1D = 2D" framing is captured in the
Objectives section above and motivates the sequence
(a → b/d in parallel → e on the 2-torus combines them).

---

## Files

| File | Purpose |
|------|---------|
| README.md | This framing document |
| derivation-1.md | Track 1 — mass and angular momentum from a confined photon (complete) |
| derivation-2.md | Track 2 — Kaluza-Klein on a 2-torus (complete) |
| derivation-3.md | Track 3 — photon on a 2-torus, 4D mass from compact momentum (complete) |
| derivation-4.md | Track 4 — recovery of the MaSt mass formula (complete) |
| derivation-5.md | Track 5 — charge identification: tube as the charge-carrying winding (in progress) |
| scripts/ | Optional verification scripts (not expected to be needed for analytical tracks) |

Future programs (Program 2, Program 3, …) will add their own
derivation files under a clear prefix when needed.