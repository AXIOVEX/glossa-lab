#!/usr/bin/env python3
"""Spec 105 Stage 2 execution: ladder rung L2 (counting and
frequency derived from recurrence) for the three ELSEWHERE
sandboxes (spec.md section 5; stage registered by
records/stage-2-registration-2026-11-25.md; test cases
TC-105-08, TC-105-09, TC-105-10).

Run on tower-compute. Reads only the custody derivation
datasets; the Indus reserve is hashed by sha256_file and
never opened or parsed (TC-105-09). Prints a JSON summary
to stdout; the summary is filed as the raw output of
record. Each sandbox is processed independently: a failure
stops that sandbox only and is reported with its step and
evidence.
"""
import hashlib, json, os, subprocess
from fractions import Fraction

HOME = os.path.expanduser("~")
CUSTODY = os.path.join(HOME, ".syncyard", "worktrees", "glossa",
                       "glossa-custody", "spec105")
REPO = os.path.join(HOME, ".syncyard", "worktrees", "glossa",
                    "s105-stage2-clone")
STAGE1_OUTPUT = os.path.join(
    REPO, "specs", "105-elsewhere-sandbox", "records",
    "stage-1-output-2026-11-25.json")

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

AWK_TALLY = r"""
function gcd(a, b,   t) { while (b) { t = b; b = a % b; a = t } return a }
{
  line = $0
  sub(/^ +/, "", line)
  sp = index(line, " ")
  cnt = substr(line, 1, sp - 1) + 0
  mark = substr(line, sp + 1)
  total += cnt
  n++
  counts[n] = cnt
  marks[n] = mark
}
END {
  for (i = 1; i <= n; i++) {
    g = gcd(counts[i], total)
    printf "%s\t%d\t%d/%d\n", marks[i], counts[i], counts[i] / g, total / g
  }
}
"""


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def derive_a(path):
    """L2, implementation A: parse the dataset JSON and tally
    recurrences with a dict, in recorded order. Returns the
    canonical ordered table lines (mark TAB count TAB reduced
    fraction), the corpus totals, and the table as tuples."""
    data = json.load(open(path, encoding="utf-8"))
    counts = {}
    n_lines = 0
    n_groups = 0
    n_tokens = 0
    for art in data:
        n_lines += len(art["lines"])
        for line in art["lines"]:
            n_groups += len(line)
            for group in line:
                n_tokens += len(group)
                for m in group:
                    counts[m] = counts.get(m, 0) + 1
    total = n_tokens
    table = []
    for m, c in counts.items():
        f = Fraction(c, total)
        table.append((m, c, f"{f.numerator}/{f.denominator}"))
    table.sort(key=lambda t: (-t[1], t[0]))
    lines = [f"{m}\t{c}\t{fr}" for (m, c, fr) in table]
    totals = {"artifacts": len(data), "lines": n_lines,
              "groups": n_groups, "tokens": n_tokens}
    return lines, totals, table


def derive_b(path):
    """L2, implementation B (independent): structural totals by
    jq expressions over the raw bytes; the tally by a jq mark
    stream through LC_ALL=C sort and uniq -c, with an awk
    tally and gcd fraction reduction, canonically ordered by
    a final sort. No code is shared with A."""
    def jq1(expr):
        r = subprocess.run(["jq", expr, path], capture_output=True,
                           text=True, check=True)
        return int(r.stdout.strip())
    totals = {"artifacts": jq1("length"),
              "lines": jq1("[.[].lines | length] | add"),
              "groups": jq1("[.[].lines[] | length] | add"),
              "tokens": jq1("[.[].lines[][] | length] | add")}
    env = {**os.environ, "LC_ALL": "C"}
    stream = subprocess.run(["jq", "-r", ".[].lines[][][]", path],
                            capture_output=True, text=True, check=True)
    srt = subprocess.run(["sort"], input=stream.stdout,
                         capture_output=True, text=True, check=True,
                         env=env)
    unc = subprocess.run(["uniq", "-c"], input=srt.stdout,
                         capture_output=True, text=True, check=True)
    awk = subprocess.run(["awk", AWK_TALLY], input=unc.stdout,
                         capture_output=True, text=True, check=True)
    ordered = subprocess.run(
        ["sort", "-t", "\t", "-k2,2nr", "-k1,1"], input=awk.stdout,
        capture_output=True, text=True, check=True, env=env)
    lines = [l for l in ordered.stdout.splitlines() if l]
    return lines, totals


def shape(table, total):
    singletons = sum(1 for _, c, _ in table if c == 1)
    tops = []
    for k in (1, 5, 10):
        taken = table[:k]
        s = sum(c for _, c, _ in taken)
        f = Fraction(s, total)
        tops.append({"marks_taken": len(taken), "tokens": s,
                     "share": f"{f.numerator}/{f.denominator}"})
    return {"inventory_size": len(table),
            "singleton_marks": singletons,
            "recurring_marks": len(table) - singletons,
            "top_shares": tops}


def stage1_expectations():
    """The Stage 1 filed censuses and inventory sizes, read from
    the study's own Stage 1 raw output (a check source, never a
    derivation input)."""
    s1 = json.load(open(STAGE1_OUTPUT, encoding="utf-8"))
    sb = s1["sandboxes"]
    exp = {}
    ind = sb["indus"]["derivation"]
    exp["indus"] = {
        "totals": {"artifacts": ind["artifacts"], "lines": ind["lines"],
                   "groups": ind["groups"], "tokens": ind["tokens"]},
        "inventory_size": sb["indus"]["derivation_result"]["inventory_size"]}
    for name in ("eteocypriot", "meroitic"):
        s = sb[name]
        exp[name] = {
            "totals": {"artifacts": s["artifacts"], "lines": s["lines"],
                       "groups": s["groups"], "tokens": s["tokens"]},
            "inventory_size": s["derivation_result"]["inventory_size"]}
    return exp


def run_sandbox(name, exp):
    fname = DATASETS[name]
    path = os.path.join(CUSTODY, fname)
    digest = sha256_file(path)
    if digest != EXPECTED_HASHES[fname]:
        return ({"sandbox": name, "status": "STOPPED",
                 "step": "dataset hash check",
                 "evidence": f"{fname} hashes {digest}, "
                             f"expected {EXPECTED_HASHES[fname]}"},
                None, None)
    lines_a, totals_a, table = derive_a(path)
    lines_b, totals_b = derive_b(path)
    if lines_a != lines_b or totals_a != totals_b:
        detail = (f"table lines A={len(lines_a)} B={len(lines_b)}; "
                  f"totals A={totals_a} B={totals_b}")
        for i, (x, y) in enumerate(zip(lines_a, lines_b)):
            if x != y:
                detail += f"; first differing line {i}: A={x!r} B={y!r}"
                break
        return ({"sandbox": name, "status": "STOPPED",
                 "step": "L2 agreement (TC-105-08)", "evidence": detail},
                None, None)
    if totals_a != exp["totals"] or len(table) != exp["inventory_size"]:
        return ({"sandbox": name, "status": "STOPPED",
                 "step": "Stage 1 census reproduction",
                 "evidence": f"derived totals {totals_a} vs Stage 1 "
                             f"{exp['totals']}; inventory {len(table)} "
                             f"vs Stage 1 {exp['inventory_size']}"},
                None, None)
    result = {"sandbox": name, "status": "COMPLETED",
              "dataset": fname, "dataset_sha256": digest,
              "totals": totals_a, "implementations_agree": True,
              "shape": shape(table, totals_a["tokens"]),
              "table": [{"mark": m, "count": c, "frequency": fr}
                        for (m, c, fr) in table]}
    return result, table, totals_a


def main():
    out = {"stage": 2, "rung": "L2", "custody": CUSTODY,
           "sandboxes": {}, "checks": []}
    exp = stage1_expectations()

    # TC-105-09: the reserve is hashed, never opened or parsed.
    reserve_hash = sha256_file(os.path.join(CUSTODY, RESERVE))
    out["checks"].append({
        "tc": "TC-105-09", "result":
            "PASS" if reserve_hash == EXPECTED_HASHES[RESERVE] else "FAIL",
        "reserve_sha256": reserve_hash,
        "note": "the reserve dataset was opened only by the hashing "
                "function; no Stage 2 derivation read it"})

    indus_table = indus_totals = None
    for name in ("indus", "eteocypriot", "meroitic"):
        r, table, totals = run_sandbox(name, exp[name])
        if name == "indus":
            indus_table, indus_totals = table, totals
        out["sandboxes"][name] = r

    agreed = [n for n, s in out["sandboxes"].items()
              if s["status"] == "COMPLETED"]
    out["checks"].append({
        "tc": "TC-105-08",
        "result": "PASS" if len(agreed) == 3 else "PARTIAL",
        "note": "both L2 implementations agree exactly, and the "
                "Stage 1 censuses and inventory sizes reproduce, "
                f"in: {', '.join(agreed) if agreed else 'none'}"})

    if indus_table is not None:
        total = indus_totals["tokens"]
        out["sandboxes"]["indus"]["baseline"] = {
            "model": "unigram",
            "rung": "L2",
            "source_dataset": DATASETS["indus"],
            "source_dataset_sha256": EXPECTED_HASHES[DATASETS["indus"]],
            "tokens_total": total,
            "inventory_size": len(indus_table),
            "probability_rule":
                "P(m) = count(m) / tokens_total over the derivation "
                "inventory; marks outside the derivation inventory "
                "carry no filed mass (the G-IND gate stage registers "
                "its unseen-mark rule and margin before unsealing, "
                "spec.md section 7)",
            "sealed_reserve_sha256": reserve_hash,
            "parameters": [{"mark": m, "count": c, "frequency": fr}
                           for (m, c, fr) in indus_table]}

    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
