"""
R60 Track 6: Joint e+p+ν solver.

Add the ν-sheet on the same architectural footing as e and p,
then solve for all six free knobs (L_x, k_x for each sheet)
against six targets (three masses, three α=α).

Sheet inputs (held fixed):
  e:  (ε=1, s=0)        Track 5 baseline
  p:  (ε=1, s=0)        Track 5 baseline
  ν:  (ε=2, s=0.022)    R61 candidate #1 — top-ranked ν geometry

Architecture (R59 F59 natural, ν now active):
  σ_ta = √α, σ_at = 4πα, g_aa = 1
  signs: e=+1, p=−1, ν=+1  (R55-consistent)

Phases:
  Phase 1   — solve at g_aa = 1, R59 F59 defaults
  Phase 1.5 — rescan against R61 candidates 2, 3, 4 (only if 1 succeeds)
  Phase 2   — free g_aa as 7th knob (only if 1 fails for all R61 candidates)

Cross-checks:
  ν₂, ν₃ masses (no separate target — shared ε_ν, s_ν)
  Δm²₃₁/Δm²₂₁ ≈ 33.6
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok, num_negative_eigs,
    alpha_coulomb, mode_6_to_11, mu_sheet, derive_L_ring,
    L_vector_from_params, mode_energy, solve, Target,
    ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI, M_E_MEV, M_P_MEV,
)
from track4_diagonal_compensation import K_NATURAL


# ── Reference modes ────────────────────────────────────────────────────

def n_e():    return mode_6_to_11((1, 2, 0, 0, 0, 0))
def n_p():    return mode_6_to_11((0, 0, 0, 0, 1, 3))

def n_nu1(triplet):
    """ν₁ as the first entry of an R61 triplet."""
    nt, nr = triplet[0]
    return mode_6_to_11((0, 0, nt, nr, 0, 0))

def n_nu2(triplet):
    nt, nr = triplet[1]
    return mode_6_to_11((0, 0, nt, nr, 0, 0))

def n_nu3(triplet):
    nt, nr = triplet[2]
    return mode_6_to_11((0, 0, nt, nr, 0, 0))


# ── R61 candidate inputs ──────────────────────────────────────────────

# (label, ε_ν, s_ν, triplet (ν₁, ν₂, ν₃), m_ν₁ in meV)
R61_CANDIDATES = [
    ("R61-#1", 2.00, 0.0220,
        [(+1,+1), (-1,+1), (+1,+2)], 32.1),
    ("R61-#2", 8.50, 0.0078,
        [(+1,+1), (-2,+1), (+1,+2)], 29.1),
    ("R61-#3", 10.00, 0.0207,
        [(+2,+1), (-1,+1), (-1,+2)], 27.8),
    ("R61-#4", 2.50, 0.0193,
        [(+1,+1), (+2,+1), (+1,+4)], 13.8),
]

# Convert meV to MeV
def meV_to_MeV(m): return m * 1e-9


# ── Three-sheet metric builder ─────────────────────────────────────────

def make_p_three(eps_e, s_e, eps_p, s_p, eps_nu, s_nu,
                  k_e, k_p, k_nu,
                  L_ring_e, L_ring_p, L_ring_nu,
                  g_aa=1.0,
                  sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0):
    """Joint e+p+ν metric with all three sheets architecturally coupled."""
    return Params(
        eps_e=eps_e, s_e=s_e,
        eps_p=eps_p, s_p=s_p,
        eps_nu=eps_nu, s_nu=s_nu,
        k_e=k_e, k_p=k_p, k_nu=k_nu,
        g_aa=g_aa,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=sign_e, sign_p=sign_p, sign_nu=sign_nu,
        L_ring_e=L_ring_e, L_ring_p=L_ring_p, L_ring_nu=L_ring_nu,
    )


# ── Joint solver (Phase 1: g_aa fixed) ────────────────────────────────

def solve_three_phase1(eps_e, s_e, eps_p, s_p, eps_nu, s_nu,
                        n6_e, n6_p, n6_nu1, m_nu1_MeV,
                        k_init=K_NATURAL):
    """6 free knobs (L_x, k_x), 6 targets (m_x, α_x = α)."""

    # Initial L from closed form at k_init
    L_e_init  = derive_L_ring(M_E_MEV,  n6_e[0],  n6_e[1],  eps_e,  s_e,  k_init)
    L_p_init  = derive_L_ring(M_P_MEV,  n6_p[4],  n6_p[5],  eps_p,  s_p,  k_init)
    L_nu_init = derive_L_ring(m_nu1_MeV, n6_nu1[2], n6_nu1[3], eps_nu, s_nu, k_init)

    p0 = make_p_three(
        eps_e, s_e, eps_p, s_p, eps_nu, s_nu,
        k_init, k_init, k_init,
        L_e_init, L_p_init, L_nu_init,
        g_aa=1.0,
    )

    # Mode arrays
    n11_e   = mode_6_to_11(n6_e)
    n11_p   = mode_6_to_11(n6_p)
    n11_nu1 = mode_6_to_11(n6_nu1)

    PENALTY = 100.0

    def res_me(p):
        G = build_metric_11(p)
        L = L_vector_from_params(p)
        if not signature_ok(G):
            return PENALTY
        return (mode_energy(G, L, n11_e) - M_E_MEV) / M_E_MEV

    def res_mp(p):
        G = build_metric_11(p)
        L = L_vector_from_params(p)
        if not signature_ok(G):
            return PENALTY
        return (mode_energy(G, L, n11_p) - M_P_MEV) / M_P_MEV

    def res_mnu1(p):
        G = build_metric_11(p)
        L = L_vector_from_params(p)
        if not signature_ok(G):
            return PENALTY
        return (mode_energy(G, L, n11_nu1) - m_nu1_MeV) / m_nu1_MeV

    def res_ae(p):
        G = build_metric_11(p)
        if not signature_ok(G):
            return PENALTY
        return (alpha_coulomb(G, n11_e) - ALPHA) / ALPHA

    def res_ap(p):
        G = build_metric_11(p)
        if not signature_ok(G):
            return PENALTY
        return (alpha_coulomb(G, n11_p) - ALPHA) / ALPHA

    def res_anu(p):
        G = build_metric_11(p)
        if not signature_ok(G):
            return PENALTY
        return (alpha_coulomb(G, n11_nu1) - ALPHA) / ALPHA

    targets = [
        Target("m_e",  res_me),
        Target("m_p",  res_mp),
        Target("m_ν1", res_mnu1),
        Target("α_e",  res_ae),
        Target("α_p",  res_ap),
        Target("α_ν",  res_anu),
    ]

    return solve(
        p0,
        free=["L_ring_e", "k_e", "L_ring_p", "k_p", "L_ring_nu", "k_nu"],
        targets=targets,
        bounds={
            "L_ring_e":  (1e-3, 1e9),
            "k_e":       (1e-6, 1e6),
            "L_ring_p":  (1e-3, 1e9),
            "k_p":       (1e-6, 1e6),
            "L_ring_nu": (1e-3, 1e15),  # ν may be very large
            "k_nu":      (1e-6, 1e6),
        },
        xtol=1e-12, ftol=1e-12,
    )


# ── Smoke check ────────────────────────────────────────────────────────

def smoke():
    print("─" * 72)
    print("Smoke check — build three-sheet metric at R61 #1, R59 F59 defaults")
    print("─" * 72)
    label, eps_nu, s_nu, triplet, m_nu1_meV = R61_CANDIDATES[0]
    m_nu1_MeV = meV_to_MeV(m_nu1_meV)

    # Initial L from closed form at k = 1/(8π)
    L_e_0  = derive_L_ring(M_E_MEV,  1, 2, 1.0, 0.0, K_NATURAL)
    L_p_0  = derive_L_ring(M_P_MEV,  1, 3, 1.0, 0.0, K_NATURAL)
    L_nu_0 = derive_L_ring(m_nu1_MeV, triplet[0][0], triplet[0][1],
                            eps_nu, s_nu, K_NATURAL)

    p0 = make_p_three(
        1.0, 0.0, 1.0, 0.0, eps_nu, s_nu,
        K_NATURAL, K_NATURAL, K_NATURAL,
        L_e_0, L_p_0, L_nu_0,
    )
    G = build_metric_11(p0)
    nneg = num_negative_eigs(G)
    print(f"  signature ok = {signature_ok(G)} (neg eigs = {nneg})")

    L = L_vector_from_params(p0)
    E_e = mode_energy(G, L, n_e())
    E_p = mode_energy(G, L, n_p())
    E_nu1 = mode_energy(G, L, n_nu1(triplet))
    ae = alpha_coulomb(G, n_e())
    ap = alpha_coulomb(G, n_p())
    anu = alpha_coulomb(G, n_nu1(triplet))

    print(f"  E_e   = {E_e:.10f} MeV (target {M_E_MEV})")
    print(f"  E_p   = {E_p:.6f} MeV (target {M_P_MEV})")
    print(f"  E_ν₁  = {E_nu1*1e9:.4f} meV (target {m_nu1_meV})")
    print(f"  α_e/α = {ae/ALPHA:.6f}")
    print(f"  α_p/α = {ap/ALPHA:.6f}")
    print(f"  α_ν/α = {anu/ALPHA:.6f}")
    print(f"  L_ring_e  = {L_e_0:.4e} fm")
    print(f"  L_ring_p  = {L_p_0:.4e} fm")
    print(f"  L_ring_ν  = {L_nu_0:.4e} fm = {L_nu_0*1e-15:.4e} m")
    print()


# ── Per-candidate solver + report ─────────────────────────────────────

def solve_and_report(label, eps_nu, s_nu, triplet, m_nu1_meV):
    print("─" * 72)
    print(f"{label}: ν-sheet ε={eps_nu}, s={s_nu}, "
          f"triplet=({triplet[0]}, {triplet[1]}, {triplet[2]}), "
          f"m_ν₁={m_nu1_meV} meV")
    print("─" * 72)
    m_nu1_MeV = meV_to_MeV(m_nu1_meV)

    rj = solve_three_phase1(
        eps_e=1.0, s_e=0.0,
        eps_p=1.0, s_p=0.0,
        eps_nu=eps_nu, s_nu=s_nu,
        n6_e=(1, 2, 0, 0, 0, 0),
        n6_p=(0, 0, 0, 0, 1, 3),
        n6_nu1=(0, 0, triplet[0][0], triplet[0][1], 0, 0),
        m_nu1_MeV=m_nu1_MeV,
    )

    print(f"  converged   = {rj.success}")
    print(f"  message     = {rj.message[:60]}")
    print(f"  cost        = {rj.cost:.4e}")
    print(f"  k_e         = {rj.params.k_e:.6e}  "
          f"({rj.params.k_e/K_NATURAL:.3f}× R59 F59)")
    print(f"  k_p         = {rj.params.k_p:.6e}  "
          f"({rj.params.k_p/K_NATURAL:.3f}× R59 F59)")
    print(f"  k_ν         = {rj.params.k_nu:.6e}  "
          f"({rj.params.k_nu/K_NATURAL:.3f}× R59 F59)")
    print(f"  L_ring_e    = {rj.params.L_ring_e:.4e} fm")
    print(f"  L_ring_p    = {rj.params.L_ring_p:.4e} fm")
    print(f"  L_ring_ν    = {rj.params.L_ring_nu:.4e} fm")
    print(f"  residuals   = {rj.residuals}")

    G = build_metric_11(rj.params)
    sig = signature_ok(G)
    print(f"  signature_ok = {sig}")
    if not sig:
        print(f"    neg eigs = {num_negative_eigs(G)}")
        return rj, None

    L = L_vector_from_params(rj.params)
    E_e = mode_energy(G, L, n_e())
    E_p = mode_energy(G, L, n_p())
    E_nu1 = mode_energy(G, L, n_nu1(triplet))
    E_nu2 = mode_energy(G, L, n_nu2(triplet))
    E_nu3 = mode_energy(G, L, n_nu3(triplet))
    ae = alpha_coulomb(G, n_e())
    ap = alpha_coulomb(G, n_p())
    anu1 = alpha_coulomb(G, n_nu1(triplet))
    anu2 = alpha_coulomb(G, n_nu2(triplet))
    anu3 = alpha_coulomb(G, n_nu3(triplet))

    print(f"  E_e         = {E_e:.10f} MeV  (target {M_E_MEV})")
    print(f"  E_p         = {E_p:.6f}  (target {M_P_MEV})")
    print(f"  E_ν₁        = {E_nu1*1e9:.6f} meV  (target {m_nu1_meV})")
    print(f"  E_ν₂        = {E_nu2*1e9:.6f} meV")
    print(f"  E_ν₃        = {E_nu3*1e9:.6f} meV")
    # Δm² ratio
    dm2_21 = E_nu2**2 - E_nu1**2
    dm2_31 = E_nu3**2 - E_nu1**2
    if dm2_21 > 0:
        ratio = dm2_31 / dm2_21
        print(f"  Δm²₃₁/Δm²₂₁ = {ratio:.4f}  (R49 target: 33.6)")
    print(f"  α_e/α       = {ae/ALPHA:.6f}")
    print(f"  α_p/α       = {ap/ALPHA:.6f}")
    print(f"  α_ν₁/α      = {anu1/ALPHA:.6f}")
    print(f"  α_ν₂/α      = {anu2/ALPHA:.6f}")
    print(f"  α_ν₃/α      = {anu3/ALPHA:.6f}")

    metrics = {
        "label": label, "converged": rj.success and sig and rj.cost < 1e-6,
        "cost": rj.cost,
        "k_e": rj.params.k_e, "k_p": rj.params.k_p, "k_nu": rj.params.k_nu,
        "E_nu2_meV": E_nu2 * 1e9,
        "E_nu3_meV": E_nu3 * 1e9,
        "ratio": ratio if dm2_21 > 0 else float("nan"),
        "ae_ratio": ae/ALPHA, "ap_ratio": ap/ALPHA, "anu1_ratio": anu1/ALPHA,
    }
    print()
    return rj, metrics


# ── Main ───────────────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("R60 Track 6 — Joint e+p+ν solver")
    print("=" * 72)
    print(f"  Architecture: σ_ta = √α (signs +1/-1/+1 for e/p/ν), "
          f"σ_at = 4πα, g_aa = 1")
    print(f"  Sheet inputs: e=(ε=1, s=0), p=(ε=1, s=0), ν from R61")
    print(f"  Free knobs: L_e, k_e, L_p, k_p, L_ν, k_ν "
          f"(loose bounds 10⁻⁶ to 10⁶ on k)")
    print(f"  Targets: m_e, m_p, m_ν₁, α_e=α, α_p=α, α_ν=α")
    print()

    smoke()

    print("=" * 72)
    print("Phase 1 — try R61 candidate #1 at g_aa = 1")
    print("=" * 72)
    label, eps_nu, s_nu, triplet, m_nu1_meV = R61_CANDIDATES[0]
    rj1, m1 = solve_and_report(label, eps_nu, s_nu, triplet, m_nu1_meV)

    if m1 and m1["converged"]:
        print()
        print("=" * 72)
        print("Phase 1.5 — rescan against R61 candidates #2, #3, #4")
        print("=" * 72)
        for cand in R61_CANDIDATES[1:]:
            label, eps_nu, s_nu, triplet, m_nu1_meV = cand
            solve_and_report(label, eps_nu, s_nu, triplet, m_nu1_meV)
    else:
        print()
        print("Phase 1 did not cleanly converge.  Phase 2 (free g_aa) "
              "would be next.")
        print("Skipping Phase 2 in this initial run; results above show "
              "the failure mode.")

    print("=" * 72)
    print("Track 6 complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
