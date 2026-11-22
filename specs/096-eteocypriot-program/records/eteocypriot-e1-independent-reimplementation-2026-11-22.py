#!/usr/bin/env python3
"""OD-8 independent reimplementation, written from freeze-record-2026-11-20.md
section 5 (and sections 2-3 for pins/census) ONLY. The driver source was not
consulted in writing this. LCCS is computed by dynamic programming (the driver
uses brute-force scan). Derivation D(name) follows R1-R3 as the freeze states
them; the consonant stems used are the letter identities for the letters that
occur in the two ground-truth names (rho->r, sigma->s, tau->t, nu->n,
kappa->k), which are the voiceless-series signs of the Common syllabary.
"""
import hashlib, json, sys, unicodedata

VOW = {"α": "a", "ε": "e", "η": "e", "ι": "i", "ο": "o", "υ": "u", "ω": "o"}
STEM = {"ρ": "r", "σ": "s", "τ": "t", "ν": "n", "κ": "k"}

def derive(word):
    w = "".join(c for c in unicodedata.normalize("NFD", word)
                if not unicodedata.combining(c)).lower().replace("ς", "σ")
    units = [("v", VOW[c]) if c in VOW else ("c", STEM[c]) for c in w]
    out, prev, i = [], "a", 0
    while i < len(units):
        kind, val = units[i]
        if kind == "v":
            out.append(val); prev = val; i += 1
        elif i + 1 < len(units) and units[i + 1][0] == "v":
            out.append(val + units[i + 1][1]); prev = units[i + 1][1]; i += 2
        else:
            out.append(val + prev); i += 1
    return out

def lccs_dp(a, b):
    best = 0
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                best = max(best, cur[j])
        prev = cur
    return best

raw = open(sys.argv[1], "rb").read()
print("corpus_sha256:", hashlib.sha256(raw).hexdigest())
corpus = json.loads(raw.decode("utf-8"))
recs = {r["id"]: r for r in corpus["inscriptions"]}
for rid, rec in recs.items():
    canon = json.dumps(rec, sort_keys=True, ensure_ascii=False).encode("utf-8")
    print(f"pin {rid}: {hashlib.sha256(canon).hexdigest()} split={rec.get('split')}")

ics = recs["ICS196"]
segments = []
for line in ics["eteocypriot_lines"]:
    for seg in line["segments"]:
        segments.append([t.strip("[]") for t in seg])
print("segments:", ["-".join(s) for s in segments])
signs = [tok for line in ics["eteocypriot_lines"]
         for seg in line["segments"] for tok in seg]
print("census: segments", len(segments), "signs", len(signs),
      "legible", sum(1 for t in signs if not t.startswith("[") and t != "?"),
      "restored", sum(1 for t in signs if t.startswith("[")),
      "damaged", sum(1 for t in signs if t == "?"))

words = ics["greek_side"]["words"]
print("greek_words:", words)
# Ground truth as stated in freeze section 5 text (1-based indices).
gt = [("Ἀρίστωνα", 5, 6), ("Ἀριστώνακτος", 6, 7)]
a1 = a2 = 0
for name, wi, gt_seg in gt:
    d = derive(name)
    scores = [lccs_dp(d, s) for s in segments]
    best = max(scores)
    a2_partner = scores.index(best) + 1
    a1_rec = (wi == gt_seg)
    a2_rec = (a2_partner == gt_seg)
    a1 += a1_rec; a2 += a2_rec
    print(f"{name}: D={ '-'.join(d) } lccs={scores} A1_partner={wi} "
          f"A1_rec={a1_rec} A2_partner={a2_partner} A2_lccs={best} A2_rec={a2_rec}")
print(f"A1_recovered_count={a1} A2_recovered_count={a2} names_total=2")
print("ics196_leg_passes (both under at least one assumption):",
      (a1 == 2) or (a2 == 2))
print("P1_passes_as_registered: False (Androkles leg TOO THIN at freeze, F-E1b;"
      " 0 Eteocypriot segments held for ANDROKLES-A/B:",
      [len(recs[r].get('eteocypriot_side') or []) for r in ('ANDROKLES-A', 'ANDROKLES-B')], ")")
