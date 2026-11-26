#!/usr/bin/env python3
"""Spec 105 Stage 6 execution: L6 boundary gates G-ETE, G-MER, G-IND.

Registered by records/stage-6-registration-2026-11-25.md (committed
before this script ran; the G-IND checker refuses to open the reserve
unless that registration is tracked and unmodified in the clone's git
index). Each gate runs under two independent checker implementations
that must agree exactly:

  A — a Python checker over the filed lower-rung outputs.
  B — an independent checker built on jq event streams over the
      datasets' raw bytes through sort/uniq -c with awk assemblies,
      sharing no code with A, re-deriving the sandbox-side structures
      it checks from the streams and applying its own copy of the
      outside tables.

The outside tables (registration section 2) live in the checker
sections below, once per implementation. The sandboxes receive
nothing: this script reads filed outputs and custody datasets and
writes only the stage output JSON.

Usage: stage-6-execution.py <clone_root> <custody_dir> <output_path>
"""

import hashlib
import json
import math
import subprocess
import sys
from fractions import Fraction

CLONE = sys.argv[1]
CUSTODY = sys.argv[2]
OUT = sys.argv[3]
RECORDS = CLONE + "/specs/105-elsewhere-sandbox/records"
REGISTRATION = "specs/105-elsewhere-sandbox/records/stage-6-registration-2026-11-25.md"

EXPECTED_HASHES = {
    "indus-derivation.json": "84476daa3a1d9ded33ee7c3eeaffb29fac0290ecf3507873206d4d60ac8b948b",
    "indus-reserve.json": "bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff",
    "eteocypriot.json": "2799d1034e8af50a110e7df69d6f79ab931cbc13db480ebbc8d4dfcf589421fe",
    "meroitic.json": "a8f551e5cc5264decbc2c01d7ee924740245ce8cbeca6b4b7f776e88a3920fb7",
}
CORPUS096_SHA256 = "2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_records(name):
    with open(RECORDS + "/" + name, encoding="utf-8") as f:
        return json.load(f)


def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError("command failed: %s\n%s" % (cmd, r.stderr))
    return r.stdout


opened_paths = []
custody_hashes = {}
for name, want in EXPECTED_HASHES.items():
    got = sha256_file(CUSTODY + "/" + name)
    custody_hashes[name] = got
    assert got == want, "custody hash mismatch for %s: %s" % (name, got)

corpus096_hash = sha256_file(
    CLONE + "/specs/096-eteocypriot-program/corpus/corpus.json")
assert corpus096_hash == CORPUS096_SHA256, "Spec 096 corpus hash mismatch"

stage1 = load_records("stage-1-output-2026-11-25.json")
stage2 = load_records("stage-2-output-2026-11-25.json")
stage3 = load_records("stage-3-output-2026-11-25.json")
stage4 = load_records("stage-4-output-2026-11-25.json")
stage5 = load_records("stage-5-output-2026-11-25.json")

result = {
    "stage": 6,
    "rung": "L6",
    "custody": custody_hashes,
    "spec096_corpus_sha256": corpus096_hash,
    "gates": {},
    "checks": {},
}

# ---------------------------------------------------------------- G-ETE
# Outside table (registration section 2): the Common syllabary values.
CYPRIOT_A = set(
    "a e i o u".split()
    + "ka ke ki ko ku la le li lo lu ma me mi mo mu na ne ni no nu "
      "pa pe pi po pu ra re ri ro ru sa se si so su ta te ti to tu "
      "wa we wi wo ya ye za ze zi zo xa xe xi xo".split()
)
assert len(CYPRIOT_A) == 59


def ete_value(mark):
    """Checker-side value of a derived mark, per the filed token
    conventions: '?' asserts no value (exempt); '[x]' carries x."""
    if mark == "?":
        return None
    if mark.startswith("[") and mark.endswith("]"):
        return mark[1:-1]
    return mark


def gate_ete_a():
    inv = stage1["sandboxes"]["eteocypriot"]["derivation_result"]["inventory"]
    lines = []
    for m in inv:
        v = ete_value(m)
        if v is None:
            lines.append("ETE1|%s|EXEMPT|EXEMPT" % m)
        else:
            lines.append("ETE1|%s|%s|%s" % (m, v, "IN" if v in CYPRIOT_A else "OUT"))
    for kind, src in (("joint", stage4["sandboxes"]["eteocypriot"]["joint_classes"]),
                      ("identity", stage5["sandboxes"]["eteocypriot"]["identity_classes"])):
        for cls in src:
            vals = {ete_value(m) for m in cls["members"]}
            vals.discard(None)
            lines.append("ETE2|%s|%s|%d|%s" % (
                kind, cls["id"], len(vals), "HOMOG" if len(vals) <= 1 else "NOT"))
    return sorted(lines)


# Implementation B: its own copy of the table, inventory re-derived from
# the dataset stream by jq + sort -u, classes read by jq as data.
CYPRIOT_B_AWK = (
    "a e i o u ka ke ki ko ku la le li lo lu ma me mi mo mu na ne ni no nu "
    "pa pe pi po pu ra re ri ro ru sa se si so su ta te ti to tu "
    "wa we wi wo ya ye za ze zi zo xa xe xi xo"
)


def gate_ete_b():
    inv = run("jq -r '.[].lines[][][]' %s/eteocypriot.json | sort -u"
              % CUSTODY).split()
    opened_paths.append(CUSTODY + "/eteocypriot.json")
    classes = run(
        "jq -r '.sandboxes.eteocypriot.joint_classes[] | "
        "\"joint\\t\" + .id + \"\\t\" + (.members | join(\",\"))' "
        + RECORDS + "/stage-4-output-2026-11-25.json; "
        "jq -r '.sandboxes.eteocypriot.identity_classes[] | "
        "\"identity\\t\" + .id + \"\\t\" + (.members | join(\",\"))' "
        + RECORDS + "/stage-5-output-2026-11-25.json")
    prog = """
BEGIN { n = split("%s", t, " "); for (i = 1; i <= n; i++) INN[t[i]] = 1 }
function value(m) {
  if (m == "?") return ""
  if (substr(m, 1, 1) == "[" && substr(m, length(m), 1) == "]")
    return substr(m, 2, length(m) - 2)
  return m
}
FNR == NR {
  v = value($0)
  if (v == "") print "ETE1|" $0 "|EXEMPT|EXEMPT"
  else print "ETE1|" $0 "|" v "|" ((v in INN) ? "IN" : "OUT")
  next
}
{
  split($3, mem, ","); delete seen; d = 0
  for (i in mem) { v = value(mem[i]); if (v != "" && !(v in seen)) { seen[v] = 1; d++ } }
  print "ETE2|" $1 "|" $2 "|" d "|" ((d <= 1) ? "HOMOG" : "NOT")
}
""" % CYPRIOT_B_AWK
    tmp_inv = "/tmp/s105s6-b-ete-inv.txt"
    with open(tmp_inv, "w", encoding="utf-8") as f:
        f.write("\n".join(inv) + "\n")
    tmp_cls = "/tmp/s105s6-b-ete-cls.txt"
    with open(tmp_cls, "w", encoding="utf-8") as f:
        f.write(classes)
    out = run("awk '%s' %s %s" % (prog.replace("'", "'\\''"), tmp_inv, tmp_cls))
    return sorted(out.splitlines())


ete_a = gate_ete_a()
ete_b = gate_ete_b()
ete_agree = ete_a == ete_b
ete1_out = [l for l in ete_a if l.startswith("ETE1|") and l.endswith("|OUT")]
ete2_bad = [l for l in ete_a if l.startswith("ETE2|") and l.endswith("|NOT")]
ete_exempt = [l for l in ete_a if l.startswith("ETE1|") and l.endswith("|EXEMPT")]
result["gates"]["G-ETE"] = {
    "status": "COMPLETED" if ete_agree else "STOPPED",
    "implementations_agree": ete_agree,
    "table_a": ete_a,
    "table_b": ete_b,
    "comparisons": {
        "ETE-1": {
            "word": "GOOD" if ete_agree and not ete1_out else "NOT-GOOD",
            "marks_checked": len([l for l in ete_a if l.startswith("ETE1|")]),
            "exempt_marks": [l.split("|")[1] for l in ete_exempt],
            "out_of_table": [l.split("|")[1] for l in ete1_out],
        },
        "ETE-2": {
            "word": "GOOD" if ete_agree and not ete2_bad else "NOT-GOOD",
            "classes_checked": len([l for l in ete_a if l.startswith("ETE2|")]),
            "non_homogeneous": [l.split("|")[2] for l in ete2_bad],
        },
    },
}
result["checks"]["TC-105-20"] = "PASS" if ete_agree else "FAIL"

# ---------------------------------------------------------------- G-MER
# Outside table (registration section 2): character -> sign named, from
# the pinned build's transliteration map, test-corpus conversion.
MER_SIGNS_A = {
    "a": "a", "e": "e", "i": "i", "o": "o", "y": "y", "w": "w",
    "b": "b", "p": "p", "m": "m", "n": "n", "N": "ne", "r": "r",
    "l": "l", "x": "ḫ", "X": "ẖ", "S": "s", "s": "se", "k": "k",
    "q": "q", "t": "t", "d": "d",
}


def mer_category(mark):
    if mark in MER_SIGNS_A:
        return "SIGN:" + MER_SIGNS_A[mark]
    if mark.isdigit():
        return "NUMERAL"
    if mark == ".":
        return "LACUNA"
    return "UNACCOUNTED"


def gate_mer_a():
    inv = stage1["sandboxes"]["meroitic"]["derivation_result"]["inventory"]
    lines = ["MER1|%s|%s" % (m, mer_category(m)) for m in inv]
    pos = {r["mark"]: r for r in stage3["sandboxes"]["meroitic"]["positions"]}
    a = pos["a"]
    lines.append("MER2|a|%d|%d" % (a["initial"] + a["sole"], a["count"]))
    i = pos["i"]
    lines.append("MER3|i|%d|%d" % (i["count"] - i["initial"] - i["sole"], i["count"]))
    return sorted(lines)


def gate_mer_b():
    # jq streams the group strings; awk classifies characters and
    # positions itself (sole/initial/final/medial per group), tallies
    # the inventory and the a/i positional counts, and applies its own
    # copy of the outside table.
    groups = run("jq -r '.[].lines[][] | join(\"\")' %s/meroitic.json" % CUSTODY)
    opened_paths.append(CUSTODY + "/meroitic.json")
    tmp = "/tmp/s105s6-b-mer-groups.txt"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(groups)
    prog = """
BEGIN {
  split("a e i o y w b p m n N r l x X S s k q t d", L, " ")
  split("a e i o y w b p m n ne r l ḫ ẖ s se k q t d", V, " ")
  for (j in L) SIGN[L[j]] = V[j]
}
{
  len = length($0)
  for (p = 1; p <= len; p++) {
    c = substr($0, p, 1); INV[c] = 1
    cls = (len == 1) ? "sole" : (p == 1) ? "initial" : (p == len) ? "final" : "medial"
    if (c == "a" || c == "i") { CNT[c]++; POS[c, cls]++ }
  }
}
END {
  for (c in INV) {
    if (c in SIGN) cat = "SIGN:" SIGN[c]
    else if (c ~ /^[0-9]$/) cat = "NUMERAL"
    else if (c == ".") cat = "LACUNA"
    else cat = "UNACCOUNTED"
    print "MER1|" c "|" cat
  }
  print "MER2|a|" (POS["a", "initial"] + POS["a", "sole"]) "|" CNT["a"]
  print "MER3|i|" (CNT["i"] - POS["i", "initial"] - POS["i", "sole"]) "|" CNT["i"]
}
"""
    out = run("awk '%s' %s" % (prog.replace("'", "'\\''"), tmp))
    return sorted(out.splitlines())


mer_a = gate_mer_a()
mer_b = gate_mer_b()
mer_agree = mer_a == mer_b


def positional_word(conforming, total):
    # Registered tolerance (D-105-26): at least 95 in 100, exact
    # fraction arithmetic: conforming/total >= 19/20.
    return "GOOD" if Fraction(conforming, total) >= Fraction(19, 20) else "NOT-GOOD"


mer1_bad = [l.split("|")[1] for l in mer_a
            if l.startswith("MER1|") and l.endswith("UNACCOUNTED")]
mer2 = [l.split("|") for l in mer_a if l.startswith("MER2|")][0]
mer3 = [l.split("|") for l in mer_a if l.startswith("MER3|")][0]
result["gates"]["G-MER"] = {
    "status": "COMPLETED" if mer_agree else "STOPPED",
    "implementations_agree": mer_agree,
    "table_a": mer_a,
    "table_b": mer_b,
    "comparisons": {
        "MER-1": {
            "word": "GOOD" if mer_agree and not mer1_bad else "NOT-GOOD",
            "marks_checked": len([l for l in mer_a if l.startswith("MER1|")]),
            "unaccounted": mer1_bad,
        },
        "MER-2": {
            "word": positional_word(int(mer2[2]), int(mer2[3])) if mer_agree else "NOT-GOOD",
            "conforming": int(mer2[2]),
            "total": int(mer2[3]),
            "conformance": "%d/%d" % (int(mer2[2]), int(mer2[3])),
        },
        "MER-3": {
            "word": positional_word(int(mer3[2]), int(mer3[3])) if mer_agree else "NOT-GOOD",
            "conforming": int(mer3[2]),
            "total": int(mer3[3]),
            "conformance": "%d/%d" % (int(mer3[2]), int(mer3[3])),
        },
    },
}
result["checks"]["TC-105-21"] = "PASS" if mer_agree else "FAIL"

# ---------------------------------------------------------------- G-IND
# Frozen by the registration (section 5): unseen-mark rule
# eps = 1/(5611+372) = 1/5983 under both models; margin 0.05 nats/token.
N_TOK = 5611
N_ART = 1336
EPS_DEN = 5983
MARGIN = 0.05
RESERVE_TOKENS = 1391
RESERVE_ARTIFACTS = 334

counts_a = {r["mark"]: r["count"] for r in stage2["sandboxes"]["indus"]["table"]}
assert sum(counts_a.values()) == N_TOK and len(counts_a) == 372
pairs_a = {(p["first"], p["second"]): p["count"]
           for p in stage3["sandboxes"]["indus"]["pairs"]}
pos_a = {r["mark"]: r for r in stage3["sandboxes"]["indus"]["positions"]}
succ_a = {m: r["successors_total"] for m, r in pos_a.items()}
init_a = {m: r["initial"] + r["sole"] for m, r in pos_a.items()}
assert sum(init_a.values()) == N_ART  # one group per derivation artifact


def score_a(reserve):
    cases = {}
    total = 0

    def add(model, rule, num, den):
        key = (model, rule, num, den)
        cases[key] = cases.get(key, 0) + 1

    for art in reserve:
        for line in art["lines"]:
            for group in line:
                prev = None
                for m in group:
                    total += 1
                    if m not in counts_a:
                        add("baseline", "unseen", 1, EPS_DEN)
                        add("derived", "unseen", 1, EPS_DEN)
                        prev = m
                        continue
                    add("baseline", "unigram", counts_a[m], N_TOK)
                    if prev is None:
                        if init_a.get(m, 0) > 0:
                            add("derived", "initial", init_a[m], N_ART)
                        else:
                            add("derived", "backoff", counts_a[m], N_TOK)
                    else:
                        c = pairs_a.get((prev, m), 0)
                        if c > 0:
                            add("derived", "pair", c, succ_a[prev])
                        else:
                            add("derived", "backoff", counts_a[m], N_TOK)
                    prev = m
    return cases, total


def means_from_cases(cases):
    sums = {"baseline": 0.0, "derived": 0.0}
    for (model, rule, num, den), n in sorted(cases.items()):
        sums[model] += n * (-math.log(num / den))
    total = sum(n for (model, *_), n in cases.items() if model == "baseline")
    return sums["baseline"] / total, sums["derived"] / total, total


def gate_ind_b():
    dev = run("jq -r '.[].lines[][] | join(\"\\t\")' %s/indus-derivation.json"
              % CUSTODY)
    opened_paths.append(CUSTODY + "/indus-derivation.json")
    res = run("jq -r '.[].lines[][] | join(\"\\t\")' %s/indus-reserve.json"
              % CUSTODY)
    opened_paths.append(CUSTODY + "/indus-reserve.json")
    f_dev, f_res = "/tmp/s105s6-b-ind-dev.txt", "/tmp/s105s6-b-ind-res.txt"
    with open(f_dev, "w", encoding="utf-8") as f:
        f.write(dev)
    with open(f_res, "w", encoding="utf-8") as f:
        f.write(res)
    prog = """
FNR == NR {
  n = split($0, t, "\\t")
  for (i = 1; i <= n; i++) {
    cnt[t[i]]++
    if (i == 1) ini[t[i]]++
    if (i > 1) { pr[t[i-1] SUBSEP t[i]]++; suc[t[i-1]]++ }
  }
  next
}
function emit(model, rule, num, den) {
  CASE[model SUBSEP rule SUBSEP num SUBSEP den]++
  LOSS[model] += -log(num / den)
}
{
  n = split($0, t, "\\t"); prev = ""
  for (i = 1; i <= n; i++) {
    m = t[i]; TOT++
    if (!(m in cnt)) { emit("baseline", "unseen", 1, 5983); emit("derived", "unseen", 1, 5983); prev = m; continue }
    emit("baseline", "unigram", cnt[m], 5611)
    if (prev == "") {
      if (ini[m] > 0) emit("derived", "initial", ini[m], 1336)
      else emit("derived", "backoff", cnt[m], 5611)
    } else if (pr[prev SUBSEP m] > 0) emit("derived", "pair", pr[prev SUBSEP m], suc[prev])
    else emit("derived", "backoff", cnt[m], 5611)
    prev = m
  }
}
END {
  for (k in CASE) { split(k, p, SUBSEP); print "CASE|" p[1] "|" p[2] "|" p[3] "|" p[4] "|" CASE[k] }
  print "TOKENS|" TOT
  printf "MEAN6|baseline|%.6f\\n", LOSS["baseline"] / TOT
  printf "MEAN6|derived|%.6f\\n", LOSS["derived"] / TOT
}
"""
    out = run("awk '%s' %s %s" % (prog.replace("'", "'\\''"), f_dev, f_res))
    cases, tokens, mean6 = {}, 0, {}
    for line in out.splitlines():
        parts = line.split("|")
        if parts[0] == "CASE":
            cases[(parts[1], parts[2], int(parts[3]), int(parts[4]))] = int(parts[5])
        elif parts[0] == "TOKENS":
            tokens = int(parts[1])
        elif parts[0] == "MEAN6":
            mean6[parts[1]] = parts[2]
    return cases, tokens, mean6


# The registration guard (registration section 5): the reserve is
# opened only if the registration file is tracked and unmodified.
guard_status = run("git -C %s status --porcelain -- %s" % (CLONE, REGISTRATION))
guard_tracked = run("git -C %s ls-files --error-unmatch %s" % (CLONE, REGISTRATION))
guard_ok = guard_status.strip() == "" and guard_tracked.strip() == REGISTRATION

if not guard_ok:
    result["gates"]["G-IND"] = {"status": "STOPPED",
                                "reason": "registration guard failed",
                                "guard_status": guard_status}
    result["checks"]["TC-105-22"] = "FAIL"
    result["checks"]["TC-105-23"] = "FAIL"
else:
    reserve_hash_sealed = custody_hashes["indus-reserve.json"]
    with open(CUSTODY + "/indus-reserve.json", encoding="utf-8") as f:
        reserve = json.load(f)  # THE UNSEALING: the only content read.
    opened_paths.append(CUSTODY + "/indus-reserve.json (content, G-IND checker)")
    reserve_hash_scored = sha256_file(CUSTODY + "/indus-reserve.json")
    cases_a, total_a = score_a(reserve)
    base_mean, der_mean, tot_check = means_from_cases(cases_a)
    assert tot_check == total_a
    cases_b, total_b, mean6_b = gate_ind_b()
    ind_agree = (cases_a == cases_b and total_a == total_b
                 and "%.6f" % base_mean == mean6_b["baseline"]
                 and "%.6f" % der_mean == mean6_b["derived"])
    diff = base_mean - der_mean
    unseen = sum(n for (model, rule, *_), n in cases_a.items()
                 if model == "baseline" and rule == "unseen")
    case_list = [{"model": k[0], "rule": k[1], "numerator": k[2],
                  "denominator": k[3], "tokens": n}
                 for k, n in sorted(cases_a.items())]
    result["gates"]["G-IND"] = {
        "status": "COMPLETED" if ind_agree else "STOPPED",
        "implementations_agree": ind_agree,
        "registration_guard": "PASS",
        "reserve_artifacts_scored": len(reserve),
        "reserve_tokens_scored": total_a,
        "reserve_hash_as_sealed": reserve_hash_sealed,
        "reserve_hash_as_scored": reserve_hash_scored,
        "unseen_tokens": unseen,
        "case_table": case_list,
        "baseline_mean_log_loss": base_mean,
        "derived_mean_log_loss": der_mean,
        "baseline_mean_log_loss_6dp": "%.6f" % base_mean,
        "derived_mean_log_loss_6dp": "%.6f" % der_mean,
        "difference": diff,
        "difference_6dp": "%.6f" % diff,
        "frozen_margin_nats_per_token": MARGIN,
        "comparisons": {
            "IND-1": {"word": "GOOD" if ind_agree and diff >= MARGIN else "NOT-GOOD"},
        },
    }
    result["checks"]["TC-105-22"] = "PASS" if ind_agree else "FAIL"
    result["checks"]["TC-105-23"] = (
        "PASS" if reserve_hash_sealed == reserve_hash_scored == EXPECTED_HASHES["indus-reserve.json"]
        else "FAIL")

result["opened_paths_audit"] = opened_paths

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=1, sort_keys=False)
    f.write("\n")

for g in ("G-ETE", "G-MER", "G-IND"):
    gate = result["gates"][g]
    print(g, gate["status"], json.dumps(gate.get("comparisons", {}), ensure_ascii=False))
print("checks:", json.dumps(result["checks"]))
if "G-IND" in result["gates"] and result["gates"]["G-IND"]["status"] == "COMPLETED":
    gi = result["gates"]["G-IND"]
    print("G-IND baseline %.6f derived %.6f diff %.6f margin %.2f unseen %d tokens %d"
          % (gi["baseline_mean_log_loss"], gi["derived_mean_log_loss"],
             gi["difference"], MARGIN, gi["unseen_tokens"],
             gi["reserve_tokens_scored"]))
