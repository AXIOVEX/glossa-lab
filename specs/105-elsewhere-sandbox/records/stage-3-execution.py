#!/usr/bin/env python3
"""Spec 105 Stage 3 execution: ladder rung L3 (order structure:
attested adjacency and positional structure) for the three
ELSEWHERE sandboxes (spec.md section 5; stage registered by
records/stage-3-registration-2026-11-25.md; test cases
TC-105-11, TC-105-12, TC-105-13).

Run on tower-compute. Reads only the custody derivation
datasets and the filed Stage 2 output of the same study (the
lower-rung output L3 reconciles against); the Indus reserve
is hashed by sha256_file and never opened or parsed
(TC-105-12). Prints a JSON summary to stdout; the summary is
filed as the raw output of record. Each sandbox is processed
independently: a failure stops that sandbox only and is
reported with its step and evidence.
"""
import hashlib, json, os, subprocess

HOME = os.path.expanduser("~")
CUSTODY = os.path.join(HOME, ".syncyard", "worktrees", "glossa",
                       "glossa-custody", "spec105")
REPO = os.path.join(HOME, ".syncyard", "worktrees", "glossa",
                    "s105-stage3-clone")
STAGE2_OUTPUT = os.path.join(
    REPO, "specs", "105-elsewhere-sandbox", "records",
    "stage-2-output-2026-11-25.json")

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

JQ_EVENTS = r"""
.[] as $art
| "AINIT\t\($art.lines[0][0][0])", "AFIN\t\($art.lines[-1][-1][-1])",
  ($art.lines[] as $line
   | "LINIT\t\($line[0][0])", "LFIN\t\($line[-1][-1])",
     "LLEN\t\($line | map(length) | add)",
     ($line[] as $g
      | "GLEN\t\($g | length)",
        (range(0; ($g | length)) as $i
         | "OCC\t\($g[$i])\t\(if ($g | length) == 1 then "sole"
                              elif $i == 0 then "initial"
                              elif $i == (($g | length) - 1) then "final"
                              else "medial" end)"),
        (range(0; (($g | length) - 1)) as $i
         | "PAIR\t\($g[$i])\t\($g[$i + 1])")
     )
  )
"""

AWK_ASSEMBLE = r"""
function emit(   m) {
  for (m in cnt) {
    printf "POS\t%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n", \
      m, cnt[m], sole[m]+0, init[m]+0, fin[m]+0, med[m]+0, \
      li[m]+0, lf[m]+0, ai[m]+0, af[m]+0, \
      sd[m]+0, st[m]+0, pd[m]+0, pt[m]+0
  }
  for (m in pairc) printf "PAIR\t%s\t%d\n", m, pairc[m]
  for (m in glen) printf "GLEN\t%s\t%d\n", m, glen[m]
  for (m in llen) printf "LLEN\t%s\t%d\n", m, llen[m]
}
{
  line = $0
  sub(/^ +/, "", line)
  sp = index(line, " ")
  c = substr(line, 1, sp - 1) + 0
  rest = substr(line, sp + 1)
  n = split(rest, F, "\t")
  if (F[1] == "PAIR") {
    key = F[2] "\t" F[3]
    pairc[key] += c
    st[F[2]] += c; sd[F[2]]++
    pt[F[3]] += c; pd[F[3]]++
  } else if (F[1] == "OCC") {
    cnt[F[2]] += c
    if (F[3] == "sole") sole[F[2]] += c
    else if (F[3] == "initial") init[F[2]] += c
    else if (F[3] == "final") fin[F[2]] += c
    else med[F[2]] += c
  } else if (F[1] == "LINIT") li[F[2]] += c
  else if (F[1] == "LFIN") lf[F[2]] += c
  else if (F[1] == "AINIT") ai[F[2]] += c
  else if (F[1] == "AFIN") af[F[2]] += c
  else if (F[1] == "GLEN") glen[F[2]] += c
  else if (F[1] == "LLEN") llen[F[2]] += c
}
END { emit() }
"""


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def derive_a(path):
    """L3, implementation A: parse the dataset JSON and derive
    the order structure directly. Returns (canonical, totals,
    structured): canonical holds the three canonical text-line
    lists (pairs, positions, lengths); structured holds the
    same content as data for the outcome record and shape."""
    data = json.load(open(path, encoding="utf-8"))
    pair_counts = {}
    pos = {}
    glen = {}
    llen = {}
    n_lines = 0
    n_groups = 0
    n_tokens = 0

    def rec(m):
        return pos.setdefault(m, {"sole": 0, "initial": 0, "final": 0,
                                  "medial": 0, "line_initial": 0,
                                  "line_final": 0, "artifact_initial": 0,
                                  "artifact_final": 0})

    for art in data:
        lines = art["lines"]
        if not lines or any(not line for line in lines):
            raise ValueError("empty line in artifact")
        for line in lines:
            if any(not g for g in line):
                raise ValueError("empty group in line")
        flat_first = lines[0][0][0]
        flat_last = lines[-1][-1][-1]
        rec(flat_first)["artifact_initial"] += 1
        rec(flat_last)["artifact_final"] += 1
        n_lines += len(lines)
        for line in lines:
            rec(line[0][0])["line_initial"] += 1
            rec(line[-1][-1])["line_final"] += 1
            llen_line = 0
            for group in line:
                n_groups += 1
                n_tokens += len(group)
                llen_line += len(group)
                glen[len(group)] = glen.get(len(group), 0) + 1
                for i, m in enumerate(group):
                    if "\t" in m or "\n" in m or "\r" in m:
                        raise ValueError(
                            f"mark carries a tab/newline character: {m!r}")
                    r = rec(m)
                    if len(group) == 1:
                        r["sole"] += 1
                    elif i == 0:
                        r["initial"] += 1
                    elif i == len(group) - 1:
                        r["final"] += 1
                    else:
                        r["medial"] += 1
                    if i + 1 < len(group):
                        key = (m, group[i + 1])
                        pair_counts[key] = pair_counts.get(key, 0) + 1
            llen[llen_line] = llen.get(llen_line, 0) + 1
    totals = {"artifacts": len(data), "lines": n_lines,
              "groups": n_groups, "tokens": n_tokens}
    succ = {}
    pred = {}
    for (a, b), c in pair_counts.items():
        s = succ.setdefault(a, [0, 0]); s[0] += 1; s[1] += c
        p = pred.setdefault(b, [0, 0]); p[0] += 1; p[1] += c
    pair_rows = sorted(pair_counts.items(),
                       key=lambda kv: (-kv[1], kv[0][0], kv[0][1]))
    pair_lines = [f"{a}\t{b}\t{c}" for (a, b), c in pair_rows]
    pos_lines = []
    pos_rows = []
    for m in sorted(pos):
        r = pos[m]
        cnt = r["sole"] + r["initial"] + r["final"] + r["medial"]
        sd, st = succ.get(m, [0, 0])
        pd, pt = pred.get(m, [0, 0])
        row = {"mark": m, "count": cnt, "sole": r["sole"],
               "initial": r["initial"], "final": r["final"],
               "medial": r["medial"], "line_initial": r["line_initial"],
               "line_final": r["line_final"],
               "artifact_initial": r["artifact_initial"],
               "artifact_final": r["artifact_final"],
               "successors_distinct": sd, "successors_total": st,
               "predecessors_distinct": pd, "predecessors_total": pt}
        pos_rows.append(row)
        pos_lines.append(
            f"{m}\t{cnt}\t{r['sole']}\t{r['initial']}\t{r['final']}\t"
            f"{r['medial']}\t{r['line_initial']}\t{r['line_final']}\t"
            f"{r['artifact_initial']}\t{r['artifact_final']}\t"
            f"{sd}\t{st}\t{pd}\t{pt}")
    len_lines = ([f"G\t{k}\t{glen[k]}" for k in sorted(glen)] +
                 [f"L\t{k}\t{llen[k]}" for k in sorted(llen)])
    structured = {
        "pairs": [{"first": a, "second": b, "count": c}
                  for (a, b), c in pair_rows],
        "positions": pos_rows,
        "group_lengths": [{"length": k, "groups": glen[k]}
                          for k in sorted(glen)],
        "line_lengths": [{"length": k, "lines": llen[k]}
                         for k in sorted(llen)],
    }
    canonical = {"pairs": pair_lines, "positions": pos_lines,
                 "lengths": len_lines}
    return canonical, totals, structured


def derive_b(path):
    """L3, implementation B (independent): structural totals by
    jq expressions over the raw bytes; the order structure by a
    jq event stream through LC_ALL=C sort and uniq -c, assembled
    by an awk program into the canonical tables, canonically
    ordered by final sorts. No code is shared with A."""
    def jq1(expr):
        r = subprocess.run(["jq", expr, path], capture_output=True,
                           text=True, check=True)
        return int(r.stdout.strip())
    totals = {"artifacts": jq1("length"),
              "lines": jq1("[.[].lines | length] | add"),
              "groups": jq1("[.[].lines[] | length] | add"),
              "tokens": jq1("[.[].lines[][] | length] | add")}
    env = {**os.environ, "LC_ALL": "C"}
    stream = subprocess.run(["jq", "-r", JQ_EVENTS, path],
                            capture_output=True, text=True, check=True)
    srt = subprocess.run(["sort"], input=stream.stdout,
                         capture_output=True, text=True, check=True,
                         env=env)
    unc = subprocess.run(["uniq", "-c"], input=srt.stdout,
                         capture_output=True, text=True, check=True)
    awk = subprocess.run(["awk", AWK_ASSEMBLE], input=unc.stdout,
                         capture_output=True, text=True, check=True)
    pair_lines, pos_lines, len_lines = [], [], []
    for line in awk.stdout.splitlines():
        if not line:
            continue
        f = line.split("\t")
        if f[0] == "PAIR":
            pair_lines.append("\t".join(f[1:]))
        elif f[0] == "POS":
            pos_lines.append("\t".join(f[1:]))
        elif f[0] in ("GLEN", "LLEN"):
            len_lines.append(("G" if f[0] == "GLEN" else "L")
                             + "\t" + f[1] + "\t" + f[2])

    def final_sort(lines, args):
        r = subprocess.run(["sort"] + args, input="\n".join(lines) + "\n",
                           capture_output=True, text=True, check=True,
                           env=env)
        return [l for l in r.stdout.splitlines() if l]
    pair_lines = final_sort(pair_lines,
                            ["-t", "\t", "-k3,3nr", "-k1,1", "-k2,2"])
    pos_lines = final_sort(pos_lines, ["-t", "\t", "-k1,1"])
    len_g = final_sort([l for l in len_lines if l.startswith("G\t")],
                       ["-t", "\t", "-k2,2n"])
    len_l = final_sort([l for l in len_lines if l.startswith("L\t")],
                       ["-t", "\t", "-k2,2n"])
    canonical = {"pairs": pair_lines, "positions": pos_lines,
                 "lengths": len_g + len_l}
    return canonical, totals


def reconcile(structured, totals, l2):
    """T5: the reconciliation identities of the registration,
    checked against the filed L2 table of the same sandbox.
    Returns (ok, detail)."""
    l2_counts = {row["mark"]: row["count"] for row in l2["table"]}
    if totals != l2["totals"]:
        return False, f"totals {totals} vs filed L2 {l2['totals']}"
    marks = {row["mark"]: row for row in structured["positions"]}
    if set(marks) != set(l2_counts):
        return False, "position table mark set differs from the L2 table"
    for m, row in marks.items():
        if row["count"] != l2_counts[m]:
            return False, (f"identity (i) fails for {m!r}: classes sum "
                           f"{row['count']} vs L2 count {l2_counts[m]}")
        if row["successors_total"] != l2_counts[m] - row["final"] - row["sole"]:
            return False, f"identity (ii) successor side fails for {m!r}"
        if row["predecessors_total"] != l2_counts[m] - row["initial"] - row["sole"]:
            return False, f"identity (ii) predecessor side fails for {m!r}"
    pair_total = sum(p["count"] for p in structured["pairs"])
    if pair_total != totals["tokens"] - totals["groups"]:
        return False, (f"identity (iii) fails: pair total {pair_total} vs "
                       f"tokens-groups {totals['tokens'] - totals['groups']}")
    if sum(r["line_initial"] for r in marks.values()) != totals["lines"]:
        return False, "identity (iv) line-initial side fails"
    if sum(r["line_final"] for r in marks.values()) != totals["lines"]:
        return False, "identity (iv) line-final side fails"
    if sum(r["artifact_initial"] for r in marks.values()) != totals["artifacts"]:
        return False, "identity (iv) artifact-initial side fails"
    if sum(r["artifact_final"] for r in marks.values()) != totals["artifacts"]:
        return False, "identity (iv) artifact-final side fails"
    gl = structured["group_lengths"]
    if sum(g["groups"] for g in gl) != totals["groups"] or \
            sum(g["length"] * g["groups"] for g in gl) != totals["tokens"]:
        return False, "identity (v) group-length side fails"
    ll = structured["line_lengths"]
    if sum(x["lines"] for x in ll) != totals["lines"] or \
            sum(x["length"] * x["lines"] for x in ll) != totals["tokens"]:
        return False, "identity (v) line-length side fails"
    return True, "identities (i)-(v) hold exactly for every mark"


def shape(structured, totals):
    pairs = structured["pairs"]
    pos = structured["positions"]
    inv = len(pos)
    return {
        "inventory_size": inv,
        "distinct_attested_pairs": len(pairs),
        "possible_ordered_pairs": inv * inv,
        "pairs_attested_once": sum(1 for p in pairs if p["count"] == 1),
        "pairs_recurring": sum(1 for p in pairs if p["count"] >= 2),
        "self_pair_tokens": sum(p["count"] for p in pairs
                                if p["first"] == p["second"]),
        "marks_no_successor": sum(1 for r in pos
                                  if r["successors_total"] == 0),
        "marks_no_predecessor": sum(1 for r in pos
                                    if r["predecessors_total"] == 0),
        "marks_no_neighbour": sum(1 for r in pos
                                  if r["successors_total"] == 0
                                  and r["predecessors_total"] == 0),
        "marks_both_neighbours": sum(1 for r in pos
                                     if r["successors_total"] > 0
                                     and r["predecessors_total"] > 0),
        "top_pairs": pairs[:10],
    }


def stage2_expectations():
    """The filed L2 totals and per-mark counts, read from the
    study's own Stage 2 raw output (a lower-rung output and the
    T5 check source, never an L3 derivation input)."""
    s2 = json.load(open(STAGE2_OUTPUT, encoding="utf-8"))
    return s2["sandboxes"]


def run_sandbox(name, l2):
    fname = DATASETS[name]
    path = os.path.join(CUSTODY, fname)
    digest = sha256_file(path)
    if digest != EXPECTED_HASHES[fname]:
        return {"sandbox": name, "status": "STOPPED",
                "step": "dataset hash check",
                "evidence": f"{fname} hashes {digest}, "
                            f"expected {EXPECTED_HASHES[fname]}"}
    try:
        canon_a, totals_a, structured = derive_a(path)
    except ValueError as e:
        return {"sandbox": name, "status": "STOPPED",
                "step": "T1 (attested ordered pairs)",
                "evidence": str(e)}
    canon_b, totals_b = derive_b(path)
    if canon_a != canon_b or totals_a != totals_b:
        detail = f"totals A={totals_a} B={totals_b}"
        for part in ("pairs", "positions", "lengths"):
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
                "step": "L3 agreement (TC-105-11)", "evidence": detail}
    ok, detail = reconcile(structured, totals_a, l2)
    if not ok:
        return {"sandbox": name, "status": "STOPPED",
                "step": "T5 (reconciliation)", "evidence": detail}
    result = {"sandbox": name, "status": "COMPLETED",
              "dataset": fname, "dataset_sha256": digest,
              "totals": totals_a, "implementations_agree": True,
              "reconciliation": detail,
              "shape": shape(structured, totals_a)}
    result.update(structured)
    return result


def main():
    out = {"stage": 3, "rung": "L3", "custody": CUSTODY,
           "sandboxes": {}, "checks": []}
    l2 = stage2_expectations()

    # TC-105-12: the reserve is hashed, never opened or parsed.
    reserve_hash = sha256_file(os.path.join(CUSTODY, RESERVE))
    out["checks"].append({
        "tc": "TC-105-12", "result":
            "PASS" if reserve_hash == EXPECTED_HASHES[RESERVE] else "FAIL",
        "reserve_sha256": reserve_hash,
        "note": "the reserve dataset was opened only by the hashing "
                "function; no Stage 3 derivation read it"})

    for name in ("indus", "eteocypriot", "meroitic"):
        out["sandboxes"][name] = run_sandbox(name, l2[name])

    agreed = [n for n, s in out["sandboxes"].items()
              if s["status"] == "COMPLETED"]
    out["checks"].append({
        "tc": "TC-105-11",
        "result": "PASS" if len(agreed) == 3 else "PARTIAL",
        "note": "both L3 implementations agree exactly, the filed L2 "
                "totals reproduce, and every T5 reconciliation identity "
                f"holds, in: {', '.join(agreed) if agreed else 'none'}"})

    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
