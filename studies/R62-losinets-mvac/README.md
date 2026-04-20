# R62 — Losinets m_vac under MaSt identifications

Numeric check of Losinets's free-photon closure

    m_vac = hbar / (rho^2 * omega)

(from Γ = 2π ρ² ω = h/m_vac at n = 1) under four geometric
identifications of (ρ, ω) drawn from MaSt (model-E) confinement
lengths and particle Compton frequencies.

**Status**: complete. Cross-particle m_vac does **not** stabilise;
the 21 GeV/c² baseline (I-1) is reproducible but identification-
specific, shifting by 260× to the proton ring (I-3) and 10¹² to the
ν-sheet ring (I-4). See [`findings.md`](findings.md).

## Scripts

```
python compute_mvac.py     # prints the four-row table and I-5 scan
```

Stdlib-only (needs nothing beyond `math`, `sys`).

## Naming note

The ticket filed this as `R60-losinets-mvac`, but `R60-losinets-projection`
(Hofstadter two-scale projection, complete) and
`R61-losinets-mantle-wake` (K-V wake mantle, complete) were already
allocated. This study took the next free number, **R62**. The trilogy
§C2 pointer was updated accordingly.
