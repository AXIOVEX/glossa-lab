#!/usr/bin/env python3
"""TC-110-07 / TC-110-08 — independent recomputation of the Spec 110
REVISED battery's gate and execution, written independently of
records/obfuscation-harness-rev2.py. It imports only the filed
harness's corpus generator (build_profile_corpus — the shared
machinery, as TC-110-02 imported the Stage 1 builder); the corpus
loaders, every statistic, every transformation, the stratum null,
and all verdict logic are reimplemented here from the revision
registration's text.

Usage: tc110-07-08-revision-verification.py REPO_ROOT CUSTODY_DIR
Reads custody/spec110-rev/gate-output-rev2.json and
raw-output-rev2.json. Exit 0 iff every check passes.
"""
import importlib.util
import json
import math
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(sys.argv[1])
CUST = Path(sys.argv[2])
spec = importlib.util.spec_from_file_location(
    "rev2harness",
    ROOT / "specs/110-obfuscation-hypothesis/records/obfuscation-harness-rev2.py")
H = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H)
build_profile_corpus = H.build_profile_corpus

fails = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
    if not ok:
        fails.append(name)


def close(a, b, tol=1e-9):
    return abs(a - b) <= tol


# ---------------------------------------------------------------------------
# Corpus loaders, reimplemented from revision registration section 6
# (the first registration's handling).

def load_indus():
    raw = json.load(open(CUST / "spec105/indus-derivation.json"))
    seqs = []
    for art in raw:
        for line in art["lines"]:
            flat = [s for g in line for s in g]
            if flat:
                seqs.append(flat)
    p100 = json.load(open(ROOT / "outputs/phase100_full_corpus.json"))
    site_of, conflicts = {}, set()
    for t in p100["translations"]:
        k = tuple(t["signs"])
        if k in site_of and site_of[k] != t["site"]:
            conflicts.add(k)
        site_of.setdefault(k, t["site"])
    sites = [None if tuple(q) in conflicts else site_of.get(tuple(q))
             for q in seqs]
    return seqs, sites


def load_meroitic():
    raw = json.load(open(CUST / "spec105/meroitic.json"))
    seqs = []
    for t in raw:
        for line in t["lines"]:
            flat = [s for g in line for s in g if s != "."]
            if flat:
                seqs.append(flat)
    return seqs


def load_eteocypriot():
    raw = json.load(open(
        ROOT / "specs/096-eteocypriot-program/corpus/corpus.json"))
    seqs = []
    for ins in raw["inscriptions"]:
        if ins.get("stratum") != "primary-amathus":
            continue
        for ln in ins.get("eteocypriot_lines") or []:
            for seg in ln["segments"]:
                if seg:
                    seqs.append(list(seg))
        for ln in ins.get("eteocypriot_side") or []:
            segs = ln.get("segments") if isinstance(ln, dict) else None
            if segs:
                for seg in segs:
                    if seg:
                        seqs.append(list(seg))
    return seqs


def load_latin():
    text = open(CUST / "spec107/de-bello-gallico-gutenberg-218.txt",
                encoding="utf-8", errors="replace").read().lower()
    words, cur = [], []
    for ch in text:
        if "a" <= ch <= "z":
            cur.append(ch)
        elif len(cur) >= 2:
            words.append(cur)
            cur = []
        else:
            cur = []
    if len(cur) >= 2:
        words.append(cur)
    return words


# ---------------------------------------------------------------------------
# Statistics, reimplemented.

def a_stats(seqs, V0):
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
    cond = defaultdict(Counter)
    for (a, b), k in pairs.items():
        cond[a][b] = k
    h2 = 0.0
    for a, ctr in cond.items():
        na = firsts[a]
        h2 += (na / m) * (-sum((k / na) * math.log2(k / na)
                               for k in ctr.values()))
    desc = sorted(c.values(), reverse=True)
    return {"N": n, "V": v,
            "A1": h / math.log2(v) if v > 1 else 0.0,
            "A2": max(c.values()) / n,
            "A3": h2 / h if h > 0 else 0.0,
            "A4": h - h2,
            "frtail": sum(desc[V0 // 2:]) / n if n else 0.0}


def a_fires(st, band):
    return {
        "flat": st["A1"] > band["A1"][1] and st["A2"] < band["A2"][0],
        "struct": st["A3"] > band["A3"][1] and st["A4"] < band["A4"][0],
        "c1": st["A3"] > band["A3"][1] or st["A4"] < band["A4"][0],
    }


def d_fire(st, dband):
    return st["V"] > dband["V"][1] and st["frtail"] > dband["frtail"][1]


def band_of(rows, keys):
    return {k: [min(r[k] for r in rows), max(r[k] for r in rows)] for k in keys}


def jsd(p, q):
    tot = 0.0
    for k in set(p) | set(q):
        a, b = p.get(k, 0.0), q.get(k, 0.0)
        mm = 0.5 * (a + b)
        if a > 0:
            tot += 0.5 * a * math.log2(a / mm)
        if b > 0:
            tot += 0.5 * b * math.log2(b / mm)
    return tot


def omnibus(strata):
    profs, toks = {}, {}
    for lab, sq in strata.items():
        c = Counter(t for q in sq for t in q)
        n = sum(c.values())
        profs[lab] = {s: k / n for s, k in c.items()}
        toks[lab] = n
    labs = list(profs)
    num = den = 0.0
    for i in range(len(labs)):
        for j in range(i + 1, len(labs)):
            w = toks[labs[i]] * toks[labs[j]]
            num += w * jsd(profs[labs[i]], profs[labs[j]])
            den += w
    return num / den if den else 0.0


def length_bin(q):
    n = len(q)
    return 0 if n <= 2 else 1 if n <= 4 else 2 if n <= 6 else 3


def stratum_null(seqs, labels, seed, draws=999):
    rng = random.Random(seed)
    bins = defaultdict(list)
    for i, q in enumerate(seqs):
        bins[length_bin(q)].append(i)
    groups = defaultdict(list)
    for i, lab in enumerate(labels):
        groups[lab].append(seqs[i])
    obs = omnibus(dict(groups))
    labs_by_bin = {b: [labels[i] for i in idxs] for b, idxs in bins.items()}
    null = []
    for _ in range(draws):
        g = defaultdict(list)
        for b, idxs in bins.items():
            labs = labs_by_bin[b][:]
            rng.shuffle(labs)
            for i, lab in zip(idxs, labs):
                g[lab].append(seqs[i])
        null.append(omnibus(dict(g)))
    null.sort()
    return obs, null[int(0.99 * (len(null) - 1))]


def b_strata(seqs, sites):
    groups = defaultdict(list)
    for q, s in zip(seqs, sites):
        if s is not None:
            groups[s].append(q)
    return {lab: sq for lab, sq in groups.items()
            if sum(len(q) for q in sq) >= 300 and len(sq) >= 30}


def b_eval(seqs, sites, seed, baseline_max):
    strata = b_strata(seqs, sites)
    if len(strata) < 2:
        return None
    keep = [(q, s) for q, s in zip(seqs, sites) if s in strata]
    obs, p99 = stratum_null([q for q, _ in keep], [s for _, s in keep], seed)
    return {"obs": obs, "null_p99": p99, "baseline_max": baseline_max,
            "strata": sorted(strata),
            "fire": obs > p99 and obs > baseline_max}


# ---------------------------------------------------------------------------
# Transformations, reimplemented from the registrations' constructions.

def make_perm(inventory, seed):
    rng = random.Random(seed)
    vals = list(inventory)
    sh = vals[:]
    rng.shuffle(sh)
    return dict(zip(vals, sh))


def t_hom(seqs, seed):
    c = Counter(t for q in seqs for t in q)
    top = [s for s, _ in c.most_common(10)]
    rng = random.Random(seed)
    return [[f"{s}#h{rng.randint(0, 1)}" if s in top else s for s in q]
            for q in seqs]


def t_poly(seqs, seed):
    inv = sorted({t for q in seqs for t in q}, key=str)
    perms = [make_perm(inv, seed + k) for k in range(3)]
    return [[perms[i % 3].get(s, s) for i, s in enumerate(q)] for q in seqs]


def t_shuf(seqs, seed):
    rng = random.Random(seed)
    out = []
    for q in seqs:
        nq = list(q)
        rng.shuffle(nq)
        out.append(nq)
    return out


def t_sub_u(seqs, seed):
    perm = make_perm(sorted({t for q in seqs for t in q}, key=str), seed)
    return [[perm.get(s, s) for s in q] for q in seqs]


def t_sub_d(seqs, sites, target, seed):
    perm = make_perm(sorted({t for q in seqs for t in q}, key=str), seed)
    return [[perm.get(s, s) for s in q] if sites[i] == target else list(q)
            for i, q in enumerate(seqs)]


def synth(V0, lengths, real_sites, seed):
    sites = None
    if real_sites is not None:
        rng = random.Random(f"spec110r2-sites-{seed}")
        sites = real_sites[:]
        rng.shuffle(sites)
    seqs, planted, _ = build_profile_corpus(seed, V0, lengths, sites)
    return seqs, planted


# ---------------------------------------------------------------------------

def main():
    gate = json.load(open(CUST / "spec110-rev/gate-output-rev2.json"))
    raw = json.load(open(CUST / "spec110-rev/raw-output-rev2.json"))

    ind_seqs, ind_sites = load_indus()
    mer_seqs = load_meroitic()
    ete_seqs = load_eteocypriot()
    lat = load_latin()
    q = len(lat) // 4
    prof = {
        "ind": {"V0": 372, "seqs": ind_seqs, "sites": ind_sites,
                "lengths": [len(s) for s in ind_seqs]},
        "mer": {"V0": 31, "seqs": mer_seqs, "sites": None,
                "lengths": [len(s) for s in mer_seqs]},
        "ete": {"V0": 32, "seqs": ete_seqs, "sites": None,
                "lengths": [len(s) for s in ete_seqs]},
    }
    for i in range(4):
        qs = lat[i * q:(i + 1) * q]
        prof[f"latq{i + 1}"] = {"V0": 26, "seqs": qs, "sites": None,
                                "lengths": [len(s) for s in qs]}

    # TC-110-07 gate section -------------------------------------------------
    for name in ("ind", "mer", "ete"):
        c = Counter(t for s in prof[name]["seqs"] for t in s)
        fc = gate["censuses"][name]
        check(f"census {name}", fc["sequences"] == len(prof[name]["seqs"])
              and fc["N"] == sum(c.values()) and fc["V"] == len(c),
              f"filed {fc} vs recomputed seqs={len(prof[name]['seqs'])} "
              f"N={sum(c.values())} V={len(c)}")

    bands, dbands = {}, {}
    band_n = {"ind": 20, "mer": 20, "ete": 12}
    for name in ("ind", "mer", "ete"):
        P = prof[name]
        rows = []
        for i in range(1, band_n[name] + 1):
            seqs, _ = synth(P["V0"], P["lengths"], P["sites"],
                            f"spec110r2-band-{name}-{i}")
            rows.append(a_stats(seqs, P["V0"]))
        bands[name] = band_of(rows, ("A1", "A2", "A3", "A4"))
        dbands[name] = band_of(rows, ("V", "frtail"))
        ok = all(close(bands[name][k][j], gate["bands"][name][k][j])
                 for k in bands[name] for j in (0, 1)) and \
            all(close(dbands[name][k][j], gate["dbands"][name][k][j])
                for k in dbands[name] for j in (0, 1))
        check(f"band {name} reproduces", ok,
              f"recomputed A={ {k: [round(x, 4) for x in v] for k, v in bands[name].items()} }")
    lat_bands, lat_dbands = {}, {}
    for qi in (1, 2, 3, 4):
        P = prof[f"latq{qi}"]
        rows = []
        for i in range(1, 13):
            seqs, _ = synth(P["V0"], P["lengths"], None,
                            f"spec110r2-band-latq{qi}-{i}")
            rows.append(a_stats(seqs, P["V0"]))
        lat_bands[qi] = band_of(rows, ("A1", "A2", "A3", "A4"))
        lat_dbands[qi] = band_of(rows, ("V", "frtail"))
        ok = all(close(lat_bands[qi][k][j], gate["lat_bands"][str(qi)][k][j])
                 for k in lat_bands[qi] for j in (0, 1))
        check(f"band latq{qi} reproduces", ok)

    base_rows = []
    for i in range(1, 21):
        seqs, sites = synth(372, prof["ind"]["lengths"], ind_sites,
                            f"spec110r2-band-ind-{i}")
        st = b_strata(seqs, sites)
        base_rows.append(omnibus(st) if len(st) >= 2 else None)
    check("B baseline reproduces",
          all(close(a, b) for a, b in zip(base_rows, gate["b_baseline_rows"]))
          and close(max(base_rows), gate["b_baseline_max"]),
          f"max recomputed {max(base_rows):.4f} vs filed {gate['b_baseline_max']:.4f}")
    baseline_max = max(base_rows)

    gate_ct = {}
    for name in ("ind", "mer", "ete"):
        P = prof[name]
        legs = []
        for i in range(5):
            seed = f"spec110r2-ctl-{name}-{i + 1}"
            seqs, sites = synth(P["V0"], P["lengths"], P["sites"], seed)
            row = {}
            nat = a_stats(seqs, P["V0"])
            row["nat_fires"] = a_fires(nat, bands[name])
            row["nat_dfire"] = d_fire(nat, dbands[name])
            hst = a_stats(t_hom(seqs, 11001 + i), P["V0"])
            row["hom_flat"] = a_fires(hst, bands[name])["flat"]
            row["hom_dfire"] = d_fire(hst, dbands[name])
            pst = a_stats(t_poly(seqs, 11101 + i), P["V0"])
            row["poly_flat"] = a_fires(pst, bands[name])["flat"]
            sst = a_stats(t_shuf(seqs, 11501 + i), P["V0"])
            sf = a_fires(sst, bands[name])
            row["shuf_struct"] = sf["struct"]
            row["shuf_c1"] = sf["c1"]
            ust = a_stats(t_sub_u(seqs, 11401 + i), P["V0"])
            uf = a_fires(ust, bands[name])
            row["subu_any_fire"] = (uf["flat"] or uf["struct"] or uf["c1"]
                                    or d_fire(ust, dbands[name]))
            filed = gate["gate"][name][i]
            ok = all(row[k] == filed[k] for k in row)
            check(f"gate {name} ctl{i} fires reproduce", ok,
                  json.dumps(row) if not ok else "")
            if name == "ind":
                bn = b_eval(seqs, sites, 11001 + i, baseline_max)
                strata = b_strata(seqs, sites)
                order = sorted(strata,
                               key=lambda s: -sum(len(x) for x in strata[s]))
                dseqs = t_sub_d(seqs, sites, order[1], 11301 + i)
                bd = b_eval(dseqs, sites, 11001 + i, baseline_max)
                okb = (close(bn["obs"], filed["b_nat"]["obs"])
                       and close(bn["null_p99"], filed["b_nat"]["null_p99"])
                       and bn["fire"] == filed["b_nat"]["fire"]
                       and close(bd["obs"], filed["b_subd"]["obs"])
                       and close(bd["null_p99"], filed["b_subd"]["null_p99"])
                       and bd["fire"] == filed["b_subd"]["fire"])
                check(f"gate ind ctl{i} B legs reproduce", okb,
                      f"nat obs {bn['obs']:.4f} p99 {bn['null_p99']:.4f}; "
                      f"subd obs {bd['obs']:.4f} p99 {bd['null_p99']:.4f}")
                row["b_nat"] = bn
                row["b_subd"] = bd
            legs.append(row)
        gate_ct[name] = legs

    panel = []
    for i, leg in enumerate(gate_ct["ind"]):
        f = leg["nat_fires"]
        panel.append({"flat": f["flat"], "struct": f["struct"], "c1": f["c1"],
                      "d": leg["nat_dfire"]})
    for qi in (1, 2, 3, 4):
        st = a_stats(prof[f"latq{qi}"]["seqs"], 26)
        f = a_fires(st, lat_bands[qi])
        panel.append({"flat": f["flat"], "struct": f["struct"], "c1": f["c1"],
                      "d": d_fire(st, lat_dbands[qi])})
    half = len(mer_seqs) // 2
    for sq in (mer_seqs, mer_seqs[:half], mer_seqs[half:]):
        st = a_stats(sq, 31)
        f = a_fires(st, bands["mer"])
        panel.append({"flat": f["flat"], "struct": f["struct"], "c1": f["c1"],
                      "d": d_fire(st, dbands["mer"])})
    fp = {k: sum(1 for p in panel if p[k]) for k in ("flat", "struct", "c1", "d")}
    check("FP panel reproduces", fp == gate["fp"],
          f"recomputed {fp} vs filed {gate['fp']}")
    fp_b = sum(1 for leg in gate_ct["ind"] if leg["b_nat"]["fire"])
    check("FP-B reproduces", fp_b == gate["fp_b"], f"{fp_b} vs {gate['fp_b']}")

    def cnt(name, key):
        return sum(1 for leg in gate_ct[name] if leg[key])

    outcomes = {}
    for name in ("ind", "mer", "ete"):
        o = {"flat_detection": cnt(name, "hom_flat") >= 4 and cnt(name, "poly_flat") >= 4,
             "struct_detection": cnt(name, "shuf_struct") >= 4,
             "c1_detection": cnt(name, "shuf_c1") >= 4,
             "d_detection": cnt(name, "hom_dfire") >= 4,
             "invariance": sum(1 for leg in gate_ct[name]
                               if not leg["subu_any_fire"]) >= 4}
        o["a_flat_scoreable"] = o["flat_detection"] and o["invariance"] and fp["flat"] <= 1
        o["a_struct_scoreable"] = o["struct_detection"] and o["invariance"] and fp["struct"] <= 1
        o["c1_scoreable"] = o["c1_detection"] and o["invariance"] and fp["c1"] <= 1
        o["d_scoreable"] = o["d_detection"] and o["invariance"] and fp["d"] <= 1
        outcomes[name] = o
        fo = gate["outcomes"][name]
        check(f"gate outcome {name} reproduces",
              all(o[k] == fo[k] for k in o), json.dumps(o) if o != fo else "")
    bg = {"detection": sum(1 for leg in gate_ct["ind"] if leg["b_subd"]["fire"]) >= 4,
          "fp_ok": fp_b <= 1}
    bg["b_scoreable"] = bg["detection"] and bg["fp_ok"]
    check("gate outcome B reproduces",
          all(bg[k] == gate["b_gate"][k] for k in bg), json.dumps(bg))

    # TC-110-08 execution section ---------------------------------------------
    def a_verdict(o, fires):
        pats = []
        if o["a_flat_scoreable"]:
            pats.append(("flattening", fires["flat"]))
        if o["a_struct_scoreable"]:
            pats.append(("structure", fires["struct"]))
        if not pats:
            return None
        hit = [n for n, f in pats if f]
        return ("SIGNATURE PRESENT (" + ", ".join(hit) + ")" if hit
                else "SIGNATURE ABSENT")

    for corp, name, V0 in (("indus", "ind", 372), ("meroitic", "mer", 31)):
        st = a_stats(prof[name]["seqs"], V0)
        fires = a_fires(st, bands[name])
        filed = raw["corpora"][corp]
        ok = all(close(st[k], filed["stats"][k])
                 for k in ("A1", "A2", "A3", "A4", "frtail")) \
            and st["V"] == filed["stats"]["V"] \
            and fires == filed["a_fires"] \
            and d_fire(st, dbands[name]) == filed["d_fire"]
        check(f"execution {corp} statistics reproduce", ok,
              f"A1={st['A1']:.4f} A2={st['A2']:.4f} A3={st['A3']:.4f} "
              f"A4={st['A4']:.4f} V={st['V']} frtail={st['frtail']:.4f}")
        want = {}
        av = a_verdict(outcomes[name], fires)
        if av is not None:
            want["A"] = av
        if name == "ind" and bg["b_scoreable"]:
            be = b_eval(ind_seqs, ind_sites, 11999, baseline_max)
            okb = close(be["obs"], filed["b"]["obs"]) \
                and close(be["null_p99"], filed["b"]["null_p99"]) \
                and be["fire"] == filed["b"]["fire"]
            check("execution indus B reproduces", okb,
                  f"obs {be['obs']:.4f} p99 {be['null_p99']:.4f} fire {be['fire']}")
            want["B"] = "SIGNATURE PRESENT" if be["fire"] else "SIGNATURE ABSENT"
        if name == "mer":
            want["B"] = ("NOT TESTABLE AT THIS POWER "
                         "(no stratum metadata in the corpus build)")
        if outcomes[name]["c1_scoreable"]:
            want["C"] = "SIGNATURE PRESENT" if fires["c1"] else "SIGNATURE ABSENT"
        if outcomes[name]["d_scoreable"]:
            want["D"] = ("SIGNATURE PRESENT" if d_fire(st, dbands[name])
                        else "SIGNATURE ABSENT")
        check(f"execution {corp} verdicts reproduce",
              want == filed["verdicts"],
              f"recomputed {want} vs filed {filed['verdicts']}")

    ete = raw["corpora"]["eteocypriot"]
    check("execution eteocypriot NOT TESTABLE",
          all(v == "NOT TESTABLE AT THIS POWER" for v in ete["verdicts"].values())
          and ete["census"]["N"] == 54 and len(ete_seqs) == 11,
          json.dumps(ete["verdicts"]))

    if fails:
        print(f"TC-110-07/08 FAIL — {len(fails)} check(s) failed")
        return 1
    print("TC-110-07/08 PASS — the revision gate (bands, legs, panel, "
          "outcomes) and the revision execution (statistics and verdicts, "
          "including every filed absence of a verdict) reproduce "
          "independently from the registered seeds and the pinned corpora.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
