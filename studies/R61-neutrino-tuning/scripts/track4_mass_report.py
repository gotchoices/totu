"""R61 Track 4 mass report.

For each of the top-15 Track 4 candidates, calibrate E₀ to the
solar Δm²₂₁ = 7.53×10⁻⁵ eV² and report absolute masses, Σm,
predicted Δm²₃₁, predicted ν₁ frequency (THz), and the full Δm²
comb of n_ring transitions.

Ad-hoc post-processing — not a new track.
"""

from __future__ import annotations

import os
import sys

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "outputs")
sys.path.insert(0, SCRIPT_DIR)

from track2_candidates import mu2, delta_m2_comb  # noqa
from track4_charge_neutrality import (  # noqa
    rank_candidates_7,
    deduplicate,
)

SOLAR_DM2_21 = 7.53e-5   # eV²
ATM_DM2_31   = 2.53e-3   # eV²
H_EV_S       = 4.135667696e-15  # Planck's constant in eV·s (for f = E/h)


def report_candidate(result, sink):
    t = result.best
    sc = result.best_scores
    eps, s = result.eps, result.s

    dmu2_21 = t.b.mu2 - t.a.mu2
    E0_sq_eV2 = SOLAR_DM2_21 / dmu2_21
    E0_meV = np.sqrt(E0_sq_eV2) * 1000

    masses_meV = [np.sqrt(m.mu2) * E0_meV for m in (t.a, t.b, t.c)]
    Sigma_m = sum(masses_meV)
    dm2_31_predicted = (t.c.mu2 - t.a.mu2) * E0_sq_eV2

    # ν₁ frequency: f = m c² / h
    f_THz = (masses_meV[0] * 1e-3) / H_EV_S / 1e12  # meV → eV, Hz → THz

    # Comb for this geometry
    comb = delta_m2_comb(eps, s, E0_sq_eV2, max_dn=4, nr_sample=3)

    sink.write(f"## Candidate at (ε_ν={eps:.3f}, s_ν={s:.5f})\n\n")
    trip_str = (f"({t.a.n_tube:+d},{t.a.n_ring:+d}), "
                f"({t.b.n_tube:+d},{t.b.n_ring:+d}), "
                f"({t.c.n_tube:+d},{t.c.n_ring:+d})")
    sink.write(f"Triplet: **{trip_str}**\n")
    sink.write(f"Composite score: **{sc.composite:.3f}**  ")
    sink.write(f"Mechanisms: {'/'.join(sc.neutrality_mechanisms)}\n\n")
    sink.write(f"E₀ (calibrated to solar Δm²₂₁): **{E0_meV:.2f} meV**\n\n")
    sink.write("| ν | mode | µ² | mass (meV) | freq (THz) | L_z/ℏ |\n")
    sink.write("|---|------|---:|-----------:|-----------:|------:|\n")
    for i, (m, mi_meV, spin) in enumerate([
        (t.a, masses_meV[0], sc.spins[0]),
        (t.b, masses_meV[1], sc.spins[1]),
        (t.c, masses_meV[2], sc.spins[2]),
    ], start=1):
        f_i_THz = (mi_meV * 1e-3) / H_EV_S / 1e12
        sink.write(
            f"| ν_{i} | ({m.n_tube:+d}, {m.n_ring:+d}) | {m.mu2:.4f} | "
            f"{mi_meV:.2f} | {f_i_THz:.2f} | {spin:.3f} |\n"
        )
    sink.write(f"\nΣm = **{Sigma_m:.1f} meV** (cosmo bound 120 meV)\n\n")
    sink.write(f"Predicted Δm²₃₁ = **{dm2_31_predicted:.3e} eV²** ")
    sink.write(f"(atmospheric target {ATM_DM2_31:.2e} eV²)\n\n")
    sink.write("**Δm² comb predictions (n_ring transitions):**\n\n")
    sink.write("| transition | Δm² (eV²) | spread |\n")
    sink.write("|:-----------|----------:|-------:|\n")
    for e in comb[:6]:
        sink.write(f"| {e.nt_from} → {e.nt_to} | {e.dm2_mean:.3e} | {e.dm2_spread:.1e} |\n")
    sink.write("\n---\n\n")


def main() -> int:
    # Re-run the Track 4 ranking
    eps_grid = np.linspace(2.0, 10.0, 17)
    base_s = np.geomspace(0.005, 0.1, 41).tolist()
    s_grid = np.array(sorted(set(base_s + [0.022, 0.060])))

    print("Recomputing Track 4 shortlist...")
    w_equal = (1/7,) * 7
    results = rank_candidates_7(
        eps_grid, s_grid, weights=w_equal,
        pair_delta=0.1, enum_delta=0.5,
        tol=0.027, target=33.6, nt_max=3, nr_max=6,
    )
    shortlist = deduplicate(results, 15)

    out_path = os.path.join(OUT_DIR, "track4_mass_report.md")
    with open(out_path, "w") as f:
        f.write("# R61 Track 4 — mass and frequency report\n\n")
        f.write(f"For each top-15 candidate, E₀ is calibrated so ")
        f.write(f"Δm²₂₁ = {SOLAR_DM2_21:.2e} eV² (solar).  All masses ")
        f.write(f"and predicted Δm²₃₁ follow from that one calibration ")
        f.write(f"plus the mode geometry.\n\n")
        f.write("Format: for each candidate, the distinguished triplet, ")
        f.write("E₀, individual ν masses in meV and frequencies in THz, ")
        f.write("Σm, predicted Δm²₃₁, and the full Δm² comb of n_ring ")
        f.write("transitions.\n\n---\n\n")
        for i, r in enumerate(shortlist, start=1):
            f.write(f"# Rank {i}\n\n")
            report_candidate(r, f)

    # Also emit a compact summary table
    summary_path = os.path.join(OUT_DIR, "track4_mass_summary.md")
    with open(summary_path, "w") as fsum:
        fsum.write("# R61 Track 4 — mass summary\n\n")
        fsum.write("| # | (ε, s) | triplet | m₁ | m₂ | m₃ | Σm | Δm²₃₁ | ν₁ (THz) | mechanisms |\n")
        fsum.write("|--:|--------|---------|---:|---:|---:|---:|------:|---------:|:-----------|\n")
        for i, r in enumerate(shortlist, start=1):
            t = r.best; sc = r.best_scores
            dmu2_21 = t.b.mu2 - t.a.mu2
            E0_sq_eV2 = SOLAR_DM2_21 / dmu2_21
            E0_meV = np.sqrt(E0_sq_eV2) * 1000
            masses = [np.sqrt(m.mu2) * E0_meV for m in (t.a, t.b, t.c)]
            Sigma_m = sum(masses)
            dm2_31 = (t.c.mu2 - t.a.mu2) * E0_sq_eV2
            f1_THz = (masses[0] * 1e-3) / H_EV_S / 1e12
            trip = (f"({t.a.n_tube:+d},{t.a.n_ring:+d}) "
                    f"({t.b.n_tube:+d},{t.b.n_ring:+d}) "
                    f"({t.c.n_tube:+d},{t.c.n_ring:+d})")
            mech = "/".join(m[:3] for m in sc.neutrality_mechanisms)
            fsum.write(
                f"| {i} | ({r.eps:.2f}, {r.s:.4f}) | {trip} | "
                f"{masses[0]:.1f} | {masses[1]:.1f} | {masses[2]:.1f} | "
                f"{Sigma_m:.1f} | {dm2_31:.2e} | {f1_THz:.2f} | {mech} |\n"
            )

    print(f"  report:  {out_path}")
    print(f"  summary: {summary_path}")

    # Print the summary to stdout too
    print()
    print("Compact summary (masses in meV, frequencies in THz):")
    print(f"{'#':<3}{'(ε, s)':<20}{'triplet':<30}{'m₁':<7}{'m₂':<7}{'m₃':<7}{'Σm':<7}{'ν₁ THz':<9}{'mech':<20}")
    for i, r in enumerate(shortlist, start=1):
        t = r.best; sc = r.best_scores
        dmu2_21 = t.b.mu2 - t.a.mu2
        E0_sq_eV2 = SOLAR_DM2_21 / dmu2_21
        E0_meV = np.sqrt(E0_sq_eV2) * 1000
        masses = [np.sqrt(m.mu2) * E0_meV for m in (t.a, t.b, t.c)]
        Sigma_m = sum(masses)
        f1_THz = (masses[0] * 1e-3) / H_EV_S / 1e12
        trip = (f"({t.a.n_tube:+d},{t.a.n_ring:+d}) "
                f"({t.b.n_tube:+d},{t.b.n_ring:+d}) "
                f"({t.c.n_tube:+d},{t.c.n_ring:+d})")
        mech = "/".join(m[:3] for m in sc.neutrality_mechanisms)
        eps_s = f"({r.eps:.2f},{r.s:.4f})"
        print(f"{i:<3}{eps_s:<20}{trip:<30}"
              f"{masses[0]:<7.1f}{masses[1]:<7.1f}{masses[2]:<7.1f}"
              f"{Sigma_m:<7.1f}{f1_THz:<9.2f}{mech:<20}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
