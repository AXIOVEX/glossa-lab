#!/usr/bin/env python3
"""Spec 112 - TC-112-06 independent recomputation.

A second implementation of the preflight figures, written from the
registered design (spec.md SS4 and the execution freeze) and reading
only the filed outputs (records/ground-truth-sets.json,
records/preflight-output.json) plus the pinned corpus objects.
Rational figures (boundary F1, slot match rate, partial precision,
shuffle yield ratio) must agree EXACTLY with the harness's filed
values; entropies must agree to 1e-9 with the same argmax slot.
Exits 0 iff every figure agrees.
"""

import hashlib
import json
import math
import random
import re
import sys
from fractions import Fraction
from functools import lru_cache

KOV = "/home/tpierson/.syncyard/worktrees/glossa/kovetsky-src"
OTT = ("/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/"
       "spec097/otten-corpus/Data/mero-corpus.txt")
SEED = 20261128
LAM = 2.0
ALPHA = 0.1
ORDER = ["invocation", "presentation", "filiation1", "filiation2",
         "offering", "closing"]


def h(b):
    return hashlib.sha256(b).hexdigest()


def held(key):
    return int(h(key.encode()), 16) % 10 == 0


def toks_of(text):
    return [t for t in re.split(r"[\s.]+", text) if t and t.isalpha()]


# ---- corpus (independent loading)
rows = [json.loads(l) for l in open(KOV + "/data/inscriptions.jsonl")]
assert h(open(KOV + "/data/inscriptions.jsonl", "rb").read()) == \
    "1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4"
first_kind = {}
for r in rows:
    if r.get("text") and r["text"] not in first_kind:
        first_kind[r["text"]] = r["kind"]
dev_texts = {t: k for t, k in first_kind.items() if not held(t)}
ott_lines = open(OTT).read().splitlines()
ott_dev = sorted({l for l in ott_lines if not held(l)})

kov_forms = set()
for t in dev_texts:
    kov_forms.update(toks_of(t))
ott_forms = set()
for l in ott_dev:
    ott_forms.update(toks_of(l))
forms = kov_forms | ott_forms

fun_texts = []
for t, k in sorted(dev_texts.items()):
    if k == "funerary":
        tt = toks_of(t)
        if len(tt) >= 4:
            fun_texts.append(tt)

# ---- independent segmenter: memoized recursion over the same
# positional-class unigram statistics, recomputed here.
counts = {c: {} for c in "IFMW"}
support = {}
for f in forms:
    n = len(f)
    seen = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            s = f[i:j]
            cls = "W" if (i == 0 and j == n) else \
                  "I" if i == 0 else "F" if j == n else "M"
            counts[cls][s] = counts[cls].get(s, 0) + 1
            if s not in seen:
                seen.add(s)
                support[s] = support.get(s, 0) + 1
totals = {c: sum(d.values()) for c, d in counts.items()}
vocab = {c: len(d) for c, d in counts.items()}
inventory = {s for s, v in support.items() if v >= 3 or len(s) == 1}


def logp(s, cls):
    return math.log((counts[cls].get(s, 0) + ALPHA) /
                    (totals[cls] + ALPHA * vocab[cls]))


def best_boundaries(form):
    n = len(form)

    @lru_cache(maxsize=None)
    def solve(i, started):
        # best (score, segmentation) for form[i:]
        if i == n:
            return (0.0, ())
        best = None
        for j in range(i + 1, n + 1):
            s = form[i:j]
            whole = (i == 0 and j == n)
            if not whole and s not in inventory and len(s) > 1:
                continue
            cls = "W" if whole else "I" if i == 0 else \
                  "F" if j == n else "M"
            rest = solve(j, True)
            if rest is None:
                continue
            sc = logp(s, cls) - (LAM if started else 0.0) + rest[0]
            cand = (sc, (s,) + rest[1])
            if best is None or cand[0] > best[0] or \
                    (cand[0] == best[0] and cand[1] < best[1]):
                best = cand
        return best

    seg = solve(0, False)[1]
    out, acc = [], 0
    for s in seg[:-1]:
        acc += len(s)
        out.append(acc)
    return out


def f1(pred, gold):
    p, g = set(pred), set(gold)
    tp = len(p & g)
    if not p and not g:
        return Fraction(1)
    if not p or not g:
        return Fraction(0)
    return Fraction(2 * tp, len(p) + len(g))


# ---- independent slot machinery
def profiles(texts):
    prof = {}
    for tt in texts:
        n = len(tt)
        for i, t in enumerate(tt):
            rel = i / (n - 1) if n > 1 else 0.0
            b = min(5, int(6 * rel))
            d = prof.setdefault(t, [0, [0] * 6, 0.0])
            d[0] += 1
            d[1][b] += 1
            d[2] += rel
    out = {}
    for t, (occ, bands, rsum) in prof.items():
        mb = max(range(6), key=lambda b: (bands[b], -b))
        out[t] = {"occ": occ, "bands": bands, "modal_band": mb,
                  "modal_mass": bands[mb] / occ, "centroid": rsum / occ,
                  "rel_sum": rsum}
    return out


def yield_of(prof):
    per = [0] * 6
    for d in prof.values():
        if d["occ"] >= 10 and d["modal_mass"] >= 0.60:
            per[d["modal_band"]] += 1
    return sum(1 for c in per if c >= 5), per


def mapping_of(prof):
    def modal(pred):
        c = sorted(((d["occ"], t) for t, d in prof.items() if pred(t)),
                   key=lambda x: (-x[0], x[1]))
        return prof[c[0][1]]["modal_band"] if c else None
    inv = modal(lambda t: t == "woSi")
    f1b = modal(lambda t: "tedxe" in t or "tdxe" in t)
    f2b = modal(lambda t: "terike" in t or "yerike" in t)
    off = modal(lambda t: t == "ato")
    if None in (inv, f1b, f2b, off):
        return None
    m = {inv: "invocation", f1b: "filiation1", f2b: "filiation2",
         off: "offering"}
    bc = {}
    for d in prof.values():
        bc.setdefault(d["modal_band"], []).append(d)
    cent = {b: sum(d["rel_sum"] for d in ds) / sum(d["occ"] for d in ds)
            for b, ds in bc.items()}
    rem = sorted((b for b in range(6) if b not in m),
                 key=lambda b: cent.get(b, 0.0))
    after = [b for b in rem if cent.get(b, 0.0) > cent.get(inv, 0.0)]
    if not after:
        return None
    m[after[0]] = "presentation"
    rest = [b for b in rem if b != after[0]]
    if rest:
        m[rest[-1]] = "closing"
    return m


def slot_of(t, i, n, prof, m):
    d = prof.get(t)
    if d is not None and d["occ"] >= 3:
        b = d["modal_band"]
    else:
        rel = i / (n - 1) if n > 1 else 0.0
        b = min(5, int(6 * rel))
    return m.get(b)


def seq_of(tt, prof, m):
    seq = []
    for i, t in enumerate(tt):
        s = slot_of(t, i, len(tt), prof, m)
        if s is not None and s not in seq:
            seq.append(s)
    return seq


def label_of(tt):
    def find(pred, lo=0):
        for i in range(lo, len(tt)):
            if pred(tt[i]):
                return i
        return None
    w = find(lambda t: t == "woSi")
    s = find(lambda t: t in ("Soreyi", "aSoreyi"))
    if w is None or s is None or w > 3 or s > 4 or w > s:
        return None
    a = find(lambda t: "tedxe" in t or "tdxe" in t, s + 1)
    b = find(lambda t: "terike" in t or "yerike" in t, s + 1)
    if a is None and b is None:
        return None
    o = find(lambda t: t == "ato" or (t.startswith("ato")
                                      and len(t) <= 7), s + 1)
    present = {"invocation"}
    anch = [i for i in (a, b, o) if i is not None]
    if min(anch) > s + 1:
        present.add("presentation")
    if a is not None:
        present.add("filiation1")
    if b is not None:
        present.add("filiation2")
    if o is not None:
        present.add("offering")
    if max(anch) < len(tt) - 1:
        present.add("closing")
    return present


def main(gt_path, out_path, verify_path):
    gt = json.load(open(gt_path))["ground_truth"]
    filed = json.load(open(out_path))
    checks = {}

    # P-1
    per = {}
    for key, rec in sorted(gt.items()):
        per[key] = f1(best_boundaries(rec["form"]), rec["boundaries"])
    vals = sorted(per.values())
    m = len(vals)
    med = vals[m // 2] if m % 2 else (vals[m // 2 - 1] + vals[m // 2]) / 2
    checks["P-1 median F1 exact"] = (str(med) == filed["P-1"]["median_f1"])
    checks["P-1 per-form F1 exact"] = all(
        str(per[k]) == filed["P-1"]["per_form_f1"][k] for k in per)
    checks["P-1 pass flag"] = \
        filed["P-1"]["pass"] == (med >= Fraction(4, 5))

    # P-2
    prof = profiles(fun_texts)
    mp = mapping_of(prof)
    filed_map = {int(k): v for k, v in
                 (filed["P-2"]["mapping"] or {}).items()}
    checks["P-2 mapping equal"] = (mp == filed_map)
    labeled = [(tt, label_of(tt)) for tt in fun_texts]
    labeled = [(tt, p) for tt, p in labeled if p is not None]
    matches = 0
    for tt, present in labeled:
        want = [s for s in ORDER if s in present]
        if seq_of(tt, prof, mp) == want:
            matches += 1
    rate = Fraction(matches, len(labeled)) if labeled else Fraction(0)
    checks["P-2 match rate exact"] = \
        (str(rate) == filed["P-2"]["match_rate"])
    per_slot = {}
    for tt in fun_texts:
        for i, t in enumerate(tt):
            s = slot_of(t, i, len(tt), prof, mp)
            if s is not None:
                per_slot.setdefault(s, {})
                per_slot[s][t] = per_slot[s].get(t, 0) + 1
    ent = {}
    for s, d in per_slot.items():
        tot = sum(d.values())
        ent[s] = -sum((c / tot) * math.log2(c / tot) for c in d.values())
    checks["P-2 entropies 1e-9"] = all(
        abs(ent[s] - filed["P-2"]["slot_entropy"][s]) < 1e-9
        for s in ent) and set(ent) == set(filed["P-2"]["slot_entropy"])
    name_max = bool(ent) and max(ent, key=lambda s: ent[s]) == \
        "presentation"
    checks["P-2 name-slot argmax"] = \
        (name_max == filed["P-2"]["name_slot_is_max_entropy"])
    checks["P-2 pass flag"] = filed["P-2"]["pass"] == \
        (rate >= Fraction(9, 10) and name_max)

    # P-3 partials (independent enumeration)
    support = {}
    prof2 = {}
    for f in forms:
        n = len(f)
        seen = set()
        for i in range(n):
            for ln in range(2, 9):
                j = i + ln
                if j > n:
                    break
                s = f[i:j]
                if s not in seen:
                    seen.add(s)
                    support.setdefault(s, set()).add(f)
                if ln == n:
                    continue
                d = prof2.setdefault(s, [0, 0, 0])
                if i == 0:
                    d[0] += 1
                elif j == n:
                    d[2] += 1
                else:
                    d[1] += 1
    gold = set()
    gm = json.load(open(KOV + "/data/gold_morphology.json"))
    for e in gm:
        if e["form"].startswith("-") and e.get("corpus_form"):
            for s in [e["corpus_form"]] + list(e.get("corpus_variants")
                                               or []):
                gold.add(s)
                gold.add(s.replace("E", "o"))
    proposals = set()
    for s, hosts in support.items():
        if len(hosts) < 10:
            continue
        ini, med, fin = prof2.get(s, [0, 0, 0])
        tot = ini + med + fin
        if tot and fin / tot >= 0.80:
            proposals.add(s)
    prec = Fraction(len(proposals & gold), len(proposals)) \
        if proposals else Fraction(0)
    checks["P-3 precision exact"] = \
        (str(prec) == filed["P-3"]["precision"])
    checks["P-3 proposal set equal"] = \
        (sorted(proposals) == filed["P-3"]["proposal_set"])
    y, _ = yield_of(prof)
    rng = random.Random(SEED)
    shuf = []
    for tt in fun_texts:
        t2 = list(tt)
        rng.shuffle(t2)
        shuf.append(t2)
    sy, _ = yield_of(profiles(shuf))
    ratio = Fraction(sy, y) if y else None
    checks["P-3 yields"] = (y == filed["P-3"]["real_yield"] and
                            sy == filed["P-3"]["shuffle_yield"])
    checks["P-3 ratio exact"] = \
        ((str(ratio) if ratio is not None else None) ==
         filed["P-3"]["shuffle_ratio"])
    checks["P-3 pass flag"] = filed["P-3"]["pass"] == \
        (prec >= Fraction(4, 5) and ratio is not None
         and ratio <= Fraction(1, 5))
    checks["pass_in_full consistent"] = filed["pass_in_full"] == bool(
        filed["P-1"]["pass"] and filed["P-2"]["pass"]
        and filed["P-3"]["pass"])

    result = {"checks": checks, "all_agree": all(checks.values()),
              "recomputed": {"P-1_median_f1": str(med),
                             "P-2_match_rate": str(rate),
                             "P-3_precision": str(prec),
                             "P-3_shuffle_ratio":
                                 str(ratio) if ratio is not None else None}}
    with open(verify_path, "w") as fh:
        json.dump(result, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print(json.dumps(result, indent=1, sort_keys=True))
    sys.exit(0 if result["all_agree"] else 1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
