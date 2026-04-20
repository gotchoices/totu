# R60 findings — Losinets Hofstadter projection

Status: **complete** — study finished; pass/fail reported below.

## Summary

Projecting the model-E proton compound mode **(0, 0, −2, 2, 1, 3)** from
the flat six-torus onto a 3D radial charge density ρ(r) does **not**
reproduce Losinets's parameter-free two-zone prediction r_m/r_c ≈ 5.2
under any of the twelve tested (density × projection) combinations.

| Criterion | Target | Result |
|---|---|---|
| C1 — two characteristic scales | yes | **met** (every variant produced ≥ 2 peaks) |
| C2 — ratio in [4.0, 6.4] | ≈ 5.2 | **failed** (best 1.77; clustered around 1.3–1.8; only spurious outlier at r_in ≈ 0.04 fm) |
| C3 — absolute scales near 0.25 and 1.3 fm | ±20 % | **failed** (outer scale hits 1.33 fm in two variants, but inner scale never below 0.39 fm) |
| C4 — neutron sign-reversed core | core–, mantle+ | **partially met**: M-C × P-1 shows sign split but with core + / mantle −, i.e. opposite of the Losinets convention |

Overall: **FAIL on the proton equivalence**.  The factor-of-3 gap
between the raw p-sheet scale ratio (L₆/L₅ ≈ 4.454 / 2.450 ≈ 1.82) and
the Hofstadter ratio (5.2) cannot be closed by the mode's winding
numbers (n₅ = 1, n₆ = 3), the ν-sheet (scale ~10¹⁰ fm — invisible on
the [0, 5 fm] grid), the Ma-S charge coupling, or any of the four
projection prescriptions tested.

## Geometry (model-E, cross-shears σ₄₅ = −0.18, σ₄₆ = +0.10)

```
L_tube_e  = 4.718e+03 fm     L_ring_e  = 1.188e+01 fm
L_tube_nu = 2.119e+11 fm     L_ring_nu = 4.238e+10 fm
L_tube_p  = 2.450   fm       L_ring_p  = 4.454   fm
E(proton  compound (0, 0, -2, 2, 1, 3))  = 938.272 MeV  (exact)
E(neutron compound (0, -4, -1, 2, 0, -3)) = 938.896 MeV (-0.071 % vs 939.565)
```

Geometry verification reproduces R54 Track 1c exactly.  The projection
candidates see only the p-sheet scales (L₅ = 2.45 fm, L₆ = 4.45 fm);
the e-sheet ring at ~12 fm sits at the edge of the radial grid, and
the ν-sheet at ~10¹⁰ fm is entirely outside it.

## Results table — proton

Abbreviations: M-A standing wave, M-B kinetic/gradient, M-C charge-weighted;
P-1 embedding-sum Gaussians, P-2 node-wavelet packets, P-3 hydrogen-like
basis (Monte-Carlo T⁶ sampling), P-4 Fourier form factor.

| M | P | n_scales | r_in (fm) | r_out (fm) | ratio | c1 | c2 | c3 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| M-A | P-1 | 2 | 0.402 | 0.712 | 1.77 | ✓ | ✗ | ✗ |
| M-A | P-2 | 2 | 0.392 | 0.612 | 1.56 | ✓ | ✗ | ✗ |
| M-A | P-3 | 4 | 0.041 | 0.412 | 10.03 | ✓ | ✗ | ✗ |
| M-A | P-4 | 4 | 0.953 | **1.333** | 1.40 | ✓ | ✗ | ✗ |
| M-B | P-1 | 2 | 0.402 | 0.712 | 1.77 | ✓ | ✗ | ✗ |
| M-B | P-2 | 2 | 0.402 | 0.612 | 1.52 | ✓ | ✗ | ✗ |
| M-B | P-3 | 3 | 0.412 | 0.522 | 1.27 | ✓ | ✗ | ✗ |
| M-B | P-4 | 4 | 1.343 | 1.804 | 1.34 | ✓ | ✗ | ✗ |
| M-C | P-1 | 2 | 0.402 | 0.712 | 1.77 | ✓ | ✗ | ✗ |
| M-C | P-2 | 2 | 0.392 | 0.612 | 1.56 | ✓ | ✗ | ✗ |
| M-C | P-3 | 4 | 0.412 | 0.532 | 1.29 | ✓ | ✗ | ✗ |
| M-C | P-4 | 4 | 0.953 | **1.333** | 1.40 | ✓ | ✗ | ✗ |

Targets: r_c ≈ 0.25 fm, r_m ≈ 1.3 fm, ratio ≈ 5.2.

Bolded values: the outer scale r_out ≈ 1.33 fm in the two Fourier-form-factor
cases (M-A × P-4 and M-C × P-4) is within 3 % of the Hofstadter mantle
radius — a suggestive match, but the partnering inner scale lands at
0.95 fm, not 0.25 fm, so the ratio is wrong.

The single outlier ratio (M-A × P-3 at 10.0) is driven by a spurious
peak at 0.04 fm inside the Gaussian-smoothing resolution and is
dismissed.

## Results table — neutron

| M | P | n_scales | r_in (fm) | r_out (fm) | ratio | sgn_in | sgn_out | c4 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| M-A | P-1 | 2 | 0.712 | 1.894 | 2.66 | + | + | ✗ |
| M-A | P-2 | 3 | 1.253 | 1.684 | 1.34 | + | + | ✗ |
| M-A | P-3 | 4 | 0.742 | 0.953 | 1.28 | + | + | ✗ |
| M-A | P-4 | 4 | 1.794 | 2.485 | 1.39 | + | + | ✗ |
| M-B | P-1 | 2 | 0.712 | 1.894 | 2.66 | + | + | ✗ |
| M-B | P-2 | 3 | 0.622 | 1.684 | 2.71 | + | + | ✗ |
| M-B | P-3 | 2 | 0.422 | 0.953 | 2.26 | + | + | ✗ |
| M-B | P-4 | 4 | 1.794 | 2.485 | 1.39 | + | + | ✗ |
| M-C | P-1 | 2 | 0.712 | 1.894 | 2.66 | + | − | ✓* |
| M-C | P-2 | 2 | 1.253 | 1.684 | 1.34 | − | − | ✗ |
| M-C | P-3 | 4 | 0.732 | 0.832 | 1.14 | − | + | ✓ |
| M-C | P-4 | 4 | 1.784 | 2.485 | 1.39 | + | + | ✗ |

Only M-C (the charge-weighted density) produces sign structure at all.
M-C × P-1 shows a **core-positive, mantle-negative** split, which is
the **opposite** of the Losinets neutron (core −, mantle +).  M-C × P-3
shows the convention-correct sign reversal (core −, mantle +), but with
a ratio of 1.14 that bears no relation to 5.2.

## Interpretation

The study falsifies the naive claim that Losinets's two-zone nucleon
is a spherically symmetric projection of the MaSt T⁶ proton eigenmode.
The information carried by the compound mode is:

- **Scales.** Only two physical scales enter the radial window
  [0, 5 fm]: L₅ = 2.45 fm (p-tube circumference) and L₆ = 4.45 fm
  (p-ring circumference), ratio 1.82.  The ν-sheet lives ~10¹⁰ fm
  out, so its winding does not contribute to any peak within the
  Hofstadter range.  The e-sheet ring at 11.9 fm sits at the grid
  edge and never produces a peak inside [0, 1.5 fm].
- **Winding.** n₆/n₅ = 3 multiplies the p-ring harmonic scale by 3,
  but only **within** a peak (sharpening it), not **between** peaks.
  There is no geometric operation that turns 1.82 into 5.2 using the
  available scales and integer windings without free parameters.
- **Cross-shears.** σ₄₅ = −0.18 and σ₄₆ = +0.10 enter the metric,
  but the mode's radial structure in the P-3 projection (which
  actually uses G̃⁻¹) still shows the same clustered ratios ~1.3,
  indicating the metric mixing does not generate a second distinct
  length scale at ~1.3 fm.

The outer scale r_out ≈ 1.33 fm appearing in the two Fourier-form-factor
variants is a coincidence: it arises from the inverse-FT of
sinc(Q·L₆/2), whose first zero is at Q = 2π/L₆ ≈ 1.41 fm⁻¹, giving a
real-space width ~ 2π/Q ≈ 4.45 fm, whose first Bessel maximum in the
3D spherical transform lands near 1.3 fm.  This is simply L₆ itself
reinterpreted — not a second geometrical scale.

### What this says about model-E

The Hofstadter two-zone structure is **not** an automatic property of
the flat-T⁶ eigenmode under any spherically symmetric projection.
Either:

1. **The projection must break spherical symmetry** — in particular,
   the radial mapping must depend on the ν-sheet coordinates in a
   non-trivial way (despite the ν-sheet scale being cosmic).  This
   would require the Ma-S coupling to blend ν-sheet phase with
   physical-space radial position; that mechanism is not present in
   model-E.

2. **Or the two-zone structure is dynamical, not kinematic** — i.e.
   the mantle at 1.3 fm emerges from self-field / Coulomb-cloud
   dynamics of the charged p-sheet mode (a Losinets-style "K-V
   outer-mantle elastic response"), not from the eigenmode amplitude
   itself.  In this reading the eigenmode gives the hard core
   (0.25–0.4 fm p-sheet structure), and the mantle is the wake — a
   phenomenon of the surrounding field, not the internal T⁶ mode.

3. **Or the ν-ring participation must be reinterpreted.**  In the
   compound proton (n₃ = −2, n₄ = +2) the ν-sheet carries windings
   but lives at cosmic L; if the L we use is not the right "radial"
   quantity for projection and should instead be derived from
   σ₄₅, σ₄₆ (a local effective radius dictated by the cross-shears),
   the ν-ring could, in principle, contribute at hadronic scales.
   Our P-3 projection does use G̃⁻¹ but still does not produce a
   ~1.3 fm feature — so this reinterpretation, if true, needs a
   projection more specific than those tried here.

### Feedback for R55

The result constrains the Ma-S derivation: to land on r_m/r_c = 5.2,
the Ma-S block cannot be a purely local rescaling — it must either
introduce a second characteristic scale at ~1.3 fm (distinct from
any in the bare L vector) or mix the ν-sheet's compact coordinate
into the physical-space projection.  A symmetric, local σ_eS / σ_pS
coupling that only rescales the p-sheet's effective radius cannot
produce the Losinets ratio.

## Conclusion

- **Criterion 1 (two scales):** met.
- **Criterion 2 (ratio 4.0–6.4):** **not met** — best ratio 1.77, all
  physically plausible variants cluster in [1.3, 1.8].
- **Criterion 3 (absolute scales ≈ 0.25, 1.3 fm):** **not met** — outer
  scale hits 1.33 fm in Fourier projection but inner scale bottoms out
  at 0.39 fm; no variant delivers both.
- **Criterion 4 (neutron sign-reversed core):** **partially met** —
  M-C × P-3 delivers the correct sign pattern but with the wrong
  magnitudes; M-C × P-1 delivers the wrong sign pattern.

The Losinets two-zone equivalence to the MaSt proton compound mode
**fails at the kinematic level**.  The finding is informative: it
points R55 toward Ma-S coupling mechanisms that introduce a
physical-space length distinct from the bare L_i, and it separates
what the T⁶ eigenmode can do (hard-core structure at ~0.3–0.4 fm)
from what the surrounding field must do (the 1.3 fm mantle), tracking
the same split Losinets himself makes between core (rotational) and
mantle (irrotational-but-circulating) zones.
