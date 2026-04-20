# Losinets

Materials and findings from engaging Dmitry Losinets's 2026 trilogy on vortex-based electrodynamics with the MaSt + GRID framework.

## What this folder is

Dmitry Losinets posted three papers on Zenodo in March 2026 developing a Kelvin–Voigt vortex-mechanical analogy for Maxwell's equations, a free-photon vortex-ring model, and a two-zone Hill-vortex model of baryons. The three papers form a coherent programme that parallels MaSt's compactified-photon particle-spectrum framework at several structural points. In April 2026 we ran a series of cross-framework derivations and numerical studies to map exactly where the frameworks agree, where they diverge, and what each can offer the other.

This folder holds the source PDFs, extracted text, and five synthesis documents. The work is complete through R60–R63 and the α↔R derivation; there are no open computational items remaining, only follow-on programmes identified in the synthesis docs.

## The three papers

| File | Subject | One-line summary |
|---|---|---|
| `losinets_EfD.pdf` / `.txt` | *Maxwell's Equations from Vortex Mechanics* | Exact formal isomorphism: Maxwell from a Kelvin–Voigt viscoelastic fluid carrying compact Hill-type vortex rings; charge = circulation invariant Q = ρ₀·r₀·Γ |
| `losinets_photon.pdf` / `.txt` | *Vortex Photon Model* | Free photon as a 3D vortex ring of radius ρ(ω) ∝ ω^(−½); Jones formalism from ring geometry; falsifiable near-field E_z ∝ sin b |
| `losinets_baryon.pdf` / `.txt` | *Baryon Magnetic Moments in a Two-Zone K-V Vortex Model* | Nucleon as a single Hill vortex with rotational core (r_c ≈ 0.25 fm) and irrotational mantle (r_m ≈ 1.3 fm); parameter-free |μ_c/μ_m| = r_m/r_c ≈ 5.2 |

## What we did

Five cross-framework derivations were run against the trilogy, each framed as a concrete ticket with pass/fail criteria:

| # | Study | Claim tested | Verdict |
|---|---|---|---|
| R60 | `studies/R60-losinets-projection/` | MaSt proton T⁶ eigenmode projects onto Losinets's two-zone charge density | **fails** kinematically (best ratio 1.77 vs target 5.2) |
| R61 | `studies/R61-losinets-mantle-wake/` | Losinets's mantle ≈ 1.3 fm is the K-V elastic wake of a MaSt eigenmode core | **partial pass** (r_mantle = 1.26 fm at η = 10⁻³, ±3%) |
| R62 | `studies/R62-losinets-mvac/` | MaSt's compactification scales fix Losinets's m_vac via the photon ring-radius relation | **fails** (4 identifications span 25 decades) |
| R63 | `studies/R63-losinets-spin-half/` | MaSt's odd-tube-winding → spin-½ rule translates into K-V language, closing Losinets's baryon §2.2 | **no candidate cleanly closes**; M1 (Hopf-linked rings) narrows the solution space |
| R-α | `losinets/alpha-vs-R.md` | α derives from Losinets's R = τ_KV via Planck-scale factors | **orthogonal axes** (R cancels algebraically); bonus: R ≈ t_P prediction if K-V is GRID coarse-graining |

## Headline findings

**The frameworks are complementary, not equivalent.** Naive point-for-point unification fails at every layer where we tested it. A layered picture emerges in its place: GRID describes the discrete Planck-scale microstructure; Losinets's K-V continuum is its long-wavelength limit (prediction: R = t_P ≈ 5.4 × 10⁻⁴⁴ s); Losinets's free photon has internal ring structure where MaSt has a plane-wave primitive (PINEM test decides); Losinets's compound-particle mantle is the K-V wake of a MaSt eigenmode core (the R61 quantitative match is the strongest three-way agreement obtained).

**Two of Losinets's own flagged open problems remain open and appear to be the same problem.** m_vac from E_ring = ℏω (photon §2.4) and L = ρ₀·Γ·r₀² quantisation in ℏ/2 (baryon §2.2) both require a full K-V derivation of the elastic + kinetic functionals beyond classical kinetic terms. MaSt does not fix either on its own, but its odd-tube-winding rule narrows the spin-½ mechanism to Hopf-linked rings.

**One numerical curiosity.** α^(−1/3) = 5.156 lands within 1% of Losinets's empirical r_m/r_c ≈ 5.2. Neither framework predicts this. Flagged for future work.

**Methodological impact on MaSt.** Losinets's trilogy supplies MaSt with candidate mechanisms for several of its own open items: a physical interpretation of compound particles (core + wake), a magnetic-moment formula (Q114-adjacent), a substrate-layer mechanical picture, and stylistic discipline around scope, diagnostic failure-reading, and experimental proposals.

## The five synthesis documents

Read these in roughly this order depending on the goal:

| Document | Purpose | Audience |
|---|---|---|
| `losinets-trilogy.md` | The original layer map and punch list. Superseded by `losinets_summary.md` for interpretive content; kept for the original framing. | Historical reference |
| `losinets_summary.md` | **Main analytical document.** Executive summary, technical background on all three frameworks, the five tested claims with results, the layered complementarity picture, open problems. | Anyone coming to the work fresh |
| `losinets_proposition.md` | Outward: what MaSt can offer Losinets, and how to approach him. Five concrete offers in priority order, four specific asks, delivery plan, expected responses. | If considering direct engagement with Losinets |
| `losinets_offerings.md` | Inward: what MaSt can take from Losinets, and how to explore it. Seven technical offers and four methodological habits, with priority ranking and follow-on study proposals. | MaSt/GRID developers planning next work |

**Quickest path in:** read the executive summary of `losinets_summary.md` (first section). That's 200 words and gives the verdict of the whole exercise. Then read whichever of the three supporting docs matches what you intend to do.

## Folder contents

```
losinets/
├── README.md                       this file
│
├── losinets-trilogy.md             original layer map and punch list (historical)
├── losinets_summary.md             main analytical synthesis
├── losinets_proposition.md         what MaSt can offer Losinets
├── losinets_offerings.md           what MaSt can take from Losinets
│
├── losinets_EfD.pdf / .txt         paper 1 — K-V substrate
├── losinets_photon.pdf / .txt      paper 2 — free photon as vortex ring
└── losinets_baryon.pdf / .txt      paper 3 — two-zone nucleon
```

External dependencies (referenced by the synthesis docs):

- `studies/R60-losinets-projection/` through `studies/R63-losinets-spin-half/` — the completed cross-framework studies.
- `losinets/alpha-vs-R.md` — the α↔R derivation and R = t_P prediction.
- `papers/white-paper.md`, `models/model-E.md` — MaSt.
- `grid/foundations.md` — GRID axioms.

## Status and next steps

**Closed for now.** All five planned cross-framework derivations have been executed. Five summary documents capture the findings, the collaboration framing, and the follow-on study proposals.

**Highest-leverage continuations** (per `losinets_offerings.md` §3):

1. Extend the R60/R61 core + K-V-wake methodology across the full MaSt compound-mode inventory — hyperons, nuclei, mesons. Each produces form-factor predictions testable at Jefferson Lab and similar facilities.
2. Apply Losinets's magnetic-moment formula μ = ρ₀·V·ω·(ω·r₀) to MaSt's electron mode as a candidate answer to Q114.
3. Derive the K-V continuum explicitly as the long-wavelength limit of GRID's phase-on-lattice dynamics and verify R = t_P falls out.
4. Close R55 using Losinets's α = π·ρ₀·r₀²·ℏ/(m_vac²·c) formula with Ma-S-derived inputs.

**If engaging Losinets externally** (per `losinets_proposition.md`): a single 2–3 page note with the four concrete offers (Planck R prediction, nucleon mantle calculation, Hopf-ring spin-½ candidate, m_vac negative result) plus the summary document as appendix. Timing: mid-to-late 2026 to allow prerequisites (K-V-language deliverable, self-derivation attempts) to settle first.
