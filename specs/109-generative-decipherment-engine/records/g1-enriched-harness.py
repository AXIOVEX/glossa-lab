#!/usr/bin/env python3
"""Spec 109, Stage 1 — G1 enriched-objective preflight harness (T104).

Executes the re-preflight of the enriched assignment-search
generator (design G1-E) registered at
specs/109-generative-decipherment-engine/records/
g1-enriched-registration-2026-11-27.md. G1-E is G1-R's search
(the filed G1 revision harness, pin SHA-256 a15c8c57..., whose
3-cycle delta and rotation this harness reuses) over an
ENRICHED objective, with ONE further change, the temperature
calibration:

  E(phi) = L(phi) + LAMBDA * P(phi)

L is the filed objective of the Stage 1 harness (pin SHA-256
f4e84285...): the duplicate-aware cross-validated predictive
log-likelihood under the frozen predictor form, imported from
the filed Stage 1 harness and unchanged. P is the
positional-consistency term: over the numeral-truncated
derivation (the same token stream L scores), each token of
sign s at position class p contributes log q_{phi(s)}(p),
where q_v is value v's positional distribution produced by
G2's positional induction (the Stage 1 harness's
positional_counts mechanization, registration section 3
family (a)) run on the value-side family corpus, smoothed at
ALPHA over the four position classes (initial / medial /
final / sole); the sign-side counts are the same induction
run on the derivation under analysis. The planted assignment
is never read by the term: its two inputs are the corpus
under analysis and the family corpus, exactly the two inputs
the pipeline would have on real material. In matrix form
P(phi) = sum_s M[s][phi(s)] with
M[s][v] = sum_p n_s(p) * log q_v(p), so swap and 3-cycle
deltas of the term are exact and O(1); the internal gate
below asserts every enriched delta form against full
rescoring, and the term's matrix form against a direct
per-token computation, before any run (a disagreement is a
STOP).

CALIBRATION (the scale study's posed question, registered in
the amendment): before the ensemble phase of each search, on
a copy of the constraint state, the harness builds the
frequency-initialized assignment (restart 0's start) and
measures delta-hat, the median |Delta E| over CALIB_K
admissible swaps sampled uniformly from the free sign pairs
(rng seeded from the search prefix). The annealing schedule
is G1-R's two-segment geometric form with every temperature
multiplied by delta-hat: T_hi = C_HI * delta-hat (segment 1,
steps 0..REHEAT_AT), reheat to T_mid = C_MID * delta-hat at
REHEAT_AT, T_lo = C_LO * delta-hat (both segments' floor).
The constants C_HI / C_MID / C_LO are frozen in the
amendment registration: they are 30 / 10 / 0.05 divided by
delta-hat-ref, the median over the five Stage 1 filed
corpora of delta-hat measured under the UNENRICHED objective
(lambda = 0) by this same rule, so at the reference scale
the calibrated schedule reproduces G1-R's filed schedule and
at any other scale it tracks the objective's own energy
scale. The search otherwise is G1-R's exactly: 40 restarts
x 160,000 steps, swaps (p = 0.7) and admissible 3-cycle
rotations (p = 0.3) under exact deltas, restart 0
frequency-initialized, each restart's best-visited state
swap-polished to a local optimum under E, the candidate the
best polished state by E. Admissibility (anchors fixed;
positional admissibility from G2's rho = 0.95 detection on
the derivation, with the filed relaxation rule), the
scoring rule, the margins, the permutation null, the
recovery computation, and every floor are the filed code
and filed values of the earlier preflights, unchanged.

Verdict mode (scale k = 1) runs five fresh corpora (seed
namespace filed in the raw output) under registration
section 2's clauses (i) and (ii) and the shuffle control
(the identical enriched pipeline on the shuffled
derivation, its own detection, term tables, and calibration
measurement), at the SAME floors as Stage 1. Diagnostic
mode (k = 2) runs the identical enriched preflight on five
fresh corpora at 2x corpus scale, built by the scale
amendment's five registered substitutions into the Stage 1
source (each target asserted to occur exactly once; the
fallback accounting of that amendment applies), as a
secondary diagnostic only: it issues no licensing verdict.

Clause (iii) is not re-run: the predictor form and the
scorers are unchanged from Stage 1, whose clause (iii) PASS
stands for the shared predictor; the positional limitation
is restated in the preflight record (positional recovery
on the Latin and Meroitic controls is NOT MEASURABLE;
ground-truth sets of 1 and 0 marks against the floor of 5).

No undeciphered-system output is produced or scored
anywhere in this run. Writes: raw-output JSON (argv[1]);
synthetic corpora and intermediates to custody (argv[2]).
Usage: g1-enriched-harness.py OUT CUSTODY_DIR SEED_NS SCALE_K
[ONLY_REPS]
"""
import hashlib
import importlib.util
import json
import math
import os
import random
import sys
import types
from collections import Counter
from datetime import datetime, timezone
from statistics import median

RECORDS = os.path.dirname(os.path.abspath(__file__))
WORKTREE = os.path.abspath(os.path.join(RECORDS, "..", "..", "..")) + "/"
STAGE1_PATH = RECORDS + "/stage-1-preflight-harness.py"
G1R_PATH = RECORDS + "/g1-revision-harness.py"
STAGE1_SHA = ("f4e84285d38f39f25d46547d9d435a32ad46506513b588ae061"
              "be7a974bc3485")
G1R_SHA = ("a15c8c578b0599b3ab6b44564361d191b8375028fbb43ee3ad6e0"
           "a6f63cdb15a")


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] S109-G1E {msg}", flush=True)


def sha(b):
    return hashlib.sha256(b).hexdigest()


# ---- pins first: any mismatch is a STOP before any build
with open(STAGE1_PATH, "rb") as f:
    stage1_src = f.read()
assert sha(stage1_src) == STAGE1_SHA, "Stage 1 harness pin mismatch"
with open(G1R_PATH, "rb") as f:
    g1r_src = f.read()
assert sha(g1r_src) == G1R_SHA, "G1 revision harness pin mismatch"
with open(__file__, "rb") as f:
    self_sha = sha(f.read())


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


H = load_module("stage1_harness", STAGE1_PATH)
NV = H.NVAL


def load_g1r():
    """The filed G1 revision harness, its Stage 1 import
    directed at this worktree's byte-identical copy (the
    scale study's loading form); only its exact 3-cycle
    delta and rotation are used."""
    src = g1r_src.decode()
    old_prefix = ("/home/tpierson/.syncyard/worktrees/glossa/"
                  "spec109-g1rev-20261127/")
    assert src.count(old_prefix) == 1
    src = src.replace(old_prefix, WORKTREE)
    mod = types.ModuleType("g1r_harness")
    exec(compile(src, "g1-revision-harness.py", "exec"),
         mod.__dict__)
    with open(mod._spec.origin, "rb") as f:
        assert sha(f.read()) == STAGE1_SHA, \
            "the revision harness loaded a Stage 1 file off pin"
    return mod


R = load_g1r()
assert (R.RESTARTS, R.STEPS, R.T_START, R.T_END, R.REHEAT_AT,
        R.REHEAT_T, R.P_CYCLE) == (40, 160000, 30.0, 0.05,
                                   80000, 10.0, 0.3), \
    "G1-R constants differ from the amendment registration"

RECOVERY_FLOOR = 0.80
POS = ("initial", "medial", "final", "sole")
# ---- G1-E registered constants (amendment registration) ----
LAMBDA = 1.0            # frozen in the amendment registration
                        # (development grid + selection rule at
                        # its section 2)
ALPHA = 0.5             # positional-profile smoothing (design constant)
RESTARTS = 40
STEPS = 160000
REHEAT_AT = 80000
P_CYCLE = 0.3
CALIB_K = 2000
CALIB_MAX_DRAWS = 40000
# calibration constants: 30 / 10 / 0.05 divided by
# delta-hat-ref = 63.904459128199335 (the median over the
# five Stage 1 filed corpora of delta-hat measured under
# the unenriched objective by the registered rule;
# amendment registration section 3)
C_HI = 0.46945080842976417
C_MID = 0.15648360280992138
C_LO = 0.000782418014049607


# ------------------------------------------------- scaled source
def load_scaled_stage1(k):
    """The filed Stage 1 source with the scale amendment's
    five registered substitutions; each target asserted to
    occur exactly once (the scale harness's loader)."""
    src = stage1_src.decode()
    pool2 = min(300 * k, 529)
    subs = [("N_ART = 1670", f"N_ART = {1670 * k}"),
            ("N_DUP = 20", f"N_DUP = {20 * k}"),
            ("len(counted_slots) < 60",
             f"len(counted_slots) < {60 * k}"),
            ("((2, 300), (3, 100))",
             f"((2, {pool2}), (3, {100 * k}))"),
            ("raise RuntimeError(f\"distinctness cap at "
             "slot {i}\")",
             "s, b = lang.sequence(rng, lengths[i], "
             "site=sites[i], counted=i in counted_slots)\n"
             "            seen.add(tuple(s))\n"
             "            seqs.append(s)\n"
             "            bounds_list.append(b)\n"
             "            FALLBACK_SLOTS.append(i)")]
    for old, new in subs:
        assert src.count(old) == 1, f"scale substitution " \
            f"target {old!r} occurs {src.count(old)} times"
        src = src.replace(old, new)
    mod = types.ModuleType(f"stage1_scaled_{k}x")
    exec(compile(src, f"stage-1-preflight-harness.py[scale-{k}x]",
                 "exec"), mod.__dict__)
    assert mod.N_ART == 1670 * k and mod.N_DUP == 20 * k
    mod.FALLBACK_SLOTS = []
    return mod


# ------------------------------------------------- the term
def logq_table(Hmod, family):
    """Value-side positional profiles: G2's positional
    induction (Hmod.positional_counts) run on the family
    corpus, smoothed at ALPHA over the four classes."""
    pos_v = Hmod.positional_counts(family)
    logq = {}
    for v in range(NV):
        c = pos_v.get(v, Counter())
        tot = sum(c.values())
        logq[v] = [math.log((c[p] + ALPHA)
                            / (tot + len(POS) * ALPHA))
                   for p in POS]
    return logq


def term_matrix(Hmod, deriv_trunc, logq):
    """M[s][v] = sum_p n_s(p) * log q_v(p), with n_s the
    sign-side positional counts of the same induction run
    on the derivation under analysis."""
    pos_s = Hmod.positional_counts(deriv_trunc)
    M = [[0.0] * NV for _ in range(NV)]
    for s in range(NV):
        c = pos_s.get(s, Counter())
        if not c:
            continue
        for v in range(NV):
            lq = logq[v]
            M[s][v] = sum(c[p] * lq[i] for i, p in enumerate(POS))
    return M


def pos_term(M, phi):
    return sum(M[s][phi[s]] for s in range(NV))


def pos_term_direct(deriv_trunc, logq, phi):
    """Independent implementation: the per-token sum, walked
    token by token."""
    tot = 0.0
    for g in deriv_trunc:
        if len(g) == 1:
            tot += logq[phi[g[0]]][3]
            continue
        for i, m in enumerate(g):
            p = 0 if i == 0 else (2 if i == len(g) - 1 else 1)
            tot += logq[phi[m]][p]
    return tot


class Enriched:
    """The enriched objective E = L + LAMBDA * P over the
    filed objective's parts, with exact deltas."""

    def __init__(self, S, I0, LW, LW0, M, lam):
        self.S, self.I0, self.LW, self.LW0 = S, I0, LW, LW0
        self.M, self.lam = M, lam

    def base(self, phi):
        return H.objective(self.S, self.I0, self.LW, self.LW0, phi)

    def total(self, phi):
        return self.base(phi) + self.lam * pos_term(self.M, phi)

    def swap_delta(self, phi, x, y):
        d = H._swap_delta(self.S, self.I0, self.LW, self.LW0,
                          phi, x, y)
        vx, vy = phi[x], phi[y]
        if vx == vy or self.lam == 0.0:
            return d
        M = self.M
        return d + self.lam * (M[x][vy] + M[y][vx]
                               - M[x][vx] - M[y][vy])

    def cycle3_delta(self, phi, x, y, z, psi):
        d = R.cycle3_delta(self.S, self.I0, self.LW, self.LW0,
                           phi, x, y, z, psi)
        if self.lam == 0.0:
            return d
        M = self.M
        return d + self.lam * (
            M[x][psi[x]] + M[y][psi[y]] + M[z][psi[z]]
            - M[x][phi[x]] - M[y][phi[y]] - M[z][phi[z]])


# ------------------------------------------------- calibration
def measure_delta_scale(E, phi_freq, admissible, fixed, seed):
    """delta-hat: the median |Delta E| over CALIB_K admissible
    swaps sampled uniformly from the free sign pairs at the
    given state (the registered calibration rule)."""
    rng = random.Random(seed)
    free = [s for s in range(NV) if s not in fixed]
    deltas, draws = [], 0
    while len(deltas) < CALIB_K and draws < CALIB_MAX_DRAWS:
        draws += 1
        x, y = rng.sample(free, 2)
        vx, vy = phi_freq[x], phi_freq[y]
        if vy not in admissible[x] or vx not in admissible[y]:
            continue
        deltas.append(abs(E.swap_delta(phi_freq, x, y)))
    assert len(deltas) == CALIB_K, "calibration sample short"
    return median(deltas), draws


# ------------------------------------------------- the search
def _propose(rng, phi, admissible, fixed, free):
    if rng.random() < P_CYCLE:
        x, y, z = rng.sample(free, 3)
        vx, vy, vz = phi[x], phi[y], phi[z]
        if vz not in admissible[x] or vx not in admissible[y] \
                or vy not in admissible[z]:
            return None
        return ("cycle", (x, y, z), R.rotate(phi, x, y, z))
    x, y = rng.sample(free, 2)
    vx, vy = phi[x], phi[y]
    if vy not in admissible[x] or vx not in admissible[y]:
        return None
    psi = list(phi)
    psi[x], psi[y] = vy, vx
    return ("swap", (x, y), psi)


def anneal_e(E, phi0, admissible, fixed, steps, seed,
             t_hi, t_mid, t_lo):
    rng = random.Random(seed)
    phi = list(phi0)
    cur = E.total(phi)
    best, best_phi = cur, list(phi)
    free = [s for s in range(NV) if s not in fixed]
    for step in range(steps):
        if step < REHEAT_AT:
            T = t_hi * (t_lo / t_hi) ** (step / REHEAT_AT)
        else:
            T = t_mid * (t_lo / t_mid) ** (
                (step - REHEAT_AT) / (steps - REHEAT_AT))
        prop = _propose(rng, phi, admissible, fixed, free)
        if prop is None:
            continue
        kind, payload, psi = prop
        if kind == "swap":
            d = E.swap_delta(phi, payload[0], payload[1])
        else:
            d = E.cycle3_delta(phi, payload[0], payload[1],
                               payload[2], psi)
        if d >= 0 or rng.random() < math.exp(d / T):
            phi = psi
            cur += d
            if cur > best:
                best, best_phi = cur, list(phi)
    return best_phi, E.total(best_phi)


def swap_polish_e(E, phi, admissible, fixed):
    phi = list(phi)
    free = [s for s in range(NV) if s not in fixed]
    while True:
        best_d, best_pair = 1e-9, None
        for i, x in enumerate(free):
            for y in free[i + 1:]:
                if phi[y] not in admissible[x] \
                        or phi[x] not in admissible[y]:
                    continue
                d = E.swap_delta(phi, x, y)
                if d > best_d:
                    best_d, best_pair = d, (x, y)
        if best_pair is None:
            return phi, E.total(phi)
        x, y = best_pair
        phi[x], phi[y] = phi[y], phi[x]


def build_E(Hmod, deriv, family, lam):
    """The enriched objective over a derivation, with its
    admissibility inputs; returns (E, deriv_trunc, logq)."""
    fam_w = Hmod.weights_from(family)
    deriv_trunc = [Hmod.truncate_numerals(g) for g in deriv]
    S, I0, LW, LW0 = Hmod.build_objective(deriv_trunc, fam_w)
    logq = logq_table(Hmod, family)
    M = term_matrix(Hmod, deriv_trunc, logq)
    return Enriched(S, I0, LW, LW0, M, lam), deriv_trunc, logq


def g1e_search(Hmod, deriv, family, anchors_sign_value, det_init,
               det_final, seed_prefix, lam=None, log_fn=None):
    """The G1-E search: G1-R's ensemble over the enriched
    objective under the calibrated schedule. Returns
    (candidate, info); info carries the calibration
    measurement, the schedule, and the objective split."""
    if lam is None:
        lam = LAMBDA
    log_fn = log_fn or (lambda m: None)
    init_vals, fin_vals = Hmod.family_positional(family)
    E, deriv_trunc, logq = build_E(Hmod, deriv, family, lam)
    admissible = {}
    for s in range(NV):
        adm = set(range(NV))
        if s in det_init:
            adm &= init_vals
        if s in det_final:
            adm &= fin_vals
        admissible[s] = adm if adm else set(range(NV))
    fixed = dict(anchors_sign_value)
    # calibration: a read-only measurement on a copy of the
    # constraint state, taken before the ensemble phase
    adm_copy = {s: set(a) for s, a in admissible.items()}
    rng0 = random.Random(f"{seed_prefix}-init0")
    phi_freq = Hmod._initial_assignment(rng0, fixed, adm_copy,
                                        deriv, family,
                                        freq_init=True)
    dhat, draws = measure_delta_scale(E, phi_freq, adm_copy,
                                      fixed,
                                      f"{seed_prefix}-calib")
    t_hi, t_mid, t_lo = C_HI * dhat, C_MID * dhat, C_LO * dhat
    log_fn(f"  calibration: delta-hat {dhat:.4f} over {draws} "
           f"draws; schedule {t_hi:.3f} -> {t_lo:.4f}, reheat "
           f"{t_mid:.3f}")
    polished = []
    for r in range(RESTARTS):
        rng = random.Random(f"{seed_prefix}-init{r}")
        phi0 = Hmod._initial_assignment(rng, fixed, admissible,
                                        deriv, family,
                                        freq_init=(r == 0))
        cand, _obj = anneal_e(E, phi0, admissible, fixed, STEPS,
                              f"{seed_prefix}-restart{r}",
                              t_hi, t_mid, t_lo)
        pphi, pobj = swap_polish_e(E, cand, admissible, fixed)
        polished.append((pobj, pphi))
        if (r + 1) % 10 == 0:
            log_fn(f"  ensemble {r + 1}/{RESTARTS} restarts "
                   f"polished (best enriched objective so far "
                   f"{max(o for o, _p in polished):.1f})")
    polished.sort(key=lambda t: -t[0])
    cand, cobj = polished[0][1], polished[0][0]
    relaxed = [s for s in range(NV) if s not in fixed
               and admissible[s] == set(range(NV))
               and (s in det_init or s in det_final)]
    info = {"objective_enriched": cobj,
            "objective_base": E.base(cand),
            "pos_term": pos_term(E.M, cand),
            "best_polished_phi": cand,
            "polished_objectives": [o for o, _p in polished],
            "delta_hat": dhat, "calib_draws": draws,
            "t_hi": t_hi, "t_mid": t_mid, "t_lo": t_lo,
            "relaxed": relaxed}
    return cand, info


def self_test(Hmod):
    """Internal gates, run before any verdict run: the
    enriched swap and 3-cycle deltas against full rescoring
    on 200 random triples/pairs, and the term's matrix form
    against its direct per-token form. Any disagreement is
    a STOP."""
    rng = random.Random("spec109-g1e-delta-selftest")
    fam = [[rng.randrange(NV) for _ in range(rng.randrange(2, 9))]
           for _ in range(300)]
    deriv = [[rng.randrange(NV) for _ in range(rng.randrange(2, 9))]
             for _ in range(300)]
    E, deriv_trunc, logq = build_E(Hmod, deriv, fam, LAMBDA)
    phi = list(range(NV))
    rng.shuffle(phi)
    assert abs(pos_term(E.M, phi)
               - pos_term_direct(deriv_trunc, logq, phi)) < 1e-9
    base = E.total(phi)
    for _ in range(200):
        x, y = rng.sample(range(NV), 2)
        psi = list(phi)
        psi[x], psi[y] = phi[y], phi[x]
        d = E.swap_delta(phi, x, y)
        exact = E.total(psi) - base
        assert abs(d - exact) < 1e-9, (d, exact)
        x, y, z = rng.sample(range(NV), 3)
        psi3 = R.rotate(phi, x, y, z)
        d3 = E.cycle3_delta(phi, x, y, z, psi3)
        exact3 = E.total(psi3) - base
        assert abs(d3 - exact3) < 1e-9, (d3, exact3)
    log("delta self-test: 200/200 enriched swap deltas and "
        "200/200 enriched 3-cycle deltas agree with full "
        "rescoring; term matrix form agrees with the direct "
        "per-token form")


def anatomy(phi, perm, truth, anchors_signs, token_counts):
    """Miss anatomy over the scored signs, by the planted
    value's role (the scale harness's construction)."""
    inv = [0] * NV
    for v, s in enumerate(perm):
        inv[s] = v
    affix = (set(truth["p1"]) | set(truth["p2"]) |
             set(truth["s1"]) | set(truth["s2"]))
    openers = set(truth["openers"])
    closers = set(truth["closers"])
    ctx = set(truth["ctx"])
    by_role = {"stems": 0, "openers": 0, "closers": 0,
               "context": 0, "affixes": 0}
    misses = 0
    for s in range(NV):
        if s in anchors_signs or token_counts[s] < 5:
            continue
        v = inv[s]
        if phi[s] == v:
            continue
        misses += 1
        if v in affix:
            by_role["affixes"] += 1
        elif v in openers:
            by_role["openers"] += 1
        elif v in closers:
            by_role["closers"] += 1
        elif v in ctx:
            by_role["context"] += 1
        else:
            by_role["stems"] += 1
    return {"misses": misses, "by_role": by_role}


def admit_corpus(Hmod, seed_ns, rep, lengths, k):
    """Admission gates: at k = 1 identical to the Stage 1 /
    G1-R harnesses; at k > 1 in the scale amendment's form
    (fallback accounting). Returns (seed, corp, extra)."""
    for attempt in range(50):
        cand_seed = (f"{seed_ns}-{rep}" if attempt == 0
                     else f"{seed_ns}-{rep}-try{attempt}")
        if k > 1:
            Hmod.FALLBACK_SLOTS = []
        corp = Hmod.build_corpus(cand_seed, lengths)
        signseqs = corp["signseqs"]
        truth = corp["truth"]
        perm = truth["perm_value_to_sign"]
        extra = {}
        if k > 1:
            fb = list(Hmod.FALLBACK_SLOTS)
            assert all(lengths[i] == 2 for i in fb), \
                f"fallback at a non-length-2 slot in rep {rep}"
            extra = {"fallbacks": len(fb)}
        if sorted(len(s) for s in signseqs) != sorted(lengths):
            continue
        _d, _r, n_try = Hmod.split_corpus(signseqs)
        if k == 1 and n_try != Hmod.N_ART - Hmod.N_DUP:
            continue
        extra["distinct"] = n_try
        if H.truth_restricted_a(truth, perm) != \
                H.truth_restricted_b(signseqs, perm):
            continue
        tc_try = Counter(m for g in signseqs for m in g)
        if any(tc_try[s] < 5 for s in range(NV)):
            continue
        return cand_seed, corp, extra
    raise AssertionError(f"no admissible corpus for rep {rep}")


def main():
    out_path, custody_dir = sys.argv[1], sys.argv[2]
    seed_ns = sys.argv[3]
    k = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    only_reps = None
    if len(sys.argv) > 5 and sys.argv[5] != "-":
        only_reps = [int(x) for x in sys.argv[5].split(",")]
    reps = 5
    Hmod = H if k == 1 else load_scaled_stage1(k)
    lengths = H.indus_lengths() * k
    assert len(lengths) == 1670 * k and sum(lengths) == 7002 * k
    log(f"G1-E preflight: seed namespace {seed_ns}; scale {k}x; "
        f"lambda {LAMBDA}; Stage 1 harness SHA-256 "
        f"{STAGE1_SHA[:12]}...; G1-R harness SHA-256 "
        f"{G1R_SHA[:12]}...; this harness SHA-256 "
        f"{self_sha[:12]}...")
    self_test(Hmod)
    results = {"design": "G1-E (enriched objective, calibrated "
                         "schedule; amendment registration "
                         "2026-11-27)",
               "seed_namespace": seed_ns,
               "scale": k,
               "stage1_harness_sha256": STAGE1_SHA,
               "g1r_harness_sha256": G1R_SHA,
               "g1e_harness_sha256": self_sha,
               "constants": {
                   "lambda": LAMBDA, "alpha": ALPHA,
                   "restarts": RESTARTS, "steps": STEPS,
                   "reheat_at": REHEAT_AT, "p_cycle": P_CYCLE,
                   "calib_k": CALIB_K,
                   "calib_max_draws": CALIB_MAX_DRAWS,
                   "c_hi": C_HI, "c_mid": C_MID, "c_lo": C_LO},
               "replications": []}
    for rep in range(1, reps + 1):
        if only_reps is not None and rep not in only_reps:
            continue
        seed, corp, extra = admit_corpus(Hmod, seed_ns, rep,
                                         lengths, k)
        signseqs = corp["signseqs"]
        truth = corp["truth"]
        perm = truth["perm_value_to_sign"]
        deriv, reserve, n_distinct = Hmod.split_corpus(signseqs)
        token_counts = Counter(m for g in signseqs for m in g)
        anchors_sv = {perm[v]: v for v in truth["anchors"]}
        inv = [0] * NV
        for v, s in enumerate(perm):
            inv[s] = v
        row = {"rep": rep, "seed": seed, "scale": k,
               "derivation_sequences": len(deriv),
               "reserve_sequences": len(reserve),
               "reserve_tokens": sum(len(g) for g in reserve)}
        row.update(extra)
        if k > 1:
            row["effective_scale"] = n_distinct / 1650.0
        pos_deriv = H.positional_counts(deriv)
        det = H.detect_restricted(pos_deriv, 0.95)
        det_init = {s for s, c in det.items() if c == "initial"}
        det_final = {s for s, c in det.items() if c == "final"}
        log(f"rep {rep}: G1-E search (seed {seed})")
        phi, info = g1e_search(Hmod, deriv, corp["family"],
                               anchors_sv, det_init, det_final,
                               seed + "-g1e", log_fn=log)
        row["g1_recovery"] = H.recovery_g1(phi, perm,
                                           set(anchors_sv),
                                           token_counts)
        row["g1_candidate_phi"] = phi
        row["g1_info"] = {kk: vv for kk, vv in info.items()
                          if kk != "best_polished_phi"}
        row["g1_best_polished_phi"] = info["best_polished_phi"]
        # truth objectives under both forms (anatomy only;
        # the search never reads the truth)
        E_chk, _dt, _lq = build_E(Hmod, deriv, corp["family"],
                                  LAMBDA)
        phi_truth = inv
        row["truth_objective_enriched"] = E_chk.total(phi_truth)
        row["truth_objective_base"] = E_chk.base(phi_truth)
        row["objective_gap_enriched"] = (
            info["objective_enriched"]
            - row["truth_objective_enriched"])
        row["objective_gap_base"] = (
            info["objective_base"] - row["truth_objective_base"])
        row["anatomy"] = anatomy(phi, perm, truth,
                                 set(anchors_sv), token_counts)
        log(f"rep {rep}: candidate recovery "
            f"{row['g1_recovery']['recovery']:.3f} "
            f"({row['g1_recovery']['hits']}/"
            f"{row['g1_recovery']['denominator']}); enriched gap "
            f"{row['objective_gap_enriched']:+.1f}, base gap "
            f"{row['objective_gap_base']:+.1f}; anatomy "
            f"{row['anatomy']['by_role']}")
        # shuffle control: the identical enriched pipeline on
        # the shuffled derivation
        rng_s2 = random.Random(seed + "-g1shuffle")
        shuf_deriv = []
        for g in deriv:
            gg = list(g)
            rng_s2.shuffle(gg)
            shuf_deriv.append(gg)
        pos_sh = H.positional_counts(shuf_deriv)
        det_sh = H.detect_restricted(pos_sh, 0.95)
        log(f"rep {rep}: G1-E shuffle control")
        phi_sh, info_sh = g1e_search(
            Hmod, shuf_deriv, corp["family"], anchors_sv,
            {s for s, c in det_sh.items() if c == "initial"},
            {s for s, c in det_sh.items() if c == "final"},
            seed + "-g1eshuf", log_fn=log)
        row["g1_shuffle_recovery"] = H.recovery_g1(
            phi_sh, perm, set(anchors_sv), token_counts)
        row["g1_shuffle_delta_hat"] = info_sh["delta_hat"]
        log(f"rep {rep}: shuffle recovery "
            f"{row['g1_shuffle_recovery']['recovery']:.3f}")
        # margins and null (Stage 1 code, unchanged)
        rng_der = random.Random(seed + "-derange")
        der = list(range(NV))
        while True:
            rng_der.shuffle(der)
            if all(der[v] != v for v in range(NV)):
                break
        phi_wrong = [der[inv[s]] for s in range(NV)]
        rng_sa = random.Random(seed + "-shufassign")
        free_signs = [s for s in range(NV) if s not in anchors_sv]
        sa_vals = [phi[s] for s in free_signs]
        rng_sa.shuffle(sa_vals)
        phi_shuffle = list(phi)
        for s, v in zip(free_signs, sa_vals):
            phi_shuffle[s] = v
        mg = H.g1_margins(corp["family"], reserve, phi, phi_wrong,
                          phi_shuffle)
        n_free = NV - len(anchors_sv)
        best_rival_total = min(mg["rivals"].values())
        penalized = mg["margin_raw"] - 2 * n_free
        p99, _dist = H.g1_null(corp["family"], reserve, phi,
                               anchors_sv, best_rival_total,
                               n_free, seed + "-null")
        row["g1_margin"] = {
            "candidate_derived_total": mg["tot_cand"]["derived_total"],
            "rivals": mg["rivals"], "margin_raw": mg["margin_raw"],
            "free_choices": n_free, "penalized_margin": penalized,
            "null_p99": p99,
            "pass": bool(penalized >= 10 and penalized > p99)}
        row["g1_relaxed"] = info["relaxed"]
        results["replications"].append(row)
        with open(f"{custody_dir}/synth-rep{rep}.json", "w") as f:
            json.dump({"seed": seed, "signseqs": signseqs,
                       "bounds": [sorted(b) for b in corp["bounds"]],
                       "sites": [corp["sites"][i]
                                 for i in range(Hmod.N_ART)],
                       "family": corp["family"], "truth": truth,
                       "counted_slots": corp["counted_slots"]}, f)
        log(f"rep {rep}: complete ({len(results['replications'])} "
            f"replications filed)")
    recs = [r["g1_recovery"]["recovery"]
            for r in results["replications"]]
    shufs = [r["g1_shuffle_recovery"]["recovery"]
             for r in results["replications"]]
    summary = {
        "g1_recovery_median": median(recs) if recs else None,
        "g1_recoveries": recs,
        "g1_shuffle_recovery_median": median(shufs) if shufs else None,
        "g1_margin_pass_reps": sum(
            1 for r in results["replications"]
            if r["g1_margin"]["pass"]),
        "g1_penalized_median": median(
            [r["g1_margin"]["penalized_margin"]
             for r in results["replications"]]) if recs else None}
    ctrl = (summary["g1_shuffle_recovery_median"] is not None
            and summary["g1_recovery_median"]
            and summary["g1_shuffle_recovery_median"]
            < 0.5 * summary["g1_recovery_median"])
    summary["verdicts"] = {
        "clause_i_recovery": bool(
            summary["g1_recovery_median"] is not None
            and summary["g1_recovery_median"] >= RECOVERY_FLOOR),
        "clause_ii_margin": summary["g1_margin_pass_reps"] >= 3,
        "shuffle_control": bool(ctrl)}
    summary["verdicts"]["verdict"] = (
        "PASSED" if all(summary["verdicts"].values()) else "FAILED")
    if k > 1:
        summary["diagnostic_only"] = True
    results["summary"] = summary
    with open(out_path, "w") as f:
        json.dump(results, f, indent=1)
    log(f"verdicts: {json.dumps(summary['verdicts'])}; median "
        f"recovery {summary['g1_recovery_median']}")
    log(f"raw output written to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
