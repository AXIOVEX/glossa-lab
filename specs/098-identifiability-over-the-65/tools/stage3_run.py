#!/usr/bin/env python3
"""Spec 098 Stage 3 runner: T301 — the scoring run (the seal
opened once).

Run on tower-compute from the Stage 3 worker clone, under
freeze v1, the execution freeze annex (estimator), and the
Stage 2 freeze. Modes:

  prepare — development-side only. Verifies the corpus pin,
            reproduces the frozen split and the seal hash from
            the split rule (the custody file is NOT read),
            reproduces the Stage 1 grid for the executed
            population of 69, runs the TC-098-01 guard over the
            development export, cross-checks the free-choice
            accounting against the Stage 2 outcome data, builds
            the candidate and rival context models for the nine
            sheeted signs on development data, computes the
            M089 development co-occurrence counts (prerequisite
            check), and smoke-tests the estimator by scoring
            development occurrences (executability only; no
            held-out material is touched and no margin from
            this mode is evidence).
  release — the single recorded release of the held-out list.
            Reads the custody file, verifies its seal hash and
            count against the committed seal record and against
            the recomputed split, and writes the release log.
            Refuses to run if a release log already exists:
            the release happens exactly once.
  score   — the scoring run. Requires the release log;
            re-verifies the seal from the custody list at
            scoring time (a mismatch voids the run: SEAL
            FAILURE, no per-sign outcomes); establishes the
            actual held-out counts for all 69 signs (decision
            rule 1's binding count test); scores every sign
            with an accepted prediction sheet whose actual
            count meets the frozen floor, under the frozen
            estimator (execution freeze annex: order-1
            neighbour-pair contexts, add-0.1 smoothing over
            the sign's development context vocabulary plus one
            unseen bucket); computes the frozen permutation
            null (B = 999, seed 9801) and the inscription-
            cluster bootstrap interval (B = 999, seed 9802);
            scores the R-E global permutation as one model;
            and assembles every sign's outcome under spec
            section 4 precedence via the reference decide()
            rule in tools/seal_and_score.py.
  verify  — recomputes every outcome from the archived raw
            scoring output via decide() and compares.

Encoding decisions (recorded in
records/stage-3-prerelease-2026-11-22.md before the release;
each is the mechanical reading of the frozen texts):

- Signatures are the Stage 2 prediction sheets' own words,
  encoded as neighbour-identity conditions (SIGNATURES below,
  each with its sheet citation). "Immediate neighbours
  include X" / "drawn from {set}" (the record does not split
  by side): at least one neighbour in the set. Side-specific
  signatures (M267): both stated sides must meet their sets
  (the filed pattern is the conjunction [AGENT]-M267-[TITLE]).
  Single-side (M375): that side must meet its set.
- Per-sign rivals take the unconditioned assignment (Stage 2
  freeze section 6): every per-sign rival's context model is
  therefore the sign's unconditioned development model, and
  the best rival is that model. Per-rival log-likelihoods are
  recorded individually; their identity is the section 6
  rule, not a computation shortcut.
- Permutation null: the null permutes value assignments over
  the sign's held-out occurrences (execution freeze annex).
  For the paired per-occurrence log-likelihood differences
  d_i = log P_candidate(c_i) - log P_rival(c_i), a permuted
  assignment credits each occurrence's difference to either
  side at random: null margins are sum_i eps_i * d_i with
  eps_i iid Rademacher, drawn from a fresh random.Random(9801)
  stream per sign, replicate-major, occurrence order as
  collected (sorted cluster id, then sequence position).
  Percentiles use linear interpolation on the sorted
  replicates (the numpy 'linear' convention).
- Bootstrap: inscription-cluster bootstrap over the clusters
  carrying the sign's held-out occurrences (resampled with
  replacement, fresh random.Random(9802) stream per sign);
  the reported interval is the 2.5th-97.5th percentile band
  of the penalized margin (the penalty is constant across
  replicates, so the band is the raw band shifted by it).
- R-E is scored as one model: each sign's held-out
  occurrences are scored under the model its received value
  induces — the signature of the value's own sign where that
  sign carries an accepted sheet, the unconditioned model
  otherwise (a value with no stated signature for the sign
  takes the unconditioned assignment). The candidate system
  is scored identically with each sign's own value. Totals
  are over all 69 signs; the free-choice multiset is the
  same in both systems, so penalties cancel in the
  difference and raw totals are reported.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC_DIR = HERE.parent
REPO = SPEC_DIR.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO / "backend"))

from seal_and_score import (  # noqa: E402
    decide,
    development_export,
    seal_hash,
    split_clusters,
    verify_seal,
)
from stage1_run import clusters, load_records, sign_tokens  # noqa: E402
from stage2_run import executed_population, free_choices  # noqa: E402

SEAL_SHA256 = "1974d83a5f667b71dbd53ecdb2e42a8221c6d4b91bdd32202b2a80579bf96cf9"
SEAL_HELD_COUNT = 517
SEAL_CLUSTERS = 2413
ALPHA = 0.1
NULL_B = 999
NULL_SEED = 9801
BOOT_B = 999
BOOT_SEED = 9802
FLOOR = 5

CUSTODY = Path.home() / "glossa-custody/spec098/heldout-clusters-v1.txt"
RUNS_DIR = Path.home() / "glossa-work/s098-stage3-runs"
RELEASE_LOG = RUNS_DIR / "release-log.json"
GRID = SPEC_DIR / "records/stage1-grid-2026-11-21.json"
STAGE2_OUTCOME = SPEC_DIR / "records/stage-2-outcome-2026-11-22.json"
STAGE2_RIVALS = SPEC_DIR / "records/stage-2-rivals-2026-11-22.json"
OUTCOME_JSON = SPEC_DIR / "records/stage-3-outcome-2026-11-22.json"

BOS = "BOS"
EOS = "EOS"

# The nine accepted prediction sheets (Stage 2 determinations),
# encoded from the sheets' own words. Forms:
#   ("any", {signs})            — at least one neighbour in the set
#   ("sides", {left}, {right})  — left in left-set AND right in right-set
#   ("right", {signs})          — right neighbour in the set
SIGNATURES = {
    "M005": (("any", frozenset({"M342"})),
             "sheet: 'immediate neighbours include M342' (filed collocation, n=4)"),
    "M030": (("any", frozenset({"M342"})),
             "sheet: 'immediate neighbours include M342' (filed collocation, n=4)"),
    "M037": (("any", frozenset({"M267"})),
             "sheet: 'immediate neighbours include M267' (filed collocation, n=4)"),
    "M068": (("any", frozenset({"M342"})),
             "sheet: 'immediate neighbours include M342' (filed collocation, n=4)"),
    "M075": (("any", frozenset({"M267"})),
             "sheet: 'immediate neighbours include M267' (filed collocation, n=4)"),
    "M089": (("any", frozenset({"M342", "M267", "M176"})),
             "sheet: 'immediate neighbours drawn from {M342, M267, M176}; "
             "the record does not split the set by side'"),
    "M267": (("sides", frozenset({"M176", "M328"}), frozenset({"M099", "M073"})),
             "sheet: 'immediate left neighbours include M176 and M328 and its "
             "immediate right neighbours include M099 and M073' (filed slot "
             "pattern [AGENT]-M267-[TITLE], read strictly as sign identities)"),
    "M347": (("any", frozenset({"M342", "M293", "M028", "M367", "M211", "M099"})),
             "sheet: 'immediate neighbours drawn from {M342, M293, M028, M367, "
             "M211, M099}; the record does not split the set by side'"),
    "M375": (("right", frozenset({"M342"})),
             "sheet: 'an immediate right neighbour: M342' (filed sequence "
             "pattern [M375]-M342-M176)"),
}


def run_id(mode: str) -> str:
    now = datetime.now(timezone.utc)
    suffix = hashlib.sha256(
        f"{now.isoformat()}:{mode}".encode()).hexdigest()[:6]
    return f"study-{now.strftime('%Y%m%dT%H%M%SZ')}-{suffix}"


def contexts_of(toks, sign):
    """(left, right) neighbour contexts of every occurrence of
    sign in one sequence, BOS/EOS sentinels at the ends
    (execution freeze annex section 3)."""
    out = []
    for i, t in enumerate(toks):
        if t == sign:
            left = toks[i - 1] if i > 0 else BOS
            right = toks[i + 1] if i + 1 < len(toks) else EOS
            out.append((left, right))
    return out


def meets(sig, ctx):
    kind = sig[0]
    left, right = ctx
    if kind == "any":
        return left in sig[1] or right in sig[1]
    if kind == "right":
        return right in sig[1]
    if kind == "sides":
        return left in sig[1] and right in sig[2]
    raise ValueError(kind)


def build_model(dev_ctxs, sig):
    """The frozen estimator (execution freeze annex section 3):
    add-ALPHA smoothing over the sign's development context
    vocabulary V plus one unseen bucket. sig=None is the
    unconditioned assignment (all development occurrences)."""
    vocab = set(dev_ctxs)
    if sig is None:
        assigned = list(dev_ctxs)
    else:
        assigned = [c for c in dev_ctxs if meets(sig, c)]
    counts = Counter(assigned)
    n = len(assigned)
    denom = n + ALPHA * (len(vocab) + 1)
    return {"vocab": vocab, "counts": counts, "n": n, "denom": denom,
            "assigned": assigned}


def logp(model, ctx):
    if ctx in model["vocab"]:
        num = model["counts"].get(ctx, 0) + ALPHA
    else:
        num = ALPHA  # the unseen-context bucket
    return math.log(num / model["denom"])


def pct(sorted_vals, p):
    """Percentile with linear interpolation (numpy 'linear')."""
    n = len(sorted_vals)
    if n == 1:
        return sorted_vals[0]
    rank = (p / 100.0) * (n - 1)
    lo = int(math.floor(rank))
    frac = rank - lo
    if lo + 1 >= n:
        return sorted_vals[-1]
    return sorted_vals[lo] + frac * (sorted_vals[lo + 1] - sorted_vals[lo])


def load_all():
    records = load_records()  # asserts the corpus SHA pin
    cl = clusters(records)
    ids = sorted(cl)
    dev_ids, held_ids = split_clusters(ids)
    return records, cl, ids, dev_ids, held_ids


def dev_contexts(cl, dev_ids, pop):
    per_sign = {}
    for r in pop:
        per_sign[r["sign"]] = []
    devset = set(dev_ids)
    for cid in sorted(devset):
        toks = sign_tokens(cl[cid])
        present = set(toks)
        for s in present:
            if s in per_sign:
                per_sign[s].extend(contexts_of(toks, s))
    return per_sign


def mode_prepare():
    rid = run_id("prepare")
    records, cl, ids, dev_ids, held_ids = load_all()
    pop = executed_population()
    checks = {}
    checks["clusters"] = len(ids)
    checks["seal_recomputed_ok"] = (
        seal_hash(held_ids) == SEAL_SHA256
        and len(held_ids) == SEAL_HELD_COUNT
        and len(ids) == SEAL_CLUSTERS)
    rows = [{"cluster_id": cid, "glossa_id": cl[cid]["glossa_id"]}
            for cid in dev_ids]
    guard = development_export(rows, held_ids)  # raises on leak
    checks["guard_rows_passed"] = len(guard)
    grid = {g["sign"]: g for g in
            json.loads(GRID.read_text(encoding="utf-8"))["grid"]}
    devc = dev_contexts(cl, dev_ids, pop)
    grid_ok = True
    for r in pop:
        s = r["sign"]
        if grid.get(s, {}).get("dev_tokens") != len(devc[s]):
            grid_ok = False
    checks["grid_reproduced"] = grid_ok
    s2 = json.loads(STAGE2_OUTCOME.read_text(encoding="utf-8"))["outcomes"]
    fc = free_choices(pop)
    checks["free_choices_match_stage2"] = all(
        fc[s]["total"] == s2[s]["free_choices"]["total"] for s in fc)
    # Model construction + executability smoke test (dev-side).
    models = {}
    smoke_ok = True
    for s, (sig, _cite) in SIGNATURES.items():
        cand = build_model(devc[s], sig)
        unc = build_model(devc[s], None)
        ll_c = sum(logp(cand, c) for c in devc[s])
        ll_u = sum(logp(unc, c) for c in devc[s])
        if not (math.isfinite(ll_c) and math.isfinite(ll_u)):
            smoke_ok = False
        models[s] = {"vocab_size": len(cand["vocab"]),
                     "n_unconditioned": unc["n"],
                     "n_candidate_assigned": cand["n"]}
    checks["smoke_ok"] = smoke_ok
    # M089 prerequisite: development co-occurrence counts with
    # each sheet partner, computed fresh from the corpus of
    # record (development clusters only).
    m089 = {}
    for partner in ("M342", "M267", "M176"):
        m089[partner] = sum(
            1 for c in devc["M089"] if partner in c)
    m089["assigned_total"] = models["M089"]["n_candidate_assigned"]
    # M267 signature anatomy on development data.
    sig267 = SIGNATURES["M267"][0]
    left_ok = sum(1 for c in devc["M267"] if c[0] in sig267[1])
    right_ok = sum(1 for c in devc["M267"] if c[1] in sig267[2])
    m267 = {"dev_occurrences": len(devc["M267"]),
            "left_set_matches": left_ok,
            "right_set_matches": right_ok,
            "both_sides_assigned": models["M267"]["n_candidate_assigned"]}
    ok = all([checks["seal_recomputed_ok"], checks["grid_reproduced"],
              checks["free_choices_match_stage2"], checks["smoke_ok"],
              checks["clusters"] == SEAL_CLUSTERS])
    print(f"run_id={rid} mode=prepare")
    print(f"checks: {json.dumps(checks, ensure_ascii=False)}")
    print(f"models: {json.dumps(models, ensure_ascii=False)}")
    print(f"m089_dev_cooccurrence: {json.dumps(m089)}")
    print(f"m267_dev_signature_anatomy: {json.dumps(m267)}")
    print(f"PAYLOAD VERDICT T301-PREPARE: corpus_pin=True "
          f"seal_recompute_ok={checks['seal_recomputed_ok']} "
          f"grid_reproduced={checks['grid_reproduced']} "
          f"guard_pass=True free_choices_match="
          f"{checks['free_choices_match_stage2']} models_built=9 "
          f"smoke_ok={smoke_ok} custody_read=False")
    return 0 if ok else 1


def read_custody():
    ids = [l.strip() for l in
           CUSTODY.read_text(encoding="utf-8").splitlines() if l.strip()]
    return ids


def mode_release():
    rid = run_id("release")
    if RELEASE_LOG.exists():
        print(f"run_id={rid} mode=release REFUSED: a release log "
              f"already exists at {RELEASE_LOG}; the held-out list "
              f"is released exactly once.")
        print("PAYLOAD VERDICT T301-RELEASE: released=False "
              "reason=already-released")
        return 1
    custody_ids = read_custody()
    ok_seal = verify_seal(custody_ids, SEAL_SHA256)
    _records, _cl, _ids, _dev, held_recomputed = load_all()
    ok_set = sorted(custody_ids) == sorted(held_recomputed)
    ok = ok_seal and len(custody_ids) == SEAL_HELD_COUNT and ok_set
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO,
                          capture_output=True, text=True).stdout.strip()
    log = {
        "run_id": rid,
        "released_at_utc": datetime.now(timezone.utc).isoformat(),
        "custody_path": str(CUSTODY),
        "held_out_clusters": len(custody_ids),
        "seal_sha256": SEAL_SHA256,
        "seal_verify_at_release": ok_seal,
        "custody_set_equals_recomputed_split": ok_set,
        "worker_clone_head_at_release": head,
        "release_rule": "freeze v1 section 3: the held-out list is "
                        "released to the scoring path exactly once, "
                        "at scoring, and the release is recorded",
    }
    if ok:
        RUNS_DIR.mkdir(parents=True, exist_ok=True)
        (RUNS_DIR / f"{rid}-release.json").write_text(
            json.dumps(log, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8")
        RELEASE_LOG.write_text(
            json.dumps(log, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8")
    print(f"run_id={rid} mode=release")
    print(json.dumps(log, ensure_ascii=False))
    print(f"PAYLOAD VERDICT T301-RELEASE: released={ok} "
          f"seal_verify={ok_seal} held={len(custody_ids)} "
          f"set_equals_recomputed={ok_set}")
    return 0 if ok else 1


def held_contexts(cl, held_ids, pop):
    """Held-out occurrences per sign, with their cluster ids.
    Order: sorted cluster id, then sequence position."""
    per_sign = {}
    for r in pop:
        per_sign[r["sign"]] = []
    heldset = set(held_ids)
    for cid in sorted(heldset):
        toks = sign_tokens(cl[cid])
        for s in set(toks):
            if s in per_sign:
                for ctx in contexts_of(toks, s):
                    per_sign[s].append({"cluster": cid, "context": ctx})
    return per_sign


def score_sign(sign, devc, held_occ, sig, fc_cand):
    cand = build_model(devc, sig)
    unc = build_model(devc, None)
    ctxs = [o["context"] for o in held_occ]
    d = [logp(cand, c) - logp(unc, c) for c in ctxs]
    ll_cand = sum(logp(cand, c) for c in ctxs)
    ll_riv = sum(logp(unc, c) for c in ctxs)
    raw_margin = ll_cand - ll_riv
    pen_margin = raw_margin - 2.0 * fc_cand  # rivals carry 0 choices
    # Permutation null: sign-flip permutation of the per-occurrence
    # differences (frozen seed, fresh stream per sign).
    rng = random.Random(NULL_SEED)
    null_margins = []
    for _b in range(NULL_B):
        m = 0.0
        for di in d:
            m += di if rng.random() < 0.5 else -di
        null_margins.append(m)
    null_margins.sort()
    null_p99 = pct(null_margins, 99)
    # Inscription-cluster bootstrap of the penalized margin.
    by_cluster = defaultdict(float)
    for o, di in zip(held_occ, d):
        by_cluster[o["cluster"]] += di
    cluster_sums = [by_cluster[c] for c in sorted(by_cluster)]
    rng_b = random.Random(BOOT_SEED)
    boot = []
    for _b in range(BOOT_B):
        tot = 0.0
        for _i in range(len(cluster_sums)):
            tot += cluster_sums[rng_b.randrange(len(cluster_sums))]
        boot.append(tot - 2.0 * fc_cand)
    boot.sort()
    outcome = decide(
        heldout_tokens=len(ctxs),
        ll_candidate=ll_cand,
        ll_best_rival=ll_riv,
        null_p99=null_p99,
        candidate_free_choices=fc_cand,
        rival_free_choices=0,
        prediction_sheet_accepted=True,
        genuine_holdout=False,
    )
    return {
        "heldout_tokens": len(ctxs),
        "heldout_clusters_with_sign": len(cluster_sums),
        "vocab_size": len(cand["vocab"]),
        "n_candidate_assigned_dev": cand["n"],
        "n_unconditioned_dev": unc["n"],
        "ll_candidate": ll_cand,
        "ll_best_rival": ll_riv,
        "raw_margin_nats": raw_margin,
        "penalized_margin_nats": pen_margin,
        "effect_size_nats_per_token": pen_margin / len(ctxs),
        "null_p99_nats": null_p99,
        "bootstrap_ci95_penalized_margin": [pct(boot, 2.5), pct(boot, 97.5)],
        "outcome": outcome,
    }


def mode_score():
    rid = run_id("score")
    if not RELEASE_LOG.exists():
        print(f"run_id={rid} mode=score REFUSED: no release log; "
              f"the seal has not been released.")
        print("PAYLOAD VERDICT T301-SCORE: scored=False "
              "reason=no-release")
        return 1
    release = json.loads(RELEASE_LOG.read_text(encoding="utf-8"))
    custody_ids = read_custody()
    # The seal must recompute at scoring time (freeze v1 s.3).
    if not verify_seal(custody_ids, SEAL_SHA256) \
            or len(custody_ids) != SEAL_HELD_COUNT:
        print(f"run_id={rid} mode=score SEAL FAILURE: the custody "
              f"list does not recompute against the committed seal "
              f"at scoring time; the run is void, no per-sign "
              f"outcomes.")
        print("PAYLOAD VERDICT T301-SCORE: scored=False "
              "reason=seal-failure")
        return 1
    records, cl, ids, dev_ids, held_recomputed = load_all()
    if sorted(custody_ids) != sorted(held_recomputed):
        print(f"run_id={rid} mode=score SEAL FAILURE: the custody "
              f"list differs from the recomputed frozen split.")
        print("PAYLOAD VERDICT T301-SCORE: scored=False "
              "reason=seal-failure")
        return 1
    pop = executed_population()
    fc = free_choices(pop)
    s2 = json.loads(STAGE2_OUTCOME.read_text(encoding="utf-8"))["outcomes"]
    rivals_data = json.loads(STAGE2_RIVALS.read_text(encoding="utf-8"))
    devc = dev_contexts(cl, dev_ids, pop)
    heldc = held_contexts(cl, custody_ids, pop)

    outcomes = {}
    scored = {}
    for r in pop:
        s = r["sign"]
        n_held = len(heldc[s])
        threshold = 10.0 + 2.0 * fc[s]["total"]
        row = {
            "sign": s, "arm": r["arm"],
            "candidate_value": r["value"],
            "dedr_as_recorded": r["dedr"],
            "free_choices": fc[s],
            "threshold_nats_vs_zero_choice_rival": threshold,
            "dev_tokens": len(devc[s]),
            "expected_heldout_tokens": s2[s]["expected_heldout_tokens"],
            "heldout_tokens_actual": n_held,
            "min_detectable_margin_nats_per_token_at_actual_count":
                (round(threshold / n_held, 3) if n_held > 0 else None),
            "sheet": s2[s]["sheet"],
            "stage2_outcome": s2[s]["stage2_outcome"],
        }
        if s in SIGNATURES and n_held >= FLOOR:
            res = score_sign(s, devc[s], heldc[s], SIGNATURES[s][0],
                             fc[s]["total"])
            row.update(res)
            row["margin_note"] = "computed at Stage 3 under the seal's single recorded release"
            row["rival_ll_note"] = (
                "every per-sign rival takes the unconditioned "
                "assignment (Stage 2 freeze section 6); ll_best_rival "
                "is that model's total and is each per-sign rival's "
                "total (R-A, R-B, R-C, R-D and any Arm E additions)")
            row["stage3_outcome"] = res["outcome"]
            scored[s] = res
        elif s in SIGNATURES:
            row["stage3_outcome"] = decide(
                heldout_tokens=n_held, ll_candidate=0.0,
                ll_best_rival=0.0, null_p99=0.0,
                prediction_sheet_accepted=True)
            row["outcome_basis"] = (
                "decision rule 1, count arm, on actual held-out "
                "counts: fewer than 5 held-out tokens; the accepted "
                "sheet does not govern and no margin is computed "
                "(Stage 2 freeze section 6 precedence)")
            row["margin_nats"] = None
            row["margin_note"] = "not computed — decision rule 1 fires on the actual count"
        else:
            row["stage3_outcome"] = decide(
                heldout_tokens=n_held, ll_candidate=0.0,
                ll_best_rival=0.0, null_p99=0.0,
                prediction_sheet_accepted=False)
            if n_held < FLOOR:
                row["outcome_basis"] = (
                    "decision rule 1, count arm, on actual held-out "
                    "counts: fewer than 5 held-out tokens"
                    + ("; frozen default (T102) confirmed by the "
                       "count test" if s == "M374" else ""))
            else:
                row["outcome_basis"] = (
                    "decision rule 2, sheet arm: no accepted "
                    "prediction sheet — NOT IDENTIFIABLE by "
                    "construction (spec 3.5, claim C098-4); the "
                    "count test does not fire rule 1 at the actual "
                    "count")
            row["margin_nats"] = None
            row["margin_note"] = "not computed — no accepted prediction sheet"
        outcomes[s] = row

    # R-E, scored as one model (Stage 2 freeze section 5).
    permutation = rivals_data["global_permutation_R-E"]
    tot_cand = 0.0
    tot_perm = 0.0
    tot_unc = 0.0
    per_sign_re = {}
    for r in pop:
        s = r["sign"]
        unc = build_model(devc[s], None)
        own_sig = SIGNATURES[s][0] if s in SIGNATURES else None
        cand_model = build_model(devc[s], own_sig) \
            if own_sig is not None else unc
        donor = permutation[s]["from_sign"]
        donor_sig = SIGNATURES[donor][0] if donor in SIGNATURES else None
        perm_model = build_model(devc[s], donor_sig) \
            if donor_sig is not None else unc
        ctxs = [o["context"] for o in heldc[s]]
        ll_o = sum(logp(cand_model, c) for c in ctxs)
        ll_p = sum(logp(perm_model, c) for c in ctxs)
        ll_u = sum(logp(unc, c) for c in ctxs)
        tot_cand += ll_o
        tot_perm += ll_p
        tot_unc += ll_u
        if own_sig is not None or donor_sig is not None:
            per_sign_re[s] = {
                "donor": donor,
                "ll_candidate_system": ll_o,
                "ll_permuted_system": ll_p,
                "ll_unconditioned": ll_u,
            }
    r_e = {
        "construction": "one model (Stage 2 freeze section 5): each "
                        "sign scored under the model its received "
                        "value induces; penalties cancel (the "
                        "free-choice multiset is unchanged by the "
                        "permutation)",
        "ll_candidate_system_total": tot_cand,
        "ll_permuted_system_total": tot_perm,
        "ll_unconditioned_system_total": tot_unc,
        "system_margin_candidate_minus_permuted_nats": tot_cand - tot_perm,
        "per_sign_contributions_where_models_differ": per_sign_re,
    }

    distribution = dict(Counter(o["stage3_outcome"]
                                for o in outcomes.values()))
    data = {
        "stage": "Spec 098 Stage 3, T301 (scoring; the seal opened once)",
        "run_id": rid,
        "scored_at_utc": datetime.now(timezone.utc).isoformat(),
        "population_count": len(pop),
        "multiplicity_family": len(pop),
        "seal": {"sha256": SEAL_SHA256, "held_out_clusters": SEAL_HELD_COUNT,
                 "verified_at_scoring": True,
                 "release_run_id": release["run_id"],
                 "released_at_utc": release["released_at_utc"]},
        "distribution": distribution,
        "scored_signs": {s: scored[s] for s in scored},
        "r_e_model_level": r_e,
        "outcomes": outcomes,
    }
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = RUNS_DIR / f"{rid}-score-raw.json"
    raw_path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n",
                        encoding="utf-8")
    OUTCOME_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n",
                            encoding="utf-8")
    print(f"run_id={rid} mode=score")
    print(f"seal verified at scoring: True; release_run_id={release['run_id']}")
    for s in sorted(scored):
        r_ = scored[s]
        print(f"  {s}: held={r_['heldout_tokens']} "
              f"ll_cand={r_['ll_candidate']:.3f} "
              f"ll_riv={r_['ll_best_rival']:.3f} "
              f"pen_margin={r_['penalized_margin_nats']:.3f} "
              f"null_p99={r_['null_p99_nats']:.3f} "
              f"outcome={r_['outcome']}")
    print(f"distribution: {json.dumps(distribution)}")
    print(f"R-E: candidate={tot_cand:.3f} permuted={tot_perm:.3f} "
          f"unconditioned={tot_unc:.3f} margin={tot_cand - tot_perm:.3f}")
    print(f"raw output: {raw_path}")
    print(f"PAYLOAD VERDICT T301-SCORE: scored=True "
          f"signs_scored={len(scored)} "
          f"distribution={json.dumps(distribution)}")
    return 0


def mode_verify():
    data = json.loads(OUTCOME_JSON.read_text(encoding="utf-8"))
    bad = []
    for s, o in data["outcomes"].items():
        if "ll_candidate" in o:
            expect = decide(
                heldout_tokens=o["heldout_tokens_actual"],
                ll_candidate=o["ll_candidate"],
                ll_best_rival=o["ll_best_rival"],
                null_p99=o["null_p99_nats"],
                candidate_free_choices=o["free_choices"]["total"],
                rival_free_choices=0,
                prediction_sheet_accepted=True,
                genuine_holdout=False)
        else:
            expect = decide(
                heldout_tokens=o["heldout_tokens_actual"],
                ll_candidate=0.0, ll_best_rival=0.0, null_p99=0.0,
                prediction_sheet_accepted=(o["sheet"] == "ACCEPTED"))
        if expect != o["stage3_outcome"]:
            bad.append((s, expect, o["stage3_outcome"]))
    dist = dict(Counter(o["stage3_outcome"]
                        for o in data["outcomes"].values()))
    ok = not bad and dist == data["distribution"]
    print(f"verify: outcomes recomputed={len(data['outcomes'])} "
          f"mismatches={bad} distribution_match={dist == data['distribution']}")
    print(f"PAYLOAD VERDICT T301-VERIFY: verified={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "prepare"
    fn = {"prepare": mode_prepare, "release": mode_release,
          "score": mode_score, "verify": mode_verify}[mode]
    raise SystemExit(fn())
