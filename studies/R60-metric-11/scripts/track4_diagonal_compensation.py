"""
R60 Track 4: Per-sheet diagonal compensation for α universality.

Tests whether allowing k_e ≠ k_p (instead of R59 F59's identical
assumption) recovers both α universality (α_e = α_p = α) and α
magnitude on a metric with internal shears active.

Free knobs:   (L_ring_e, k_e, L_ring_p, k_p)
Targets:      E(electron) = m_e
              E(proton)   = m_p
              α_Coulomb(electron) = α
              α_Coulomb(proton)   = α

Two modes:
  per-sheet — each sheet's α coupling solved independently with
              the other sheet's tube↔ℵ entry zeroed (sign = 0).
              Says what each sheet "wants" in isolation.
  joint     — both sheets active with signs +/-.  The "right"
              answer because α extraction on each sheet depends
              on the other via shared ℵ.
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

K_NATURAL = 1.0 / EIGHT_PI


# ── Mode shorthands ─────────────────────────────────────────────────────

def n_e():   return mode_6_to_11((1, 2, 0, 0, 0, 0))
def n_p():   return mode_6_to_11((0, 0, 0, 0, 1, 3))


# ── Builders ───────────────────────────────────────────────────────────

def make_p_e_only(eps_e, s_e, k_e, L_ring_e):
    """e-sheet active in isolation (sign_p = sign_nu = 0)."""
    return Params(
        eps_e=eps_e, s_e=s_e,
        eps_p=1.0, s_p=0.0,
        eps_nu=1.0, s_nu=0.0,
        k_e=k_e, k_p=1.0, k_nu=1.0,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=+1.0, sign_p=0.0, sign_nu=0.0,
        L_ring_e=L_ring_e, L_ring_p=1.0, L_ring_nu=1.0,
    )


def make_p_p_only(eps_p, s_p, k_p, L_ring_p):
    """p-sheet active in isolation (sign_e = sign_nu = 0)."""
    return Params(
        eps_e=1.0, s_e=0.0,
        eps_p=eps_p, s_p=s_p,
        eps_nu=1.0, s_nu=0.0,
        k_e=1.0, k_p=k_p, k_nu=1.0,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=0.0, sign_p=-1.0, sign_nu=0.0,
        L_ring_e=1.0, L_ring_p=L_ring_p, L_ring_nu=1.0,
    )


def make_p_joint(eps_e, s_e, k_e, L_ring_e,
                  eps_p, s_p, k_p, L_ring_p):
    """Joint e+p with both signs on."""
    return Params(
        eps_e=eps_e, s_e=s_e,
        eps_p=eps_p, s_p=s_p,
        eps_nu=1.0, s_nu=0.0,
        k_e=k_e, k_p=k_p, k_nu=1.0,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=0.0,
        L_ring_e=L_ring_e, L_ring_p=L_ring_p, L_ring_nu=1.0,
    )


# ── Per-sheet solvers (2x2) ────────────────────────────────────────────

def solve_e_only(eps_e, s_e, k_init=None, L_init=None):
    """Find (L_ring_e, k_e) hitting (m_e, α_e=α) on the e-sheet alone."""
    if k_init is None:
        k_init = K_NATURAL
    if L_init is None:
        L_init = derive_L_ring(M_E_MEV, 1, 2, eps_e, s_e, k_init)
    p0 = make_p_e_only(eps_e, s_e, k_init, L_init)

    def res_mass(p):
        G = build_metric_11(p)
        L = L_vector_from_params(p)
        if not signature_ok(G):
            return 100.0
        E = mode_energy(G, L, n_e())
        return (E - M_E_MEV) / M_E_MEV

    def res_alpha(p):
        G = build_metric_11(p)
        if not signature_ok(G):
            return 100.0
        ae = alpha_coulomb(G, n_e())
        return (ae - ALPHA) / ALPHA

    targets = [Target("m_e", res_mass), Target("α_e", res_alpha)]
    result = solve(
        p0, free=["L_ring_e", "k_e"], targets=targets,
        bounds={"L_ring_e": (1e-3, 1e9), "k_e": (1e-6, 1e3)},
        xtol=1e-12, ftol=1e-12,
    )
    return result


def solve_p_only(eps_p, s_p, k_init=None, L_init=None):
    """Find (L_ring_p, k_p) hitting (m_p, α_p=α) on the p-sheet alone."""
    if k_init is None:
        k_init = K_NATURAL
    if L_init is None:
        L_init = derive_L_ring(M_P_MEV, 1, 3, eps_p, s_p, k_init)
    p0 = make_p_p_only(eps_p, s_p, k_init, L_init)

    def res_mass(p):
        G = build_metric_11(p)
        L = L_vector_from_params(p)
        if not signature_ok(G):
            return 100.0
        E = mode_energy(G, L, n_p())
        return (E - M_P_MEV) / M_P_MEV

    def res_alpha(p):
        G = build_metric_11(p)
        if not signature_ok(G):
            return 100.0
        ap = alpha_coulomb(G, n_p())
        return (ap - ALPHA) / ALPHA

    targets = [Target("m_p", res_mass), Target("α_p", res_alpha)]
    result = solve(
        p0, free=["L_ring_p", "k_p"], targets=targets,
        bounds={"L_ring_p": (1e-3, 1e9), "k_p": (1e-6, 1e3)},
        xtol=1e-12, ftol=1e-12,
    )
    return result


# ── Joint solver (4x4) ─────────────────────────────────────────────────

def solve_joint(eps_e, s_e, eps_p, s_p,
                 k_e_init=None, k_p_init=None,
                 L_e_init=None, L_p_init=None):
    """Find (L_e, k_e, L_p, k_p) hitting all four targets jointly."""
    if k_e_init is None: k_e_init = K_NATURAL
    if k_p_init is None: k_p_init = K_NATURAL
    if L_e_init is None: L_e_init = derive_L_ring(M_E_MEV, 1, 2, eps_e, s_e, k_e_init)
    if L_p_init is None: L_p_init = derive_L_ring(M_P_MEV, 1, 3, eps_p, s_p, k_p_init)

    p0 = make_p_joint(eps_e, s_e, k_e_init, L_e_init,
                      eps_p, s_p, k_p_init, L_p_init)

    def res_me(p):
        G = build_metric_11(p)
        L = L_vector_from_params(p)
        if not signature_ok(G):
            return 100.0
        return (mode_energy(G, L, n_e()) - M_E_MEV) / M_E_MEV

    def res_mp(p):
        G = build_metric_11(p)
        L = L_vector_from_params(p)
        if not signature_ok(G):
            return 100.0
        return (mode_energy(G, L, n_p()) - M_P_MEV) / M_P_MEV

    def res_ae(p):
        G = build_metric_11(p)
        if not signature_ok(G):
            return 100.0
        return (alpha_coulomb(G, n_e()) - ALPHA) / ALPHA

    def res_ap(p):
        G = build_metric_11(p)
        if not signature_ok(G):
            return 100.0
        return (alpha_coulomb(G, n_p()) - ALPHA) / ALPHA

    targets = [Target("m_e", res_me), Target("m_p", res_mp),
               Target("α_e", res_ae), Target("α_p", res_ap)]
    result = solve(
        p0,
        free=["L_ring_e", "k_e", "L_ring_p", "k_p"],
        targets=targets,
        bounds={
            "L_ring_e": (1e-3, 1e9),
            "k_e":      (1e-6, 1e3),
            "L_ring_p": (1e-3, 1e9),
            "k_p":      (1e-6, 1e3),
        },
        xtol=1e-12, ftol=1e-12,
    )
    return result


# ── Reporting ──────────────────────────────────────────────────────────

def report_per_sheet(label, eps_e, s_e, eps_p, s_p):
    print("─" * 72)
    print(f"Per-sheet solves: {label}")
    print(f"  e: ε={eps_e}, s={s_e};  p: ε={eps_p}, s={s_p}")
    print("─" * 72)

    re = solve_e_only(eps_e, s_e)
    print(f"  e-sheet alone:")
    print(f"    converged   = {re.success}  ({re.message[:50]})")
    print(f"    L_ring_e    = {re.params.L_ring_e:.6e}")
    print(f"    k_e         = {re.params.k_e:.6e}  "
          f"(R59 F59: {K_NATURAL:.6e})")
    print(f"    residuals   = {re.residuals}")
    G = build_metric_11(re.params)
    if signature_ok(G):
        L = L_vector_from_params(re.params)
        print(f"    E_e         = {mode_energy(G, L, n_e()):.10f} "
              f"(target {M_E_MEV})")
        print(f"    α_e/α       = {alpha_coulomb(G, n_e())/ALPHA:.6f}")

    rp = solve_p_only(eps_p, s_p)
    print(f"  p-sheet alone:")
    print(f"    converged   = {rp.success}  ({rp.message[:50]})")
    print(f"    L_ring_p    = {rp.params.L_ring_p:.6e}")
    print(f"    k_p         = {rp.params.k_p:.6e}  "
          f"(R59 F59: {K_NATURAL:.6e})")
    print(f"    residuals   = {rp.residuals}")
    G = build_metric_11(rp.params)
    if signature_ok(G):
        L = L_vector_from_params(rp.params)
        print(f"    E_p         = {mode_energy(G, L, n_p()):.6f} "
              f"(target {M_P_MEV})")
        print(f"    α_p/α       = {alpha_coulomb(G, n_p())/ALPHA:.6f}")
    print()
    return re, rp


def report_joint(label, eps_e, s_e, eps_p, s_p,
                  re_init=None, rp_init=None):
    print("─" * 72)
    print(f"Joint solve: {label}")
    print(f"  e: ε={eps_e}, s={s_e};  p: ε={eps_p}, s={s_p}")
    print("─" * 72)

    # Use per-sheet results as warm start if available
    k_e_init = re_init.params.k_e if re_init else None
    k_p_init = rp_init.params.k_p if rp_init else None
    L_e_init = re_init.params.L_ring_e if re_init else None
    L_p_init = rp_init.params.L_ring_p if rp_init else None

    rj = solve_joint(eps_e, s_e, eps_p, s_p,
                      k_e_init, k_p_init, L_e_init, L_p_init)
    print(f"  converged   = {rj.success}  ({rj.message[:60]})")
    print(f"  cost (½‖r‖²)= {rj.cost:.4e}")
    print(f"  L_ring_e    = {rj.params.L_ring_e:.6e}")
    print(f"  k_e         = {rj.params.k_e:.6e}  "
          f"(R59 F59: {K_NATURAL:.6e}, ratio {rj.params.k_e/K_NATURAL:.4f})")
    print(f"  L_ring_p    = {rj.params.L_ring_p:.6e}")
    print(f"  k_p         = {rj.params.k_p:.6e}  "
          f"(R59 F59: {K_NATURAL:.6e}, ratio {rj.params.k_p/K_NATURAL:.4f})")
    print(f"  k_e / k_p   = {rj.params.k_e/rj.params.k_p:.4f}  "
          f"(R59 F59: 1.0)")
    print(f"  residuals   = {rj.residuals}")

    G = build_metric_11(rj.params)
    sig = signature_ok(G)
    print(f"  signature_ok = {sig}")
    if sig:
        L = L_vector_from_params(rj.params)
        E_e = mode_energy(G, L, n_e())
        E_p = mode_energy(G, L, n_p())
        ae = alpha_coulomb(G, n_e())
        ap = alpha_coulomb(G, n_p())
        print(f"  E_e         = {E_e:.10f}  (target {M_E_MEV}, "
              f"rel = {(E_e-M_E_MEV)/M_E_MEV:+.2e})")
        print(f"  E_p         = {E_p:.6f}  (target {M_P_MEV}, "
              f"rel = {(E_p-M_P_MEV)/M_P_MEV:+.2e})")
        print(f"  α_e/α       = {ae/ALPHA:.6f}")
        print(f"  α_p/α       = {ap/ALPHA:.6f}")
        print(f"  α_p/α_e     = {ap/ae if ae != 0 else float('nan'):.8f}")
    print()
    return rj


# ── (ε, s) → (k_e, k_p) map ────────────────────────────────────────────

def map_k_grid():
    print("=" * 72)
    print("(ε, s) → (k_e, k_p) map (joint solve at each grid point)")
    print("=" * 72)
    eps_e_vals = [0.1, 0.5, 1.0]
    s_e_vals   = [1.5, 2.0, 2.5]
    eps_p_vals = [0.1, 0.55, 1.0]
    s_p_vals   = [0.1, 0.5, 1.0]

    results = []
    print(f"  {'ε_e':>5s}  {'s_e':>5s}  {'ε_p':>5s}  {'s_p':>5s}  "
          f"{'k_e':>10s}  {'k_p':>10s}  {'k_e/k_p':>9s}  "
          f"{'cost':>9s}  ok")
    for eps_e in eps_e_vals:
        for s_e in s_e_vals:
            for eps_p in eps_p_vals:
                for s_p in s_p_vals:
                    rj = solve_joint(eps_e, s_e, eps_p, s_p)
                    G = build_metric_11(rj.params)
                    sig = signature_ok(G)
                    converged_ok = rj.success and sig and rj.cost < 1e-6
                    results.append({
                        "eps_e": eps_e, "s_e": s_e,
                        "eps_p": eps_p, "s_p": s_p,
                        "k_e": rj.params.k_e, "k_p": rj.params.k_p,
                        "cost": rj.cost, "ok": converged_ok,
                    })
                    print(f"  {eps_e:>5.2f}  {s_e:>5.2f}  "
                          f"{eps_p:>5.2f}  {s_p:>5.2f}  "
                          f"{rj.params.k_e:>10.4e}  "
                          f"{rj.params.k_p:>10.4e}  "
                          f"{rj.params.k_e/rj.params.k_p:>9.4f}  "
                          f"{rj.cost:>9.2e}  "
                          f"{'YES' if converged_ok else 'no'}")
    return results


def analyze_k_patterns(results):
    print()
    print("=" * 72)
    print("Pattern analysis: does k_x scale predictably with (ε_x, s_x)?")
    print("=" * 72)
    ok = [r for r in results if r["ok"]]
    print(f"  {len(ok)} of {len(results)} grid points converged cleanly")
    if not ok:
        print("  (no converged points to analyze)")
        return

    # Check if k_e depends only on (ε_e, s_e), not on (ε_p, s_p)
    print()
    print("  Does k_e depend only on (ε_e, s_e)?")
    print(f"    {'(ε_e, s_e)':>12s}  {'k_e values':>30s}  spread")
    e_groups = {}
    for r in ok:
        key = (r["eps_e"], r["s_e"])
        e_groups.setdefault(key, []).append(r["k_e"])
    for key, vals in sorted(e_groups.items()):
        if len(vals) > 1:
            spread = (max(vals) - min(vals)) / np.mean(vals)
            sample = ", ".join(f"{v:.3e}" for v in vals[:3])
            print(f"    {str(key):>12s}  {sample:>30s}  {spread:.2%}")

    print()
    print("  Does k_p depend only on (ε_p, s_p)?")
    print(f"    {'(ε_p, s_p)':>12s}  {'k_p values':>30s}  spread")
    p_groups = {}
    for r in ok:
        key = (r["eps_p"], r["s_p"])
        p_groups.setdefault(key, []).append(r["k_p"])
    for key, vals in sorted(p_groups.items()):
        if len(vals) > 1:
            spread = (max(vals) - min(vals)) / np.mean(vals)
            sample = ", ".join(f"{v:.3e}" for v in vals[:3])
            print(f"    {str(key):>12s}  {sample:>30s}  {spread:.2%}")


# ── Main ───────────────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("R60 Track 4 — Per-sheet diagonal compensation for α universality")
    print("=" * 72)
    print(f"  R59 F59 reference: k = 1/(8π) = {K_NATURAL:.6e}")
    print(f"  Architecture: σ_ta = √α (signs +/-/0), σ_at = 4πα, g_aa = 1")
    print()

    # Smoke 1 — clean (no shear)
    print("=" * 72)
    print("Smoke 1: shearless clean reference (should recover R59 F59)")
    print("=" * 72)
    re, rp = report_per_sheet("clean", 1.0, 0.0, 1.0, 0.0)
    rj = report_joint("clean", 1.0, 0.0, 1.0, 0.0, re, rp)

    # Smoke 2 — Track 3 best (already 1.05 universality)
    print("=" * 72)
    print("Smoke 2: Track 3 best — (0.1, 1.5) e + (0.55, 0.162) p")
    print("=" * 72)
    re, rp = report_per_sheet("T3 best", 0.1, 1.5, 0.55, 0.162037)
    rj = report_joint("T3 best", 0.1, 1.5, 0.55, 0.162037, re, rp)

    # Stress — Track 3 worst (8.78 ratio)
    print("=" * 72)
    print("Stress: Track 3 worst — (1.0, 1.5) e + (0.55, 0.162) p")
    print("=" * 72)
    re, rp = report_per_sheet("T3 worst", 1.0, 1.5, 0.55, 0.162037)
    rj = report_joint("T3 worst", 1.0, 1.5, 0.55, 0.162037, re, rp)

    # Pathology — Track 3 zero-α point
    print("=" * 72)
    print("Pathology: Track 3 α≈0 — (0.5, 2.0) e + (0.55, 0.162) p")
    print("=" * 72)
    re, rp = report_per_sheet("T3 zero", 0.5, 2.0, 0.55, 0.162037)
    rj = report_joint("T3 zero", 0.5, 2.0, 0.55, 0.162037, re, rp)

    # k-grid map
    print()
    results = map_k_grid()
    analyze_k_patterns(results)

    print()
    print("=" * 72)
    print("Track 4 complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
