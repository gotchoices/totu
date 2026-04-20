"""
R60 — common code for the Losinets Hofstadter projection.

Builds the model-E MaD geometry with cross-shears σ₄₅ = −0.18,
σ₄₆ = +0.10 (0-indexed keys (3, 4) and (3, 5)) and exposes:

  * metric build (copied from R54 track1c — the canonical metric
    construction for the compound proton/neutron modes).
  * 6D density variants M-A (standing wave |ψ|²),
    M-B (gradient / kinetic density), M-C (charge-weighted by
    Ma-S coupling sign).
  * Four projections P-1..P-4 from T⁶ to 3D radial ρ(r).
  * A scale-detection routine that classifies 1/2/>2-scale profiles
    and reports (r_inner, r_outer, ratio).

The four projections are not unique canonical maps — the methodology
is to try all and report (see the ticket).
"""

import os
import sys
import math
from itertools import product as iproduct

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model_d import (
    M_E_MEV, M_P_MEV, DM2_21,
    _TWO_PI_HC, solve_shear_for_alpha,
)

# ── Model-E geometry (R53 Solution D + R54 compound-mode tuning) ──
EPS_E, S_E = 397.074, 2.004200
EPS_P = 0.55
S_P = solve_shear_for_alpha(EPS_P, n_tube=1, n_ring=3)
EPS_NU, S_NU = 5.0, 0.022

M_PROTON = 938.272
M_NEUTRON = 939.565

# Neutron-neighborhood cross-shears from R54 track1c (model-E inventory)
SIGMA_CROSS = {(3, 4): -0.18, (3, 5): +0.10}

# Proton and neutron compound modes (from model-E.md)
PROTON_MODE = (0, 0, -2, 2, 1, 3)
NEUTRON_MODE = (0, -4, -1, 2, 0, -3)

# Ma-S coupling sign per sheet (e, ν, p): −, 0, +
MaS_SIGN = {'e': -1.0, 'nu': 0.0, 'p': +1.0}

# Hofstadter targets
R_CORE_TARGET = 0.25   # fm
R_MANTLE_TARGET = 1.3  # fm
RATIO_TARGET = 5.2
RATIO_WINDOW = (4.0, 6.4)


# ════════════════════════════════════════════════════════════════
#  Metric construction (from R54 track1c)
# ════════════════════════════════════════════════════════════════

def build_metric(L, s_e, s_nu, s_p, sigma=None):
    """6×6 dimensionless metric G̃ with individual cross entries."""
    if sigma is None:
        sigma = {}
    S = np.zeros((6, 6))
    S[0, 1] = s_e; S[2, 3] = s_nu; S[4, 5] = s_p
    B = np.diag(L) @ (np.eye(6) + S)
    Gt = B.T @ B
    for i in range(6):
        for j in range(6):
            Gt[i, j] /= (L[i] * L[j])
    for (i, j), val in sigma.items():
        Gt[i, j] += val; Gt[j, i] += val
    eigs = np.linalg.eigvalsh(Gt)
    if np.any(eigs <= 0):
        return None, None
    return Gt, np.linalg.inv(Gt)


def build_circumferences():
    """Return L = [L₁, …, L₆] in fm for the model-E geometry."""
    mu_e = math.sqrt((1 / EPS_E) ** 2 + (2 - S_E) ** 2)
    L_ring_e = _TWO_PI_HC * mu_e / M_E_MEV
    mu_p = math.sqrt((1 / EPS_P) ** 2 + (3 - S_P) ** 2)
    L_ring_p = _TWO_PI_HC * mu_p / M_P_MEV
    E0_nu = math.sqrt(DM2_21 / (4 * S_NU)) * 1e-6
    L_ring_nu = _TWO_PI_HC / E0_nu
    L = np.array([EPS_E * L_ring_e, L_ring_e,
                  EPS_NU * L_ring_nu, L_ring_nu,
                  EPS_P * L_ring_p, L_ring_p])
    return L, (L_ring_e, L_ring_nu, L_ring_p)


def mode_energy(n, L, Gti):
    n_arr = np.asarray(n, dtype=float)
    nt = n_arr / L
    E2 = _TWO_PI_HC ** 2 * nt @ Gti @ nt
    return math.sqrt(max(E2, 0))


# ════════════════════════════════════════════════════════════════
#  Sheet metadata
# ════════════════════════════════════════════════════════════════

SHEETS = [
    # (label, tube_idx, ring_idx, MaS sign)
    ('e',  0, 1, MaS_SIGN['e']),
    ('nu', 2, 3, MaS_SIGN['nu']),
    ('p',  4, 5, MaS_SIGN['p']),
]


def active_directions(n):
    """Return list of (i, n_i) for each compact direction with nonzero winding."""
    return [(i, int(n[i])) for i in range(6) if n[i] != 0]


def sheet_of(i):
    """Which sheet (label, sign) does coordinate i live on?"""
    for label, it, ir, sign in SHEETS:
        if i in (it, ir):
            return label, sign
    raise AssertionError


# ════════════════════════════════════════════════════════════════
#  6D density variants
# ════════════════════════════════════════════════════════════════
#
# All take a mode tuple n and an optional field grid; return a
# callable density(θ) or samples on a Monte Carlo cloud of θ points.
# ════════════════════════════════════════════════════════════════

def density_MA(theta, n):
    """M-A standing-wave density: ρ(θ) = ∏_i cos²(n_i θ_i) for active i."""
    rho = np.ones(theta.shape[0])
    for i in range(6):
        if n[i] != 0:
            rho = rho * np.cos(n[i] * theta[:, i]) ** 2
    return rho


def density_MB(theta, n, Gti):
    """M-B kinetic/gradient density: |∇ψ|² for ψ = ∏ cos(n_i θ_i).

    ∂_i ψ = -n_i sin(n_i θ_i) · ∏_{j≠i} cos(n_j θ_j).
    |∇ψ|²_G = Σ_ij G̃⁻¹_ij · ∂_i ψ · ∂_j ψ.
    """
    grads = np.zeros((theta.shape[0], 6))
    # Precompute cos products
    cos_all = np.ones(theta.shape[0])
    cos_i = np.ones((theta.shape[0], 6))
    for i in range(6):
        c = np.cos(n[i] * theta[:, i]) if n[i] != 0 else np.ones(theta.shape[0])
        cos_i[:, i] = c
    full = np.prod(cos_i, axis=1)
    for i in range(6):
        if n[i] == 0:
            grads[:, i] = 0.0
            continue
        # Replace cos(n_i θ_i) with −n_i sin(n_i θ_i) in the product
        s = -n[i] * np.sin(n[i] * theta[:, i])
        c_i = cos_i[:, i]
        # Avoid division by near-zero cosines
        prod_without_i = np.where(np.abs(c_i) > 1e-9,
                                  full / np.where(c_i == 0, 1.0, c_i),
                                  np.prod(np.delete(cos_i, i, axis=1), axis=1))
        grads[:, i] = s * prod_without_i
    # Quadratic form with G̃⁻¹ (dimensionless metric inverse)
    quad = np.einsum('ki,ij,kj->k', grads, Gti, grads)
    return quad


def density_MC(theta, n):
    """M-C charge-weighted density.

    Decompose the density as a sum over sheets, weighted by the Ma-S
    coupling sign (−1 for e, 0 for ν, +1 for p).  Each sheet's
    contribution is the standing-wave density restricted to that
    sheet's two coordinates.
    """
    rho = np.zeros(theta.shape[0])
    for label, it, ir, sign in SHEETS:
        if sign == 0.0:
            continue
        if n[it] == 0 and n[ir] == 0:
            continue
        part = np.ones(theta.shape[0])
        if n[it] != 0:
            part = part * np.cos(n[it] * theta[:, it]) ** 2
        if n[ir] != 0:
            part = part * np.cos(n[ir] * theta[:, ir]) ** 2
        rho = rho + sign * part
    return rho


DENSITY_FUNCS = {
    'M-A': lambda theta, n, Gti: density_MA(theta, n),
    'M-B': lambda theta, n, Gti: density_MB(theta, n, Gti),
    'M-C': lambda theta, n, Gti: density_MC(theta, n),
}


# ════════════════════════════════════════════════════════════════
#  Projections T⁶ → 3D radial ρ(r)
# ════════════════════════════════════════════════════════════════

def radial_grid(r_max=5.0, n_r=400):
    return np.linspace(1e-3, r_max, n_r)


def _gaussian_peak(r_grid, center, width, amp=1.0):
    return amp * np.exp(-((r_grid - center) / width) ** 2)


def projection_P1(n, L, Gti, density_key, r_grid):
    """P-1 embedding-sum: each active compact dim i contributes a Gaussian
    peak at r_i = L_i / (2π), width = r_i / (2π·|n_i|).

    Weighted by Ma-S coupling sign if density_key == 'M-C'.
    """
    rho = np.zeros_like(r_grid)
    for i, ni in active_directions(n):
        r_i = L[i] / (2 * math.pi)
        # Skip ν-sheet contributions (scale ≫ r_max; invisible on grid)
        if r_i > 20 * r_grid.max():
            continue
        w_i = max(r_i / (2 * math.pi * abs(ni)), 0.01)
        amp = 1.0
        if density_key == 'M-C':
            _, sign = sheet_of(i)
            if sign == 0:
                continue
            amp = sign
        elif density_key == 'M-B':
            # Kinetic weight: |n_i / L_i|² × G̃⁻¹_{ii}
            amp = abs((ni / L[i]) ** 2 * Gti[i, i])
        # M-A: amplitude 1
        rho = rho + _gaussian_peak(r_grid, r_i, w_i, amp)
    return rho


def projection_P2(n, L, Gti, density_key, r_grid):
    """P-2 node-wavelet packets: each active dim i contributes |n_i|
    peaks at the standing-wave antinodes, r_{i,k} = (k+0.5)·L_i/(2π·|n_i|)
    for k = 0..|n_i|−1, each with width L_i/(4π·|n_i|).

    Weighted by Ma-S coupling sign for M-C.
    """
    rho = np.zeros_like(r_grid)
    for i, ni in active_directions(n):
        if L[i] / (2 * math.pi) > 20 * r_grid.max():
            continue
        n_abs = abs(ni)
        base = L[i] / (2 * math.pi * n_abs)
        w = base / 2.0
        amp = 1.0
        if density_key == 'M-C':
            _, sign = sheet_of(i)
            if sign == 0:
                continue
            amp = sign
        elif density_key == 'M-B':
            amp = abs((ni / L[i]) ** 2 * Gti[i, i])
        for k in range(n_abs):
            r_k = (k + 0.5) * base
            rho = rho + _gaussian_peak(r_grid, r_k, w, amp)
    return rho


def projection_P3(n, L, Gti, density_key, r_grid, n_samples=20000):
    """P-3 hydrogen-like basis projection.

    Sample θ ∈ T⁶ uniformly; for each sample map 6D to 3D radial via
    r(θ) = |Σ_i (L_i/2π) cos(θ_i) sign_factor_i|  (vector sum embedding).
    Build a weighted histogram using the requested 6D density.

    The "hydrogen-like" aspect is that once ρ(r) is formed, the
    characteristic scales appear as peaks (like 1s + 2s nodes).

    Uses only active directions with reasonable embedding radius.
    """
    rng = np.random.default_rng(seed=20260418)
    theta = rng.uniform(0.0, 2 * math.pi, size=(n_samples, 6))

    # Restrict to active dims with radius within grid
    active = [(i, int(n[i])) for i in range(6)
              if n[i] != 0 and L[i] / (2 * math.pi) < 20 * r_grid.max()]
    if not active:
        return np.zeros_like(r_grid)

    # Project r = sqrt( Σ_i (L_i/2π)² sin²(θ_i/2) · weight_i )
    # Use half-angle so r=0 corresponds to all θ_i=0 (mode at center-of-phase)
    r = np.zeros(n_samples)
    for i, ni in active:
        R_i = L[i] / (2 * math.pi)
        # Half-angle radial contribution, weighted by |n_i| (faster oscillation = tighter)
        r2_i = (R_i ** 2) * (np.sin(theta[:, i] / 2) ** 2) * (1.0 / max(1, abs(ni)))
        r = r + r2_i
    r = np.sqrt(r + 1e-12)

    # Build density weights
    if density_key == 'M-A':
        w = density_MA(theta, n)
    elif density_key == 'M-B':
        w = density_MB(theta, n, Gti)
    elif density_key == 'M-C':
        w = density_MC(theta, n)
    else:
        raise ValueError(density_key)

    # Histogram
    edges = np.concatenate([[0.0], 0.5 * (r_grid[:-1] + r_grid[1:]), [r_grid[-1] * 1.01]])
    rho, _ = np.histogram(r, bins=edges, weights=w)
    # Divide by r² to get a volume-normalised radial density
    vol = 4 * math.pi * np.maximum(r_grid, 1e-3) ** 2
    rho = rho / vol
    # Smooth (Gaussian width = grid spacing × 3)
    dr = r_grid[1] - r_grid[0]
    sigma_smooth = 3 * dr
    rho = _gaussian_smooth(rho, dr, sigma_smooth)
    return rho


def projection_P4(n, L, Gti, density_key, r_grid):
    """P-4 Fourier form factor.

    Model: ρ̂(Q) = Σ_i c_i · sinc(Q·L_i / 2) where sinc(x) = sin(x)/x
    is the form factor of a uniform sphere of radius L_i/2.
    c_i weight includes Ma-S sign for M-C.
    Inverse Fourier transform to ρ(r) via the standard formula
    ρ(r) = (1/(2π² r)) ∫ Q·sin(Q·r)·ρ̂(Q) dQ.
    """
    Q = np.linspace(0.001, 30.0, 2000)  # Q in fm⁻¹
    rho_hat = np.zeros_like(Q)
    for i, ni in active_directions(n):
        R_i = L[i] / 2.0  # radius of uniform-sphere analogue
        if R_i > 50 * r_grid.max():
            continue
        amp = 1.0
        if density_key == 'M-C':
            _, sign = sheet_of(i)
            if sign == 0:
                continue
            amp = sign
        elif density_key == 'M-B':
            amp = abs((ni / L[i]) ** 2 * Gti[i, i])
        # Uniform-sphere form factor: 3·(sin(QR)−QR·cos(QR))/(QR)³
        QR = Q * R_i
        ff = np.where(QR > 1e-6,
                      3 * (np.sin(QR) - QR * np.cos(QR)) / (QR ** 3),
                      1.0 - (QR ** 2) / 10)
        # Mode amplitude also modulates by sinc at Q·L/(2π·|n_i|) — captures
        # the winding structure
        wavelength = L[i] / (2 * math.pi * abs(ni))
        mod = np.cos(Q * wavelength * abs(ni) / 2)  # beats at winding scale
        rho_hat = rho_hat + amp * ff * mod

    # Inverse spherical Fourier transform
    rho = np.zeros_like(r_grid)
    dQ = Q[1] - Q[0]
    for idx, r in enumerate(r_grid):
        integrand = Q * np.sin(Q * r) * rho_hat
        rho[idx] = np.sum(integrand) * dQ / (2 * math.pi ** 2 * max(r, 1e-6))
    return rho


PROJECTION_FUNCS = {
    'P-1': projection_P1,
    'P-2': projection_P2,
    'P-3': projection_P3,
    'P-4': projection_P4,
}


# ════════════════════════════════════════════════════════════════
#  Utilities
# ════════════════════════════════════════════════════════════════

def _gaussian_smooth(y, dx, sigma):
    n = max(1, int(4 * sigma / dx))
    x = np.arange(-n, n + 1) * dx
    k = np.exp(-0.5 * (x / sigma) ** 2)
    k = k / k.sum()
    return np.convolve(y, k, mode='same')


# ════════════════════════════════════════════════════════════════
#  Scale extraction
# ════════════════════════════════════════════════════════════════

def detect_scales(r_grid, rho, n_peaks_max=4, min_rel_height=0.02):
    """Classify ρ(r) as 1-scale, 2-scale, or >2-scale.

    Uses |ρ|·r² (radial probability density) to find peaks.
    Returns dict:
      'n_scales': int — number of detected scales
      'scales':   list of (r, amplitude, sign) sorted by r
      'ratio':    float or None — ratio of outer/inner scale (|r|)
    """
    # Radial density weighted by r² (what Losinets reports as "shell thickness")
    weighted = np.abs(rho) * (r_grid ** 2)
    if weighted.max() < 1e-30:
        return {'n_scales': 0, 'scales': [], 'ratio': None}
    w_norm = weighted / weighted.max()

    # Local maxima
    peaks = []
    for i in range(2, len(r_grid) - 2):
        if (w_norm[i] > w_norm[i - 1] and w_norm[i] > w_norm[i + 1]
                and w_norm[i] > min_rel_height):
            # Preserve sign info from the unweighted density
            peaks.append((r_grid[i], w_norm[i], np.sign(rho[i])))

    # Also check the right edge (tail peaks)
    # Remove duplicates within 5% relative separation
    peaks.sort(key=lambda p: p[0])
    deduped = []
    for p in peaks:
        if deduped and abs(p[0] - deduped[-1][0]) / p[0] < 0.05:
            if p[1] > deduped[-1][1]:
                deduped[-1] = p
        else:
            deduped.append(p)

    # Take up to n_peaks_max, keeping the most prominent ones
    deduped.sort(key=lambda p: -p[1])
    top = sorted(deduped[:n_peaks_max], key=lambda p: p[0])

    n_scales = len(top)
    if n_scales >= 2:
        ratio = top[-1][0] / top[0][0]
    else:
        ratio = None
    return {'n_scales': n_scales, 'scales': top, 'ratio': ratio}


def classify_2scale(result):
    """Return (n_inner, n_outer, ratio) if 2-scale structure, else None.

    If more than 2 peaks are found, pick the two most prominent
    (fall back to outermost × innermost).
    """
    scales = result['scales']
    if len(scales) < 2:
        return None
    # Keep the two most prominent by amplitude
    top2 = sorted(scales, key=lambda p: -p[1])[:2]
    top2.sort(key=lambda p: p[0])
    r_in, r_out = top2[0][0], top2[1][0]
    return r_in, r_out, r_out / r_in


def criteria_pass(r_in, r_out, sign_in=None, sign_out=None, mode='proton'):
    """Evaluate Losinets success criteria on a 2-scale extraction."""
    ratio = r_out / r_in
    c1 = True  # 2-scale already confirmed
    c2 = RATIO_WINDOW[0] <= ratio <= RATIO_WINDOW[1]
    c3 = (abs(r_in - R_CORE_TARGET) / R_CORE_TARGET < 0.2 and
          abs(r_out - R_MANTLE_TARGET) / R_MANTLE_TARGET < 0.2)
    c4 = True
    if mode == 'neutron' and sign_in is not None and sign_out is not None:
        c4 = (sign_in * sign_out < 0)
    return {'c1': c1, 'c2': c2, 'c3': c3, 'c4': c4}


# ════════════════════════════════════════════════════════════════
#  Run harness for a single mode
# ════════════════════════════════════════════════════════════════

def run_all_variants(mode, label='proton', r_max=5.0, n_r=500, verbose=True):
    """Run M × P = 12 combinations for a single mode.  Returns list of dicts."""
    L, (Lre, Lrnu, Lrp) = build_circumferences()
    Gt, Gti = build_metric(L, S_E, S_NU, S_P, SIGMA_CROSS)
    if Gt is None:
        raise RuntimeError("Metric non-PD at model-E geometry")

    E_mode = mode_energy(mode, L, Gti)
    if verbose:
        print(f"\n{label} mode {mode}:  E = {E_mode:.3f} MeV")
        print(f"  L = {[f'{x:.3e}' for x in L]} fm")

    r_grid = radial_grid(r_max, n_r)
    results = []

    for m_key in ('M-A', 'M-B', 'M-C'):
        for p_key in ('P-1', 'P-2', 'P-3', 'P-4'):
            proj = PROJECTION_FUNCS[p_key]
            try:
                rho = proj(mode, L, Gti, m_key, r_grid)
            except Exception as exc:
                if verbose:
                    print(f"  {m_key}×{p_key}: error {exc}")
                results.append({'M': m_key, 'P': p_key, 'error': str(exc)})
                continue
            scales = detect_scales(r_grid, rho)
            two_scale = classify_2scale(scales)
            entry = {
                'M': m_key, 'P': p_key, 'E_MeV': E_mode,
                'rho': rho, 'r_grid': r_grid,
                'n_scales': scales['n_scales'],
                'scales': scales['scales'],
                'ratio': scales['ratio'],
                'two_scale': two_scale,
            }
            results.append(entry)
    return results, L, Gti
