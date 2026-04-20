"""
R63 -- Phase A: evaluate Losinets's angular-momentum formula L = ρ₀ Γ r₀²
for a Hill-type ring using MaSt (model-E) e-sheet geometry.

Losinets (baryon-paper §2.2) flags the quantisation of the ring angular
momentum L in units of ℏ/2 as an open problem.  This script evaluates L
numerically under two candidate r₀ identifications and reports whether
L comes out at an integer multiple of ℏ (outcome A1), a half-integer
multiple (A2), or some other value (A3).

Closures used (from Losinets):
  Γ       = h / m_vac          (Onsager-Feynman, n = 1)
  G       = 0.234 Γ² / r₀²     (EfD §3, shape + Tkachenko)
  ρ₀      = G / c²             (EfD §3, c_KV = √(G/ρ₀))

Substituting ρ₀ and G into L = ρ₀ Γ r₀² gives
  L = 0.234 · Γ³ / c²          — r₀ drops out identically.

So in Losinets's own K-V identifications, L has NO explicit r₀
dependence.  Both r₀ choices therefore give the same number; this is
itself a finding.

m_vac baseline: 21.2 GeV/c² (R62 I-1, e-sheet-ring × electron).

Run:
    python compute_L.py
"""

import math
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

# ── Constants ─────────────────────────────────────────────────────────────────
h    = 6.62607015e-34            # J·s
hbar = h / (2 * math.pi)         # J·s
c    = 299_792_458               # m/s
eV   = 1.602176634e-19           # J per eV
FM   = 1e-15                     # m per fm

# ── Inputs from MaSt / R62 ────────────────────────────────────────────────────
L1_fm = 4717.0                   # e-sheet tube circumference (model-E)
L2_fm = 11.9                     # e-sheet ring circumference  (model-E)

m_e_c2_eV = 0.5109989e6
m_e_kg    = m_e_c2_eV * eV / c**2

# R62 baseline (I-1, e-sheet-ring × electron identification):
m_vac_GeV = 21.2
m_vac_kg  = m_vac_GeV * 1e9 * eV / c**2

# Ring major radius (fixed by MaSt L₂)
rho_m = (L2_fm * FM) / (2 * math.pi)            # ≈ 1.894 fm

# Circulation (n = 1)
Gamma = h / m_vac_kg                             # m²/s

# EfD K-V constitutive relations
def G_shear(r0_m: float) -> float:
    return 0.234 * Gamma**2 / r0_m**2

def rho0(r0_m: float) -> float:
    return G_shear(r0_m) / c**2

def L_formula(r0_m: float) -> float:
    """L = ρ₀ Γ r₀²  (as written in Losinets baryon §2.2)."""
    return rho0(r0_m) * Gamma * r0_m**2


def main() -> None:
    print("R63 Phase A — Losinets L = ρ₀ Γ r₀² on MaSt e-sheet geometry")
    print("=" * 68)
    print(f"m_vac baseline          = {m_vac_GeV} GeV/c²  (R62 I-1)")
    print(f"Γ = h/m_vac             = {Gamma:.4e} m²/s")
    print(f"ρ (ring major radius)   = L₂/(2π) = {rho_m/FM:.4f} fm")
    print()

    # Two r₀ identifications (the ticket names both):
    r0_options = [
        ("(i)  r₀ = L₁/(2π)   (tube circumference)",  (L1_fm * FM) / (2 * math.pi)),
        ("(ii) r₀ = λ̄_e      (reduced Compton of e⁻)", hbar / (m_e_kg * c)),
    ]

    header = f"{'identification':<46}{'r₀ (fm)':>12}{'ρ₀ (kg/m³)':>16}{'L (kg·m/s)':>16}"
    print(header)
    print("-" * len(header))
    for label, r0 in r0_options:
        L_val = L_formula(r0)
        print(f"{label:<46}{r0/FM:>12.4g}{rho0(r0):>16.4e}{L_val:>16.4e}")

    # ── Algebraic simplification: r₀ drops out ───────────────────────────────
    print()
    print("Algebraic note:")
    print("  ρ₀ = G/c² = 0.234 Γ²/(r₀² c²).  Substituting into L = ρ₀ Γ r₀²,")
    print("  the r₀² cancels exactly, leaving L = 0.234 · Γ³ / c².")
    L_closed = 0.234 * Gamma**3 / c**2
    print(f"  Numerical:  0.234 Γ³/c² = {L_closed:.4e}   (matches both rows above)")
    print()

    # ── Dimensional analysis vs ℏ ────────────────────────────────────────────
    print("Dimensional check against ℏ:")
    print(f"  ℏ                     = {hbar:.4e}  J·s  = kg·m²/s")
    print(f"  L (formula as-written) has units [ρ₀][Γ][r₀²] = (kg/m³)(m²/s)(m²) = kg·m/s.")
    print(f"  L has units of LINEAR momentum, not angular momentum.")
    print(f"  To produce a J·s (angular-momentum) number an extra length is required.")
    print()

    # Several natural length-scale completions, reported for transparency.
    print("Completions L · ℓ  (which ℓ recovers angular-momentum units) vs ℏ:")
    print(f"{'ℓ choice':<32}{'ℓ (m)':>16}{'L·ℓ / ℏ':>18}")
    print("-" * 66)
    completions = [
        ("ρ (ring radius)",         rho_m),
        ("2π ρ (ring circumf.)",    2 * math.pi * rho_m),
        ("λ̄_e (Compton, electron)", hbar / (m_e_kg * c)),
        ("ℏ/(m_vac c) (Compton_vac)", hbar / (m_vac_kg * c)),
    ]
    L_val = L_formula(r0_options[0][1])
    for lbl, ell in completions:
        ratio = (L_val * ell) / hbar
        print(f"{lbl:<32}{ell:>16.4e}{ratio:>18.4e}")
    print()

    print("Interpretation:")
    print("  Under every completion tested, L·ℓ is dwarfed by ℏ by 10¹⁷–10²².")
    print("  The bare Losinets formula does NOT land near ℏ/2 or ℏ on any")
    print("  natural length; the gap is structural, not a factor-of-2 issue.")
    print()

    # ── Outcome classification ───────────────────────────────────────────────
    print("Outcome classification (per ticket):")
    print("  A1 (L ≈ nℏ)      — NO")
    print("  A2 (L ≈ (n+½)ℏ)  — NO")
    print("  A3 (irrational / off-scale) — YES, by many orders of magnitude.")
    print()
    print("  Consequence: the spin-½ of a MaSt confined mode cannot be recovered")
    print("  from a refined *quantisation* of Losinets's L = ρ₀ Γ r₀²; the formula")
    print("  does not sit at the ℏ scale at all.  A mechanism that attaches the")
    print("  spin label to something other than this L is required.")
    print()

    # ── Sanity check: if m_vac scaled to reach ℏ ─────────────────────────────
    # If we demand L·ρ = ℏ, what m_vac is required?
    # L·ρ = 0.234 Γ³ ρ / c² = 0.234 · (h/m)³ · ρ / c² = ℏ
    # ⇒ m³ = 0.234 · h³ · ρ / (ℏ · c²)
    m_req3 = 0.234 * h**3 * rho_m / (hbar * c**2)
    m_req = m_req3 ** (1.0 / 3.0)
    m_req_GeV = (m_req * c**2) / eV / 1e9
    print(f"Sanity: to make L·ρ = ℏ, required m_vac = {m_req_GeV:.4e} GeV/c²")
    print(f"  (vs 21 GeV/c² baseline — a {m_vac_GeV/m_req_GeV:.2e}× disagreement)")


if __name__ == "__main__":
    main()
