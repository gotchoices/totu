# R62 findings — Losinets m_vac under four MaSt identifications

Status: **complete** — cross-particle m_vac does **not** stabilise under
any of the four geometric identifications tested.

## What was computed

For the Losinets free-photon relation Γ = 2π ρ² ω = h/m_vac (n = 1),

$$ m_{\mathrm{vac}} = \frac{\hbar}{\rho^{2}\,\omega} $$

we evaluated (ρ, ω) under four identifications drawn from MaSt model-E
confinement lengths and particle Compton angular frequencies, with
ρ = L/(2π) in each case. The script `compute_mvac.py` reproduces the
table below in < 1 s.

| # | identification | ρ = L/(2π) (fm) | ω (rad/s) | m_vac |
|---|---|---:|---:|---:|
| I-1 | e-sheet ring × electron    (L₂ = 11.9 fm)      | 1.894       | 7.76 × 10²⁰ | **21.2 GeV/c²** |
| I-2 | e-sheet tube × electron    (L₁ = 4717 fm)      | 750.7       | 7.76 × 10²⁰ | 135 keV/c² |
| I-3 | p-sheet ring × proton      (L₆ = 4.45 fm)      | 0.708       | 1.43 × 10²⁴ | 82.7 MeV/c² |
| I-4 | ν-sheet ring × ν₃ (58.2 meV, L₄ = 4.2 × 10¹⁰ fm) | 6.69 × 10⁹ | 8.84 × 10¹³ | 15 meV/c² |

Ratios to the I-1 baseline span **25 orders of magnitude**: I-2 6.4 × 10⁻⁶,
I-3 3.9 × 10⁻³, I-4 7.0 × 10⁻¹³. The ω ↔ 2πω sensitivity variant scales
every row uniformly by 1/(2π) ≈ 0.159; cross-particle ratios are
unchanged, and the agreement story is insensitive to that convention.

The I-1 = 21.2 GeV/c² value reproduces the acceptance-test baseline
(trilogy §C2, pre-R62) to 2 significant figures.

## Agreement

**No.** The two charged, ring-based identifications I-1 and I-3 do **not**
land within an order of magnitude: their ratio is

$$ \frac{m_{\mathrm{vac}}^{\mathrm{(I\text{-}1)}}}{m_{\mathrm{vac}}^{\mathrm{(I\text{-}3)}}} = 2.57 \times 10^{2} $$

— about 260×, or 2.4 decades apart. Cross-particle universality of
m_vac fails at the level the identification was supposed to test.

## Interpretation of the I-1 / I-3 disagreement

Since m_vac ∝ 1/(ρ² ω), the ratio decomposes exactly as

$$ \frac{m_{\mathrm{vac}}^{\mathrm{(I\text{-}1)}}}{m_{\mathrm{vac}}^{\mathrm{(I\text{-}3)}}} = \left(\frac{\rho_{p}}{\rho_{e}}\right)^{2}\,\frac{\omega_{p}}{\omega_{e}} = \left(\frac{L_{6}}{L_{2}}\right)^{2}\,\frac{m_{p}}{m_{e}} = (0.374)^{2} \cdot 1836.15 = 0.140 \cdot 1836 = 257. $$

Diagnosing the factors listed in the ticket:

- **Factor of 2π (ρ convention).** Not relevant; the 2π appears identically
  in every identification (ρ = L/(2π) throughout), so it cannot explain
  any cross-particle disagreement. The ω → 2πω sensitivity check
  confirms this — it is a uniform rescaling.
- **Factor of m_p/m_e (Compton-restatement).** Partially present: the
  ω_p/ω_e = m_p/m_e = 1836 contributes one factor. If the L's also
  scaled Compton-fashion, L ∝ 1/m, then (L₂/L₆)² would equal
  (m_p/m_e)² = 3.37 × 10⁶ and the combination would leave a residual
  factor m_p/m_e — just restating the Compton relation with no
  new content.
- **Factor tied to L₂/L₆ (geometry-driven).** This is where the
  disagreement actually lives. MaSt's L-values are **not** a Compton
  ladder: L₂/L₆ = 2.67, not 1836. The e-sheet ring is ~2.7× the
  p-sheet ring, not ~1800×. That mismatch — between a geometry that
  was fitted to eigenmode mass spectra and a geometry that would need
  L ∝ 1/m to make m_vac universal — is the full source of the 257×
  gap. For I-1 and I-3 to agree, the p-sheet ring ρ would need to
  shrink to ρ_e · √(m_e/m_p) ≈ 0.044 fm (≈ L = 0.28 fm), far below
  L₅ = 2.45 fm and L₆ = 4.45 fm.

Bottom line on I-1/I-3: **geometry-driven**, not a 2π convention error,
not a pure Compton restatement. MaSt L's are particle-eigenmode scales,
not free-photon ring scales, so identifying them with Losinets's ρ(ω)
enforces no universality.

## ν-sheet stress test (I-4)

L₄ = 4.2 × 10¹⁰ fm ≈ 42 μm pushes ρ into the macroscopic optical regime,
while ω_ν ≈ 88 THz sits in the far-IR. Together they drive

$$ m_{\mathrm{vac}}^{\mathrm{(I\text{-}4)}} \approx 15~\mathrm{meV}/c^{2} $$

— of order the neutrino masses themselves (m_ν₃ = 58.2 meV). An m_vac
below the particle's own rest energy is physically incoherent: the
"vacuum" particle would be lighter than the ring excitation it
supports, so the Onsager–Feynman quantisation Γ = h/m_vac would imply
a circulation larger than the particle's own Compton area divided by
itself. This is a hard failure, not a near-miss.

The broader reading: using a 3D free-photon ring identification on the
ν-sheet is the wrong category. ν-sheet scales are a compactification
radius of a 6-torus dimension, with a particle whose rest energy is
meV. They carry no free-photon content. Losinets's ρ(ω) relation is a
statement about extended 3D vortex rings in the K-V vacuum; MaSt's
L₄ is a length on a compact internal dimension. The 10¹² factor in
I-4/I-1 is a direct consequence of that category mismatch — and it
rules out the ν-sheet as a test-bed for any free-ring identification.

## I-5 (exploratory, energy condition) — does not close

Substituting ρ_m = G/c² = 0.234 Γ²/(r₀² c²) (from EfD §3) into the
classical thin-core kinetic energy

$$ E_{\mathrm{ring}} \approx \tfrac{1}{2}\,\rho_{m}\,\Gamma^{2}\,\rho\,\bigl[\ln(8\rho/r_{0}) - 7/4\bigr] $$

and setting E_ring = ℏω with ω = ℏ/(m_vac ρ²) (the n = 1 closure),
together with Γ = h/m_vac = 2π ℏ / m_vac, yields

$$ m_{\mathrm{vac}}^{3} = 0.117 \cdot (2\pi)^{4} \cdot \hbar^{2} \cdot \rho^{3} \cdot \bigl[\ln(8\rho/r_{0}) - 7/4\bigr] / (r_{0}^{2}\,c^{2}). $$

m_vac does **not** cancel, so the algebraic exercise is not empty —
but r₀ enters as a second free parameter, so the closure pins a
one-parameter family (m_vac, r₀), not a number. An indicative scan at
ρ = L₂/(2π) = 1.894 fm gives m_vac from ≈ 1 keV/c² (r₀ = 2 fm) up to
≈ 20 keV/c² (r₀ = 0.1 fm) — five to seven orders of magnitude below
I-1, confirming that the kinetic-KE form cannot by itself recover the
21 GeV scale.

This reproduces Losinets's own §2.4 disclaimer: the classical kinetic
form is a **lower bound** on E_ring; a full K-V elastic-energy
derivation (including the K-V shear storage and the shape-stability
pressure jump) is required to close m_vac from (c, G, ν₀). The 21 GeV
baseline of I-1 is therefore an *identification*, not a *derivation*,
and it sits in a regime the kinetic form alone cannot reproduce
without a new scale r₀.

## Bottom line

**No identification gives an order-of-magnitude-stable m_vac across
particles.** The I-1 baseline 21 GeV/c² is numerically sensible and
reproducible (pre-R62), but it is a point value of a per-particle
recipe, not a universal prediction: swapping the electron ring for the
proton ring shifts the result by 260×, swapping it for the ν-sheet
ring shifts it by 10¹². The disagreement is geometry-driven — MaSt
L-values are eigenmode scales, not free-photon ring scales, so the
two roles do not coincide automatically.

A universal m_vac from MaSt geometry alone would require either
(i) a new identification in which ρ rescales as 1/√(mω) between
particles (no such scale currently exists in model-E), or
(ii) closing I-5 with the proper K-V elastic-energy term so that r₀
and m_vac are jointly fixed by Losinets's own substrate parameters.
Both remain open.

## Pointers

- Script: `compute_mvac.py` (stdlib-only; prints the table and I-5 scan).
- Inputs: `papers/white-paper.md` §3 (L-table); `models/model-E.md`
  (particle inventory); `reference/losinets_photon.txt` §2.4
  (Γ closure and open m_vac problem).
- Companion studies: `R60-losinets-projection/` (Hofstadter projection);
  `R61-losinets-mantle-wake/` (K-V wake mantle).
- Ticket: `tickets/implement/4-losinets-mvac-identifications.md`.
