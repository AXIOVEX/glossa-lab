#!/usr/bin/env python3
"""TC-109-02 re-run — G1 identifiability-scale study verification
(Spec 109; TC-109-02 is registered "re-run for each later
generator", and the scale amendment's section 8 files this
script as the independent recomputation of the study's
figures).

Recomputes, from the custody corpora and the study runs' raw
outputs, every figure the scale study record files, and
evaluates the amendment's section 5 decision rule
mechanically over the recomputed figures. Independence: the
recovery figures and the miss anatomies are recomputed by
this script's own code from the filed candidate assignments
(not by the harness's functions); the margins and the null
are recomputed from the filed assignments through the Stage
1 harness's scorers (whose two implementations assert
agreement per figure, as in Stage 1); each candidate's
objective and the planted truth's objective are rescored
from the filed assignments under the Stage 1 objective
construction; the two ground-truth constructions are the
Stage 1 harness's independent pair, as in every preflight
of this study.

Usage: g1-scale-tc109-02-verification.py RECORDS_DIR \
    CUSTODY_2X_DIR CUSTODY_4X_DIR RESULT_JSON
"""
import hashlib
import importlib.util
import json
import random
import sys
from collections import Counter
from statistics import median

RECORDS, CUST2, CUST4, RESULT = sys.argv[1:5]
spec = importlib.util.spec_from_file_location(
    "h", f"{RECORDS}/stage-1-preflight-harness.py")
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
NV = h.NVAL

checks = []


def check(name, ok, detail=""):
    checks.append({"check": name, "pass": bool(ok),
                   "detail": detail})
    print(("PASS " if ok else "FAIL ") + name
          + (" — " + detail if detail else ""), flush=True)


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def own_recovery(phi, perm, anchors_signs, token_counts):
    inv = {}
    for v, s in enumerate(perm):
        inv[s] = v
    scored = [s for s in range(NV)
              if s not in anchors_signs and token_counts[s] >= 5]
    hits = sum(1 for s in scored if phi[s] == inv[s])
    return hits, len(scored)


def own_anatomy(phi, perm, truth, anchors_signs, token_counts):
    inv = {}
    for v, s in enumerate(perm):
        inv[s] = v
    affix = (set(truth["p1"]) | set(truth["p2"])
             | set(truth["s1"]) | set(truth["s2"]))
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
        elif v in truth["openers"]:
            by_role["openers"] += 1
        elif v in truth["closers"]:
            by_role["closers"] += 1
        elif v in truth["ctx"]:
            by_role["context"] += 1
        else:
            by_role["stems"] += 1
    return {"misses": misses, "by_role": by_role}


def verify_scale(cust, k):
    raw = json.load(open(f"{cust}/raw-output.json"))
    tag = f"{k}x"
    check(f"{tag}: stage-1 harness pin matches the filed "
          f"Stage 1 harness",
          raw["stage1_harness_sha256"]
          == sha256(f"{RECORDS}/stage-1-preflight-harness.py"),
          raw["stage1_harness_sha256"][:12])
    check(f"{tag}: G1-R harness pin matches the filed "
          f"revision harness",
          raw["g1r_harness_sha256"]
          == sha256(f"{RECORDS}/g1-revision-harness.py"),
          raw["g1r_harness_sha256"][:12])
    check(f"{tag}: scale harness pin matches the filed "
          f"scale harness",
          raw["scale_harness_sha256"]
          == sha256(f"{RECORDS}/g1-scale-harness.py"),
          raw["scale_harness_sha256"][:12])
    check(f"{tag}: amendment pin matches the filed scale "
          f"registration",
          raw["amendment_registration_sha256"] == sha256(
              f"{RECORDS}/g1-scale-registration-2026-11-27.md"),
          raw["amendment_registration_sha256"][:12])
    check(f"{tag}: seed namespace is the registered fresh "
          f"namespace",
          raw["seed_namespace"] == f"spec109-scl{k}-synth",
          raw["seed_namespace"])
    check(f"{tag}: profile block states scale {k}",
          raw["scale"] == k
          and raw["profile"]["artifacts"] == 1670 * k
          and raw["profile"]["tokens"] == 7002 * k)
    recs, shufs, pens = [], [], []
    for row in raw["replications"]:
        rep = row["rep"]
        corp = json.load(open(f"{cust}/synth-rep{rep}.json"))
        signseqs, truth = corp["signseqs"], corp["truth"]
        perm = truth["perm_value_to_sign"]
        check(f"{tag} rep {rep}: seed of record matches "
              f"custody", corp["seed"] == row["seed"],
              row["seed"])
        check(f"{tag} rep {rep}: profile recomputes "
              f"({1670*k} artifacts / {7002*k} tokens / "
              f"{60*k} counted / family 4000)",
              len(signseqs) == 1670 * k
              and sum(len(g) for g in signseqs) == 7002 * k
              and len(corp["counted_slots"]) == 60 * k
              and len(corp["family"]) == 4000)
        deriv, reserve, n_distinct = h.split_corpus(signseqs)
        check(f"{tag} rep {rep}: distinct and effective "
              f"scale recompute",
              n_distinct == row["distinct"]
              and abs(row["effective_scale"]
                      - n_distinct / 1650) < 1e-12,
              f"distinct {n_distinct}, effective "
              f"{n_distinct/1650:.3f}x")
        len2_slots = sum(1 for g in signseqs if len(g) == 2)
        len2_distinct = len({tuple(g) for g in signseqs
                             if len(g) == 2})
        check(f"{tag} rep {rep}: fallback count at or above "
              f"the combinatorial floor, length-2 distinct "
              f"within the 529 cap",
              row["fallback_slots"] >= 269 * k - 529
              and len2_distinct <= 529
              and len2_slots == 269 * k,
              f"F {row['fallback_slots']} (floor "
              f"{269*k-529}), len-2 distinct {len2_distinct}")
        check(f"{tag} rep {rep}: two ground-truth "
              f"constructions agree",
              h.truth_restricted_a(truth, perm)
              == h.truth_restricted_b(signseqs, perm))
        token_counts = Counter(m for g in signseqs for m in g)
        anchors_sv = {perm[v]: v for v in truth["anchors"]}
        phi = row["g1_candidate_phi"]
        check(f"{tag} rep {rep}: candidate is a permutation "
              f"of the 60 values respecting the anchors",
              sorted(phi) == list(range(NV))
              and all(phi[s] == v for s, v in anchors_sv.items()))
        hits, denom = own_recovery(phi, perm, set(anchors_sv),
                                   token_counts)
        check(f"{tag} rep {rep}: recovery recomputes by "
              f"own code",
              hits == row["g1_recovery"]["hits"]
              and denom == row["g1_recovery"]["denominator"]
              and denom == 57,
              f"{hits}/{denom}")
        ana = own_anatomy(phi, perm, truth, set(anchors_sv),
                          token_counts)
        check(f"{tag} rep {rep}: miss anatomy recomputes "
              f"by own code", ana == row["anatomy"],
              f"misses {ana['misses']}, stems "
              f"{ana['by_role']['stems']}")
        fam_w = h.weights_from(corp["family"])
        deriv_trunc = [h.truncate_numerals(g) for g in deriv]
        S, I0, LW, LW0 = h.build_objective(deriv_trunc, fam_w)
        cand_obj = h.objective(S, I0, LW, LW0, phi)
        truth_phi = [0] * NV
        for v, s in enumerate(perm):
            truth_phi[s] = v
        truth_obj = h.objective(S, I0, LW, LW0, truth_phi)
        check(f"{tag} rep {rep}: candidate and truth "
              f"objectives rescore; gap recomputes",
              abs(cand_obj - row["objective_gap"]["candidate"])
              < 1e-6
              and abs(truth_obj
                      - row["objective_gap"]["planted_truth"])
              < 1e-6
              and abs((cand_obj - truth_obj)
                      - row["objective_gap"]["gap"]) < 1e-6,
              f"gap {cand_obj - truth_obj:+.1f}")
        rng_der = random.Random(row["seed"] + "-derange")
        der = list(range(NV))
        while True:
            rng_der.shuffle(der)
            if all(der[v] != v for v in range(NV)):
                break
        inv = [0] * NV
        for v, s in enumerate(perm):
            inv[s] = v
        phi_wrong = [der[inv[s]] for s in range(NV)]
        rng_sa = random.Random(row["seed"] + "-shufassign")
        free_signs = [s for s in range(NV) if s not in anchors_sv]
        sa_vals = [phi[s] for s in free_signs]
        rng_sa.shuffle(sa_vals)
        phi_shuffle = list(phi)
        for s, v in zip(free_signs, sa_vals):
            phi_shuffle[s] = v
        mg = h.g1_margins(corp["family"], reserve, phi,
                          phi_wrong, phi_shuffle)
        n_free = NV - len(anchors_sv)
        penalized = mg["margin_raw"] - 2 * n_free
        p99, _dist = h.g1_null(corp["family"], reserve, phi,
                               anchors_sv,
                               min(mg["rivals"].values()),
                               n_free, row["seed"] + "-null")
        check(f"{tag} rep {rep}: penalized margin and null "
              f"p99 recompute",
              abs(penalized
                  - row["g1_margin"]["penalized_margin"]) < 1e-6
              and abs(p99 - row["g1_margin"]["null_p99"]) < 1e-9
              and row["g1_margin"]["pass"]
              == bool(penalized >= 10 and penalized > p99),
              f"penalized {penalized:.1f}, p99 {p99:.1f}")
        recs.append(row["g1_recovery"]["recovery"])
        shufs.append(row["g1_shuffle_recovery"]["recovery"])
        pens.append(row["g1_margin"]["penalized_margin"])
    summ = raw["summary"]
    check(f"{tag}: summary medians recompute from the "
          f"per-replication figures",
          abs(summ["g1_recovery_median"] - median(recs)) < 1e-12
          and abs(summ["g1_shuffle_recovery_median"]
                  - median(shufs)) < 1e-12
          and abs(summ["g1_penalized_median"] - median(pens))
          < 1e-9)
    check(f"{tag}: summary clause flags are the registered "
          f"forms over the recomputed figures",
          summ["clause_i_at_scale"]
          == bool(median(recs) >= 0.80)
          and summ["clause_ii_margin"]
          == bool(summ["g1_margin_pass_reps"] >= 3)
          and summ["shuffle_control"]
          == bool(median(shufs) < 0.5 * median(recs))
          and summ["anatomy_intact"]
          == all(r["anatomy"]["by_role"]["stems"] == 0
                 for r in raw["replications"]))
    check(f"{tag}: no undeciphered-system output exists "
          f"in the raw output (synthetic namespaces only)",
          raw["seed_namespace"].startswith("spec109-scl"))
    return summ


s2 = verify_scale(CUST2, 2)
s4 = verify_scale(CUST4, 4)

# the amendment's section 5 decision rule, evaluated
# mechanically over the verified summaries
med2 = s2["g1_recovery_median"]
med4 = s4["g1_recovery_median"]
if not s2["shuffle_control"] or not s4["shuffle_control"]:
    outcome = "MIXED (shuffle control failed; the affected " \
              "scale's figure is void)"
elif med4 >= 0.80 and s4["anatomy_intact"]:
    outcome = "A SUPPORTED"
elif med4 < 0.80 and med2 < 0.80:
    outcome = "B SUPPORTED"
elif med2 >= 0.80 and med4 < 0.80:
    outcome = "MIXED (crossing at 2x but not 4x)"
elif med4 >= 0.80 and not s4["anatomy_intact"]:
    outcome = "MIXED (anatomy changed character at 4x)"
else:
    outcome = "MIXED (unclassified by the registered table)"
check("decision rule (amendment section 5) evaluated over "
      "the verified medians", True,
      f"2x median {med2:.3f}, 4x median {med4:.3f}, "
      f"4x anatomy intact {s4['anatomy_intact']}, shuffle "
      f"2x {s2['shuffle_control']}, 4x "
      f"{s4['shuffle_control']} -> {outcome}")

n_pass = sum(1 for c in checks if c["pass"])
result = {"test_case": "TC-109-02 (scale study re-run form)",
          "checks": checks,
          "passed": n_pass, "total": len(checks),
          "decision_outcome": outcome,
          "verdict": "PASS" if n_pass == len(checks) else "FAIL"}
with open(RESULT, "w") as f:
    json.dump(result, f, indent=1)
print(f"TC-109-02 scale verification: {n_pass}/{len(checks)} "
      f"checks PASS; decision: {outcome}")
sys.exit(0 if n_pass == len(checks) else 1)
