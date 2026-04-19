# R61 findings — Losinets mantle as K-V elastic wake

Status: **complete** — study finished; pass/fail below.

## Summary

Testing R60's Interpretation 2: that Losinets's mantle (≈ 1.3 fm) is the
K-V elastic wake of a rotational core (≈ 0.25–0.4 fm) in the surrounding
viscoelastic medium, rather than a feature of the MaSt T⁶ eigenmode
amplitude itself.

Verdict: **partial pass**. The Hill-vortex exterior has no intrinsic
length scale — it produces a pure 1/r⁶ kinetic-energy decay from the core
surface outward (not 1/r⁴ as the ticket estimated; the ticket's hint
formula r_mantle = r_core·η^(−1/4) is the 2-D dipole scaling and is
wrong for a 3-D axisymmetric Hill exterior). Any 1.3 fm scale must
therefore enter as either (a) a coupling to a second particle scale,
(b) a chosen detection/noise threshold η, or (c) a derived geometric
ratio. The quantitative picture:

| source of r_mantle | input | r_mantle | note |
|---|---|---:|---|
| pion Compton λ̄_π± | m_π (external) | 1.41 fm | within 9%, but a new scale enters |
| η = 10⁻³ wake threshold on r_core = 0.40 fm | R60 inner-scale | 1.26 fm | within 3%, but η is a chosen cutoff |
| η = 10⁻³ on r_core = 0.25 fm | Losinets Hofstadter | 0.79 fm | miss −39% |
| α^(−1/3)·r_core, r_core = 0.25 fm | α + Losinets r_c | 1.29 fm | within 1%, parameter-free |
| ν₀/c (K-V viscous length) | m_vac (out of scope) | — | deferred |

The **strongest numerical match is a coincidence not derived from
Losinets's K-V equations**: α^(−1/3) ≈ 5.156 is within 1% of
Losinets's empirical r_m/r_c ≈ 5.2, and with r_core = 0.25 fm it yields
1.29 fm, within 1% of the Hofstadter mantle. The **strongest K-V
match** is η = 10⁻³ × 1/r⁶ decay from r_core = 0.4 fm (the R60/MaSt
inner scale), giving 1.26 fm. Both matches require an input (α, or η,
or r_core) that the K-V framework proper does not fix.

Pass/fail per the ticket's criteria:

| Criterion | Target | Result |
|---|---|---|
| Task A closed-form Hill exterior | yes | **met** (ψ = A·sin²θ/r, A = Ur₀³/2) |
| Task B ≥ 1 candidate within 20% without free params | 1.3 fm ±20% | **met** — pion Compton (±9%) and α^(−1/3)·r_c (±1% for r_c=0.25 fm) both qualify |
| Task C physically-defensible threshold η gives 1.3 fm for both r_core | 1.3 fm | **partial** — η = 10⁻³ matches for r_core = 0.4 fm only; r_core = 0.25 fm needs η ≈ 5·10⁻⁵ |
| Task D proton/neutron wake equivalent | yes | **met** (|u|² independent of sgn Γ) |

Net: the hypothesis survives at the level of "a K-V wake picture can
accommodate r_mantle ≈ 1.3 fm using plausible inputs, and is consistent
with the proton↔neutron core-reversal convention," but Losinets's K-V
framework *alone* — shear modulus G, viscosity η₀, circulation Γ — does
not *derive* 1.3 fm from a 0.25 or 0.4 fm core without an auxiliary
input. The two cleanest matches (pion Compton; α^(−1/3)) both live
outside the K-V equations per se.

## Framework recap (Losinets EfD §3.1, Appendix F; baryon §2.2)

**Linearised K-V exterior** (EfD eqs 10–11):

> ∇·u = 0,   ρ₀ ∂_tt u = −∇δp + G ∇²u + η₀ ∇² ∂_t u

with shear modulus G ≈ 0.234 Γ²/r₀², wave speed c_KV = √(G/ρ₀), and
relaxation R = η₀/G = ν₀/c_KV² (single time constant).

**Hill-vortex exterior stream function** (EfD Appendix F eq 60 text,
lab frame with fluid at rest at infinity — drop the uniform-flow term):

> ψ_ext(r, θ) = A sin²θ / r,    A = U r₀³ / 2

giving axisymmetric velocities

> u_r = 2A cosθ / r³,    u_θ = A sinθ / r³

so

> |u|²(r, θ) = (A²/r⁶)(4 cos²θ + sin²θ),  ⟨|u|²⟩_Ω = 2 A² / r⁶.

**Circulation–velocity relation** (EfD eq 67 text): Γ = 5 U r₀, giving
A = Γ r₀² / 10. **Zone angular velocity** (baryon eq 4):
ω = Γ/(2π r₀²).

## Task A — exterior velocity and energy density

Implemented in `scripts/exterior_hill.py`. Sanity check at the proton
Compton frequency ω_N = m_p c²/ℏ ≈ 1.425 × 10²⁴ rad/s, with Γ and U
computed from ω = Γ/(2π r₀²) and Γ = 5 U r₀:

```
r_core = 0.25 fm:  Γ = 5.6e-7 m²/s,  U = 4.5e8 m/s,  U/c = 1.49
r_core = 0.40 fm:  Γ = 1.4e-6 m²/s,  U = 7.2e8 m/s,  U/c = 2.39
```

Comment: when ω is identified with the proton natural frequency, the
implied Hill-vortex translation speed U exceeds c, so the identification
ω ↔ ω_N is *not* directly self-consistent within a non-relativistic K-V
framework (consistent with EfD's stated non-relativistic scope). The
wake-decay geometry (|u|² ∝ (r₀/r)⁶) is however independent of this
identification; it follows from incompressibility and axisymmetry alone.
See `plots/out_exterior_hill.txt`.

## Task B — candidate characteristic scales

`scripts/candidate_scales.py`; output in `plots/out_candidate_scales.txt`.

| candidate | formula | r_mantle (fm) | vs 1.30 fm | m_vac-free? |
|---|---|---:|---:|:---:|
| K-V viscous length | ν₀/c | — | — | no (needs m_vac) |
| Hill exterior pure decay | (no length) | — | — | n/a |
| Charged pion Compton | ℏ/(m_π± c) | 1.414 | +8.8% | yes |
| Neutral pion Compton | ℏ/(m_π0 c) | 1.462 | +12.5% | yes |
| α^(−1/3)·r_core [0.25 fm] | α + Losinets r_c | 1.289 | −0.9% | yes |
| α^(−1/3)·r_core [0.40 fm] | α + R60 r_c | 2.062 | +58.6% | yes |
| α^(−1/3)·λ̄_p | α + m_p | 1.084 | −16.6% | yes |
| 5.2·λ̄_p | empirical ratio × m_p | 1.094 | −15.9% | partially |

Two parameter-free candidates land within 20% of Losinets's 1.3 fm:
charged-pion Compton (+9%) and α^(−1/3)·r_c (with r_c = 0.25 fm: −1%).

The α^(−1/3) ratio ≈ 5.156 is within 1% of Losinets's empirically-fit
r_m/r_c ≈ 5.2 — a striking numerical coincidence. No mechanism in
Losinets's K-V paper produces this ratio; it would require α (a
dimensionless EM coupling absent from Losinets's framework, where the
sole dimensionful dial is R = ν₀/c²) to appear as a 3-D-geometric
exponent. This could be an artefact or a hint that the K-V mantle scale
is set by the classical EM coupling at a different layer (GRID / MaSt).

## Task C — energy-threshold calculation

`scripts/wake_threshold.py`; output in `plots/out_wake_threshold.txt`.

Operational: r_mantle where ⟨|u|²⟩(r_mantle) / ⟨|u|²⟩(r_core) = η.
With 1/r⁶ decay this gives r_mantle = r_core · η^(−1/6).

For r_core = 0.40 fm (R60/MaSt inner scale):
- η = 10⁻² → 0.86 fm (−34%)
- η = 10⁻³ → 1.26 fm (−3%) ✓ ← matches Losinets's 1.30 fm within 3%
- η = 10⁻⁴ → 1.86 fm (+43%)

For r_core = 0.25 fm (Losinets Hofstadter):
- η = 10⁻³ → 0.79 fm (−39%)
- η = 10⁻⁴ → 1.16 fm (−11%) ✓
- η = 3·10⁻⁵ → 1.42 fm (+9%) ✓

η ≈ 10⁻³ corresponds to the −30 dB "end of radiative near-field"
convention for dipole antennas; η ≈ 10⁻⁴ is the typical detector /
spectroscopy noise floor. Neither has a *unique* physical interpretation
in the Hofstadter scattering geometry, and no single η hits 1.30 fm
simultaneously for both candidate r_core values.

**Interpretation**: with the correct 1/r⁶ dipole decay, the exterior
energy density falls so steeply that the *choice of threshold* only
weakly moves r_mantle (one decade of η shifts it by 47%). That is a
feature — it means any threshold within a reasonable physical range
produces a similar mantle size on the fm scale. It is also a limitation:
the precise 1.3 fm value cannot be pinned without an independent reason
to prefer one threshold over another.

## Task D — neutron consistency

The exterior velocity u(r) is linear in the dipole amplitude A ∝ Γ.
Reversing the core circulation (proton → neutron) flips A → −A and
therefore u → −u, leaving |u| invariant. The wake energy density and
its radial profile are therefore identical between proton and neutron:
r_mantle(proton) = r_mantle(neutron), as Losinets's construction
requires. **Pass.**

## Interpretation

Three separable points:

1. **Losinets's K-V framework is consistent with r_mantle ≈ 1.3 fm** —
   the exterior decay is steep enough that any reasonable noise-floor
   interpretation lands within a factor of ~2 of 1.3 fm for a nucleon-
   sized core. The framework does not *fail* this test; it simply does
   not *uniquely predict* 1.3 fm without auxiliary input.

2. **The MaSt eigenmode core (≈ 0.4 fm from R60) is compatible with a
   1.26 fm wake at η = 10⁻³**, which is within 3% of Hofstadter's
   1.3 fm. This is the quantitative expression of R60's Interpretation 2
   and supports the complementary picture: MaSt supplies the core
   amplitude (≈ 0.4 fm), Losinets's K-V medium supplies the surrounding
   field response (≈ 1.3 fm wake), Hofstadter measures the sum.

3. **The α^(−1/3) ratio = 5.156 lands within 1% of Losinets's empirical
   r_m/r_c ≈ 5.2.** This is numerically striking but not derived; it
   would require α to enter a geometric wake scale, which cannot happen
   in either the pure K-V picture or the pure MaSt picture without a
   bridge. Flag for R62 or a coordinated Losinets–MaSt–GRID sub-study.

## Open items

- **α^(−1/3) coincidence.** Is it? Or is there a mechanism via, e.g.,
  Ma-S coupling in MaSt that produces a ratio of 5.2 (= α^(−1/3)
  approximately) between an inner compound-mode amplitude radius and a
  surrounding wake scale? Worth examining whether GRID's α-derivation
  predicts such a geometric consequence.

- **m_vac-dependent calibration.** If m_vac is fixed by an independent
  MaSt identification (ticket `implement/3-losinets-mvac-identifications.md`),
  the K-V viscous length ν₀/c becomes computable and either (a)
  overlaps with 1.3 fm — absolute prediction — or (b) fails to. Either
  outcome is informative.

- **Dynamic wake vs static.** The current calculation is static (|u|²
  from the dipole; energy density proportional to ρ₀|u|²). The full
  K-V response at nonzero ω adds a viscous skin depth c/ω that, at
  ω_N = m_p c²/ℏ, is ≈ 0.21 fm (the proton reduced Compton) — sub-fm
  and therefore *smaller* than r_core, meaning the static picture is
  not obviously the correct regime. A full dynamic treatment is a
  separate ticket if this picture survives scrutiny.

## Pass/fail conclusion

| Criterion | Verdict |
|---|---|
| A — Hill exterior derivation | ✓ met |
| B — ≥ 1 candidate within 20% without free parameters | ✓ met (pion Compton; α^(−1/3)·r_c) |
| C — defensible η gives 1.3 fm for both r_core | ○ partial (works for r_core = 0.4 fm at η = 10⁻³; r_core = 0.25 fm needs smaller η) |
| D — proton/neutron mantle equivalence | ✓ met |

**Overall: partial pass.** The hypothesis R60-Interpretation-2 survives
quantitatively: a K-V wake of a nucleon-sized core lands at a
Hofstadter-compatible mantle scale under physically reasonable
assumptions, and is *identically* consistent with Losinets's
proton↔neutron core-reversal convention. But 1.3 fm drops out only
with an input the K-V framework does not fix internally — either a
noise threshold η ≈ 10⁻³, or a coupling to m_π, or the MaSt/GRID
coupling α via a 5.16 geometric factor. The deliverable to Losinets is
therefore not "your K-V equations alone produce 1.3 fm"; it is:

> "MaSt supplies r_core ≈ 0.4 fm from the T⁶ eigenmode; your Hill-
> vortex exterior (ψ = A sin²θ/r, |u|² ∝ 1/r⁶) decays to 0.1% of its
> surface value at r ≈ 1.26 fm — within 3% of the Hofstadter mantle."

That is a clean three-way picture worth communicating, with the caveat
that η = 10⁻³ is an assumption-of-regime rather than a derivation.

## Files

- `scripts/exterior_hill.py` — Hill exterior velocity, energy density,
  wake-decay ratio, r_mantle = r_core · η^(−1/6) inverter.
- `scripts/candidate_scales.py` — five candidate lengths, tabulated.
- `scripts/wake_threshold.py` — η sweep for both r_core values.
- `plots/out_*.txt` — captured script outputs.
