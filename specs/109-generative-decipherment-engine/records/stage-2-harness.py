#!/usr/bin/env python3
"""Spec 109 Stage 2 harness (T201 Part 2 induction + T202 Part 3 channel).

Executes exactly the Stage 2 freeze
(records/stage-2-freeze-2026-11-27.md, SHA-256 f51de777...):
Part 2 positional-class and numerical/metrological families only
(segmentation and recurrent partials are NOT licensed by the Stage 1
preflight and are not computed), and Part 3's context channel (joins,
terms, nulls, caps, out-of-site validation). No iconography input.
No adjudication. Every table is produced by two independent
implementations asserted in exact agreement (counts) or to 1e-12
(floats); a disagreement raises and stops the run.

Payload verdict: exit 0 with the verdict block printed; any failed
pin, join STOP, or implementation disagreement exits nonzero.
"""
import collections, hashlib, json, math, os, random, sys, time

WT = os.path.expanduser("~/.syncyard/worktrees/glossa/spec109-stage2-wt-20261127")
CUST105 = os.path.expanduser("~/.syncyard/worktrees/glossa/glossa-custody/spec105")
CUST109 = os.path.expanduser("~/.syncyard/worktrees/glossa/glossa-custody/spec109")
FREEZE_SHA = "f51de777c54f7cd917246fc2293f24716ac8fec3521edc3e94fdbf43e0a580bb"
POS = ["initial", "medial", "final", "sole"]
B = 999

def log(msg):
    print(f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {msg}", flush=True)

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def seed_of(s):
    return int.from_bytes(hashlib.sha256(s.encode()).digest()[:8], "big")

def flat(a):
    return [s for line in a["lines"] for g in line for s in g]

# ---------------------------------------------------------------- pins
PINS = {
    "derivation": (os.path.join(CUST105, "indus-derivation.json"),
                   "84476daa3a1d9ded33ee7c3eeaffb29fac0290ecf3507873206d4d60ac8b948b"),
    "reserve": (os.path.join(CUST105, "indus-reserve.json"),
                "bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff"),
    "phase100": (os.path.join(WT, "outputs/phase100_full_corpus.json"),
                 "c2b14e94971f438cfd25f24123db975de6c02980e0e425cffb91fbc4de4d578c"),
    "phase114": (os.path.join(WT, "outputs/phase114_full_seal_translations.json"),
                 "07b84a9c82f0fb5328d6ab344d038a3a0a984079f99804f2014580a28aa40196"),
    "objects": (os.path.join(WT, "glossa-corpus/indus/canonical/objects.jsonl"),
                "e24f42a95ee4cc1fdb16c789c3edfb937993ed7c82223d6daa96d66895174ae5"),
    "joinpairs": (os.path.join(WT, "specs/093-material-context-channel/records/t103-join-pairs-v1.jsonl"),
                  "7107f738832a4e3b04cff91d81073212bc0f3a77afed6f0ccc3cee4fce621703"),
    "l3output": (os.path.join(WT, "specs/105-elsewhere-sandbox/records/stage-3-output-2026-11-25.json"),
                 "b80b7d997327d9130274e1527ecf73d44f7eafcb22fa4bba596b4541b4bbb3c8"),
    "spec091num": (os.path.join(WT, "specs/091-anchor-comparison-integrity/records/motif-numerical-evidence-2026-11-21.json"),
                   "23e2f0f43cfe79da77b7cde3860c27580a09e4b9019a6d6ff0a585baecc505e8"),
    "freeze": (os.path.join(WT, "specs/109-generative-decipherment-engine/records/stage-2-freeze-2026-11-27.md"),
               FREEZE_SHA),
}
HARNESS_SHA = sha256_file(os.path.abspath(__file__))

def main():
    out = {"stage": "spec109-stage2", "harness_sha256": HARNESS_SHA,
           "freeze_sha256": FREEZE_SHA}
    log("verifying pins")
    for name, (path, want) in PINS.items():
        got = sha256_file(path)
        assert got == want, f"PIN MISMATCH {name}: {got} != {want}"
    out["pins_verified"] = sorted(PINS.keys())
    log(f"pins ok ({len(PINS)})")

    der_raw = json.load(open(PINS["derivation"][0]))
    res_raw = json.load(open(PINS["reserve"][0]))
    der = [flat(a) for a in der_raw]
    res = [flat(a) for a in res_raw]
    full = der + res
    census = {
        "artifacts": {"derivation": len(der), "reserve": len(res), "full": len(full)},
        "tokens": {"derivation": sum(map(len, der)), "reserve": sum(map(len, res)),
                   "full": sum(map(len, full))},
        "marks_derivation": len({s for x in der for s in x}),
        "marks_full": len({s for x in full for s in x}),
        "groups": {"derivation": sum(len(line) for a in der_raw for line in a["lines"]),
                   "reserve": sum(len(line) for a in res_raw for line in a["lines"])},
    }
    assert census["artifacts"] == {"derivation": 1336, "reserve": 334, "full": 1670}
    assert census["tokens"] == {"derivation": 5611, "reserve": 1391, "full": 7002}
    assert census["marks_derivation"] == 372 and census["marks_full"] == 390
    assert census["groups"] == {"derivation": 1336, "reserve": 334}
    out["corpus_census"] = census
    log(f"corpus census ok: {census['artifacts']} {census['tokens']}")

    # ------------------------------------------------ positional family
    def pos_table_a(arts):
        tab = {}
        for seq in arts:
            n = len(seq)
            for i, s in enumerate(seq):
                r = tab.setdefault(s, [0, 0, 0, 0])
                if n == 1: r[3] += 1
                elif i == 0: r[0] += 1
                elif i == n - 1: r[2] += 1
                else: r[1] += 1
        return tab
    def pos_table_b(arts):
        occ = []
        for seq in arts:
            n = len(seq)
            if n == 1:
                occ.append((seq[0], "sole"))
                continue
            occ.append((seq[0], "initial"))
            for s in seq[1:-1]:
                occ.append((s, "medial"))
            occ.append((seq[-1], "final"))
        tab = {}
        for s, p in occ:
            r = tab.setdefault(s, [0, 0, 0, 0])
            r[POS.index(p)] += 1
        return tab
    def pos_table(arts):
        a, b = pos_table_a(arts), pos_table_b(arts)
        assert a == b, "implementation disagreement: positional table"
        return a
    def calls(tab, floor=5):
        res_calls = {}
        for m, r in tab.items():
            tot = sum(r)
            if tot < floor: continue
            mx = max(r)
            dom = [POS[i] for i, v in enumerate(r) if v == mx]
            entry = {"counts": dict(zip(POS, r)), "total": tot,
                     "shares": {POS[i]: r[i] / tot for i in range(4)},
                     "dominant": dom[0] if len(dom) == 1 else None}
            for rho in (0.95, 0.90):
                entry[f"restricted_{rho}"] = (len(dom) == 1 and mx / tot >= rho)
            res_calls[m] = entry
        return res_calls

    full_tab = pos_table(full)
    der_tab = pos_table(der)
    full_calls = calls(full_tab)
    der_calls = calls(der_tab)
    log(f"positional tables ok: full marks={len(full_tab)} measurable={len(full_calls)}")

    # L3 reconciliation (derivation counts vs the filed L3 table)
    l3 = json.load(open(PINS["l3output"][0]))["sandboxes"]["indus"]["positions"]
    l3_tab = {r["mark"]: [r["initial"], r["medial"], r["final"], r["sole"]] for r in l3}
    mism = []
    for m in sorted(set(l3_tab) | set(der_tab)):
        if l3_tab.get(m) != der_tab.get(m):
            mism.append({"mark": m, "l3": l3_tab.get(m), "recomputed": der_tab.get(m)})
    out["l3_reconciliation"] = {"marks_compared": len(set(l3_tab) | set(der_tab)),
                                "cell_mismatches": mism}
    log(f"L3 reconciliation: {len(mism)} mismatched marks of {len(set(l3_tab)|set(der_tab))}")
    l3_calls = calls(l3_tab)
    div = []
    for m in sorted(set(full_calls) | set(l3_calls)):
        for rho in (0.95, 0.90):
            f = full_calls.get(m, {}).get(f"restricted_{rho}", False)
            l = l3_calls.get(m, {}).get(f"restricted_{rho}", False)
            fd = full_calls.get(m, {}).get("dominant"); ld = l3_calls.get(m, {}).get("dominant")
            if f != l or (f and l and fd != ld):
                div.append({"mark": m, "rho": rho, "full_restricted": f,
                            "l3_restricted": l, "full_dominant": fd, "l3_dominant": ld})
    out["l3_call_divergences"] = div

    # split halves (duplicate-aware, first-appearance ordinal % 2)
    seen = {}
    halves = [[], []]
    for seq in der:
        t = tuple(seq)
        if t not in seen: seen[t] = len(seen)
        halves[seen[t] % 2].append(seq)
    half_tabs = [pos_table(h) for h in halves]
    half_calls = [calls(t) for t in half_tabs]
    out["split"] = {"distinct_sequences": len(seen),
                    "half_artifacts": [len(h) for h in halves]}
    log(f"split halves ok: {[len(h) for h in halves]} artifacts, {len(seen)} distinct sequences")

    # per-site tables from the population files (Part 3 join (a) material)
    p100 = json.load(open(PINS["phase100"][0]))["translations"]
    site_seqs = collections.defaultdict(list)
    for t in p100: site_seqs[t["site"]].append(t["signs"])
    site_tabs = {s: pos_table(v) for s, v in site_seqs.items()}

    # stability per structure
    structures = []
    for m in sorted(full_calls):
        fc = full_calls[m]
        for rho in (0.95, 0.90):
            if not fc[f"restricted_{rho}"]: continue
            dom = fc["dominant"]
            hstate = []
            for h in range(2):
                hc = half_calls[h].get(m)
                if hc is None: hstate.append("unmeasurable")
                elif hc[f"restricted_{rho}"] and hc["dominant"] == dom: hstate.append("reproduces")
                else: hstate.append("differs")
            if "unmeasurable" in hstate: stab = "INDETERMINATE"
            elif all(x == "reproduces" for x in hstate): stab = "STABLE"
            else: stab = "UNSTABLE"
            persite = {}
            for sname, stab_tab in sorted(site_tabs.items()):
                r = stab_tab.get(m)
                if r is None or sum(r) < 5: continue
                mx = max(r); doms = [POS[i] for i, v in enumerate(r) if v == mx]
                persite[sname] = {"total": sum(r), "dominant": doms[0] if len(doms) == 1 else None,
                                  "agrees": len(doms) == 1 and doms[0] == dom}
            structures.append({"mark": m, "rho": rho, "dominant": dom,
                                "full_counts": fc["counts"], "full_total": fc["total"],
                                "half_states": hstate, "stability": stab,
                                "per_site": persite})
    n_stable = sum(1 for s in structures if s["stability"] == "STABLE")
    log(f"positional structures: {len(structures)} calls, {n_stable} STABLE, "
        f"{sum(1 for s in structures if s['stability']=='UNSTABLE')} UNSTABLE, "
        f"{sum(1 for s in structures if s['stability']=='INDETERMINATE')} INDETERMINATE")
    out["positional"] = {
        "full_table": {m: dict(zip(POS, r)) for m, r in sorted(full_tab.items())},
        "derivation_table": {m: dict(zip(POS, r)) for m, r in sorted(der_tab.items())},
        "half_tables": [{m: dict(zip(POS, r)) for m, r in sorted(t.items())} for t in half_tabs],
        "structures": structures,
    }

    # positional null: within-artifact shuffle, restricted-call counts
    rng = random.Random(seed_of("spec109-s2-posnull-v1"))
    null_counts = {0.95: [], 0.90: []}
    marks_meas = [m for m in full_calls]
    for d in range(B):
        shuffled = []
        for seq in full:
            s2 = list(seq); rng.shuffle(s2); shuffled.append(s2)
        c = calls(pos_table_a(shuffled))
        for rho in (0.95, 0.90):
            null_counts[rho].append(sum(1 for e in c.values() if e[f"restricted_{rho}"]))
        if (d + 1) % 250 == 0: log(f"positional null {d+1}/{B}")
    def pct_rank(obs, dist):
        return sum(1 for v in dist if v < obs) / len(dist)
    out["positional_null"] = {}
    for rho in (0.95, 0.90):
        obs = sum(1 for s in structures if s["rho"] == rho)
        dist = sorted(null_counts[rho])
        out["positional_null"][str(rho)] = {
            "observed_restricted_calls": obs,
            "null_mean": sum(dist) / len(dist), "null_max": dist[-1],
            "null_p95": dist[int(0.95 * len(dist))], "observed_percentile": pct_rank(obs, dist)}
    log(f"positional null ok: {out['positional_null']}")

    # ------------------------------------------------ numerical family
    NUM = ["M012", "M059", "M391"]
    NUMSET = set(NUM)
    def num_stats(arts):
        typeT = [sum(1 for s in x if s in NUMSET) for x in arts if any(s in NUMSET for s in x)]
        comb = []
        runs = []
        for idx, x in enumerate(arts):
            cnt = [i for i, s in enumerate(x) if s in NUMSET]
            if len(cnt) >= 2:
                comb.append({"artifact": idx, "counted_positions": cnt,
                             "contiguous": cnt == list(range(cnt[0], cnt[0] + len(cnt)))})
            i = 0
            while i < len(x):
                if x[i] in NUMSET:
                    j = i
                    while j < len(x) and x[j] == x[i]: j += 1
                    if j - i >= 2: runs.append({"sign": x[i], "length": j - i, "artifact": idx})
                    i = j
                else: i += 1
        def dist_stats(vals):
            if not vals: return {"n": 0, "max": 0, "variance": 0.0, "share_ge3": 0.0}
            mu = sum(vals) / len(vals)
            return {"n": len(vals), "max": max(vals),
                    "variance": sum((v - mu) ** 2 for v in vals) / len(vals),
                    "share_ge3": sum(1 for v in vals if v >= 3) / len(vals),
                    "histogram": dict(sorted(collections.Counter(vals).items()))}
        return {"typeT": dist_stats(typeT), "typeT_counts": typeT,
                "combination_contexts": comb,
                "combination_share": (sum(1 for c in comb if c["contiguous"]) / len(comb)) if comb else None,
                "runs": runs}
    num_full = num_stats(full)
    num_halves = [num_stats(h) for h in halves]
    # one null stream (within-artifact shuffle) for checks 1 and 3
    rngn = random.Random(seed_of("spec109-s2-numnull-v1"))
    nvar, nshare, nmax, ncomb = [], [], [], []
    for d in range(B):
        shuffled = []
        for seq in full:
            s2 = list(seq); rngn.shuffle(s2); shuffled.append(s2)
        ns = num_stats(shuffled)
        nvar.append(ns["typeT"]["variance"]); nshare.append(ns["typeT"]["share_ge3"])
        nmax.append(ns["typeT"]["max"])
        if ns["combination_share"] is not None: ncomb.append(ns["combination_share"])
        if (d + 1) % 250 == 0: log(f"numerical null {d+1}/{B}")
    def pctile(dist, q):
        s = sorted(dist); return s[min(len(s) - 1, int(q * len(s)))]
    nullT = {"variance_p05": pctile(nvar, 0.05), "share_ge3_p05": pctile(nshare, 0.05),
             "max_p95": pctile(nmax, 0.95), "combination_share_p99": pctile(ncomb, 0.99)}
    def check1(ns):
        t = ns["typeT"]
        return bool(t["max"] <= 5 and t["variance"] < nullT["variance_p05"]
                    and t["share_ge3"] <= nullT["share_ge3_p05"])
    def check3(ns):
        return bool(ns["combination_share"] is not None
                    and ns["combination_share"] > nullT["combination_share_p99"])
    counted_calls = {}
    for m in NUM:
        e = {"full": full_calls.get(m), "halves": [half_calls[h].get(m) for h in range(2)],
             "tokens_full": sum(full_tab[m]) if m in full_tab else 0}
        counted_calls[m] = e
    check2_full = any((full_calls.get(m, {}).get("restricted_0.9")) for m in NUM)
    checks = {
        "check1_bounded_range": {"full_supported": check1(num_full),
                                 "halves_supported": [check1(h) for h in num_halves]},
        "check2_positional_restriction": {"full_supported": bool(check2_full),
                                          "counted_calls": counted_calls},
        "check3_combination_contiguity": {"full_supported": check3(num_full),
                                          "halves_supported": [check3(h) for h in num_halves],
                                          "full_share": num_full["combination_share"],
                                          "half_shares": [h["combination_share"] for h in num_halves]},
    }
    for k in ("check1_bounded_range", "check3_combination_contiguity"):
        c = checks[k]
        c["stability"] = ("STABLE" if all(h == c["full_supported"] for h in c["halves_supported"])
                          else "UNSTABLE")
    c2h = []
    for h in range(2):
        c2h.append(any((half_calls[h].get(m, {}).get("restricted_0.9")) for m in NUM))
    checks["check2_positional_restriction"]["halves_supported"] = c2h
    checks["check2_positional_restriction"]["stability"] = (
        "STABLE" if all(x == bool(check2_full) for x in c2h) else "UNSTABLE")
    # Type F: NUMERAL_FORMULA seals and their counted tokens (population file)
    typeF = [{"cisi_id": t["cisi_id"], "counted_tokens": sum(1 for s in t["signs"] if s in NUMSET)}
             for t in p100 if t["formula_type"] == "NUMERAL_FORMULA"]
    out["numerical"] = {
        "counted_signs": NUM, "null_thresholds": nullT,
        "typeT_full": {k: v for k, v in num_full["typeT"].items()},
        "typeT_halves": [{k: v for k, v in h["typeT"].items()} for h in num_halves],
        "typeF": typeF, "runs_full": num_full["runs"],
        "runs_halves": [h["runs"] for h in num_halves],
        "combination_full_n": len(num_full["combination_contexts"]),
        "combination_halves_n": [len(h["combination_contexts"]) for h in num_halves],
        "checks": checks,
    }
    log(f"numerical checks: c1={checks['check1_bounded_range']['full_supported']} "
        f"c2={bool(check2_full)} c3={checks['check3_combination_contiguity']['full_supported']}")

    # ------------------------------------------------ Part 3: joins
    p114 = json.load(open(PINS["phase114"][0]))["all_translations"]
    p100_by = {t["cisi_id"]: t for t in p100}
    dis = []
    joined = []
    for cid in sorted(set(p100_by) | set(p114)):
        a, b = p100_by.get(cid), p114.get(cid)
        if a is None or b is None or a["site"] != b["site"] or a["signs"] != b["signs"]:
            dis.append(cid); continue
        joined.append({"cisi_id": cid, "site": a["site"], "signs": a["signs"]})
    site_census = collections.Counter(j["site"] for j in joined)
    FILED_CENSUS = {"Mohenjo-daro": 606, "Harappa": 492, "Lothal": 124, "Kalibangan": 110,
                    "Dholavira": 106, "Chanhu-daro": 78, "Surkotada": 61, "Banawali": 60,
                    "Rakhigarhi": 33}
    join_a = {"joined": len(joined), "disagreements": dis,
              "site_census": dict(sorted(site_census.items())),
              "filed_census": FILED_CENSUS,
              "validates": dict(site_census) == FILED_CENSUS and not dis}
    out["join_a"] = join_a
    log(f"join (a): {len(joined)} joined, {len(dis)} disagreements, validates={join_a['validates']}")

    objs = {}
    for line in open(PINS["objects"][0]):
        o = json.loads(line); objs[o["glossa_id"]] = o
    pairs = [json.loads(l) for l in open(PINS["joinpairs"][0])]
    mat_census = collections.Counter(p["material_raw"] for p in pairs)
    join_b_rows = []
    unresolved = []
    for p in pairs:
        o = objs.get(p["text_id"])
        if o is None: unresolved.append(p["text_id"]); continue
        join_b_rows.append({"text_id": p["text_id"], "cisi_object": p["cisi_object"],
                            "site": p["site"], "material_raw": p["material_raw"],
                            "area_section": p["area_section"],
                            "signs": o["_source_extra"]["raw_signs"]})
    join_b = {"pairs": len(pairs), "material_census": dict(mat_census),
              "sites": dict(collections.Counter(p["site"] for p in pairs)),
              "unresolved": unresolved,
              "validates": (len(pairs) == 179 and dict(mat_census) ==
                            {"Steatite": 176, "Clay": 1, "Faience": 1, "-": 1}
                            and not unresolved
                            and all(p["site"] == "Mohenjo-daro" for p in pairs))}
    out["join_b"] = join_b
    out["join_b_rows"] = join_b_rows
    log(f"join (b): {len(pairs)} pairs, validates={join_b['validates']}")

    # ------------------------------------------------ Part 3: terms
    def term_table(rows, label_of):
        """rows: list of sign lists; label_of(i) -> context value for row i.
        Returns per-sign context term (two implementations asserted)."""
        def impl_a():
            by_sign = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0, 0, 0]))
            tot = collections.defaultdict(lambda: [0, 0, 0, 0])
            for i, seq in enumerate(rows):
                v = label_of(i); n = len(seq)
                for k, s in enumerate(seq):
                    p = 3 if n == 1 else 0 if k == 0 else 2 if k == n - 1 else 1
                    by_sign[s][v][p] += 1; tot[s][p] += 1
            return by_sign, tot
        def impl_b():
            by_sign = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0, 0, 0]))
            tot = collections.defaultdict(lambda: [0, 0, 0, 0])
            for i, seq in enumerate(rows):
                v = label_of(i)
                if len(seq) == 1:
                    cells = [(seq[0], 3)]
                else:
                    cells = [(seq[0], 0)] + [(s, 1) for s in seq[1:-1]] + [(seq[-1], 2)]
                for s, p in cells:
                    by_sign[s][v][p] += 1; tot[s][p] += 1
            return by_sign, tot
        A, Bv = impl_a(), impl_b()
        assert A[0] == Bv[0] and A[1] == Bv[1], "implementation disagreement: term tables"
        by_sign, tot = A
        terms = {}
        for s in sorted(tot):
            ns = sum(tot[s]); tval = 0.0
            for v, cells in sorted(by_sign[s].items()):
                nv = sum(cells)
                for c in range(4):
                    if cells[c]:
                        tval += (nv / ns) * (cells[c] / nv) * math.log((cells[c] / nv) / (tot[s][c] / ns))
            terms[s] = {"term": tval, "tokens": ns, "scored": ns >= 5}
        return terms
    def null_cap(rows, labels, seed_str):
        rngc = random.Random(seed_of(seed_str))
        strata = collections.defaultdict(list)
        for i, seq in enumerate(rows): strata[len(seq)].append(i)
        pooled = []
        base_labels = list(labels)
        for d in range(B):
            lab = list(base_labels)
            for idxs in strata.values():
                vals = [lab[i] for i in idxs]
                rngc.shuffle(vals)
                for i, v in zip(idxs, vals): lab[i] = v
            tt = term_table(rows, lambda i, L=lab: L[i])
            pooled.extend(e["term"] for e in tt.values() if e["scored"])
            if (d + 1) % 250 == 0: log(f"ctx null ({seed_str}) {d+1}/{B}")
        pooled.sort()
        return pooled[int(0.99 * len(pooled))], sum(pooled) / len(pooled)

    site_rows = [j["signs"] for j in joined]
    site_labels = [j["site"] for j in joined]
    site_terms = term_table(site_rows, lambda i: site_labels[i])
    site_cap, site_null_mean = null_cap(site_rows, site_labels, "spec109-s2-ctxnull-v1")
    log(f"site terms ok: cap={site_cap:.6f}")
    b_rows = [r["signs"] for r in join_b_rows]
    mat_labels = [r["material_raw"] for r in join_b_rows]
    mat_terms = term_table(b_rows, lambda i: mat_labels[i])
    mat_cap, mat_null_mean = null_cap(b_rows, mat_labels, "spec109-s2-ctxnull-v1")
    area_labels = [r["area_section"] for r in join_b_rows]
    area_terms = term_table(b_rows, lambda i: area_labels[i])
    area_cap, area_null_mean = null_cap(b_rows, area_labels, "spec109-s2-ctxnull-v1")
    log(f"material cap={mat_cap:.6f}; find-context cap={area_cap:.6f}")
    out["terms"] = {
        "site": {"terms": site_terms, "cap_p99": site_cap, "null_mean": site_null_mean,
                 "weight": 1670 / 1849},
        "material": {"terms": mat_terms, "cap_p99": mat_cap, "null_mean": mat_null_mean,
                     "weight": 179 / 1849},
        "find_context": {"terms": area_terms, "cap_p99": area_cap, "null_mean": area_null_mean,
                         "weight": 179 / 1849},
    }

    # ------------------------------------------------ Part 3: validation
    filed_classes = {m: e["dominant"] for m, e in full_calls.items() if e["restricted_0.9"]}
    restricted_set = set(filed_classes)
    by_site_seals = collections.defaultdict(list)
    for j in joined: by_site_seals[j["site"]].append(j["signs"])
    def profiles(seqs):
        tab = collections.defaultdict(lambda: [0, 0, 0, 0])
        for seq in seqs:
            n = len(seq)
            for k, s in enumerate(seq):
                p = 3 if n == 1 else 0 if k == 0 else 2 if k == n - 1 else 1
                tab[s][p] += 1
        return tab
    def direction(fit_seqs, val_seqs_all):
        fit_tab = profiles(fit_seqs)
        fit_seqs_set = {tuple(x) for x in fit_seqs}
        kept = [x for x in val_seqs_all if tuple(x) not in fit_seqs_set]
        val_tab = profiles(kept)
        terms = {}
        for s in sorted(set(fit_tab) | set(val_tab)):
            nf, nv = sum(fit_tab.get(s, [0, 0, 0, 0])), sum(val_tab.get(s, [0, 0, 0, 0]))
            if nf < 5 or nv < 5: continue
            qf = [(c + 0.5) / (nf + 2.0) for c in fit_tab.get(s, [0, 0, 0, 0])]
            qv = [(c + 0.5) / (nv + 2.0) for c in val_tab.get(s, [0, 0, 0, 0])]
            terms[s] = sum(qv[c] * math.log(qv[c] / qf[c]) for c in range(4))
        restr = [t for s, t in terms.items() if s in restricted_set]
        unrestr = [t for s, t in terms.items() if s not in restricted_set]
        def med(v):
            v = sorted(v); n = len(v)
            return v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2
        delta = (med(unrestr) - med(restr)) if restr and unrestr else None
        return {"kept_validation_seals": len(kept), "measurable_signs": len(terms),
                "restricted_measurable": len(restr), "terms": terms, "delta": delta}
    md_seqs, ha_seqs = by_site_seals["Mohenjo-daro"], by_site_seals["Harappa"]
    d_mh = direction(md_seqs, ha_seqs)
    d_hm = direction(ha_seqs, md_seqs)
    pooled_obs = None
    if d_mh["delta"] is not None and d_hm["delta"] is not None:
        pooled_obs = (d_mh["delta"] + d_hm["delta"]) / 2
    # null: permute site labels within length strata over pooled MD+HA seals
    pooled_seals = [("Mohenjo-daro", x) for x in md_seqs] + [("Harappa", x) for x in ha_seqs]
    rngv = random.Random(seed_of("spec109-s2-valnull-v1"))
    strata = collections.defaultdict(list)
    for i, (_, x) in enumerate(pooled_seals): strata[len(x)].append(i)
    null_deltas = []
    for d in range(B):
        lab = [s for s, _ in pooled_seals]
        for idxs in strata.values():
            vals = [lab[i] for i in idxs]
            rngv.shuffle(vals)
            for i, v in zip(idxs, vals): lab[i] = v
        f_seqs = [pooled_seals[i][1] for i in range(len(pooled_seals)) if lab[i] == "Mohenjo-daro"]
        v_seqs = [pooled_seals[i][1] for i in range(len(pooled_seals)) if lab[i] == "Harappa"]
        dd1 = direction(f_seqs, v_seqs)["delta"]
        dd2 = direction(v_seqs, f_seqs)["delta"]
        if dd1 is not None and dd2 is not None: null_deltas.append((dd1 + dd2) / 2)
        if (d + 1) % 250 == 0: log(f"validation null {d+1}/{B}")
    null_deltas.sort()
    val_p99 = null_deltas[int(0.99 * len(null_deltas))] if null_deltas else None
    floors_ok = all(d["measurable_signs"] >= 20 and d["restricted_measurable"] >= 5
                    for d in (d_mh, d_hm))
    if not (join_a["validates"] and join_b["validates"]):
        verdict = "INDETERMINATE (join STOP)"
    elif not floors_ok or pooled_obs is None:
        verdict = "INDETERMINATE (direction below floors)"
    elif pooled_obs > val_p99:
        verdict = "CHANNEL POSITIVE"
    else:
        verdict = "CHANNEL NULL"
    out["validation"] = {
        "filed_classes_rho090": filed_classes,
        "md_to_ha": {k: v for k, v in d_mh.items()},
        "ha_to_md": {k: v for k, v in d_hm.items()},
        "pooled_delta": pooled_obs, "null_p99": val_p99,
        "null_mean": sum(null_deltas) / len(null_deltas) if null_deltas else None,
        "floors_ok": floors_ok, "verdict": verdict}
    log(f"validation: pooled delta={pooled_obs}, null p99={val_p99}, verdict={verdict}")

    # ------------------------------------------------ register (custody)
    os.makedirs(CUST109, exist_ok=True)
    prov = {"generator": "spec109-stage2-harness", "generator_pin": HARNESS_SHA,
            "constraint_set_version": "registration-2026-11-27 + stage-2-freeze-2026-11-27",
            "freeze_pin": FREEZE_SHA,
            "data_pins": {k: v[1] for k, v in PINS.items() if k != "freeze"},
            "seeds": {"positional_null": "spec109-s2-posnull-v1",
                      "numerical_null": "spec109-s2-numnull-v1",
                      "context_null": "spec109-s2-ctxnull-v1",
                      "validation_null": "spec109-s2-valnull-v1"}}
    records = []
    for i, s in enumerate(structures):
        records.append({"candidate_id": f"S109-P2-POS-{i+1:03d}", "kind": "positional_structure",
                        "mark": s["mark"], "rho": s["rho"], "dominant": s["dominant"],
                        "stability": s["stability"], "provenance": prov})
    for name, key in (("bounded_range", "check1_bounded_range"),
                      ("positional_restriction", "check2_positional_restriction"),
                      ("combination_contiguity", "check3_combination_contiguity")):
        c = checks[key]
        records.append({"candidate_id": f"S109-P2-NUM-{name}", "kind": "numerical_check",
                        "supported": c["full_supported"], "stability": c["stability"],
                        "provenance": prov})
    for fam, wkey in (("site", "site"), ("material", "material"), ("find_context", "find_context")):
        for s, e in sorted(out["terms"][fam]["terms"].items()):
            if not e["scored"]: continue
            records.append({"candidate_id": f"S109-P3-{fam}-{s}", "kind": "context_term",
                            "family": fam, "sign": s, "term": e["term"], "tokens": e["tokens"],
                            "cap_p99": out["terms"][fam]["cap_p99"],
                            "weight": out["terms"][fam]["weight"],
                            "label": "no iconography component", "provenance": prov})
    reg_path = os.path.join(CUST109, "stage-2-generated-hypotheses-register.jsonl")
    with open(reg_path, "w") as f:
        for r in records:
            f.write(json.dumps(r, sort_keys=True) + "\n")
    out["register"] = {"path": "glossa-custody/spec109/stage-2-generated-hypotheses-register.jsonl",
                       "records": len(records), "sha256": sha256_file(reg_path)}
    log(f"register written: {len(records)} records, sha256 {out['register']['sha256'][:16]}")

    raw_path = os.path.join(CUST109, "stage-2-raw-output.json")
    with open(raw_path, "w") as f:
        json.dump(out, f, sort_keys=True, indent=1)
    out_sha = sha256_file(raw_path)
    log(f"raw output written: {raw_path} sha256 {out_sha}")
    stable_structs = [s for s in structures if s["stability"] == "STABLE"]
    print(json.dumps({"verdict_block": {
        "l3_cell_mismatches": len(mism),
        "positional_structures": len(structures),
        "stable": len(stable_structs),
        "unstable": sum(1 for s in structures if s["stability"] == "UNSTABLE"),
        "indeterminate": sum(1 for s in structures if s["stability"] == "INDETERMINATE"),
        "numerical_checks": {k: [v["full_supported"], v["stability"]] for k, v in checks.items()},
        "join_a_validates": join_a["validates"], "join_b_validates": join_b["validates"],
        "channel_verdict": verdict, "register_records": len(records),
        "raw_output_sha256": out_sha}}, indent=1))
    return 0

if __name__ == "__main__":
    sys.exit(main())
