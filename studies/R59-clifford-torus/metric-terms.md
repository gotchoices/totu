# R59 Metric Terms — knobs, values, and constraints

A reference for every metric coefficient R59 has considered, what it
controls, what value (if any) has been assigned to it, and whether
it is constrained or free.

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
| 5 | ν_t | Compact | ~μm–mm (neutrino tube) |
| 6 | ν_r | Compact | ~μm–mm (neutrino ring) |
| 7 | S_x | Extended | macroscopic (3D space) |
| 8 | S_y | Extended | macroscopic |
| 9 | S_z | Extended | macroscopic |
| 10 | t | Extended | time (Lorentzian) |

Reading order: **Material → Space → time** (matches the project's
"MaSt" framework name).  The 4×4 spacetime block (S₃ + t) sits in
the lower-right corner; the 7×7 material block (ℵ + 6 Ma) sits in
the upper-left.  The off-diagonal blocks between them (upper-right
and lower-left, mirror images by symmetry) are where R59's
α-architecture entries live.

Within each sheet, **tube comes before ring** to match the MaSt
notation convention `(n_tube, n_ring)`.

---

## Visual layout

The metric is symmetric — only upper triangle + diagonal shown.
Lower triangle is the mirror image (no unique information).
Notation:

- `1` = identity diagonal (Ma normalized)
- `1+εs` = ring diagonal inflated by internal shear
- `.` = zero
- **Bold** = consumed by model-E particle spectrum
- *Italic* = R59 proposed (variable)

```
           ℵ      p_t    p_r    e_t    e_r    ν_t    ν_r    S_x    S_y    S_z    t
         ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
   ℵ   0 │*g_aa*│*-σta*│  .   │*+σta*│  .   │  .   │  .   │  .   │  .   │  .   │*σ_at*│
         ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
   p_t 1 │      │  1   │**s_p**│  .   │  .   │  .   │**σ34**│  .   │  .   │  .   │  .   │
         ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
   p_r 2 │      │      │**1+εs**│  .   │  .   │  .   │**σ35**│  .   │  .   │  .   │  .   │
         ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
   e_t 3 │      │      │      │  1   │**s_e**│  .   │  .   │  .   │  .   │  .   │  .   │
         ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
   e_r 4 │      │      │      │      │**1+εs**│  .   │  .   │  .   │  .   │  .   │  .   │
         ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
   ν_t 5 │      │      │      │      │      │  1   │**s_ν**│  .   │  .   │  .   │  .   │
         ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
   ν_r 6 │      │      │      │      │      │      │**1+εs**│  .   │  .   │  .   │  .   │
         ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
   S_x 7 │      │      │      │      │      │      │      │  +1  │  .   │  .   │  .   │
         ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
   S_y 8 │      │      │      │      │      │      │      │      │  +1  │  .   │  .   │
         ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
   S_z 9 │      │      │      │      │      │      │      │      │      │  +1  │  .   │
         ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
   t  10 │      │      │      │      │      │      │      │      │      │      │ -1   │
         └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
```

**Reading the structure:**

- **Upper-left 7×7** (rows/cols 0–6): the *Material* block — ℵ +
  6 Ma. Contains all internal shears, cross-sheet shears, and the
  ℵ↔Ma_tube R59 architecture entries.
- **Lower-right 4×4** (rows/cols 7–10): the *Spacetime* block.
  All zeros except the identity S diagonals and the −1 t diagonal.
  This block stays diagonal (g(S,t) = 0 always — F40).
- **Upper-right and lower-left rectangles** (Material↔Spacetime):
  in the current architecture only the (0, 10) and (10, 0) entry
  is nonzero — the σ_at entry that connects ℵ to time.  Everything
  else in this cross-block is either zero (untested) or has been
  tested and found to break signature (Ma↔S, Ma↔t direct entries).

---

## Bold = consumed by model-E spectrum (cannot move)

| Symbol | Position | Value | Used for |
|--------|----------|-------|----------|
| s_p | (1,2) | 0.162037 | α at p-sheet via R19 |
| s_e | (3,4) | 2.004200 | Generation structure (R53) |
| s_ν | (5,6) | 0.022 | Neutrino mass ratio (R49) |
| σ34 | (1,6) | −0.18 | Neutron region cross-shear (R54) |
| σ35 | (2,6) | +0.10 | Neutron region cross-shear (R54) |
| (Ma diagonals) | (1,1)…(6,6) | 1 to ~6e5 | Driven by ε ratios + L scales |

---

## Italic = R59 proposed (variable for α coupling)

| Symbol | Position(s) | Status |
|--------|-------------|--------|
| σ_ta (magnitude) | (0,3), (0,1) | tube↔ℵ entries; signs ± from charge formula |
| σ_at | (0,10) | single ℵ↔t entry |
| g_aa | (0,0) | ℵ diagonal — assumed 1, never derived (F50–F52) |

**The R59 universality case (F42, F45) uses 3 numerical knobs +
charge-sign convention** for tube polarity.

---

## Critical conflict (F41)

The bold s_e at (3,4) makes the e-tube near-singular (smallest
Ma eigenvalue ~10⁻³).  Adding *+σ_ta* at (0,3) — required for the
universality architecture — pushes the smallest eigenvalue past
zero.  This means the tube↔ℵ architecture **cannot coexist with
model-E's internal shears**.  Either model-E's spectrum mechanism
must be replaced (so internal shears can be zeroed), or the α
architecture must move to a different block.  This is the central
R60 problem.

---

## ℵ in or out of the loop?

| Architecture | ℵ status | Outcome |
|--------------|----------|---------|
| Direct Ma↔t (10D) on model-E | OUT | Fails — F35 |
| Direct Ma↔t (10D) on clean metric | OUT | Caps at 0.57α — F48 |
| Ring↔ℵ↔t on model-E | IN | Fails — F39 |
| Tube↔ℵ↔t on model-E | IN | Breaks signature — F41 |
| Tube↔ℵ↔t on clean metric | IN | Universal but α not natural — F44, F50 |

**Verdict for R59:** ℵ stays in the loop **if** we want a chance
of reaching α.  Direct Ma↔t cannot get past 57% of α.  ℵ-mediated
can reach α but requires tuning.  ℵ is not derived, and its
diagonal is not pinned.

For R60: ℵ status remains an **open question** in the sense that
its scale (g(ℵ,ℵ)) is unconstrained.  But ℵ is structurally
required if α magnitude is to come from this family of metric
architectures.

---

## What this means for R60

The R59 results identify a clear architectural picture and a clear
remaining problem:

**What's settled:**
- Tube↔ℵ↔t gives exact structural universality (α_e = α_p = α_q
  for any singly-charged particle), arising from |n_tube| = 1.
- ℵ is needed in the loop (direct Ma↔t can't reach α).
- Model-E's internal shears block tube-based ℵ coupling.

**What's open for R60:**
- Particle spectrum without internal shears: can it be reproduced
  by some other mechanism (cross-sheet only, or ε ratios alone)?
- α magnitude: not derivable from this architecture's natural
  values.  Needs an external mechanism (extended R19, GRID lattice
  scale, moduli potential, etc.).
- ν-sheet integration: never directly tested in R59.

**The R60 challenge:** find a metric that:
1. Reproduces the model-E particle spectrum
2. Allows tube↔ℵ↔t for charge universality
3. Has a natural α magnitude from somewhere

These three requirements may be mutually compatible (model-F
exists) or in conflict (model-F doesn't exist).  R60 is scoped to
find out.
