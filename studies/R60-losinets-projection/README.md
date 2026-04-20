# R60 — Losinets Hofstadter projection

Project the MaSt (model-E) proton compound mode (0, 0, −2, 2, 1, 3) and
neutron compound mode (0, −4, −1, 2, 0, −3) from the compact six-torus
onto a 3D radial charge density ρ(r) and test Losinets's parameter-free
two-zone prediction r_m/r_c ≈ 5.2.

Targets (Losinets / Hofstadter 1960s electron-scattering data):

- **r_c ≈ 0.25 fm** (inner core scale)
- **r_m ≈ 1.3 fm** (outer mantle scale)
- **ratio r_m/r_c ≈ 5.2 ± 1.2** (parameter-free from equal-charge condition)

## Success criteria

1. Proton projection exhibits exactly two characteristic radial scales
2. Ratio lies in [4.0, 6.4]
3. Absolute scales within ~20% of 0.25 fm and 1.3 fm
4. Neutron projection has sign-reversed core (negative core, positive mantle, net charge 0)

## Contents

- `scripts/common.py` — shared MaD build, density variants (M-A, M-B, M-C), projections (P-1..P-4), scale extraction
- `scripts/project_proton.py` — runs the 12 (M × P) combinations for the proton
- `scripts/project_neutron.py` — runs the same 12 for the neutron and checks sign structure
- `findings.md` — results table, pass/fail on each criterion, narrative
- `STATUS.md` — study state

## References

- Ticket: [`tickets/implement/4-losinets-hofstadter-projection.md`](../../tickets/implement/4-losinets-hofstadter-projection.md)
- Losinets baryon paper: [`losinets/losinets_baryon.pdf`](../../losinets/losinets_baryon.pdf)
- Trilogy notes §C1: [`losinets/losinets-trilogy.md`](../../losinets/losinets-trilogy.md)
- Model-E: [`models/model-E.md`](../../models/model-E.md)
- Engine: [`studies/lib/ma_model_d.py`](../lib/ma_model_d.py)
- Parent study (metric build): [`studies/R54-compound-modes`](../R54-compound-modes/)
