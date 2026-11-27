#!/usr/bin/env python3
"""TC-109-02 re-run — G1 revision preflight conformance verification
(Spec 109; TC-109-02 is registered "re-run for each later
generator").

Recomputes, from the custody corpora and the revision run's raw
output, every figure the G1 revision preflight record files, and
checks the filed verdict is the mechanical consequence of
registration section 2's floors over the recomputed figures.
Independence: the recovery figures are recomputed by this
script's own code from the filed candidate assignments (not by
the harness's recovery function); the margins and the null are
recomputed from the filed assignments through the Stage 1
harness's scorers (whose two implementations assert agreement
per figure, as in Stage 1); the candidate's objective is
rescored from its filed assignment and checked against the
filed ensemble record.

Usage: g1-revision-tc109-02-verification.py RECORDS_DIR CUSTODY_RUN_DIR
"""
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from statistics import median

RECORDS, CUST = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location(
    "h", f"{RECORDS}/stage-1-preflight-harness.py")
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
NV = h.NVAL

raw = json.load(open(f"{CUST}/raw-output.json"))
checks = []


def check(name, ok, detail=""):
    checks.append({"check": name, "pass": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + name
          + (" — " + detail if detail else ""), flush=True)


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


check("stage-1 harness pin matches the filed Stage 1 harness",
      raw["stage1_harness_sha256"]
      == sha256(f"{RECORDS}/stage-1-preflight-harness.py"),
      raw["stage1_harness_sha256"][:12])
check("seed namespace is the registered fresh namespace",
      raw["seed_namespace"] == "spec109-s1r-synth",
      raw["seed_namespace"])

recs, shufs, pens = [], [], []
for row in raw["replications"]:
    rep = row["rep"]
    corp = json.load(open(f"{CUST}/synth-rep{rep}.json"))
    seqs = [list(s) for s in corp["signseqs"]]
    truth = corp["truth"]
    perm = truth["perm_value_to_sign"]
    check(f"rep{rep} corpus profile",
          len(seqs) == 1670 and sum(len(s) for s in seqs) == 7002
          and len({tuple(s) for s in seqs}) == 1650)
    check(f"rep{rep} seed of record matches custody",
          corp["seed"] == row["seed"], row["seed"])
    t_a = h.truth_restricted_a(truth, perm)
    t_b = h.truth_restricted_b(seqs, perm)
    check(f"rep{rep} ground-truth constructions agree", t_a == t_b)
    deriv, reserve, _nd = h.split_corpus(seqs)
    token_counts = Counter(m for g in seqs for m in g)
    anchors_sv = {perm[v]: v for v in truth["anchors"]}
    inv = [0] * NV
    for v, s in enumerate(perm):
        inv[s] = v
    phi = row["g1_candidate_phi"]
    check(f"rep{rep} candidate is an admissible-form assignment",
          sorted(phi) == list(range(NV))
          and all(phi[s] == v for s, v in anchors_sv.items()))
    check(f"rep{rep} candidate is the filed best polished state",
          phi == row["g1_best_polished_phi"])
    # independent recovery recomputation (this script's own code)
    hits = denom = 0
    for s in range(NV):
        if s in anchors_sv or token_counts[s] < 5:
            continue
        denom += 1
        if phi[s] == inv[s]:
            hits += 1
    rec = hits / denom
    check(f"rep{rep} recovery recomputes",
          hits == row["g1_recovery"]["hits"]
          and denom == row["g1_recovery"]["denominator"]
          and abs(rec - row["g1_recovery"]["recovery"]) < 1e-12,
          f"{hits}/{denom}")
    # candidate objective rescored from the filed assignment
    fam_w = h.weights_from(corp["family"])
    deriv_trunc = [h.truncate_numerals(g) for g in deriv]
    S, I0, LW, LW0 = h.build_objective(deriv_trunc, fam_w)
    obj = h.objective(S, I0, LW, LW0, phi)
    check(f"rep{rep} candidate objective recomputes",
          abs(obj - row["g1_info"]["objective"]) < 1e-6
          and abs(obj - row["g1_info"]["best_polished_objective"]) < 1e-6,
          f"{obj:.1f}")
    # margins and null recomputed from the filed assignment
    import random
    rng_der = random.Random(row["seed"] + "-derange")
    der = list(range(NV))
    while True:
        rng_der.shuffle(der)
        if all(der[v] != v for v in range(NV)):
            break
    phi_wrong = [der[inv[s]] for s in range(NV)]
    rng_sa = random.Random(row["seed"] + "-shufassign")
    free_signs = [s for s in range(NV) if s not in anchors_sv]
    sa_vals = [phi[s] for s in free_signs]
    rng_sa.shuffle(sa_vals)
    phi_shuffle = list(phi)
    for s, v in zip(free_signs, sa_vals):
        phi_shuffle[s] = v
    mg = h.g1_margins(corp["family"], reserve, phi, phi_wrong,
                      phi_shuffle)
    n_free = NV - len(anchors_sv)
    penalized = mg["margin_raw"] - 2 * n_free
    p99, _d = h.g1_null(corp["family"], reserve, phi, anchors_sv,
                        min(mg["rivals"].values()), n_free,
                        row["seed"] + "-null")
    check(f"rep{rep} margin and null recompute",
          abs(penalized - row["g1_margin"]["penalized_margin"]) < 1e-6
          and abs(p99 - row["g1_margin"]["null_p99"]) < 1e-6
          and row["g1_margin"]["pass"]
          == bool(penalized >= 10 and penalized > p99),
          f"penalized {penalized:.1f}, p99 {p99:.1f}")
    recs.append(rec)
    shufs.append(row["g1_shuffle_recovery"]["recovery"])
    pens.append(penalized)

summ = raw["summary"]
check("summary medians recompute",
      abs(median(recs) - summ["g1_recovery_median"]) < 1e-12
      and abs(median(shufs) - summ["g1_shuffle_recovery_median"]) < 1e-12
      and abs(median(pens) - summ["g1_penalized_median"]) < 1e-6)
v = summ["verdicts"]
check("verdict is the mechanical consequence of the floors",
      v["clause_i_recovery"] == (median(recs) >= 0.80)
      and v["clause_ii_margin"] == (summ["g1_margin_pass_reps"] >= 3)
      and v["shuffle_control"]
      == (median(shufs) < 0.5 * median(recs))
      and v["verdict"] == ("PASSED" if (v["clause_i_recovery"]
                                        and v["clause_ii_margin"]
                                        and v["shuffle_control"])
                           else "FAILED"),
      v["verdict"])
check("no undeciphered-system output in the run's raw output",
      set(raw.keys()) == {"design", "seed_namespace",
                          "stage1_harness_sha256", "constants",
                          "replications", "summary"})

passed = all(c["pass"] for c in checks)
print("TC-109-02 (G1 revision): %s (%d/%d checks)"
      % ("PASS" if passed else "FAIL",
         sum(c["pass"] for c in checks), len(checks)), flush=True)
json.dump({"test": "TC-109-02", "scope": "G1 revision re-preflight",
           "pass": passed, "checks": checks},
          open(f"{CUST}/tc-109-02-result.json", "w"), indent=1)
sys.exit(0 if passed else 1)
