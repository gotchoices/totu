"""
R61 Task C — energy-threshold calculation for the K-V wake extent.

Operational definition: r_mantle is the radius at which the angle-averaged
exterior kinetic-energy density w(r) falls to fraction η of its value at
the core surface:
                    w(r_mantle) / w(r_core) = η

For the Hill-vortex exterior dipole (see exterior_hill.py),
                    w(r) ∝ |u|²(r) ∝ 1/r⁶
so
                    r_mantle = r_core · η^(−1/6).

The ticket's hint computed η^(−1/4), assuming |u|² ∝ 1/r⁴ (2-D dipole
scaling).  The correct 3-D axisymmetric Hill exterior gives 1/r³ velocity
and therefore 1/r⁶ energy density; we use that correct scaling here.

Sweep η over several orders of magnitude for both candidate r_core values
and report which (r_core, η) combinations hit Losinets's r_mantle ≈ 1.3 fm.
"""

import math

r_core_values = {
    "0.25 fm (Losinets Hofstadter)":      0.25,
    "0.40 fm (R60 MaSt inner-scale)":     0.40,
}

# Thresholds to scan
eta_values = [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5]

target_fm = 1.30
target_band = 0.20   # ±20% "within tolerance" band

print("=" * 72)
print("R61 Task C — wake-threshold scan (Hill exterior, |u|² ∝ 1/r⁶)")
print("=" * 72)

print(f"\nTarget mantle radius: {target_fm} fm  (Losinets Hofstadter inputs, ±1.2 fm)")
print("Pass band (ticket C): |r_mantle − 1.3 fm| / 1.3 fm ≤ 20%")

for rc_label, rc_fm in r_core_values.items():
    print(f"\n--- r_core = {rc_label} ---")
    print(f"    {'η':>10s}    {'r_mantle/r_core':>16s}    {'r_mantle (fm)':>14s}    {'% off 1.3 fm':>12s}")
    print(f"    {'-'*10:>10s}    {'-'*16:>16s}    {'-'*14:>14s}    {'-'*12:>12s}")
    for eta in eta_values:
        ratio = eta ** (-1.0 / 6.0)
        r_m = rc_fm * ratio
        off_pct = 100 * (r_m / target_fm - 1)
        marker = ""
        if abs(off_pct) <= 20:
            marker = "  ✓"
        elif abs(off_pct) <= 50:
            marker = "  *"
        print(f"    {eta:10.4g}    {ratio:16.4f}    {r_m:14.4f}    {off_pct:+12.1f}%{marker}")

# Invert: what η does each r_core need to hit 1.3 fm exactly?
print("\n--- η required to hit r_mantle = 1.30 fm exactly ---")
for rc_label, rc_fm in r_core_values.items():
    required = (target_fm / rc_fm) ** (-6)
    print(f"  r_core = {rc_label:32s}  η_required = {required:.3e}")
print("""
Physical-plausibility note for η:

  10⁻²  ≈ −20 dB   "typical detection noise floor" ratio.  Fails with
                   1/r⁶ decay — gives r_mantle only ≈ 2× r_core.
  10⁻³  ≈ −30 dB   Common 'end of near-field' convention for dipole antennas.
                   Hits r_mantle ≈ 1.26 fm for r_core = 0.40 fm — match
                   within 3% of Losinets's 1.3 fm.  Requires 0.4 fm input.
  10⁻⁴  ≈ −40 dB   Spectroscopy / detector noise limit.  Hits 1.16 fm
                   for r_core = 0.25 fm — off by 11%, inside the ±20% band.
  10⁻⁵  Impractically low for a physical scattering experiment.

With the *correct* 1/r⁶ exterior-energy decay there is no single η with
a cleanly-derived meaning that hits 1.3 fm simultaneously for both r_core
inputs.  Partial match only.
""")

# Neutron check
print("=" * 72)
print("Task D — neutron consistency")
print("=" * 72)
print("""
The Hill-vortex exterior dipole amplitude A = U r_core³ / 2 depends on U.
Reversing the core circulation (Γ → −Γ) gives U → −U (EfD Γ = 5 U r_core);
the exterior velocity flips sign (u → −u) but the magnitude |u| is
unchanged.  Therefore:

    w_mantle(proton) = w_mantle(neutron)
    r_mantle(proton) = r_mantle(neutron)     ✓

Losinets's construction takes the neutron's core rotation reversed while
the mantle zone is unchanged.  The wake picture is *identically* consistent
with this: the mantle as an exterior response depends only on |Γ|, not sgn Γ.

Pass.
""")
