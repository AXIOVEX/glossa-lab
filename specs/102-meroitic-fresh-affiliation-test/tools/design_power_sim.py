#!/usr/bin/env python3
"""Spec 102 design-stage counting and power simulation (2026-11-22).

Design stage only: this script computes no study result. It (1) counts the
held material's concept ceiling with the Spec 097 campaign pipeline imported
unchanged, (2) validates the graded statistic T of Spec 102 section 3.2
against the executed Stage 4.2 lists, and (3) measures T's injection power
by the OD-15 section 4 method. Inputs are the custody holdings on
tower-compute (CC BY 4.0 / CC BY-SA 4.0 only); outputs are aggregates.
"""
import sys, collections, random, statistics
sys.argv = ["pipeline-v2.py", "design"]
import importlib.util
spec = importlib.util.spec_from_file_location(
    "p2", "/home/tpierson/glossa-work/meroitic-scratch/campaign/pipeline-v2.py")
p2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p2)

vocab = p2.build_vocab()
by_concept = collections.defaultdict(list)
for v in vocab:
    if v["concept"]:
        by_concept[v["concept"]].append(v)
concepts = sorted(by_concept)
nes = p2.asjp_forms(p2.NES_LANGS); aa = p2.asjp_forms(p2.AA_LANGS)
print("concept-bearing forms:", sum(len(x) for x in by_concept.values()),
      "concepts:", concepts)

def cscore(mer_skels, comp_forms):
    best = 0
    for ms in mer_skels:
        for (_, f) in comp_forms:
            cs = p2.asjp_skel(f)
            if not ms or not cs or ms[0] != cs[0]:
                continue
            s = 2 if (len(ms) == 1 or len(cs) == 1 or ms[1] == cs[1]) else 1
            best = max(best, s)
    return best

def build(comp):
    return {c: cscore([p2.skeleton(v["norm"]) for v in by_concept[c]],
                      comp.get(c, [])) for c in concepts}

def perm_null(comp, nperm=20000, seed=777001):
    rng = random.Random(seed)
    allforms = [f for fs in comp.values() for f in fs]
    counts = {c: len(comp[c]) for c in sorted(comp)}
    null = []
    for _ in range(nperm):
        pool = list(allforms); rng.shuffle(pool); idx = 0; sh = {}
        for c in sorted(comp):
            sh[c] = pool[idx:idx + counts[c]]; idx += counts[c]
        null.append(sum(build(sh).values()))
    return null

for name, comp in (("R1", nes), ("R2", aa)):
    obs = sum(build(comp).values()); null = perm_null(comp)
    p = (1 + sum(1 for x in null if x >= obs)) / (1 + len(null))
    print(name, {"T_obs": obs, "T_null_mean": round(statistics.mean(null), 3),
                 "perm_p": round(p, 4),
                 "T_99pct": sorted(null)[int(0.99 * len(null))]})

def injection_power(comp, theta, d, reps=4000, seed=424242):
    rng = random.Random(seed)
    null = perm_null(comp, nperm=4000, seed=777002)
    bar = sorted(null)[int(0.99 * len(null))]
    hits = 0
    for _ in range(reps):
        comp2 = {c: list(fs) for c, fs in comp.items()}
        for c in concepts:
            if rng.random() < theta and rng.random() < d:
                v = rng.choice(by_concept[c])
                comp2.setdefault(c, []).append(("INJ", p2.skeleton(v["norm"]) + "a"))
        hits += sum(build(comp2).values()) > bar
    return hits / reps

for theta in (0.2, 0.35, 0.5, 0.65):
    for d in (1.0, 0.75, 0.5):
        print("INJ R1 theta", theta, "d", d,
              "power", round(injection_power(nes, theta, d), 3))
