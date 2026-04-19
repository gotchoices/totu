# Derivation 4 — Recovery of the MaSt mass formula

Show that the MaSt mass formula

<!-- μ² = (n_t/ε)² + (n_r − s n_t)² -->
$$
\mu^{2} \;=\; \left(\frac{n_{t}}{\varepsilon}\right)^{2}
        \;+\; \left(n_{r} - s\,n_{t}\right)^{2}
$$

— previously postulated in MaSt model-D / model-E and used to
fit the empirical particle inventory in R49 — is a derived
consequence of the photon-on-2-torus mass formula

<!-- m²c² = h^ab P_a P_b -->
$$
m^{2}\,c^{2} \;=\; h^{ab}\,P_{a}\,P_{b}
$$

(F7) with a specific parametrization of the 2×2 internal
metric in terms of the aspect ratio ε and shear s.  The
identification fixes the "shear" parameter s in MaSt
operationally as a specific function of the geometric
off-diagonal entry g_45 of the internal metric, and the
"aspect ratio" ε as the ratio of the two compact periods.

This closes the loop opened in F1 (confined photon → rest
mass) and continued in F4–F6 (KK on a 2-torus) and F7–F9
(photon on the 2-torus): MaSt's mass formula is no longer a
postulate.  It is what the photon-on-2-torus picture
*predicts*.

---

## Inputs

1. **F7** (photon-on-2-torus mass formula): m²c² = h^ab P_a P_b,
   where h^ab is the inverse of the 2×2 internal metric g_ab on
   the 2-torus and P_a are the conserved compact momenta (units
   of momentum).
2. **Standing-wave quantization** of the compact momenta:
   P_a = n_a h / L_a with n_a ∈ ℤ and L_a the compact period
   in direction a.
3. **MaSt's empirical mass formula** as the target: stated above.
4. **Convention** — to be made explicit and motivated in
   Section B: the index 4 is "tube" (the smaller compact
   direction) and 5 is "ring" (the larger), with L_4 = L_t,
   L_5 = L_r = ε L_t.

No new physics is introduced.  This derivation is pure algebra
on F7 plus a parametrization choice.

---

## Section A — The two formulas side by side

### A.1 — Expand F7 with standing-wave quantization

> *Purpose: get F7 into a form directly comparable with MaSt's
> formula — a quadratic form in two integers.*

Substitute P_a = n_a h / L_a into m²c² = h^ab P_a P_b and write
out the three terms (h^44 n_4², 2 h^45 n_4 n_5, h^55 n_5²):

<!-- m²c² = h² × [h^44 n_4²/L_4² + 2 h^45 n_4 n_5/(L_4 L_5) + h^55 n_5²/L_5²] -->
$$
m^{2}\,c^{2}
\;=\; h^{2}\!\left[
    \frac{h^{44}\,n_{4}^{2}}{L_{4}^{2}}
    \;+\; \frac{2\,h^{45}\,n_{4}\,n_{5}}{L_{4}\,L_{5}}
    \;+\; \frac{h^{55}\,n_{5}^{2}}{L_{5}^{2}}
    \right].
$$

Two natural scales appear: h/L_4 and h/L_5 (each with units of
momentum).  Their ratio L_5/L_4 will become the aspect ratio
ε.  Their absolute scales factor out as the overall mass
units.

### A.2 — Expand MaSt's formula as a quadratic form

> *Purpose: get MaSt's formula into the same shape so coefficient
> matching is mechanical.*

Expand μ² = (n_t/ε)² + (n_r − s n_t)²:

<!-- μ² = n_t²(1/ε² + s²) + n_r² − 2 s n_t n_r -->
$$
\mu^{2}
\;=\; n_{t}^{2}\!\left(\tfrac{1}{\varepsilon^{2}} + s^{2}\right)
\;+\; n_{r}^{2}
\;-\; 2\,s\,n_{t}\,n_{r}.
$$

Three coefficients to match:

| Term | MaSt coefficient |
|------|------------------|
| n_t² | 1/ε² + s² |
| n_r² | 1 |
| n_t n_r | −2 s |

Note that the coefficient of n_t² is *larger* than that of n_r²
(when ε > 1) — the "tube" quantum number n_t carries more mass
per unit excitation than the "ring" n_r.  This is the
counterintuitive feature of MaSt's parametrization: the
short-period direction (the one with higher Compton-like mass
scale h/L_t) is naturally associated with a larger contribution
to μ².

---

## Section B — Convention choice

### B.1 — Assignment of compact directions

> *Purpose: state the convention that ties the abstract
> 2-torus indices (4, 5) to MaSt's tube/ring labels.*

We adopt the assignment

<!-- 4 ↔ tube,  5 ↔ ring -->
$$
\text{index 4} \;\longleftrightarrow\; \text{tube} \quad(n_{4} = n_{t}),
\qquad
\text{index 5} \;\longleftrightarrow\; \text{ring} \quad(n_{5} = n_{r}),
$$

with compact periods

<!-- L_4 = L_t,  L_5 = L_r = ε L_t -->
$$
L_{4} \;=\; L_{t}, \qquad L_{5} \;=\; L_{r} \;=\; \varepsilon\,L_{t},
$$

so that the **aspect ratio**

<!-- ε ≡ L_r / L_t -->
$$
\varepsilon \;\equiv\; \frac{L_{r}}{L_{t}}
$$

is the ratio of the larger to the smaller compact period.  The
physical interpretation of "tube" and "ring" is taken from
MaSt: the tube is the smaller compact direction (small
cross-section radius of a torus) and the ring is the larger
(the main loop).  For the electron sheet, R53 finds ε of order
10² to 10³, so ε ≫ 1 in practical cases.

The opposite assignment (4 ↔ ring, 5 ↔ tube) would give a
relabeled-but-equivalent parametrization; the choice above is
made to match MaSt's convention literally so that n_4 = n_t and
n_5 = n_r without index gymnastics in the final formula.

### B.2 — Mass scale

> *Purpose: pick the natural overall mass unit.*

Substitute L_4 = L_t and L_5 = ε L_t into A.1's expansion:

<!-- m²c² = (h/L_t)² × [h^44 n_t² + 2 h^45 n_t n_r/ε + h^55 n_r²/ε²] -->
$$
m^{2}\,c^{2}
\;=\; \left(\frac{h}{L_{t}}\right)^{\!2}\!\left[
       h^{44}\,n_{t}^{2}
    \;+\; \frac{2\,h^{45}\,n_{t}\,n_{r}}{\varepsilon}
    \;+\; \frac{h^{55}\,n_{r}^{2}}{\varepsilon^{2}}
    \right].
$$

The natural mass scale is h/(L_t c) — the Compton-like mass
associated with the smaller compact period.  Define

<!-- M ≡ h / (L_t c) -->
$$
M \;\equiv\; \frac{h}{L_{t}\,c}.
$$

Then m²c² = M² c² × [bracketed expression], so

<!-- (m/M)² = h^44 n_t² + 2 h^45 n_t n_r/ε + h^55 n_r²/ε² -->
$$
\left(\frac{m}{M}\right)^{\!2}
\;=\; h^{44}\,n_{t}^{2}
\;+\; \frac{2\,h^{45}\,n_{t}\,n_{r}}{\varepsilon}
\;+\; \frac{h^{55}\,n_{r}^{2}}{\varepsilon^{2}}.
$$

We will identify the dimensionless ratio m/M with MaSt's μ in
the next section.

---

## Section C — Solving for the metric

### C.1 — Coefficient equations

> *Purpose: equate the expansion from B.2 with MaSt's quadratic
> form from A.2 term by term.*

Setting (m/M)² ≡ μ² and matching the coefficients of n_t², n_r²,
and n_t n_r between B.2 and A.2:

<!-- h^44 = 1/ε² + s²  (n_t² coefficient) -->
$$
h^{44} \;=\; \tfrac{1}{\varepsilon^{2}} + s^{2}, \tag{C1}
$$

<!-- h^55/ε² = 1  (n_r² coefficient) -->
$$
\frac{h^{55}}{\varepsilon^{2}} \;=\; 1
\;\;\Longrightarrow\;\;
h^{55} \;=\; \varepsilon^{2}, \tag{C2}
$$

<!-- 2 h^45 / ε = -2s  (n_t n_r coefficient) -->
$$
\frac{2\,h^{45}}{\varepsilon} \;=\; -2\,s
\;\;\Longrightarrow\;\;
h^{45} \;=\; -\varepsilon\,s. \tag{C3}
$$

So the inverse internal metric has components

<!-- h^ab = [[1/ε² + s², -ε s], [-ε s, ε²]] -->
$$
h^{ab}
\;=\;
\begin{pmatrix}
\tfrac{1}{\varepsilon^{2}} + s^{2} & -\varepsilon\,s \\[4pt]
-\varepsilon\,s & \varepsilon^{2}
\end{pmatrix}.
$$

### C.2 — The internal metric g_ab

> *Purpose: invert h^ab to get g_ab, completing the
> parametrization.*

Determinant of h^ab:

<!-- det h^ab = (1/ε² + s²) × ε² - (-ε s)² = 1 + s²ε² - s²ε² = 1 -->
$$
\det h^{ab}
\;=\; \left(\tfrac{1}{\varepsilon^{2}} + s^{2}\right)\varepsilon^{2}
   \;-\; (-\varepsilon\,s)^{2}
\;=\; 1 + s^{2}\varepsilon^{2} - s^{2}\varepsilon^{2}
\;=\; 1.
$$

A clean normalization: **det h^ab = 1**, equivalently
**det g_ab = 1** (since the determinant of an inverse is the
inverse of the determinant).

With det = 1, the inverse of h^ab is just the cofactor matrix:

<!-- g_ab = [[ε², ε s], [ε s, 1/ε² + s²]] -->
$$
\boxed{\;
g_{ab}
\;=\;
\begin{pmatrix}
\varepsilon^{2} & \varepsilon\,s \\[4pt]
\varepsilon\,s & \tfrac{1}{\varepsilon^{2}} + s^{2}
\end{pmatrix}
\;}
$$

In components:

<!-- g_44 = ε² (tube),  g_55 = 1/ε² + s² (ring),  g_45 = ε s (shear) -->
$$
g_{44} \;=\; \varepsilon^{2},
\qquad
g_{55} \;=\; \tfrac{1}{\varepsilon^{2}} + s^{2},
\qquad
g_{45} \;=\; \varepsilon\,s.
$$

This is the **MaSt parametrization** of the 2×2 internal metric:
the metric g_ab is uniquely determined by the two parameters
(ε, s) once the convention from B.1 is fixed.

### C.3 — Sanity check by direct substitution

> *Purpose: verify the parametrization reproduces MaSt's formula
> without any algebra slip.*

Substitute g_ab from C.2 (or equivalently h^ab from C.1) and
P_a = n_a h/L_a from inputs into m²c² = h^ab P_a P_b.  Use
L_4 = L_t, L_5 = ε L_t:

$$
m^{2}\,c^{2}
\;=\; \left(\tfrac{1}{\varepsilon^{2}} + s^{2}\right)\!
        \left(\frac{n_{t}\,h}{L_{t}}\right)^{\!2}
\;+\; 2(-\varepsilon\,s)\!
        \left(\frac{n_{t}\,h}{L_{t}}\right)\!
        \left(\frac{n_{r}\,h}{\varepsilon\,L_{t}}\right)
\;+\; \varepsilon^{2}\!
        \left(\frac{n_{r}\,h}{\varepsilon\,L_{t}}\right)^{\!2}.
$$

Simplify each term by pulling out (h/L_t)²:

$$
m^{2}\,c^{2}
\;=\; \left(\frac{h}{L_{t}}\right)^{\!2}\!\left[
       \left(\tfrac{1}{\varepsilon^{2}} + s^{2}\right)\,n_{t}^{2}
   \;-\; 2\,s\,n_{t}\,n_{r}
   \;+\; n_{r}^{2}
   \right].
$$

Divide both sides by M² c² = (h/L_t)²:

$$
\left(\frac{m}{M}\right)^{\!2}
\;=\; \left(\tfrac{1}{\varepsilon^{2}} + s^{2}\right)\,n_{t}^{2}
\;-\; 2\,s\,n_{t}\,n_{r}
\;+\; n_{r}^{2}.
$$

Recognize the right-hand side as MaSt's expansion (A.2) and
re-collapse it:

<!-- (m/M)² = (n_t/ε)² + (n_r - s n_t)² -->
$$
\boxed{\;
\left(\frac{m}{M}\right)^{\!2}
\;=\; \left(\frac{n_{t}}{\varepsilon}\right)^{\!2}
   \;+\; (n_{r} - s\,n_{t})^{2}
\;}
$$

This is **MaSt's mass formula** verbatim, with the
identification

<!-- μ ≡ m/M, where M = h/(L_t c) -->
$$
\mu \;\equiv\; \frac{m}{M},
\qquad M \;=\; \frac{h}{L_{t}\,c}.
$$

The MaSt parameters (ε, s) and the dimensionless mass μ are
now operationally defined in terms of geometric quantities of
the 2-torus.

---

## Section D — Geometric interpretation

### D.1 — The aspect ratio ε

> *Purpose: identify ε with a directly geometric quantity.*

By construction (B.1):

<!-- ε = L_r / L_t -->
$$
\varepsilon \;=\; \frac{L_{r}}{L_{t}},
$$

the ratio of the ring-direction compact period to the
tube-direction compact period.  When ε ≫ 1, the ring is much
longer than the tube — the 2-torus is an "elongated" cylinder
with a small cross-section.  When ε = 1, the two compact
directions are equally long (and the metric reduces to
g_44 = 1, g_55 = 1 + s², g_45 = s — a sheared square torus).

The mass scale M = h/(L_t c) is set by the *tube* (the smaller
period).  Particles whose mass is dominated by the n_t
contribution have mass of order M; those dominated by the n_r
contribution have mass of order M/ε (smaller, scaling
inversely with ε).

### D.2 — The shear s and its relation to derivation-2's shear

> *Purpose: identify what s "is" in geometric terms, and
> reconcile MaSt's s with the dimensionless shear parameter
> introduced in F6.*

The MaSt shear s appears in two places of the parametrization:

- In the off-diagonal metric entry: g_45 = ε s.
- In the diagonal entry of the ring direction:
  g_55 = 1/ε² + s² (as a quadratic correction).

The **dimensionless shear** of derivation-2 was defined as

<!-- s_geom ≡ g_45 / √(g_44 g_55) -->
$$
s_{\text{geom}}
\;\equiv\; \frac{g_{45}}{\sqrt{g_{44}\,g_{55}}}.
$$

Substituting our parametrization:

<!-- s_geom = ε s / √(ε² × (1/ε² + s²)) = ε s / √(1 + ε² s²) -->
$$
s_{\text{geom}}
\;=\; \frac{\varepsilon\,s}{\sqrt{\varepsilon^{2}\!\left(\tfrac{1}{\varepsilon^{2}} + s^{2}\right)}}
\;=\; \frac{\varepsilon\,s}{\sqrt{1 + \varepsilon^{2}\,s^{2}}}.
$$

So MaSt's s and the derivation-2 dimensionless shear s_geom are
**not the same parameter**.  They are related by

<!-- s_geom = εs / √(1 + ε²s²)  ↔  εs = s_geom / √(1 - s_geom²) -->
$$
\boxed{\;
s_{\text{geom}} \;=\; \frac{\varepsilon\,s}{\sqrt{1 + \varepsilon^{2}\,s^{2}}}
\quad\Longleftrightarrow\quad
\varepsilon\,s \;=\; \frac{s_{\text{geom}}}{\sqrt{1 - s_{\text{geom}}^{\,2}}}
\;}
$$

For small ε s (i.e., ε s ≪ 1):

<!-- s_geom ≈ ε s -->
$$
s_{\text{geom}} \;\approx\; \varepsilon\,s
\quad (\varepsilon\,s \ll 1).
$$

Geometric meaning of MaSt's s: when ε s is small, MaSt's shear
is the geometric off-diagonal entry of the 2×2 internal
metric, divided by ε — equivalently, "shear per unit aspect
ratio."

When ε s is *not* small (e.g., ε ≫ 1 with s of order 1/ε or
larger), s_geom approaches the saturation limit |s_geom| < 1
of derivation-2's positivity constraint.  This is a real
geometric constraint: the 2×2 internal block must remain
positive definite, which translates to |s_geom| < 1 for any
real (ε, s) — and that constraint is automatically satisfied
by the parametrization C.2 (since
1 + ε²s² > ε²s² always, so |s_geom| < 1 always).

### D.3 — Equivalent parametrizations under coordinate
choices

> *Purpose: note that the specific form g_44 = ε², g_55 =
> 1/ε² + s², g_45 = ε s is one coordinate choice among many.
> Other choices give different-looking but equivalent metrics.*

The intrinsic geometry of the 2-torus is fixed by (ε, s) and
the lattice; the *components* g_ab depend on the coordinates
used to describe it.  The C.2 parametrization corresponds to
coordinates (x^4, x^5) with periods (L_t, ε L_t).  Two other
useful choices:

**(a) Equal compact periods.**  Define rescaled coordinates
y^4 = ε x^4 with period y^4 ∈ [0, ε L_t).  Then both compact
periods become ε L_t, and the metric transforms as
g'_44 = g_44/ε² = 1, g'_55 = g_55, g'_45 = g_45/ε = s.  The
resulting metric

$$
g'_{ab}
\;=\;
\begin{pmatrix}
1 & s \\[2pt]
s & \tfrac{1}{\varepsilon^{2}} + s^{2}
\end{pmatrix}
$$

has g'_44 = 1 (Euclidean-like in the tube direction) and the
same det = 1/ε².  Both forms produce the same μ², just via
different coordinate paths.

**(b) Intrinsically-flat sheared lattice.**  In some Cartesian-
like (X, Y) plane, place lattice basis vectors

$$
\mathbf{E}_{t} \;=\; (1/\varepsilon,\; -s),
\qquad
\mathbf{E}_{r} \;=\; (0,\; 1).
$$

Then |E_t|² = 1/ε² + s², |E_r|² = 1, E_t · E_r = −s.  The
metric in this basis is

$$
g''_{ab}
\;=\;
\begin{pmatrix}
\tfrac{1}{\varepsilon^{2}} + s^{2} & -s \\[2pt]
-s & 1
\end{pmatrix},
$$

and the lattice points are {n_t E_t + n_r E_r : n_t, n_r ∈ ℤ}.
The squared lattice-vector lengths are exactly μ² in MaSt
units:

$$
|n_{t}\,\mathbf{E}_{t} + n_{r}\,\mathbf{E}_{r}|^{2}
\;=\; n_{t}^{2}\!\left(\tfrac{1}{\varepsilon^{2}} + s^{2}\right)
\;-\; 2\,s\,n_{t}\,n_{r}
\;+\; n_{r}^{2}
\;=\; \mu^{2}.
$$

This is the cleanest *intrinsic* picture: **MaSt's mass formula
is the squared length of the lattice vector (n_t, n_r) on a
flat 2-torus with basis vectors (1/ε, −s) and (0, 1)**.  The
aspect ratio ε is the inverse of |E_t|'s V₁-component; the
shear s is minus E_t's V₂-component (equivalently, minus
E_t · E_r when |E_r| = 1).

All three parametrizations are coordinate-equivalent on the
same physical 2-torus.

---

## Section E — Worked example: lowest mass eigenvalues

### E.1 — Mass spectrum for example (ε, s)

> *Purpose: show concretely how the formula generates a discrete
> mass spectrum, and check that it produces sensible
> structure.*

Pick ε = 13 (electron-sheet-like, a representative R49 value)
and s = 0.1 (modest shear) for concreteness.  The dimensionless
mass squared is

$$
\mu^{2}(n_{t}, n_{r})
\;=\; \left(\frac{n_{t}}{13}\right)^{\!2} + (n_{r} - 0.1\,n_{t})^{2}.
$$

Tabulate the lowest few states sorted by μ² ascending.  The
notation "(n_t, n_r) ∼" denotes the sign-aligned case where
n_t and n_r have the same sign (so that −s n_t n_r is
negative, lowering μ²); "(n_t, n_r) ≁" denotes opposite signs
(raising μ²).

| State | (n_t/ε)² | (n_r − s n_t)² | μ² | μ |
|-------|----------|----------------|------|----|
| (0, 0) | 0 | 0 | 0 | 0 |
| (±1, 0) | 0.0059 | 0.01 | 0.0159 | 0.126 |
| (±2, 0) | 0.0237 | 0.04 | 0.0637 | 0.252 |
| (±1, ±1) ∼ | 0.0059 | 0.81 | 0.816 | 0.903 |
| (0, ±1) | 0 | 1 | 1 | 1 |
| (±1, ±1) ≁ | 0.0059 | 1.21 | 1.216 | 1.103 |
| (±1, ±2) ∼ | 0.0059 | 3.61 | 3.616 | 1.902 |
| (0, ±2) | 0 | 4 | 4 | 2 |
| (±1, ±2) ≁ | 0.0059 | 4.41 | 4.416 | 2.101 |

Two qualitative features:

- **Degeneracies are lifted by the shear.**  In the unsheared
  Pythagorean case (s = 0), states (n_t, ±n_r) and (n_t, ∓n_r)
  would be exactly degenerate.  The shear breaks this: e.g.,
  (1, 1) has μ² ≈ 0.815 while (1, −1) has μ² ≈ 1.215.  The
  splitting is of order 4 s n_t n_r — small for small s but
  meaningful for excited states.
- **Tube excitations are very light.**  States with n_r = 0
  and n_t = 1, 2, ... have μ ≈ n_t/ε — much smaller than M.
  This is the "tube ladder" of light modes that MaSt predicts
  on each sheet.

### E.2 — The s = 0 limit

> *Purpose: confirm the s → 0 limit reproduces the Pythagorean
> result of F8 with appropriate aspect-ratio scaling.*

Set s = 0 in MaSt's formula: μ² = (n_t/ε)² + n_r².

Compare to F8's canonical Pythagorean (equal radii L_4 = L_5 = L,
no shear): m c = (h/L) √(n_4² + n_5²), i.e., μ_F8² = n_4² + n_5².

The two formulas agree if we identify n_4 = n_t/ε and n_5 = n_r —
i.e., the tube quantum number is rescaled by 1/ε due to the
asymmetric periods L_t ≠ L_r.  The ε in MaSt's formula thus
encodes the period asymmetry that F8's canonical case
deliberately set to unity.

The Pythagorean structure of F8 is preserved in MaSt's formula:
both are sums of two squares of integer-linear combinations.
The shear s rotates and stretches the basis of the 2D lattice
(D.3) but leaves the "sum of squares" structure intact.

### E.3 — Limits and constraints

- **No mass gap (vacuum).**  (n_t, n_r) = (0, 0) gives μ = 0:
  the 4D photon (massless mode) is automatically present in
  the spectrum.
- **Lightest charged mode.**  The lowest |n_t| with n_t ≠ 0 is
  |n_t| = 1.  Its mass is at most √(1/ε² + s²) (with n_r = 0)
  or somewhat less for optimal n_r.
- **Heaviest "ground state" of n_r tower.**  At n_r = 1 with
  n_t = 0, μ = 1 (one unit of M).  This is the "ring ladder."
- **Degeneracy preservation under (n_t, n_r) → (−n_t, −n_r).**
  μ²(n_t, n_r) = μ²(−n_t, −n_r) since both terms are squared.
  So states with charge +Q_A and −Q_A have identical mass —
  the particle/antiparticle mass equality is automatic.

---

## Section F — What this establishes

### F.1 — MaSt's mass formula is no longer a postulate

> *Purpose: state the central result of this derivation
> precisely.*

The formula μ² = (n_t/ε)² + (n_r − s n_t)², which model-D /
model-E adopted as an empirical postulate fitted to the
particle inventory, is a **derived consequence** of:

1. The Kaluza-Klein hypothesis (compact extra dimensions, F4).
2. The cylinder condition (compact directions don't probe
   field variation, F4).
3. The Planck-Einstein relation (E = ℏω, used in F1 and F7).
4. The standing-wave boundary condition on compact directions
   (single-valuedness of the wavefunction).
5. The choice of two compact dimensions (a 2-torus).
6. The convention that index 4 is "tube" (smaller period),
   index 5 is "ring" (larger period).

No additional postulates.  The formula is fixed up to the choice
of (ε, s) (two real parameters per sheet, plus the overall
mass scale M = h/(L_t c)).

### F.2 — The geometric meaning of (ε, s)

| MaSt parameter | Geometric meaning |
|----------------|-------------------|
| ε | Ratio of compact periods L_r / L_t (aspect ratio of the 2-torus) |
| s | Off-diagonal entry of the 2×2 internal metric, normalized: g_45 = ε s with the metric in the C.2 form.  Equivalently, g_45 / ε² in the equal-period parametrization (D.3a).  Equivalently, minus the V₂-component of the tube basis vector E_t = (1/ε, −s) in the intrinsically-flat picture (D.3b). |
| M | Compton-like mass scale h/(L_t c) of the smaller compact direction |
| s_geom | Derivation-2's dimensionless shear g_45/√(g_44 g_55) = εs/√(1 + ε²s²), automatically less than 1 |

### F.3 — What is *not* derived here

This derivation pins down the parametrization (ε, s) ↔ g_ab(ε,
s) and recovers MaSt's mass formula.  It does **not**
determine:

- The numerical values of (ε, s) for the three MaSt sheets.
  Those are inputs from R49 / R53 / model-D, fitted to the
  particle inventory.  This derivation just shows the *form*
  is right.
- The overall mass scale M.  This is set by L_t, the smaller
  compact period — which corresponds to the Compton wavelength
  of the lightest excitation on the sheet.  Determining L_t
  from first principles is a separate question (handled in
  R59 and the GRID derivation).
- The assignment of which compact direction is "tube" and
  which is "ring."  This is a convention; we adopted MaSt's
  here.  Reversing the assignment swaps the roles of (n_t, n_r)
  in the formula but produces an equivalent quadratic form.
- The role of the magnetic-moment / spin / charge
  identifications.  Those are separate derivations.

The result is structural: MaSt has the right mass formula
*structure*; the inputs (ε, s, M) are still empirical fits to
known particle data.

---

## Lemma (Track 4 result)

We have shown:

> **(F11) Recovery of MaSt's mass formula.**  Substituting the
> parametrization
>
> $$
> g_{44} \;=\; \varepsilon^{2},
> \qquad
> g_{55} \;=\; \tfrac{1}{\varepsilon^{2}} + s^{2},
> \qquad
> g_{45} \;=\; \varepsilon\,s
> $$
>
> (with det g_ab = 1) into the photon-on-2-torus mass formula
> m²c² = h^ab P_a P_b (F7), with the convention 4 ↔ tube,
> 5 ↔ ring, L_4 = L_t, L_5 = ε L_t, recovers the MaSt formula
>
> $$
> \mu^{2} \;=\; \left(\frac{n_{t}}{\varepsilon}\right)^{\!2}
>          \;+\; (n_{r} - s\,n_{t})^{2},
> \qquad
> \mu \;\equiv\; \frac{m\,L_{t}\,c}{h},
> $$
>
> identically and exactly.
>
> **(F12) Geometric meaning of MaSt's parameters.**
>
> - **ε** is the aspect ratio L_r / L_t — the ratio of the
>   ring compact period to the tube compact period.
> - **s** is the off-diagonal entry of the 2×2 internal metric,
>   normalized by the aspect ratio: g_45 = ε s.
> - The dimensionless Killing-momentum shear of F6,
>   s_geom = g_45/√(g_44 g_55), is related to MaSt's s by
>   s_geom = ε s / √(1 + ε² s²); the two coincide only in the
>   limit ε s ≪ 1.
> - The overall mass scale M = h/(L_t c) is the Compton-like
>   mass associated with the smaller compact period.
>
> **(F13) Mode spectrum.**  The mass spectrum
> {μ(n_t, n_r) : n_t, n_r ∈ ℤ} is a discrete set determined
> entirely by (ε, s).  It includes a massless mode (the 4D
> photon at n_t = n_r = 0), a "tube ladder" of light modes
> (n_t ≠ 0, n_r = 0, masses ∼ n_t/ε), a "ring ladder" of
> heavier modes (n_t = 0, n_r ≠ 0, masses ∼ n_r), and a
> 2D grid of mixed modes whose degeneracies are lifted by the
> shear.

The "electron-from-light" hypothesis now has a complete mass
formula derived from first principles.  What remains is:
identifying which compact direction carries electric charge,
deriving the spin assignment from the cross-coupling, and
extending the construction across the three MaSt sheets with
their inter-sheet shears.
