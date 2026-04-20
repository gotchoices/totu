"""
R61 Task A — Hill-vortex exterior velocity field and kinetic-energy density.

Background (Losinets EfD §3.1, Appendix F; baryon paper §2.2)
-------------------------------------------------------------
In the co-moving frame the Hill spherical vortex has stream function

    ψ_ext^com(r, θ) = (U/2) (r₀³/r − r²) sin²θ       (r ≥ r₀)

where U is the translation speed of the vortex and r₀ the core radius.
The −(U/2) r² sin²θ term encodes the uniform counter-flow present in the
co-moving frame; in the lab frame, with fluid at rest at infinity and
the vortex held stationary, this uniform piece drops out, leaving the
pure external dipole

    ψ_ext(r, θ) = A · sin²θ / r,       A ≡ U r₀³ / 2

The axisymmetric Stokes-stream-function velocity components are

    u_r = (1 / (r² sinθ)) ∂ψ/∂θ =  2A cosθ / r³
    u_θ = −(1 / (r sinθ)) ∂ψ/∂r =   A sinθ / r³

so

    |u|²(r, θ) = (A² / r⁶) · (4 cos²θ + sin²θ)

and ⟨|u|²⟩_θ = (A² / r⁶) · 2 (spherical-surface average with weight sinθ).

The K-V circulation obeys the Hill relation  Γ = 5 U r₀  (EfD eq 67 inline),
so  A = Γ r₀² / 10.

Kinetic-energy density:  w_kin(r, θ) = ½ ρ₀ |u|²
Elastic contribution in steady oscillation at angular frequency ω scales as
½ G |∇d|² with d ≈ u/(iω), i.e. ~|u|² as well.  We therefore use |u|² as
the wake-decay proxy and track its radial fall-off.

Note: ticket estimated |u|² ∝ 1/r⁴.  The correct 3-D dipole exterior gives
|u|² ∝ 1/r⁶.  All downstream threshold formulas use r_mantle = r_core · η^(−1/6).
"""

import math
import numpy as np


def hill_dipole_amplitude(U, r_core):
    """A = U r_core^3 / 2.  Units: whatever U, r_core are given in."""
    return 0.5 * U * r_core**3


def hill_U_from_circulation(Gamma, r_core):
    """Hill-vortex relation Γ = 5 U r_core  (EfD eq 67 text)."""
    return Gamma / (5.0 * r_core)


def hill_omega_from_circulation(Gamma, r_core):
    """Zone angular velocity ω = Γ/(2π r_core²)  (baryon eq 4)."""
    return Gamma / (2.0 * math.pi * r_core**2)


def exterior_velocity(r, theta, U, r_core):
    """Return (u_r, u_theta) for a stationary Hill vortex (lab frame).

    Valid for r >= r_core.  Inside the core the interior solution applies.
    """
    A = hill_dipole_amplitude(U, r_core)
    u_r = 2.0 * A * np.cos(theta) / r**3
    u_t = A * np.sin(theta) / r**3
    return u_r, u_t


def u_sq(r, theta, U, r_core):
    """|u|² for exterior dipole.  Scales as (r_core/r)^6 at fixed θ."""
    A = hill_dipole_amplitude(U, r_core)
    return (A**2 / r**6) * (4.0 * np.cos(theta)**2 + np.sin(theta)**2)


def u_sq_angular_avg(r, U, r_core):
    """Angle-averaged |u|² (weighted by sinθ dθ on the unit sphere):

        ⟨|u|²⟩ = (A² / r⁶) · 2
    """
    A = hill_dipole_amplitude(U, r_core)
    return 2.0 * A**2 / r**6


def kinetic_energy_density(r, theta, rho0, U, r_core):
    """½ ρ₀ |u|²  at (r, θ)."""
    return 0.5 * rho0 * u_sq(r, theta, U, r_core)


def wake_decay_ratio(r, r_core):
    """Angle-averaged |u(r)|² / |u(r_core)|².

    From (A²/r⁶)·2 normalised to (A²/r_core⁶)·2:   (r_core / r)^6.
    """
    return (r_core / r) ** 6


def r_mantle_from_threshold(r_core, eta):
    """Invert (r_core/r_mantle)^6 = η  →  r_mantle = r_core · η^(−1/6)."""
    return r_core * eta ** (-1.0 / 6.0)


if __name__ == "__main__":
    # Sanity: reproduce surface velocity magnitude and dipole decay.
    # Take Γ such that the angular velocity ω = ω_N (proton natural frequency).
    import sys, os
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(here, "..", "..", "lib"))
    from constants import hbar, c

    m_p = 1.67262192369e-27  # kg  (PDG 2022)
    omega_N = m_p * c * c / hbar  # natural proton angular frequency (rad/s)
    print(f"ω_N = {omega_N:.3e} rad/s")

    for r_core_fm in (0.25, 0.40):
        r_core = r_core_fm * 1e-15  # fm → m
        Gamma = omega_N * 2.0 * math.pi * r_core**2  # from ω = Γ/(2π r²)
        U = hill_U_from_circulation(Gamma, r_core)
        print(f"\nr_core = {r_core_fm} fm")
        print(f"  Γ = {Gamma:.3e} m²/s,  U = {U:.3e} m/s,  U/c = {U/c:.3e}")
        print(f"  angle-avg |u(r_core)|² = {u_sq_angular_avg(r_core, U, r_core):.3e} (m/s)²")

        for r_fm in (r_core_fm * 2, r_core_fm * 3.162, r_core_fm * 4.642, 1.3e0):
            r = r_fm * 1e-15
            ratio = wake_decay_ratio(r, r_core)
            print(f"  r = {r_fm:5.3f} fm  →  |u|²/|u₀|² = {ratio:.4e}")
