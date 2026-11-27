#!/usr/bin/env python3
"""Spec 107, test I-2 — Indus scramble-simulation identifiability
calibration, cycle 2. Executes the registration filed at
specs/107-active-decipherment-loop/records/cycle-2-registration-2026-11-27.md
section 3, under the owner's OD-O-1 ruling (2026-11-27 08:27 ET).

The machinery is I-1's, by reference: the same two donor corpora
(Meroitic from the pinned Kovetsky build; Latin, Caesar's De Bello
Gallico from Project Gutenberg, bytes pinned in custody at cycle 1),
the same target shape (Spec 105 custody datasets), the same cipher
and duplicate-aware split, the same G-IND-form predictor (Spec 105
Stage 6 registration section 5, weights as registered,
unnormalized) scored by two independent implementations that must
agree to six decimal places on every replication (TC-107-02), and
the same RIGHT / WRONG / SHUFFLE conditions and R1 statistic.

What cycle 2 changes, and only this:

1. The duplication construction. I-1's generator missed its
   registered duplication rate (Round O finding). Here each
   replication first admits U = A' - floor(d x A') DISTINCT
   artifact sequences by admission sampling under I-1's reshaping
   (a drawn sequence is admitted only if not already in the
   sample; the draw cap is 200 x A' draws per replication), and
   the remaining floor(d x A') sample slots are exact copies of
   held sequences chosen uniformly at random, so the achieved
   duplication rate (A' - U)/A' meets the registered rate at
   every scale in the grid (floor(20/1670 x 835) = 10,
   floor(20/1670 x 1670) = 20, floor(20/1670 x 3340) = 40).

2. The OD-O-1 PREFLIGHT, run over the full grid before any
   scoring: (1) the target shape recomputed from the Spec 105
   custody datasets must reproduce the registered values
   (A = 1,670 artifacts, T = 7,002 tokens, inventory 390,
   d = 20/1670 exactly); (2) every replication's achieved
   duplication rate must lie within +/-0.01 of d; (3) the R2
   ground-truth sets at rho = 0.95 and rho = 0.90, computed by
   two independent implementations, must agree exactly. Any
   preflight failure stops the run before scoring: the failure,
   with its figures, is written to the raw-output path as I-2's
   outcome and the script exits 3. No scoring number is produced
   by a run whose preflight failed.

3. R2 re-specified at realistic restriction levels. Ground
   truth is computed on the donor stream at the occurrence
   threshold 20, over NON-SOLE occurrences: a mark's class is
   the class of its larger non-sole share (initial vs final);
   it is in the ground-truth restricted set at level rho iff
   its larger non-sole share is >= rho. Marks occurring only as
   sole artifacts are excluded entirely. An exact tie between
   the two shares has no larger share and is not restricted.
   Detection mirrors this on the sample. The verdict is taken
   at 1x at rho*, the strictest level measurable for the donor
   (measurability: the median over replications of the count of
   ground-truth marks restricted in the sample is >= 5); PASS
   at a level is median sensitivity >= 0.50 and median false-
   positive rate <= 0.10. R3 is description only, as in I-1.

Seeds: random.Random("spec107-i2-{donor}-{scale}-{rep}").
Writes the raw-output JSON (argv[1]); argv[2] is the custody
dir holding donor B's pinned bytes.
"""
import hashlib
import json
import math
import random
import sys
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from statistics import median

KOVETSKY = "/home/tpierson/.syncyard/worktrees/glossa/kovetsky-src/data/inscriptions.jsonl"
KOVETSKY_SHA256 = "1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4"
CUSTODY105 = "/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/spec105"
LATIN_URL = "https://www.gutenberg.org/cache/epub/218/pg218.txt"
LATIN_MIRRORS = ["https://gutenberg.pglaf.org/cache/epub/218/pg218.txt"]
SCALES = (0.5, 1.0, 2.0)
REPS = 20
RHOS = (0.95, 0.90)
UNMAPPED = "\x00UNMAPPED"
REGISTERED_SHAPE = {"artifacts": 1670, "tokens": 7002, "inventory": 390}
REGISTERED_D = Fraction(20, 1670)


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] I-2 {msg}", flush=True)


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
        fetched_from = "custody (acquired at cycle 1)"
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


def top100_pairs(groups):
    pairs = Counter()
    for g in groups:
        pairs.update(zip(g, g[1:]))
    return [tuple(p) for p, _ in pairs.most_common(100)]


# ------------------------------------------------------- R2 ground truth
def truth_r2_impl_a(groups, rho):
    """Implementation A: direct positional pass. Per mark, counts
    over non-sole occurrences by position class."""
    total = Counter()
    pos = defaultdict(Counter)
    for g in groups:
        total.update(g)
        if len(g) == 1:
            continue
        for i, m in enumerate(g):
            pos[m]["initial" if i == 0 else
                    "final" if i == len(g) - 1 else "medial"] += 1
    out = {}
    for m, t in total.items():
        if t < 20:
            continue
        ns = sum(pos[m].values())
        if ns == 0:
            continue  # sole-only: excluded entirely
        si = pos[m]["initial"] / ns
        sf = pos[m]["final"] / ns
        if si != sf and max(si, sf) >= rho:
            out[m] = "initial" if si > sf else "final"
    return out


def truth_r2_impl_b(groups, rho):
    """Implementation B: boundary counters. Initial/final counts
    from group boundaries; non-sole totals from multi-mark groups
    only. Independent code path from implementation A."""
    total = Counter()
    init = Counter()
    fin = Counter()
    nonsole_total = Counter()
    for g in groups:
        total.update(g)
        if len(g) >= 2:
            init[g[0]] += 1
            fin[g[-1]] += 1
            nonsole_total.update(g)
    out = {}
    for m, t in total.items():
        if t < 20 or nonsole_total[m] == 0:
            continue
        si = init[m] / nonsole_total[m]
        sf = fin[m] / nonsole_total[m]
        if si != sf and max(si, sf) >= rho:
            out[m] = "initial" if si > sf else "final"
    return out


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
    n_dup_exact = len(full) - len(set(full))
    return {"artifacts": len(full), "tokens": sum(lengths),
            "lengths": lengths, "inventory": len(inventory),
            "duplication_rate": n_dup_exact / len(full),
            "duplicated_artifacts": n_dup_exact,
            "lengths_multiset_sha256": hashlib.sha256(
                json.dumps(sorted(lengths)).encode()).hexdigest()}


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
    """The cycle-2 duplication construction (registration section 3).

    Admits U = A' - floor(d x A') distinct artifact sequences by
    admission sampling under I-1's reshaping, then fills the
    remaining floor(d x A') slots with exact copies of held
    sequences chosen uniformly at random. Returns None if the
    draw cap (200 x A') is reached before U distinct sequences
    are held — a preflight failure. Otherwise returns the
    replication with its achieved duplication rate."""
    total_groups = len(donor_groups)
    starts = [0]
    for g in donor_groups:
        starts.append(starts[-1] + len(g))
    n_art = int(round(shape["artifacts"] * scale))
    lengths = shape["lengths"]
    n_dup = (shape["duplicated_artifacts"] * n_art) // shape["artifacts"]
    n_unique = n_art - n_dup
    cap = 200 * n_art
    admitted, seen = [], set()
    draws = 0
    while len(admitted) < n_unique:
        draws += 1
        if draws > cap:
            return None
        L = rng.choice(lengths)
        start = rng.randrange(total_groups)
        art, got, idx = [], 0, start
        while got < L:
            g = donor_groups[idx % total_groups]
            art.append(tuple(g))
            got += len(g)
            idx += 1
        art = tuple(art)
        if art not in seen:
            seen.add(art)
            admitted.append(art)
    sample_raw = list(admitted)
    for _ in range(n_dup):
        sample_raw.append(admitted[rng.randrange(n_unique)])
    achieved = (n_art - len(seen)) / n_art
    perm = inventory_sorted[:]
    rng.shuffle(perm)
    cipher = dict(zip(inventory_sorted, perm))
    ciphered = [tuple(tuple(cipher[m] for m in g) for g in art)
                for art in sample_raw]
    seen2, distinct = set(), []
    for art in ciphered:
        if art not in seen2:
            seen2.add(art)
            distinct.append(art)
    side = {art: (i % 5 == 4) for i, art in enumerate(distinct)}
    deriv = [g for art in ciphered if not side[art] for g in art]
    reserve = [g for art in ciphered if side[art] for g in art]
    sample = deriv + reserve
    return {"deriv": deriv, "reserve": reserve, "sample": sample,
            "n_distinct": len(distinct), "cipher": cipher,
            "achieved_duplication": achieved, "draws": draws,
            "n_artifacts": n_art, "n_unique": n_unique}


def rank_map(deriv_a, deriv_b):
    """Map donor A's labels to donor B's labels by derivation frequency
    rank (ties by label). Returns dict A-label -> B-label or None."""
    def ranked(deriv):
        freq = Counter(m for g in deriv for m in g)
        return sorted(freq, key=lambda m: (-freq[m], m))
    ra, rb = ranked(deriv_a), ranked(deriv_b)
    return {a: (rb[i] if i < len(rb) else None) for i, a in enumerate(ra)}


def sample_positional_stats(sample_groups):
    total = Counter()
    init = Counter()
    fin = Counter()
    nonsole_total = Counter()
    pairs = set()
    for g in sample_groups:
        total.update(g)
        if len(g) >= 2:
            init[g[0]] += 1
            fin[g[-1]] += 1
            nonsole_total.update(g)
            pairs.update(zip(g, g[1:]))
    return total, init, fin, nonsole_total, pairs


def r2_at_level(stats, truth_restricted_ciphered, rho):
    """Detection and scoring at one level rho, per the registered
    re-specification. truth_restricted_ciphered maps ciphered mark ->
    class. Returns sensitivity (None when no ground-truth mark is
    restricted in the sample), the false-positive rate, and the
    measurability count."""
    total, init, fin, nonsole_total, _ = stats
    detected = {}
    for m, t in total.items():
        if t < 20 or nonsole_total[m] == 0:
            continue
        si = init[m] / nonsole_total[m]
        sf = fin[m] / nonsole_total[m]
        if si != sf and max(si, sf) >= rho:
            detected[m] = "initial" if si > sf else "final"
    in_sample = [m for m in truth_restricted_ciphered
                 if total[m] >= 20]
    hits = sum(1 for m in in_sample
               if detected.get(m) == truth_restricted_ciphered[m])
    denom = sum(1 for m, t in total.items()
                if t >= 20 and nonsole_total[m] > 0)
    fps = sum(1 for m in detected if m not in truth_restricted_ciphered)
    return {"sensitivity": (hits / len(in_sample)) if in_sample else None,
            "false_positive_rate": (fps / denom) if denom else None,
            "truth_in_sample": len(in_sample),
            "detected": len(detected)}


def r3(sample_groups, truth_top100, cipher):
    _, _, _, _, pairset = sample_positional_stats(sample_groups)
    truth = {(cipher[a], cipher[b]) for a, b in truth_top100}
    return sum(1 for p in truth if p in pairset) / len(truth)


# ---------------------------------------------------------------- main
def main():
    out_path, custody_dir = sys.argv[1], sys.argv[2]
    shape = target_shape()
    log(f"target shape recomputed: {shape['artifacts']} artifacts, "
        f"{shape['tokens']} tokens, inventory {shape['inventory']}, "
        f"d={shape['duplication_rate']:.9f}")
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
        d["truth_top100"] = top100_pairs(d["groups"])
        log(f"donor {name}: inventory {len(d['inventory'])}")

    # ---------------------------------------------------------- PREFLIGHT
    log("PREFLIGHT (1/3): target shape against the registered values")
    shape_ok = (shape["artifacts"] == REGISTERED_SHAPE["artifacts"]
                and shape["tokens"] == REGISTERED_SHAPE["tokens"]
                and shape["inventory"] == REGISTERED_SHAPE["inventory"]
                and Fraction(shape["duplicated_artifacts"],
                             shape["artifacts"]) == REGISTERED_D)
    preflight = {"shape_check": {
        "artifacts": shape["artifacts"], "tokens": shape["tokens"],
        "inventory": shape["inventory"],
        "duplicated_artifacts": shape["duplicated_artifacts"],
        "lengths_multiset_sha256": shape["lengths_multiset_sha256"],
        "pass": shape_ok}}
    failures = []
    if not shape_ok:
        failures.append("target shape does not reproduce the "
                        "registered values")

    log("PREFLIGHT (2/3): constructing all 120 replications; "
        "achieved duplication measured per replication")
    reps_cache = {}
    dup_record = {}
    constructed = 0
    for scale in SCALES:
        for rep in range(1, REPS + 1):
            for name in ("meroitic", "latin"):
                d = donors[name]
                rng = random.Random(f"spec107-i2-{name}-{scale}-{rep}")
                r = make_replication(d["groups"], d["inventory"],
                                     shape, scale, rng)
                if r is None:
                    failures.append(
                        f"draw cap reached: {name} x{scale} rep {rep}")
                    r = {"deriv": [], "reserve": [], "sample": [],
                         "n_distinct": 0, "cipher": {},
                         "achieved_duplication": None, "draws": None,
                         "n_artifacts": int(round(
                             shape["artifacts"] * scale)),
                         "n_unique": None}
                reps_cache[(name, scale, rep)] = r
                dup_record[f"{name}|{scale}|{rep}"] = \
                    r["achieved_duplication"]
                constructed += 1
                if constructed % 20 == 0:
                    log(f"preflight construction {constructed}/120 "
                        f"replications")
    dup_failures = [k for k, v in dup_record.items()
                    if v is None
                    or abs(v - float(REGISTERED_D)) > 0.01]
    if dup_failures:
        failures.append(
            f"achieved duplication outside +/-0.01 of d in "
            f"{len(dup_failures)} replication(s): {dup_failures[:6]}")
    preflight["duplication"] = {
        "registered_d": float(REGISTERED_D),
        "per_replication": dup_record,
        "all_within_tolerance": not dup_failures,
        "min": min(v for v in dup_record.values() if v is not None),
        "max": max(v for v in dup_record.values() if v is not None)}
    log(f"preflight duplication: min "
        f"{preflight['duplication']['min']:.6f}, max "
        f"{preflight['duplication']['max']:.6f}, registered "
        f"{float(REGISTERED_D):.6f}; failures so far: {len(failures)}")

    log("PREFLIGHT (3/3): R2 ground-truth sets by two implementations")
    truth_sets = {}
    agreement = {}
    for name, d in donors.items():
        truth_sets[name] = {}
        agreement[name] = {}
        for rho in RHOS:
            a = truth_r2_impl_a(d["groups"], rho)
            b = truth_r2_impl_b(d["groups"], rho)
            agreement[name][str(rho)] = (a == b)
            if a != b:
                failures.append(
                    f"ground-truth disagreement at {name} rho={rho}: "
                    f"A {len(a)} marks vs B {len(b)} marks")
            truth_sets[name][str(rho)] = a
            log(f"donor {name} rho={rho}: ground-truth restricted "
                f"marks {len(a)}; implementations agree: {a == b}")
    preflight["ground_truth"] = {
        "agreement": agreement,
        "set_sizes": {n: {r: len(s) for r, s in v.items()}
                      for n, v in truth_sets.items()}}
    preflight["failures"] = failures
    preflight["pass"] = not failures

    if failures:
        log(f"PREFLIGHT FAILED ({len(failures)} failure(s)); no "
            f"scoring runs. Failures: {failures}")
        json.dump({"test": "I-2 (Spec 107 cycle 2)",
                   "outcome": "PREFLIGHT FAILURE — no scoring run",
                   "target_shape": {k: shape[k] for k in
                                    ("artifacts", "tokens", "inventory",
                                     "duplication_rate",
                                     "lengths_multiset_sha256")},
                   "donor_pins": {k: v["pin"] for k, v in donors.items()},
                   "preflight": preflight, "verdict": None},
                  open(out_path, "w"), indent=1, ensure_ascii=False)
        log(f"preflight failure record written to {out_path}")
        return 3
    log("PREFLIGHT PASSED: shape exact, duplication within tolerance "
        "in 120/120 replications, ground-truth sets in exact "
        "two-implementation agreement")

    # ------------------------------------------------------------ SCORING
    cells_done = 0
    results = {}
    for scale in SCALES:
        for name in ("meroitic", "latin"):
            other = "latin" if name == "meroitic" else "meroitic"
            rows = []
            for rep in range(1, REPS + 1):
                r = reps_cache[(name, scale, rep)]
                deriv, reserve, sample = r["deriv"], r["reserve"], \
                    r["sample"]
                cipher = r["cipher"]
                adv_right = advantage(deriv, reserve)
                o_deriv = reps_cache[(other, scale, rep)]["deriv"]
                mapping = rank_map(deriv, o_deriv)
                o_reserve = [tuple(mapping[m] if mapping.get(m)
                                   is not None else UNMAPPED
                                   for m in g) for g in reserve]
                adv_wrong = advantage(o_deriv, o_reserve)
                shuf_rng = random.Random(
                    f"spec107-i2-{name}-{scale}-{rep}-shuffle")
                shuf = []
                for g in deriv:
                    gg = list(g)
                    shuf_rng.shuffle(gg)
                    shuf.append(tuple(gg))
                adv_shuffle = advantage(shuf, reserve)
                stats = sample_positional_stats(sample)
                r2 = {}
                for rho in RHOS:
                    truth_c = {cipher[m]: k for m, k in
                               truth_sets[name][str(rho)].items()}
                    r2[str(rho)] = r2_at_level(stats, truth_c, rho)
                rows.append({
                    "rep": rep, "advantage_right": adv_right,
                    "advantage_wrong": adv_wrong,
                    "advantage_shuffle": adv_shuffle,
                    "derivation_tokens": sum(len(g) for g in deriv),
                    "reserve_tokens": sum(len(g) for g in reserve),
                    "distinct_artifacts": r["n_distinct"],
                    "achieved_duplication": r["achieved_duplication"],
                    "r2": r2,
                    "r3": r3(sample, donors[name]["truth_top100"],
                             cipher),
                })
            results[f"{name}|{scale}"] = rows
            cells_done += 1
            med = {k: median(r[k] for r in rows) for k in
                   ("advantage_right", "advantage_wrong",
                    "advantage_shuffle")}
            log(f"cell {name} x{scale} done ({cells_done}/6 cells): "
                f"median advantages R {med['advantage_right']:.4f} / "
                f"W {med['advantage_wrong']:.4f} / "
                f"S {med['advantage_shuffle']:.4f}")

    verdict = evaluate(results)
    log(f"I-2 verdict: {verdict['verdict']}")
    json.dump({"test": "I-2 (Spec 107 cycle 2)",
               "target_shape": {k: shape[k] for k in
                                ("artifacts", "tokens", "inventory",
                                 "duplication_rate",
                                 "lengths_multiset_sha256")},
               "donor_pins": {k: v["pin"] for k, v in donors.items()},
               "preflight": preflight,
               "ground_truth_r2": truth_sets,
               "ground_truth_top100_pairs": {
                   k: [list(p) for p in v["truth_top100"]]
                   for k, v in donors.items()},
               "results": results, "verdict": verdict},
              open(out_path, "w"), indent=1, ensure_ascii=False)
    log(f"raw output written to {out_path}")
    return 0


def evaluate(results):
    """The registered verdict rule (registration section 3), at 1x,
    with R2 at each donor's rho*."""
    per = {}
    for name in ("meroitic", "latin"):
        rows = results[f"{name}|1.0"]
        d = {"median_right": median(r["advantage_right"] for r in rows),
             "median_wrong": median(r["advantage_wrong"] for r in rows),
             "median_shuffle": median(r["advantage_shuffle"]
                                      for r in rows),
             "r2_by_rho": {}}
        for rho in RHOS:
            lvl = [r["r2"][str(rho)] for r in rows]
            sens = [x["sensitivity"] for x in lvl
                    if x["sensitivity"] is not None]
            d["r2_by_rho"][str(rho)] = {
                "measurable": median(x["truth_in_sample"]
                                     for x in lvl) >= 5,
                "median_truth_in_sample": median(
                    x["truth_in_sample"] for x in lvl),
                "median_sensitivity": median(sens) if sens else None,
                "median_fpr": median(x["false_positive_rate"]
                                     for x in lvl
                                     if x["false_positive_rate"]
                                     is not None),
            }
        d["rho_star"] = next(
            (str(rho) for rho in RHOS
             if d["r2_by_rho"][str(rho)]["measurable"]), None)
        per[name] = d

    def r1_positive(d):
        return (d["median_right"] >= 0.05
                and d["median_right"] >= 2 * max(d["median_wrong"],
                                                 d["median_shuffle"]))

    def r1_negative(d):
        return (d["median_right"] < 0.05
                or max(d["median_wrong"], d["median_shuffle"])
                >= 0.5 * d["median_right"])

    def r2_ok(d):
        lvl = d["r2_by_rho"][d["rho_star"]]
        return (lvl["median_sensitivity"] is not None
                and lvl["median_sensitivity"] >= 0.50
                and lvl["median_fpr"] is not None
                and lvl["median_fpr"] <= 0.10)

    evals = {}
    for name, d in per.items():
        if r1_negative(d):
            evals[name] = "NEGATIVE"
        elif r1_positive(d) and (d["rho_star"] is None or r2_ok(d)):
            evals[name] = "POSITIVE"
        else:
            evals[name] = "MIDDLE"
    if any(v == "NEGATIVE" for v in evals.values()):
        verdict = "NEGATIVE"
    elif all(v == "POSITIVE" for v in evals.values()):
        if not any(d["rho_star"] is not None for d in per.values()):
            verdict = "INDETERMINATE"
        else:
            verdict = "POSITIVE"
    else:
        verdict = "INDETERMINATE"
    return {"per_donor_1x": per, "donor_evaluations": evals,
            "verdict": verdict}


if __name__ == "__main__":
    sys.exit(main())
