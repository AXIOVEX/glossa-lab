#!/usr/bin/env python3
"""Spec 107, test M-2 — calibration STOP-gate administration.

Reconstructs the registered basis from the pinned Kovetsky build
only, under pipeline-v2 conventions (tokens_of and same_place_rate
verbatim from the Spec 097 campaign pipeline, PLACE table
verbatim, development partition by freeze v2 section 1's rule),
and compares the four filed figures. Also computes the NES
reference from the ASJP custody lists as a conventions control.
Writes the calibration JSON (argv[1]). The gate's result is in
records/m2-outcome-record-2026-11-27.md: the reconstruction does
not reproduce the filed figures, and M-2 stops.
"""
import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone

KOV = "/home/tpierson/.syncyard/worktrees/glossa/kovetsky-src"
KOV_SHA256 = "1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4"
ASJP = "/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/spec097"
NES_LANGS = ["OLD_NUBIAN", "NOBIIN", "DONGOLESE_NUBIAN",
             "KUNUZ_NUBIAN", "MEIDOB_NUBIAN", "NARA"]
FILED = {"words": 12863, "cvc_pairs": 13406,
         "same_place_rate": 0.3152, "nes_reference_rate": 0.3038}


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] M-2 calibration {msg}", flush=True)


def tokens_of(text):
    return [t for t in re.split(r"[\s.]+", text.lower())
            if t and not t.startswith("#")]


PLACE = {"p": "labial", "b": "labial", "m": "labial",
         "k": "velar", "q": "velar", "g": "velar", "x": "velar",
         "t": "coronal", "d": "coronal", "s": "coronal",
         "z": "coronal", "n": "coronal", "l": "coronal",
         "r": "coronal"}


def same_place_rate(words):
    tot = 0
    same = 0
    for w in words:
        cons = [(i, c) for i, c in enumerate(w)
                if c not in "aeiou" and c.isalpha()]
        for (i1, c1), (i2, c2) in zip(cons, cons[1:]):
            if i2 - i1 == 2:
                tot += 1
                if PLACE.get(c1) and PLACE.get(c1) == PLACE.get(c2):
                    same += 1
    return (same / tot if tot else None), tot


def main():
    out_path = sys.argv[1]
    raw = open(f"{KOV}/data/inscriptions.jsonl", "rb").read()
    assert hashlib.sha256(raw).hexdigest() == KOV_SHA256
    ins = [json.loads(l) for l in raw.decode("utf-8").splitlines()
           if l.strip()]
    seen = {}
    for d in ins:
        t = (d.get("text") or "").strip()
        if t and t not in seen:
            seen[t] = d
    dev = [t for t in seen
           if int(hashlib.sha256(t.encode("utf-8")).hexdigest(), 16)
           % 10 != 0]
    log(f"development partition: {len(dev)} texts (filed 335)")
    words = []
    for t in dev:
        words += tokens_of(t)
    rate, tot = same_place_rate(words)
    log(f"reconstructed: words {len(words)} (filed 12863); CVC pairs "
        f"{tot} (filed 13406); same-place rate {rate:.4f} "
        f"(filed 0.3152)")
    nes_words = []
    with open(f"{ASJP}/forms.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["Language_ID"] in NES_LANGS:
                nes_words.append(r["Form"].lower())
    nes_rate, nes_tot = same_place_rate(nes_words)
    log(f"NES reference: {nes_rate:.4f} over {len(nes_words)} forms "
        f"(filed 0.3038)")
    result = {
        "test": "M-2 calibration gate (Spec 107 cycle 2)",
        "build_sha256": KOV_SHA256,
        "development_texts": len(dev),
        "reconstructed": {"words": len(words), "cvc_pairs": tot,
                          "same_place_rate": rate,
                          "nes_reference_rate": nes_rate,
                          "nes_forms": len(nes_words),
                          "nes_pairs": nes_tot},
        "filed": FILED,
        "gate_pass": (len(words) == FILED["words"]
                      and tot == FILED["cvc_pairs"]
                      and round(rate, 4) == FILED["same_place_rate"]
                      and round(nes_rate, 4)
                      == FILED["nes_reference_rate"]),
    }
    json.dump(result, open(out_path, "w"), indent=1,
              ensure_ascii=False)
    log(f"gate pass: {result['gate_pass']} — written to {out_path}")
    return 0 if result["gate_pass"] else 3


if __name__ == "__main__":
    sys.exit(main())
