# R63 findings — translating MaSt's spin-½ rule into K-V language

Status: **complete** — three candidate mechanisms tested against
Losinets's baryon-paper §2.2 open problem and MaSt's compound-mode spin
inventory.  **Verdict: none closes the problem cleanly.**  M1
(half-wrap double cover) reproduces the compound rule but requires
importing spinor structure not native to K-V; M2 (paired circulation)
fails at the composition step; M3 (embedding-parity label) matches
labels but leaves Losinets's angular-momentum quantisation untouched.

**Naming.** Study lives at `R63-` because R60, R61, R62 were already
allocated.  The companion tickets are `R60-losinets-projection`,
`R61-losinets-mantle-wake`, and `R62-losinets-mvac`.

---

## Phase A — numerical evaluation of L = ρ₀ Γ r₀²

Script: `compute_L.py` (stdlib-only, < 1 s).

Inputs (ticket-specified):
- Ring major radius ρ = L₂/(2π) = **1.894 fm** (MaSt e-sheet).
- Circulation Γ = h/m_vac at n = 1, with m_vac = 21.2 GeV/c² (R62 I-1).
  Γ = 1.753 × 10⁻⁸ m²/s.
- Shear modulus G = 0.234 Γ²/r₀² (EfD §3).
- Medium density ρ₀ = G/c² = 0.234 Γ²/(r₀² c²).
- Two r₀ identifications: (i) L₁/(2π) = 750.7 fm; (ii) λ̄_e = 386.2 fm.

### Key algebraic result

Substituting the EfD closures into L:

<!-- L = ρ₀ Γ r₀² = 0.234 Γ²/(r₀² c²) · Γ · r₀² = 0.234 · Γ³ / c² -->
$$
L = \rho_{0}\,\Gamma\,r_{0}^{2}
  = \frac{0.234\,\Gamma^{2}}{r_{0}^{2}\,c^{2}}\cdot\Gamma\cdot r_{0}^{2}
  = \frac{0.234\,\Gamma^{3}}{c^{2}}.
$$

**r₀ drops out identically.**  Both identifications give the same
number (verified numerically to the floating-point precision of the
script).  This is itself a finding: under Losinets's own K-V
identifications the r₀ choice that Phase A's ticket asked us to
"report both ways" is spurious — L is determined by Γ and c alone
once G = 0.234 Γ²/r₀² is used.

### Numerical outcome

| r₀ identification           | r₀ (fm) | ρ₀ (kg/m³)  | L (SI)          |
|---|---:|---:|---:|
| (i)  L₁/(2π)                |  750.7  | 1.42 × 10⁻⁹ | 1.403 × 10⁻⁴¹   |
| (ii) λ̄_e                    |  386.2  | 5.37 × 10⁻⁹ | 1.403 × 10⁻⁴¹   |

### Dimensional issue (the real story)

The formula L = ρ₀ Γ r₀² has SI units

> [ρ₀][Γ][r₀²] = (kg/m³)(m²/s)(m²) = **kg·m/s**,

i.e. **linear momentum**, not angular momentum.  It is not directly
comparable to ℏ (= kg·m²/s) without supplying an additional length.
Several natural completions ℓ were tried; every one dwarfs ℏ by
17–22 orders of magnitude:

| ℓ                              |  ℓ (m)     | L·ℓ / ℏ        |
|---|---:|---:|
| ρ (ring radius)                | 1.9 × 10⁻¹⁵ | 2.5 × 10⁻²²    |
| 2π ρ                           | 1.2 × 10⁻¹⁴ | 1.6 × 10⁻²¹    |
| λ̄_e                            | 3.9 × 10⁻¹³ | 5.1 × 10⁻²⁰    |
| ℏ/(m_vac c)                    | 9.3 × 10⁻¹⁸ | 1.2 × 10⁻²⁴    |

To make L·ρ land at exactly ℏ, m_vac would have to shrink from
21 GeV/c² to ~1.3 keV/c² (a factor 1.6 × 10⁷).

**Outcome (per ticket taxonomy): A3.**  L does not land at either an
integer or a half-integer multiple of ℏ; the mismatch is structural
(dimensional + scale), not a factor-of-2 issue.

**Consequence.** Spin-½ in a MaSt confined mode cannot be recovered
from a refined *quantisation* of Losinets's bare angular-momentum
expression.  Any mechanism that attaches spin-½ to this L via a
quantisation refinement is already impossible.  The spin label must
attach to *something else*: a topological sector, a phase-coupling
partner, or an identification between traversals.

---

## Phase B — three candidate mechanisms, five-row inventory

The MaSt spin rule (§4 of the white paper):

> # of odd tube-winding integers in {n₁, n₃, n₅} determines spin parity:
> odd count → spin ½; even count → spin 0 or 1.

Inventory under test (from `models/model-E.md`):

| Mode      | (n₁, n₂, n₃, n₄, n₅, n₆) | Odd tubes | Obs. spin |
|-----------|-------------------------|-----------|-----------|
| electron  | (1, 2, 0, 0, 0, 0)      |    1      |   ½       |
| π±        | (−1, −1, −3, −3, 0, 0)  |    2      |   0       |
| proton    | (0, 0, −2, 2, 1, 3)     |    1      |   ½       |
| neutron   | (0, −4, −1, 2, 0, −3)   |    1      |   ½       |
| Σ−        | (−1, 2, −2, 2, −2, −2)  |    1      |   ½       |

### M1 — half-wrap / double-cover identification

**Claim.** An odd tube-winding integer means the confined-photon path
returns to its initial state only after *two* traversals, so the
angular momentum per single traversal is ℏ/2.  Composition: a
confined mode crossing k tubes is a tensor product of k factors, each
a spinor (spin-½) if the tube winding is odd and a scalar if even.
Spinor × spinor ∈ {spin-0, spin-1}, spinor × spinor × spinor ∈
{spin-½, spin-³⁄₂}.  Ground-state selection is handled separately.

In pure K-V variables, M1 reads: two Hopf-linked Hill rings with
odd linking number require two circuits of the primary to close the
joint phase, so the effective Onsager-Feynman quantum per single
circuit is Γ/2, and L per single traversal is halved.  The
"confined" photon in MaSt maps onto the primary ring; the tube
winding integer maps onto the linking number with a partner circuit.

| Row        | Odd tubes | M1 predicts                        | Pass? |
|---|---|---|---|
| electron   | 1         | one spinor factor → ½              | ✓     |
| π±         | 2         | 0 ⊕ 1 sector; spin-0 allowed       | ✓ (ambiguity acknowledged) |
| proton     | 1         | one spinor factor → ½              | ✓     |
| neutron    | 1         | one spinor factor → ½              | ✓     |
| Σ−         | 1         | one spinor factor → ½              | ✓     |

**Disposition.** M1 reproduces the parity rule for all five rows.
The one residual ambiguity — the 2-odd case gives {0, 1} rather
than 0 uniquely — is shared by MaSt itself (the particle table
contains both spin-0 and spin-1 compound modes with two odd tube
windings; e.g. the ρ meson mode has sh = 2 and spin 1), so M1 is
no worse than the MaSt statement it is translating.

**But** the "double cover" input is spinor geometry, not K-V.  M1
is in K-V vocabulary *only if* Hopf-linking of Hill rings is the
realisation, and no K-V derivation of the ℏ/2-per-traversal
quantum from linking has been done in Losinets's papers or here.
M1 **survives the inventory test**, but **does not yet close the
open problem in K-V-native language** — it shows what structural
ingredient closure would require.

### M2 — paired circulation + reference phase (the trilogy §T3 conjecture)

**Claim.** The object compactified is not a single Losinets ring but
a (ring + reference phase) pair.  Free decomposition of such a pair
gives {spin-0, spin-1}, matching the Jones-vector structure of the
free photon.  An odd tube-winding constraint projects onto the
spin-½ sector by coupling the Jones phase to the winding parity.

**Composition test.** Two odd windings on different sheets — the
charged-pion configuration — would require the *composition of two
projections*.  In K-V variables the projection is a phase
identification: Jones a ↔ (−1)^(n_tube/1).  Composing two such
identifications can land on either scalar (spin-0) or vector
(spin-1).  There is no K-V selection rule picking spin-0 without
importing something external.

| Row        | Odd tubes | M2 predicts                              | Pass? |
|---|---|---|---|
| electron   | 1         | projection onto spin-½                   | ✓     |
| π±         | 2         | composition ambiguous; spin-0 or spin-1  | ✗ ambiguous — needs non-K-V selector |
| proton     | 1         | projection onto spin-½                   | ✓     |
| neutron    | 1         | projection onto spin-½                   | ✓     |
| Σ−         | 1         | projection onto spin-½                   | ✓     |

**Disposition.** M2 survives the single-odd rows by restatement but
**fails at the two-odd (π±) row** — it provides no mechanism in K-V
variables for selecting spin-0 over spin-1 when two projections
compose.  The Jones formalism of the free photon is strictly spin-1
and the projection recipe cannot reduce to spin-0 without a
non-K-V ingredient (a pair-wise phase-cancellation rule that
Losinets's photon paper does not supply).  Of the three candidates
M2 is the least supported by K-V.

### M3 — spin label from embedding parity, not from Γ

**Claim.** The circulation Γ remains spin-1 everywhere; L = ρ₀ Γ r₀²
stays quantised in units of ℏ, not ℏ/2.  The "½" that MaSt reads
off odd tube-winding parity is a label on the *compactification
sector*, not a feature of the ring's angular momentum.

**Composition.** Parity adds mod 2 over k factors: k odd windings
land in the parity-odd sector (spin-½ *label*) if k is odd,
parity-even sector (spin-0 or 1 *label*) if k is even.

| Row        | Odd tubes | M3 predicts                              | Pass? |
|---|---|---|---|
| electron   | 1         | parity-odd sector (spin-½ label)         | ✓     |
| π±         | 2         | parity-even sector (spin-0 or 1 label)   | ✓     |
| proton     | 1         | parity-odd sector (spin-½ label)         | ✓     |
| neutron    | 1         | parity-odd sector (spin-½ label)         | ✓     |
| Σ−         | 1         | parity-odd sector (spin-½ label)         | ✓     |

**Disposition.** M3 reproduces the compound-rule table exactly — it
is the minimal restatement of the rule.  Composition works by
construction (parity is additive mod 2).  But: M3 does **not**
derive ℏ/2 quantisation of L in Losinets's own equation; it simply
keeps the ℏ quantisation and attaches a parity label elsewhere.
Losinets's §2.2 open problem, stated as "quantisation of L in units
of ℏ/2", **is not closed by M3**.  M3's verdict on the open problem
is: "the problem as stated has no solution; the correct K-V
statement is that L is quantised in ℏ and spin-½ is not a property
of L at all."  That is a useful *structural* answer (it reframes
the question), not a *mechanical* one (it does not build a K-V
object whose angular momentum is ℏ/2).

---

## Phase B summary table

| Mechanism | electron | π± | proton | neutron | Σ− | Closes §2.2? |
|---|---|---|---|---|---|---|
| **M1** half-wrap     | ✓ | ✓ (with {0,1} ambiguity shared by MaSt) | ✓ | ✓ | ✓ | Conditionally, *if* Hopf-linked K-V derivation supplied |
| **M2** paired circ.  | ✓ | **✗ ambiguous** | ✓ | ✓ | ✓ | No — composition rule not K-V-derivable |
| **M3** embedding label | ✓ | ✓ | ✓ | ✓ | ✓ | No — relabels, does not derive ℏ/2 for L |

---

## Verdict

**None of the three candidates closes Losinets's baryon §2.2 open
problem cleanly in K-V language.**  The closest analytic call is
**M1**: it reproduces the compound-mode spin rule for all five
inventory rows with the same parity structure MaSt observes, and
the ℏ/2-per-traversal factor falls out of the double-cover
identification once the mechanism is accepted.  But the required
ingredient — two Hopf-linked Hill rings whose joint phase closes
only after two circuits of the primary — is **not** derived in
Losinets's trilogy, and would need a fresh K-V computation of the
phase accumulated along a linked ring pair.

**M2** fails at the charged-pion row: two odd windings compose to
{spin-0, spin-1} under paired-circulation projection with no K-V
mechanism for selecting the spin-0 component.  This falsifies the
conjecture floated in the earlier version of `losinets-trilogy.md`
§T3.

**M3** is the minimal reframe: the spin label attaches to
compactification parity, not to L.  It matches the inventory by
construction and implies that Losinets's formula L = ρ₀ Γ r₀²
remains a spin-1 angular momentum, not a half-integer one.  It is
the safest statement but it does **not** close §2.2 — it reframes
the problem as having no solution in its original wording.

### Structural reading

The negative result is informative.  Phase A already showed that
L = ρ₀ Γ r₀², evaluated under Losinets's own closures, is
20+ orders of magnitude off the ℏ scale and dimensionally not an
angular momentum at all.  Neither an M1-style halving nor an
M3-style relabelling addresses that gap.  A genuine K-V derivation
of half-integer spin would require *either*:

- **(a) a separate K-V object** (not a single Hill ring) whose
  circulation quantum is h/(2 m_vac) by construction — e.g. a
  Hopf-linked pair with odd linking number, or a ring whose phase
  is coupled to a reference-phase partner such that closure
  requires two circuits, *and*
- **(b) a K-V derivation of the elastic + kinetic angular-momentum
  functional** whose ground state has ℏ value (so the halved
  version gives ℏ/2).  This is the same §2.4 elastic-energy closure
  R62 flagged for m_vac — the two open problems are the same
  problem.

Until (a) + (b) are supplied, MaSt's spin rule is doing work that
K-V alone cannot currently express.  That is itself a structural
result about the trilogy-MaSt layer map: **T3 (spin sector) is the
deepest of the three tensions**, and R63 sharpens the negative
verdict on it.

---

## Bottom line (one-line verdicts)

- **Phase A**: L has the wrong units and wrong scale (A3), by 10²⁰.
- **M1**: survives all five rows; best candidate; not yet K-V-derived.
- **M2**: fails at π±; paired-circulation conjecture falsified here.
- **M3**: matches all rows by relabelling; does not close §2.2.
- **Closure verdict**: §2.2 stays **open**; R63 narrows the solution
  space to the M1 direction (linked-ring double cover) pending a
  K-V phase derivation not present in the trilogy.

---

## Pointers

- Script: `compute_L.py` (Phase A arithmetic; stdlib only).
- Inputs: `models/model-E.md` (particle inventory); `papers/white-paper.md`
  §4 (spin topological rule); `losinets/losinets_baryon.txt` §2.2
  (L = ρ₀ Γ r₀² and open-problem statement).
- Companion: `R62-losinets-mvac/findings.md` (m_vac open problem);
  the two §2.4 and §2.2 closures are structurally linked.
- Trilogy integration: `losinets/losinets-trilogy.md` §T3.
- Ticket: `tickets/implement/3-losinets-spin-half-mechanism.md`.
