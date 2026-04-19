"""
R60 Track 5 Part 1: Proton sheet viability with shearless electron.

Fix the electron sheet at (ε_e=1, s_e=0) — Track 4 Smoke 1
confirmed this is a clean reference point.  Vary (ε_p, s_p)
over a 2D grid and joint-solve for (L_e, k_e, L_p, k_p) against
(m_e, m_p, α_e=α, α_p=α) at each point.

Goal: characterize the viable proton region under shearless e
and report concrete candidate proton configurations for Track 6.
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
from track4_diagonal_compensation import (
    make_p_joint, solve_joint, K_NATURAL, n_e, n_p,
)


# ── Single-point solve helper ─────────────────────────────────────────

def solve_one(eps_p: float, s_p: float, eps_e=1.0, s_e=0.0):
    """Joint solve at fixed shearless e, varying p."""
    rj = solve_joint(eps_e, s_e, eps_p, s_p)
    G = build_metric_11(rj.params)
    sig = signature_ok(G)
    L = L_vector_from_params(rj.params)

    if sig:
        E_e = mode_energy(G, L, n_e())
        E_p = mode_energy(G, L, n_p())
        ae = alpha_coulomb(G, n_e())
        ap = alpha_coulomb(G, n_p())
    else:
        E_e = E_p = ae = ap = float("nan")

    converged = (
        rj.success and sig and rj.cost < 1e-6
        and abs(E_e - M_E_MEV) / M_E_MEV < 1e-6
        and abs(E_p - M_P_MEV) / M_P_MEV < 1e-6
        and abs(ae / ALPHA - 1) < 1e-3
        and abs(ap / ALPHA - 1) < 1e-3
    )
    return {
        "eps_p": eps_p, "s_p": s_p,
        "k_e": rj.params.k_e, "k_p": rj.params.k_p,
        "L_ring_p": rj.params.L_ring_p,
        "k_ratio": rj.params.k_e / rj.params.k_p if rj.params.k_p else float("nan"),
        "ae_ratio": ae / ALPHA, "ap_ratio": ap / ALPHA,
        "cost": rj.cost,
        "sig_ok": sig,
        "converged": converged,
    }


def smoke():
    print("─" * 72)
    print("Smoke check — reproduce Track 4 Smoke 1 at (1, 0, 1, 0)")
    print("─" * 72)
    r = solve_one(1.0, 0.0)
    print(f"  k_e = {r['k_e']:.6e} (R59 F59: {K_NATURAL:.6e})")
    print(f"  k_p = {r['k_p']:.6e} (R59 F59: {K_NATURAL:.6e})")
    print(f"  α_e/α = {r['ae_ratio']:.6f}, α_p/α = {r['ap_ratio']:.6f}")
    print(f"  converged = {r['converged']}, cost = {r['cost']:.2e}")
    print()


# ── 2D scan ────────────────────────────────────────────────────────────

def run_grid():
    print("=" * 72)
    print("Proton viability grid at (ε_e=1, s_e=0) shearless electron")
    print("=" * 72)
    eps_p_vals = np.logspace(np.log10(0.1), np.log10(3.0), 11)
    s_p_vals = np.linspace(0.0, 3.0, 13)

    results = []
    n_ok = 0
    print(f"  Grid: {len(eps_p_vals)} ε_p × {len(s_p_vals)} s_p = "
          f"{len(eps_p_vals)*len(s_p_vals)} points")
    print()
    print(f"  {'ε_p':>6s}  {'s_p':>5s}  {'s·ε':>5s}  "
          f"{'k_e':>10s}  {'k_p':>10s}  {'k_e/k_p':>8s}  "
          f"{'α_e/α':>8s}  {'α_p/α':>8s}  ok")
    for eps_p in eps_p_vals:
        for s_p in s_p_vals:
            r = solve_one(eps_p, s_p)
            results.append(r)
            if r["converged"]:
                n_ok += 1
            sε = s_p * eps_p
            tag = "YES" if r["converged"] else "no"
            print(f"  {eps_p:>6.3f}  {s_p:>5.2f}  {sε:>5.2f}  "
                  f"{r['k_e']:>10.3e}  {r['k_p']:>10.3e}  "
                  f"{r['k_ratio']:>8.3f}  "
                  f"{r['ae_ratio']:>8.4f}  {r['ap_ratio']:>8.4f}  {tag}")
    print()
    print(f"  Converged: {n_ok}/{len(results)} = {100*n_ok/len(results):.1f}%")
    return results


def report_candidates(results, n_picks: int = 5):
    print("─" * 72)
    print("Candidate proton configurations (converged, sorted by k-natural-ness)")
    print("─" * 72)
    ok = [r for r in results if r["converged"]]
    if not ok:
        print("  No converged points.")
        return

    # Sort by closeness of k_e and k_p to natural value (1/(8π))
    def naturalness(r):
        return (abs(r["k_e"] - K_NATURAL) / K_NATURAL +
                abs(r["k_p"] - K_NATURAL) / K_NATURAL)
    ok.sort(key=naturalness)

    print(f"  {'rank':>4s}  {'ε_p':>6s}  {'s_p':>5s}  {'s·ε':>5s}  "
          f"{'k_e':>9s}  {'k_p':>9s}  {'L_ring_p (fm)':>14s}  "
          f"{'k-nat'}")
    for i, r in enumerate(ok[:n_picks]):
        sε = r["s_p"] * r["eps_p"]
        nat = naturalness(r)
        print(f"  {i+1:>4d}  {r['eps_p']:>6.3f}  {r['s_p']:>5.2f}  "
              f"{sε:>5.2f}  {r['k_e']:>9.3e}  {r['k_p']:>9.3e}  "
              f"{r['L_ring_p']:>14.4e}  {nat:.4f}")
    print()


# ── Main ───────────────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("R60 Track 5 Part 1 — Proton viability at shearless electron")
    print("=" * 72)
    print(f"  Architecture: σ_ta = √α (sign_e=+1, sign_p=−1, sign_nu=0),")
    print(f"                σ_at = 4πα, g_aa = 1; ν uncoupled placeholder")
    print(f"  Fixed: (ε_e, s_e) = (1.0, 0.0) — Track 4 Smoke 1 reference")
    print()

    smoke()
    results = run_grid()
    report_candidates(results, n_picks=10)

    print("=" * 72)
    print("Track 5 Part 1 complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
