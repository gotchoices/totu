# α and R sit on orthogonal axes of K–V parameter space

GRID's one electromagnetic input is the dimensionless coupling α ≈ 1/137.
Losinets's one electromagnetic input is the K–V relaxation time R ≡ τ_KV =
η₀/G = ν₀/c². Earlier trilogy notes (and the original C4 punch-list item)
asked whether the two could be the same dial in different clothing — i.e.
whether α = f(R · ω_Planck) for some clean dimensionless combination.

This note works the algebra. The answer:

> Within Losinets's own correspondence table, **R drops out of α**. The
> parameters that determine α in K–V language are (ρ₀, r₀, m_vac) plus
> the universal constants (ℏ, c). R fixes the viscoelastic time and
> thereby the SI–to–mechanical conversion (it carries the "s" in
> A = R·u), but it cancels from the dimensionless ratio α.

The two dials are logically independent inputs to the same parameter
space. Both frameworks remain "one-dial-per-framework"; the dials are
not two names for the same number.

A conditional escape — outcome #2 of the ticket — is available *if and
only if* Losinets's open ring-energy closure (photon §2.4) is solved.
That is laid out in §4 below as a contingent result, not a derivation.

This document supersedes the speculative §C4 ("α from R") of
[`losinets/losinets-trilogy.md`](../losinets/losinets-trilogy.md).

---

## 1. The two single dials

| Framework | Single EM dial | Units | What it sets |
|---|---|---|---|
| GRID | α | dimensionless | Energy cost of a unit topological winding (axiom A6). All of Maxwell's coupling structure follows. |
| Losinets (K–V vacuum) | R = η₀/G = ν₀/c² | s | Viscoelastic relaxation time of the medium. Carries the "second" that converts mechanical units (m, kg, s) to SI EM units (V, T, A). |
| MaSt | α (inherited from GRID) | dimensionless | Same as GRID; MaSt does not introduce a new EM coupling. |

Both α and R are the *minimum* inputs to their respective frameworks
once Maxwell's equations are derived. Neither paper writes the bridge
between them. Here we work it.

---

## 2. The K–V correspondence (recap)

From Losinets EfD §7.4 (Table 1), the EM ↔ K–V dictionary is:

| SI EM quantity | K–V analogue | Mechanical units |
|---|---|---|
| Permittivity ε₀ | ρ₀ (bulk mass density) | kg·m⁻³ |
| Permeability μ₀ | 1/(ρ₀c²) = 1/G | m·s²·kg⁻¹ |
| Vector potential A | R·u (with u solenoidal velocity) | m |
| Charge Q | ρ₀ · r₀ · Γ | kg·s⁻¹ |
| Circulation Γ (Onsager–Feynman) | n·h/m_vac | m²·s⁻¹ |
| Relaxation time R = τ_KV | η₀/G = ν₀/c² | s |
| Wave speed | √(G/ρ₀) = c | m·s⁻¹ |

Two facts to mark:

- **m_vac is not derived.** It is the effective medium-quantum mass
  appearing in the imported Onsager–Feynman quantisation Γ = h/m_vac.
  Photon §2.4 explicitly flags determination of m_vac from K–V elastic
  ring energy as an open problem.
- **R appears only via A = R·u.** R is the conversion factor that gives
  the vector potential SI units (V·s·m⁻¹) from a mechanical velocity
  (m·s⁻¹). It does not enter Q, Γ, ρ₀, c, or any other quantity in the
  table independently.

---

## 3. Translating α into K–V parameters

The SI definition of the fine-structure constant is:

<!-- α = e² / (4π ε₀ ℏ c) -->
$$
\alpha \;=\; \frac{e^{2}}{4\pi\,\varepsilon_{0}\,\hbar\,c}
$$

Substitute the K–V identifications **e ↔ Q = ρ₀·r₀·Γ** and
**ε₀ ↔ ρ₀**:

<!-- α = (ρ₀ r₀ Γ)² / (4π ρ₀ ℏ c) = ρ₀ r₀² Γ² / (4π ℏ c) -->
$$
\alpha \;=\; \frac{(\rho_{0}\,r_{0}\,\Gamma)^{2}}{4\pi\,\rho_{0}\,\hbar\,c}
       \;=\; \frac{\rho_{0}\,r_{0}^{2}\,\Gamma^{2}}{4\pi\,\hbar\,c}
$$

Now substitute the Onsager–Feynman quantisation **Γ = h/m_vac =
2πℏ/m_vac** (n = 1):

<!-- α = ρ₀ r₀² (2π ℏ / m_vac)² / (4π ℏ c) = π ρ₀ r₀² ℏ / (m_vac² c) -->
$$
\boxed{\;\alpha \;=\; \frac{\pi\,\rho_{0}\,r_{0}^{2}\,\hbar}{m_{\text{vac}}^{2}\,c}\;}
$$

Equivalently, with the "medium Compton length" L_vac ≡ ℏ/(m_vac·c):

<!-- α = (r₀/L_vac)² · (π ρ₀ L_vac³ / m_vac) -->
$$
\alpha \;=\; \Bigl(\frac{r_{0}}{L_{\text{vac}}}\Bigr)^{\!2}
          \cdot \frac{\pi\,\rho_{0}\,L_{\text{vac}}^{3}}{m_{\text{vac}}}
$$

The first factor is a geometric ratio (core size to medium Compton
length); the second factor is π times the dimensionless number density
of medium quanta inside one L_vac³ box.

### 3.1 R does not appear

R = η₀/G enters the K–V derivation only through the substitution
A = R·u that converts a mechanical velocity field to an SI vector
potential. In the dimensionless ratio α, the SI factors of "s" cancel:

- Q = ρ₀·r₀·Γ and ε₀ = ρ₀ are both written without R.
- ℏ and c are universal.
- Γ = h/m_vac is written without R.

So α is determined by the substrate parameters (ρ₀, r₀, m_vac) plus
universal constants. R lives on a different axis: it sets the
relaxation time of the medium, which controls dissipation of A and the
effective viscous correction to the source-free Maxwell equations
(§4.6 EfD), but it leaves α untouched.

### 3.2 Dimensional audit

[ρ₀] = kg·m⁻³, [r₀²] = m², [ℏ] = kg·m²·s⁻¹, [m_vac²] = kg², [c] = m·s⁻¹.

<!-- [ρ₀ r₀² ℏ / (m_vac² c)] = (kg·m⁻³)(m²)(kg·m²·s⁻¹) / (kg² · m·s⁻¹) = dimensionless -->
$$
\frac{[\rho_0][r_0^{2}][\hbar]}{[m_{\text{vac}}^{2}][c]}
= \frac{(\text{kg}\,\text{m}^{-3})(\text{m}^{2})(\text{kg}\,\text{m}^{2}\,\text{s}^{-1})}
       {(\text{kg}^{2})(\text{m}\,\text{s}^{-1})}
= 1.
$$

Confirmed dimensionless.

### 3.3 Sanity plug at the Planck scale

Set (ρ₀, r₀, m_vac) = (m_P/L_P³, L_P, m_P) and use ℏ = c = 1 in Planck
units. Then

<!-- α_Planck = π · (m_P/L_P³) · L_P² · ℏ / (m_P² · c) = π · ℏ / (m_P · c · L_P) = π -->
$$
\alpha_{\text{Planck-substrate}}
   \;=\; \pi \cdot \frac{(m_P/L_P^{3})\,L_P^{2}\,\hbar}{m_P^{2}\,c}
   \;=\; \frac{\pi\,\hbar}{m_P\,c\,L_P}
   \;=\; \pi
$$

(using ℏ/(m_P c L_P) = 1 by definition of the Planck mass). So a fully
Planckian K–V medium gives α ~ O(1), not α ≈ 1/137. To match the
measured α the formula requires non-Planckian inputs:

- holding ρ₀ = ρ_P and r₀ = L_P forces m_vac² = 137π · m_P², i.e.
  m_vac ≈ 20.7 m_P — a heavier-than-Planck medium quantum, or
- holding m_vac = m_P forces ρ₀·r₀² ≈ 1/(137π) (Planck units), i.e. a
  rarefied substrate or sub-Planck core, or
- some combination.

**Take-away:** the formula is dimensionally self-consistent and
numerically defensible, but pinning α to the measured 1/137 still
requires choosing two of the three inputs (ρ₀, r₀, m_vac) from outside
Losinets's framework. GRID does not provide them either — the lattice
spacing fixes a length scale (L_P) but not the K–V density or core
radius the formula needs.

---

## 4. Conditional outcome #2 — the ring-energy closure escape

Losinets photon §2.4 records as an open problem:

> "A complete quantitative check — computing the K–V elastic energy of
> the ring and verifying E_ring = ℏω — would fix m_vac in terms of c,
> G, and ν₀, and remains an open problem."

If that closure is achieved, then m_vac becomes a function of (ρ₀, c,
ν₀), or equivalently (ρ₀, c, R·c²). Pure dimensional analysis fixes
the only possible form (up to a dimensionless prefactor κ):

<!-- m_vac = κ · ρ₀ · c³ · R³ -->
$$
m_{\text{vac}} \;=\; \kappa\,\rho_{0}\,c^{3}\,R^{3}.
$$

Dimensional check: [ρ₀ c³ R³] = (kg·m⁻³)(m³·s⁻³)(s³) = kg ✓.

Substituting into the boxed α:

<!-- α = π r₀² ℏ / (κ² ρ₀ c⁷ R⁶) -->
$$
\alpha \;=\; \frac{\pi\,r_{0}^{2}\,\hbar}{\kappa^{2}\,\rho_{0}\,c^{7}\,R^{6}}
$$

So **conditional on the §2.4 closure**, α and R are related — but the
relation also pulls in r₀ and ρ₀ as free parameters. This is not the
outcome-#1 form `α = (factor) · R · ω_P`; it is a two-parameter
relation `α = α(R, r₀; ρ₀, c)` that depends on an open derivation.

Status: speculative. Record but do not rely on.

---

## 5. The ticket's μ₀/G_shear warning — a unit-mixing error

The original ticket flagged:

> "Using μ₀ = 4π × 10⁻⁷ H/m and treating G as spacetime shear modulus
> ≈ c⁴/(8πG_N) gives R ≈ 1.5 × 10⁻¹²⁶ s — absurdly small."

The reason this is absurd is that **the substitution is dimensionally
incoherent**, not that R is small.

Dimensional check:

- [μ₀] = H·m⁻¹ = kg·m·A⁻²·s⁻²
- [G_shear] = Pa = kg·m⁻¹·s⁻²
- [μ₀ / G_shear] = (kg·m·A⁻²·s⁻²) · (m·s²·kg⁻¹) = **m²·A⁻²**

That is not seconds. The naive ratio is in units of m²/A², so the
"1.5 × 10⁻¹²⁶ s" is a unit error masquerading as a number.

The K–V identification "μ₀ ↔ 1/G" in EfD Table 1 is an identification
*within* the K–V mechanical-units column, not an SI cross-substitution.
Reading it as an SI equivalence is the mistake.

### 5.1 Corrected Planck-scale R estimate

In Planck units (ℏ = c = G_N = 1):

- Spacetime shear modulus G_shear = c⁴/(8πG_N) = 1/(8π) (Planck pressure).
- Wave-speed match c_wave = √(G_shear/ρ₀) = c = 1 forces
  ρ₀ = G_shear/c² = 1/(8π) (Planck density, up to prefactor).
- Dynamic viscosity at the Planck cutoff (mean-free-path ≈ L_P):
  η₀ ≈ ρ₀·c·L_P = 1/(8π).
- Therefore R = η₀/G_shear = 1, in Planck units.

Restoring units:

<!-- R ≈ t_P ≈ 5.4 × 10⁻⁴⁴ s -->
$$
R \;\approx\; t_P \;\approx\; 5.4 \times 10^{-44}\ \text{s}.
$$

This is **80 orders of magnitude larger** than the spurious
1.5 × 10⁻¹²⁶ s number, and it is what GRID *predicts* for R if the
K–V medium is the coarse-grained Planck lattice: the relaxation time
of the substrate equals the Planck time, the natural light-crossing
of one cell.

This is a falsifiable cross-framework prediction. Losinets does not
measure R directly, but any future experimental bound on R (e.g. from
superfluid-vortex analogues, or from a near-field PINEM photon-ring
study that pins down the K–V dissipation scale) either corroborates
the R ~ t_P identification or falsifies the picture that the K–V
medium *is* the coarse-grained GRID lattice.

The numerical coincidences floating around the trilogy notes (e.g.
α^(−1/3) ≈ 5.156 ≈ r_m/r_c) are unrelated to this — they live in
the C1′ baryon thread, not the C4 substrate thread.

---

## 6. Where this leaves the layer map

The trilogy's "single dial" framing in
[`losinets/losinets-trilogy.md`](../losinets/losinets-trilogy.md)
must be weakened, but not abandoned:

- Each framework still has **exactly one EM input** of its own kind:
  α (dimensionless) for GRID/MaSt; R (a time) for Losinets.
- Those two inputs are **logically independent**. R is a property of
  the medium dynamics (viscoelastic relaxation); α is a property of
  the energy cost of topological windings in the discrete substrate.
- Even if the GRID lattice and the K–V medium describe the same
  physical substrate, the parameter spaces overlap on **orthogonal
  axes**. The substrate-equivalence picture (T1 in the trilogy) is
  not refuted, but it does not collapse the two dials.
- The unconditional bridge α = π·ρ₀·r₀²·ℏ/(m_vac²·c) shows that α is
  fully fixed by *substrate* parameters (ρ₀, r₀, m_vac) — none of
  which is R. The conditional bridge of §4 only emerges if a Losinets
  open problem is solved.

So both "GRID and Losinets are the same one-dial theory" and "GRID and
Losinets are unrelated" are wrong. The accurate statement is:

> The two frameworks may describe the same substrate, but their
> minimum free inputs sit on different axes of that substrate's
> parameter space. Reducing the joint-framework free-parameter count
> below two requires either GRID to predict (ρ₀, r₀, m_vac) — which
> would derive α — or Losinets to solve the §2.4 ring-energy closure —
> which would yield a (still parametric) α↔R relation through r₀.

---

## 7. Summary

| Outcome (per ticket) | Status |
|---|---|
| #1 — clean α = f(R · ω_Planck) | **Not supported.** Algebra shows α depends on (ρ₀, r₀, m_vac), not on R. |
| #2 — α = f(R) up to known factor | **Conditional only.** Requires the §2.4 ring-energy closure, and even then introduces r₀ as a second knob. |
| #3 — α and R orthogonal in K–V space | **Honest answer.** The boxed result α = π·ρ₀·r₀²·ℏ/(m_vac²·c) places α and R on different axes. |

Bonus result: GRID predicts **R ≈ t_P** if the K–V medium is the
coarse-grained Planck lattice (§5.1). The ticket's "1.5 × 10⁻¹²⁶ s"
warning was a dimensional error in disguise, not a substantive
disagreement with this prediction.

---

## Cross-links

- [`grid/foundations.md`](foundations.md) §"Open questions" — Q2 and the
  new sibling Q2b (α ↔ R).
- [`losinets/losinets-trilogy.md`](../losinets/losinets-trilogy.md)
  §C4 — replaced placeholder with the result derived here.
- [`primers/alpha-in-grid.md`](../primers/alpha-in-grid.md) §6 — pointer
  to this derivation as the Losinets-side attempt at α.
- Sources: Losinets EfD §4.6, §7.4 (correspondence table, R definition);
  Losinets photon §2.4 (open m_vac closure).
