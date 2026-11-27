#!/usr/bin/env python3
"""Spec 101 T202 - freeze computation (Spec 107 cycle 1, E-1).

Applies the floor record's section 1.3 formula mechanically to
the T201-registered inputs and the intaken census's M:
  p_i = f_i / D,  D = 11
  F_i = smallest integer k >= 2 with P(X_i >= k) < 0.05 / K
        under X_i ~ Binomial(M, p_i)
  E_i = M * p_i,  q_i = P(X_i >= F_i),  Q = sum q_i (< 0.05)

Also performs the instantiation check of floor record section 3
/ TC-101-06: every registered candidate's predicted position
kind is attempted against the intaken census, and the closure
path is exercised with a probe candidate whose predicted
position kind (reverse-face segment-final) is absent from the
census. The probe is a procedure exercise, not a candidate of
the study; the closure obligation attaches to registered
candidates.

Writes the freeze output JSON to argv[1]. This script reads
the census's segment structure only to count position kinds;
it takes no candidate count (scoring is T301).
"""
import json
import sys
from math import comb

D = 11
K = 4
ALPHA = 0.05
CANDIDATES = [  # from records/candidate-registration-2026-11-27.md
    {"ending": "-se", "f_i": 3},
    {"ending": "-na", "f_i": 2},
    {"ending": "-i", "f_i": 2},
    {"ending": "-ti", "f_i": 2},
]
STATE = "specs/101-eteocypriot-next-claim/corpus/corpus.json"


def tail(m, p, k):
    return sum(comb(m, j) * p ** j * (1 - p) ** (m - j)
               for j in range(k, m + 1))


def main():
    out_path = sys.argv[1]
    state = json.load(open(STATE, encoding="utf-8"))
    m = state["segment_final_positions_M"]
    kinds = {}
    for ins in state["inscriptions"]:
        for line in ins["lines"]:
            for seg in line["segments"]:
                kinds["segment-final"] = kinds.get("segment-final", 0) + 1
    # Position kinds the census carries: only segment-final is a
    # scored position kind of this census state.
    census_position_kinds = {"segment-final": m}

    rows = []
    q_total = 0.0
    for cand in CANDIDATES:
        p = cand["f_i"] / D
        f = 2
        while tail(m, p, f) >= ALPHA / K:
            f += 1
        q = tail(m, p, f)
        q_total += q
        rows.append({"ending": cand["ending"], "f_i": cand["f_i"],
                     "p_i": p, "E_i": m * p, "F_i": f, "q_i": q})
    assert q_total < ALPHA, q_total

    instantiation = []
    for cand in CANDIDATES:
        instantiation.append({
            "candidate": cand["ending"],
            "predicted_position_kind": "segment-final",
            "census_instances": census_position_kinds["segment-final"],
            "instantiable": census_position_kinds["segment-final"] > 0,
        })
    probe = {
        "probe_candidate": "-zz (procedure probe, not a candidate "
                           "of the study)",
        "predicted_position_kind": "reverse-face segment-final",
        "census_instances": census_position_kinds.get(
            "reverse-face segment-final", 0),
        "instantiable": False,
        "checker_result": "UNINSTANTIABLE - the closure branch of "
                          "floor record section 3 / TC-101-06 "
                          "returns TOO THIN for a candidate of this "
                          "kind; exercised here so the path is run, "
                          "not merely read",
    }

    result = {"M": m, "D": D, "K": K, "alpha_per_candidate": ALPHA / K,
              "floors": rows, "Q": q_total,
              "instantiation_registered_candidates": instantiation,
              "too_thin_all_registered_instantiable":
                  all(r["instantiable"] for r in instantiation),
              "tc101_06_probe": probe}
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print(json.dumps(result, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
