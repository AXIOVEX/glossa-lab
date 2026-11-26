#!/usr/bin/env python3
"""Spec 105 Stage 5 execution: ladder rung L5 (the derived
meaning system: per-mark role records, role identity, and
role overlap) for the three ELSEWHERE sandboxes (spec.md
section 5; stage registered by
records/stage-5-registration-2026-11-25.md; test cases
TC-105-17, TC-105-18, TC-105-19).

A mark's role at this rung is its complete filed profile
across the ladder -- its L2 frequency position, its L3
attested successor and predecessor sets and positional
support, and its L4 substitution-class assignment --
assembled as one record per mark. Role identity is keyed
on content (count, Succ, Pred, Pos); role overlap is the
component-agreement degree over those four components.
No phonetic value, gloss, translation, or semantic
content of any kind is assigned or implied (D-105-23):
a role is a structural profile inside the sandbox only.

Run on tower-compute. Implementation A reads only the
filed Stage 2, Stage 3, and Stage 4 outputs of the same
sandbox; implementation B reads only the custody
derivation dataset's raw bytes and re-derives the
frequency, context, and class structures by its own
passes. The Indus reserve is hashed by sha256_file and
never opened or parsed (TC-105-18). Prints a JSON
summary to stdout; the summary is filed as the raw
output of record. Each sandbox is processed
independently: a failure stops that sandbox only and is
reported with its step and evidence.
"""
import hashlib, json, os, subprocess

HOME = os.path.expanduser("~")
CUSTODY = os.path.join(HOME, ".syncyard", "worktrees", "glossa",
                       "glossa-custody", "spec105")
REPO = os.path.join(HOME, ".syncyard", "worktrees", "glossa",
                    "s105-stage5-clone")
RECORDS = os.path.join(REPO, "specs", "105-elsewhere-sandbox",
                       "records")
STAGE2_OUTPUT = os.path.join(RECORDS, "stage-2-output-2026-11-25.json")
STAGE3_OUTPUT = os.path.join(RECORDS, "stage-3-output-2026-11-25.json")
STAGE4_OUTPUT = os.path.join(RECORDS, "stage-4-output-2026-11-25.json")

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

# ---------------------------------------------------------------- B
# B's stream programs (jq + awk). No code is shared with A.

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

# B counts pass: counted TOK events -> CNT lines (mark, count).
AWK_TOK = r"""
{
  line = $0
  sub(/^ +/, "", line)
  sp = index(line, " ")
  cnt = substr(line, sp + 1)
  n = split(cnt, F, "\t")
  printf "CNT\t%s\t%s\n", F[2], substr(line, 1, sp - 1)
}
"""

# B rank pass: CNT lines sorted by count descending, mark byte
# order -> RNK lines (mark, rank, count, reduced fraction).
AWK_RANK = r"""
function gcd(a, b,   t) { while (b) { t = a % b; a = b; b = t } return a }
{
  n = split($0, F, "\t")
  k++
  mk[k] = F[2]; ct[k] = F[3] + 0
  total += F[3]
}
END {
  for (i = 1; i <= k; i++) {
    g = gcd(ct[i], total)
    printf "RNK\t%s\t%s\t%s\t%d/%d\n", mk[i], i, ct[i], ct[i] / g, total / g
  }
}
"""

# B context pass 1: counted events -> distinct context events.
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

# B context pass 2: sorted context events -> one MK line per mark:
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

# B context pass 3: MK lines -> CAND lines carrying the component
# counts, so the signature (fields between the kind tag and the
# final mark field) is an injective encoding of the context.
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

# B context pass 4: sorted CAND lines -> class lines without ids,
# grouped by (kind, signature); members arrive in byte order.
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
    tsucc = ""; tpred = ""
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

# B context pass 5: assign class ids in canonical order (string
# substitution on the raw line; no field rebuild, so empty fields
# survive).
AWK_IDS = r"""
$1 == "SC" { nsc++; sub(/^SC\t/, "SC-" nsc "\t"); print; next }
$1 == "PC" { npc++; sub(/^PC\t/, "PC-" npc "\t"); print; next }
$1 == "JC" { njc++; sub(/^JC\t/, "JC-" njc "\t"); print; next }
{ print }
"""

# B assembly pass 1: id'd class lines + MK lines -> CTX lines:
# CTX, mark, successor class, predecessor class, joint class,
# joint class size, |Succ|, successors..., "", |Pred|,
# predecessors..., "", |Pos|, support...
AWK_CTX = r"""
/^MK\t/ {
  n = split($0, F, "\t")
  m = F[2]; sd = F[3] + 0; pd = F[4] + 0; sp = F[5] + 0
  succ = ""; pred = ""; sup = ""
  for (i = 1; i <= sd; i++) succ = succ (i > 1 ? "\t" : "") F[5 + i]
  off = 6 + sd
  for (i = 1; i <= pd; i++) pred = pred (i > 1 ? "\t" : "") F[off + i]
  off = off + 1 + pd
  for (i = 1; i <= sp; i++) sup = sup (i > 1 ? "\t" : "") F[off + i]
  ctx = sd
  if (succ != "") ctx = ctx "\t" succ
  ctx = ctx "\t\t" pd
  if (pred != "") ctx = ctx "\t" pred
  ctx = ctx "\t\t" sp
  if (sup != "") ctx = ctx "\t" sup
  c[m] = ctx
  marks[m] = 1
  next
}
{
  n = split($0, F, "\t")
  id = F[1]; size = F[2] + 0
  kind = substr(id, 1, 2)
  for (i = 1; i <= size; i++) {
    if (kind == "SC") sc[F[2 + i]] = id
    else if (kind == "PC") pc[F[2 + i]] = id
    else { jc[F[2 + i]] = id; jsz[F[2 + i]] = size }
  }
  next
}
END {
  for (m in marks)
    printf "CTX\t%s\t%s\t%s\t%s\t%s\t%s\n", \
      m, sc[m], pc[m], jc[m], jsz[m], c[m]
}
"""

# B assembly pass 2: RNK lines + CTX lines -> role lines:
# mark, count, fraction, rank, successor class, predecessor class,
# joint class, joint class size, |Succ|, successors..., "",
# |Pred|, predecessors..., "", |Pos|, support...
AWK_ROLE = r"""
{
  n = split($0, F, "\t")
  if (F[1] == "RNK") {
    rnk[F[2]] = F[4] "\t" F[5] "\t" F[3]
    marks[F[2]] = 1
  } else if (F[1] == "CTX") {
    suf = F[3]
    for (i = 4; i <= n; i++) suf = suf "\t" F[i]
    ctx[F[2]] = suf
    marks[F[2]] = 1
  }
}
END {
  for (m in marks) print m "\t" rnk[m] "\t" ctx[m]
}
"""

# B identity pass 1: role lines -> KEY lines: the identity key
# (count, |Succ|, successors, "", |Pred|, predecessors, "",
# |Pos|, positions) with the mark last, for sorted grouping.
AWK_KEY = r"""
{
  n = split($0, F, "\t")
  mark = F[1]; count = F[2]; sd = F[9] + 0
  succ = ""; pred = ""; pos = ""
  for (i = 1; i <= sd; i++) succ = succ (i > 1 ? "\t" : "") F[9 + i]
  pd = F[11 + sd] + 0
  for (i = 1; i <= pd; i++) pred = pred (i > 1 ? "\t" : "") F[11 + sd + i]
  sp = F[13 + sd + pd] + 0
  for (i = 1; i <= sp; i++) pos = pos (i > 1 ? "\t" : "") F[13 + sd + pd + i]
  line = "KEY\t" count "\t" sd
  if (succ != "") line = line "\t" succ
  line = line "\t\t" pd
  if (pred != "") line = line "\t" pred
  line = line "\t\t" sp
  if (pos != "") line = line "\t" pos
  print line "\t" mark
}
"""

# B identity pass 2: sorted KEY lines -> identity class lines
# without ids: RC, size, members..., "", count, fraction, |Succ|,
# successors..., "", |Pred|, predecessors..., "", |Pos|,
# positions...  TOTAL (the sandbox token total) arrives via -v.
AWK_GROUP5 = r"""
function gcd(a, b,   t) { while (b) { t = a % b; a = b; b = t } return a }
function flush(   i, line, g) {
  if (count == 0) return
  line = "RC\t" count
  for (i = 1; i <= count; i++) line = line "\t" mem[i]
  g = gcd(kcount + 0, TOTAL)
  line = line "\t\t" kcount "\t" (kcount / g) "/" (TOTAL / g) "\t" ksd
  if (ksucc != "") line = line "\t" ksucc
  line = line "\t\t" kpd
  if (kpred != "") line = line "\t" kpred
  line = line "\t\t" ksp
  if (kpos != "") line = line "\t" kpos
  print line
  count = 0
}
{
  n = split($0, F, "\t")
  mark = F[n]
  tcount = F[2]; tsd = F[3] + 0
  tsucc = ""; tpred = ""; tpos = ""
  for (i = 1; i <= tsd; i++) tsucc = tsucc (i > 1 ? "\t" : "") F[3 + i]
  tpd = F[5 + tsd] + 0
  for (i = 1; i <= tpd; i++) tpred = tpred (i > 1 ? "\t" : "") F[5 + tsd + i]
  tsp = F[7 + tsd + tpd] + 0
  for (i = 1; i <= tsp; i++) tpos = tpos (i > 1 ? "\t" : "") F[7 + tsd + tpd + i]
  sig = tcount "\t" tsd "\t" tsucc "\t" tpd "\t" tpred "\t" tsp "\t" tpos
  if (count > 0 && sig != cursig) flush()
  if (count == 0) {
    cursig = sig
    kcount = tcount; ksd = tsd; ksucc = tsucc
    kpd = tpd; kpred = tpred; ksp = tsp; kpos = tpos
  }
  count++
  mem[count] = mark
}
END { flush() }
"""

# B identity pass 3: assign RC ids in canonical order.
AWK_IDS5 = r"""
$1 == "RC" { nrc++; sub(/^RC\t/, "RC-" nrc "\t"); print; next }
{ print }
"""

# B overlap pass: role lines (byte order) -> the PAIRS line, then
# one line per mark: mark, degree counts 0..4, degree-3 members...,
# "", degree-4 members...
AWK_OVERLAP = r"""
{
  n = split($0, F, "\t")
  k++
  mk[k] = F[1]; ct[k] = F[2]
  sd = F[9] + 0
  ss = sd
  for (i = 1; i <= sd; i++) ss = ss "\t" F[9 + i]
  pd = F[11 + sd] + 0
  ps = pd
  for (i = 1; i <= pd; i++) ps = ps "\t" F[11 + sd + i]
  sp = F[13 + sd + pd] + 0
  us = sp
  for (i = 1; i <= sp; i++) us = us "\t" F[13 + sd + pd + i]
  s1[k] = ss; s2[k] = ps; s3[k] = us
}
END {
  for (i = 1; i <= k; i++)
    for (j = i + 1; j <= k; j++) {
      d = (ct[i] == ct[j]) + (s1[i] == s1[j]) + (s2[i] == s2[j]) \
          + (s3[i] == s3[j])
      dc[i, d]++; dc[j, d]++; pr[d]++
      if (d == 3) {
        d3[i] = d3[i] (d3[i] == "" ? "" : "\t") mk[j]
        d3[j] = d3[j] (d3[j] == "" ? "" : "\t") mk[i]
      } else if (d == 4) {
        d4[i] = d4[i] (d4[i] == "" ? "" : "\t") mk[j]
        d4[j] = d4[j] (d4[j] == "" ? "" : "\t") mk[i]
      }
    }
  printf "PAIRS\t%d\t%d\t%d\t%d\t%d\n", \
    pr[0] + 0, pr[1] + 0, pr[2] + 0, pr[3] + 0, pr[4] + 0
  for (i = 1; i <= k; i++) {
    line = mk[i]
    for (d = 0; d <= 4; d++) line = line "\t" (dc[i, d] + 0)
    if (d3[i] != "") line = line "\t" d3[i]
    line = line "\t"
    if (d4[i] != "") line = line "\t" d4[i]
    print line
  }
}
"""


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def role_key(role):
    return (role["count"], tuple(role["successors"]),
            tuple(role["predecessors"]), tuple(role["positions"]))


def assemble(roles):
    """S2-S3 from the per-mark role records: the identity
    partition (canonical class table) and the overlap table.
    roles is the inventory-ordered (byte order) role list.
    Returns (structured, canonical) additions."""
    inventory = [r["mark"] for r in roles]

    groups = {}
    for r in roles:
        groups.setdefault(role_key(r), []).append(r["mark"])
    classes = [(sorted(members), key)
               for key, members in groups.items()]
    classes.sort(key=lambda ck: (-len(ck[0]), ck[0]))
    freq_of_count = {r["count"]: r["frequency"] for r in roles}
    rc_rows, rc_lines = [], []
    for i, (members, key) in enumerate(classes, 1):
        cid = f"RC-{i}"
        cnt, succ, pred, pos = key
        row = {"id": cid, "size": len(members), "members": members,
               "count": cnt, "frequency": freq_of_count[cnt],
               "successors": list(succ), "predecessors": list(pred),
               "positions": list(pos)}
        rc_rows.append(row)
        rc_lines.append("\t".join(
            [cid, str(len(members))] + members
            + ["", str(cnt), row["frequency"], str(len(succ))]
            + list(succ) + ["", str(len(pred))] + list(pred)
            + ["", str(len(pos))] + list(pos)))

    deg_counts = {m: [0, 0, 0, 0, 0] for m in inventory}
    deg_members = {m: {3: [], 4: []} for m in inventory}
    pairs = [0, 0, 0, 0, 0]
    for i, a in enumerate(roles):
        ka = role_key(a)
        for b in roles[i + 1:]:
            kb = role_key(b)
            d = sum(1 for x, y in zip(ka, kb) if x == y)
            pairs[d] += 1
            deg_counts[a["mark"]][d] += 1
            deg_counts[b["mark"]][d] += 1
            if d >= 3:
                deg_members[a["mark"]][d].append(b["mark"])
                deg_members[b["mark"]][d].append(a["mark"])
    ov_rows, ov_lines = [], []
    for r in roles:
        m = r["mark"]
        row = {"mark": m, "degree_counts": deg_counts[m],
               "degree_3_members": deg_members[m][3],
               "degree_4_members": deg_members[m][4]}
        ov_rows.append(row)
        ov_lines.append("\t".join(
            [m] + [str(x) for x in deg_counts[m]]
            + deg_members[m][3] + [""] + deg_members[m][4]))
    pairs_line = "PAIRS\t" + "\t".join(str(x) for x in pairs)
    structured = {"identity_classes": rc_rows, "overlap": ov_rows,
                  "overlap_pairs": {f"degree_{d}": pairs[d]
                                    for d in range(5)}}
    canonical = {"identity_classes": rc_lines, "overlap": ov_lines,
                 "overlap_pairs": pairs_line}
    return structured, canonical


def derive_a(l2, l3, l4):
    """L5, implementation A: role records assembled from the
    filed L2 frequency table, the filed L3 pair and positional
    tables, and the filed L4 class and assignment tables of the
    same sandbox, parsed as data. Returns (canonical, totals,
    structured)."""
    filed_marks = set()
    for row in l2["table"]:
        filed_marks.add(row["mark"])
    for row in l3["positions"]:
        filed_marks.add(row["mark"])
    for p in l3["pairs"]:
        filed_marks.add(p["first"])
        filed_marks.add(p["second"])
    for row in l4["assignments"]:
        filed_marks.add(row["mark"])
    for kind in ("successor_classes", "predecessor_classes",
                 "joint_classes"):
        for c in l4[kind]:
            filed_marks.update(c["members"])
    for m in filed_marks:
        if "\t" in m or "\n" in m or "\r" in m:
            raise ValueError(
                f"mark carries a tab/newline character: {m!r}")

    rank, count, freq = {}, {}, {}
    for i, row in enumerate(l2["table"]):
        rank[row["mark"]] = i + 1
        count[row["mark"]] = row["count"]
        freq[row["mark"]] = row["frequency"]
    succ, pred, support = {}, {}, {}
    for row in l3["positions"]:
        m = row["mark"]
        succ[m] = set()
        pred[m] = set()
        support[m] = frozenset(c for c in POS_CLASSES if row[c] > 0)
    for p in l3["pairs"]:
        succ[p["first"]].add(p["second"])
        pred[p["second"]].add(p["first"])
    asg = {row["mark"]: row for row in l4["assignments"]}
    jc_size = {c["id"]: c["size"] for c in l4["joint_classes"]}

    roles, role_lines = [], []
    for m in sorted(succ):
        a = asg[m]
        role = {"mark": m, "count": count[m], "frequency": freq[m],
                "rank": rank[m],
                "successor_class": a["successor_class"],
                "predecessor_class": a["predecessor_class"],
                "joint_class": a["joint_class"],
                "joint_class_size": jc_size[a["joint_class"]],
                "successors": sorted(succ[m]),
                "predecessors": sorted(pred[m]),
                "positions": sorted(support[m])}
        roles.append(role)
        role_lines.append("\t".join(
            [m, str(role["count"]), role["frequency"],
             str(role["rank"]), role["successor_class"],
             role["predecessor_class"], role["joint_class"],
             str(role["joint_class_size"]),
             str(len(role["successors"]))] + role["successors"]
            + ["", str(len(role["predecessors"]))] + role["predecessors"]
            + ["", str(len(role["positions"]))] + role["positions"]))
    structured, canonical = assemble(roles)
    structured["roles"] = roles
    canonical["roles"] = role_lines
    totals = dict(l4["totals"])
    return canonical, totals, structured


def run(cmd, text=None, env=None):
    return subprocess.run(cmd, input=text, capture_output=True,
                          text=True, check=True, env=env)


def derive_b(path):
    """L5, implementation B (independent): totals and counts by
    jq expressions over the raw bytes; ranks by a byte-order
    sort and an awk pass; contexts and the three L4 partitions
    by a jq event stream through LC_ALL=C sort and uniq -c with
    awk assemblies; role records, identity classes, and the
    overlap table assembled by further awk passes. No code is
    shared with A."""
    def jq1(expr):
        r = run(["jq", expr, path])
        return int(r.stdout.strip())
    totals = {"artifacts": jq1("length"),
              "lines": jq1("[.[].lines | length] | add"),
              "groups": jq1("[.[].lines[] | length] | add"),
              "tokens": jq1("[.[].lines[][] | length] | add"),
              "inventory": jq1("[.[].lines[][][]] | unique | length")}
    env = {**os.environ, "LC_ALL": "C"}

    # Counts and ranks.
    toks = run(["jq", "-r", r'.[].lines[][][] | "TOK\t\(.)"', path])
    srt = run(["sort"], text=toks.stdout, env=env)
    unc = run(["uniq", "-c"], text=srt.stdout)
    cnts = run(["awk", AWK_TOK], text=unc.stdout)
    ranked = run(["sort", "-t", "\t", "-k3,3nr", "-k2,2"],
                 text=cnts.stdout, env=env)
    rnks = run(["awk", AWK_RANK], text=ranked.stdout)

    # Contexts and the three partitions (B's own passes over the
    # event stream, as at L4).
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
    class_lines = []
    for tag in ("SC", "PC", "JC"):
        ordered = final_sort(raw[tag], ["-t", "\t", "-k2,2nr", "-k3"])
        idd = run(["awk", AWK_IDS], text="\n".join(ordered) + "\n")
        class_lines.extend(l for l in idd.stdout.splitlines() if l != "")

    # Role records: join ranks and contexts per mark, byte order.
    ctxs = run(["awk", AWK_CTX],
               text="\n".join(class_lines) + "\n" + marks.stdout)
    roles = run(["awk", AWK_ROLE], text=rnks.stdout + ctxs.stdout)
    role_lines = final_sort(
        [l for l in roles.stdout.splitlines() if l != ""],
        ["-t", "\t", "-k1,1"])

    # Identity classes from the role lines.
    keys = run(["awk", AWK_KEY], text="\n".join(role_lines) + "\n")
    srt4 = run(["sort"], text=keys.stdout, env=env)
    grp = run(["awk", "-v", f"TOTAL={totals['tokens']}", AWK_GROUP5],
              text=srt4.stdout)
    rc_ordered = final_sort(
        [l for l in grp.stdout.splitlines() if l != ""],
        ["-t", "\t", "-k2,2nr", "-k3"])
    rc_idd = run(["awk", AWK_IDS5],
                 text="\n".join(rc_ordered) + "\n")
    rc_lines = [l for l in rc_idd.stdout.splitlines() if l != ""]

    # Overlap table from the role lines.
    ovs = run(["awk", AWK_OVERLAP], text="\n".join(role_lines) + "\n")
    ov_all = [l for l in ovs.stdout.splitlines() if l != ""]
    pairs_line = [l for l in ov_all if l.startswith("PAIRS\t")][0]
    ov_lines = [l for l in ov_all if not l.startswith("PAIRS\t")]

    canonical = {"roles": role_lines, "identity_classes": rc_lines,
                 "overlap": ov_lines, "overlap_pairs": pairs_line}
    return canonical, totals


def reconcile(structured, totals, l2, l3, l4):
    """S4: the reconciliation identities of the registration,
    checked against the filed L2, L3, and L4 outputs of the
    same sandbox. Returns (ok, detail)."""
    inv = totals["inventory"]
    roles = {r["mark"]: r for r in structured["roles"]}
    if set(roles) != {row["mark"] for row in l2["table"]}:
        return False, "identity (i) fails: role coverage differs " \
                      "from the filed L2 inventory"
    if sum(c["size"] for c in structured["identity_classes"]) != inv:
        return False, "identity (i) fails: identity class sizes " \
                      "do not sum to the inventory"
    if sum(r["count"] for r in roles.values()) != totals["tokens"]:
        return False, "identity (ii) fails: counts do not sum to " \
                      "the filed token total"
    induced = [r["mark"] for r in sorted(
        roles.values(), key=lambda r: (-r["count"], r["mark"]))]
    if induced != [row["mark"] for row in l2["table"]]:
        return False, "identity (ii) fails: the ordering induced " \
                      "by (count desc, mark byte order) differs from " \
                      "the filed L2 ordering"
    for row in l2["table"]:
        r = roles[row["mark"]]
        if r["count"] != row["count"] or r["frequency"] != row["frequency"]:
            return False, f"identity (ii) fails for {row['mark']!r}"
    pos = {row["mark"]: row for row in l3["positions"]}
    succ, pred = {}, {}
    for m in roles:
        succ[m] = set()
        pred[m] = set()
    for p in l3["pairs"]:
        succ[p["first"]].add(p["second"])
        pred[p["second"]].add(p["first"])
    for m, r in roles.items():
        if set(r["successors"]) != succ[m] or set(r["predecessors"]) != pred[m]:
            return False, f"identity (iii) fails for {m!r}"
        if len(r["successors"]) != pos[m]["successors_distinct"] or \
                len(r["predecessors"]) != pos[m]["predecessors_distinct"]:
            return False, f"identity (iii) distinct side fails for {m!r}"
        if set(r["positions"]) != {c for c in POS_CLASSES if pos[m][c] > 0}:
            return False, f"identity (iii) support side fails for {m!r}"
    asg = {row["mark"]: row for row in l4["assignments"]}
    jc = {c["id"]: c for c in l4["joint_classes"]}
    for m, r in roles.items():
        a = asg[m]
        if (r["successor_class"], r["predecessor_class"],
                r["joint_class"]) != (a["successor_class"],
                                      a["predecessor_class"],
                                      a["joint_class"]):
            return False, f"identity (iv) fails for {m!r}"
        c = jc[r["joint_class"]]
        if r["joint_class_size"] != c["size"]:
            return False, f"identity (iv) size side fails for {m!r}"
        if (c["successors"], c["predecessors"], c["positions"]) != \
                (r["successors"], r["predecessors"], r["positions"]):
            return False, f"identity (iv) context side fails for {m!r}"
    rc_by_mark = {}
    for c in structured["identity_classes"]:
        for m in c["members"]:
            rc_by_mark[m] = c
    for c in structured["identity_classes"]:
        if len({roles[m]["joint_class"] for m in c["members"]}) != 1:
            return False, f"identity (iv) refinement fails for {c['id']}"
    pair_sums = [0, 0, 0, 0, 0]
    for row in structured["overlap"]:
        if sum(row["degree_counts"]) != inv - 1:
            return False, f"identity (v) fails for {row['mark']!r}"
        expect4 = [m for m in rc_by_mark[row["mark"]]["members"]
                   if m != row["mark"]]
        if row["degree_4_members"] != expect4:
            return False, f"identity (v) degree-4 side fails for " \
                          f"{row['mark']!r}"
        for d in range(5):
            pair_sums[d] += row["degree_counts"][d]
    for d in range(5):
        if pair_sums[d] % 2 != 0 or \
                pair_sums[d] != 2 * structured["overlap_pairs"][f"degree_{d}"]:
            return False, f"identity (v) pair side fails at degree {d}"
    if pair_sums[4] != sum(c["size"] * (c["size"] - 1)
                           for c in structured["identity_classes"]):
        return False, "identity (v) degree-4 sum side fails"
    nrc = len(structured["identity_classes"])
    if nrc < len(l4["joint_classes"]) or nrc > inv:
        return False, "identity (vi) fails: identity class count " \
                      "out of bounds"
    return True, "identities (i)-(vi) hold exactly for every mark"


def shape(structured, totals):
    classes = structured["identity_classes"]
    return {
        "inventory_size": totals["inventory"],
        "identity_classes": len(classes),
        "largest_identity_class_size": max(c["size"] for c in classes),
        "marks_sharing_role": sum(c["size"] for c in classes
                                  if c["size"] >= 2),
        "marks_with_unique_role": sum(c["size"] for c in classes
                                      if c["size"] == 1),
        "overlap_pairs": structured["overlap_pairs"],
        "marks_with_degree_3_partner":
            sum(1 for r in structured["overlap"]
                if r["degree_counts"][3] > 0),
        "top_identity_classes": [
            {"id": c["id"], "size": c["size"], "members": c["members"],
             "count": c["count"]} for c in classes[:5]],
    }


def filed_inputs():
    s2 = json.load(open(STAGE2_OUTPUT, encoding="utf-8"))
    s3 = json.load(open(STAGE3_OUTPUT, encoding="utf-8"))
    s4 = json.load(open(STAGE4_OUTPUT, encoding="utf-8"))
    return s2["sandboxes"], s3["sandboxes"], s4["sandboxes"]


def run_sandbox(name, l2, l3, l4):
    fname = DATASETS[name]
    path = os.path.join(CUSTODY, fname)
    digest = sha256_file(path)
    if digest != EXPECTED_HASHES[fname]:
        return {"sandbox": name, "status": "STOPPED",
                "step": "dataset hash check",
                "evidence": f"{fname} hashes {digest}, "
                            f"expected {EXPECTED_HASHES[fname]}"}
    for stage, filed in (("L3", l3), ("L4", l4)):
        if filed["dataset_sha256"] != EXPECTED_HASHES[fname]:
            return {"sandbox": name, "status": "STOPPED",
                    "step": f"filed {stage} input check",
                    "evidence": f"the filed Stage {stage[-1]} output "
                                f"records dataset hash "
                                f"{filed['dataset_sha256']} for {fname}, "
                                f"expected {EXPECTED_HASHES[fname]}"}
    if l3["totals"] != l2["totals"]:
        return {"sandbox": name, "status": "STOPPED",
                "step": "filed L2/L3 input check",
                "evidence": f"L3 totals {l3['totals']} vs filed L2 "
                            f"totals {l2['totals']}"}
    l4_base = {k: l4["totals"][k]
               for k in ("artifacts", "lines", "groups", "tokens")}
    if l4_base != l3["totals"]:
        return {"sandbox": name, "status": "STOPPED",
                "step": "filed L3/L4 input check",
                "evidence": f"L4 totals {l4_base} vs filed L3 "
                            f"totals {l3['totals']}"}
    try:
        canon_a, totals_a, structured = derive_a(l2, l3, l4)
    except ValueError as e:
        return {"sandbox": name, "status": "STOPPED",
                "step": "S1 (role records)", "evidence": str(e)}
    canon_b, totals_b = derive_b(path)
    if canon_a != canon_b or totals_a != totals_b:
        detail = f"totals A={totals_a} B={totals_b}"
        for part in ("roles", "identity_classes", "overlap",
                     "overlap_pairs"):
            if canon_a[part] != canon_b[part]:
                if isinstance(canon_a[part], list):
                    detail += (f"; {part}: A lines={len(canon_a[part])} "
                               f"B lines={len(canon_b[part])}")
                    for i, (x, y) in enumerate(zip(canon_a[part],
                                                   canon_b[part])):
                        if x != y:
                            detail += (f"; first differing {part} line "
                                       f"{i}: A={x!r} B={y!r}")
                            break
                else:
                    detail += f"; {part}: A={canon_a[part]!r} " \
                              f"B={canon_b[part]!r}"
                break
        return {"sandbox": name, "status": "STOPPED",
                "step": "L5 agreement (TC-105-17)", "evidence": detail}
    ok, detail = reconcile(structured, totals_a, l2, l3, l4)
    if not ok:
        return {"sandbox": name, "status": "STOPPED",
                "step": "S4 (reconciliation)", "evidence": detail}
    result = {"sandbox": name, "status": "COMPLETED",
              "dataset": fname, "dataset_sha256": digest,
              "totals": totals_a, "implementations_agree": True,
              "reconciliation": detail,
              "shape": shape(structured, totals_a)}
    result.update(structured)
    return result


def main():
    out = {"stage": 5, "rung": "L5", "custody": CUSTODY,
           "sandboxes": {}, "checks": []}
    l2_all, l3_all, l4_all = filed_inputs()

    # TC-105-18: the reserve is hashed, never opened or parsed.
    reserve_hash = sha256_file(os.path.join(CUSTODY, RESERVE))
    out["checks"].append({
        "tc": "TC-105-18", "result":
            "PASS" if reserve_hash == EXPECTED_HASHES[RESERVE] else "FAIL",
        "reserve_sha256": reserve_hash,
        "note": "the reserve dataset was opened only by the hashing "
                "function; no Stage 5 derivation read it"})

    for name in ("indus", "eteocypriot", "meroitic"):
        out["sandboxes"][name] = run_sandbox(name, l2_all[name],
                                             l3_all[name], l4_all[name])

    agreed = [n for n, s in out["sandboxes"].items()
              if s["status"] == "COMPLETED"]
    out["checks"].append({
        "tc": "TC-105-17",
        "result": "PASS" if len(agreed) == 3 else "PARTIAL",
        "note": "both L5 implementations agree exactly, the filed "
                "L2/L3/L4 totals reproduce, and every S4 reconciliation "
                f"identity holds, in: {', '.join(agreed) if agreed else 'none'}"})

    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
