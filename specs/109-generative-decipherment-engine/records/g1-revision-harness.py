#!/usr/bin/env python3
"""Spec 109, Stage 1 — G1 revision preflight harness (T102).

Executes the G1 re-preflight registered at
specs/109-generative-decipherment-engine/records/
g1-revision-registration-2026-11-27.md: the revised
assignment-search generator (design G1-R) run on five
FRESH synthetic corpora (seeds "spec109-s1r-synth-{1..5}",
admission gates identical to the Stage 1 harness), judged
under registration section 2's clauses (i) and (ii) and the
shuffle control, at the SAME floors as Stage 1 (recovery
median >= 0.80 across the 5 replications; margin clears in
the median replication; shuffle recovery < 0.5 x right
recovery). Clause (iii) is not re-run: the predictor form
and the scorers are unchanged (the Stage 1 record's clause
(iii) PASS stands for the shared predictor), and this
harness reuses the Stage 1 harness's code for the corpus
construction, the objective, the scorers, the margins, the
null, and the recovery computation — imported from the
filed Stage 1 harness, whose SHA-256 is pinned in the raw
output. Only the search differs.

THE REVISED SEARCH (G1-R), as registered. The objective,
the admissibility construction (anchors fixed; positional
admissibility from G2's rho = 0.95 detection on the
derivation, with the filed relaxation rule), the scoring
rule, and every floor are IDENTICAL to Stage 1. What
changes is how the candidate is produced from the
objective's landscape:

  1. Ensemble phase: 40 restarts x 160,000 steps of
     simulated annealing with an enriched move set
     (admissible swaps with probability 0.7, admissible
     3-cycle rotations with probability 0.3, exact deltas
     throughout). Temperature: geometric 30 -> 0.05 over
     the first 80,000 steps, one reheat to 10 at step
     80,000, geometric 10 -> 0.05 over the second 80,000.
     Restart 0 is frequency-initialized; restarts 1..39
     are random admissible assignments. Each restart
     returns its best-visited state, swap-polished
     (steepest ascent over admissible swaps) to a local
     optimum.
  2. Candidate selection: the best polished state by
     objective — the Stage 1 selection rule, unchanged.
     What the revision changes is the search that produces
     the states the rule selects among.

Development history (filed in full at the amendment
record): two marginal-refinement forms were built and
measured on the Stage 1 corpora (seen material,
development only) and neither is carried into the
registered design. (a) Marginals from free-running
fixed-temperature chains (T* = 10) seeded at the best
polished states: the chains' wander diluted the optima
and cost recovery against the ensemble's own best state
on both smoke corpora (0.649 against 0.702; 0.772
against 0.807). (b) Per-sign modal aggregation over the
polished optima (elite band, top-10/12, all-40;
softmax-weighted and unweighted): the polished ensemble
concentrates in one basin family (elite-band pairwise
Hamming distance median 3-4 signs), so every aggregation
probed returned the argmax state itself — identical
recovery in all 11 aggregation cells across replications
2, 3, and 5 — while the ensemble's own spread showed the
objective ranking among near-optima is uncorrelated
with recovery at this resolution (replication 2's
ranks 5-7 by objective recover 0.842 against ranks
1-4's 0.772-0.789, and no selector over the ensemble
reaches them). The refinement stage the Stage 1 record
names was therefore evaluated and set aside on the
record, and the revision's claim is the narrower,
evidenced one: the enriched ensemble finds the basin
the filed search missed (replication 5: best polished
state 0.807, its objective 24.5 nats above the planted
truth's and alone in its 50-nat band, where the filed
search's best was 0.614 at 497.7 nats below truth).

Rationale (diagnosis at the amendment record): recovery
is a per-sign criterion, and the Stage 1 anatomy showed
the objective's near-optimal plateau is wide in exactly
the per-sign directions recovery counts — the filed
best states beat the planted truth's objective by
+26..+50 nats on four corpora while missing 10-17 signs,
almost all edge values, in short permutation cycles —
while the fifth corpus was a basin failure (best found
497.7 nats BELOW truth at a swap-local optimum). The
joint argmax is the wrong estimator for a per-sign
criterion and swap-only annealing cannot leave deep
local optima; G1-R therefore estimates per-sign marginal
modes over a Boltzmann ensemble of the SAME objective
(the refinement stage the Stage 1 record names) and
enriches the move set with the cycle moves the filed
error anatomy exhibits.

Internal gates: the 3-cycle delta is asserted against
full rescoring on 200 random triples before any run
(a disagreement is a STOP); every recovery figure is
computed by the Stage 1 harness's recovery_g1, which
asserts its own two implementations agree; every margin
figure by the Stage 1 scorers A/B in agreement.

No undeciphered-system output is produced or scored
anywhere in this run. Writes: raw-output JSON (argv[1]);
synthetic corpora and intermediates to custody (argv[2]).
"""
import hashlib
import importlib.util
import json
import math
import random
import sys
from collections import Counter
from datetime import datetime, timezone
from statistics import median

_spec = importlib.util.spec_from_file_location(
    "stage1_harness",
    "/home/tpierson/.syncyard/worktrees/glossa/spec109-g1rev-20261127/"
    "specs/109-generative-decipherment-engine/records/"
    "stage-1-preflight-harness.py")
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)

NV = H.NVAL
RECOVERY_FLOOR = 0.80
# ---- G1-R registered constants (amendment record) ----
RESTARTS = 40
STEPS = 160000
T_START, T_END = 30.0, 0.05
REHEAT_AT, REHEAT_T = 80000, 10.0
P_CYCLE = 0.3


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] S109-G1R {msg}", flush=True)


def sha(b):
    return hashlib.sha256(b).hexdigest()


# ------------------------------------------------- enriched moves
def cycle3_delta(S, I0, LW, LW0, phi, x, y, z, nphi):
    """Exact objective change when signs x, y, z take the new
    values nphi[x], nphi[y], nphi[z] (a rotation of their current
    values). Sums every term involving x, y, or z exactly once."""
    T = (x, y, z)
    old = new = 0.0
    for s in T:
        old += I0[s] * LW0[phi[s]]
        new += I0[s] * LW0[nphi[s]]
        lw_o, lw_n = LW[phi[s]], LW[nphi[s]]
        row = S[s]
        for b in range(NV):
            pb = phi[b]
            nb = nphi[b] if b in T else pb
            if row[b]:
                old += row[b] * lw_o[pb]
                new += row[b] * lw_n[nb]
    for a in range(NV):
        if a in T:
            continue
        pa = phi[a]
        lw = LW[pa]
        rowa = S[a]
        for s in T:
            if rowa[s]:
                old += rowa[s] * lw[phi[s]]
                new += rowa[s] * lw[nphi[s]]
    return new - old


def rotate(phi, x, y, z):
    psi = list(phi)
    psi[x], psi[y], psi[z] = phi[z], phi[x], phi[y]
    return psi


def _propose(rng, phi, admissible, fixed, free):
    """One proposal: (kind, payload, new_phi_or_None). Admissibility
    is checked on the rotated/swapped values."""
    if rng.random() < P_CYCLE:
        x, y, z = rng.sample(free, 3)
        vx, vy, vz = phi[x], phi[y], phi[z]
        if vz not in admissible[x] or vx not in admissible[y] \
                or vy not in admissible[z]:
            return None
        psi = rotate(phi, x, y, z)
        return ("cycle", (x, y, z), psi)
    x, y = rng.sample(free, 2)
    vx, vy = phi[x], phi[y]
    if vy not in admissible[x] or vx not in admissible[y]:
        return None
    psi = list(phi)
    psi[x], psi[y] = vy, vx
    return ("swap", (x, y), psi)


def _delta(S, I0, LW, LW0, phi, prop):
    kind, payload, psi = prop
    if kind == "swap":
        x, y = payload
        return H._swap_delta(S, I0, LW, LW0, phi, x, y)
    x, y, z = payload
    return cycle3_delta(S, I0, LW, LW0, phi, x, y, z, psi)


def anneal_rev(S, I0, LW, LW0, phi0, admissible, fixed, steps, seed):
    rng = random.Random(seed)
    phi = list(phi0)
    cur = H.objective(S, I0, LW, LW0, phi)
    best, best_phi = cur, list(phi)
    free = [s for s in range(NV) if s not in fixed]
    for step in range(steps):
        if step < REHEAT_AT:
            T = T_START * (T_END / T_START) ** (step / REHEAT_AT)
        else:
            T = REHEAT_T * (T_END / REHEAT_T) ** (
                (step - REHEAT_AT) / (steps - REHEAT_AT))
        prop = _propose(rng, phi, admissible, fixed, free)
        if prop is None:
            continue
        d = _delta(S, I0, LW, LW0, phi, prop)
        if d >= 0 or rng.random() < math.exp(d / T):
            phi = prop[2]
            cur += d
            if cur > best:
                best, best_phi = cur, list(phi)
    return best_phi, H.objective(S, I0, LW, LW0, best_phi)


def swap_polish(S, I0, LW, LW0, phi, admissible, fixed):
    phi = list(phi)
    free = [s for s in range(NV) if s not in fixed]
    while True:
        best_d, best_pair = 1e-9, None
        for i, x in enumerate(free):
            for y in free[i + 1:]:
                if phi[y] not in admissible[x] \
                        or phi[x] not in admissible[y]:
                    continue
                d = H._swap_delta(S, I0, LW, LW0, phi, x, y)
                if d > best_d:
                    best_d, best_pair = d, (x, y)
        if best_pair is None:
            return phi, H.objective(S, I0, LW, LW0, phi)
        x, y = best_pair
        phi[x], phi[y] = phi[y], phi[x]


def g1r_search(deriv, family, anchors_sign_value, det_init, det_final,
               seed_prefix):
    fam_w = H.weights_from(family)
    init_vals, fin_vals = H.family_positional(family)
    deriv_trunc = [H.truncate_numerals(g) for g in deriv]
    S, I0, LW, LW0 = H.build_objective(deriv_trunc, fam_w)
    admissible = {}
    for s in range(NV):
        adm = set(range(NV))
        if s in det_init:
            adm &= init_vals
        if s in det_final:
            adm &= fin_vals
        admissible[s] = adm if adm else set(range(NV))
    fixed = dict(anchors_sign_value)
    # ---- ensemble phase
    polished = []
    for r in range(RESTARTS):
        rng = random.Random(f"{seed_prefix}-init{r}")
        phi0 = H._initial_assignment(rng, fixed, admissible, deriv,
                                     family, freq_init=(r == 0))
        cand, _obj = anneal_rev(S, I0, LW, LW0, phi0, admissible, fixed,
                                STEPS, f"{seed_prefix}-restart{r}")
        pphi, pobj = swap_polish(S, I0, LW, LW0, cand, admissible, fixed)
        polished.append((pobj, pphi))
        if (r + 1) % 10 == 0:
            log(f"  ensemble {r + 1}/{RESTARTS} restarts polished "
                f"(best objective so far "
                f"{max(o for o, _p in polished):.1f})")
    polished.sort(key=lambda t: -t[0])
    cand, cobj = polished[0][1], polished[0][0]
    relaxed = [s for s in range(NV) if s not in fixed
               and admissible[s] == set(range(NV))
               and (s in det_init or s in det_final)]
    info = {"objective": cobj,
            "best_polished_objective": polished[0][0],
            "best_polished_phi": polished[0][1],
            "polished_objectives": [o for o, _p in polished],
            "relaxed": relaxed}
    return cand, info


def self_test_delta():
    """Internal gate: the 3-cycle delta against full rescoring on
    random states/triples; any disagreement is a STOP."""
    rng = random.Random("spec109-g1r-delta-selftest")
    fam = [[rng.randrange(NV) for _ in range(rng.randrange(2, 9))]
           for _ in range(300)]
    fam_w = H.weights_from(fam)
    deriv = [[rng.randrange(NV) for _ in range(rng.randrange(2, 9))]
             for _ in range(300)]
    S, I0, LW, LW0 = H.build_objective(deriv, fam_w)
    phi = list(range(NV))
    rng.shuffle(phi)
    base = H.objective(S, I0, LW, LW0, phi)
    for _ in range(200):
        x, y, z = rng.sample(range(NV), 3)
        psi = rotate(phi, x, y, z)
        d = cycle3_delta(S, I0, LW, LW0, phi, x, y, z, psi)
        exact = H.objective(S, I0, LW, LW0, psi) - base
        assert abs(d - exact) < 1e-9, (d, exact)
    log("delta self-test: 200/200 3-cycle deltas agree with full "
        "rescoring")


def main():
    out_path, custody_dir = sys.argv[1], sys.argv[2]
    seed_ns = sys.argv[3] if len(sys.argv) > 3 else "spec109-s1r-synth"
    reps = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    only_reps = None
    if len(sys.argv) > 5 and sys.argv[5] != "-":
        only_reps = [int(x) for x in sys.argv[5].split(",")]
    search_only = len(sys.argv) > 6 and sys.argv[6] == "search-only"
    stage1_path = _spec.origin
    with open(stage1_path, "rb") as f:
        stage1_sha = sha(f.read())
    log(f"G1-R preflight: seed namespace {seed_ns}; Stage 1 harness "
        f"SHA-256 {stage1_sha}")
    self_test_delta()
    lengths = H.indus_lengths()
    results = {"design": "G1-R (amendment registration 2026-11-27)",
               "seed_namespace": seed_ns,
               "stage1_harness_sha256": stage1_sha,
               "constants": {
                   "restarts": RESTARTS, "steps": STEPS,
                   "t_start": T_START, "t_end": T_END,
                   "reheat_at": REHEAT_AT, "reheat_t": REHEAT_T,
                   "p_cycle": P_CYCLE},
               "replications": []}
    for rep in range(1, reps + 1):
        if only_reps is not None and rep not in only_reps:
            continue
        # admission gates identical to the Stage 1 harness
        seed = None
        for attempt in range(50):
            cand_seed = (f"{seed_ns}-{rep}" if attempt == 0
                         else f"{seed_ns}-{rep}-try{attempt}")
            corp = H.build_corpus(cand_seed, lengths)
            signseqs = corp["signseqs"]
            truth = corp["truth"]
            perm = truth["perm_value_to_sign"]
            if sorted(len(s) for s in signseqs) != sorted(lengths):
                continue
            _d, _r, n_try = H.split_corpus(signseqs)
            if n_try != H.N_ART - H.N_DUP:
                continue
            if H.truth_restricted_a(truth, perm) != \
                    H.truth_restricted_b(signseqs, perm):
                continue
            tc_try = Counter(m for g in signseqs for m in g)
            if any(tc_try[s] < 5 for s in range(NV)):
                continue
            seed = cand_seed
            break
        assert seed is not None, f"no admissible corpus for rep {rep}"
        deriv, reserve, n_distinct = H.split_corpus(signseqs)
        token_counts = Counter(m for g in signseqs for m in g)
        anchors_sv = {perm[v]: v for v in truth["anchors"]}
        row = {"rep": rep, "seed": seed, "distinct": n_distinct,
               "derivation_sequences": len(deriv),
               "reserve_sequences": len(reserve),
               "reserve_tokens": sum(len(g) for g in reserve)}
        pos_deriv = H.positional_counts(deriv)
        det = H.detect_restricted(pos_deriv, 0.95)
        det_init = {s for s, c in det.items() if c == "initial"}
        det_final = {s for s, c in det.items() if c == "final"}
        log(f"rep {rep}: G1-R search (seed {seed})")
        phi, info = g1r_search(deriv, corp["family"], anchors_sv,
                               det_init, det_final, seed + "-g1r")
        row["g1_recovery"] = H.recovery_g1(phi, perm, set(anchors_sv),
                                           token_counts)
        row["g1_candidate_phi"] = phi
        row["g1_info"] = {k: v for k, v in info.items()
                          if k != "best_polished_phi"}
        row["g1_best_polished_phi"] = info["best_polished_phi"]
        row["g1_best_polished_recovery"] = H.recovery_g1(
            info["best_polished_phi"], perm, set(anchors_sv),
            token_counts)
        log(f"rep {rep}: candidate recovery "
            f"{row['g1_recovery']['recovery']:.3f} "
            f"({row['g1_recovery']['hits']}/"
            f"{row['g1_recovery']['denominator']}); best polished state "
            f"{row['g1_best_polished_recovery']['recovery']:.3f}")
        if search_only:
            row["g1_shuffle_recovery"] = None
            row["g1_margin"] = None
            results["replications"].append(row)
            with open(f"{custody_dir}/synth-rep{rep}.json", "w") as f:
                json.dump({"seed": seed, "signseqs": signseqs,
                           "bounds": [sorted(b) for b in corp["bounds"]],
                           "sites": [corp["sites"][i]
                                     for i in range(H.N_ART)],
                           "family": corp["family"], "truth": truth,
                           "counted_slots": corp["counted_slots"]}, f)
            log(f"rep {rep}: complete (search-only dev mode)")
            continue
        # shuffle control: identical revised pipeline on the
        # shuffled derivation (Stage 1's control construction)
        rng_s2 = random.Random(seed + "-g1shuffle")
        shuf_deriv = []
        for g in deriv:
            gg = list(g)
            rng_s2.shuffle(gg)
            shuf_deriv.append(gg)
        pos_sh = H.positional_counts(shuf_deriv)
        det_sh = H.detect_restricted(pos_sh, 0.95)
        log(f"rep {rep}: G1-R shuffle control")
        phi_sh, _info_sh = g1r_search(
            shuf_deriv, corp["family"], anchors_sv,
            {s for s, c in det_sh.items() if c == "initial"},
            {s for s, c in det_sh.items() if c == "final"},
            seed + "-g1rshuf")
        row["g1_shuffle_recovery"] = H.recovery_g1(
            phi_sh, perm, set(anchors_sv), token_counts)
        log(f"rep {rep}: shuffle recovery "
            f"{row['g1_shuffle_recovery']['recovery']:.3f}")
        # margins and null (Stage 1 code, unchanged)
        rng_der = random.Random(seed + "-derange")
        der = list(range(NV))
        while True:
            rng_der.shuffle(der)
            if all(der[v] != v for v in range(NV)):
                break
        inv = [0] * NV
        for v, s in enumerate(perm):
            inv[s] = v
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
        p99, _dist = H.g1_null(corp["family"], reserve, phi, anchors_sv,
                               best_rival_total, n_free, seed + "-null")
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
                                 for i in range(H.N_ART)],
                       "family": corp["family"], "truth": truth,
                       "counted_slots": corp["counted_slots"]}, f)
        log(f"rep {rep}: complete ({len(results['replications'])} "
            f"replications filed)")
    recs = [r["g1_recovery"]["recovery"] for r in results["replications"]]
    shufs = [r["g1_shuffle_recovery"]["recovery"]
             for r in results["replications"]
             if r["g1_shuffle_recovery"] is not None]
    summary = {
        "g1_recovery_median": median(recs) if recs else None,
        "g1_recoveries": recs,
        "g1_shuffle_recovery_median": median(shufs) if shufs else None,
        "g1_margin_pass_reps": sum(1 for r in results["replications"]
                                   if r["g1_margin"] and r["g1_margin"]["pass"]),
        "g1_penalized_median": median(
            [r["g1_margin"]["penalized_margin"]
             for r in results["replications"]
             if r["g1_margin"]]) if recs else None}
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
    results["summary"] = summary
    with open(out_path, "w") as f:
        json.dump(results, f, indent=1)
    log(f"verdicts: {json.dumps(summary['verdicts'])}; median recovery "
        f"{summary['g1_recovery_median']}")
    log(f"raw output written to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
