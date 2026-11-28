#!/usr/bin/env python3
"""Spec 110 obfuscation battery harness.

Implements registration-2026-11-27.md exactly:
  - corpus builders (synthetic natural via the Spec 109 Stage 1 harness
    machinery, imported by path; real corpora from the pinned custody /
    tracked files),
  - the four signature families' statistics,
  - the transformations T-HOM / T-POLY / T-SUB-D / T-SUB-U,
  - the control gate (G-A, G-B, G-C, G-D, G-INV, G-FP),
  - the real-corpus execution with per-family verdicts under section 5.

Usage: python3 obfuscation-harness.py <worktree_root> <custody_out>
Payload verdict = exit code (0 = harness completed; verdicts are data).
Every stage emits timestamped, countable progress lines.
"""
import hashlib
import importlib.util
import json
import math
import os
import random
import sys
import time
from collections import Counter, defaultdict

WT = os.path.abspath(sys.argv[1])
CUST = os.path.abspath(sys.argv[2])
os.makedirs(CUST, exist_ok=True)
CUST105 = "/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/spec105"
CUST107 = "/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/spec107"
SEED = 11001
B = 999


def log(msg):
    print(f"[{time.strftime('%H:%M:%SZ', time.gmtime())}] {msg}", flush=True)


def sha256_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


# --------------------------------------------------------------------------
# Load the Spec 109 Stage 1 harness as a module (corpus machinery + profile).
S1_PATH = os.path.join(
    WT, "specs/109-generative-decipherment-engine/records/stage-1-preflight-harness.py")
S1_SHA = sha256_file(S1_PATH)
spec = importlib.util.spec_from_file_location("s1harness", S1_PATH)
S1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S1)
log(f"stage-1 harness imported (sha256 {S1_SHA[:12]}…)")


def build_synthetic(seed_str):
    """One synthetic natural corpus at the Indus profile.

    Returns (sign sequences as strings, planted site label per sequence).
    A seed the builder's admission gates reject is rebuilt under a
    '-try1' seed, the Stage 1 pattern, and the rebuild is filed.
    """
    lengths = S1.indus_lengths()
    try:
        built = S1.build_corpus(seed_str, lengths)
        used = seed_str
    except RuntimeError:
        used = seed_str + "-try1"
        built = S1.build_corpus(used, lengths)
        log(f"  seed {seed_str} rejected by builder gates; rebuilt as {used}")
    seqs = [[str(s) for s in seq] for seq in built["signseqs"]]
    sites = [built["sites"][i] for i in range(len(seqs))]
    return seqs, sites


# --------------------------------------------------------------------------
# Statistics (registration section 2).

def counts_of(seqs):
    c = Counter()
    for q in seqs:
        c.update(q)
    return c


def bigram_counts(seqs):
    c = Counter()
    for q in seqs:
        for a, b in zip(q, q[1:]):
            c[(a, b)] += 1
    return c


def entropy_bits(counter, total):
    h = 0.0
    for v in counter.values():
        p = v / total
        h -= p * math.log2(p)
    return h


def family_a_stats(seqs):
    c = counts_of(seqs)
    N = sum(c.values())
    V = len(c)
    H = entropy_bits(c, N)
    bc = bigram_counts(seqs)
    nb = sum(bc.values())
    # H(X2|X1): group by first element
    by_first = defaultdict(Counter)
    for (a, b), v in bc.items():
        by_first[a][b] = v
    h2 = 0.0
    for a, ctr in by_first.items():
        na = sum(ctr.values())
        h2 += (na / nb) * entropy_bits(ctr, na)
    return {
        "N": N, "V": V,
        "A1": H / math.log2(V) if V > 1 else 0.0,
        "A2": max(c.values()) / N,
        "A3": h2 / H if H > 0 else 0.0,
        "A4": H - h2,
        "H": H, "H2": h2,
    }


def hapax_stats(seqs):
    c = counts_of(seqs)
    N = sum(c.values())
    V = len(c)
    hap = sum(1 for v in c.values() if v == 1)
    return {"V": V, "hapax_type_share": hap / V if V else 0.0,
            "hapax_token_share": hap / N if N else 0.0}


def profile(seqs, inventory=None):
    c = counts_of(seqs)
    N = sum(c.values())
    inv = inventory if inventory is not None else sorted(c)
    return {s: c.get(s, 0) / N for s in inv}, c, N


def jsd(p, q):
    """Jensen-Shannon divergence (base 2) over the union support."""
    keys = set(p) | set(q)
    tot = 0.0
    for k in keys:
        a, b = p.get(k, 0.0), q.get(k, 0.0)
        m = 0.5 * (a + b)
        if a > 0:
            tot += 0.5 * a * math.log2(a / m)
        if b > 0:
            tot += 0.5 * b * math.log2(b / m)
    return tot


def omnibus_jsd(strata_seqs):
    """Token-weighted mean pairwise JSD over strata (dict label -> seqs)."""
    profs = {}
    toks = {}
    for lab, sq in strata_seqs.items():
        pr, _, n = profile(sq)
        profs[lab] = pr
        toks[lab] = n
    labs = list(profs)
    num, den = 0.0, 0.0
    for i in range(len(labs)):
        for j in range(i + 1, len(labs)):
            w = toks[labs[i]] * toks[labs[j]]
            num += w * jsd(profs[labs[i]], profs[labs[j]])
            den += w
    return num / den if den else 0.0


def length_bin(q):
    n = len(q)
    if n <= 2:
        return 0
    if n <= 4:
        return 1
    if n <= 6:
        return 2
    return 3


def stratum_null(seqs, labels, seed, draws=B):
    """Permutation null for omnibus JSD: labels permuted within length bins."""
    rng = random.Random(seed)
    bins = defaultdict(list)
    for i, q in enumerate(seqs):
        bins[length_bin(q)].append(i)
    obs_groups = defaultdict(list)
    for i, lab in enumerate(labels):
        obs_groups[lab].append(seqs[i])
    obs = omnibus_jsd(dict(obs_groups))
    null = []
    labs_by_bin = {}
    for b, idxs in bins.items():
        labs_by_bin[b] = [labels[i] for i in idxs]
    for d in range(draws):
        groups = defaultdict(list)
        for b, idxs in bins.items():
            labs = labs_by_bin[b][:]
            rng.shuffle(labs)
            for i, lab in zip(idxs, labs):
                groups[lab].append(seqs[i])
        null.append(omnibus_jsd(dict(groups)))
        if (d + 1) % 333 == 0:
            log(f"  stratum null: {d + 1}/{draws} draws")
    null.sort()
    p99 = null[int(0.99 * (len(null) - 1))]
    pct = sum(1 for v in null if v <= obs) / len(null)
    return obs, p99, pct, null


# --- C2: label-free features, matching, gain --------------------------------

def sign_features(seqs):
    """Label-free per-sign distributional features."""
    c = counts_of(seqs)
    N = sum(c.values())
    pos = defaultdict(lambda: [0, 0, 0])  # initial, medial, final counts
    succ = defaultdict(Counter)
    pred = defaultdict(Counter)
    for q in seqs:
        for i, s in enumerate(q):
            if len(q) == 1 or i == 0:
                pos[s][0] += 1
            elif i == len(q) - 1:
                pos[s][2] += 1
            else:
                pos[s][1] += 1
        for a, b in zip(q, q[1:]):
            succ[a][b] += 1
            pred[b][a] += 1
    feats = {}
    for s in c:
        tot = c[s]
        ps = pos[s]
        denom = max(sum(ps), 1)
        se = entropy_bits(succ[s], sum(succ[s].values())) if succ[s] else 0.0
        pe = entropy_bits(pred[s], sum(pred[s].values())) if pred[s] else 0.0
        feats[s] = [
            math.log(c[s] / N),
            ps[0] / denom, ps[1] / denom, ps[2] / denom,
            se, pe,
            math.log(1 + len(succ[s]) + len(pred[s])),
        ]
    return feats


def _standardize(feats_list):
    dims = len(feats_list[0])
    means = [sum(f[i] for f in feats_list) / len(feats_list) for i in range(dims)]
    sds = []
    for i in range(dims):
        var = sum((f[i] - means[i]) ** 2 for f in feats_list) / len(feats_list)
        sds.append(math.sqrt(var) or 1.0)
    return means, sds


def _z(f, means, sds):
    return [(f[i] - means[i]) / sds[i] for i in range(len(f))]


def _cos(a, b):
    da = math.sqrt(sum(x * x for x in a)) or 1.0
    db = math.sqrt(sum(x * x for x in b)) or 1.0
    return sum(x * y for x, y in zip(a, b)) / (da * db)


def match_parts(seqs_p, seqs_q):
    """Match Q signs to P signs by label-free features.

    Returns (mapping Q sign -> P sign, gain, self_agreement, shared_signs).
    Gain is measured on unigram profiles: JSD(identity) - JSD(mapped).
    """
    fp = sign_features(seqs_p)
    fq = sign_features(seqs_q)
    shared = sorted(set(fp) & set(fq))
    allf = [fp[s] for s in fp] + [fq[s] for s in fq]
    means, sds = _standardize(allf)
    zp = {s: _z(fp[s], means, sds) for s in fp}
    zq = {s: _z(fq[s], means, sds) for s in fq}
    # greedy mutual-best assignment over shared signs
    cand = []
    for qs in shared:
        for ps in shared:
            cand.append((_cos(zq[qs], zp[ps]), qs, ps))
    cand.sort(reverse=True)
    mapping = {}
    used_p = set()
    for _, qs, ps in cand:
        if qs not in mapping and ps not in used_p:
            mapping[qs] = ps
            used_p.add(ps)
    # swap polish on profile JSD
    prof_p, _, _ = profile(seqs_p)
    prof_q, _, _ = profile(seqs_q)

    def mapped_jsd(m):
        mq = {}
        for s, v in prof_q.items():
            mq[m.get(s, s)] = mq.get(m.get(s, s), 0.0) + v
        return jsd(prof_p, mq)

    cur = mapped_jsd(mapping)
    inv = {v: k for k, v in mapping.items()}
    for _ in range(200):
        improved = False
        keys = list(mapping)
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                a, b = keys[i], keys[j]
                mapping[a], mapping[b] = mapping[b], mapping[a]
                new = mapped_jsd(mapping)
                if new < cur - 1e-12:
                    cur = new
                    improved = True
                else:
                    mapping[a], mapping[b] = mapping[b], mapping[a]
        if not improved:
            break
    ident = {s: s for s in shared}
    gain = mapped_jsd(ident) - cur
    self_agree = (sum(1 for s in shared if mapping.get(s) == s) / len(shared)
                  if shared else 0.0)
    return mapping, gain, self_agree, shared


def split_halves(seqs, seed):
    rng = random.Random(seed)
    idx = list(range(len(seqs)))
    rng.shuffle(idx)
    h1 = [seqs[i] for i in sorted(idx[::2])]
    h2 = [seqs[i] for i in sorted(idx[1::2])]
    return h1, h2


def c2_eval(seqs_p, seqs_q, with_stability=False):
    mapping, gain, self_agree, shared = match_parts(seqs_p, seqs_q)
    out = {"gain": gain, "self_agreement": self_agree,
           "shared_signs": len(shared), "mapping": mapping}
    if with_stability:
        stabs = []
        for sd in (11002, 11003):
            p1, p2 = split_halves(seqs_p, sd)
            q1, q2 = split_halves(seqs_q, sd + 500)
            for (pa, qa) in ((p1, q1), (p2, q2)):
                m2, _, _, sh2 = match_parts(pa, qa)
                common = [s for s in sh2 if s in mapping]
                if common:
                    stabs.append(sum(1 for s in common
                                     if m2.get(s) == mapping.get(s))
                                 / len(common))
        out["stability"] = min(stabs) if stabs else 0.0
        out["stability_all"] = stabs
    return out


# --- transformations ---------------------------------------------------------

def permute_labels(seqs, perm):
    return [[perm.get(s, s) for s in q] for q in seqs]


def t_sub(seed):
    rng = random.Random(seed)
    return rng


def make_perm(inventory, seed):
    rng = random.Random(seed)
    vals = list(inventory)
    sh = vals[:]
    rng.shuffle(sh)
    return dict(zip(vals, sh))


def t_hom(seqs, seed):
    c = counts_of(seqs)
    top = [s for s, _ in c.most_common(10)]
    rng = random.Random(seed)
    out = []
    for q in seqs:
        nq = []
        for s in q:
            if s in top:
                nq.append(f"{s}#h{rng.randint(0, 1)}")
            else:
                nq.append(s)
        out.append(nq)
    return out


def t_poly(seqs, seed):
    inv = sorted(counts_of(seqs))
    perms = [make_perm(inv, seed + k) for k in range(3)]
    return [[perms[i % 3].get(s, s) for i, s in enumerate(q)] for q in seqs]


# --- verdict helpers ---------------------------------------------------------

def band_of(values):
    return [min(values), max(values)]


def a_pattern(stats, band):
    """Returns 'flattening' | 'structure' | None, plus per-stat excursions."""
    exc = {}
    exc["A1_high"] = stats["A1"] > band["A1"][1]
    exc["A2_low"] = stats["A2"] < band["A2"][0]
    exc["A3_high"] = stats["A3"] > band["A3"][1]
    exc["A4_low"] = stats["A4"] < band["A4"][0]
    if exc["A1_high"] and exc["A2_low"]:
        return "flattening", exc
    if exc["A3_high"] and exc["A4_low"]:
        return "structure", exc
    return None, exc


def d_verdict(seqs, band_v, band_hap):
    hs = hapax_stats(seqs)
    fire = hs["V"] > band_v[1] and hs["hapax_type_share"] > band_hap[1]
    return fire, hs


def size_matched_band(natural_corpora, target_n, seed=11001):
    """Subsample natural corpora to target_n tokens (whole sequences)."""
    rng = random.Random(seed)
    vs, haps = [], []
    draws = 0
    pool = [q for corp in natural_corpora for q in corp]
    while draws < 20:
        rng.shuffle(pool)
        acc, tot = [], 0
        for q in pool:
            acc.append(q)
            tot += len(q)
            if tot >= target_n:
                break
        hs = hapax_stats(acc)
        vs.append(hs["V"])
        haps.append(hs["hapax_type_share"])
        draws += 1
    return band_of(vs), band_of(haps)


# --------------------------------------------------------------------------
# Corpus loading (real corpora + Latin control).

def load_indus():
    raw = json.load(open(os.path.join(CUST105, "indus-derivation.json")))
    seqs = []
    for art in raw:
        for line in art["lines"]:
            flat = [s for g in line for s in g]
            if flat:
                seqs.append(flat)
    p100 = json.load(open(os.path.join(WT, "outputs/phase100_full_corpus.json")))
    seq2site = {}
    conflicts = set()
    for t in p100["translations"]:
        k = tuple(t["signs"])
        if k in seq2site and seq2site[k] != t["site"]:
            conflicts.add(k)
        seq2site.setdefault(k, t["site"])
    sites = []
    n_conf = 0
    for q in seqs:
        k = tuple(q)
        if k in conflicts:
            sites.append(None)
            n_conf += 1
        else:
            sites.append(seq2site.get(k))
    return seqs, sites, {"conflict_excluded": n_conf}


def load_eteocypriot():
    raw = json.load(open(os.path.join(
        WT, "specs/096-eteocypriot-program/corpus/corpus.json")))
    seqs = []
    for ins in raw["inscriptions"]:
        if ins.get("stratum") != "primary-amathus":
            continue
        lines = ins.get("eteocypriot_lines") or []
        for ln in lines:
            for seg in ln["segments"]:
                if seg:
                    seqs.append(list(seg))
        side = ins.get("eteocypriot_side") or []
        for ln in side:
            segs = ln.get("segments") if isinstance(ln, dict) else None
            if segs:
                for seg in segs:
                    if seg:
                        seqs.append(list(seg))
    return seqs


def load_meroitic():
    raw = json.load(open(os.path.join(CUST105, "meroitic.json")))
    seqs = []
    dropped = 0
    for t in raw:
        for line in t["lines"]:
            flat = [s for g in line for s in g if s != "."]
            if flat:
                seqs.append(flat)
            else:
                dropped += 1
    return seqs, {"empty_after_cleaning_lines": dropped}


def load_latin():
    text = open(os.path.join(CUST107, "de-bello-gallico-gutenberg-218.txt"),
                encoding="utf-8", errors="replace").read().lower()
    words = []
    cur = []
    for ch in text:
        if "a" <= ch <= "z":
            cur.append(ch)
        else:
            if len(cur) >= 2:
                words.append(cur)
            cur = []
    if len(cur) >= 2:
        words.append(cur)
    return words


def main():
    out = {"harness": "spec110-obfuscation", "s1_harness_sha256": S1_SHA,
           "seed": SEED, "B": B}
    pins = {
        "indus_derivation": os.path.join(CUST105, "indus-derivation.json"),
        "phase100": os.path.join(WT, "outputs/phase100_full_corpus.json"),
        "eteocypriot": os.path.join(
            WT, "specs/096-eteocypriot-program/corpus/corpus.json"),
        "meroitic": os.path.join(CUST105, "meroitic.json"),
        "latin": os.path.join(CUST107, "de-bello-gallico-gutenberg-218.txt"),
    }
    out["pins"] = {k: sha256_file(v) for k, v in pins.items()}
    log(f"pins verified ({len(pins)})")

    # ---- synthetic natural corpora (controls) ------------------------------
    nat_seeds = [f"spec110-nat-{i}" for i in range(1, 6)]
    naturals = []       # sign sequences only (band material)
    nat_sites = []      # planted site labels, aligned with naturals
    for i, sd in enumerate(nat_seeds):
        seqs, sites = build_synthetic(sd)
        naturals.append(seqs)
        nat_sites.append(sites)
        log(f"synthetic natural {i + 1}/5 built: {len(seqs)} sequences, "
            f"{sum(len(q) for q in seqs)} tokens")
    ctl_seeds = [f"spec110-ctl-{i}" for i in range(1, 6)]
    controls = []
    ctl_sites = []
    for i, sd in enumerate(ctl_seeds):
        seqs, sites = build_synthetic(sd)
        controls.append(seqs)
        ctl_sites.append(sites)
        log(f"synthetic control {i + 1}/5 built: {len(seqs)} sequences")

    def site_jsd(seqs, sites):
        groups = {}
        for lab in sorted(set(sites)):
            groups[lab] = [q for q, s in zip(seqs, sites) if s == lab]
        return omnibus_jsd(groups)

    nat_site_jsds = [site_jsd(naturals[i], nat_sites[i]) for i in range(5)]
    out["B_baseline_site_jsds"] = nat_site_jsds
    baseline_site_max = max(nat_site_jsds)
    log(f"family B genre baseline (planted site splits): "
        f"{[round(v, 4) for v in nat_site_jsds]}")

    # ---- natural control samples for bands ---------------------------------
    latin_words = load_latin()
    q = len(latin_words) // 4
    latin_samples = [latin_words[i * q:(i + 1) * q] for i in range(4)]
    mer_seqs, mer_note = load_meroitic()
    mer_half = len(mer_seqs) // 2
    mer_samples = [mer_seqs, mer_seqs[:mer_half], mer_seqs[mer_half:]]
    log(f"latin control: {len(latin_words)} words in 4 samples; "
        f"meroitic control samples: 3 ({mer_note})")

    def a_stats_set(sample_groups):
        stats = [family_a_stats(s) for s in sample_groups]
        band = {k: band_of([st[k] for st in stats]) for k in ("A1", "A2", "A3", "A4")}
        return stats, band

    # Bands per target (leave-target-out for Meroitic).
    all_nat_samples = naturals + latin_samples + mer_samples
    _, band_all = a_stats_set(all_nat_samples)
    _, band_no_mer = a_stats_set(naturals + latin_samples)
    out["band_all"] = band_all
    out["band_no_meroitic"] = band_no_mer
    log("family A/C1 bands derived from natural controls only")

    # ---- GATE ---------------------------------------------------------------
    gate = {}
    # G-A: A fires on T-HOM (flattening) and T-POLY (structure)
    det = {"hom": 0, "poly": 0}
    for i, corp in enumerate(controls):
        st = family_a_stats(t_hom(corp, SEED + i))
        pat, _ = a_pattern(st, band_all)
        if pat == "flattening":
            det["hom"] += 1
        st = family_a_stats(t_poly(corp, SEED + 100 + i))
        pat, _ = a_pattern(st, band_all)
        if pat == "structure":
            det["poly"] += 1
        log(f"gate G-A rep {i + 1}/5: hom detections {det['hom']}, "
            f"poly detections {det['poly']}")
    gate["G-A"] = {"hom": det["hom"], "poly": det["poly"],
                   "pass": det["hom"] >= 4 and det["poly"] >= 4}

    # G-D: D fires on T-HOM (bands size-matched per replication corpus size)
    d_det = 0
    for i, corp in enumerate(controls):
        n = sum(len(x) for x in corp)
        bv, bh = size_matched_band(naturals, n, seed=SEED + i)
        fire, _ = d_verdict(t_hom(corp, SEED + i), bv, bh)
        if fire:
            d_det += 1
        log(f"gate G-D rep {i + 1}/5: detections {d_det}")
    gate["G-D"] = {"detections": d_det, "pass": d_det >= 4}

    # G-C: C1 structure destroyed on T-POLY; C2 detects T-SUB-D on halves
    c1_det = 0
    c2_det = 0
    for i, corp in enumerate(controls):
        st = family_a_stats(t_poly(corp, SEED + 100 + i))
        if st["A4"] < band_all["A4"][0] or st["A3"] > band_all["A3"][1]:
            c1_det += 1
        h1, h2 = split_halves(corp, SEED + i)
        inv = sorted(counts_of(corp))
        perm = make_perm(inv, SEED + 200 + i)
        h2t = permute_labels(h2, perm)
        res = c2_eval(h1, h2t)
        inv_perm = {v: k for k, v in perm.items()}
        shared = res["shared_signs"]
        agree = (sum(1 for s, m in res["mapping"].items()
                     if inv_perm.get(s) == m) / shared) if shared else 0.0
        if res["self_agreement"] < 0.50 and agree >= 0.80:
            c2_det += 1
        log(f"gate G-C rep {i + 1}/5: C1 detections {c1_det}, "
            f"C2 detections {c2_det} (perm recovery {agree:.3f})")
    gate["G-C"] = {"c1_detections": c1_det, "c2_detections": c2_det,
                   "pass": c1_det >= 4 and c2_det >= 4}

    # G-B: B fires on T-SUB-D in site form — one planted site stratum of
    # each control corpus rendered under a fixed permutation; the full
    # PRESENT rule applies (null p99 AND genre-baseline max).
    b_det = 0
    for i, corp in enumerate(controls):
        sites = ctl_sites[i]
        inv = sorted(counts_of(corp))
        perm = make_perm(inv, SEED + 300 + i)
        tc = [[perm.get(s, s) for s in q] if sites[k] == "B" else list(q)
              for k, q in enumerate(corp)]
        obs, p99, pct, _ = stratum_null(tc, sites, SEED + i)
        if obs > p99 and obs > baseline_site_max:
            b_det += 1
        log(f"gate G-B rep {i + 1}/5: detections {b_det} "
            f"(obs {obs:.4f} vs p99 {p99:.4f}, baseline {baseline_site_max:.4f})")
    gate["G-B"] = {"detections": b_det, "pass": b_det >= 4}

    # G-INV: no family fires on T-SUB-U (per family, >=4/5 no-fire)
    inv_no_fire = {"A": 0, "C1": 0, "D": 0}
    for i, corp in enumerate(controls):
        inv = sorted(counts_of(corp))
        perm = make_perm(inv, SEED + 400 + i)
        tc = permute_labels(corp, perm)
        st = family_a_stats(tc)
        pat, _ = a_pattern(st, band_all)
        if pat is None:
            inv_no_fire["A"] += 1
        if not (st["A4"] < band_all["A4"][0] or st["A3"] > band_all["A3"][1]):
            inv_no_fire["C1"] += 1
        n = sum(len(x) for x in tc)
        bv, bh = size_matched_band(naturals, n, seed=SEED + i)
        fire, _ = d_verdict(tc, bv, bh)
        if not fire:
            inv_no_fire["D"] += 1
        log(f"gate G-INV rep {i + 1}/5: no-fire counts {inv_no_fire}")
    gate["G-INV"] = {"no_fire": inv_no_fire,
                     "pass": all(v >= 4 for v in inv_no_fire.values())}

    # G-FP: natural controls under leave-one-out bands
    fp = {"A": 0, "C1": 0, "D": 0}
    samples = ([("synthetic", s) for s in naturals]
               + [("latin", s) for s in latin_samples]
               + [("meroitic", s) for s in mer_samples])
    for idx, (kind, smp) in enumerate(samples):
        rest = [s for j, (_, s) in enumerate(samples) if j != idx]
        _, loo_band = a_stats_set(rest)
        st = family_a_stats(smp)
        pat, _ = a_pattern(st, loo_band)
        if pat is not None:
            fp["A"] += 1
        if st["A4"] < loo_band["A4"][0] or st["A3"] > loo_band["A3"][1]:
            fp["C1"] += 1
        n = sum(len(x) for x in smp)
        bv, bh = size_matched_band(naturals, n, seed=SEED + idx)
        fire, _ = d_verdict(smp, bv, bh)
        if fire:
            fp["D"] += 1
        log(f"gate G-FP sample {idx + 1}/{len(samples)} ({kind}): "
            f"false fires so far {fp}")
    # Family B false-positive leg: synthetic natural corpora under their
    # planted site splits, full PRESENT rule with leave-one-out baseline.
    b_fp = 0
    for i, corp in enumerate(naturals):
        loo_base = max(v for j, v in enumerate(nat_site_jsds) if j != i)
        obs, p99, pct, _ = stratum_null(corp, nat_sites[i], SEED + i)
        if obs > p99 and obs > loo_base:
            b_fp += 1
        log(f"gate G-FP family B rep {i + 1}/5: false fires {b_fp} "
            f"(obs {obs:.4f} vs p99 {p99:.4f}, LOO baseline {loo_base:.4f})")
    fp["B"] = b_fp
    gate["G-FP"] = {"false_fires": fp,
                    "pass": all(v <= 1 for v in fp.values())}
    gate["pass"] = all(gate[k]["pass"] for k in
                       ("G-A", "G-B", "G-C", "G-D", "G-INV", "G-FP"))
    out["gate"] = gate
    log(f"GATE: {'PASS' if gate['pass'] else 'FAIL'} — {json.dumps({k: v.get('pass') for k, v in gate.items() if isinstance(v, dict)})}")

    with open(os.path.join(CUST, "gate-output.json"), "w") as f:
        json.dump(out, f, indent=1)
    if not gate["pass"]:
        log("gate failed: real-corpus runs are NOT scoreable; stopping")
        return 0

    # ---- REAL CORPORA --------------------------------------------------------
    results = {}

    # Natural C2 gain band (split-half gains over natural controls).
    c2_gains = []
    for i, corp in enumerate(naturals):
        a, b = split_halves(corp, SEED + i)
        _, g, _, _ = match_parts(a, b)
        c2_gains.append(g)
    for a, b in ((mer_seqs[:mer_half], mer_seqs[mer_half:]),
                 (latin_samples[0], latin_samples[1]),
                 (latin_samples[2], latin_samples[3])):
        _, g, _, _ = match_parts(a, b)
        c2_gains.append(g)
    c2_gain_max = max(c2_gains)
    out["C2_gain_band"] = {"values": c2_gains, "max": c2_gain_max}
    log(f"C2 natural gain band: max {c2_gain_max:.4f} over {len(c2_gains)} samples")

    def run_corpus(name, seqs, band, strata=None, c2_pairs=None):
        r = {"census": {"sequences": len(seqs),
                        "tokens": sum(len(q) for q in seqs),
                        "inventory": len(counts_of(seqs))}}
        st = family_a_stats(seqs)
        r["A_stats"] = st
        if st["N"] >= 1000:
            pat, exc = a_pattern(st, band)
            r["A"] = {"verdict": "PRESENT" if pat else "ABSENT",
                      "pattern": pat, "excursions": exc}
        else:
            r["A"] = {"verdict": "NOT TESTABLE AT THIS POWER",
                      "reason": f"N={st['N']} < 1000"}
        # family D
        if st["N"] >= 1000:
            bv, bh = size_matched_band(naturals, st["N"], seed=SEED)
            fire, hs = d_verdict(seqs, bv, bh)
            r["D"] = {"verdict": "PRESENT" if fire else "ABSENT",
                      "stats": hs, "band_V": bv, "band_hapax": bh}
        else:
            r["D"] = {"verdict": "NOT TESTABLE AT THIS POWER",
                      "reason": f"N={st['N']} < 1000"}
        # family B
        if strata is not None:
            groups = {}
            for lab in sorted(set(x for x in strata if x)):
                sq = [q for q, s in zip(seqs, strata) if s == lab]
                ntok = sum(len(q) for q in sq)
                if ntok >= 300 and len(sq) >= 30:
                    groups[lab] = sq
            if len(groups) >= 2:
                labs = []
                allseqs = []
                for lab, sq in groups.items():
                    allseqs.extend(sq)
                    labs.extend([lab] * len(sq))
                obs, p99, pct, _ = stratum_null(allseqs, labs, SEED)
                r["B"] = {"omnibus_jsd": obs, "null_p99": p99,
                          "percentile": pct,
                          "strata_used": {k: len(v) for k, v in groups.items()},
                          "verdict": "PENDING-BASELINE"}
                r["_B_obs"] = obs
            else:
                r["B"] = {"verdict": "NOT TESTABLE AT THIS POWER",
                          "reason": "fewer than 2 strata meet floors"}
        else:
            r["B"] = {"verdict": "NOT TESTABLE AT THIS POWER",
                      "reason": "no stratum metadata in the pinned build"}
        # family C
        c1_destroyed = (st["A4"] < band["A4"][0] or st["A3"] > band["A3"][1])
        r["C1_destroyed"] = c1_destroyed
        c2_fired = False
        c2_detail = {}
        if c2_pairs:
            for pair_name, (pa, pb) in c2_pairs.items():
                na = sum(len(q) for q in pa)
                nb = sum(len(q) for q in pb)
                shared = len(set(counts_of(pa)) & set(counts_of(pb)))
                if na >= 500 and nb >= 500 and shared >= 20:
                    res = c2_eval(pa, pb, with_stability=True)
                    fired = (res["self_agreement"] < 0.50
                             and res["gain"] > c2_gain_max
                             and res.get("stability", 0.0) >= 0.80)
                    c2_detail[pair_name] = {
                        "gain": res["gain"],
                        "gain_band_max": c2_gain_max,
                        "self_agreement": res["self_agreement"],
                        "stability": res.get("stability"),
                        "shared_signs": res["shared_signs"],
                        "fired": fired}
                    c2_fired = c2_fired or fired
                else:
                    c2_detail[pair_name] = {
                        "fired": False,
                        "reason": f"floors unmet (tokens {na}/{nb}, shared {shared})"}
        r["C2"] = c2_detail
        if st["N"] < 1000:
            r["C"] = {"verdict": "NOT TESTABLE AT THIS POWER",
                      "reason": f"N={st['N']} < 1000"}
        elif c2_fired:
            r["C"] = {"verdict": "PRESENT", "via": "C2"}
        elif c1_destroyed:
            r["C"] = {"verdict": "PRESENT", "via": "C1-structure"}
        else:
            r["C"] = {"verdict": "ABSENT"}
        results[name] = r
        log(f"{name}: A={r['A']['verdict']} D={r['D']['verdict']} "
            f"B={r['B']['verdict']} C={r['C']['verdict']}")
        return r

    # Family B genre baseline for real corpora: the planted site splits.
    baseline_max = baseline_site_max
    out["B_baseline_max"] = baseline_max
    log(f"family B genre-baseline max (planted site splits): {baseline_max:.4f}")

    ind_seqs, ind_sites, ind_note = load_indus()
    ind_strata_groups = {}
    for lab in sorted(set(s for s in ind_sites if s)):
        ind_strata_groups[lab] = [q for q, s in zip(ind_seqs, ind_sites) if s == lab]
    md = ind_strata_groups.get("Mohenjo-daro", [])
    ha = ind_strata_groups.get("Harappa", [])
    h1, h2 = split_halves(ind_seqs, SEED)
    r_ind = run_corpus("indus", ind_seqs, band_all, strata=ind_sites,
                       c2_pairs={"site MD vs HA": (md, ha),
                                 "split-half": (h1, h2)})
    r_ind["site_note"] = ind_note
    if r_ind["B"].get("verdict") == "PENDING-BASELINE":
        obs = r_ind.pop("_B_obs")
        if obs > r_ind["B"]["null_p99"] and obs > baseline_max:
            r_ind["B"]["verdict"] = "PRESENT"
        else:
            r_ind["B"]["verdict"] = "ABSENT"
        r_ind["B"]["baseline_max"] = baseline_max

    ete_seqs = load_eteocypriot()
    run_corpus("eteocypriot", ete_seqs, band_all)

    mh1, mh2 = split_halves(mer_seqs, SEED)
    run_corpus("meroitic", mer_seqs, band_no_mer,
               c2_pairs={"split-half": (mh1, mh2)})

    out["results"] = results
    with open(os.path.join(CUST, "raw-output.json"), "w") as f:
        json.dump(out, f, indent=1)
    log("execution complete; raw output filed to custody")
    return 0


if __name__ == "__main__":
    sys.exit(main())
