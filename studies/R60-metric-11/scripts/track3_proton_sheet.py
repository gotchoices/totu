"""
R60 Track 3: Proton sheet viability map.

Same idea as Track 2 but for the proton sheet.  Characterize the
(ε_p, s_p) range under which the R59 F59 α architecture remains
signature-OK with the proton sheet active alongside an
already-fixed electron sheet.

Free knobs: ε_p, s_p.  L_ring_p is derived from m_p.  ν-sheet is
identity placeholder.  α knobs at R59 F59 (k = 1/(8π), σ_ta = √α
with sign +1 for e-tube and −1 for p-tube, σ_at = 4πα, g_aa = 1).

Reports:
  Region C — p-sheet alone (no e-sheet active), signature OK
             under R59 F59 α.  Should match Track 2's Region B
             form by symmetry.
  Region D — joint e+p, several different e-sheet anchors.
             Identifies whether e-sheet choice meaningfully
             tightens the p-sheet viable range.
  Smoke    — model-E (ε_p=0.55, s_p=0.162); should be deep
             inside Region D.
  α univ   — α_p / α_e at representative points (R59 F45).
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok, num_negative_eigs,
    alpha_coulomb, mode_6_to_11, mu_sheet, derive_L_ring,
    L_vector_from_params, mode_energy,
    ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI, M_E_MEV, M_P_MEV,
)


# ── Metric builders ────────────────────────────────────────────────────

def _params_p_only(eps_p: float, s_p: float, alpha_on: bool = True) -> Params:
    """11D metric with p-sheet active; e and ν as identity placeholders."""
    k_p = 1.0 / EIGHT_PI if alpha_on else 1.0
    sigma_ta = SQRT_ALPHA if alpha_on else 0.0
    sigma_at = FOUR_PI * ALPHA if alpha_on else 0.0
    return Params(
        eps_e=1.0, s_e=0.0,
        eps_p=eps_p, s_p=s_p,
        eps_nu=1.0, s_nu=0.0,
        k_e=1.0, k_p=k_p, k_nu=1.0,
        g_aa=1.0,
        sigma_ta=sigma_ta,
        sigma_at=sigma_at,
        sign_e=0.0, sign_p=-1.0, sign_nu=0.0,  # only p coupled
        L_ring_e=1.0, L_ring_nu=1.0,
        L_ring_p=None,  # derived
    )


def _params_joint_ep(eps_e: float, s_e: float,
                      eps_p: float, s_p: float,
                      alpha_on: bool = True) -> Params:
    """Joint e+p: both sheets active at R59 F59 α; ν is placeholder."""
    k = 1.0 / EIGHT_PI if alpha_on else 1.0
    sigma_ta = SQRT_ALPHA if alpha_on else 0.0
    sigma_at = FOUR_PI * ALPHA if alpha_on else 0.0
    return Params(
        eps_e=eps_e, s_e=s_e,
        eps_p=eps_p, s_p=s_p,
        eps_nu=1.0, s_nu=0.0,
        k_e=k, k_p=k, k_nu=1.0,
        g_aa=1.0,
        sigma_ta=sigma_ta,
        sigma_at=sigma_at,
        sign_e=+1.0, sign_p=-1.0, sign_nu=0.0,
        L_ring_e=None, L_ring_nu=1.0, L_ring_p=None,  # both derived
    )


def _fill_L(p: Params, n_e=(1, 2), n_p=(1, 3)) -> Params:
    """Derive L_ring_e from m_e and L_ring_p from m_p (closed-form)."""
    updates = {}
    if p.L_ring_e is None:
        updates["L_ring_e"] = derive_L_ring(
            M_E_MEV, n_e[0], n_e[1], p.eps_e, p.s_e, p.k_e)
    if p.L_ring_p is None:
        updates["L_ring_p"] = derive_L_ring(
            M_P_MEV, n_p[0], n_p[1], p.eps_p, p.s_p, p.k_p)
    return p.copy_with(**updates) if updates else p


def signature_p_only(eps_p: float, s_p: float) -> tuple[bool, float]:
    """Signature check on the p-sheet-only configuration."""
    p = _params_p_only(eps_p, s_p, alpha_on=True)
    G = build_metric_11(p)
    eigs = np.linalg.eigvalsh(G)
    n_neg = int(np.sum(eigs < 0))
    pos_eigs = eigs[eigs > 0]
    margin = float(pos_eigs.min()) if pos_eigs.size > 0 else 0.0
    return n_neg == 1, margin


def signature_joint(eps_e: float, s_e: float,
                     eps_p: float, s_p: float) -> tuple[bool, float]:
    """Signature check on the joint e+p configuration."""
    p = _params_joint_ep(eps_e, s_e, eps_p, s_p, alpha_on=True)
    G = build_metric_11(p)
    eigs = np.linalg.eigvalsh(G)
    n_neg = int(np.sum(eigs < 0))
    pos_eigs = eigs[eigs > 0]
    margin = float(pos_eigs.min()) if pos_eigs.size > 0 else 0.0
    return n_neg == 1, margin


# ── Smoke checks ───────────────────────────────────────────────────────

def smoke_checks():
    print("─" * 72)
    print("Smoke checks")
    print("─" * 72)

    # 1. Model-E proton at p-sheet alone
    eps_p_E, s_p_E = 0.55, 0.162037
    sig, margin = signature_p_only(eps_p_E, s_p_E)
    print(f"  Model-E p-sheet only ({eps_p_E}, {s_p_E}):")
    print(f"    s·ε = {s_p_E * eps_p_E:.4f}  "
          f"(Track 2 boundary 3/√2 ≈ 2.121)")
    print(f"    signature OK = {sig}, margin = {margin:.4e}")

    # 2. Joint e+p at Track 2 corner + model-E proton
    sig, margin = signature_joint(1.0, 1.5, eps_p_E, s_p_E)
    print(f"  Joint (ε_e=1, s_e=1.5) + (ε_p={eps_p_E}, s_p={s_p_E}):")
    print(f"    signature OK = {sig}, margin = {margin:.4e}")

    # 3. Universality: α_p / α_e at the joint point
    p = _fill_L(_params_joint_ep(1.0, 1.5, eps_p_E, s_p_E))
    G = build_metric_11(p)
    if signature_ok(G):
        ae = alpha_coulomb(G, mode_6_to_11((1, 2, 0, 0, 0, 0)))
        ap = alpha_coulomb(G, mode_6_to_11((0, 0, 0, 0, 1, 3)))
        print(f"    α_e = {ae:.6e}  ({ae/ALPHA:.6f}×α)")
        print(f"    α_p = {ap:.6e}  ({ap/ALPHA:.6f}×α)")
        print(f"    α_p / α_e = {ap/ae:.8f}  (R59 F45: structural = 1.0)")

        # Verify masses come out at target after L_ring derivation
        L = L_vector_from_params(p)
        E_e = mode_energy(G, L, mode_6_to_11((1, 2, 0, 0, 0, 0)))
        E_p = mode_energy(G, L, mode_6_to_11((0, 0, 0, 0, 1, 3)))
        print(f"    E(electron) = {E_e:.10f} MeV  (target {M_E_MEV})")
        print(f"    E(proton)   = {E_p:.6f} MeV  (target {M_P_MEV})")
    print()


# ── 2D scans ──────────────────────────────────────────────────────────

def run_scan_p_only():
    eps_values = np.logspace(np.log10(0.1), np.log10(1000.0), 61)
    s_values = np.linspace(-3.0, 3.0, 121)
    sig_grid = np.zeros((len(eps_values), len(s_values)), dtype=bool)
    margin_grid = np.zeros((len(eps_values), len(s_values)), dtype=float)
    for i, eps in enumerate(eps_values):
        for j, s in enumerate(s_values):
            ok, m = signature_p_only(eps, s)
            sig_grid[i, j] = ok
            margin_grid[i, j] = m
    return eps_values, s_values, sig_grid, margin_grid


def run_scan_joint(eps_e: float, s_e: float):
    eps_values = np.logspace(np.log10(0.1), np.log10(1000.0), 61)
    s_values = np.linspace(-3.0, 3.0, 121)
    sig_grid = np.zeros((len(eps_values), len(s_values)), dtype=bool)
    margin_grid = np.zeros((len(eps_values), len(s_values)), dtype=float)
    for i, eps in enumerate(eps_values):
        for j, s in enumerate(s_values):
            ok, m = signature_joint(eps_e, s_e, eps, s)
            sig_grid[i, j] = ok
            margin_grid[i, j] = m
    return eps_values, s_values, sig_grid, margin_grid


# ── Boundary refinement ───────────────────────────────────────────────

def refine_boundary_joint(eps_e: float, s_e: float):
    """Bisect to find the s_p · ε_p boundary at the joint e+p config."""
    print(f"  Boundary refinement at e-sheet ({eps_e}, {s_e}):")
    print(f"    {'s_p':>6s}  {'ε_p_max':>10s}  {'s_p · ε_p':>10s}")

    def sig_at(eps_p, s_p):
        return signature_joint(eps_e, s_e, eps_p, s_p)[0]

    products = []
    for s_target in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
        lo, hi = 1e-3, 100.0
        if not sig_at(lo, s_target):
            print(f"    {s_target:>6.2f}  (signature fails at ε=0)")
            continue
        if sig_at(hi, s_target):
            print(f"    {s_target:>6.2f}  (signature OK to ε={hi})")
            continue
        for _ in range(40):
            mid = math.sqrt(lo * hi)
            if sig_at(mid, s_target):
                lo = mid
            else:
                hi = mid
        prod = lo * s_target
        products.append(prod)
        print(f"    {s_target:>6.2f}  {lo:>10.4f}  {prod:>10.4f}")
    return products


# ── Region summary ────────────────────────────────────────────────────

def summarize_region(label, eps_values, s_values, sig_grid):
    n_total = sig_grid.size
    n_pass = int(sig_grid.sum())
    print(f"  {label}: {n_pass} / {n_total} pts ({100*n_pass/n_total:.1f}%)")


def report_e_anchor_comparison(anchors):
    """Run joint scans for several e-anchors and compare."""
    print("=" * 72)
    print("Region D — joint e+p signature, multiple e-sheet anchors")
    print("=" * 72)

    results = []
    for label, (eps_e, s_e) in anchors.items():
        print(f"\n─── e-anchor: {label} (ε_e={eps_e}, s_e={s_e}) " + "─" * 12)
        eps_values, s_values, sig_grid, margin_grid = run_scan_joint(
            eps_e, s_e)
        n_pass = int(sig_grid.sum())
        n_total = sig_grid.size
        print(f"  Region D ({label}): {n_pass}/{n_total} pts "
              f"({100*n_pass/n_total:.1f}%)")
        # Boundary refinement
        products = refine_boundary_joint(eps_e, s_e)
        if products:
            print(f"  → s·ε boundary mean: {np.mean(products):.4f}, "
                  f"std: {np.std(products):.4f}")
        # Test model-E proton inclusion
        sig_E, margin_E = signature_joint(eps_e, s_e, 0.55, 0.162037)
        print(f"  Model-E proton (0.55, 0.162) included? {sig_E} "
              f"(margin {margin_E:.4e})")
        results.append({
            "label": label,
            "eps_e": eps_e, "s_e": s_e,
            "n_pass": n_pass, "n_total": n_total,
            "products": products,
            "sig_E": sig_E,
            "margin_E": margin_E,
        })
    return results


def report_universality_at_candidates(anchors, candidate_points):
    """Compute α_p / α_e for each (e-anchor, p-candidate) combo."""
    print("\n" + "=" * 72)
    print("α_Coulomb universality on the joint e+p metric (R59 F45 check)")
    print("=" * 72)
    for label_e, (eps_e, s_e) in anchors.items():
        print(f"\n  e-anchor: {label_e} (ε_e={eps_e}, s_e={s_e})")
        print(f"  {'(ε_p, s_p)':>20s}  {'α_e/α':>12s}  {'α_p/α':>12s}  "
              f"{'α_p/α_e':>12s}")
        for label_p, (eps_p, s_p) in candidate_points.items():
            p = _fill_L(_params_joint_ep(eps_e, s_e, eps_p, s_p))
            G = build_metric_11(p)
            if not signature_ok(G):
                print(f"  {label_p:>20s}  (signature failed)")
                continue
            ae = alpha_coulomb(G, mode_6_to_11((1, 2, 0, 0, 0, 0)))
            ap = alpha_coulomb(G, mode_6_to_11((0, 0, 0, 0, 1, 3)))
            ratio_pe = ap / ae if ae != 0 else float("nan")
            print(f"  {label_p:>20s}  {ae/ALPHA:>12.6f}  "
                  f"{ap/ALPHA:>12.6f}  {ratio_pe:>12.8f}")


# ── Main ──────────────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("R60 Track 3 — Proton sheet viability map")
    print("=" * 72)
    print(f"  Architecture: k = 1/(8π), σ_ta = √α (sign_e=+1, sign_p=−1),")
    print(f"                g_aa = 1, σ_at = 4πα; ν uncoupled placeholder")
    print()

    smoke_checks()

    # Region C — p-sheet alone
    print("=" * 72)
    print("Region C — p-sheet alone (no e-sheet)")
    print("=" * 72)
    eps_values, s_values, sig_C, margin_C = run_scan_p_only()
    summarize_region("Region C", eps_values, s_values, sig_C)
    print()
    print("  Boundary refinement (p-sheet alone):")
    print(f"    {'s_p':>6s}  {'ε_p_max':>10s}  {'s_p · ε_p':>10s}")
    products_C = []
    for s_target in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
        lo, hi = 1e-3, 100.0
        if not signature_p_only(lo, s_target)[0]:
            print(f"    {s_target:>6.2f}  (signature fails at ε=0)")
            continue
        if signature_p_only(hi, s_target)[0]:
            print(f"    {s_target:>6.2f}  (signature OK to ε={hi})")
            continue
        for _ in range(40):
            mid = math.sqrt(lo * hi)
            if signature_p_only(mid, s_target)[0]:
                lo = mid
            else:
                hi = mid
        prod = lo * s_target
        products_C.append(prod)
        print(f"    {s_target:>6.2f}  {lo:>10.4f}  {prod:>10.4f}")
    if products_C:
        print(f"  → s·ε boundary mean: {np.mean(products_C):.4f}")
    print()

    # Region D — joint e+p across multiple e-anchors
    e_anchors = {
        "corner-1.0":   (1.0, 1.5),
        "corner-edge":  (1.4, 1.5),
        "high-margin":  (0.1, 1.5),
        "mid-shear":    (0.5, 2.0),
    }
    results = report_e_anchor_comparison(e_anchors)

    # Universality check on a panel of (e-anchor, p-candidate) combos
    p_candidates = {
        "model-E (0.55, 0.162)":   (0.55, 0.162037),
        "p-corner (1.0, 1.5)":     (1.0, 1.5),
        "low-margin (1.0, 2.0)":   (1.0, 2.0),
        "high-margin (0.1, 0.1)":  (0.1, 0.1),
    }
    report_universality_at_candidates(e_anchors, p_candidates)

    # Final summary
    print("\n" + "=" * 72)
    print("Track 3 summary")
    print("=" * 72)
    print(f"  Region C ({(100*sig_C.sum()/sig_C.size):.1f}% of grid)")
    for r in results:
        print(f"  Region D, {r['label']}: "
              f"{r['n_pass']}/{r['n_total']} pts "
              f"({100*r['n_pass']/r['n_total']:.1f}%); "
              f"model-E proton included = {r['sig_E']}")
    print()
    print("Track 3 complete.")


if __name__ == "__main__":
    main()
