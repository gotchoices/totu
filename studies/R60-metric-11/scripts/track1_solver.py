"""
R60 Track 1: Solver infrastructure for the 11D metric with α coupling.

Primitives (all usable independently):

    build_metric_11(params)        -> 11x11 array (symmetric)
    signature_ok(G)                -> bool  (exactly one negative eigenvalue)
    mode_energy(G, L, n11)         -> float (MeV)
    alpha_coulomb(G, n11)          -> float (dimensionless)
    solve(params0, free, targets)  -> SolveResult

Index ordering (R59 convention, T⁶ × S × t × ℵ):

    0: ℵ   (aleph, sub-Planck internal dim)
    1: p_t,  2: p_r     (proton sheet: tube, ring)
    3: e_t,  4: e_r     (electron sheet)
    5: ν_t,  6: ν_r     (neutrino sheet)
    7: S_x,  8: S_y,  9: S_z  (3D space, Euclidean)
   10: t                (time, Lorentzian -1)

Ma-block mode 6-tuple ordering when interpreted as model-E mode
(electron sheet, neutrino sheet, proton sheet):
    n6 = (n_et, n_er, n_νt, n_νr, n_pt, n_pr)
Use mode_6_to_11(n6) to translate into the 11-slot mode vector.

Track 1 is infrastructure only — no physics conclusions.  Four
smoke tests verify each primitive against a known result:
    T1  11D reproduces model-E masses when α knobs are off
    T2  R59 F59 natural-form point gives α_Coulomb = α
    T3  F41 signature rejection on shear-saturated e-tube
    T4  Single-knob fit of L_ring_e against m_e converges
"""

import math
from dataclasses import dataclass, field, replace
from typing import Callable, Sequence

import numpy as np
from scipy.optimize import least_squares

# ── Constants ────────────────────────────────────────────────────────

ALPHA       = 1.0 / 137.036
SQRT_ALPHA  = math.sqrt(ALPHA)
PI          = math.pi
TWO_PI      = 2 * PI
FOUR_PI     = 4 * PI
EIGHT_PI    = 8 * PI

# hbar*c in MeV·fm — match lib/ma_model_d convention
HBAR_C_MEV_FM = 197.3269804
TWO_PI_HC     = TWO_PI * HBAR_C_MEV_FM

M_E_MEV  = 0.5109989461
M_P_MEV  = 938.272

# Indices into the 11D metric
I_ALEPH   = 0
I_P_TUBE  = 1;  I_P_RING  = 2
I_E_TUBE  = 3;  I_E_RING  = 4
I_NU_TUBE = 5;  I_NU_RING = 6
I_SX, I_SY, I_SZ = 7, 8, 9
I_T       = 10

MA_SLICE   = slice(1, 7)   # the six Ma dimensions in the 11D ordering

# Sheet-block indices for the (tube, ring) pairs
P_BLOCK  = (I_P_TUBE,  I_P_RING)
E_BLOCK  = (I_E_TUBE,  I_E_RING)
NU_BLOCK = (I_NU_TUBE, I_NU_RING)


# ── Ma mode helpers ──────────────────────────────────────────────────

def mode_6_to_11(n6) -> np.ndarray:
    """Translate a model-E 6-tuple (n_et, n_er, n_νt, n_νr, n_pt, n_pr)
    into the 11-slot vector used by this module."""
    n11 = np.zeros(11)
    n11[I_E_TUBE]  = n6[0]
    n11[I_E_RING]  = n6[1]
    n11[I_NU_TUBE] = n6[2]
    n11[I_NU_RING] = n6[3]
    n11[I_P_TUBE]  = n6[4]
    n11[I_P_RING]  = n6[5]
    return n11


def mu_sheet(n_tube: int, n_ring: int, eps: float, s: float) -> float:
    """Dimensionless single-sheet mode energy used by model-E."""
    return math.sqrt((n_tube / eps) ** 2 + (n_ring - n_tube * s) ** 2)


# ── Parameters ───────────────────────────────────────────────────────

@dataclass
class Params:
    """Parametric 11D metric configuration.

    Sheet geometry (three sheets):
      eps_*         tube/ring aspect ratio
      s_*           in-sheet shear
      L_ring_*      ring circumference (fm); if None, derived from mass
      k_*           per-sheet diagonal scale (R59 F53; k_e = k_p for universality)

    α-coupling knobs (R59 F59 natural-form target):
      g_aa          ℵ diagonal                (default 1)
      sigma_ta      |tube↔ℵ| magnitude         (R59: √α)
      sigma_at      ℵ↔t                       (R59: 4πα)
      sign_e, sign_p, sign_nu
                    signs on tube↔ℵ per sheet  (R59: +1, −1, 0)

    Cross-sheet Ma shears (σ dict keyed by 11-index pairs (i, j),
    with i, j ∈ MA_SLICE).  Missing entries default to zero.
    """

    eps_e: float      = 397.074
    eps_nu: float     = 5.0
    eps_p: float      = 0.55
    s_e: float        = 2.004200
    s_nu: float       = 0.022
    s_p: float        = 0.162037
    L_ring_e: float   = None
    L_ring_nu: float  = None
    L_ring_p: float   = None
    k_e: float        = 1.0
    k_p: float        = 1.0
    k_nu: float       = 1.0
    g_aa: float       = 1.0
    sigma_ta: float   = 0.0
    sigma_at: float   = 0.0
    sign_e: float     = +1.0
    sign_p: float     = -1.0
    sign_nu: float    = 0.0
    sigma_cross: dict = field(default_factory=dict)

    def copy_with(self, **updates) -> "Params":
        """Return a new Params with selected fields updated."""
        return replace(self, **updates)


# ── Reference mode L-derivation ──────────────────────────────────────

def derive_L_ring(target_mass_MeV: float, n_tube: int, n_ring: int,
                   eps: float, s: float, k: float) -> float:
    """
    Closed-form L_ring such that mode_energy((n_tube, n_ring)) = target_mass
    on an isolated sheet with diagonal scale k.

    E = (2π ℏc) × μ / (L_ring × √k)
    →  L_ring = (2π ℏc) × μ / (m × √k)
    """
    mu = mu_sheet(n_tube, n_ring, eps, s)
    return TWO_PI_HC * mu / (target_mass_MeV * math.sqrt(k))


def fill_derived_L(p: Params,
                    n_e=(1, 2), n_p=(1, 3)) -> Params:
    """Fill any L_ring_* = None using the reference-mode closed form."""
    updates = {}
    if p.L_ring_e is None:
        updates["L_ring_e"] = derive_L_ring(
            M_E_MEV, n_e[0], n_e[1], p.eps_e, p.s_e, p.k_e)
    if p.L_ring_p is None:
        updates["L_ring_p"] = derive_L_ring(
            M_P_MEV, n_p[0], n_p[1], p.eps_p, p.s_p, p.k_p)
    if p.L_ring_nu is None:
        # Track 1 does not require ν ring calibration; placeholder fm
        updates["L_ring_nu"] = 1.0
    return p.copy_with(**updates) if updates else p


# ── Metric construction ─────────────────────────────────────────────

def _sheet_block(eps: float, s: float, k: float) -> np.ndarray:
    """Dimensionless 2x2 Ma block for one sheet.

    Derivation.  Physical sheet metric from shear-twisted torus:
        B = diag(L_tube, L_ring) · (I + [[0, s], [0, 0]])
        G_phys = B^T B
    Normalize to dimensionless: G̃_ij = G_phys_ij / (L_i L_j).
    With L_tube = ε · L_ring, this gives:
        G̃_sheet = [[1,        s·ε        ],
                   [s·ε,      1 + (s·ε)² ]]
    (cross-check: mode energy on this block is (2πℏc / L_ring)
    × √((1/ε)² + (n_r − s·n_t)²), matching model-E's μ_sheet.)

    The k scale is applied uniformly to the whole sheet block, per
    the R59 F53 diagonal-scaling parameterization.
    """
    se = s * eps
    block = np.array([[1.0, se        ],
                      [se,  1.0 + se*se]])
    return k * block


def build_metric_11(p: Params) -> np.ndarray:
    """Construct the symmetric 11x11 metric from a Params object."""
    G = np.zeros((11, 11))

    # ── Material block: 3 sheets, each a 2x2 ──
    p_block  = _sheet_block(p.eps_p,  p.s_p,  p.k_p)
    e_block  = _sheet_block(p.eps_e,  p.s_e,  p.k_e)
    nu_block = _sheet_block(p.eps_nu, p.s_nu, p.k_nu)
    G[1:3, 1:3] = p_block
    G[3:5, 3:5] = e_block
    G[5:7, 5:7] = nu_block

    # ── Cross-sheet Ma shears ──
    for (i, j), v in p.sigma_cross.items():
        G[i, j] += v
        G[j, i] += v  # symmetric

    # ── Space (Euclidean identity) ──
    G[I_SX, I_SX] = 1.0
    G[I_SY, I_SY] = 1.0
    G[I_SZ, I_SZ] = 1.0

    # ── Time (Lorentzian) ──
    G[I_T, I_T] = -1.0

    # ── ℵ diagonal ──
    G[I_ALEPH, I_ALEPH] = p.g_aa

    # ── tube ↔ ℵ couplings (signed per sheet) ──
    if p.sigma_ta != 0.0:
        for sign_val, tube_idx in (
            (p.sign_e,  I_E_TUBE),
            (p.sign_p,  I_P_TUBE),
            (p.sign_nu, I_NU_TUBE),
        ):
            val = sign_val * p.sigma_ta
            if val != 0.0:
                G[I_ALEPH,  tube_idx] = val
                G[tube_idx, I_ALEPH]  = val

    # ── ℵ ↔ t coupling ──
    if p.sigma_at != 0.0:
        G[I_ALEPH, I_T] = p.sigma_at
        G[I_T, I_ALEPH] = p.sigma_at

    return G


# ── Signature and spectrum checks ────────────────────────────────────

def signature_ok(G: np.ndarray) -> bool:
    """True if the metric has exactly one negative eigenvalue (time only)."""
    eigs = np.linalg.eigvalsh(G)
    return int(np.sum(eigs < 0)) == 1


def num_negative_eigs(G: np.ndarray) -> int:
    return int(np.sum(np.linalg.eigvalsh(G) < 0))


# ── Mode energy ──────────────────────────────────────────────────────

def L_vector_from_params(p: Params) -> np.ndarray:
    """Per-dimension L for the Ma slice (fm).  S and t get 1.0 placeholder.

    Model-E convention: L_tube = ε × L_ring.
    Ordering matches the 11D index layout.
    """
    L = np.ones(11)
    L[I_P_TUBE]  = p.eps_p  * p.L_ring_p
    L[I_P_RING]  = p.L_ring_p
    L[I_E_TUBE]  = p.eps_e  * p.L_ring_e
    L[I_E_RING]  = p.L_ring_e
    L[I_NU_TUBE] = p.eps_nu * p.L_ring_nu
    L[I_NU_RING] = p.L_ring_nu
    L[I_ALEPH]   = 1.0  # dimensionless; n_ℵ = 0 for all particle modes
    return L


def mode_energy(G: np.ndarray, L: np.ndarray, n11: np.ndarray) -> float:
    """Energy in MeV for a mode.  Uses the Ma subspace only.

    For particle modes we take n_S = n_t = n_ℵ = 0.  Treat the Ma block
    in isolation: ñ = n/L on the six Ma indices, E = 2πℏc √(ñ · G̃⁻¹_Ma · ñ).

    NOTE: This does *not* include back-reaction from the α coupling on
    the Ma mass spectrum — a deliberate simplification for Track 1
    smoke tests.  Coupling-induced mass shifts (R59 F13, ~1.3%) will
    be handled once α-on tracks begin.
    """
    G_ma = G[MA_SLICE, MA_SLICE]
    G_ma_inv = np.linalg.inv(G_ma)
    n_ma = n11[MA_SLICE]
    L_ma = L[MA_SLICE]
    n_tilde = n_ma / L_ma
    E2 = (TWO_PI_HC ** 2) * (n_tilde @ G_ma_inv @ n_tilde)
    return math.sqrt(max(E2, 0.0))


# ── α_Coulomb extraction (R59 Track 3g formula) ─────────────────────

def alpha_coulomb(G: np.ndarray, n11: np.ndarray) -> float:
    """Effective Coulomb α for the given mode.

    Formula (R59 track3g):
        Q  = (ñ_Ma · G⁻¹[Ma, t]) × (−G⁻¹[t, t])
        α  = Q² / (4π)

    With the ñ = n factor (no L here — R59 worked in the dimensionless
    metric; see track3g_natural_form_scan.py).  For R60 the L scaling
    is separate from the α extraction.
    """
    try:
        G_inv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return float("nan")
    n_ma = n11[MA_SLICE]
    ma_t_col = G_inv[MA_SLICE, I_T]
    Q = float((n_ma @ ma_t_col) * (-G_inv[I_T, I_T]))
    return Q * Q / FOUR_PI


# ── Joint solver ─────────────────────────────────────────────────────

@dataclass
class Target:
    """One residual function to drive to zero.

    `fn(params) -> float` returns the residual (any units).  The solver
    divides by `scale` to normalize across heterogeneous targets.
    """
    name: str
    fn: Callable[[Params], float]
    scale: float = 1.0


@dataclass
class SolveResult:
    params: Params
    residuals: np.ndarray
    cost: float
    success: bool
    jacobian: np.ndarray | None
    message: str


def solve(params0: Params,
          free: Sequence[str],
          targets: Sequence[Target],
          bounds: dict | None = None,
          **ls_kwargs) -> SolveResult:
    """Least-squares fit over a subset of Params fields.

    Parameters
    ----------
    params0   initial Params
    free      names of fields in Params to let the solver vary
    targets   list of Target; each contributes one residual
    bounds    optional dict {field: (low, high)}
    """
    x0 = np.array([getattr(params0, k) for k in free], dtype=float)

    lo = [-np.inf] * len(free)
    hi = [ np.inf] * len(free)
    if bounds:
        for i, k in enumerate(free):
            if k in bounds:
                a, b = bounds[k]
                lo[i], hi[i] = a, b

    def residual_vec(x):
        updates = {k: float(x[i]) for i, k in enumerate(free)}
        p = params0.copy_with(**updates)
        r = [t.fn(p) / t.scale for t in targets]
        return np.array(r, dtype=float)

    res = least_squares(residual_vec, x0, bounds=(lo, hi), **ls_kwargs)
    updates = {k: float(res.x[i]) for i, k in enumerate(free)}
    p_final = params0.copy_with(**updates)
    return SolveResult(
        params=p_final,
        residuals=res.fun,
        cost=float(res.cost),
        success=bool(res.success),
        jacobian=res.jac if hasattr(res, "jac") else None,
        message=str(res.message),
    )


# ═════════════════════════════════════════════════════════════════════
#  Smoke tests
# ═════════════════════════════════════════════════════════════════════

def _model_E_params() -> Params:
    """Model-E Ma-only configuration (α knobs off, k = 1).
    ε_e, s_e from R53 Solution D; ε_p, s_p from R54; ε_ν, s_ν from R49."""
    p = Params(
        eps_e=397.074, s_e=2.004200,
        eps_p=0.55,    s_p=0.162037,
        eps_nu=5.0,    s_nu=0.022,
        k_e=1.0, k_p=1.0, k_nu=1.0,
        g_aa=1.0, sigma_ta=0.0, sigma_at=0.0,
    )
    return fill_derived_L(p)


def _r59_f59_params() -> Params:
    """R59 F59 natural-form clean metric (shearless, α knobs on)."""
    p = Params(
        eps_e=1.0, s_e=0.0,
        eps_p=1.0, s_p=0.0,
        eps_nu=1.0, s_nu=0.0,
        k_e=1.0 / EIGHT_PI, k_p=1.0 / EIGHT_PI, k_nu=1.0,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA,
        sigma_at=FOUR_PI * ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=0.0,
    )
    # L's are irrelevant for α_Coulomb; leave at placeholder 1 fm
    return p.copy_with(L_ring_e=1.0, L_ring_p=1.0, L_ring_nu=1.0)


def _fmt(x, n=10):
    return f"{x:.{n}g}"


def smoke_test_T1():
    """Reproduce model-E masses in 11D (α knobs off)."""
    print("─" * 72)
    print("T1: 11D reproduces model-E masses when α knobs are off")
    print("─" * 72)
    p = _model_E_params()
    G = build_metric_11(p)
    L = L_vector_from_params(p)

    ok_sig = signature_ok(G)
    nneg = num_negative_eigs(G)
    print(f"  signature_ok = {ok_sig}  (neg eigs = {nneg}, expect 1)")

    E_e = mode_energy(G, L, mode_6_to_11((1, 2, 0, 0, 0, 0)))
    E_p = mode_energy(G, L, mode_6_to_11((0, 0, 0, 0, 1, 3)))
    rel_e = abs(E_e - M_E_MEV) / M_E_MEV
    rel_p = abs(E_p - M_P_MEV) / M_P_MEV
    print(f"  E(electron) = {_fmt(E_e)} MeV,  rel error = {_fmt(rel_e, 2)}")
    print(f"  E(proton)   = {_fmt(E_p)} MeV,  rel error = {_fmt(rel_p, 2)}")

    passed = ok_sig and rel_e < 1e-10 and rel_p < 1e-10
    print(f"  RESULT: {'PASS' if passed else 'FAIL'}")
    return passed


def smoke_test_T2():
    """Reproduce R59 F59 natural-form α_Coulomb = α."""
    print("─" * 72)
    print("T2: R59 F59 natural-form point gives α_Coulomb = α to <100 ppm")
    print("─" * 72)
    p = _r59_f59_params()
    G = build_metric_11(p)
    ok_sig = signature_ok(G)
    nneg = num_negative_eigs(G)
    print(f"  signature_ok = {ok_sig}  (neg eigs = {nneg}, expect 1)")

    # Try the electron mode as (1,2,0,0,0,0) — the R59 reference
    ae = alpha_coulomb(G, mode_6_to_11((1, 2, 0, 0, 0, 0)))
    ap = alpha_coulomb(G, mode_6_to_11((0, 0, 0, 0, 1, 3)))
    an = alpha_coulomb(G, mode_6_to_11((0, 0, 1, 1, 0, 0)))

    ratio_e = ae / ALPHA
    ratio_p = ap / ALPHA
    ratio_ep = ae / ap if ap != 0 else float("inf")
    print(f"  α_e/α = {_fmt(ratio_e, 8)}")
    print(f"  α_p/α = {_fmt(ratio_p, 8)}")
    print(f"  α_e/α_p = {_fmt(ratio_ep, 8)}  (universality; expect 1)")
    print(f"  α_ν = {_fmt(an, 4)}  (ν neutrality; expect 0)")

    passed_e  = abs(ratio_e - 1.0) < 1e-4
    passed_u  = abs(ratio_ep - 1.0) < 1e-10
    passed_nu = abs(an) < 1e-20
    passed = ok_sig and passed_e and passed_u and passed_nu
    print(f"  RESULT: {'PASS' if passed else 'FAIL'}")
    return passed


def smoke_test_T3():
    """F41 signature rejection — shear-saturated e-tube + any tube↔ℵ."""
    print("─" * 72)
    print("T3: F41 signature rejection on model-E Ma + tube↔ℵ")
    print("─" * 72)
    p = _model_E_params().copy_with(
        sigma_ta=SQRT_ALPHA,
        sigma_at=FOUR_PI * ALPHA,
    )
    G = build_metric_11(p)
    nneg = num_negative_eigs(G)
    print(f"  neg eigs = {nneg}  (expect > 1 → signature_ok == False)")
    ok = signature_ok(G)
    print(f"  signature_ok = {ok}  (expect False)")
    # Also try a tiny coupling to verify it's the shear that breaks it
    p_small = _model_E_params().copy_with(sigma_ta=0.01, sigma_at=0.01)
    G_small = build_metric_11(p_small)
    nneg_small = num_negative_eigs(G_small)
    print(f"  at σ = 0.01: neg eigs = {nneg_small}  (F41 says still bad)")

    passed = (not ok) and nneg_small > 1
    print(f"  RESULT: {'PASS' if passed else 'FAIL'}")
    return passed


def smoke_test_T4():
    """Single-knob solve: fit L_ring_e against target m_e."""
    print("─" * 72)
    print("T4: solver converges single-knob fit of L_ring_e against m_e")
    print("─" * 72)
    p0 = _model_E_params().copy_with(L_ring_e=1000.0)  # bad initial guess
    expected_L = derive_L_ring(M_E_MEV, 1, 2, p0.eps_e, p0.s_e, p0.k_e)

    def residual_me(p: Params) -> float:
        G = build_metric_11(p)
        L = L_vector_from_params(p)
        E_e = mode_energy(G, L, mode_6_to_11((1, 2, 0, 0, 0, 0)))
        return (E_e - M_E_MEV) / M_E_MEV

    targets = [Target("m_e", residual_me, scale=1.0)]
    result = solve(
        p0, free=["L_ring_e"], targets=targets,
        bounds={"L_ring_e": (1.0, 1e6)},
        xtol=1e-12, ftol=1e-12,
    )
    got_L = result.params.L_ring_e
    rel_L = abs(got_L - expected_L) / expected_L
    final_resid = float(result.residuals[0])
    print(f"  closed-form L_ring_e = {_fmt(expected_L)}")
    print(f"  solver  L_ring_e     = {_fmt(got_L)}")
    print(f"  rel error vs closed  = {_fmt(rel_L, 3)}")
    print(f"  residual (m_e, rel)  = {_fmt(final_resid, 3)}")
    print(f"  solver message       = {result.message}")
    passed = rel_L < 1e-6 and abs(final_resid) < 1e-6
    print(f"  RESULT: {'PASS' if passed else 'FAIL'}")
    return passed


# ── Sanity: simple particle fits (not definitive) ────────────────────

def sanity_electron_fit():
    """Two-knob sanity: fit (L_ring_e, eps_e) against (m_e) with α coupling on.

    Not a physics result — just confirms the solver handles multi-knob
    with α coupling active and the metric-11 environment.  Expected:
    converges to an (L, ε) pair (many pairs satisfy one target).
    """
    print("─" * 72)
    print("Sanity: electron L_ring_e × eps_e at α coupling on")
    print("─" * 72)
    # R59 F59 natural-form knobs with shears zero (clean Ma)
    p0 = Params(
        eps_e=1.5, s_e=0.0,
        eps_p=1.0, s_p=0.0,
        eps_nu=1.0, s_nu=0.0,
        k_e=1.0/EIGHT_PI, k_p=1.0/EIGHT_PI, k_nu=1.0,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
    )
    p0 = p0.copy_with(L_ring_e=100.0, L_ring_p=1.0, L_ring_nu=1.0)

    def residual_me(p: Params) -> float:
        G = build_metric_11(p)
        L = L_vector_from_params(p)
        if not signature_ok(G):
            return 1e6
        E_e = mode_energy(G, L, mode_6_to_11((1, 2, 0, 0, 0, 0)))
        return (E_e - M_E_MEV) / M_E_MEV

    targets = [Target("m_e", residual_me, scale=1.0)]
    result = solve(
        p0,
        free=["L_ring_e"],   # only one free (target is one residual)
        targets=targets,
        bounds={"L_ring_e": (0.1, 1e6)},
        xtol=1e-12, ftol=1e-12,
    )
    # Report α_Coulomb at the solution to confirm α coupling is on
    G = build_metric_11(result.params)
    ae = alpha_coulomb(G, mode_6_to_11((1, 2, 0, 0, 0, 0)))
    L = L_vector_from_params(result.params)
    E_e = mode_energy(G, L, mode_6_to_11((1, 2, 0, 0, 0, 0)))
    print(f"  eps_e      = {_fmt(result.params.eps_e)}")
    print(f"  L_ring_e   = {_fmt(result.params.L_ring_e)}")
    print(f"  E_e        = {_fmt(E_e)} MeV  (target {M_E_MEV})")
    print(f"  α_e/α      = {_fmt(ae / ALPHA, 6)}")
    print(f"  residual   = {_fmt(float(result.residuals[0]), 3)}")
    print(f"  converged  = {result.success}  ({result.message})")
    return result


# ═════════════════════════════════════════════════════════════════════
#  Entry point
# ═════════════════════════════════════════════════════════════════════

def main():
    print("=" * 72)
    print("R60 Track 1 — Solver infrastructure smoke tests")
    print("=" * 72)
    print(f"  ALPHA    = {ALPHA}")
    print(f"  √α       = {SQRT_ALPHA}")
    print(f"  1/(8π)   = {1/EIGHT_PI}")
    print(f"  4πα      = {FOUR_PI*ALPHA}")
    print()

    results = {
        "T1": smoke_test_T1(),
        "T2": smoke_test_T2(),
        "T3": smoke_test_T3(),
        "T4": smoke_test_T4(),
    }
    print()
    print("─" * 72)
    print("Sanity checks (not definitive, not part of acceptance):")
    print("─" * 72)
    sanity_electron_fit()

    print()
    print("=" * 72)
    print("Summary")
    print("=" * 72)
    for k, v in results.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
    all_passed = all(results.values())
    print(f"  ALL: {'PASS' if all_passed else 'FAIL'}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
