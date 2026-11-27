#!/usr/bin/env python3
"""Spec 109 Stage 2 verification: TC-109-04 (Part 2 conformance),
TC-109-05 (Part 3 conformance), TC-109-03 (replay).

Independent recomputation from the filed intermediate tables and the
pinned sources, by an implementation separate from the harness's two.
Exit 0 iff every check passes; the check list is printed as JSON.
"""
import collections, hashlib, json, math, os, subprocess, sys

WT = os.path.expanduser("~/.syncyard/worktrees/glossa/spec109-stage2-wt-20261127")
REC = os.path.join(WT, "specs/109-generative-decipherment-engine/records")
CUST105 = os.path.expanduser("~/.syncyard/worktrees/glossa/glossa-custody/spec105")
CUST109 = os.path.expanduser("~/.syncyard/worktrees/glossa/glossa-custody/spec109")
POS = ["initial", "medial", "final", "sole"]
checks = []
def check(name, ok, detail=""):
    checks.append({"check": name, "pass": bool(ok), "detail": detail})

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def flat(a):
    return [s for line in a["lines"] for g in line for s in g]

# ---- third implementation of the positional table (slice-based) ----
def pos_table_c(arts):
    tab = {}
    for seq in arts:
        if len(seq) == 1:
            cells = [(seq[0], "sole")]
        else:
            cells = ([(seq[0], "initial")] + [(s, "medial") for s in seq[1:-1]]
                     + [(seq[-1], "final")])
        for s, p in cells:
            r = tab.setdefault(s, dict.fromkeys(POS, 0))
            r[p] += 1
    return tab

der = [flat(a) for a in json.load(open(os.path.join(CUST105, "indus-derivation.json")))]
res = [flat(a) for a in json.load(open(os.path.join(CUST105, "indus-reserve.json")))]
full = der + res
ptab = json.load(open(os.path.join(REC, "stage-2-positional-table.json")))
check("TC109-04 full positional table recomputes",
      pos_table_c(full) == ptab["full_table"])
check("TC109-04 derivation positional table recomputes",
      pos_table_c(der) == ptab["derivation_table"])

def calls(tab):
    out = {}
    for m, r in tab.items():
        tot = sum(r.values())
        if tot < 5: continue
        mx = max(r.values())
        doms = [p for p in POS if r[p] == mx]
        e = {"dominant": doms[0] if len(doms) == 1 else None, "total": tot}
        for rho in (0.95, 0.90):
            e[rho] = len(doms) == 1 and mx / tot >= rho
        out[m] = e
    return out

seen, halves = {}, [[], []]
for seq in der:
    t = tuple(seq)
    if t not in seen: seen[t] = len(seen)
    halves[seen[t] % 2].append(seq)
half_tabs = [pos_table_c(h) for h in halves]
check("TC109-04 half tables recompute",
      all(half_tabs[h] == ptab["half_tables"][h] for h in range(2)))
fc, hc = calls(ptab["full_table"]), [calls(t) for t in ptab["half_tables"]]
recomputed_structures = []
for m in sorted(fc):
    for rho in (0.95, 0.90):
        if not fc[m][rho]: continue
        states = []
        for h in range(2):
            e = hc[h].get(m)
            states.append("unmeasurable" if e is None else
                          "reproduces" if e[rho] and e["dominant"] == fc[m]["dominant"] else "differs")
        stab = ("INDETERMINATE" if "unmeasurable" in states else
                "STABLE" if all(x == "reproduces" for x in states) else "UNSTABLE")
        recomputed_structures.append({"mark": m, "rho": rho, "dominant": fc[m]["dominant"],
                                      "stability": stab})
filed_structures = [{"mark": s["mark"], "rho": s["rho"], "dominant": s["dominant"],
                     "stability": s["stability"]} for s in ptab["structures"]]
check("TC109-04 structures recompute from filed tables",
      recomputed_structures == filed_structures,
      f"{len(filed_structures)} structures")

l3 = json.load(open(os.path.join(WT, "specs/105-elsewhere-sandbox/records/stage-3-output-2026-11-25.json")))
l3_tab = {r["mark"]: {"initial": r["initial"], "medial": r["medial"],
                      "final": r["final"], "sole": r["sole"]}
          for r in l3["sandboxes"]["indus"]["positions"]}
check("TC109-04 L3 reconciliation exact",
      all(l3_tab.get(m) == ptab["derivation_table"].get(m)
          for m in set(l3_tab) | set(ptab["derivation_table"]))
      and ptab["l3_reconciliation"]["cell_mismatches"] == [])
l3c = calls(l3_tab)
divs = 0
for m in set(fc) | set(l3c):
    for rho in (0.95, 0.90):
        f = fc.get(m, {}).get(rho, False); l = l3c.get(m, {}).get(rho, False)
        if f != l or (f and l and fc[m]["dominant"] != l3c[m]["dominant"]): divs += 1
check("TC109-04 L3 call divergences recompute", divs == len(ptab["l3_call_divergences"]) == 50)

filings = json.load(open(os.path.join(REC, "stage-2-gate-filings.json")))
stable = [s for s in filed_structures if s["stability"] == "STABLE"]
check("TC109-04 every STABLE structure has a gate filing reference",
      len(filings) == len(stable) == 108
      and {(f["mark"], f["rho"]) for f in filings} == {(s["mark"], s["rho"]) for s in stable}
      and all(f["gate"] == "Spec 091 anchor comparison" for f in filings))

# ---- numerical spot recomputation ----
NUM = {"M012", "M059", "M391"}
tt = collections.Counter(sum(1 for s in x if s in NUM) for x in full if any(s in NUM for s in x))
ntab = json.load(open(os.path.join(REC, "stage-2-numerical-table.json")))
check("TC109-04 Type-T distribution recomputes",
      {int(k): v for k, v in ntab["typeT_full"]["histogram"].items()} == dict(tt)
      and ntab["typeT_full"]["n"] == 486 and ntab["typeT_full"]["max"] == 3)
check("TC109-04 check-1 degeneracy is as disclosed",
      abs(ntab["null_thresholds"]["variance_p05"] - ntab["typeT_full"]["variance"]) < 1e-12
      and ntab["checks"]["check1_bounded_range"]["full_supported"] is False)
check("TC109-04 counted tokens recompute",
      all(sum(1 for x in full for s in x if s == m) == ntab["checks"]["check2_positional_restriction"]
          ["counted_calls"][m]["tokens_full"] for m in NUM))

# ---- TC-109-05 ----
pairs_path = os.path.join(WT, "specs/093-material-context-channel/records/t103-join-pairs-v1.jsonl")
check("TC109-05 join pairs pin", sha256_file(pairs_path) ==
      "7107f738832a4e3b04cff91d81073212bc0f3a77afed6f0ccc3cee4fce621703")
pairs = [json.loads(l) for l in open(pairs_path)]
check("TC109-05 join (b) census recomputes",
      len(pairs) == 179
      and collections.Counter(p["material_raw"] for p in pairs) ==
          {"Steatite": 176, "Clay": 1, "Faience": 1, "-": 1}
      and all(p["site"] == "Mohenjo-daro" for p in pairs))
p100 = {t["cisi_id"]: t for t in json.load(open(os.path.join(WT, "outputs/phase100_full_corpus.json")))["translations"]}
p114 = json.load(open(os.path.join(WT, "outputs/phase114_full_seal_translations.json")))["all_translations"]
check("TC109-05 join (a) census recomputes",
      all(p100[k]["site"] == p114[k]["site"] and p100[k]["signs"] == p114[k]["signs"] for k in p100)
      and collections.Counter(t["site"] for t in p100.values()) ==
          {"Mohenjo-daro": 606, "Harappa": 492, "Lothal": 124, "Kalibangan": 110,
           "Dholavira": 106, "Chanhu-daro": 78, "Surkotada": 61, "Banawali": 60, "Rakhigarhi": 33})

def term_for(rows, labels, sign):
    byv = collections.defaultdict(lambda: [0, 0, 0, 0]); tot = [0, 0, 0, 0]
    for seq, v in zip(rows, labels):
        n = len(seq)
        for k, s in enumerate(seq):
            if s != sign: continue
            p = 3 if n == 1 else 0 if k == 0 else 2 if k == n - 1 else 1
            byv[v][p] += 1; tot[p] += 1
    ns = sum(tot); t = 0.0
    for v, cells in byv.items():
        nv = sum(cells)
        for c in range(4):
            if cells[c]: t += (cells[c] / ns) * math.log((cells[c] / nv) / (tot[c] / ns))
    return t

ctx = json.load(open(os.path.join(REC, "stage-2-context-terms.json")))
site_rows = [p100[k]["signs"] for k in sorted(p100)]
site_labels = [p100[k]["site"] for k in sorted(p100)]
t_m048 = term_for(site_rows, site_labels, "M048")
check("TC109-05 site term M048 recomputes",
      abs(t_m048 - ctx["terms"]["site"]["terms"]["M048"]["term"]) < 1e-9,
      f"{t_m048:.6f} vs {ctx['terms']['site']['terms']['M048']['term']:.6f}")
objs = {}
for line in open(os.path.join(WT, "glossa-corpus/indus/canonical/objects.jsonl")):
    o = json.loads(line); objs[o["glossa_id"]] = o
b_rows = [objs[p["text_id"]]["_source_extra"]["raw_signs"] for p in pairs]
b_labels = [p["material_raw"] for p in pairs]
t_p276 = term_for(b_rows, b_labels, "P276")
check("TC109-05 material term P276 recomputes",
      abs(t_p276 - ctx["terms"]["material"]["terms"]["P276"]["term"]) < 1e-9,
      f"{t_p276:.6f} vs {ctx['terms']['material']['terms']['P276']['term']:.6f}")
check("TC109-05 weights are the frozen effective-N shares",
      abs(ctx["terms"]["site"]["weight"] - 1670 / 1849) < 1e-12
      and abs(ctx["terms"]["material"]["weight"] - 179 / 1849) < 1e-12
      and abs(ctx["terms"]["find_context"]["weight"] - 179 / 1849) < 1e-12)
reg = [json.loads(l) for l in open(os.path.join(CUST109, "stage-2-generated-hypotheses-register.jsonl"))]
ct = [r for r in reg if r["kind"] == "context_term"]
check("TC109-05 register terms carry caps and the no-iconography label",
      all(r["label"] == "no iconography component" for r in ct)
      and all(abs(r["cap_p99"] - ctx["terms"][r["family"]]["cap_p99"]) < 1e-12 for r in ct)
      and all(min(r["term"], r["cap_p99"]) <= r["cap_p99"] for r in ct))
check("TC109-05 no iconography field in any join row",
      all("iconography" not in json.dumps(r) for r in json.load(open(os.path.join(REC, "stage-2-joinb-table.json")))))
check("TC109-05 channel verdict is the frozen rule's consequence",
      ctx["validation"]["verdict"] == "CHANNEL NULL"
      and ctx["validation"]["pooled_delta"] <= ctx["validation"]["null_p99"]
      and ctx["join_a"]["validates"] and ctx["join_b"]["validates"])

# ---- TC-109-03 replay ----
raw = json.load(open(os.path.join(REC, "stage-2-raw-output.json")))
want_reg = raw["register"]["sha256"]; want_raw = sha256_file(os.path.join(REC, "stage-2-raw-output.json"))
r = subprocess.run([sys.executable, os.path.join(REC, "stage-2-harness.py")],
                   capture_output=True, text=True)
got_reg = sha256_file(os.path.join(CUST109, "stage-2-generated-hypotheses-register.jsonl"))
got_raw = sha256_file(os.path.join(CUST109, "stage-2-raw-output.json"))
check("TC109-03 replay reproduces the register and raw output exactly",
      r.returncode == 0 and got_reg == want_reg and got_raw == want_raw,
      f"register {got_reg[:12]} raw {got_raw[:12]}")

npass = sum(1 for c in checks if c["pass"])
print(json.dumps({"pass": npass, "total": len(checks), "checks": checks}, indent=1))
sys.exit(0 if npass == len(checks) else 1)
