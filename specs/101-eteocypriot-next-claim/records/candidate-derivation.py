#!/usr/bin/env python3
"""Spec 101 T201 - candidate derivation (Spec 107 cycle 1, E-1).

Derives the recurring-ending candidates from the ICS 196
development set alone, by the mechanical rule registered in
Spec 101 spec.md section 3.1 P-2 and derived in the floor
record (records/floor-derivation-and-outcome-registration-
2026-11-22.md) section 2: a sign sequence recurring at
segment-final position in at least two development segments.

Inputs: the Spec 096 corpus file ONLY (ICS 196 entry,
split = development). The Perna-side state is never opened
by this script (registration precedence, TC-101-02).

Writes the derivation output JSON to argv[1].
"""
import json
import sys
from collections import Counter

CORPUS096 = "specs/096-eteocypriot-program/corpus/corpus.json"


def main():
    out_path = sys.argv[1]
    corpus = json.load(open(CORPUS096, encoding="utf-8"))
    entry = [i for i in corpus["inscriptions"] if i["id"] == "ICS196"]
    assert len(entry) == 1 and entry[0]["split"] == "development"
    segments = []
    for line in entry[0]["eteocypriot_lines"]:
        segments.extend(line["segments"])
    assert len(segments) == 11, len(segments)

    suffix_counts = Counter()
    suffix_segments = {}
    for idx, seg in enumerate(segments, start=1):
        for length in range(1, len(seg) + 1):
            suf = tuple(seg[-length:])
            suffix_counts[suf] += 1
            suffix_segments.setdefault(suf, []).append(idx)

    recurring = {s: c for s, c in suffix_counts.items() if c >= 2}
    len1 = {s: c for s, c in recurring.items() if len(s) == 1}
    len_ge2 = {s: c for s, c in recurring.items() if len(s) >= 2}

    candidates = []
    for suf in sorted(len1, key=lambda s: (-len1[s], s)):
        candidates.append({
            "ending": "-" + suf[0],
            "signs": list(suf),
            "f_i": len1[suf],
            "development_segments": suffix_segments[suf],
            "predicted_positions":
                "segment-final positions of the Perna-side census",
        })

    result = {
        "derivation": "mechanical rule of spec.md 3.1 P-2 over the "
                      "ICS 196 development set alone",
        "development_segments_D": len(segments),
        "recurring_suffixes_total": len(recurring),
        "recurring_length_ge_2": {
            "-".join(s): c for s, c in sorted(len_ge2.items())},
        "candidates_K": len(candidates),
        "candidates": candidates,
    }
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print(json.dumps(result, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
