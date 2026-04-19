"""
R62 -- Losinets m_vac under four geometric identifications of MaSt scales.

For a free photon modelled as a Losinets vortex ring, the Onsager-Feynman
quantisation Gamma = n*h/m_vac and the kinematic circulation
Gamma = 2*pi * rho^2 * omega combine (n = 1) to

    m_vac = hbar / (rho^2 * omega)

This script computes m_vac under four candidate identifications of
(rho, omega) drawn from MaSt (model-E) confinement scales and particle
Compton frequencies, to test whether any choice yields an
order-of-magnitude stable m_vac across particles and sheets.

Run:
    python compute_mvac.py
"""

import math
import sys

# Windows consoles default to cp1252; force UTF-8 so Greek/math glyphs print.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

# ── Constants ─────────────────────────────────────────────────────────────────
hbar = 1.054571817e-34           # J·s
c = 299_792_458                  # m/s
eV = 1.602176634e-19             # J per eV

# kg → eV/c² conversion: E = m c², divide by eV
KG_TO_EV = c * c / eV            # ≈ 5.6096e35 eV/c² per kg
KG_TO_MEV = KG_TO_EV * 1e-6
KG_TO_GEV = KG_TO_EV * 1e-9

FM = 1e-15                       # m per fm

# ── MaSt model-E L values (white-paper §3, fm) ────────────────────────────────
L1 = 4717.0         # e-sheet tube
L2 = 11.9           # e-sheet ring
L3 = 2.1e11         # ν-sheet tube
L4 = 4.2e10         # ν-sheet ring
L5 = 2.45           # p-sheet tube
L6 = 4.45           # p-sheet ring

# ── Particle Compton angular frequencies (ω = m c² / ℏ, rad/s) ────────────────
m_e_c2_eV = 0.5109989e6          # electron  rest energy (eV)
m_p_c2_eV = 938.272e6            # proton    rest energy (eV)
m_nu3_c2_eV = 58.2e-3            # heaviest predicted ν₃ eigenstate (eV)

omega_e = m_e_c2_eV * eV / hbar
omega_p = m_p_c2_eV * eV / hbar
omega_nu = m_nu3_c2_eV * eV / hbar


def m_vac(rho_fm: float, omega: float) -> float:
    """m_vac from Γ = 2π ρ² ω = h/m_vac at n = 1 → m_vac = ℏ/(ρ²ω). kg."""
    rho = rho_fm * FM
    return hbar / (rho * rho * omega)


def fmt_mass(m_kg: float) -> str:
    """Render a mass in physically-natural units (eV/c² → GeV/c²)."""
    ev = m_kg * KG_TO_EV
    if ev < 1.0:
        return f"{ev*1e3:8.3g} meV/c²"
    if ev < 1e3:
        return f"{ev:8.3g} eV/c²"
    if ev < 1e6:
        return f"{ev*1e-3:8.3g} keV/c²"
    if ev < 1e9:
        return f"{ev*1e-6:8.3g} MeV/c²"
    if ev < 1e12:
        return f"{ev*1e-9:8.3g} GeV/c²"
    return f"{ev*1e-12:8.3g} TeV/c²"


# ── Identifications ──────────────────────────────────────────────────────────
IDENTIFICATIONS = [
    ("I-1  e-sheet ring  × electron",  L2 / (2 * math.pi), omega_e),
    ("I-2  e-sheet tube  × electron",  L1 / (2 * math.pi), omega_e),
    ("I-3  p-sheet ring  × proton  ",  L6 / (2 * math.pi), omega_p),
    ("I-4  ν-sheet ring  × ν₃      ",  L4 / (2 * math.pi), omega_nu),
]


def main() -> None:
    print("Losinets m_vac = ℏ/(ρ² ω), n = 1")
    print("ρ is taken as L/(2π) for each identification (L a MaSt length).\n")

    header = f"{'label':<32}{'ρ (fm)':>14}{'ω (rad/s)':>14}{'m_vac (kg)':>18}{'m_vac':>18}"
    print(header)
    print("-" * len(header))

    rows = []
    for label, rho_fm, omega in IDENTIFICATIONS:
        m = m_vac(rho_fm, omega)
        rows.append((label, rho_fm, omega, m))
        print(f"{label:<32}{rho_fm:>14.4g}{omega:>14.3e}{m:>18.3e}  {fmt_mass(m):>16}")

    # ── Ratios to I-1 ─────────────────────────────────────────────────────────
    print("\nRatios of m_vac to the I-1 baseline (e-sheet ring × electron):")
    m_I1 = rows[0][3]
    for label, _, _, m in rows:
        ratio = m / m_I1
        print(f"  {label}: {ratio:.3e}  (log10 = {math.log10(ratio):+.2f})")

    # ── Sensitivity variant: ω → 2π ω ─────────────────────────────────────────
    # If one reads "ω" as 2πf rather than the angular frequency, m_vac scales
    # uniformly by 1/(2π). This shifts every row by the same factor, so
    # cross-particle ratios are unchanged; absolute values move by ~0.16×.
    print("\nSensitivity variant ω → 2π·ω (treat Compton as 2πf instead of ω):")
    print("  Uniform factor 1/(2π) ≈ 0.1592 on every m_vac above. Ratios unchanged.")
    for label, rho_fm, omega, _ in rows:
        m_alt = m_vac(rho_fm, 2 * math.pi * omega)
        print(f"  {label}: {fmt_mass(m_alt)}")

    # ── Baseline check ────────────────────────────────────────────────────────
    m_I1_gev = m_I1 * KG_TO_GEV
    ok = 18.0 < m_I1_gev < 24.0
    print(f"\nBaseline check: I-1 = {m_I1_gev:.2f} GeV/c² (target ≈ 21 GeV): "
          f"{'PASS' if ok else 'FAIL'}")

    # ── I-5 (exploratory): energy-condition closure ──────────────────────────
    # Losinets's thin-core classical vortex-ring KE:
    #   E_ring ≈ ½ ρ_m Γ² ρ [ ln(8ρ/r₀) − 7/4 ]
    # In the EfD substrate, G ≈ 0.234 Γ²/r₀²,  c = √(G/ρ_m),
    # so ρ_m = G/c² = 0.234 Γ²/(r₀² c²).  Substituting:
    #   E_ring ≈ ½ · 0.234 Γ²/(r₀² c²) · Γ² · ρ · [ln(8ρ/r₀) − 7/4]
    #         = 0.117 · Γ⁴ · ρ / (r₀² c²) · [ln(8ρ/r₀) − 7/4].
    # Setting E_ring = ℏω with Γ = h/m_vac = 2π ℏ/m_vac:
    #   ℏω = 0.117 · (2π)⁴ ℏ⁴/m_vac⁴ · ρ / (r₀² c²) · [ln(8ρ/r₀) − 7/4]
    # and using ω = ℏ/(m_vac ρ²) (the n=1 closure):
    #   ℏ · ℏ/(m_vac ρ²) = 0.117 · (2π)⁴ ℏ⁴ ρ / (m_vac⁴ r₀² c²) · Λ
    # where Λ = ln(8ρ/r₀) − 7/4. Solving:
    #   m_vac³ = 0.117 · (2π)⁴ · ℏ² · ρ³ · Λ / (r₀² c²)
    # m_vac does NOT cancel — it comes out as a cube-root, but r₀ enters as
    # an independent free parameter. The closure only constrains the
    # combination (m_vac, r₀). This is documented (§2.4 photon paper) as
    # still open pending a K–V *elastic* energy derivation; the classical
    # kinetic form above is a lower bound, not the true E_ring.
    print("\nI-5 (exploratory, energy condition):")
    print("  Substituting ρ_m = 0.234 Γ²/(r₀² c²) into the thin-core kinetic")
    print("  energy E_ring = ½ρ_m Γ² ρ [ln(8ρ/r₀) − 7/4] and setting E_ring = ℏω")
    print("  gives  m_vac³ = 0.117·(2π)⁴·ℏ²·ρ³·[ln(8ρ/r₀) − 7/4] / (r₀² c²).")
    print("  m_vac does NOT cancel, but r₀ enters as a second free input;")
    print("  the closure pins a one-parameter family (m_vac, r₀), not a number.")
    print("  This reproduces Losinets's §2.4 statement that a proper K-V")
    print("  *elastic* energy derivation is required to close m_vac from c, G, ν₀.")

    # Indicative numerical scan over r₀ ∈ [0.1, 10] fm for ρ = L₂/(2π):
    rho_fm = L2 / (2 * math.pi)
    print(f"\n  Indicative scan at ρ = L₂/(2π) = {rho_fm:.3f} fm:")
    print(f"    {'r₀ (fm)':>10}{'Λ = ln(8ρ/r₀)−7/4':>24}{'m_vac (I-5, kg)':>20}{'m_vac':>18}")
    for r0_fm in (0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0):
        rho = rho_fm * FM
        r0 = r0_fm * FM
        arg = 8.0 * rho / r0
        if arg <= 1.0:
            continue  # log domain
        Lam = math.log(arg) - 7.0 / 4.0
        if Lam <= 0:
            continue
        m3 = 0.117 * (2 * math.pi) ** 4 * hbar * hbar * rho ** 3 * Lam / (r0 * r0 * c * c)
        m = m3 ** (1.0 / 3.0)
        print(f"    {r0_fm:>10.3g}{Lam:>24.3f}{m:>20.3e}  {fmt_mass(m):>16}")


if __name__ == "__main__":
    main()
