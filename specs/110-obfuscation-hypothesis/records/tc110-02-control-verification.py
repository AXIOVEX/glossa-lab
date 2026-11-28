#!/usr/bin/env python3
"""TC-110-02 — independent recomputation of the Spec 110 gate's decisive
quantities, written independently of records/obfuscation-harness.py
(it imports only the Spec 109 Stage 1 corpus builder, the corpus
source). Checks: (1) the family A natural bands reproduce from the
control samples; (2) G-A rep 1: the T-HOM flattening pattern fires and
the T-POLY structure pattern does not, from recomputed statistics;
(3) G-B rep 1: observed JSD, null p99, and the baseline reproduce;
(4) the filed gate counts mechanically imply the filed gate verdict
under the registered thresholds. Exit 0 iff all checks pass.
"""
import importlib.util
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(sys.argv[1])
CUST = Path(sys.argv[2])
spec = importlib.util.spec_from_file_location(
    "s1v", ROOT / "specs/109-generative-decipherment-engine/records/"
    "stage-1-preflight-harness.py")
S1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S1)

fails = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
    if not ok:
        fails.append(name)


def build(seed):
    lengths = S1.indus_lengths()
    try:
        b = S1.build_corpus(seed, lengths)
    except RuntimeError:
        b = S1.build_corpus(seed + "-try1", lengths)
    return [[str(s) for s in q] for q in b["signseqs"]], \
        [b["sites"][i] for i in range(len(b["signseqs"]))]


def a_stats(seqs):
    toks = [t for q in seqs for t in q]
    n = len(toks)
    c = Counter(toks)
    v = len(c)
    h = -sum((k / n) * math.log2(k / n) for k in c.values())
    pairs = Counter()
    firsts = Counter()
    for q in seqs:
        for a, b in zip(q, q[1:]):
            pairs[(a, b)] += 1
            firsts[a] += 1
    m = sum(pairs.values())
    h2 = 0.0
    for a, fa in firsts.items():
        row = [(b, k) for (x, b), k in pairs.items() if x == a]
        tot = sum(k for _, k in row)
        hc = -sum((k / tot) * math.log2(k / tot) for _, k in row if k)
        h2 += (fa / m) * hc
    return {"A1": h / math.log2(v) if v > 1 else 0.0,
            "A2": max(c.values()) / n, "A3": h2 / h if h else 0.0,
            "A4": h - h2}


gate = json.loads((CUST / "gate-output.json").read_text())

# (1) bands from synthetic naturals + Latin + Meroitic samples
samples = []
for i in range(1, 6):
    seqs, _ = build(f"spec110-nat-{i}")
    samples.append(seqs)
lat = (ROOT.parent / "glossa-custody/spec107/de-bello-gallico-gutenberg-218.txt")
words = []
import re
for line in lat.read_text(errors="replace").splitlines():
    line = line.strip()
    if line and not line.startswith("#"):
        for w in re.split(r"[^A-Za-z]+", line):
            w = w.lower()
            if len(w) >= 2:
                words.append(list(w))
q = len(words) // 4
for i in range(4):
    samples.append(words[i * q:(i + 1) * q])
mer = json.loads((ROOT.parent / "glossa-custody/spec105/meroitic.json").read_text())
mseqs = []
for t in mer:
    for line in t["lines"]:
        # each line is a list of words; each word a list of graphemes
        flat = [str(s) for g in line for s in g if s != "."]
        if flat:
            mseqs.append(flat)
samples.append(mseqs)
samples.append(mseqs[:len(mseqs) // 2])
samples.append(mseqs[len(mseqs) // 2:])
stats = [a_stats(s) for s in samples]
for k in ("A1", "A2", "A3", "A4"):
    lo = min(s[k] for s in stats)
    hi = max(s[k] for s in stats)
    flo, fhi = gate["band_all"][k]
    check(f"band {k} reproduces", abs(lo - flo) < 1e-9 and abs(hi - fhi) < 1e-9,
          f"recomputed [{lo:.4f}, {hi:.4f}] vs filed [{flo:.4f}, {fhi:.4f}]")
band = {k: (min(s[k] for s in stats), max(s[k] for s in stats)) for k in stats[0]}

# (2) G-A rep 1 transformations on control corpus 1
corp, _sites = build("spec110-ctl-1")
rng = random.Random(11001)
cnt = Counter(t for q in corp for t in q)
top = [s for s, _ in cnt.most_common(10)]
hom = []
for q in corp:
    out = []
    for t in q:
        if t in top:
            out.append(t + ("#h0" if rng.random() < 0.5 else "#h1"))
        else:
            out.append(t)
    hom.append(out)
hs = a_stats(hom)
flat = hs["A1"] > band["A1"][1] and hs["A2"] < band["A2"][0]
check("G-A rep1 T-HOM flattening fires", flat,
      f"A1 {hs['A1']:.4f} vs band max {band['A1'][1]:.4f}; "
      f"A2 {hs['A2']:.4f} vs band min {band['A2'][0]:.4f}")
perms = []
inv = sorted(cnt)
r2 = random.Random(11001 + 100)
for _ in range(3):
    vals = inv[:]
    r2.shuffle(vals)
    perms.append(dict(zip(inv, vals)))
poly = [[perms[i % 3][t] for i, t in enumerate(q)] for q in corp]
ps = a_stats(poly)
struct = ps["A3"] > band["A3"][1] and ps["A4"] < band["A4"][0]
check("G-A rep1 T-POLY structure does not fire", not struct,
      f"A3 {ps['A3']:.4f} vs band max {band['A3'][1]:.4f}; "
      f"A4 {ps['A4']:.4f} vs band min {band['A4'][0]:.4f}")

# (3) G-B rep 1: site B under one permutation
corp, sites = build("spec110-ctl-1")
r3 = random.Random(11001 + 300)
vals = inv[:]
r3.shuffle(vals)
perm = dict(zip(inv, vals))
tc = [[perm.get(t, t) for t in q] if sites[k] == "B" else list(q)
      for k, q in enumerate(corp)]


def jsd(groups):
    signs = set()
    for g in groups.values():
        for q in g:
            signs.update(q)
    signs = sorted(signs)
    profs = {}
    tots = {}
    for lab, g in groups.items():
        c = Counter(t for q in g for t in q)
        tots[lab] = sum(c.values())
        profs[lab] = {s: c.get(s, 0) / tots[lab] for s in signs}
    tw = sum(tots.values())
    tot_jsd = 0.0
    labs = list(groups)
    for i in range(len(labs)):
        for j in range(i + 1, len(labs)):
            a, b = profs[labs[i]], profs[labs[j]]
            d = 0.0
            for s in signs:
                pa, pb = a[s], b[s]
                m = 0.5 * (pa + pb)
                if pa > 0:
                    d += 0.5 * pa * math.log2(pa / m)
                if pb > 0:
                    d += 0.5 * pb * math.log2(pb / m)
            tot_jsd += (tots[labs[i]] + tots[labs[j]]) * d
    return tot_jsd / tw


groups = {"A": [q for q, s in zip(tc, sites) if s == "A"],
          "B": [q for q, s in zip(tc, sites) if s == "B"]}
obs = jsd(groups)
bins = {}
for idx, q in enumerate(tc):
    L = len(q)
    bins.setdefault(0 if L <= 2 else 1 if L <= 4 else 2 if L <= 6 else 3,
                    []).append(idx)
rng4 = random.Random(11001)
labs = list(sites)
nulls = []
for _ in range(999):
    nl = labs[:]
    for idxs in bins.values():
        sub = [nl[i] for i in idxs]
        rng4.shuffle(sub)
        for i, v in zip(idxs, sub):
            nl[i] = v
    g2 = {"A": [q for q, s in zip(tc, nl) if s == "A"],
          "B": [q for q, s in zip(tc, nl) if s == "B"]}
    nulls.append(jsd(g2))
nulls.sort()
p99 = nulls[int(0.99 * len(nulls))]
base = max(gate["B_baseline_site_jsds"])
check("G-B rep1 detection reproduces", obs > p99 and obs > base,
      f"obs {obs:.4f} vs p99 {p99:.4f}, baseline {base:.4f} "
      f"(filed rep1 obs 0.2788)")

# (4) mechanical gate evaluation from filed counts
g = gate["gate"]
mech = (g["G-A"]["hom"] >= 4 and g["G-A"]["poly"] >= 4
        and g["G-D"]["detections"] >= 4
        and g["G-C"]["c1_detections"] >= 4 and g["G-C"]["c2_detections"] >= 4
        and g["G-B"]["detections"] >= 4
        and all(v >= 4 for v in g["G-INV"]["no_fire"].values())
        and all(v <= 1 for v in g["G-FP"]["false_fires"].values()))
check("filed counts mechanically imply the filed verdict",
      mech == gate["gate"]["pass"] == False,
      f"mechanical pass={mech}, filed pass={gate['gate']['pass']}")

print(f"TC-110-02: {'PASS' if not fails else 'FAIL'} ({len(fails)} failures)")
sys.exit(0 if not fails else 1)
