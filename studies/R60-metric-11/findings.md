# R60 Findings — index

Detailed findings per track are in separate files below.  This
document is a brief summary only.  See [README.md](README.md) for
framings, [metric-terms.md](metric-terms.md) for the parameter
reference, and [metric-terms.csv](metric-terms.csv) for the full
entry-by-entry grid.

## Track index

| Track | Focus | F-range | Outcome | Details |
|------:|:------|:--------|:--------|:--------|
| 1 | Solver infrastructure (11D metric builder, signature check, mode energy, α extractor, least-squares fitter + smoke tests) | F1–F4 | All four smoke tests pass. Solver validated against R59 F59 and model-E at floating-point precision. | [findings-1.md](findings-1.md) |
| 2 | Electron sheet viability map — (ε_e, s_e) region under R59 F59 α | F5–F10 | Signature OK iff `s·ε ≤ 3/√2` (exact closed form). Ghost-order requires `s ≥ 3/2`. Overlap is a bounded triangle with corner (ε=√2, s=3/2). Model-E's s·ε ≈ 796 is 375× over the bound. | [findings-2.md](findings-2.md) |
| 3 | Proton sheet viability map — (ε_p, s_p) under R59 F59 α at joint e+p | F11–F16 | Joint signature bound tightens to `(sε_e)² + (sε_p)² ≤ 7/2`. **Critical surprise:** α universality breaks when shears are on (α_p/α_e drifts to 8.78× at some anchors). R59 F59's clean-metric claims don't survive shears at constant k. | [findings-3.md](findings-3.md) |
| 4 | Per-sheet diagonal compensation — free k_x per sheet to rescue α universality | F17–F21 | Joint 4×4 solve (L_e, k_e, L_p, k_p) against (m_e, m_p, α_e, α_p) converges cleanly in 66% of tested (ε, s) configs. Two failure modes: signature cliff, and α-decoupling at R53 generation resonance. | [findings-4.md](findings-4.md) |
| 5 | Proton viability under shearless electron + closed-form α-decoupling locus | F22–F26 | Derived `Q = 0 ⟺ n_r/n_t = sε + 1/(sε)` for any single-sheet mode (validated to 10⁻³¹). Key rules: **(1, 1) modes never decouple**, (1, 2) decouples at sε = 1, (1, 3) at sε ≈ 0.382 or 2.618. With shearless e, proton region is 72.7% viable. | [findings-5.md](findings-5.md) |
| 6 | Joint e+p+ν solver with ν architecturally coupled (sign_nu = +1) on R61 candidate ν-sheet geometries | F27–F31 | Joint 6×6 solve converges for 3 of 4 R61 candidates at R59 F59 defaults. **But α is mode-dependent within sheared sheets** (ν₁ targeted at α but ν₂ lands at 1.19α, ν₃ at 0.91α — 28% spread). Problem surfaces. | [findings-6.md](findings-6.md) |
| 7, 7b | Ring↔ℵ structural cancellation (add σ_ra = sε·σ_ta per sheet) + re-solve on augmented metric | F32–F38 | Cancellation works exactly: **ν-mode spread collapses from 28% to 0%**. Re-solve gives all targets at α to floating-point precision with k_e = k_p = k_ν = 0.04696 = 1.1803/(8π). Untargeted ν₂, ν₃ land at α automatically. R60 architecture validated on both axes. | [findings-7.md](findings-7.md) |
| 7c | Inter-sheet shear compatibility check — test whether activating Ma cross-sheet σ entries preserves α universality | F39–F41 | **Negative.** Most cross-sheet activations break signature OR α universality. Track 7's per-sheet fix doesn't extend freely. Cross-sheet σ is not a free knob — pool item **h** would derive an extended prescription if Track 8 needs it. | [findings-7.md](findings-7.md) |
| 7d | Magic-shear baseline re-solve — use s_e = 2, s_p = 3 to make target modes lightest on each sheet | F42–F45 | **Clean win** on e and p: joint solve converges at same single-k value (1.1803/(8π)); all targets met; α universal across sheets AND across modes; ghost ordering ✓ on e and p. ν-sheet (1, 0) ghost persists (handle via R61 filter, pool item **j**). Track 8 baseline established. | [findings-7.md](findings-7.md) |
| 8 | Compound mode search (μ, τ, neutron) on Track 7d baseline | F46–F50 | **Mixed.** Discovered compound α is exactly quantized: `α/α = (n_et − n_pt + n_νt)²`. Clean tau match (2,−6,−2,*,1,−1) at 0.37% off with α = α; clean neutron match (−1,6,−1,*,−1,−3) at 0.14% off with α = α. **Muon blocked** by mass desert 50–200 MeV — no low-order compound reaches it on this metric. Model-E tuples don't survive the L-scale transition. | [findings-8.md](findings-8.md) |
| 8b | Extreme-geometry e-sheet sanity check — does σ_ra lift Track 2's sε bound? | F51 | **Yes, confirmed.** Signature holds at sε = 0.8, 2.25, 10, 100, 795 (model-E), 2000. σ_ra = (sε)·σ_ta makes signature u-independent. Track 2 bound is a property of the un-augmented metric only; augmentation removes it. | [findings-8.md](findings-8.md) |
| 9 | Re-solve with model-E extreme e-sheet (ε=397, s=2.004) on the σ_ra-augmented architecture | F52–F56 | **Major win.** Joint solver converges at k_e = k_p = k_ν = 0.04696 (single-k symmetry survives sε = 796!). All α universal. **Muon at model-E tuple (1,1,-2,-2,0,0) lands at 104.78 MeV — 0.83% off, matching model-E's own accuracy.** Tau at (2,3,-2,*,1,-1): 0.19% off. Neutron at (-1,-2,-1,*,-1,-3): 0.14% off. Model-E's spectrum revives on R60's augmented architecture with α universality as a bonus. | [findings-9.md](findings-9.md) |
| 10 | Broader hadron inventory on Track 9 baseline | F57–F62 | **R60 recovers 16/18 of model-E's matched particles.** 4 match at model-E's tuples (e, p bare, μ, Σ⁺ at 0.02%); 12 need R60-native tuples at α_sum = −1 (all within 2.5%, several better than model-E — ρ at 0.49% vs 0.97%, K± at 0.95% vs 1.77%); 2 still poor (π⁰, π± at ~23–25%, same failure as model-E). All R60 tuples are α-universal by construction. The α-sum filter acts as a natural selection rule. | [findings-10.md](findings-10.md) |
| 11 | Nuclear scaling audit (d, ⁴He, ¹²C, ⁵⁶Fe) | F63–F66 | **Nuclear scaling law works on R60.** All 4 nuclei within 1.6% (model-E was ≤ 1.1%). Deuterium matches model-E exactly (0.05%) with small decoration. **α_Coulomb = Z² × α to floating-point precision** for every Z tested (Z=1, 2, 6, 26 → α = 1, 4, 36, 676 exactly). The compound-α quantization rule naturally delivers nuclear Coulomb physics. | [findings-11.md](findings-11.md) |
| 12 | Proton sheet alignment with model-E (ε_p=0.55, s_p=0.162) | F67–F71 | **Clean alignment.** Model-E's compound tuples now land within ~1.6% on R60, comparable to model-E's own accuracy. 8 of 18 tuples have α = α (matching exactly at model-E level); 10 have α ≠ 1 (need R60-native alternatives). Single-k symmetry (k=0.04696) preserved. Nuclear scaling identical (not p-sheet-sensitive). **Track 12 baseline is the model-F candidate.** | [findings-12.md](findings-12.md) |
| 13 | R60-native α-universal inventory (13a) + ν-candidate sweep (13b) | F72–F77 | **13a:** R60 gives a clean α-universal inventory for 14 of 16 non-pion particles within ≤ 1.6%. Several R60-native tuples beat model-E (Ξ⁰ 19×, η 8×). Neutral compounds split into α = 0 (η, η′, φ, ρ, K⁰, π⁰) vs α = α (Λ, Σ⁻, n, Ξ⁻, Ξ⁰, η′ etc.). **13b:** Five ν candidates tested on Track 12 architecture; all converge with identical inventory + nuclear accuracy (ν is invisible at these L scales). R61 #1 and R49 Family A tie for cleanest (full α universality on ν triplet, Δm² ratio 33.59). Model-F can document multiple viable ν options. | [findings-13.md](findings-13.md) |
| 14 | Analytical derivation of k = 1.1803/(8π) — pool item f (partial) | F78–F81 | **Partial resolution.** Phase 1 (empirical): confirmed k is a true fixed point — solver converges to 1.1803/(8π) from any k_init ≥ K_NAT. Phase 2 (symbolic): derived single-sheet α_Coulomb expression cleanly; multi-sheet derivation not closed. Phase 3 (natural form search): best match (1+4πα)² = 1.19181 is 0.97% off — no closed-form match found. **k is structural (confirmed); closed-form expression remains open.** | [findings-14.md](findings-14.md) |

## Current R60 baseline (Track 12 — model-F candidate)

Working metric after Track 12:

| Parameter | Value |
|-----------|-------|
| Sheet inputs (ε, s) | e: (397.074, 2.004200); p: (0.55, 0.162037); ν: (2.0, 0.022) |
| ν mode triplet | R61 #1: (+1,+1)(−1,+1)(+1,+2) (others viable — Track 13 pending) |
| k (all three sheets) | 4.696 × 10⁻² = 1.1803/(8π) |
| L_ring_e | 54.83 fm |
| L_ring_p | 20.55 fm |
| L_ring_ν | 1.96 × 10¹¹ fm |
| g_aa | 1 |
| σ_ta (tube↔ℵ) | √α (signs +1/−1/+1 for e/p/ν) |
| σ_ra_e (ring↔ℵ) | +67.98 (derived sε_e·σ_ta) |
| σ_ra_p (ring↔ℵ) | −0.00757 (derived) |
| σ_ra_ν (ring↔ℵ) | +0.003759 (derived) |
| σ_at (ℵ↔t) | 4πα |

All targets (three masses, three α = α) met at floating-point
precision.  Δm²₃₁/Δm²₂₁ = 33.59 cross-checks against R49's 33.6.
Ghost ordering natural on e-sheet (generation resonance).
Inventory: 8 model-E tuples at α = α match directly; 10 need
R60-native α-universal alternatives (Track 13a).  Nuclear scaling
at 0.05–1.5%.  Pion failure inherited from model-E.

## Status

Tracks 1–7b complete.  Architecture validated.  Ready for Track 8
(compound modes — μ, τ, neutron, hadrons) on the above baseline.
