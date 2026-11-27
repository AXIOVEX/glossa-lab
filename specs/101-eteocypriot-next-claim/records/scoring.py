#!/usr/bin/env python3
"""Spec 101 T301 - the registered scoring run (Spec 107 cycle 1).

Counts each registered candidate at its registered positions in
the Perna-side state, by the final-sign extraction rule of the
freeze addendum (records/freeze-addendum-2026-11-27.md, Table 3),
and applies the verdict rule of the floor record section 1.5.

Deterministic: the outcome JSON (argv[1]) is byte-identical
across runs over the same state. Uses only the tables stated in
the freeze addendum (C101-3).
"""
import json
import sys

STATE = "specs/101-eteocypriot-next-claim/corpus/corpus.json"
CANDIDATES = {"-se": ("se", 33), "-na": ("na", 25),
              "-i": ("i", 25), "-ti": ("ti", 25)}
Q = 0.03115339858698945


def main():
    out_path = sys.argv[1]
    state = json.load(open(STATE, encoding="utf-8"))
    counts = {k: 0 for k in CANDIDATES}
    per_inscription = {}
    finals = 0
    for ins in state["inscriptions"]:
        sub = {k: 0 for k in CANDIDATES}
        for line in ins["lines"]:
            for seg in line["segments"]:
                finals += 1
                final = seg["signs"][-1]
                for name, (label, _f) in CANDIDATES.items():
                    if final == label:
                        counts[name] += 1
                        sub[name] += 1
        per_inscription[ins["id"]] = sub
    rows = []
    supported = False
    for name in ("-se", "-na", "-i", "-ti"):
        label, floor = CANDIDATES[name]
        hit = counts[name] >= floor
        supported = supported or hit
        rows.append({"candidate": name, "sign": label,
                     "count": counts[name], "floor": floor,
                     "at_or_above_floor": hit,
                     "per_inscription": {
                         k: v[name] for k, v in per_inscription.items()}})
    verdict = ("SUPPORTED (at postdictive strength)"
               if supported and Q < 0.05 else "NOT SUPPORTED")
    result = {"state_sha256_expected":
              "9535108dfcbd93adb6b10ba8c2ca40cfd7a5710b02bb45f1c5768f00a54a631c",
              "segment_final_positions_scored": finals,
              "candidates": rows, "Q": Q, "verdict_C101-1": verdict,
              "target": "ENRICHMENT (OD-D-1); NOT SUPPORTED is "
                        "expressly not a recurrence finding"}
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print(json.dumps(result, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
