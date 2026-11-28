#!/usr/bin/env python3
"""Spec 111 P1 distributional measurement (filed harness).
Structural profiles of the three program systems vs the program's
deciphered control (Latin, Spec 107 donor text) and a synthetic
matched null, computed from the custody token streams (Spec 105
sandboxes) with one declared feature set. Progress lines are
timestamped and countable."""
import json, math, random, re, sys, time
from collections import Counter

CUST = "/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/spec105/"
LATIN = "/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/spec107/de-bello-gallico-gutenberg-218.txt"

def log(msg):
    print(f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {msg}", flush=True)

def flatten(obj):
    texts = []
    def walk(o):
        if isinstance(o, dict):
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            if o and all(isinstance(x, str) for x in o):
                texts.append(list(o))
            else:
                for v in o: walk(v)
    walk(obj)
    return [t for t in texts if t]

def profile(texts):
    toks = [t for text in texts for t in text]
    V = len(set(toks)); T = len(toks)
    c = Counter(toks)
    H1 = -sum((n/T)*math.log2(n/T) for n in c.values())
    bigrams = Counter()
    for text in texts:
        for a, b in zip(text, text[1:]): bigrams[(a, b)] += 1
    nb = sum(bigrams.values())
    Hb = -sum((n/nb)*math.log2(n/nb) for n in bigrams.values()) if nb else 0.0
    hapax = sum(1 for n in c.values() if n == 1)/V if V else 0.0
    # positional restriction: signs with >=5 tokens, dominant position share
    pos = {}
    for text in texts:
        for i, t in enumerate(text):
            p = "initial" if i == 0 else ("final" if i == len(text)-1 else "medial")
            pos.setdefault(t, Counter())[p] += 1
    meas = [t for t, cc in pos.items() if sum(cc.values()) >= 5]
    restr = sum(1 for t in meas if max(pos[t].values())/sum(pos[t].values()) >= 0.90)
    return {"texts": len(texts), "tokens": T, "inventory": V,
            "mean_text_len": T/len(texts) if texts else 0.0,
            "H1_bits": H1, "cond_entropy_bits": Hb - H1,
            "hapax_fraction": hapax,
            "positional_restricted_share": (restr/len(meas) if meas else 0.0),
            "measurable_signs_positional": len(meas)}

def main():
    systems = {}
    for name, fn in [("indus", "indus-derivation.json"), ("eteocypriot", "eteocypriot.json"), ("meroitic", "meroitic.json")]:
        texts = flatten(json.load(open(CUST+fn)))
        systems[name] = texts
        log(f"loaded {name}: {len(texts)} texts")
    raw = open(LATIN, encoding="utf-8", errors="replace").read()
    sents = re.split(r"[.!?]+", raw)
    latin = [[ch for ch in s.lower() if ch.isalpha()] for s in sents]
    latin = [s for s in latin if len(s) >= 2]
    systems["latin_control"] = latin
    log(f"loaded latin_control: {len(latin)} sentence-texts")
    # synthetic null: Indus texts with sign identities permuted per text-position pool
    rng = random.Random(11101)
    pool = [t for text in systems["indus"] for t in text]
    synth = []
    for text in systems["indus"]:
        synth.append([rng.choice(pool) for _ in text])
    systems["synthetic_null"] = synth
    log("built synthetic_null matched to indus text lengths")
    profs = {}
    for i, (name, texts) in enumerate(systems.items(), 1):
        profs[name] = profile(texts)
        log(f"profile {i}/5 {name}: {profs[name]}")
    feats = ["inventory", "mean_text_len", "H1_bits", "cond_entropy_bits", "hapax_fraction", "positional_restricted_share"]
    names = list(profs)
    mu = {f: sum(profs[n][f] for n in names)/len(names) for f in feats}
    sd = {f: (sum((profs[n][f]-mu[f])**2 for n in names)/len(names))**0.5 or 1.0 for f in feats}
    def dist(a, b):
        return math.sqrt(sum(((profs[a][f]-profs[b][f])/sd[f])**2 for f in feats))
    D = {a: {b: round(dist(a, b), 4) for b in names} for a in names}
    trio = ["indus", "eteocypriot", "meroitic"]
    within = [D[a][b] for i, a in enumerate(trio) for b in trio[i+1:]]
    to_ctrl = [D[a][c] for a in trio for c in ["latin_control", "synthetic_null"]]
    out = {"features": feats, "profiles": profs, "distances": D,
           "within_trio_mean": sum(within)/len(within), "within_trio": within,
           "trio_to_controls_mean": sum(to_ctrl)/len(to_ctrl), "trio_to_controls": to_ctrl,
           "meroitic_to_latin": D["meroitic"]["latin_control"],
           "indus_to_eteocypriot": D["indus"]["eteocypriot"],
           "note": "Descriptive, low-power: 5 systems, 6 features, one real control. Filed as the distributional leg of P1 only."}
    json.dump(out, open(sys.argv[1], "w"), indent=1)
    log(f"DONE within_trio_mean={out['within_trio_mean']:.4f} trio_to_controls_mean={out['trio_to_controls_mean']:.4f}")
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
