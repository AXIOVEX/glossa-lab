#!/usr/bin/env python3
"""Spec 107, test I-1 — Indus scramble-simulation identifiability
calibration. Executes the registration filed at
specs/107-active-decipherment-loop/records/cycle-1-registration-2026-11-26.md
section 2.

Two donor corpora of known structure (Meroitic from the pinned
Kovetsky build; Latin, Caesar's De Bello Gallico from Project
Gutenberg, pinned in the run record at acquisition, before any
scoring) are reshaped to the Indus corpus profile (artifact count,
token count, per-artifact length distribution, duplication rate,
from the Spec 105 custody datasets), ciphered, split
duplicate-aware (distinct sequences by first-appearance ordinal,
ordinal % 5 == 4 to the reserve), and scored with the program's own
G-IND-form predictor (Spec 105 Stage 6 registration section 5,
weights as registered, unnormalized) under RIGHT / WRONG / SHUFFLE
conditions, plus the L3 positional statistics (R2) and adjacency
recovery (R3). Scales 0.5x / 1x / 2x, 20 replications per
(donor x scale), seeds random.Random("spec107-i1-{donor}-{scale}-{rep}").

Two independent implementations of the predictor scoring must agree
on every replication's advantages to six decimal places, or the run
STOPS (TC-107-02). Writes the raw-output JSON (argv[1]); the donor B
bytes and intermediates stay in custody (argv[2] = custody dir).
"""
import hashlib
import json
import math
import random
import sys
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from statistics import median

KOVETSKY = "/home/tpierson/.syncyard/worktrees/glossa/kovetsky-src/data/inscriptions.jsonl"
KOVETSKY_SHA256 = "1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4"
CUSTODY105 = "/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/spec105"
LATIN_URL = "https://www.gutenberg.org/cache/epub/218/pg218.txt"
LATIN_MIRRORS = ["https://gutenberg.pglaf.org/cache/epub/218/pg218.txt"]
SCALES = (0.5, 1.0, 2.0)
REPS = 20
UNMAPPED = "\x00UNMAPPED"


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] I-1 {msg}", flush=True)


# ---------------------------------------------------------------- donors
def meroitic_stream():
    raw = open(KOVETSKY, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == KOVETSKY_SHA256
    groups = []
    for line in raw.decode("utf-8").splitlines():
        if not line.strip():
            continue
        text = json.loads(line).get("text")
        if text is not None:
            groups.extend(list(w) for w in text.split(" "))
    return groups


def latin_stream(custody_dir):
    path = f"{custody_dir}/de-bello-gallico-gutenberg-218.txt"
    fetched_from = None
    try:
        raw = open(path, "rb").read()
        fetched_from = "custody (acquired at this run's first attempt)"
    except FileNotFoundError:
        raw = None
        for url in [LATIN_URL] + LATIN_MIRRORS:
            try:
                req = urllib.request.Request(
                    url, headers={"User-Agent": "glossa-lab-research"})
                with urllib.request.urlopen(req) as resp:
                    raw = resp.read()
                fetched_from = url
                break
            except Exception:
                continue
        if raw is None:
            raise RuntimeError("donor B acquisition failed on all routes")
        open(path, "wb").write(raw)
    sha = hashlib.sha256(raw).hexdigest()
    text = raw.decode("utf-8-sig")
    start = text.index("*** START OF")
    start = text.index("\n", start) + 1
    end = text.index("*** END OF")
    body = text[start:end]
    head = body[:20000].upper()
    assert "GALLIA EST OMNIS" in head or "BELLO GALLICO" in head, \
        "donor B identity check failed"
    prepared = []
    for ch in body.lower():
        if ch == "j":
            ch = "i"
        elif ch == "u":
            ch = "v"
        prepared.append(ch if "a" <= ch <= "z" or ch.isspace() else " ")
    groups = [list(w) for w in "".join(prepared).split()]
    return groups, {"url": LATIN_URL, "fetched_from": fetched_from,
                    "path": path, "sha256": sha, "bytes": len(raw)}


def ground_truth(groups):
    pos = defaultdict(Counter)
    pairs = Counter()
    for g in groups:
        if len(g) == 1:
            pos[g[0]]["sole"] += 1
            continue
        for i, m in enumerate(g):
            pos[m]["initial" if i == 0 else
                    "final" if i == len(g) - 1 else "medial"] += 1
        pairs.update(zip(g, g[1:]))
    restricted = {}
    for m, c in pos.items():
        total = sum(c.values())
        if total < 20:
            continue
        if (c["initial"] + c["sole"]) / total >= 0.99:
            restricted[m] = "initial"
        elif (c["final"] + c["sole"]) / total >= 0.99:
            restricted[m] = "final"
    top100 = [tuple(p) for p, _ in pairs.most_common(100)]
    return restricted, top100


# ---------------------------------------------------------------- target
def target_shape():
    def load(name):
        data = json.load(open(f"{CUSTODY105}/{name}"))
        return [tuple(tuple(g) for g in art["lines"][0]) for art in data]
    deriv = load("indus-derivation.json")
    reserve = load("indus-reserve.json")
    full = []
    di = ri = 0
    for i in range(len(deriv) + len(reserve)):
        if i % 5 == 4:
            full.append(reserve[ri]); ri += 1
        else:
            full.append(deriv[di]); di += 1
    lengths = [sum(len(g) for g in art) for art in full]
    inventory = {m for art in full for g in art for m in g}
    d = (len(full) - len(set(full))) / len(full)
    return {"artifacts": len(full), "tokens": sum(lengths),
            "lengths": lengths, "inventory": len(inventory),
            "duplication_rate": d}


# ---------------------------------------------------------------- scorer A
def score_a(deriv_groups, reserve_groups):
    """Direct implementation of the Stage 6 section 5 rules."""
    c = Counter()
    ic = Counter()
    pc = Counter()
    st = Counter()
    for g in deriv_groups:
        ic[g[0]] += 1
        for i, m in enumerate(g):
            c[m] += 1
            if i:
                pc[(g[i - 1], m)] += 1
                st[g[i - 1]] += 1
    N = sum(c.values())
    V = len(c)
    G = len(deriv_groups)
    eps = 1.0 / (N + V)

    def w_base(m):
        return c[m] / N if m in c else eps

    def w_derived(prev, m):
        if m not in c:
            return eps
        if prev is None:
            return ic[m] / G if ic[m] > 0 else c[m] / N
        if pc[(prev, m)] > 0:
            return pc[(prev, m)] / st[prev]
        return c[m] / N

    base = derived = n = 0
    for g in reserve_groups:
        for i, m in enumerate(g):
            prev = g[i - 1] if i else None
            base += -math.log(w_base(m))
            derived += -math.log(w_derived(prev, m))
            n += 1
    return base / n, derived / n


# ---------------------------------------------------------------- scorer B
def score_b(deriv_groups, reserve_groups):
    """Independent implementation: context-grouped accumulation."""
    uni = Counter(m for g in deriv_groups for m in g)
    N = sum(uni.values())
    V = len(uni)
    G = len(deriv_groups)
    eps = 1.0 / (N + V)
    initial = Counter(g[0] for g in deriv_groups)
    succ = defaultdict(Counter)
    for g in deriv_groups:
        for a, b in zip(g, g[1:]):
            succ[a][b] += 1
    succ_tot = {a: sum(s.values()) for a, s in succ.items()}

    contexts = Counter()
    for g in reserve_groups:
        contexts[(None, g[0])] += 1
        for a, b in zip(g, g[1:]):
            contexts[(a, b)] += 1
    base = derived = n = 0
    for (prev, m), k in contexts.items():
        if m in uni:
            wb = uni[m] / N
            if prev is None:
                wd = initial[m] / G if initial[m] > 0 else wb
            elif succ[prev][m] > 0:
                wd = succ[prev][m] / succ_tot[prev]
            else:
                wd = wb
        else:
            wb = wd = eps
        base += -math.log(wb) * k
        derived += -math.log(wd) * k
        n += k
    return base / n, derived / n


def advantage(deriv_groups, reserve_groups):
    ba, da = score_a(deriv_groups, reserve_groups)
    bb, db = score_b(deriv_groups, reserve_groups)
    adv_a, adv_b = ba - da, bb - db
    if abs(adv_a - adv_b) > 1e-6:
        raise AssertionError(f"scorer disagreement: {adv_a} vs {adv_b}")
    return adv_a


# ---------------------------------------------------------------- shaping
def make_replication(donor_groups, inventory_sorted, shape, scale, rng):
    total_groups = len(donor_groups)
    starts = [0]
    for g in donor_groups:
        starts.append(starts[-1] + len(g))
    n_art = int(round(shape["artifacts"] * scale))
    lengths = shape["lengths"]
    artifacts = []
    for _ in range(n_art):
        L = rng.choice(lengths)
        start = rng.randrange(total_groups)
        art, got, idx = [], 0, start
        while got < L:
            g = donor_groups[idx % total_groups]
            art.append(tuple(g))
            got += len(g)
            idx += 1
        artifacts.append(tuple(art))
    n_dup = int(round(shape["duplication_rate"] * n_art))
    if n_dup:
        for tgt in rng.sample(range(n_art), n_dup):
            src = rng.randrange(n_art)
            if src != tgt:
                artifacts[tgt] = artifacts[src]
    perm = inventory_sorted[:]
    rng.shuffle(perm)
    cipher = dict(zip(inventory_sorted, perm))
    ciphered = [tuple(tuple(cipher[m] for m in g) for g in art)
                for art in artifacts]
    seen, distinct = set(), []
    for art in ciphered:
        if art not in seen:
            seen.add(art)
            distinct.append(art)
    side = {art: (i % 5 == 4) for i, art in enumerate(distinct)}
    deriv = [g for art in ciphered if not side[art] for g in art]
    reserve = [g for art in ciphered if side[art] for g in art]
    sample = deriv + reserve
    return deriv, reserve, sample, len(distinct), cipher


def rank_map(deriv_a, deriv_b):
    """Map donor A's labels to donor B's labels by derivation frequency
    rank (ties by label). Returns dict A-label -> B-label or None."""
    def ranked(deriv):
        freq = Counter(m for g in deriv for m in g)
        return sorted(freq, key=lambda m: (-freq[m], m))
    ra, rb = ranked(deriv_a), ranked(deriv_b)
    return {a: (rb[i] if i < len(rb) else None) for i, a in enumerate(ra)}


def positional_stats(sample_groups):
    pos = defaultdict(Counter)
    pairs = set()
    for g in sample_groups:
        if len(g) == 1:
            pos[g[0]]["sole"] += 1
            continue
        for i, m in enumerate(g):
            pos[m]["initial" if i == 0 else
                    "final" if i == len(g) - 1 else "medial"] += 1
        pairs.update(zip(g, g[1:]))
    return pos, pairs


def r2(sample_groups, truth_restricted, cipher):
    pos, _ = positional_stats(sample_groups)
    truth = {cipher[m]: k for m, k in truth_restricted.items()}
    if len(truth) < 5:
        return None
    detected = {}
    for m, c in pos.items():
        total = sum(c.values())
        if total < 20:
            continue
        if (c["initial"] + c["sole"]) / total >= 0.99:
            detected[m] = "initial"
        elif (c["final"] + c["sole"]) / total >= 0.99:
            detected[m] = "final"
    tp = sum(1 for m, k in truth.items()
             if sum(pos[m].values()) >= 20 and detected.get(m) == k)
    measurable = sum(1 for m in truth if sum(pos[m].values()) >= 20)
    fp_base = sum(1 for m in detected if m not in truth)
    fp_denom = sum(1 for m, c in pos.items() if sum(c.values()) >= 20)
    return {"sensitivity": (tp / measurable) if measurable else None,
            "measurable_truth_marks": measurable,
            "false_positive_rate": (fp_base / fp_denom) if fp_denom else None}


def r3(sample_groups, truth_top100, cipher):
    _, pairs = positional_stats(sample_groups)
    truth = {(cipher[a], cipher[b]) for a, b in truth_top100}
    return sum(1 for p in truth if p in pairs) / len(truth)


# ---------------------------------------------------------------- main
def main():
    out_path, custody_dir = sys.argv[1], sys.argv[2]
    shape = target_shape()
    log(f"target shape: {shape['artifacts']} artifacts, {shape['tokens']} "
        f"tokens, inventory {shape['inventory']}, duplication "
        f"d={shape['duplication_rate']:.4f}")
    donors = {}
    mero = meroitic_stream()
    donors["meroitic"] = {"groups": mero, "pin": {"file": KOVETSKY,
                                                 "sha256": KOVETSKY_SHA256}}
    latin, latin_pin = latin_stream(custody_dir)
    donors["latin"] = {"groups": latin, "pin": latin_pin}
    log(f"donor B pinned before scoring: {latin_pin['sha256'][:16]}... "
        f"({latin_pin['bytes']} bytes); latin groups {len(latin)}")
    for name, d in donors.items():
        d["inventory"] = sorted({m for g in d["groups"] for m in g})
        d["truth_restricted"], d["truth_top100"] = ground_truth(d["groups"])
        log(f"donor {name}: inventory {len(d['inventory'])}, ground-truth "
            f"restricted marks {len(d['truth_restricted'])}")

    cells_done = 0
    results = {}
    reps_cache = {}
    for scale in SCALES:
        for rep in range(1, REPS + 1):
            for name in ("meroitic", "latin"):
                d = donors[name]
                rng = random.Random(f"spec107-i1-{name}-{scale}-{rep}")
                reps_cache[(name, scale, rep)] = make_replication(
                    d["groups"], d["inventory"], shape, scale, rng)
        for name in ("meroitic", "latin"):
            other = "latin" if name == "meroitic" else "meroitic"
            rows = []
            for rep in range(1, REPS + 1):
                deriv, reserve, sample, n_distinct, cipher = \
                    reps_cache[(name, scale, rep)]
                adv_right = advantage(deriv, reserve)
                o_deriv = reps_cache[(other, scale, rep)][0]
                mapping = rank_map(deriv, o_deriv)
                # Translate the reserve into the wrong model's label
                # space by frequency rank. A target type with no aligned
                # counterpart becomes the UNMAPPED sentinel, which is
                # outside the wrong derivation's inventory and so scores
                # at epsilon under both models (registration section 2);
                # groups are never dropped.
                o_reserve = [tuple(mapping[m] if mapping.get(m) is not None
                                   else UNMAPPED for m in g)
                             for g in reserve]
                adv_wrong = advantage(o_deriv, o_reserve)
                shuf_rng = random.Random(f"spec107-i1-{name}-{scale}-{rep}-shuffle")
                shuf = []
                for g in deriv:
                    gg = list(g)
                    shuf_rng.shuffle(gg)
                    shuf.append(tuple(gg))
                adv_shuffle = advantage(shuf, reserve)
                rows.append({
                    "rep": rep, "advantage_right": adv_right,
                    "advantage_wrong": adv_wrong,
                    "advantage_shuffle": adv_shuffle,
                    "derivation_tokens": sum(len(g) for g in deriv),
                    "reserve_tokens": sum(len(g) for g in reserve),
                    "distinct_artifacts": n_distinct,
                    "r2": r2(sample, donors[name]["truth_restricted"], cipher),
                    "r3": r3(sample, donors[name]["truth_top100"], cipher),
                })
            results[f"{name}|{scale}"] = rows
            cells_done += 1
            med = {k: median(r[k] for r in rows) for k in
                   ("advantage_right", "advantage_wrong", "advantage_shuffle")}
            log(f"cell {name} x{scale} done ({cells_done}/6 cells): "
                f"median advantages R {med['advantage_right']:.4f} / "
                f"W {med['advantage_wrong']:.4f} / S {med['advantage_shuffle']:.4f}")

    verdict = evaluate(results)
    log(f"I-1 verdict: {verdict['verdict']}")
    json.dump({"test": "I-1 (Spec 107 cycle 1)", "target_shape": shape,
               "donor_pins": {k: v["pin"] for k, v in donors.items()},
               "ground_truth": {k: {"restricted": v["truth_restricted"],
                                    "top100_pairs": [list(p) for p in v["truth_top100"]]}
                                for k, v in donors.items()},
               "results": results, "verdict": verdict},
              open(out_path, "w"), indent=1, ensure_ascii=False)
    log(f"raw output written to {out_path}")
    return 0


def evaluate(results):
    """The registered verdict rule (registration section 2), at 1x."""
    per = {}
    for name in ("meroitic", "latin"):
        rows = results[f"{name}|1.0"]
        r2s = [r["r2"] for r in rows if r["r2"] is not None]
        per[name] = {
            "median_right": median(r["advantage_right"] for r in rows),
            "median_wrong": median(r["advantage_wrong"] for r in rows),
            "median_shuffle": median(r["advantage_shuffle"] for r in rows),
            "r2_measurable": len(r2s) > 0,
            "r2_median_sensitivity": (median(x["sensitivity"] for x in r2s
                                             if x["sensitivity"] is not None)
                                      if r2s else None),
            "r2_median_fpr": (median(x["false_positive_rate"] for x in r2s
                                     if x["false_positive_rate"] is not None)
                              if r2s else None),
        }

    def r1_positive(d):
        return (d["median_right"] >= 0.05
                and d["median_right"] >= 2 * max(d["median_wrong"],
                                                 d["median_shuffle"]))

    def r1_negative(d):
        return (d["median_right"] < 0.05
                or max(d["median_wrong"], d["median_shuffle"])
                >= 0.5 * d["median_right"])

    def r2_ok(d):
        return (d["r2_median_sensitivity"] is not None
                and d["r2_median_sensitivity"] >= 0.50
                and d["r2_median_fpr"] is not None
                and d["r2_median_fpr"] <= 0.10)

    # Per-donor states under the registered rule. A donor is NEGATIVE
    # iff its R1 negative conditions hold; POSITIVE iff its R1 positive
    # conditions hold and its R2 clause passes (the R2 clause binds a
    # donor only where R2 is measurable for that donor; where it is
    # measurable for exactly one donor, that donor's clause alone is
    # evaluated); otherwise the donor is in the middle zone.
    evals = {}
    for name, d in per.items():
        if r1_negative(d):
            evals[name] = "NEGATIVE"
        elif r1_positive(d) and (not d["r2_measurable"] or r2_ok(d)):
            evals[name] = "POSITIVE"
        else:
            evals[name] = "MIDDLE"
    # Test verdict: NEGATIVE iff either donor is NEGATIVE; POSITIVE
    # iff both are POSITIVE — except that R2 measurable for neither
    # donor while R1 is positive for both is INDETERMINATE; every
    # other configuration (donor disagreement) is INDETERMINATE.
    if any(v == "NEGATIVE" for v in evals.values()):
        verdict = "NEGATIVE"
    elif all(v == "POSITIVE" for v in evals.values()):
        if not any(d["r2_measurable"] for d in per.values()):
            verdict = "INDETERMINATE"
        else:
            verdict = "POSITIVE"
    else:
        verdict = "INDETERMINATE"
    return {"per_donor_1x": per, "donor_evaluations": evals,
            "verdict": verdict}


if __name__ == "__main__":
    sys.exit(main())
