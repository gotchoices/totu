# Derivation 3 — Photon on a 2-torus: 4D mass from compact momentum

**Program 1, Track 3.**  Replace Track 2's massive test particle
with a **null trajectory** (a photon) in the same 6D geometry.
Use Track 1's lemma to interpret the result.  Read off the
projected 4D rest mass as the magnitude of the conserved
compact momentum vector (P_4, P_5) measured in the inverse
internal metric h^ab.  In the canonical case the result is the
**Pythagorean mass formula** m c = (h/L) √(n_4² + n_5²); the
general case is a quadratic form m²c² = h^ab P_a P_b that is
the structural seed of MaSt's mass formula.

---

## Inputs

In addition to derivations 1 and 2:

1. **Track 1 lemma F1–F3** (derivation-1):
   - F1: a photon between mirrors has rest mass m = nh/(2Lc)
     in the rest frame of the mirrors, with Lorentz-invariant
     inertia.
   - F2: a photon orbiting a 1D ring of circumference L has
     rest mass m = nh/(Lc) and quantized angular momentum
     L_z = nℏ.
   - F3: the linear cavity confines a photon to make mass; the
     ring confines it to make mass + angular momentum.  The
     2-torus extends this to mass + two quantum numbers.
2. **Track 2 lemma F4–F6** (derivation-2):
   - F4: U(1)×U(1) gauge structure with two conserved compact
     momenta P_4, P_5.
   - F5: two-charge Lorentz force on the projected particle.
   - F6: internal shear g_45 cross-couples the two charges and
     mixes P_a with kinetic w^b.
3. **The 6D null condition** for a photon:
   G_AB k^A k^B = 0, where k^A is the photon's 6D wave
   4-vector.
4. **Standing-wave quantization** on the compact directions
   (derivation-2 D.4): P_a = n_a h/L_a with n_a ∈ ℤ.

For this derivation we restrict to **flat 4D spacetime with no
external gauge fields turned on**: g_μν = η_μν, A_μ = 0,
B_μ = 0.  This isolates the rest-mass derivation from
gravitational and Lorentz-force complications, both of which
are independent of the rest-mass identification and were already
treated in Tracks 1 and 2.  Turning on either A_μ or B_μ at the
end recovers Track 2's two-charge Lorentz force acting on the
massive projected particle.

Signature: (−, +, +, +, +, +).

---

## Section A — The 6D null trajectory

### A.1 — The photon in 6D

> *Purpose: state precisely what we mean by "a photon on a
> 2-torus" and why the 6D worldline is null.*

A photon is the quantum of the electromagnetic field; classically
it is a packet of light, traveling at the local speed of light
along null geodesics of whatever metric it lives in.  In 6D
(M⁴ × T²) the photon's worldline is null with respect to G_AB:

<!-- G_AB k^A k^B = 0 -->
$$
G_{AB}\,k^{A}\,k^{B} \;=\; 0,
$$

where k^A = dx^A/dλ is the photon's 6D wave 4-vector with λ an
affine parameter.  This is the higher-dimensional analog of
the familiar 4D null condition η_μν k^μ k^ν = 0 for light in
flat spacetime.

Crucially, k^A has six independent components.  The photon
moves at the local speed of light *in 6D* — but its motion
divides into a 4D part k^μ (motion in extended spacetime) and
a compact part k^4, k^5 (motion around the torus).  When the
compact components are nonzero, the 4D part is *not* null:
the projected 4D motion appears slower than light, with a
specific deficit that we will identify with the rest mass.

This is the central conceptual move of Program 1: a 6D null
worldline with nontrivial compact motion projects to a 4D
massive worldline.  Track 1 established the 1D cases (linear
cavity, 1D ring) where the same geometry produced the same
result: confined light → rest mass.  This derivation makes the
2-torus case explicit.

### A.2 — Conservation of P_4 and P_5 for null trajectories

> *Purpose: confirm that derivation-2 D.2's conservation argument
> applies to photons exactly as it applies to massive particles.*

The Killing-vector argument (derivation-2 D.2) used only that:
(i) the metric does not depend on x^4 or x^5 (cylinder
condition), and (ii) the trajectory is a geodesic.  Neither
condition cares whether the geodesic is timelike or null.

For a null geodesic with affine parameter λ, the geodesic
equation reads d²x^A/dλ² + Γ^A_BC k^B k^C = 0.  For any
Killing vector ξ, the projection ξ_A p^A of the photon's
4-momentum p^A = ℏ k^A is conserved along λ.  Specializing
to ξ = ∂/∂x^a and using p^A = ℏ k^A:

<!-- P_a ≡ ξ_A^(a) p^A = ℏ G_aB k^B = ℏ g_ab w^b,  d P_a/dλ = 0 -->
$$
P_{a} \;\equiv\; \hbar\,G_{aB}\,k^{B} \;=\; \hbar\,g_{ab}\,w^{b},
\qquad
\frac{dP_{a}}{d\lambda} \;=\; 0,
$$

where w^b = k^b + A^b_μ k^μ is the gauge-covariant compact
wavenumber (with A^4 = A_μ, A^5 = B_μ).  In our restricted
setup with A_μ = B_μ = 0 this simplifies to w^b = k^b.

The factor of ℏ is bundled into the definition so that P_a
has units of momentum (kg·m/s), matching the convention of
derivation-2.  This is the same momentum that obeys the
standing-wave quantization P_a = n_a h/L_a (derivation-2 D.4).

### A.3 — Decomposition of k^A

> *Purpose: split the 6D wave vector into spacetime and
> compact pieces, which we will treat differently.*

Write the components of k^A explicitly:

| Index | Symbol | Interpretation |
|-------|--------|----------------|
| μ ∈ {0,1,2,3} | k^μ | 4D wave 4-vector (frequency + 3-wavevector) |
| 4 | k^4 | wavenumber along first compact direction |
| 5 | k^5 | wavenumber along second compact direction |

In our restricted setup (A_μ = B_μ = 0), the gauge-covariant
compact wavenumbers reduce to the bare ones: w^4 = k^4,
w^5 = k^5.  The conservation laws of A.2 then read

<!-- P_4 = ℏ(g_44 k^4 + g_45 k^5) ,  P_5 = ℏ(g_45 k^4 + g_55 k^5) -->
$$
P_{4} \;=\; \hbar\!\left(g_{44}\,k^{4} \;+\; g_{45}\,k^{5}\right),
\qquad
P_{5} \;=\; \hbar\!\left(g_{45}\,k^{4} \;+\; g_{55}\,k^{5}\right).
$$

Both are conserved along the trajectory (and both have units of
momentum).

The 4D wave 4-vector k^μ is *not* a priori conserved —
spacetime translation invariance in 4D would be needed for
that, and we have not (yet) imposed it.  In a flat 4D spacetime
(g_μν = η_μν, no x^μ-dependence anywhere), k^μ is also
conserved by the additional 4D Killing vectors ∂/∂x^μ.  But the
mass-shell relation that follows from the null condition holds
locally regardless, so we don't need to invoke conservation of
k^μ for the rest-mass derivation.

---

## Section B — Decomposing the null condition

### B.1 — Setup

> *Purpose: state the simplifications used, then expand the 6D
> null condition.*

Restricted setup for this section: g_μν = η_μν (flat 4D),
A^a_μ = 0 (no gauge potentials).  The metric ansatz from
derivation-2 A.2 reduces to

<!-- ds² = η_μν dx^μ dx^ν + g_ab dx^a dx^b -->
$$
ds^{2} \;=\; \eta_{\mu\nu}\,dx^{\mu}\,dx^{\nu}
        \;+\; g_{ab}\,dx^{a}\,dx^{b}.
$$

The 6D metric in matrix form is block-diagonal:

<!-- G_AB = diag(η, g) -->
$$
G_{AB} \;=\;
\begin{pmatrix}
\eta_{\mu\nu} & 0 \\[2pt]
0 & g_{ab}
\end{pmatrix},
$$

with the 2×2 internal block g_ab still potentially having a
nonzero shear g_45.  The gauge-field corrections of derivation-2
A.2 vanish entirely in this gauge.

### B.2 — Expanding G_AB k^A k^B = 0

> *Purpose: do the algebra.*

With G_AB block-diagonal:

<!-- G_AB k^A k^B = η_μν k^μ k^ν + g_ab k^a k^b -->
$$
G_{AB}\,k^{A}\,k^{B}
\;=\; \eta_{\mu\nu}\,k^{\mu}\,k^{\nu}
\;+\; g_{ab}\,k^{a}\,k^{b}.
$$

(There is no cross-term G_μa k^μ k^a because G_μa = g_ab A^b_μ
and we set A^a_μ = 0.)

The null condition G_AB k^A k^B = 0 then becomes

<!-- η_μν k^μ k^ν = -g_ab k^a k^b -->
$$
\boxed{\;
\eta_{\mu\nu}\,k^{\mu}\,k^{\nu}
\;=\; -\,g_{ab}\,k^{a}\,k^{b}
\;}
$$

This is the **central identity** for the rest of the
derivation.  It says: the 4D part of the photon's wave-vector
norm is *minus* the compact part.

Two observations:

- The 4D inner product η_μν k^μ k^ν has the sign of "−E²/c² + |**k**|²"
  in the (−,+,+,+) signature: it is negative when the 4D
  motion is timelike-like (E²/c² > |**k**|²) and zero when 4D
  null.
- The compact inner product g_ab k^a k^b is positive (g_ab is
  positive definite, both compact directions are spacelike).

So the 4D inner product is negative whenever the compact motion
is nontrivial — the projected 4D motion is **timelike** when
the photon has compact momentum.

### B.3 — Identification with the 4D mass shell

> *Purpose: make the projected-mass identification rigorous.*

A massive particle in 4D with rest mass m has a 4-momentum
p^μ satisfying the mass-shell relation

<!-- η_μν p^μ p^ν = -m²c² -->
$$
\eta_{\mu\nu}\,p^{\mu}\,p^{\nu} \;=\; -\,m^{2}\,c^{2}.
$$

The Planck–Einstein relation E = ℏω with E = c |p^0| etc.
identifies the 4-momentum with the wave 4-vector:

<!-- p^μ = ℏ k^μ -->
$$
p^{\mu} \;=\; \hbar\,k^{\mu}.
$$

(This is the same Planck–Einstein input that derivation-1
allowed; nothing new.)  Substituting into the mass shell:

<!-- ℏ² η_μν k^μ k^ν = -m²c² -->
$$
\hbar^{2}\,\eta_{\mu\nu}\,k^{\mu}\,k^{\nu} \;=\; -\,m^{2}\,c^{2}.
$$

Combine with the boxed identity from B.2:

<!-- ℏ² (-g_ab k^a k^b) = -m²c² -->
$$
\hbar^{2}\!\left(-\,g_{ab}\,k^{a}\,k^{b}\right) \;=\; -\,m^{2}\,c^{2},
$$

which simplifies to

<!-- m²c² = ℏ² g_ab k^a k^b -->
$$
\boxed{\;
m^{2}\,c^{2} \;=\; \hbar^{2}\,g_{ab}\,k^{a}\,k^{b}
\;}
$$

The projected 4D rest mass squared equals the compact-direction
norm of the wave-vector (times ℏ²).  This is the **photon-on-
torus mass formula** in its cleanest form.

The Track 1 connection is now visible.  In Track 1A (linear
cavity), the photon's wavenumber along the cavity axis was
k = π n / L; the squared cavity wavenumber was k² = (πn/L)²,
and the Planck–Einstein relation gave m = ℏk/c.  Here we are
doing the *same thing* in two compact dimensions: the rest
mass is set by the magnitude of the compact wavenumber,
weighted by the internal metric g_ab.

### B.4 — Mass formula in terms of conserved P_a

> *Purpose: rewrite the mass formula in terms of the conserved
> quantities (which are physically meaningful as charges) rather
> than the raw wavenumbers.*

In the restricted setup of this section (A^a_μ = 0), w^a = k^a
and P_a = ℏ g_ab k^b (from A.2).  Solve for ℏk^a using h^ab
from derivation-2 B.2:

<!-- ℏ k^a = h^ab P_b -->
$$
\hbar\,k^{a} \;=\; h^{ab}\,P_{b}.
$$

Substitute into B.3's boxed mass formula m²c² = ℏ² g_ab k^a k^b:

<!-- m²c² = g_ab (ℏk^a)(ℏk^b) = g_ab (h^ac P_c)(h^bd P_d) -->
$$
m^{2}\,c^{2}
\;=\; g_{ab}\,(\hbar\,k^{a})(\hbar\,k^{b})
\;=\; g_{ab}\,(h^{ac}\,P_{c})\,(h^{bd}\,P_{d}).
$$

First contract over a: g_ab h^ac = δ^c_b (definition of the
inverse, verified in derivation-2 B.3 case 4).  Then contract
over b: δ^c_b h^bd = h^cd.  So g_ab h^ac h^bd = h^cd, giving:

<!-- m²c² = h^ab P_a P_b -->
$$
\boxed{\;
m^{2}\,c^{2} \;=\; h^{ab}\,P_{a}\,P_{b}
\;}
$$

This is the **general mass formula**: the projected 4D rest
mass squared is the inverse-internal-metric quadratic form of
the two conserved compact momenta.  No factors of ℏ remain
explicitly — they are absorbed into the definition of P_a as a
momentum-like quantity (A.2).  The formula is dimensionally
clean: h^ab has units of inverse-(metric units) and P_a P_b
of momentum², giving the correct (mass × velocity)² on the
right.

---

## Section C — Canonical case: Pythagorean mass formula

### C.1 — Diagonal internal metric, equal radii

> *Purpose: pick the simplest possible 2-torus and read off the
> mass spectrum.*

Take the simplest non-trivial 2-torus:

- Equal radii: L_4 = L_5 = L.
- Diagonal internal metric: g_44 = g_55 = 1, g_45 = 0
  (no shear).

Then h^ab = δ^ab (the inverse of the identity 2×2 is the
identity), and the mass formula collapses to a Euclidean
inner product:

<!-- m²c² = P_4² + P_5² -->
$$
m^{2}\,c^{2} \;=\; P_{4}^{2} \;+\; P_{5}^{2}.
$$

### C.2 — m c = √(P_4² + P_5²)

> *Purpose: rewrite as a Pythagorean magnitude.*

Take the square root:

<!-- m c = √(P_4² + P_5²) -->
$$
\boxed{\;
m\,c \;=\; \sqrt{P_{4}^{2} \;+\; P_{5}^{2}}
\;}
$$

The 4D rest energy mc is the **Pythagorean magnitude** of the
two compact momenta P_4, P_5.

This is the natural 2-torus generalization of Track 1's results:

- Track 1A (linear cavity, 1 quantum number n): mc = nh/(2L).
- Track 1B (1D ring, 1 quantum number n): mc = nh/L.
- Track 3 (2D torus, 2 quantum numbers n_4, n_5):
  mc = (h/L) √(n_4² + n_5²).

The 2-torus combines two ring directions, and the rest mass is
the Euclidean magnitude of the contributions from each.

### C.3 — Standing-wave quantization → discrete spectrum

> *Purpose: get the explicit discrete mass spectrum.*

Single-valuedness of the photon's standing wave on the 2-torus
requires P_a = n_a h/L_a (derivation-2 D.4).  With L_4 = L_5 = L:

<!-- P_a = n_a h/L -->
$$
P_{a} \;=\; \frac{n_{a}\,h}{L}, \qquad n_{a} \in \mathbb{Z}.
$$

Substitute into the boxed C.2 result:

<!-- m c = (h/L) √(n_4² + n_5²) -->
$$
\boxed{\;
m \;=\; \frac{h}{L\,c}\,\sqrt{n_{4}^{2} \;+\; n_{5}^{2}}
\;}
$$

The mass spectrum is a discrete set of values labeled by
(n_4, n_5) ∈ ℤ × ℤ.  Tabulating the lowest few:

| (n_4, n_5) | n_4² + n_5² | m / (h/Lc) |
|------------|-------------|------------|
| (0, 0) | 0 | 0 |
| (±1, 0), (0, ±1) | 1 | 1 |
| (±1, ±1) | 2 | √2 ≈ 1.414 |
| (±2, 0), (0, ±2) | 4 | 2 |
| (±2, ±1), (±1, ±2) | 5 | √5 ≈ 2.236 |
| (±2, ±2) | 8 | 2√2 ≈ 2.828 |

Notice the **degeneracies**: (±1, 0), (0, ±1), (1, 0), (−1, 0)
all give m/(h/Lc) = 1.  These are different states with the
same mass — a multiplicity that, in Program 1's eventual
electron derivation, will need to be matched against observed
particle multiplicities (e.g., spin states) or lifted by
breaking the symmetry (asymmetric radii or shear).

The (0, 0) state is massless — a 4D photon, as expected when
neither compact momentum is excited.

---

## Section D — General case with shear

### D.1 — Mass formula as a quadratic form

> *Purpose: write the general mass formula explicitly in terms
> of g_44, g_55, g_45 and study its structure.*

Reinstate generic g_ab.  From derivation-2 B.2, the inverse
internal metric is

$$
h^{ab}
\;=\;
\frac{1}{G}
\begin{pmatrix}
g_{55} & -g_{45} \\[2pt]
-g_{45} & g_{44}
\end{pmatrix},
\qquad G \;\equiv\; g_{44}\,g_{55} \;-\; g_{45}^{2}.
$$

The mass formula B.4 reads:

<!-- m²c² = h^ab P_a P_b = (g_55 P_4² - 2 g_45 P_4 P_5 + g_44 P_5²) / G -->
$$
m^{2}\,c^{2}
\;=\; h^{ab}\,P_{a}\,P_{b}
\;=\; \frac{g_{55}\,P_{4}^{2} \;-\; 2\,g_{45}\,P_{4}\,P_{5}
            \;+\; g_{44}\,P_{5}^{2}}{G}.
$$

This is a positive-definite quadratic form in (P_4, P_5).
Three observations:

1. The off-diagonal term −2 g_45 P_4 P_5 / G has a **minus
   sign** even though g_45 may be positive (the sign flip
   came from inverting the 2×2 internal block).  So a positive
   shear suppresses mass when n_4 and n_5 have the same sign,
   and enhances it when they have opposite signs.
2. The denominator G = g_44 g_55 (1 − s²) goes to zero as
   |s| → 1 (recalling s ≡ g_45/√(g_44 g_55) is the dimensionless
   shear).  In this limit the mass diverges for any nonzero
   P_a — the 2×2 internal block becomes singular and the
   2-torus degenerates to a 1D direction.
3. Setting g_45 = 0 reduces to a diagonal form:
   m²c² = P_4²/g_44 + P_5²/g_55, which is a generalized
   Pythagorean (with anisotropic weights).  Setting further
   g_44 = g_55 = 1 recovers Section C.

### D.2 — Eigenvalues and "principal mass directions"

> *Purpose: diagonalize the mass formula to identify the
> "natural" mass eigenstates.*

The quadratic form h^ab P_a P_b has principal axes given by
the eigenvectors of h^ab.  The 2×2 matrix h^ab has eigenvalues

<!-- λ_± = (h^44 + h^55 ± √((h^44 - h^55)² + 4 (h^45)²)) / 2 -->
$$
\lambda_{\pm}
\;=\;
\tfrac{1}{2}\!\left[
   h^{44} + h^{55}
   \;\pm\; \sqrt{(h^{44} - h^{55})^{2} + 4\,(h^{45})^{2}}
\right].
$$

In the principal-axes coordinates (P̃_4, P̃_5):

<!-- m²c² = λ_+ P̃_4² + λ_- P̃_5² -->
$$
m^{2}\,c^{2} \;=\; \lambda_{+}\,\tilde{P}_{4}^{2}
                \;+\; \lambda_{-}\,\tilde{P}_{5}^{2}.
$$

The (P̃_4, P̃_5) are linear combinations of (P_4, P_5) that
**diagonalize** the mass formula — these are the "principal
mass directions."

Interpretation: when the shear is on, the natural quantum
numbers for *mass* are not the same as the natural quantum
numbers for *charge*.  Charge eigenstates have definite
(P_4, P_5) — these are the conserved quantities of derivation-2.
Mass eigenstates have definite (P̃_4, P̃_5) — linear
combinations involving the shear.

A pure-charge eigenstate (say P_4 ≠ 0, P_5 = 0) is therefore
*not* a pure-mass eigenstate when s ≠ 0; it is a superposition
in the principal-mass basis.  This is a **kinematic mixing**
of charge and mass, originating in the off-diagonal h^45 of
the inverse internal metric.

This mixing is the structural origin of MaSt's
(n_r − s n_t)² combination: the mass formula depends on
shear-shifted linear combinations of the charge labels.

### D.3 — Structural form of the MaSt mass formula

MaSt's empirically-found mass formula reads

<!-- μ² = (n_t/ε)² + (n_r - s n_t)² -->
$$
\mu^{2} \;=\; \left(\frac{n_{t}}{\varepsilon}\right)^{2}
        \;+\; \left(n_{r} - s\,n_{t}\right)^{2}.
$$

The "n_t/ε" term is the **tube** contribution scaled by the
inverse aspect ratio; the "n_r − s n_t" term is the **ring**
contribution shifted by the shear times the tube quantum number.

This is exactly the kind of quadratic form that B.4's general
formula produces, with (P_4, P_5) ↔ (n_t, n_r) and the
internal metric chosen with an aspect ratio ε and a shear s.
The structural ingredients are all here:

- A quadratic form in the two compact-momentum quanta.
- A characteristic ratio (the aspect ratio ε) that scales one
  contribution relative to the other.
- A linear shift of one quantum by the shear times the other,
  exactly the "n_r − s n_t" combination.

The explicit parametrization that maps (g_44, g_55, g_45) to
(ε, s) and recovers MaSt's prefactors is treated in a
dedicated derivation.  Here we have shown only the structural
correspondence: the quadratic form m²c² = h^ab P_a P_b admits
a (n_r − s n_t) cross-term whenever g_45 ≠ 0, matching MaSt's
formula in form.

---

## Section E — Inertial mass on the 2-torus

### E.1 — Lorentz boost of the cavity-photon system

> *Purpose: confirm that Track 1's inertia argument applies
> unchanged.*

Track 1A (derivation-1, A.6) showed that a photon-in-a-cavity
system has inertial mass identical to its rest energy
divided by c² — the cavity-photon 4-momentum transforms under
Lorentz boosts as a single composite massive object, with the
expected γ-factors.

The same argument applies here.  In a frame F where the
2-torus is at rest (and the photon is bouncing around inside
its compact directions), the projected 4-momentum is
p^μ = (E/c, **0**) with E = mc² the photon's total energy.
Boosting to a frame F′ in which the 2-torus moves with
velocity v in direction n̂:

<!-- p'^0 = γ E/c ,  p'^i = γ v_i E/c² × c = γ m v_i -->
$$
p'^{0} \;=\; \gamma\,\frac{E}{c},
\qquad
p'^{i} \;=\; \gamma\,m\,v^{i},
$$

where γ = (1 − v²/c²)^(−1/2) and m = E/c² is the projected rest
mass from Section B.

The 4-momentum transforms exactly as a massive particle's would.
By the inertia-from-Lorentz-covariance argument of derivation-1
A.6.1, this means: pushing on the 2-torus (or equivalently,
pushing on the projected particle) requires a force F = dp/dt
that scales as γm × dv/dt — the standard relativistic inertia.

The 2-torus + photon system **is** a massive particle from the
4D point of view, with all the inertial properties we expect.
The argument did not use the specific 1D cavity geometry of
Track 1; only the existence of a rest frame for the cavity and
the fact that the photon's compact-direction momentum cancels
on average in that frame.  Both hold here:

- The rest frame for the 2-torus exists because the 2-torus is
  a rigid geometric object with definite 4D motion.
- The compact-direction momentum cancels on time-average in
  the rest frame because the photon is in a standing-wave
  state (closed orbit on the torus).

### E.2 — Why the photon-on-torus picture is the right model

> *Purpose: state the central conceptual claim of Program 1
> precisely, supported by what has been proven so far.*

A **6D null trajectory with nontrivial compact momentum
projects to a 4D massive trajectory.**  More specifically:

- The 4D 4-momentum p^μ satisfies the mass-shell relation
  with rest mass m given by the compact-momentum quadratic
  form (B.4).
- The projected particle has Lorentz-covariant inertia, just
  like any other massive particle (E.1).
- It carries U(1)×U(1) charges (Q_A, Q_B) ∝ (P_4, P_5)
  inherited from the compact momenta (derivation-2 D.3, F5).
- It feels Lorentz forces from each U(1) gauge field
  independently (derivation-2 E.2), with shear-induced
  cross-coupling (F6).
- Standing-wave quantization gives a discrete mass and
  charge spectrum (C.3).

The 6D entity is **light** (a null trajectory).  The 4D entity
is a **massive charged particle** (electron-like in its
qualitative features, with mass and charge both quantized
and the quanta linked to the same integer pair (n_4, n_5)).

This is the "electron from light" picture.  This derivation
does not yet show the projected particle has spin = ½ or
magnetic moment = eℏ/2m; those questions are taken up in
subsequent derivations.  The geometric framework that should
produce them — the sheared 2-torus with its U(1)×U(1) gauge
structure and its kinematic mass-charge mixing — is now
established.

### E.3 — A note on the photon's 6D speed

> *Purpose: head off a confusion that often arises with KK
> "particles from extra dimensions" pictures.*

The photon moves at the local 6D speed of light (its 6D
worldline is null).  Sometimes this is described as "the
photon zips around the extra dimensions," which can be
misleading: the compact dimensions are physically distinct
from the spacetime ones, not just very small spatial loops in
3+1.

A more precise statement: the 6D wave-4-vector k^A has a
spacetime part k^μ and a compact part (k^4, k^5).  The
magnitudes of these two parts are linked by the null condition
B.2: increasing one decreases the other, in such a way that
the total 6D inner product remains zero.  In the rest frame
of the 2-torus, the spacetime part of k^μ has only a temporal
component (no 3-velocity), and all of the "kinetic" content
sits in the compact part.  The photon is, in this sense,
"running in place" around the torus while not moving through
3-space — and the energy of that compact running is what we
read out as the rest mass.

This picture cleanly resolves the apparent paradox of "a
massless photon producing a massive particle."  The photon
is massless in the sense that its 6D worldline is null.  The
projected 4D particle is massive in the sense that its 4D
worldline is timelike with a definite, Lorentz-invariant rest
mass.  Both statements are true simultaneously and refer to
different objects: a 6D worldline vs its 4D projection.

---

## Lemma (Track 3 result)

We have shown:

> **(F7) Photon-on-2-torus mass formula (general).**  A
> photon — a null trajectory in 6D = M⁴ × T² — has a 4D
> projected rest mass m given by
>
> <!-- m²c² = h^ab P_a P_b -->
> $$
> m^{2}\,c^{2} \;=\; h^{ab}\,P_{a}\,P_{b},
> $$
>
> where h^ab is the inverse internal metric of the 2-torus
> and P_a are the two conserved compact momenta from
> derivation-2 D.2 (units of momentum, with ℏ absorbed into
> the definition).
>
> **(F8) Pythagorean mass formula (canonical case).**  When
> g_ab = δ_ab (no shear, equal-radii torus) and the standing-
> wave quantization gives P_a = n_a h/L:
>
> <!-- m = (h/Lc) √(n_4² + n_5²) -->
> $$
> m \;=\; \frac{h}{L\,c}\,\sqrt{n_{4}^{2} \;+\; n_{5}^{2}},
> \qquad n_{4}, n_{5} \in \mathbb{Z}.
> $$
>
> The 4D rest mass is the Euclidean magnitude (in standing-
> wave-quantum units) of the two compact momentum quanta.
>
> **(F9) Mass-charge mixing from shear.**  When g_45 ≠ 0, the
> mass formula h^ab P_a P_b has off-diagonal terms.  The
> principal-mass eigenstates (the basis that diagonalizes the
> mass formula) are linear combinations of the charge
> eigenstates (the basis in which P_4 and P_5 are diagonal).
> A pure-charge eigenstate (e.g. P_4 ≠ 0, P_5 = 0) is *not* a
> pure-mass eigenstate; the shear introduces a kinematic
> mixing between charge and mass that propagates into the
> standing-wave spectrum as the (n_r − s n_t)-style cross-
> term observed empirically in MaSt.
>
> **(F10) Inertia and Lorentz covariance.**  The projected
> particle has inertial mass equal to its rest energy divided
> by c²; its 4-momentum transforms as a single massive
> object's would under Lorentz boosts.  The cavity-photon
> argument of derivation-1 A.6 applies unchanged to the
> 2-torus case.

F7–F10 together equip the "electron from light" hypothesis
with a concrete, derived rest-mass formula (F7), a clean
canonical case showing the **Pythagorean structure** (F8),
the **mass-charge mixing** mechanism (F9) that connects the
geometry to MaSt's empirically-found mass formula, and the
**inertia** property (F10) that confirms the projected
particle behaves as a real massive object.
