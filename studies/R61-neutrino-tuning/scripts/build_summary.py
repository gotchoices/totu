"""Build R61/findings-summary.md — one concise table of all shortlisted candidates."""

from __future__ import annotations

import os
import sys

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STUDY_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from track4_charge_neutrality import rank_candidates_7, deduplicate

SOLAR_DM2_21 = 7.53e-5
HC_EV_NM     = 1239.84193           # hc in eV·nm
H_EV_S       = 4.135667696e-15      # Planck's h in eV·s


def main() -> int:
    eps_grid = np.linspace(2.0, 10.0, 17)
    base_s = np.geomspace(0.005, 0.1, 41).tolist()
    s_grid = np.array(sorted(set(base_s + [0.022, 0.060])))
    w_equal = (1/7,) * 7
    results = rank_candidates_7(
        eps_grid, s_grid, weights=w_equal,
        pair_delta=0.1, enum_delta=0.5,
        tol=0.027, target=33.6, nt_max=3, nr_max=6,
    )
    shortlist = deduplicate(results, 15)

    out = os.path.join(STUDY_DIR, "findings-summary.md")
    with open(out, "w") as f:
        f.write("# R61 — candidate summary\n\n")
        f.write("Top-15 ν-sheet candidates under Track 4 scoring "
                "(charge-neutrality + harmonic flag, equal weights).  "
                "Masses calibrated to solar Δm²₂₁ = 7.53×10⁻⁵ eV².  "
                "Frequencies: f = mc²/h; wavelengths: λ_C = hc/mc²; "
                "sheet circumferences: L_ring = hc/E₀, L_tube = ε · L_ring.\n\n")

        f.write("| # | triplet | ε | s | ratio | m₁/m₂/m₃ (meV) | f₁/f₂/f₃ (THz) | λ₁/λ₂/λ₃ (μm) | Σm (meV) | L_ring/L_tube (μm) | E₀ (meV) | mechanisms | comp |\n")
        f.write("|--:|---------|--:|--:|------:|---------------:|---------------:|--------------:|---------:|------------------:|---------:|:-----------|-----:|\n")

        for i, r in enumerate(shortlist, start=1):
            t = r.best
            sc = r.best_scores
            dmu2_21 = t.b.mu2 - t.a.mu2
            E0_sq = SOLAR_DM2_21 / dmu2_21
            E0_meV = np.sqrt(E0_sq) * 1000
            masses = [np.sqrt(m.mu2) * E0_meV for m in (t.a, t.b, t.c)]
            freqs = [m * 1e-3 / H_EV_S / 1e12 for m in masses]
            wavelengths = [HC_EV_NM / (m * 1e-3) / 1000 for m in masses]  # nm → μm
            Sigma_m = sum(masses)
            L_ring_um = (HC_EV_NM / (E0_meV * 1e-3)) / 1000
            L_tube_um = L_ring_um * r.eps

            trip = (f"({t.a.n_tube:+d},{t.a.n_ring:+d}) "
                    f"({t.b.n_tube:+d},{t.b.n_ring:+d}) "
                    f"({t.c.n_tube:+d},{t.c.n_ring:+d})")
            mech = "/".join(m[:3] for m in sc.neutrality_mechanisms)
            m_str = f"{masses[0]:.1f}/{masses[1]:.1f}/{masses[2]:.1f}"
            f_str = f"{freqs[0]:.2f}/{freqs[1]:.2f}/{freqs[2]:.2f}"
            l_str = f"{wavelengths[0]:.1f}/{wavelengths[1]:.1f}/{wavelengths[2]:.1f}"
            L_str = f"{L_ring_um:.1f}/{L_tube_um:.1f}"

            f.write(
                f"| {i} | {trip} | {r.eps:.2f} | {r.s:.4f} | {t.ratio:.2f} | "
                f"{m_str} | {f_str} | {l_str} | {Sigma_m:.0f} | "
                f"{L_str} | {E0_meV:.1f} | {mech} | {sc.composite:.2f} |\n"
            )

        f.write("\n**Legend.** ")
        f.write("`triplet` = (n_tube, n_ring) for ν₁, ν₂, ν₃.  ")
        f.write("`mechanisms`: Maj = Majorana (±n_tube pair within 10% mu² split); ")
        f.write("R48 = inherently uncharged (|n_tube|≥2 per CP synchronization rule).  ")
        f.write("`comp` = composite score [0–1] under 7-criterion equal-weight scoring.\n\n")
        f.write("See [findings.md](findings.md) for full derivation; ")
        f.write("[outputs/track4_shortlist.md](outputs/track4_shortlist.md) ")
        f.write("for per-criterion breakdown.\n")

    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
