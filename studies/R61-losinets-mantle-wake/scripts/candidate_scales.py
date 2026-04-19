"""
R61 Task B — evaluate the five candidate length scales that could set r_mantle.

Question: which (if any) K-V or coupled length naturally produces ~1.3 fm
given a nucleon-sized rotational core?

Candidates (ticket §Setup):
  1. Viscous screening length  ξ_visc = √(η₀ τ / ρ₀) with τ = R = η₀/G.
     ⇒ ξ_visc = ν₀/c, where ν₀ = η₀/ρ₀.
  2. K-V relaxation length  ℓ_R = c R = c·η₀/G = ν₀/c. Same as (1).
     (R = ν₀/c² has units of time; cR has units of length.)
  3. Hill-exterior dipole decay — *no intrinsic length* (pure 1/r³ velocity
     ⇒ 1/r⁶ energy density).  Any characteristic scale must come from a
     threshold (Task C) or from another scale coupled in.
  4. Pion Compton wavelength  λ̄_π = ℏ/(m_π c).
  5. α^(−1/3) expansion of a core scale:  r_core · α^(−1/3)  and related.

Candidate (1)=(2) requires knowing η₀/ρ₀·c, which absolutely requires m_vac
(ν₀ has SI units m²/s and is fixed by the medium's material properties).
That is *deliberately out of scope* per the ticket.  We report the formulas
and the numerical expression only *if* a reasonable m_vac is assumed.

Candidates (4) and (5) are m_vac-free: they use only Standard-Model inputs
(m_π, α) and optionally a choice of r_core.
"""

import math

# ── inputs ────────────────────────────────────────────────────────────────────
alpha = 7.2973525693e-3
m_pi = 139.57039e6 * 1.602176634e-19 / (299_792_458.0 ** 2)  # charged pion, kg
m_pi0 = 134.9768e6 * 1.602176634e-19 / (299_792_458.0 ** 2)  # neutral pion, kg
m_p = 1.67262192369e-27  # proton mass, kg
hbar = 1.054571817e-34
c = 299_792_458.0

# proton reduced Compton
lambda_bar_p = hbar / (m_p * c)  # m
# pion Compton (charged)
lambda_bar_pi = hbar / (m_pi * c)
# pion Compton (neutral)
lambda_bar_pi0 = hbar / (m_pi0 * c)

# Losinets's Hofstadter inputs
r_core_Losinets = 0.25e-15  # m
r_mantle_target = 1.30e-15  # m

# R60 MaSt-projection inner-scale cluster
r_core_MaSt = 0.40e-15

print("=" * 72)
print("R61 Task B — candidate characteristic lengths")
print("=" * 72)

print(f"\nProton reduced Compton λ̄_p = {lambda_bar_p * 1e15:.4f} fm")
print(f"Pion±  reduced Compton λ̄_π  = {lambda_bar_pi * 1e15:.4f} fm")
print(f"Pion0  reduced Compton λ̄_π0 = {lambda_bar_pi0 * 1e15:.4f} fm")
print(f"α = 1/{1/alpha:.3f};  α^(-1/3) = {alpha**(-1/3):.4f}")

print("\n-- Candidate 1 & 2: K-V viscous/relaxation length ξ = ν₀/c --")
print("  Requires material input ν₀ (= η₀/ρ₀); equivalent to fixing m_vac.")
print("  Out of scope for this ticket (see tickets/implement/3-losinets-mvac-identifications).")
print(f"  Target to match: ξ = 1.3 fm  ⇒  ν₀ = c · 1.3 fm = {c * 1.3e-15:.3e} m²/s")
print("  (for comparison: liquid helium-II ν ≈ 2e-8 m²/s; atmosphere ν ≈ 1.5e-5 m²/s)")

print("\n-- Candidate 3: Hill-exterior decay --")
print("  No intrinsic length.  1/r⁶ kinetic energy density.")
print("  Characteristic scale must be set by threshold (Task C).")

print("\n-- Candidate 4: Pion reduced Compton wavelength --")
print(f"  λ̄_π±  = {lambda_bar_pi*1e15:.4f} fm    (vs 1.30 fm → miss {100*(lambda_bar_pi*1e15/1.3 - 1):+.1f}%)")
print(f"  λ̄_π0  = {lambda_bar_pi0*1e15:.4f} fm    (vs 1.30 fm → miss {100*(lambda_bar_pi0*1e15/1.3 - 1):+.1f}%)")
print("  Brings an extra particle scale into a model that purports to derive")
print("  nucleon structure from one vortex.  Accept only if an independent")
print("  mechanism couples the pion field to the K-V mantle.")

print("\n-- Candidate 5: α-derived expansion of a core scale --")
print(f"  α^(-1/3)                         = {alpha**(-1/3):.4f}")
print(f"  α^(-1/3) · λ̄_p                   = {alpha**(-1/3)*lambda_bar_p*1e15:.4f} fm")
for r_core_label, r_core in [("0.25 fm (Losinets)", r_core_Losinets),
                              ("0.40 fm (MaSt/R60)", r_core_MaSt)]:
    r_m = r_core * alpha**(-1/3)
    print(f"  α^(-1/3) · r_core [{r_core_label}] = {r_m*1e15:.4f} fm    "
          f"(vs 1.30 fm → miss {100*(r_m/r_mantle_target - 1):+.1f}%)")
print("  The α^(-1/3) ratio ≈ 5.157 is strikingly close to Losinets's")
print("  empirical r_m/r_c ≈ 5.2 (±1.2).  With r_core = 0.25 fm this lands")
print("  at 1.289 fm — parameter-free, within 1% of the Hofstadter mantle.")
print("  This is NOT derived from Losinets's linearised K-V framework; it")
print("  is a numerical coincidence worth flagging.  A mechanism would need")
print("  to connect the K-V wake extent to the dimensionless EM coupling α.")

print("\n-- Summary table (no free parameters) --")
print(f"  {'candidate':40s}  {'r_mantle (fm)':>14s}  {'% off 1.3':>10s}")
print(f"  {'-'*40:40s}  {'-'*14:>14s}  {'-'*10:>10s}")
cand = [
    ("λ̄_π± (charged pion Compton)",             lambda_bar_pi*1e15),
    ("λ̄_π0 (neutral pion Compton)",             lambda_bar_pi0*1e15),
    ("α^(-1/3)·r_core  [r_core = 0.25 fm]",     r_core_Losinets*alpha**(-1/3)*1e15),
    ("α^(-1/3)·r_core  [r_core = 0.40 fm]",     r_core_MaSt*alpha**(-1/3)*1e15),
    ("α^(-1/3)·λ̄_p",                            lambda_bar_p*alpha**(-1/3)*1e15),
    ("5.2 · λ̄_p (Losinets ratio × MaSt λ̄_p)",   5.2*lambda_bar_p*1e15),
]
for name, val in cand:
    off = 100*(val/1.3 - 1)
    marker = "  ✓" if abs(off) < 20 else ("  *" if abs(off) < 50 else "")
    print(f"  {name:40s}  {val:>14.4f}  {off:>+9.1f}%{marker}")

print("\n✓ = within 20%  (ticket pass threshold for Task B).")
