# R61 — Losinets mantle as K-V elastic wake

Tests R60's Interpretation 2: the mantle at ≈ 1.3 fm is the Kelvin–Voigt
elastic wake of the charged rotational core (≈ 0.25–0.4 fm), not a
feature of the MaSt T⁶ eigenmode amplitude itself.

**Status**: complete (partial pass). See `findings.md`.

Key result: with the Hill-vortex exterior (ψ = A sin²θ/r, |u|² ∝ 1/r⁶)
and r_core = 0.40 fm (the R60/MaSt inner-scale peak), the wake energy
density falls to 10⁻³ of its surface value at r ≈ 1.26 fm — within 3%
of Losinets's Hofstadter-based mantle radius r_m ≈ 1.30 fm. The match
requires a threshold choice (η = 10⁻³) that the K-V framework does not
fix internally.

## Scripts

```
python scripts/exterior_hill.py      # Task A — exterior field & |u|²
python scripts/candidate_scales.py   # Task B — five candidate lengths
python scripts/wake_threshold.py     # Task C & D — η sweep, neutron check
```

All three require only `numpy` and the project's `studies/lib/constants.py`.
