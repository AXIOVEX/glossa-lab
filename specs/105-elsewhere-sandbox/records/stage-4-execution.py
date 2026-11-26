#!/usr/bin/env python3
"""Spec 105 Stage 4 execution: ladder rung L4 (substitution
classes: marks grouped by shared recorded contexts) for the
three ELSEWHERE sandboxes (spec.md section 5; stage
registered by records/stage-4-registration-2026-11-25.md;
test cases TC-105-14, TC-105-15, TC-105-16).

Run on tower-compute. Implementation A reads only the filed
Stage 3 output of the same sandbox (the L3 pair and
positional tables) and the filed Stage 2 totals;
implementation B reads only the custody derivation
dataset's raw bytes and re-derives the contexts by its own
adjacency and occurrence pass. The Indus reserve is hashed
by sha256_file and never opened or parsed (TC-105-15).
Prints a JSON summary to stdout; the summary is filed as
the raw output of record. Each sandbox is processed
independently: a failure stops that sandbox only and is
reported with its step and evidence.
"""
import hashlib, json, os, subprocess

HOME = os.path.expanduser("~")
CUSTODY = os.path.join(HOME, ".syncyard", "worktrees", "glossa",
                       "glossa-custody", "spec105")
REPO = os.path.join(HOME, ".syncyard", "worktrees", "glossa",
                    "s105-stage4-clone")
RECORDS = os.path.join(REPO, "specs", "105-elsewhere-sandbox",
                       "records")
STAGE3_OUTPUT = os.path.join(RECORDS, "stage-3-output-2026-11-25.json")
STAGE2_OUTPUT = os.path.join(RECORDS, "stage-2-output-2026-11-25.json")

DATASETS = {  # derivation datasets only; the reserve is hashed, never read
    "indus": "indus-derivation.json",
    "eteocypriot": "eteocypriot.json",
    "meroitic": "meroitic.json",
}
RESERVE = "indus-reserve.json"
EXPECTED_HASHES = {
    "indus-derivation.json":
        "84476daa3a1d9ded33ee7c3eeaffb29fac0290ecf3507873206d4d60ac8b948b",
    "indus-reserve.json":
        "bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff",
    "eteocypriot.json":
        "2799d1034e8af50a110e7df69d6f79ab931cbc13db480ebbc8d4dfcf589421fe",
    "meroitic.json":
        "a8f551e5cc5264decbc2c01d7ee924740245ce8cbeca6b4b7f776e88a3920fb7",
}
POS_CLASSES = ("sole", "initial", "final", "medial")

JQ_EVENTS = r"""
.[] as $art
| ($art.lines[] as $line
   | ($line[] as $g
      | (range(0; ($g | length)) as $i
         | "OCC\t\($g[$i])\t\(if ($g | length) == 1 then "sole"
                              elif $i == 0 then "initial"
                              elif $i == (($g | length) - 1) then "final"
                              else "medial" end)"),
        (range(0; (($g | length) - 1)) as $i
         | "PAIR\t\($g[$i])\t\($g[$i + 1])")
     )
  )
"""

# B pass 1: counted events -> distinct context events.
AWK_EVENTS = r"""
{
  line = $0
  sub(/^ +/, "", line)
  sp = index(line, " ")
  rest = substr(line, sp + 1)
  n = split(rest, F, "\t")
  if (F[1] == "PAIR") {
    printf "SUC\t%s\t%s\n", F[2], F[3]
    printf "PRE\t%s\t%s\n", F[3], F[2]
  } else if (F[1] == "OCC") {
    printf "SUP\t%s\t%s\n", F[2], F[3]
  }
}
"""

# B pass 2: sorted context events -> one MK line per mark:
# MK, mark, |Succ|, |Pred|, |Pos|, successors..., "", predecessors...,
# "", support... (components in byte order from the sorted stream).
AWK_MARKS = r"""
{
  if ($1 == "SUC") { succ[$2] = succ[$2] $3 "\t"; sd[$2]++ }
  else if ($1 == "PRE") { pred[$2] = pred[$2] $3 "\t"; pd[$2]++ }
  else if ($1 == "SUP") { sup[$2] = sup[$2] $3 "\t"; sp[$2]++ }
  marks[$2] = 1
}
END {
  for (m in marks) {
    line = "MK\t" m "\t" (sd[m] + 0) "\t" (pd[m] + 0) "\t" (sp[m] + 0)
    s = succ[m]; sub(/\t$/, "", s)
    p = pred[m]; sub(/\t$/, "", p)
    u = sup[m]; sub(/\t$/, "", u)
    if (s != "") line = line "\t" s
    line = line "\t"
    if (p != "") line = line "\t" p
    line = line "\t"
    if (u != "") line = line "\t" u
    print line
  }
}
"""

# B pass 3: MK lines -> CAND lines carrying the component counts, so
# the signature (fields between the kind tag and the final mark
# field) is an injective encoding of the context.
AWK_CAND = r"""
{
  n = split($0, F, "\t")
  mark = F[2]; sd = F[3] + 0; pd = F[4] + 0; sp = F[5] + 0
  succ = ""; pred = ""; sup = ""
  for (i = 1; i <= sd; i++) succ = succ (i > 1 ? "\t" : "") F[5 + i]
  off = 6 + sd
  for (i = 1; i <= pd; i++) pred = pred (i > 1 ? "\t" : "") F[off + i]
  off = off + 1 + pd
  for (i = 1; i <= sp; i++) sup = sup (i > 1 ? "\t" : "") F[off + i]
  sline = "S\t" sd
  if (succ != "") sline = sline "\t" succ
  print sline "\t" mark
  pline = "P\t" pd
  if (pred != "") pline = pline "\t" pred
  print pline "\t" mark
  jline = "J\t" sd "\t" pd "\t" sp
  if (succ != "") jline = jline "\t" succ
  if (pred != "") jline = jline "\t" pred
  if (sup != "") jline = jline "\t" sup
  print jline "\t" mark
}
"""

# B pass 4: sorted CAND lines -> class lines without ids, grouped by
# (kind, signature); members arrive in byte order. The parsed context
# is held in t* variables and only becomes the current group's c*
# context after any flush of the previous group.
AWK_GROUP = r"""
function flush(   i, line) {
  if (count == 0) return
  if (kind == "S") {
    line = "SC\t" count
    for (i = 1; i <= count; i++) line = line "\t" mem[i]
    line = line "\t"
    if (csucc != "") line = line "\t" csucc
  } else if (kind == "P") {
    line = "PC\t" count
    for (i = 1; i <= count; i++) line = line "\t" mem[i]
    line = line "\t"
    if (cpred != "") line = line "\t" cpred
  } else {
    line = "JC\t" count
    for (i = 1; i <= count; i++) line = line "\t" mem[i]
    line = line "\t"
    if (csucc != "") line = line "\t" csucc
    line = line "\t"
    if (cpred != "") line = line "\t" cpred
    line = line "\t"
    if (csup != "") line = line "\t" csup
  }
  print line
  count = 0
}
{
  n = split($0, F, "\t")
  k = F[1]; mark = F[n]
  if (k == "S") {
    sd = F[2] + 0; tsucc = ""
    for (i = 1; i <= sd; i++) tsucc = tsucc (i > 1 ? "\t" : "") F[2 + i]
    sig = "S\t" F[2] "\t" tsucc
    tpred = ""; tsup = ""
  } else if (k == "P") {
    pd = F[2] + 0; tpred = ""
    for (i = 1; i <= pd; i++) tpred = tpred (i > 1 ? "\t" : "") F[2 + i]
    sig = "P\t" F[2] "\t" tpred
    tsucc = ""; tsup = ""
  } else {
    sd = F[2] + 0; pd = F[3] + 0; sp = F[4] + 0
    tsucc = ""; tpred = ""; tsup = ""
    for (i = 1; i <= sd; i++) tsucc = tsucc (i > 1 ? "\t" : "") F[4 + i]
    off = 4 + sd
    for (i = 1; i <= pd; i++) tpred = tpred (i > 1 ? "\t" : "") F[off + i]
    off = off + pd
    for (i = 1; i <= sp; i++) tsup = tsup (i > 1 ? "\t" : "") F[off + i]
    sig = "J\t" F[2] "\t" F[3] "\t" F[4] "\t" tsucc "\t" tpred "\t" tsup
  }
  if (count > 0 && sig != cursig) flush()
  if (count == 0) {
    kind = k; cursig = sig
    csucc = tsucc; cpred = tpred; csup = tsup
  }
  count++
  mem[count] = mark
}
END { flush() }
"""

# B pass 5: assign class ids in canonical order (string substitution
# on the raw line; no field rebuild, so empty fields survive).
AWK_IDS = r"""
$1 == "SC" { nsc++; sub(/^SC\t/, "SC-" nsc "\t"); print; next }
$1 == "PC" { npc++; sub(/^PC\t/, "PC-" npc "\t"); print; next }
$1 == "JC" { njc++; sub(/^JC\t/, "JC-" njc "\t"); print; next }
{ print }
"""

# B pass 6: class tables + MK lines -> the assignment table.
AWK_ASSIGN = r"""
/^MK\t/ {
  n = split($0, F, "\t")
  sd[F[2]] = F[3]; pd[F[2]] = F[4]; sp[F[2]] = F[5]
  marks[F[2]] = 1
  next
}
{
  n = split($0, F, "\t")
  id = F[1]; size = F[2] + 0
  kind = substr(id, 1, 2)
  for (i = 1; i <= size; i++) {
    if (kind == "SC") sc[F[2 + i]] = id
    else if (kind == "PC") pc[F[2 + i]] = id
    else jc[F[2 + i]] = id
  }
  next
}
END {
  for (m in marks)
    printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\n", \
      m, sc[m], pc[m], jc[m], sd[m], pd[m], sp[m]
}
"""


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build_tables(succ, pred, support):
    """S2-S4 from per-mark contexts: the three partitions, the
    canonical class tables with ids, and the assignment table.
    Returns (structured, canonical)."""
    inventory = sorted(support)

    def partition(keyfn):
        groups = {}
        for m in inventory:
            groups.setdefault(keyfn(m), []).append(m)
        classes = [(sorted(members), key)
                   for key, members in groups.items()]
        classes.sort(key=lambda ck: (-len(ck[0]), ck[0]))
        return classes

    sc_classes = partition(lambda m: tuple(sorted(succ[m])))
    pc_classes = partition(lambda m: tuple(sorted(pred[m])))
    jc_classes = partition(lambda m: (tuple(sorted(succ[m])),
                                      tuple(sorted(pred[m])),
                                      tuple(sorted(support[m]))))

    def emit(classes, prefix, kind):
        rows, lines, assign = [], [], {}
        for i, (members, key) in enumerate(classes, 1):
            cid = f"{prefix}-{i}"
            for m in members:
                assign[m] = cid
            row = {"id": cid, "size": len(members), "members": members}
            if kind == "SC":
                row["successors"] = list(key)
                lines.append("\t".join([cid, str(len(members))]
                                       + members + [""] + list(key)))
            elif kind == "PC":
                row["predecessors"] = list(key)
                lines.append("\t".join([cid, str(len(members))]
                                       + members + [""] + list(key)))
            else:
                row["successors"] = list(key[0])
                row["predecessors"] = list(key[1])
                row["positions"] = list(key[2])
                lines.append("\t".join([cid, str(len(members))]
                                       + members + [""] + list(key[0])
                                       + [""] + list(key[1])
                                       + [""] + list(key[2])))
            rows.append(row)
        return rows, lines, assign

    sc_rows, sc_lines, sc_assign = emit(sc_classes, "SC", "SC")
    pc_rows, pc_lines, pc_assign = emit(pc_classes, "PC", "PC")
    jc_rows, jc_lines, jc_assign = emit(jc_classes, "JC", "JC")

    asg_rows, asg_lines = [], []
    for m in inventory:
        row = {"mark": m, "successor_class": sc_assign[m],
               "predecessor_class": pc_assign[m],
               "joint_class": jc_assign[m],
               "successors_distinct": len(succ[m]),
               "predecessors_distinct": len(pred[m]),
               "positions_support": len(support[m])}
        asg_rows.append(row)
        asg_lines.append(
            f"{m}\t{sc_assign[m]}\t{pc_assign[m]}\t{jc_assign[m]}\t"
            f"{len(succ[m])}\t{len(pred[m])}\t{len(support[m])}")
    structured = {"successor_classes": sc_rows,
                  "predecessor_classes": pc_rows,
                  "joint_classes": jc_rows,
                  "assignments": asg_rows}
    canonical = {"successor_classes": sc_lines,
                 "predecessor_classes": pc_lines,
                 "joint_classes": jc_lines,
                 "assignments": asg_lines}
    return structured, canonical


def derive_a(l3):
    """L4, implementation A: contexts read from the filed L3
    tables (the attested pair table and the per-mark positional
    table of the same sandbox, parsed as data). Returns
    (canonical, totals, structured)."""
    succ, pred, support = {}, {}, {}
    for row in l3["positions"]:
        m = row["mark"]
        if "\t" in m or "\n" in m or "\r" in m:
            raise ValueError(
                f"mark carries a tab/newline character: {m!r}")
        succ[m] = set()
        pred[m] = set()
        support[m] = frozenset(c for c in POS_CLASSES if row[c] > 0)
    for p in l3["pairs"]:
        succ[p["first"]].add(p["second"])
        pred[p["second"]].add(p["first"])
    structured, canonical = build_tables(succ, pred, support)
    totals = dict(l3["totals"])
    totals["inventory"] = len(l3["positions"])
    return canonical, totals, structured


def run(cmd, text=None, env=None):
    return subprocess.run(cmd, input=text, capture_output=True,
                          text=True, check=True, env=env)


def derive_b(path):
    """L4, implementation B (independent): structural totals by
    jq expressions over the raw bytes; the contexts by a jq
    event stream through LC_ALL=C sort and uniq -c, assembled
    by awk programs into the canonical tables, canonically
    ordered by final sorts. No code is shared with A."""
    def jq1(expr):
        r = run(["jq", expr, path])
        return int(r.stdout.strip())
    totals = {"artifacts": jq1("length"),
              "lines": jq1("[.[].lines | length] | add"),
              "groups": jq1("[.[].lines[] | length] | add"),
              "tokens": jq1("[.[].lines[][] | length] | add"),
              "inventory": jq1("[.[].lines[][][]] | unique | length")}
    env = {**os.environ, "LC_ALL": "C"}
    stream = run(["jq", "-r", JQ_EVENTS, path])
    srt = run(["sort"], text=stream.stdout, env=env)
    unc = run(["uniq", "-c"], text=srt.stdout)
    events = run(["awk", AWK_EVENTS], text=unc.stdout)
    srt2 = run(["sort"], text=events.stdout, env=env)
    marks = run(["awk", AWK_MARKS], text=srt2.stdout)
    cand = run(["awk", AWK_CAND], text=marks.stdout)
    srt3 = run(["sort"], text=cand.stdout, env=env)
    grouped = run(["awk", AWK_GROUP], text=srt3.stdout)

    def final_sort(lines, args):
        if not lines:
            return []
        r = run(["sort"] + args, text="\n".join(lines) + "\n", env=env)
        return [l for l in r.stdout.splitlines() if l != ""]
    raw = {"SC": [], "PC": [], "JC": []}
    for line in grouped.stdout.splitlines():
        if line:
            raw[line.split("\t", 1)[0]].append(line)
    canonical = {}
    assign_input = []
    for tag, key in (("SC", "successor_classes"),
                     ("PC", "predecessor_classes"),
                     ("JC", "joint_classes")):
        ordered = final_sort(raw[tag], ["-t", "\t", "-k2,2nr", "-k3"])
        idd = run(["awk", AWK_IDS], text="\n".join(ordered) + "\n")
        lines = [l for l in idd.stdout.splitlines() if l != ""]
        canonical[key] = lines
        assign_input.extend(lines)
    asg = run(["awk", AWK_ASSIGN],
              text="\n".join(assign_input) + "\n" + marks.stdout)
    canonical["assignments"] = final_sort(
        [l for l in asg.stdout.splitlines() if l != ""],
        ["-t", "\t", "-k1,1"])
    return canonical, totals


def reconcile(structured, totals, l3):
    """S5: the reconciliation identities of the registration,
    checked against the filed L3 tables of the same sandbox.
    Returns (ok, detail)."""
    pos = {row["mark"]: row for row in l3["positions"]}
    inv = totals["inventory"]
    if set(pos) != {r["mark"] for r in structured["assignments"]}:
        return False, "identity (ii) fails: assignment coverage " \
                      "differs from the L3 inventory"
    for kind in ("successor_classes", "predecessor_classes",
                 "joint_classes"):
        if sum(c["size"] for c in structured[kind]) != inv:
            return False, f"identity (i) fails for {kind}"
    asg = {r["mark"]: r for r in structured["assignments"]}
    jc_by_id = {c["id"]: c for c in structured["joint_classes"]}
    for c in structured["joint_classes"]:
        sc_ids = {asg[m]["successor_class"] for m in c["members"]}
        pc_ids = {asg[m]["predecessor_class"] for m in c["members"]}
        if len(sc_ids) != 1 or len(pc_ids) != 1:
            return False, f"identity (iii) fails for {c['id']}"
    positive_cells = 0
    for m, row in pos.items():
        a = asg[m]
        if a["successors_distinct"] != row["successors_distinct"]:
            return False, f"identity (iv) successor side fails for {m!r}"
        if a["predecessors_distinct"] != row["predecessors_distinct"]:
            return False, f"identity (iv) predecessor side fails for {m!r}"
        support = set(jc_by_id[a["joint_class"]]["positions"])
        filed = {c for c in POS_CLASSES if row[c] > 0}
        if support != filed:
            return False, f"identity (v) fails for {m!r}"
        positive_cells += len(filed)
    if sum(r["positions_support"] for r in asg.values()) != positive_cells:
        return False, "identity (v) support-sum side fails"
    njc = len(structured["joint_classes"])
    if njc < max(len(structured["successor_classes"]),
                 len(structured["predecessor_classes"])) or njc > inv:
        return False, "identity (vi) fails: joint class count out of bounds"
    return True, "identities (i)-(vi) hold exactly for every mark"


def shape(structured, totals):
    def kind_shape(classes):
        return {"classes": len(classes),
                "largest_class_size": max(c["size"] for c in classes),
                "singleton_classes":
                    sum(1 for c in classes if c["size"] == 1)}
    empty_succ = [c for c in structured["successor_classes"]
                  if not c["successors"]]
    empty_pred = [c for c in structured["predecessor_classes"]
                  if not c["predecessors"]]
    return {
        "inventory_size": totals["inventory"],
        "successor_classes": kind_shape(structured["successor_classes"]),
        "predecessor_classes": kind_shape(
            structured["predecessor_classes"]),
        "joint_classes": kind_shape(structured["joint_classes"]),
        "marks_with_substitute": sum(
            c["size"] for c in structured["joint_classes"]
            if c["size"] >= 2),
        "marks_without_substitute": sum(
            c["size"] for c in structured["joint_classes"]
            if c["size"] == 1),
        "empty_successor_class_size":
            empty_succ[0]["size"] if empty_succ else 0,
        "empty_predecessor_class_size":
            empty_pred[0]["size"] if empty_pred else 0,
        "top_joint_classes": [
            {"id": c["id"], "size": c["size"], "members": c["members"],
             "successors": len(c["successors"]),
             "predecessors": len(c["predecessors"]),
             "positions": c["positions"]}
            for c in structured["joint_classes"][:5]],
    }


def filed_inputs():
    s3 = json.load(open(STAGE3_OUTPUT, encoding="utf-8"))
    s2 = json.load(open(STAGE2_OUTPUT, encoding="utf-8"))
    return s3["sandboxes"], s2["sandboxes"]


def run_sandbox(name, l3, l2):
    fname = DATASETS[name]
    path = os.path.join(CUSTODY, fname)
    digest = sha256_file(path)
    if digest != EXPECTED_HASHES[fname]:
        return {"sandbox": name, "status": "STOPPED",
                "step": "dataset hash check",
                "evidence": f"{fname} hashes {digest}, "
                            f"expected {EXPECTED_HASHES[fname]}"}
    if l3["dataset_sha256"] != EXPECTED_HASHES[fname]:
        return {"sandbox": name, "status": "STOPPED",
                "step": "filed L3 input check",
                "evidence": "the filed Stage 3 output records dataset "
                            f"hash {l3['dataset_sha256']} for {fname}, "
                            f"expected {EXPECTED_HASHES[fname]}"}
    if l3["totals"] != l2["totals"]:
        return {"sandbox": name, "status": "STOPPED",
                "step": "filed L2/L3 input check",
                "evidence": f"L3 totals {l3['totals']} vs filed L2 "
                            f"totals {l2['totals']}"}
    try:
        canon_a, totals_a, structured = derive_a(l3)
    except ValueError as e:
        return {"sandbox": name, "status": "STOPPED",
                "step": "S1 (contexts)", "evidence": str(e)}
    canon_b, totals_b = derive_b(path)
    if canon_a != canon_b or totals_a != totals_b:
        detail = f"totals A={totals_a} B={totals_b}"
        for part in ("successor_classes", "predecessor_classes",
                     "joint_classes", "assignments"):
            if canon_a[part] != canon_b[part]:
                detail += (f"; {part}: A lines={len(canon_a[part])} "
                           f"B lines={len(canon_b[part])}")
                for i, (x, y) in enumerate(zip(canon_a[part],
                                               canon_b[part])):
                    if x != y:
                        detail += (f"; first differing {part} line {i}: "
                                   f"A={x!r} B={y!r}")
                        break
                break
        return {"sandbox": name, "status": "STOPPED",
                "step": "L4 agreement (TC-105-14)", "evidence": detail}
    ok, detail = reconcile(structured, totals_a, l3)
    if not ok:
        return {"sandbox": name, "status": "STOPPED",
                "step": "S5 (reconciliation)", "evidence": detail}
    result = {"sandbox": name, "status": "COMPLETED",
              "dataset": fname, "dataset_sha256": digest,
              "totals": totals_a, "implementations_agree": True,
              "reconciliation": detail,
              "shape": shape(structured, totals_a)}
    result.update(structured)
    return result


def main():
    out = {"stage": 4, "rung": "L4", "custody": CUSTODY,
           "sandboxes": {}, "checks": []}
    l3_all, l2_all = filed_inputs()

    # TC-105-15: the reserve is hashed, never opened or parsed.
    reserve_hash = sha256_file(os.path.join(CUSTODY, RESERVE))
    out["checks"].append({
        "tc": "TC-105-15", "result":
            "PASS" if reserve_hash == EXPECTED_HASHES[RESERVE] else "FAIL",
        "reserve_sha256": reserve_hash,
        "note": "the reserve dataset was opened only by the hashing "
                "function; no Stage 4 derivation read it"})

    for name in ("indus", "eteocypriot", "meroitic"):
        out["sandboxes"][name] = run_sandbox(name, l3_all[name],
                                             l2_all[name])

    agreed = [n for n, s in out["sandboxes"].items()
              if s["status"] == "COMPLETED"]
    out["checks"].append({
        "tc": "TC-105-14",
        "result": "PASS" if len(agreed) == 3 else "PARTIAL",
        "note": "both L4 implementations agree exactly, the filed "
                "L2/L3 totals reproduce, and every S5 reconciliation "
                f"identity holds, in: {', '.join(agreed) if agreed else 'none'}"})

    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
