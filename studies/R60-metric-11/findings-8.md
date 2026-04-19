# R60 Track 8: Compound mode search (μ, τ, neutron)

**Scope.**  Search compound 6-tuples matching observed muon,
tau, neutron masses on the Track 7d magic-shear baseline.  Four
phases: Phase 1 evaluates model-E's compound tuples verbatim,
Phase 2 brute-forces alternative tuples, Phase 3 audits α on
the top matches, Phase 4 adds an α = α filter based on the
Phase 3 discovery.

Script: [scripts/track8_compound_modes.py](scripts/track8_compound_modes.py).

## F46. Model-E compound tuples don't survive the R60 metric transition

Phase 1 plugged model-E's inventory tuples into the Track 7d
augmented metric:

| Particle | Model-E 6-tuple | R60 predicted | Target | Δ |
|----------|:----------------|--------------:|-------:|--:|
| muon | (1, 1, −2, −2, 0, 0) | **0.5504 MeV** | 105.658 MeV | **−99.5%** |
| tau  | (3, −6, 2, −2, 2, 3) | 2188.38 MeV | 1776.86 MeV | +23.2% |
| neutron | (0, −4, −1, 2, 0, −3) | 1125.91 MeV | 939.565 MeV | +19.8% |

Model-E's compounds don't match R60 masses.  The reason is
structural: Track 7d's L scales (L_ring_e = 2.8×10⁴ fm,
L_ring_p = 15.2 fm, L_ring_ν = 2.0×10¹¹ fm) differ from
model-E's, and compound-mode energies are sums-of-squares
dominated by the sheet with the largest `n/L` contribution.
With L_ν so huge, any ν-sheet winding at |n| ≤ 6 contributes
~10⁻¹⁰ of the mass — essentially nothing.  Model-E's muon tuple
collapses to its e-sheet (1, 1) piece alone, giving 1.08× m_e.

## F47. α_Coulomb for compound modes is exactly quantized

Phase 3 α audit on Phase 2's top brute-force matches showed a
clean pattern: every compound mode has

> **α_Coulomb = (n_et − n_pt + n_νt)² × α**

Examples (all α measured to 10⁻⁶):

| Mode | n_et − n_pt + n_νt | Predicted | Measured |
|------|---:|---:|---:|
| muon tuple (1, 1, −2, −2, 0, 0) | −1 | 1 | 1.0000 |
| tau tuple (3, −6, 2, −2, 2, 3) | +3 | 9 | 9.0000 |
| neutron tuple (0, −4, −1, 2, 0, −3) | −1 | 1 | 1.0000 |
| Phase 2 top match (2, −6, −6, n, 1, −1) | −5 | 25 | 24.9999 |
| Phase 2 top match (1, −6, −6, n, 0, 0) | −5 | 25 | 24.9999 |

**Interpretation.**  On the ring↔ℵ augmented metric, compound-mode
α is entirely determined by a linear combination of the three
sheets' tube windings weighted by their σ_ta signs.  Not by
geometry.  Every mode with `n_et − n_pt + n_νt = ±1` gives
α = α; every mode with ±2 gives 4α; etc.  α universality is
structurally quantized — a feature, not a bug of the R60
architecture.

For α = α (matching electron / proton / ν₁), compound modes
must satisfy: **n_et − n_pt + n_νt = ±1**.

## F48. α-filtered search: clean wins on tau and neutron, block on muon

Phase 4 enforced the α = α constraint and re-ran the brute-force
search at |n_i| ≤ 6.  Results:

**Tau — clean match:**

| Rank | 6-tuple | E (MeV) | Δ | α/α |
|-----:|:--------|-------:|--:|----:|
| 1 | (2, −6, −2, n_νr, 1, −1) | 1770.31 | −0.37% | 1.0000 |

(n_νr is effectively free — all 10 top matches share the same
energy because ν-sheet contribution is negligible at |n_i| ≤ 6.)

Charge check: Q = −2 + 1 = −1 ✓.  Spin-½: n_et=2 (even),
n_νt=−2 (even), n_pt=1 (odd) → 1 odd sheet → spin-½ ✓.
α check: n_et − n_pt + n_νt = 2 − 1 + (−2) = −1 → α = α ✓.
0.37% residual is comparable to model-E's best hadron matches.

**Neutron — clean match:**

| Rank | 6-tuple | E (MeV) | Δ | α/α |
|-----:|:--------|-------:|--:|----:|
| 1 | (−1, 6, −1, n_νr, −1, −3) | 938.26 | −0.14% | 1.0000 |

Charge: Q = 1 + (−1) = 0 ✓.  Spin-½: n_et=−1 (odd), n_νt=−1
(odd), n_pt=−1 (odd) → 3 odd sheets → spin-½ ✓.
α check: −1 − (−1) + (−1) = −1 → α = α ✓.
0.14% residual matches model-E's 0.07% at comparable quality.

**Muon — block:**

| Rank | 6-tuple | E (MeV) | Δ | α/α |
|-----:|:--------|-------:|--:|----:|
| 1 | (1, −6, −2, n_νr, 0, 0) | 1.71 | **−98.4%** | 1.0000 |

Best candidate at |n_i| ≤ 6 lands at 1.71 MeV, 62× below the
muon mass.  The full Phase 4 search found *no* compound with
α = α landing in the 50–200 MeV window.

## F49. The muon block is a scale problem, not a filter problem

Why muon is hard on Track 7d:

- Pure e-sheet modes at magic shear: mass = m_e × μ(1, n_r) / 2.5.
  At |n_r| ≤ 6, max μ ≈ 4.7, giving max e-mass ~0.96 MeV.
- Pure p-sheet modes: minimum mass = m_p × 2.5/2.5 = 938 MeV.
- ν-sheet contributions are negligible at any mode at this L_ν.
- Compound modes are sum-of-squares of the above, so they can't
  interpolate.  Adding a small p-contribution (say μ_p at
  minimum 2.5, giving ~938 MeV) to an e-contribution (<1 MeV)
  gives E ≈ 938 MeV.  No middle ground.

**The 50–200 MeV window is a mass desert on Track 7d.**  The
only ways into it are (a) very high e-sheet harmonics (requires
|n_er| ~ 500, per R50 Track 11 analog), or (b) different L
scales that don't separate sheet energies so sharply.  Neither
is available at the current (ε, s, k) configuration without
re-opening Track 7's fit.

Model-D / model-E hit the same wall — R50 F56 noted "zero Q=−1
spin-½ modes between 5 and 200 MeV across all sign branches."
Model-E eventually landed muon as a compound `(1, 1, −2, −2, 0, 0)`
that *could* interpolate given L_ν at a different scale.  With
our L_ν pinned by Δm² matching (R49), the compound-interpolation
path is closed at |n_i| ≤ 6.

## F50. Status and block

**Clean results:**

- Tau at (2, −6, −2, *, 1, −1), 0.37% off, α = α
- Neutron at (−1, 6, −1, *, −1, −3), 0.14% off, α = α
- Compound α is exactly quantized: `α/α = (n_et − n_pt + n_νt)²`
- The constraint for α = α (matching electron/proton/ν₁):
  `n_et − n_pt + n_νt = ±1`

**Block:**

- Muon at |n_i| ≤ 6 doesn't land within 50% of target.  The
  50–200 MeV window is a mass desert on Track 7d geometry.
- Extending to |n_i| = 500+ is the R50 Track 11 route (muon as
  high harmonic).  Possible but not immediate; produces many
  ghost modes.

**What this tells us:**

1. **Compound α is structurally quantized.**  This is a
   *feature* of R60's architecture, not a bug.  Electrically
   charged compound modes naturally have α = 1, 4, 9, 16, ...
   times α, determined only by tube winding numbers.  Integer
   Coulomb charge Q = ±1 plus integer α-ratio is consistent
   with how we observe charged particles (muon, pion, proton
   all have ±1 unit charge AND couple with the same α).
2. **The R59 F59 architecture plus Track 7 ring↔ℵ fix gives a
   *clean* universality structure** — every α = α mode is
   identified by a single integer relation, which is elegant.
3. **Cross-sheet σ would not help the muon** — it's a
   mass-scale issue, not an α issue.  Pool item **h** is not
   the fix for this block.

## Decision point

The Track 8 block is muon placement, not α universality.
Options:

- **(a) High-harmonic muon search** (R50 Track 11 analog).
  Extend |n_i| up to ~500 and look for electron-sheet
  high-order modes.  Likely finds muon as (1, n_er) with n_er
  near 490 or similar.  Produces many ghost modes that we'd
  need a filter for (R56 routing or R61 pairs).
- **(b) Different Track 7d (ε, s) geometry** that produces
  different L scales.  Probably means shrinking ε_p further
  (raising p-sheet ring mass) or something similar.  Re-opens
  the Track 7d fit but might put muon in reach of low-order
  compounds.
- **(c) Accept muon as high-harmonic, claim victory on
  tau/neutron.**  R60 partial success: we have α universality
  structural, two compound hadrons matched, muon needs more
  work.  Document and move on to broader hadron inventory
  (Σ, Λ, Ξ, Ω, etc.) at α = α.
- **(d) Investigate the L-scale constraint.**  Why does Track
  7d produce these specific L values?  The "single-k symmetry"
  (k_e = k_p = k_ν = 1.1803/(8π)) forces specific L ratios via
  the mass calibration.  Is there a way to break this symmetry
  cleanly to produce more muon-friendly L scales without
  losing α universality?
