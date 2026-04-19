# R60 Metric Terms — knobs, values, and constraints

A reference for every entry in the R60 11×11 metric: what it
controls, what value (if any) has been assigned to it, and its
constraint status under model-F (Track 12 baseline).

Companion CSV: [metric-terms.csv](metric-terms.csv) — same data,
spreadsheet-friendly.

---

## Index ordering

Dimensions are ordered by physical scale, smallest to largest:

| Index | Symbol | Type | Scale |
|-------|--------|------|-------|
| 0 | ℵ | Compact (sub-Planck) | smallest (GRID lattice edge) |
| 1 | p_t | Compact | ~fm (proton tube) |
| 2 | p_r | Compact | ~fm (proton ring) |
| 3 | e_t | Compact | ~pm (electron tube) |
| 4 | e_r | Compact | ~pm (electron ring) |
| 5 | ν_t | Compact | ~μm to mm (neutrino tube) |
| 6 | ν_r | Compact | ~μm to mm (neutrino ring) |
| 7 | S_x | Extended | macroscopic (3D space) |
| 8 | S_y | Extended | macroscopic |
| 9 | S_z | Extended | macroscopic |
| 10 | t | Extended | time (Lorentzian) |

Reading order: **ℵ → Material → Space → time**.  The 7×7 Material
block (indices 0–6) contains ℵ plus the three Ma sheets.  The
4×4 Spacetime block (indices 7–10) stays diagonal.  Off-diagonal
entries between them (the (0, 10) and its mirror) are where the
R60 α-architecture lives.

Within each sheet, **tube before ring** to match the MaSt mode
notation `(n_tube, n_ring)`.

---

## Visual layout

The metric is symmetric — only upper triangle + diagonal shown.
Lower triangle is the mirror image (no unique information).

Notation:

- `1` = identity diagonal (ℵ or S)
- `k` = per-sheet Ma diagonal scale = **0.04696 = 1.1803/(8π)** (single-k)
- `k·sε` = in-sheet shear off-diagonal
- `k·(1+(sε)²)` = ring diagonal of sheet block
- `.` = zero
- **Bold** = pinned by R59 F59 natural form (architecture)
- *Italic* = derived (structural, Track 7 prescription)
- ~strikethrough~ = tested and ruled out (see notes below)

```
           ℵ      p_t     p_r     e_t     e_r     ν_t     ν_r     S_x     S_y     S_z     t
         ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐
   ℵ   0 │ **1** │**-T**│ *R_p* │**+T** │ *R_e* │**+T** │ *R_ν* │   .   │   .   │   .   │ **A** │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   p_t 1 │       │   k   │ k·sε_p│   .   │   .   │   .   │   .   │   .   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   p_r 2 │       │       │k(1+sε²)│  .   │   .   │   .   │   .   │   .   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   e_t 3 │       │       │       │   k   │ k·sε_e│   .   │   .   │   .   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   e_r 4 │       │       │       │       │k(1+sε²)│  .   │   .   │   .   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   ν_t 5 │       │       │       │       │       │   k   │ k·sε_ν│   .   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   ν_r 6 │       │       │       │       │       │       │k(1+sε²)│  .   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   S_x 7 │       │       │       │       │       │       │       │  +1   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   S_y 8 │       │       │       │       │       │       │       │       │  +1   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   S_z 9 │       │       │       │       │       │       │       │       │       │  +1   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   t  10 │       │       │       │       │       │       │       │       │       │       │  -1   │
         └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘
```

Legend for the ℵ row:
- **+T** = +σ_ta = +√α (tube↔ℵ coupling, sign for e and ν sheets)
- **−T** = −σ_ta = −√α (tube↔ℵ coupling, sign for p sheet)
- *R_p, R_e, R_ν* = σ_ra per sheet = **(s·ε)·σ_ta** (derived, Track 7)
- **A** = σ_at = 4πα (ℵ↔t coupling, single global)
- **1** = g_aa (ℵ diagonal, pinned at natural form)

**Reading the structure:**

- **ℵ row** is where model-F's α architecture lives.  All
  non-trivial off-diagonals (tube and ring) connect Ma back to
  time via the σ_at link.
- **Sheet blocks** (rows/cols 1-2, 3-4, 5-6) are the Ma 2×2
  blocks per sheet, each uniformly scaled by `k`.
- **Cross-sheet** entries (e.g. p_t ↔ e_t, e_r ↔ ν_r) are all
  zero in R60 baseline.  Most tested cross-entries break
  signature or α universality (Track 7c F39); cross-sheet use
  reserved for future work with a proper structural prescription
  (pool item h).
- **S↔S and S↔t** block stays diagonal (no frame-dragging).
- **Direct Ma↔t** entries ruled out by R59 F2 / F43 (catastrophic
  mass shifts / broken universality).

---

## Numerical values at model-F baseline (Track 12)

### Global knobs

| Symbol | Value | Role |
|--------|-------|------|
| **g_aa** | 1 | ℵ diagonal, R59 F59 natural |
| **σ_ta** | √α ≈ 0.08542 | tube↔ℵ magnitude (signs ±1) |
| **σ_at** | 4πα ≈ 0.09170 | ℵ↔t coupling |
| **k** | 1.1803/(8π) ≈ 0.04696 | per-sheet diagonal scale (single-k) |

### Per-sheet geometry (inputs)

| Sheet | ε | s | sε | L_ring (fm) |
|-------|--:|--:|--:|---:|
| e | 397.074 | 2.004200 | 795.82 | 54.83 |
| p | 0.55 | 0.162037 | 0.0891 | 20.55 |
| ν | 2.0 | 0.022 | 0.044 | 1.96 × 10¹¹ |

### Derived ring↔ℵ entries

| Symbol | Formula | Value |
|--------|---------|------:|
| σ_ra_e | +(sε)_e · σ_ta | +67.98 |
| σ_ra_p | −(sε)_p · σ_ta | −0.00761 |
| σ_ra_ν | +(sε)_ν · σ_ta | +0.003759 |

---

## Status flag summary

| Flag | Meaning | Count |
|------|---------|------:|
| **Bold** pinned | R59 F59 natural form, not tunable | 5 (g_aa, σ_at, three σ_ta with signs) |
| *Italic* derived | Structural from Track 7 prescription | 3 (σ_ra per sheet) |
| regular (fit) | Free under solver; all converge to single k | 1 (k, shared across sheets) |
| `.` zero | Unused in R60 baseline | rest of 11×11 |

---

## What each block does

| Block | Role | Controls |
|-------|------|----------|
| ℵ diagonal | Reference scale for the α-mediator dimension | g_aa = 1 (assumed natural) |
| ℵ ↔ tube | α-delivery chain: Ma winding → ℵ | Sets α universality across charged particles |
| ℵ ↔ ring | **Cancels shear-induced mode-dependence (Track 7)** | Makes α mode-independent within each sheet |
| ℵ ↔ t | Closes the coupling chain to spacetime | Delivers α to Coulomb coupling in S |
| Sheet (i,i+1) shear | In-sheet structure — generation resonance, ghost ordering | Sets which mode is lightest on each sheet |
| Sheet ring diag | 1 + (sε)² — receives the shear contribution | Secondary mass structure |
| S diagonals | Flat Minkowski spatial | Standard |
| t diagonal | Lorentzian | Standard |
| Cross-sheet | Currently zero | Reserved for compound-mode tuning if ever needed |

---

## Critical constraints (all satisfied in baseline)

1. **Signature**: exactly one negative eigenvalue (the t direction).
2. **σ_ra prescription**: σ_ra_x = (s·ε)_x · σ_ta_x per sheet
   cancels shear-induced mode-dependence in α extraction.
3. **Single-k symmetry**: k_e = k_p = k_ν emergent from joint
   solve (verified across 6+ geometries; Track 14).
4. **α-sum rule**: α_Coulomb/α = (n_et − n_pt + n_νt)² for any
   compound mode.  For |Q|=1 particles α = α requires
   |α_sum| = 1.  For Z-nuclei α_sum = −Z gives α = Z²α.

---

## Historical note (ruled-out entries)

Entries that prior studies have tested and ruled out:

| Entries | Status | Reference |
|---------|--------|-----------|
| Direct Ma ↔ t (6 entries) | ~breaks signature or spectrum~ | R59 F2, F43 |
| ℵ ↔ S (3 entries) | ~R55 tested; replaced with ℵ ↔ t~ | R59 F59 chose ℵ↔t |
| p_t ↔ e_t (internal cross) | ~breaks signature~ | R59 F28 |
| p_t ↔ ν_r, ν_t ↔ p_t, etc. | mostly break signature or α universality (Track 7c); pool item h would address |
| Ring ↔ t direct | ~destroys universality~ | R59 F43 |

---

## See also

- [metric-terms.csv](metric-terms.csv) — full entry-by-entry grid
  with status flags (spreadsheet-friendly)
- [findings.md](findings.md) — track index with summary results
- [models/model-F.md](../../models/model-F.md) — the canonical
  model writeup using these parameters
