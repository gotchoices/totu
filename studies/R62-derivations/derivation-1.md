# Derivation 1 — Mass and angular momentum from a confined photon

**Program 1, Track 1.**  Foundational lemma for the photon-on-
torus program.  We prove that a photon confined to a finite
spatial region has rest mass in the cavity rest frame, identify
that rest mass as inertial mass (resistance to acceleration), and
in the circular case show that the orbital angular momentum is
quantized in units of ℏ.

---

## Inputs

The whole derivation uses only:

1. **Special relativity.** A free photon has 4-momentum p^μ
   satisfying p^μ p_μ = 0 (null trajectory).
2. **The Planck–Einstein relation** for a photon's energy:
   E = hf = hc/λ.  This is the one quantum input — Planck
   1900 / Einstein 1905 — and it is needed only to convert
   between wavelength and energy.
3. **Standing-wave boundary conditions** appropriate to each
   geometry (single-valuedness on a closed region).
4. **Conservation of momentum** at boundaries (mirror reflections
   conserve energy and reverse the normal component of momentum).
5. **Lorentz invariance of the 4-momentum** (4-vectors transform
   as 4-vectors between inertial frames).

No quantum mechanics beyond E = hf.  No general relativity.  No
Kaluza–Klein.  Metric signature is (−, +, +, +) throughout, so
that p^μ p_μ = −E²/c² + |**p**|² = 0 for a free photon.

---

## Part A — Linear cavity at rest (the light clock)

### Goal

Show that a photon bouncing between two parallel mirrors in
their rest frame F has rest mass m = nh/(2Lc), where L is the
mirror separation and n indexes the standing-wave mode.  Then
show that the same m governs how the cavity-photon system
responds to acceleration — i.e., m is the inertial mass.

### A.1 — Geometric setup

> *Purpose: fix coordinates and the boundary condition.*

Two perfectly reflecting mirrors lie at z = 0 and z = L, normal
to the z-axis, both at rest in inertial frame F.  A single photon
bounces along the z-axis between them.  The mirrors do no net
work on the photon (perfect reflection: each bounce reverses
p_z but leaves |p_z| unchanged).

The standing-wave boundary condition — the requirement that the
photon's phase return to itself after a full round trip — is

<!-- 2L = n λ,  n ∈ ℤ⁺ -->
$$
2L = n\,\lambda, \qquad n \in \mathbb{Z}^+.
$$

This is the same condition as for a vibrating string fixed at
both ends.  Each round trip covers distance 2L; for steady state,
this distance must equal an integer number of wavelengths.

### A.2 — Photon 4-momentum on each leg of the bounce

> *Purpose: write down the explicit 4-momentum so we can average
> it in the next step.*

A photon travelling in the +z direction with energy E has
4-momentum

<!-- p_+^μ = (E/c,  0, 0, +E/c) -->
$$
p_+^{\mu} \;=\; \left(\frac{E}{c},\; 0,\; 0,\; +\frac{E}{c}\right).
$$

A photon travelling in the −z direction has

<!-- p_-^μ = (E/c,  0, 0, -E/c) -->
$$
p_-^{\mu} \;=\; \left(\frac{E}{c},\; 0,\; 0,\; -\frac{E}{c}\right).
$$

Both satisfy p^μ p_μ = −E²/c² + (E/c)² = 0 (null), as required
for a free photon.  The energy E is the same on both legs because
perfect reflection conserves it.

The photon spends equal proper time τ_leg = L/c on each leg
(travel time at speed c across distance L).  One round trip takes

<!-- T = 2L / c -->
$$
T \;=\; \frac{2L}{c}.
$$

### A.3 — Time-averaged 4-momentum of the cavity-photon system

> *Purpose: show that, averaged over one period, the system's
> spatial momentum is zero.  This is the bookkeeping that turns
> a null 4-momentum into a timelike one.*

Average the photon's 4-momentum over one round trip:

<!-- ⟨p^μ⟩ = (1/T) ∫₀ᵀ p^μ(t) dt -->
$$
\langle p^{\mu}\rangle
\;=\; \frac{1}{T}\int_0^T p^{\mu}(t)\,dt.
$$

The temporal component is constant (energy E throughout):

<!-- ⟨p^0⟩ = E/c -->
$$
\langle p^{0}\rangle \;=\; \frac{E}{c}.
$$

The spatial components: the photon's x and y momenta are zero on
both legs.  The z-momentum is +E/c for half the period and −E/c
for the other half, so

<!-- ⟨p^z⟩ = (1/T)[(E/c)(L/c) + (-E/c)(L/c)] = 0 -->
$$
\langle p^{z}\rangle
\;=\; \frac{1}{T}\!\left[\frac{E}{c}\cdot\frac{L}{c}
       \;+\;\left(-\frac{E}{c}\right)\!\cdot\frac{L}{c}\right]
\;=\; 0.
$$

The instantaneous *photon* momentum oscillates between ±E/c.  The
*system* (mirrors + photon) has zero spatial momentum at every
instant by momentum conservation: each bounce transfers momentum 2E/c from the photon to the
mirror (the photon's momentum reverses from +E/c to −E/c),
keeping the total system momentum (photon + both mirrors)
at zero in F at every instant.

The system's 4-momentum is therefore

<!-- P^μ = (E/c, 0, 0, 0) -->
$$
P^{\mu} \;=\; \left(\frac{E}{c},\; 0,\; 0,\; 0\right).
$$

This is **timelike** — a stark difference from the photon's null
4-momentum.

### A.4 — Rest mass identification

> *Purpose: read off the rest mass from the 4-momentum.*

For any 4-momentum P^μ, the rest mass m is defined by

<!-- m² c² = -P^μ P_μ -->
$$
m^2 c^2 \;=\; -\,P^{\mu} P_{\mu}.
$$

(This is just the relativistic identity E² = m²c⁴ + |**p**|²c²
rewritten.  In our signature, E² − |**p**|²c² = m²c⁴ becomes
−P^μ P_μ = m²c².)

Substituting P^μ = (E/c, 0, 0, 0):

<!-- -P^μ P_μ = -(-(E/c)² + 0) = (E/c)² -->
$$
-P^{\mu} P_{\mu}
\;=\; -\!\left[-\!\left(\frac{E}{c}\right)^{\!2} + 0\right]
\;=\; \left(\frac{E}{c}\right)^{\!2}.
$$

Therefore

<!-- m c = E/c   →   m = E/c² -->
$$
m \;=\; \frac{E}{c^2}.
$$

The cavity-photon system has **rest mass equal to the photon's
energy divided by c²** — Einstein's mass-energy equivalence,
applied to a confined photon.

### A.5 — Standing-wave condition gives the wavelength formula

> *Purpose: convert the rest-mass result from energy to
> wavelength so we can read off the geometric scale.*

Substitute the Planck–Einstein relation E = hc/λ into m = E/c²:

<!-- m = h / (λ c) -->
$$
m \;=\; \frac{h}{\lambda\,c}.
$$

The standing-wave condition 2L = nλ gives λ = 2L/n, so

<!-- m = n h / (2 L c) -->
$$
\boxed{\;m \;=\; \frac{n\,h}{2\,L\,c}\;}
\qquad (n \in \mathbb{Z}^+).
$$

The rest mass is set by the cavity length and the standing-wave
mode number.  The lowest mode (n = 1, λ = 2L) gives the smallest
rest mass for a given cavity length.

### A.6 — The same m is the inertial mass

> *Purpose: prove that the m we just derived is not just a label
> for energy — it also quantifies how hard it is to accelerate the
> system.  Two arguments: a deductive one from Lorentz invariance,
> and a verification by Doppler bookkeeping.*

#### A.6.1 — Lorentz boost argument

In the cavity rest frame F, the system has 4-momentum

<!-- P^μ = (E/c, 0, 0, 0) -->
$$
P^{\mu} \;=\; \left(\frac{E}{c},\; 0,\; 0,\; 0\right).
$$

Now consider an inertial frame F′ in which the cavity moves at
velocity v in the +z direction (equivalently, F′ moves at
velocity −v relative to F).  By Lorentz invariance, the system's
4-momentum in F′ is obtained by a Lorentz boost:

<!-- P^0' = γ (P^0 + v P^z / c) = γ E / c -->
$$
P^{0\prime} \;=\; \gamma\!\left(P^{0} + \frac{v}{c}\,P^{z}\right)
            \;=\; \gamma\,\frac{E}{c},
$$

<!-- P^z' = γ (P^z + v P^0 / c) = γ v E / c² -->
$$
P^{z\prime} \;=\; \gamma\!\left(P^{z} + \frac{v}{c}\,P^{0}\right)
            \;=\; \gamma\,\frac{v\,E}{c^{2}},
$$

with γ = (1 − v²/c²)^(−1/2) and P^x = P^y = 0 unchanged.

Substituting m = E/c²:

<!-- E' = γ m c²,  p_z' = γ m v -->
$$
E' \;=\; \gamma\,m\,c^{2}, \qquad
p_{z}' \;=\; \gamma\,m\,v.
$$

These are **exactly** the energy and momentum of a free
relativistic particle of rest mass m moving at velocity v.  The
cavity-photon system therefore obeys the same dynamics as such a
particle — including Newton's second law in its relativistic form

<!-- F = d(γ m v) / dt -->
$$
F \;=\; \frac{d\,(\gamma m v)}{dt}.
$$

The coefficient that resists acceleration is m = E/c².  This is
the inertial mass.

The "least cost" framing: among all inertial frames, F (the
cavity rest frame) gives the system the **smallest** energy
(E vs. γE > E in any boosted frame).  The rest frame is the
minimum-energy configuration; moving the system away from it
costs work in the form of relativistic kinetic energy
(γ − 1)mc².  The system resists being moved with coefficient m
because being moved costs energy.

#### A.6.2 — Verification by Doppler bookkeeping

For physical insight, we verify A.6.1 by directly computing the
work needed to accelerate the cavity using the Doppler shift on
each bounce.

Suppose mirror 1 (at z = 0) starts moving in the +z direction
with small velocity v ≪ c, while mirror 2 (at z = L) is held
fixed.  A photon travelling in the −z direction hits mirror 1.
For a mirror moving toward the source at speed v, the standard
relativistic Doppler formula for reflected light gives

<!-- f' = f · (c+v)/(c-v) ≈ f · (1 + 2v/c)  for v << c -->
$$
f' \;=\; f\,\frac{c + v}{c - v}
   \;\approx\; f\!\left(1 + \frac{2v}{c}\right).
$$

The photon's energy increases by

<!-- ΔE_photon = h Δf ≈ 2 h f · v / c = 2 E · v / c -->
$$
\Delta E_{\text{photon}}
\;\approx\; \frac{2\,E\,v}{c}\quad\text{per bounce}.
$$

By energy conservation, this energy comes from work done by
mirror 1.  The photon bounces back and forth at a rate
1/T = c/(2L), so the time-averaged rate of work input is

<!-- dW/dt = (2 E v / c) · (c / 2L) = E v / L -->
$$
\frac{dW}{dt} \;=\; \frac{E\,v}{L}.
$$

To accelerate the cavity from rest to a final velocity v_f, we
integrate over time as v ramps up.  In the non-relativistic
limit, the kinetic energy of a particle of mass m is (1/2)mv²,
so the work-energy theorem requires

<!-- ∫ (E v / L) dt = (1/2) m v_f² -->
$$
\int_0^{t_f}\!\!\frac{E\,v}{L}\,dt \;=\; \tfrac{1}{2}\,m\,v_f^{2}.
$$

Using v(t) = a t and v_f = a t_f, the left side evaluates to
(E / L) · (v_f² t_f / 2) — but this carries an extra t_f.
The resolution is that the *photon's energy itself increases*
during the acceleration (the Doppler shifts cumulate), so E in
the cavity rest frame at the end is greater than E at the start.

Working through the bookkeeping carefully (or, equivalently,
just trusting Lorentz invariance from A.6.1), the net work done
on the cavity equals the relativistic kinetic energy
(γ − 1)mc² with m = E_initial / c².  This is the same m as
A.4, A.5, and A.6.1.

The detailed Doppler calculation is a consistency check, not an
independent derivation.  Lorentz invariance has already pinned
down the answer; the Doppler argument shows that the photon
field carries the inertia in a physically intuitive way (the
work goes into Doppler-shifting the trapped light).

### A.7 — Generalization: any confining geometry works

> *Purpose: state the lemma in a form that doesn't depend on
> physical mirrors.*

Inspect what was actually used:

- **Step A.1:** A boundary condition that singles out a discrete
  set of wavelengths (a standing-wave condition).
- **Steps A.2–A.4:** The photon's null 4-momentum, the time
  average over a periodic motion, and the rest-mass identity.
- **Step A.5:** The Planck–Einstein relation E = hf.
- **Step A.6:** Lorentz invariance.

Nothing in this list requires the confinement to be implemented
by physical mirrors.  Any geometric mechanism that imposes a
periodicity 2L on the photon's motion produces the same
result.  In particular, if the photon is confined to a **compact
spatial dimension** — a circle of circumference L, with no
mirrors needed because periodicity does the confining — the
standing-wave condition becomes L = nλ (one full wavelength per
trip around, etc.) instead of 2L = nλ, and the rest mass becomes

<!-- m = n h / (L c)   for a circular compact dimension -->
$$
m \;=\; \frac{n\,h}{L\,c}
\qquad\text{(circular compact dimension)}.
$$

The factor of two between this and the linear-cavity result
(equation in A.5) reflects the geometric difference: the cavity
needs *two* trips to return to its starting phase (out and back),
while the circle returns in *one* trip.

This is the bridge to the photon-on-torus program: any compact
direction in higher dimensions, populated by a photon, gives a
4D rest mass set by the standing-wave mode number on that
direction.

---

## Part B — Photon orbiting a 1D ring

### Goal

Replace the linear cavity with a circular 1D ring of
circumference L.  Show that the same arguments give the same
rest mass m = nh/(Lc), but now also produce a quantized angular
momentum L_z = nℏ from the photon's tangential motion.  Show
that this angular momentum makes the system gyroscopically
stable.

### B.1 — Geometric setup

> *Purpose: fix coordinates for circular motion and state the
> single-valuedness boundary condition.*

A circular 1D ring of circumference L lies in the xy-plane,
centered on the origin, in inertial frame F.  Its radius is

<!-- r = L / (2π) -->
$$
r \;=\; \frac{L}{2\pi}.
$$

A single photon orbits the ring tangentially.  Let φ be the
photon's angular position about the z-axis at time t; for
definiteness take the orbit to be counter-clockwise so dφ/dt =
c/r > 0.

**Boundary condition.**  The photon's wavefunction must be
single-valued on the ring: after one trip around, it returns to
itself.  This requires the wavelength to fit an integer number
of times around the circumference,

<!-- L = n λ,  n ∈ ℤ⁺ -->
$$
L \;=\; n\,\lambda, \qquad n \in \mathbb{Z}^+.
$$

(Note the factor of 2 difference from Part A's 2L = nλ.  The
ring is a single loop, not an out-and-back path.)

### B.2 — Photon 4-momentum at angular position φ

> *Purpose: write down the spatial momentum vector at every point
> on the orbit so we can compute both linear and angular averages.*

The photon's 3-momentum has magnitude E/c (massless) and points
tangent to the circle.  At angular position φ, the unit tangent
is (−sin φ, cos φ, 0) (counter-clockwise convention), so

<!-- p(φ) = (E/c) (−sin φ, cos φ, 0) -->
$$
\mathbf{p}(\varphi)
\;=\; \frac{E}{c}\,(-\sin\varphi,\;\cos\varphi,\; 0).
$$

The 4-momentum is

<!-- p^μ(φ) = (E/c, -(E/c) sin φ, (E/c) cos φ, 0) -->
$$
p^{\mu}(\varphi) \;=\;
\left(\frac{E}{c},\;-\frac{E}{c}\sin\varphi,\;
\frac{E}{c}\cos\varphi,\; 0\right).
$$

Check: p^μ p_μ = −(E/c)² + (E/c)² sin²φ + (E/c)² cos²φ + 0 = 0.
Null, as required.

The energy E is constant in time: whatever mechanism confines
the photon to the ring does no work on it (the constraint force
is centripetal, perpendicular to the photon's motion).  As in
A.7, we leave the confining mechanism unspecified — the results
hold for any geometry that achieves circular confinement.

### B.3 — Time-averaged spatial momentum is zero

> *Purpose: same as A.3 — collapse the null instantaneous
> 4-momentum into a timelike average.*

Average over one orbital period T = L/c (or equivalently over
φ ∈ [0, 2π]):

<!-- ⟨p_x⟩ = (E/c) (1/2π) ∫₀^{2π} (-sin φ) dφ = 0 -->
$$
\langle p_x\rangle \;=\;
\frac{E}{c}\,\frac{1}{2\pi}\!\int_0^{2\pi}\!(-\sin\varphi)\,d\varphi
\;=\; 0,
$$

<!-- ⟨p_y⟩ = (E/c) (1/2π) ∫₀^{2π} cos φ dφ = 0 -->
$$
\langle p_y\rangle \;=\;
\frac{E}{c}\,\frac{1}{2\pi}\!\int_0^{2\pi}\!\cos\varphi\,d\varphi
\;=\; 0,
$$

and ⟨p_z⟩ = 0 trivially.  So

<!-- ⟨P^μ⟩ = (E/c, 0, 0, 0) -->
$$
\langle P^{\mu}\rangle \;=\; \left(\frac{E}{c},\; 0,\; 0,\; 0\right).
$$

Same form as Part A.

### B.4 — Rest mass

> *Purpose: read off the rest mass.  Then specialize the
> wavelength using the ring boundary condition.*

By the same identity as A.4,

<!-- m = E / c² -->
$$
m \;=\; \frac{E}{c^{2}}.
$$

Substituting E = hc/λ and λ = L/n (from B.1):

<!-- m = n h / (L c) -->
$$
\boxed{\;m \;=\; \frac{n\,h}{L\,c}\;}
\qquad (n \in \mathbb{Z}^+).
$$

This matches the result quoted in A.7 for "any compact direction
of circumference L."  The ring case *is* the simplest realization
of a 1D compact direction.

### B.5 — Quantized angular momentum from single-valuedness

> *Purpose: this is the new physics that the ring geometry makes
> available — angular momentum about the ring axis, automatically
> quantized in units of ℏ.*

The angular momentum about the z-axis is L_z = (**r** × **p**)_z
where **r** = (r cos φ, r sin φ, 0) is the photon's position on
the ring.  Compute:

<!-- L_z = r p_y - y p_x = r cos φ · (E/c) cos φ + r sin φ · (E/c) sin φ = r E / c -->
$$
L_z(\varphi)
\;=\; x\,p_y - y\,p_x
\;=\; r\cos\varphi\cdot\frac{E}{c}\cos\varphi
   \;+\; r\sin\varphi\cdot\frac{E}{c}\sin\varphi
\;=\; \frac{r\,E}{c}.
$$

(The minus signs in **p** combined with the position components
give a sum of cos² + sin² = 1.)

Strikingly, L_z is **independent of φ**: the angular momentum is
constant in time, equal at every instant to rE/c.  Substituting
r = L/(2π) and E = nhc/L (from B.4):

<!-- L_z = (L / 2π) · (n h c / L) / c = n h / (2π) = n ℏ -->
$$
L_z
\;=\; \frac{L}{2\pi}\cdot\frac{n\,h\,c\,/\,L}{c}
\;=\; \frac{n\,h}{2\pi}
\;=\; n\,\hbar.
$$

So

<!-- L_z = n ℏ -->
$$
\boxed{\;L_z \;=\; n\,\hbar\;}
\qquad (n \in \mathbb{Z}^+).
$$

The orbiting photon has angular momentum quantized in units of
ℏ.  This came out of:

- the photon's relativistic energy-momentum relation |**p**| =
  E/c,
- the single-valuedness boundary condition L = nλ,
- the geometric definition of angular momentum, L_z = r × p_t,
- the Planck–Einstein relation E = hf to introduce h.

No quantum mechanics beyond the Planck–Einstein relation.  No
spinors, no Pauli matrices.  The same n that sets the rest mass
also sets the angular momentum, so they are not independent
quantities in this geometry: m and L_z are locked together by

<!-- L_z = n ℏ,  m = n h / (L c)  →  L_z / m = L c / (2π) = r c -->
$$
\frac{L_z}{m} \;=\; \frac{L\,c}{2\pi} \;=\; r\,c.
$$

### B.6 — Gyroscopic stability

> *Purpose: show that the angular momentum from B.5 makes the
> system mechanically resistant to tilting — i.e., it has
> rotational inertia in the same sense a spinning top does.*

The system carries angular momentum **L** = (0, 0, L_z) along
the z-axis.  Newton's second law for rotational motion is

<!-- τ = dL/dt -->
$$
\boldsymbol{\tau} \;=\; \frac{d\mathbf{L}}{dt}.
$$

If we apply a torque τ_x about the x-axis (trying to tilt the
ring), the angular-momentum vector responds by precessing rather
than tilting straight away.  In the gyroscope limit (L large
compared to the perturbation), |dL/dt| = Ω × |L| where Ω is the
precession rate, giving

<!-- |τ| = Ω · n ℏ -->
$$
|\boldsymbol{\tau}| \;=\; \Omega \cdot n\,\hbar.
$$

The torque required to tilt the ring at any rate is *proportional
to the angular momentum*.  The system "holds its position" in
the same sense a spinning top does — it processes around external
torques rather than yielding to them.

This is the rotational analog of A.6's translational inertia: the
photon's confinement produces resistance to changes in linear
*and* angular state of motion, both quantified by the same kind
of bookkeeping (4-momentum conservation, plus an extra geometric
ingredient — the radius — for the rotational case).

### B.7 — Comparison and the "two outputs for free" point

> *Purpose: make explicit what the ring case adds over the linear
> case, since this is the conceptual hinge for later tracks.*

Side-by-side:

| Geometry | Confinement | Rest mass m | Angular momentum L_z |
|----------|-------------|-------------|----------------------|
| Linear cavity (Part A) | 2L = nλ | nh / (2Lc) | none (linear motion) |
| Circular ring (Part B) | L = nλ | nh / (Lc) | nℏ |

Both produce rest mass.  The ring produces, *in addition*, a
quantized angular momentum.  The extra output costs no extra
postulate: the same E, the same n, the same h, the same
single-valuedness condition — only the geometry has changed.

**This is the program's central observation in miniature.**  A
single compact dimension delivers one output (mass, on the
linear; mass + angular momentum, on the circle).  Generalizing
from one compact direction to a 2-torus lets each direction
independently deliver its own output via the same mechanism,
and the cross-coupling between them (the off-diagonal 2×2 metric
entry — what MaSt calls **shear**) is conjectured to deliver a
*third* output: spin.

The orbital angular momentum L_z = nℏ derived here is
**integer-valued** for any positive integer n.  It is not yet
the half-integer spin of an electron.  Half-integer values
require a more delicate construction (a holonomy phase that is
half what one would naively expect), and that construction needs
the cross-coupling that only a 2-torus provides.  Part B
establishes the *classical-geometric* ingredient (orbital angular
momentum from confined light); the *topological* ingredient
(a 2π rotation that returns the wavefunction to its negative)
is the question for whether spin is realizable from the 2×2
sheared torus metric.

---

## Lemma (Track 1 result)

We have shown:

> **(F1) Linear cavity.**  A photon confined to a linear cavity
> of length L by a standing-wave boundary condition has rest
> mass m = nh / (2Lc) in the cavity rest frame.  This rest mass
> is also the inertial mass: the cavity-photon system, viewed
> from a frame moving at velocity v relative to the cavity,
> carries 4-momentum identical to that of a free relativistic
> particle of rest mass m moving at v.
>
> **(F2) Circular ring.**  A photon orbiting a 1D ring of
> circumference L has rest mass m = nh / (Lc) and angular
> momentum L_z = nℏ about the ring axis.  The ring's gyroscopic
> stability — its resistance to tilting under an applied torque
> — is quantified by L_z and exhibits standard precession
> dynamics.
>
> **(F3, interpretive)**  1D linear confinement of a photon
> produces rest mass and inertia.  1D circular confinement
> produces, in addition, a quantized angular momentum.  These
> two outputs come from the same mechanism — confinement of a
> null-trajectory object by a standing-wave boundary condition
> — applied to two different geometries.  The 2-torus, which
> combines both confinement geometries with a cross-coupling,
> is the natural setting in which to ask whether mass, charge,
> and spin can all emerge together from a single photon ansatz.

F1–F3 are invoked by the subsequent derivations of Program 1
without re-derivation.
