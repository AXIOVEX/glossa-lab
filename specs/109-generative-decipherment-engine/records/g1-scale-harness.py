#!/usr/bin/env python3
"""Spec 109 — G1 identifiability-scale study harness (T103).

Executes the study registered at
specs/109-generative-decipherment-engine/records/
g1-scale-registration-2026-11-27.md: the G1-R preflight —
generator, objective, admissibility, scoring, floors, and
clause structure IDENTICAL to the G1 revision amendment
(records/g1-revision-registration-2026-11-27.md) — run on
fresh synthetic Indus-profile corpora at scale 2x and 4x,
five replications each, to decide between the two live
explanations of G1-R's clause (i) failure at 1x: (A)
information (identifiability rises with corpus scale) and
(B) objective design (it does not). The decision rule is
registered in the amendment at section 5, before any run.

Scale enters ONLY through corpus construction, exactly as
the amendment registers: the Stage 1 harness's own
Language and build_corpus code (pin SHA-256 f4e84285...)
executed from a source in which five textual
substitutions carry the scale definition — N_ART =
1670k, N_DUP = 20k, the counted-slot cap 60k, the
stem-pool targets in their saturation form ((2, 529),
(3, 100k)): a length-2 stem is a pair of the 23 stem
values, so 529 is the inventory maximum and the scaled
pool saturates there — and the rejection loop's
cap-exhaustion raise replaced by the registered
fallback acceptance (distinct length-2 sequences are
capped at 529 while length-2 demand is 269k, so the
filed distinctness gate is combinatorially
unattainable at scale; the fallback slot is recorded
in FALLBACK_SLOTS, its count F and the measured
distinct count and effective scale are filed per
corpus, and a fallback at any length other than 2 is
a STOP). Each substitution target is asserted to
occur exactly once in the filed source before
replacement; a failed assertion is a STOP. The family
corpus stays at 4,000 sequences (the frozen
predictor's value-side reference). The search is
the filed G1 revision harness's code (pin SHA-256
a15c8c57...), loaded with its Stage 1 import directed at
this worktree's byte-identical copy of the filed Stage 1
harness; the pin is asserted before any run. The search
budget is the registered G1-R budget at every scale.

Per replication the raw output files: recovery (the
Stage 1 harness's recovery_g1, two implementations in
asserted agreement), the shuffle-control recovery, the
penalized margin and null 99th percentile (Stage 1
scorers), the candidate's objective and the planted
truth's objective under the identical objective
construction and their difference, and the miss anatomy
over the scored signs (stems vs openers / closers /
context / affixes), computed here from the custody
truth.

No undeciphered-system output is produced or scored
anywhere in this run. Writes: raw-output JSON (argv[1]);
synthetic corpora to custody (argv[2]). Usage:
g1-scale-harness.py OUT CUSTODY_DIR SEED_NS SCALE_K
"""
import hashlib
import importlib.util
import json
import random
import sys
import types
from collections import Counter
from datetime import datetime, timezone
from statistics import median

WT = ("/home/tpierson/.syncyard/worktrees/glossa/"
      "spec109-scale-wt-20261127")
RECORDS = (WT + "/specs/109-generative-decipherment-engine/records")
STAGE1_PATH = RECORDS + "/stage-1-preflight-harness.py"
G1R_PATH = RECORDS + "/g1-revision-harness.py"
AMENDMENT_PATH = RECORDS + "/g1-scale-registration-2026-11-27.md"
STAGE1_SHA = ("f4e84285d38f39f25d46547d9d435a32ad46506513b588ae061"
              "be7a974bc3485")
G1R_SHA = ("a15c8c578b0599b3ab6b44564361d191b8375028fbb43ee3ad6e0"
           "a6f63cdb15a")
RECOVERY_FLOOR = 0.80


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] S109-G1SCALE {msg}", flush=True)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---- pins first: any mismatch is a STOP before any build
with open(STAGE1_PATH, "rb") as f:
    stage1_src = f.read()
assert sha(stage1_src) == STAGE1_SHA, "Stage 1 harness pin mismatch"
with open(G1R_PATH, "rb") as f:
    g1r_src = f.read()
assert sha(g1r_src) == G1R_SHA, "G1 revision harness pin mismatch"
with open(AMENDMENT_PATH, "rb") as f:
    amendment_sha = sha(f.read())
with open(__file__, "rb") as f:
    self_sha = sha(f.read())

H = load_module("stage1_harness", STAGE1_PATH)
NV = H.NVAL


def load_scaled_stage1(k):
    """The filed Stage 1 source with the amendment's five
    registered scale substitutions; each target asserted to
    occur exactly once."""
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
            f"target {old!r} occurs {src.count(old)} times, " \
            f"expected 1"
        src = src.replace(old, new)
    mod = types.ModuleType(f"stage1_scaled_{k}x")
    exec(compile(src, f"stage-1-preflight-harness.py[scale-{k}x]",
                 "exec"), mod.__dict__)
    assert mod.N_ART == 1670 * k and mod.N_DUP == 20 * k
    mod.FALLBACK_SLOTS = []
    return mod


def load_g1r():
    """The filed G1 revision harness, its Stage 1 import
    directed at this worktree's byte-identical copy."""
    src = g1r_src.decode()
    old_prefix = ("/home/tpierson/.syncyard/worktrees/glossa/"
                  "spec109-g1rev-20261127/")
    assert src.count(old_prefix) == 1
    src = src.replace(old_prefix, WT + "/")
    mod = types.ModuleType("g1r_harness")
    exec(compile(src, "g1-revision-harness.py", "exec"),
         mod.__dict__)
    with open(mod._spec.origin, "rb") as f:
        assert sha(f.read()) == STAGE1_SHA, \
            "the revision harness loaded a Stage 1 file off pin"
    return mod


def anatomy(phi, perm, truth, anchors_signs, token_counts):
    """Miss anatomy over the scored signs (the recovery
    denominator's set), classified by the planted value's
    role. The role partition is exact: openers, closers,
    context, and affix values are disjoint planted sets;
    every remaining value is a stem value."""
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


def main():
    out_path, custody_dir = sys.argv[1], sys.argv[2]
    seed_ns = sys.argv[3]
    k = int(sys.argv[4])
    reps = 5
    log(f"scale study: k={k}, seed namespace {seed_ns}; "
        f"Stage 1 harness SHA-256 {STAGE1_SHA[:12]}...; "
        f"G1-R harness SHA-256 {G1R_SHA[:12]}...; amendment "
        f"SHA-256 {amendment_sha[:12]}...")
    HK = load_scaled_stage1(k)
    R = load_g1r()
    assert (R.RESTARTS, R.STEPS, R.T_START, R.T_END, R.REHEAT_AT,
            R.REHEAT_T, R.P_CYCLE) == (40, 160000, 30.0, 0.05,
                                       80000, 10.0, 0.3), \
        "G1-R constants differ from the amendment registration"
    R.self_test_delta()
    lengths = H.indus_lengths() * k
    assert len(lengths) == 1670 * k and sum(lengths) == 7002 * k
    results = {"study": "Spec 109 G1 identifiability-scale "
                        "study (T103)",
               "scale": k,
               "seed_namespace": seed_ns,
               "stage1_harness_sha256": STAGE1_SHA,
               "g1r_harness_sha256": G1R_SHA,
               "scale_harness_sha256": self_sha,
               "amendment_registration_sha256": amendment_sha,
               "profile": {"artifacts": 1670 * k,
                           "tokens": 7002 * k,
                           "duplicates": 20 * k,
                           "distinct_at_1x_form": 1650 * k,
                           "counted_slots": 60 * k,
                           "stem_pools": {"2": min(300 * k, 529),
                                          "3": 100 * k},
                           "family_sequences": 4000},
               "constants": {"restarts": R.RESTARTS,
                             "steps": R.STEPS,
                             "t_start": R.T_START,
                             "t_end": R.T_END,
                             "reheat_at": R.REHEAT_AT,
                             "reheat_t": R.REHEAT_T,
                             "p_cycle": R.P_CYCLE},
               "replications": []}
    for rep in range(1, reps + 1):
        # admission gates identical in form to the G1-R
        # harness, in their scale form (amendment section 3)
        seed = None
        fallbacks = None
        for attempt in range(50):
            cand_seed = (f"{seed_ns}-{rep}" if attempt == 0
                         else f"{seed_ns}-{rep}-try{attempt}")
            HK.FALLBACK_SLOTS = []
            corp = HK.build_corpus(cand_seed, lengths)
            fb = list(HK.FALLBACK_SLOTS)
            # a fallback at any length other than 2 falsifies
            # the amendment's filed combinatorics: STOP
            assert all(lengths[i] == 2 for i in fb), \
                f"fallback at a non-length-2 slot in rep {rep}"
            signseqs = corp["signseqs"]
            truth = corp["truth"]
            perm = truth["perm_value_to_sign"]
            if sorted(len(s) for s in signseqs) != sorted(lengths):
                continue
            if H.truth_restricted_a(truth, perm) != \
                    H.truth_restricted_b(signseqs, perm):
                continue
            tc_try = Counter(m for g in signseqs for m in g)
            if any(tc_try[s] < 5 for s in range(NV)):
                continue
            seed = cand_seed
            fallbacks = fb
            break
        assert seed is not None, f"no admissible corpus for rep {rep}"
        deriv, reserve, n_distinct = HK.split_corpus(signseqs)
        token_counts = Counter(m for g in signseqs for m in g)
        anchors_sv = {perm[v]: v for v in truth["anchors"]}
        row = {"rep": rep, "seed": seed, "distinct": n_distinct,
               "fallback_slots": len(fallbacks),
               "effective_scale": n_distinct / 1650,
               "derivation_sequences": len(deriv),
               "reserve_sequences": len(reserve),
               "reserve_tokens": sum(len(g) for g in reserve)}
        log(f"k={k} rep {rep}: corpus admitted (seed {seed}); "
            f"distinct {n_distinct}, fallbacks "
            f"{len(fallbacks)}, effective scale "
            f"{n_distinct / 1650:.3f}x")
        pos_deriv = H.positional_counts(deriv)
        det = H.detect_restricted(pos_deriv, 0.95)
        det_init = {s for s, c in det.items() if c == "initial"}
        det_final = {s for s, c in det.items() if c == "final"}
        log(f"k={k} rep {rep}: G1-R search (seed {seed})")
        phi, info = R.g1r_search(deriv, corp["family"], anchors_sv,
                                 det_init, det_final, seed + "-g1r")
        row["g1_recovery"] = H.recovery_g1(phi, perm,
                                           set(anchors_sv),
                                           token_counts)
        row["g1_candidate_phi"] = phi
        row["g1_info"] = {kk: v for kk, v in info.items()
                          if kk != "best_polished_phi"}
        row["g1_best_polished_phi"] = info["best_polished_phi"]
        row["g1_best_polished_recovery"] = H.recovery_g1(
            info["best_polished_phi"], perm, set(anchors_sv),
            token_counts)
        # objective gap: the planted truth scored under the
        # identical objective construction (amendment sec. 4)
        fam_w = H.weights_from(corp["family"])
        deriv_trunc = [H.truncate_numerals(g) for g in deriv]
        S, I0, LW, LW0 = H.build_objective(deriv_trunc, fam_w)
        truth_phi = [0] * NV
        for v, s in enumerate(perm):
            truth_phi[s] = v
        truth_obj = H.objective(S, I0, LW, LW0, truth_phi)
        row["objective_gap"] = {
            "candidate": info["objective"],
            "planted_truth": truth_obj,
            "gap": info["objective"] - truth_obj}
        row["anatomy"] = anatomy(phi, perm, truth,
                                 set(anchors_sv), token_counts)
        log(f"k={k} rep {rep}: candidate recovery "
            f"{row['g1_recovery']['recovery']:.3f} "
            f"({row['g1_recovery']['hits']}/"
            f"{row['g1_recovery']['denominator']}); objective "
            f"gap {row['objective_gap']['gap']:+.1f} nats; "
            f"misses {row['anatomy']['misses']} "
            f"(stems {row['anatomy']['by_role']['stems']})")
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
        log(f"k={k} rep {rep}: G1-R shuffle control")
        phi_sh, _info_sh = R.g1r_search(
            shuf_deriv, corp["family"], anchors_sv,
            {s for s, c in det_sh.items() if c == "initial"},
            {s for s, c in det_sh.items() if c == "final"},
            seed + "-g1rshuf")
        row["g1_shuffle_recovery"] = H.recovery_g1(
            phi_sh, perm, set(anchors_sv), token_counts)
        log(f"k={k} rep {rep}: shuffle recovery "
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
        p99, _dist = H.g1_null(corp["family"], reserve, phi,
                               anchors_sv, best_rival_total, n_free,
                               seed + "-null")
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
                                 for i in range(HK.N_ART)],
                       "family": corp["family"], "truth": truth,
                       "counted_slots": corp["counted_slots"]}, f)
        log(f"k={k} rep {rep}: complete "
            f"({len(results['replications'])} replications filed)")
    recs = [r["g1_recovery"]["recovery"]
            for r in results["replications"]]
    shufs = [r["g1_shuffle_recovery"]["recovery"]
             for r in results["replications"]]
    summary = {
        "g1_recovery_median": median(recs),
        "g1_recoveries": recs,
        "g1_shuffle_recovery_median": median(shufs),
        "g1_margin_pass_reps": sum(1 for r in results["replications"]
                                   if r["g1_margin"]["pass"]),
        "g1_penalized_median": median(
            [r["g1_margin"]["penalized_margin"]
             for r in results["replications"]]),
        "objective_gaps": [r["objective_gap"]["gap"]
                           for r in results["replications"]],
        "stem_misses_per_rep": [r["anatomy"]["by_role"]["stems"]
                                for r in results["replications"]],
        "effective_scale_median": median(
            [r["effective_scale"] for r in results["replications"]]),
        "anatomy_intact": all(
            r["anatomy"]["by_role"]["stems"] == 0
            for r in results["replications"])}
    ctrl = summary["g1_shuffle_recovery_median"] \
        < 0.5 * summary["g1_recovery_median"]
    summary["clause_i_at_scale"] = bool(
        summary["g1_recovery_median"] >= RECOVERY_FLOOR)
    summary["clause_ii_margin"] = summary["g1_margin_pass_reps"] >= 3
    summary["shuffle_control"] = bool(ctrl)
    results["summary"] = summary
    with open(out_path, "w") as f:
        json.dump(results, f, indent=1)
    log(f"k={k}: median recovery "
        f"{summary['g1_recovery_median']:.3f}; anatomy intact "
        f"{summary['anatomy_intact']}; shuffle control "
        f"{summary['shuffle_control']}; clause (ii) "
        f"{summary['clause_ii_margin']}")
    log(f"raw output written to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
