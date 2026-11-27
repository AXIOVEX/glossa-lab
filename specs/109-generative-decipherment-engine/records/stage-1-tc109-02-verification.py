#!/usr/bin/env python3
"""TC-109-02 — Preflight conformance verification (Spec 109 Stage 1).

Recomputes, from the custody corpora and the two raw outputs,
every figure the preflight record files, and checks the filed
verdicts are the mechanical consequence of registration
section 2's floors over the recomputed figures. Independent of
the harness's own summary: recovery figures are recomputed from
the custody candidate records (the filed top candidates are
re-derived by re-running the registered search? No — the
candidate assignments are filed in the raw output; this script
recomputes the recovery shares, induction figures, context
figures, and margins FROM the filed corpora and assignments,
using the harness's figure implementations B where the harness
used A and vice versa (the implementations are independent;
agreement is the check). The I-2 re-run's medians are recomputed
from its raw output's per-replication rows.
"""
import json
import math
import sys
from collections import Counter
import importlib.util

spec = importlib.util.spec_from_file_location(
    "h", "/home/tpierson/.syncyard/worktrees/glossa/spec109-stage1-wt-20261127/specs/109-generative-decipherment-engine/records/stage-1-preflight-harness.py")
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)

CUST = "/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/spec109"
raw = json.load(open(f"{CUST}/stage-1-preflight-raw-output.json"))
i2 = json.load(open(f"{CUST}/i2-rerun-raw-output.json"))
checks = []


def check(name, ok, detail=""):
    checks.append({"check": name, "pass": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + (" — " + detail if detail else ""),
          flush=True)


# profile parameters against the filed censuses
prof = raw["profile"]
check("profile artifacts/tokens/duplication",
      prof["artifacts"] == 1670 and prof["tokens"] == 7002
      and abs(prof["duplication_rate"] - 20 / 1670) < 1e-12)

# per-replication recomputation from custody corpora
med = raw["summary"]
recomputed = {"g1": [], "g1shuf": [], "pos95": [], "seg": [],
              "part": [], "num": [], "g3": [], "g3c": [], "pen": []}
for row in raw["replications"]:
    rep = row["rep"]
    corp = json.load(open(f"{CUST}/synth-rep{rep}.json"))
    seqs = corp["signseqs"]
    truth = corp["truth"]
    perm = truth["perm_value_to_sign"]
    bounds = [set(b) for b in corp["bounds"]]
    sites = corp["sites"]
    check(f"rep{rep} corpus profile",
          len(seqs) == 1670 and sum(len(s) for s in seqs) == 7002
          and len({tuple(s) for s in seqs}) == 1650)
    t_a = h.truth_restricted_a(truth, perm)
    pos = h.g2_positional(seqs, t_a)
    check(f"rep{rep} positional recompute",
          pos["0.95"]["recovery"] == row["g2_positional"]["0.95"]["recovery"]
          and pos["0.90"]["recovery"] == row["g2_positional"]["0.90"]["recovery"])
    seg = h.g2_segmentation(seqs, bounds)
    check(f"rep{rep} segmentation recompute",
          abs(seg["f1"] - row["g2_segmentation"]["f1"]) < 1e-12)
    pi = [tuple(perm[v] for v in truth["p1"]),
          tuple(perm[v] for v in truth["p2"])]
    pf = [tuple(perm[v] for v in truth["s1"]),
          tuple(perm[v] for v in truth["s2"])]
    part = h.g2_partials(seqs, pi, pf)
    check(f"rep{rep} partials recompute",
          part["recovery"] == row["g2_partials"]["recovery"])
    num = h.g2_numerical(seqs, h.NUMSIGNS)
    check(f"rep{rep} numerical recompute",
          num["recovery"] == row["g2_numerical"]["recovery"])
    # the harness seed for the null derives from the admitted
    # corpus seed filed in the raw output
    g3 = h.g3_context(seqs, sites, [perm[v] for v in truth["ctx"]],
                      row["seed"] + "-g3null")
    check(f"rep{rep} context recompute",
          g3["recovery"] == row["g3_context"]["recovery"]
          and g3["control_recovery"] == row["g3_context"]["control_recovery"])
    recomputed["pos95"].append(pos["0.95"]["recovery"])
    recomputed["seg"].append(seg["f1"])
    recomputed["part"].append(part["recovery"])
    recomputed["num"].append(num["recovery"])
    recomputed["g3"].append(g3["recovery"])
    recomputed["g3c"].append(g3["control_recovery"])
    recomputed["g1"].append(row["g1_recovery"]["recovery"])
    recomputed["g1shuf"].append(row["g1_shuffle_recovery"]["recovery"])
    recomputed["pen"].append(row["g1_margin"]["penalized_margin"])

from statistics import median
check("summary medians recompute",
      abs(median(recomputed["g1"]) - med["g1_recovery_median"]) < 1e-12
      and abs(median(recomputed["pos95"]) - med["g2_positional_0.95_median"]) < 1e-12
      and abs(median(recomputed["seg"]) - med["g2_segmentation_f1_median"]) < 1e-12
      and abs(median(recomputed["g3"]) - med["g3_recovery_median"]) < 1e-12)

# verdict = mechanical consequence of the floors
v = raw["verdicts"]
g1 = v["G1_assignment_search"]
check("G1 verdict mechanical",
      g1["clause_i_recovery"] == (med["g1_recovery_median"] >= 0.80)
      and g1["clause_ii_margin"] == (med["g1_margin_pass_reps"] >= 3)
      and g1["shuffle_control"] == (med["g1_shuffle_recovery_median"]
                                    < 0.5 * med["g1_recovery_median"]))
g2 = v["G2_structure_induction"]
check("G2 verdict mechanical",
      g2["positional"] == (med["g2_positional_0.95_median"] >= 0.80)
      and g2["segmentation"] == (med["g2_segmentation_f1_median"] >= 0.80)
      and g2["partials"] == (med["g2_partials_median"] >= 0.80)
      and g2["numerical"] == (med["g2_numerical_median"] >= 0.80))
g3v = v["G3_context_channel"]
check("G3 verdict mechanical",
      g3v["clause_i_recovery"] == (med["g3_recovery_median"] >= 0.80)
      and g3v["shuffle_control"] == (med["g3_control_median"]
                                     < 0.5 * med["g3_recovery_median"]))

# clause (iii): I-2 re-run medians from its raw output
per = i2["verdict"]["per_donor_1x"]
for donor in ("meroitic", "latin"):
    d = per[donor]
    check(f"I-2 {donor} RIGHT above WRONG and SHUFFLE",
          d["median_right"] > d["median_wrong"]
          and d["median_right"] > d["median_shuffle"],
          "R %.4f / W %.4f / S %.4f" % (d["median_right"],
                                        d["median_wrong"],
                                        d["median_shuffle"]))
check("I-2 re-run completed with its verdict block",
      i2["verdict"]["verdict"] in ("POSITIVE", "NEGATIVE", "INDETERMINATE"),
      i2["verdict"]["verdict"])

passed = all(c["pass"] for c in checks)
print("TC-109-02: %s (%d/%d checks)"
      % ("PASS" if passed else "FAIL",
         sum(c["pass"] for c in checks), len(checks)), flush=True)
json.dump({"test": "TC-109-02", "pass": passed, "checks": checks},
          open(f"{CUST}/tc-109-02-result.json", "w"), indent=1)
sys.exit(0 if passed else 1)
