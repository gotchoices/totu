# Derivations — From Photon to Particle

**Status:** In progress (3 of ~10 derivations complete)

A roadmap and index for the analytical derivations that put
MaSt on a first-principles foundation.  Each derivation is a
self-contained proof, building on the ones before it.  The
full algebra lives in the study files (linked below); this
paper provides the overview, the "why this step," and the
logical dependencies.

---

## 1. What we derive and from what

### The question

MaSt models particles as standing electromagnetic waves on
compact 2-tori.  The model postulates a mass formula, charge
assignments, spin rules, and coupling constants — and these
postulates successfully reproduce 18 of 20 known particle
masses from 4 inputs.  But postulates are not proofs.

**Can the postulates be derived from more basic principles?**

### The inputs

The entire derivation chain uses only:

| Input | Source | Role |
|-------|--------|------|
| Special relativity | Einstein 1905 | 4-momentum, Lorentz invariance |
| E = hf | Planck 1900 / Einstein 1905 | Converts wavelength to energy (the one quantum input) |
| Standing-wave boundary conditions | Classical wave physics | Single-valuedness on compact domains |
| Differential geometry | Mathematics | Metrics, Christoffel symbols, geodesics |
| The cylinder condition | Klein 1926 | Fields don't vary along compact directions |

No quantum field theory.  No Lagrangians.  No gauge groups
postulated.  No Higgs mechanism.  The gauge structure (U(1)
symmetries, charge conservation, Lorentz force) emerges from
the geometry.

### What falls out

| Derived quantity | Which derivation | Status |
|-----------------|-----------------|--------|
| Rest mass from confinement | D1 (Track 1) | **Complete** |
| Quantized angular momentum | D1 (Track 1) | **Complete** |
| Inertial mass = rest mass | D1 (Track 1) | **Complete** |
| U(1)×U(1) gauge structure | D2 (Track 2) | **Complete** |
| Two-charge Lorentz force | D2 (Track 2) | **Complete** |
| Internal shear as new physics | D2 (Track 2) | **Complete** |
| Photon-on-torus mass formula | D3 (Track 3) | **Complete** |
| Mass-charge mixing from shear | D3 (Track 3) | **Complete** |
| MaSt mass formula μ² = (n_t/ε)² + (n_r − s n_t)² | D4 (Track 4) | In progress |
| Charge = tube compact momentum | *\<future\>* | Planned |
| Lorentz force on standing-wave states | *\<future\>* | Planned |
| Spin from holonomy on sheared torus | *\<future\>* | Planned (high-risk) |
| Magnetic moment from charge + spin | *\<future\>* | Planned |
| Compound modes from cross-shears | *\<future\>* | Planned |
| Full 6D particle inventory | *\<future\>* | Planned |

---

## 2. The roadmap

The derivations build in three stages: first the compact
(Ma) physics, then the junction with spacetime (St), and
finally the substrate dimension (ℵ) that links them through
time.

```
══════════════════════════════════════════════════════════
 STAGE 1: Physics on the compact dimensions (Ma, 6D)
══════════════════════════════════════════════════════════

D1: Confined photon → mass + angular momentum
│
│   (special relativity + E = hf + boundary conditions)
│
▼
D2: Kaluza-Klein on a 2-torus
│
│   (differential geometry + cylinder condition)
│
├──────────────────┬──────────────────┐
▼                  ▼                  ▼
D3: Mass        <future>:         <future>:
│               Charge             Spin (?)
▼                  │                  │
D4: MaSt μ²        │              <future>:
│                  │              Mag moment
└─────────┬────────┘                  │
          ▼                           │
       <future>:                      │
       Lorentz force                  │
          │                           │
          └──────────┬────────────────┘
                     ▼
               <future>:
               Two-tori + cross-shears
                     │
                     ▼
               <future>:
               Full 6D MaSt (all three sheets)


══════════════════════════════════════════════════════════
 STAGE 2: Junction with spacetime (Ma + St = 10D)
══════════════════════════════════════════════════════════

        D10 (6D Ma block established)
              │
              ▼
     ┌────────────────────┐
     │  Spacetime block   │
     │  (3 S + 1 t = 4D)  │
     │  = standard GR     │
     │  Minkowski metric   │
     └────────┬───────────┘
              │
              ▼
     Ma-St off-diagonal block
     (how compact modes source
      fields in spacetime)
              │
              ▼
     Coulomb force, EM radiation,
     gravitational coupling


══════════════════════════════════════════════════════════
 STAGE 3: The ℵ substrate (Ma + ℵ + St = 11D)
══════════════════════════════════════════════════════════

     ┌──── Ma (6D) ────┐
     │                  │
     │   Ma-ℵ coupling  │
     │   (per-sheet     │
     │    ring entries) │
     │                  │
     └──────┬───────────┘
            │
            ▼
     ┌──── ℵ (1D) ─────┐
     │                  │
     │  ℵ diagonal = 1  │
     │  (Planck-scale   │
     │   substrate)     │
     │                  │
     │   ℵ-t coupling   │◄── the seat of α (?)
     │   (links compact │
     │    modes to time) │
     │                  │
     └──────┬───────────┘
            │
            ▼
     ┌──── St (4D) ────┐
     │                  │
     │  3 S + 1 t       │
     │  (flat spacetime) │
     │                  │
     └──────────────────┘
```

**Stage 1** (D1–D10) derives the physics that lives ON the
compact dimensions: mass, charge, spin, the mass formula,
compound modes.  This is the particle spectrum.

**Stage 2** joins the 6D Ma block to the 4D spacetime block,
producing the 10D metric.  The spacetime block IS standard
GR (Minkowski in the flat limit).  The off-diagonal Ma-St
entries encode how compact modes produce observable effects
in spacetime — the Coulomb field, electromagnetic radiation,
and gravitational coupling.

**Stage 3** adds the ℵ dimension (11D total).  ℵ is the
Planck-scale substrate on which the GRID lattice lives.  It
mediates the Ma-St coupling through time: the Ma-ℵ entries
connect compact modes to the substrate, and the ℵ-t entry
connects the substrate to the time dimension.  Whether ℵ is
the seat of α = 1/137 — the single coupling constant that
sets the strength of electromagnetism — is an open question
explored in R55 and R59.  The derivation of α from geometry
remains the outstanding unsolved problem.

D3, D5, D7 are independent given D2 — they can be done in
any order.  D6 needs both D3 and D5 (mass + charge).  D8
needs D7 (spin).  D9 and D10 integrate everything.  Stages
2 and 3 build on Stage 1's completed 6D block.

---

## 3. The derivations

### D1 — Mass and angular momentum from a confined photon

**File:** [`studies/R62-derivations/derivation-1.md`](
../studies/R62-derivations/derivation-1.md)
**Status:** Complete
**Uses:** SR, E = hf, standing-wave boundary conditions

A photon bouncing between two mirrors (Part A) or orbiting a
ring (Part B) has rest mass m = nh/(Lc) in the cavity's rest
frame.  This mass is also the inertial mass — the system
resists acceleration with coefficient m.

The ring case additionally produces quantized angular momentum
L_z = nℏ from the photon's tangential motion.  The gyroscopic
stability is standard.

**Key results (F1-F3):**
- F1: linear cavity → rest mass + inertia
- F2: ring → rest mass + angular momentum nℏ
- F3: the 2-torus is the natural next step (two confinement
  directions with cross-coupling)


### D2 — Kaluza-Klein on a 2-torus

**File:** [`studies/R62-derivations/derivation-2.md`](
../studies/R62-derivations/derivation-2.md)
**Status:** Complete
**Uses:** D1 + differential geometry, cylinder condition

Generalize KK from one compact circle to a 2-torus (T²).
The 6×6 metric (4 spacetime + 2 compact) produces two
independent U(1) gauge fields (A_μ and B_μ) from the
off-diagonal entries.  Two conserved compact momenta P_4, P_5
are identified as charges.

The genuinely new ingredient vs 5D KK: the **internal shear**
g_45, the off-diagonal entry within the 2×2 compact block.
When g_45 ≠ 0:
- The two gauge fields cross-couple in the Christoffel symbols
- Conserved charges P_a and kinetic velocities w^b are related
  by a non-diagonal matrix
- A pure-charge eigenstate has nonzero kinetic velocity in the
  OTHER compact direction (the origin of MaSt's n_r − s n_t)

**Key results (F4-F6):**
- F4: U(1)×U(1) gauge structure with two conserved charges
- F5: two-charge Lorentz force from the 6D geodesic projection
- F6: shear cross-coupling (new physics with no 5D analog)


### D3 — Photon on a 2-torus: 4D mass from compact momentum

**File:** [`studies/R62-derivations/derivation-3.md`](
../studies/R62-derivations/derivation-3.md)
**Status:** Complete
**Uses:** D1 + D2 + 6D null condition

Replace D2's massive test particle with a photon (null
trajectory in 6D).  The 6D null condition G_AB k^A k^B = 0
splits into:

> η_μν k^μ k^ν = −g_ab k^a k^b

The left side is the 4D mass-shell; the right side is the
compact momentum norm.  Therefore:

> **m²c² = h^ab P_a P_b**

The 4D rest mass is the inverse-internal-metric quadratic
form of the two conserved compact momenta.

For a diagonal, equal-radii torus: m = (h/Lc)√(n₄² + n₅²)
— the Pythagorean mass formula.

With shear: the mass formula has off-diagonal terms that mix
the two compact momenta — mass eigenstates differ from charge
eigenstates.  This is the structural origin of MaSt's
(n_r − s n_t) combination.

**Key results (F7-F10):**
- F7: general mass formula m²c² = h^ab P_a P_b
- F8: Pythagorean special case
- F9: mass-charge mixing from shear
- F10: inertia and Lorentz covariance confirmed


### D4 — Recovery of the MaSt mass formula

**File:** [`studies/R62-derivations/derivation-4.md`](
../studies/R62-derivations/derivation-4.md)
**Status:** In progress
**Uses:** D3 + explicit parametrization of g_ab in terms of (ε, s)

Map D3's general quadratic form h^ab P_a P_b to MaSt's
empirically-found formula μ² = (n_t/ε)² + (n_r − s n_t)²
by choosing the parametrization g_ab(ε, s).  This closes
the loop: **the MaSt mass formula is derived, not postulated.**


### *\<future\>* — Charge identification: tube as the charge-carrying winding

**Status:** Planned (pool item d)
**Uses:** D2

Declare that the tube direction couples to spacetime
(g_μ4 ≠ 0) while the ring does not (g_μ5 = 0).  Show that
charge Q then equals the compact momentum on the tube
winding, recovering MaSt's Q = −n₁ + n₅ as a one-time
convention.


### *\<future\>* — Lorentz force on standing-wave states

**Status:** Planned (pool item e)
**Uses:** D3 + charge derivation

Show that the Lorentz force from D2's geodesic projection
still holds when the test particle is a standing-wave
eigenstate (not a free particle on a single geodesic).
The cleanest demonstration that mass, charge, and the
Lorentz force all come from the same geometric source.


### *\<future\>* — Spin from holonomy on the sheared 2-torus

**Status:** Planned (pool item f) — **highest-risk, highest-reward**
**Uses:** D2

The hypothesis: parallel transport around the two cycles of
the sheared 2-torus produces a holonomy phase.  When this
phase equals π × (odd integer), the wavefunction changes sign
under a 2π rotation — the defining property of spin ½.

If this works, MaSt's empirical spin rule (odd tube winding
→ spin ½) is derived from the torus metric.  If it doesn't,
the spin rule remains a postulate, and the failure tells us
what extra structure is needed.


### *\<future\>* — Magnetic moment from charge + spin

**Status:** Planned (pool item g, depends on spin derivation)

Once charge and spin are derived from the same geometry, the
magnetic moment follows from Lorentz covariance — E and B
always come as a matched set in F_μν.  The Dirac-equation
analog on the 2-torus should give g = 2 with no free
parameters.  Anomalous corrections (g − 2) are a stretch
goal.


### *\<future\>* — Compound modes from cross-shears (two 2-tori)

**Status:** Planned (pool item h)

Extend from one 2-torus to two with cross-shears between
them.  Show that compound modes (modes spanning both tori)
emerge as eigenstates of the joint 4×4 metric.  This is the
analytical version of what R54 did numerically — the neutron,
baryons, and mesons as cross-sheet modes.


### *\<future\>* — Full 6D MaSt with three sheets

**Status:** Planned (pool item i)

Three 2-tori (electron, neutrino, proton sheets) with all 12
cross-shear entries.  Show that the resulting 6D structure
recovers the full model-E particle inventory.  Mostly
bookkeeping once the preceding derivations are in place, but
the deliverable that proves the program reaches the existing
predictions.

---

## 4. What remains open

Even if all 10 derivations succeed:

- **α = 1/137** is an input, not derived.  The coupling
  constant enters through the Ma-St off-diagonal entries.
  Studies R55 and R59 explored mechanisms but did not derive α
  from geometry alone.

- **The compact dimension scales** (L_electron, L_proton,
  L_neutrino) are inputs.  Why these specific sizes is not
  addressed by the derivations — they take the geometry as
  given and derive the physics on it.

- **The strong and weak forces** are partially addressed
  (cross-sheet coupling may be the strong force; the neutrino
  sheet may mediate the weak) but not rigorously derived.

- **Spin (D7) is high-risk.**  Standard physics derives spin
  from spinor representations of the Lorentz group.  The
  holonomy approach is a hypothesis.  If D7 fails, spin
  remains a postulate.

---

## 5. Relationship to other documents

| Document | Role |
|----------|------|
| [`primers/kaluza-klein.md`](../primers/kaluza-klein.md) | Background: KK theory from scratch, including Lorentz force derivation (Appendix A).  D2 generalizes this to two compact dimensions. |
| [`primers/charge-from-energy.md`](../primers/charge-from-energy.md) | Intuitive narrative of the charge mechanism (bending → leakage → charge).  D5 makes it rigorous. |
| [`primers/size-matters.md`](../primers/size-matters.md) | The Compton view: mass as frequency, particles as cavities.  D1 proves this. |
| [`models/model-E.md`](../models/model-E.md) | The working model whose postulates the derivations aim to prove.  D4 derives its mass formula; D10 would reproduce its full inventory. |
| [`grid/charge-emergence.md`](../grid/charge-emergence.md) | GRID-level charge mechanism (junction leakage from bending).  Complements D5's KK-level derivation. |
| [`papers/gut.md`](gut.md) | The narrative paper ("Good Unification Theory") that tells the story these derivations make rigorous. |
| [`studies/R62-derivations/`](../studies/R62-derivations/) | The study containing the actual derivation files and the full program framing. |

---

## References within the derivation chain

Each derivation produces numbered lemma results (F1, F2, ...)
that subsequent derivations cite.  The chain:

| Result | Statement | Used by |
|--------|-----------|---------|
| F1 | Linear cavity: m = nh/(2Lc), inertia | D3 |
| F2 | Ring: m = nh/(Lc), L_z = nℏ | D3 |
| F3 | 2-torus is the natural next step | D2 framing |
| F4 | U(1)×U(1) gauge structure | D3, future (charge, spin) |
| F5 | Two-charge Lorentz force | future (Lorentz on standing waves) |
| F6 | Shear cross-coupling | D3, D4, future (spin) |
| F7 | Mass formula m²c² = h^ab P_a P_b | D4, future (compound modes) |
| F8 | Pythagorean special case | D4 |
| F9 | Mass-charge mixing from shear | D4, future (spin) |
| F10 | Inertia on the 2-torus | future (Lorentz on standing waves) |
