"""
R60 Track 2: Electron sheet viability map.

Characterize the electron sheet alone as a 2D parameter problem in
(ε_e, s_e).  Report:

  Region A — ghost-order favorable: μ(1,1) ≥ μ(1,2).  Closed form
             s_e ≥ 1.5 (independent of ε), confirmed numerically.
  Region B — signature preserved under R59 F59 α knobs
             (k_e = 1/(8π), σ_ta = √α on e-tube, g_aa = 1,
             σ_at = 4πα), with the ν and p sheets as uncoupled
             identity placeholders.
  Overlap  — the intersection.  If nonempty, Track 3 (ν-sheet)
             proceeds from one of these points.

No muon, no tau — those are compound modes that need ν and p
sheets (Tracks 3, 4).  Track 2 is pure electron sheet + α.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok, num_negative_eigs,
    mu_sheet, ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI,
)


# ── Metric builder for Track 2: e-sheet only, α knobs on ──────────────

def _e_only_params(eps_e: float, s_e: float,
                   alpha_on: bool = True) -> Params:
    """11D metric with e-sheet carrying all the structure.

    ν and p sheets are identity placeholders (ε=1, s=0, k=1) with
    no tube↔ℵ coupling (sign = 0).  They contribute nothing to
    e-sheet physics.

    When alpha_on=True, e-sheet runs at the R59 F59 α architecture:
    k_e = 1/(8π), σ_ta = √α on e-tube (sign_e = +1), g_aa = 1,
    σ_at = 4πα.
    """
    k_e   = 1.0 / EIGHT_PI if alpha_on else 1.0
    sigma_ta = SQRT_ALPHA if alpha_on else 0.0
    sigma_at = FOUR_PI * ALPHA if alpha_on else 0.0
    return Params(
        eps_e=eps_e, s_e=s_e,
        eps_p=1.0, s_p=0.0,
        eps_nu=1.0, s_nu=0.0,
        k_e=k_e, k_p=1.0, k_nu=1.0,
        g_aa=1.0,
        sigma_ta=sigma_ta,
        sigma_at=sigma_at,
        sign_e=+1.0, sign_p=0.0, sign_nu=0.0,  # p, ν uncoupled
        L_ring_e=1.0, L_ring_p=1.0, L_ring_nu=1.0,
    )


def signature_pass(eps_e: float, s_e: float) -> tuple[bool, int, float]:
    """Test signature under R59 F59 α knobs.  Returns (ok, n_neg, min_pos).

    min_pos is the smallest positive eigenvalue — the margin to the
    signature cliff.  Larger = more room.
    """
    p = _e_only_params(eps_e, s_e, alpha_on=True)
    G = build_metric_11(p)
    eigs = np.linalg.eigvalsh(G)
    n_neg = int(np.sum(eigs < 0))
    ok = n_neg == 1
    # the margin is the smallest positive eigenvalue (above zero)
    pos_eigs = eigs[eigs > 0]
    min_pos = float(pos_eigs.min()) if pos_eigs.size > 0 else 0.0
    return ok, n_neg, min_pos


def ghost_order_ok(eps_e: float, s_e: float) -> bool:
    """Ghost ordering: μ(1,1) ≥ μ(1,2).  Closed form: s ≥ 1.5."""
    mu11 = mu_sheet(1, 1, eps_e, s_e)
    mu12 = mu_sheet(1, 2, eps_e, s_e)
    return mu11 >= mu12


# ── Smoke cross-checks (match Track 1 T3) ──────────────────────────────

def smoke_checks():
    print("─" * 72)
    print("Smoke checks (pre-scan)")
    print("─" * 72)
    # At R53 Solution D, α off: ghost order should be OK
    ok = ghost_order_ok(397.074, 2.004200)
    mu12 = mu_sheet(1, 2, 397.074, 2.004200)
    mu11 = mu_sheet(1, 1, 397.074, 2.004200)
    print(f"  R53 Solution D (397.074, 2.004200):")
    print(f"    μ(1,2) = {mu12:.6f}, μ(1,1) = {mu11:.6f}, "
          f"ghost_order_ok = {ok}")

    # At R53 Solution D, α on: signature should fail (per Track 1 T3)
    sig_ok, n_neg, min_pos = signature_pass(397.074, 2.004200)
    print(f"    α-on signature: neg eigs = {n_neg}, ok = {sig_ok} "
          f"(expect False, reproduces T3)")

    # At clean shearless (ε=1, s=0), α on: signature should pass (R59 F59)
    sig_ok, n_neg, min_pos = signature_pass(1.0, 0.0)
    print(f"  Clean (1.0, 0.0):  neg eigs = {n_neg}, ok = {sig_ok} "
          f"(expect True, min_pos = {min_pos:.4f})")
    print()


# ── 2D scan ─────────────────────────────────────────────────────────────

def run_scan():
    """Scan (ε_e, s_e) and report Region A / B overlap."""
    # Log-spaced eps, linear s.  Range covers everything discussed in R53/R59.
    eps_values = np.logspace(np.log10(0.1), np.log10(1000.0), 61)
    s_values   = np.linspace(-3.0, 3.0, 121)

    # Grids
    ghost_grid = np.zeros((len(eps_values), len(s_values)), dtype=bool)
    sig_grid   = np.zeros((len(eps_values), len(s_values)), dtype=bool)
    margin_grid = np.zeros((len(eps_values), len(s_values)), dtype=float)

    for i, eps in enumerate(eps_values):
        for j, s in enumerate(s_values):
            ghost_grid[i, j] = ghost_order_ok(eps, s)
            sig_ok, _, min_pos = signature_pass(eps, s)
            sig_grid[i, j] = sig_ok
            margin_grid[i, j] = min_pos

    return eps_values, s_values, ghost_grid, sig_grid, margin_grid


# ── Region summaries ────────────────────────────────────────────────────

def summarize_regions(eps_values, s_values,
                      ghost_grid, sig_grid, margin_grid):
    n_eps = len(eps_values)
    n_s   = len(s_values)
    total = n_eps * n_s

    n_A = int(ghost_grid.sum())
    n_B = int(sig_grid.sum())
    overlap = ghost_grid & sig_grid
    n_AB = int(overlap.sum())

    print("─" * 72)
    print("Region summary")
    print("─" * 72)
    print(f"  Scan grid: {n_eps} ε values × {n_s} s values = {total} points")
    print(f"  Region A (ghost order OK, s ≥ 1.5):     {n_A} pts "
          f"({100*n_A/total:.1f}% of grid)")
    print(f"  Region B (signature OK under α knobs):  {n_B} pts "
          f"({100*n_B/total:.1f}% of grid)")
    print(f"  Overlap (A ∩ B):                        {n_AB} pts "
          f"({100*n_AB/total:.1f}% of grid)")
    print()

    # Characterize Region B: for each eps, find the range of s that passes
    print("  Region B (signature) by ε — range of s where signature OK:")
    print(f"    {'ε':>10s}  {'s range':>20s}  {'margin max':>12s}")
    for i in range(0, n_eps, 6):  # every 6th eps value
        eps = eps_values[i]
        s_pass = s_values[sig_grid[i]]
        if len(s_pass) == 0:
            print(f"    {eps:>10.3f}  {'(no s passes)':>20s}")
        else:
            s_lo, s_hi = s_pass.min(), s_pass.max()
            margin_max = margin_grid[i].max()
            print(f"    {eps:>10.3f}  [{s_lo:>+6.2f}, {s_hi:>+6.2f}]"
                  f"{'':>4s}  {margin_max:>12.4e}")
    print()

    return overlap, n_A, n_B, n_AB


def pick_candidates(eps_values, s_values, overlap, margin_grid,
                     n_picks: int = 5):
    """Pick representative overlap points with comfortable margin."""
    if not overlap.any():
        print("  Overlap is empty — no candidates.")
        return []

    print("─" * 72)
    print(f"Candidate points (overlap, sorted by signature margin)")
    print("─" * 72)

    # Collect all overlap points
    ii, jj = np.where(overlap)
    points = []
    for i, j in zip(ii, jj):
        points.append({
            "eps_e": float(eps_values[i]),
            "s_e":   float(s_values[j]),
            "margin": float(margin_grid[i, j]),
        })
    # Sort by margin descending (most comfortable first)
    points.sort(key=lambda p: -p["margin"])

    # Report top n_picks spread over the region
    # Naive spread: just take the top-margin points
    top = points[:n_picks]
    print(f"  {'ε_e':>10s}  {'s_e':>8s}  {'sig margin':>14s}  "
          f"{'ghost gap μ(1,1)/μ(1,2)':>24s}")
    for p in top:
        mu12 = mu_sheet(1, 2, p["eps_e"], p["s_e"])
        mu11 = mu_sheet(1, 1, p["eps_e"], p["s_e"])
        ratio = mu11 / mu12 if mu12 > 0 else float("inf")
        print(f"  {p['eps_e']:>10.4f}  {p['s_e']:>8.3f}  "
              f"{p['margin']:>14.4e}  {ratio:>24.4f}")
    print()
    return top


def refine_overlap_boundary():
    """Find the largest ε where s = 1.5 (the ghost-order edge) still
    preserves signature.  This is the sharp characterization of the
    overlap's upper-ε boundary."""
    print("─" * 72)
    print("Boundary refinement: largest ε where s = 1.5 passes signature")
    print("─" * 72)

    # s = 1.5 is the ghost-order edge.  Walk ε up and find where
    # signature fails.
    def sig_at(eps, s):
        return signature_pass(eps, s)[0]

    # Bisect in ε for a few s values just above the ghost-order edge
    for s_target in (1.5, 1.6, 1.7, 1.8, 2.0, 2.5, 3.0):
        lo, hi = 0.01, 10.0
        if not sig_at(lo, s_target):
            print(f"  s = {s_target}: signature fails even at ε = {lo}")
            continue
        if sig_at(hi, s_target):
            print(f"  s = {s_target}: signature OK all the way to ε = {hi}")
            continue
        for _ in range(40):
            mid = math.sqrt(lo * hi)  # geometric bisection (log ε)
            if sig_at(mid, s_target):
                lo = mid
            else:
                hi = mid
        print(f"  s = {s_target:.2f}: signature boundary at ε ≈ {lo:.4f}")
    print()

    # Also: for a fixed ε, find the largest s that passes signature
    print("  For fixed ε, largest s where signature passes:")
    for eps_target in (0.1, 0.3, 0.5, 1.0, 1.5, 2.0):
        # Bisect in s
        lo, hi = 0.0, 10.0
        if not sig_at(eps_target, lo):
            print(f"  ε = {eps_target}: signature fails at s = 0")
            continue
        if sig_at(eps_target, hi):
            print(f"  ε = {eps_target}: signature OK all the way to s = {hi}")
            continue
        for _ in range(40):
            mid = (lo + hi) / 2
            if sig_at(eps_target, mid):
                lo = mid
            else:
                hi = mid
        ghost_note = "ghost OK" if lo >= 1.5 else "ghost FAIL"
        print(f"  ε = {eps_target:.2f}: s_max ≈ {lo:.4f}  ({ghost_note})")
    print()


def scan_s_boundary_examples(eps_values, s_values, sig_grid):
    """For a few representative ε values, show the s boundary of signature."""
    print("─" * 72)
    print("Signature boundary in s for selected ε values")
    print("─" * 72)
    picks_eps = [0.1, 0.55, 1.0, 5.0, 100.0, 397.0]
    for eps_target in picks_eps:
        # find nearest eps index
        i = int(np.argmin(np.abs(eps_values - eps_target)))
        eps = eps_values[i]
        s_pass = s_values[sig_grid[i]]
        if len(s_pass) == 0:
            print(f"  ε ≈ {eps:.3f}: signature fails everywhere")
        else:
            s_lo, s_hi = s_pass.min(), s_pass.max()
            print(f"  ε ≈ {eps:.3f}: signature OK for s ∈ "
                  f"[{s_lo:+.3f}, {s_hi:+.3f}]")
    print()


# ── Main ────────────────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("R60 Track 2 — Electron sheet viability map")
    print("=" * 72)
    print(f"  α    = {ALPHA}")
    print(f"  √α   = {SQRT_ALPHA}")
    print(f"  1/(8π) = {1/EIGHT_PI}")
    print(f"  4πα  = {FOUR_PI*ALPHA}")
    print(f"  Architecture: k_e = 1/(8π), σ_ta = +√α on e-tube,")
    print(f"                g_aa = 1, σ_at = 4πα; ν, p uncoupled")
    print()

    smoke_checks()
    eps_values, s_values, ghost_grid, sig_grid, margin_grid = run_scan()
    overlap, n_A, n_B, n_AB = summarize_regions(
        eps_values, s_values, ghost_grid, sig_grid, margin_grid)
    scan_s_boundary_examples(eps_values, s_values, sig_grid)
    refine_overlap_boundary()
    pick_candidates(eps_values, s_values, overlap, margin_grid, n_picks=10)

    print("=" * 72)
    print("Track 2 scan complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
