#!/usr/bin/env python3
"""Spec 099 — inference log reference implementation.

Implements, as the package's reference implementation:

- ``validate_log`` — the schema of spec section 3.2
  (TC-099-01).
- ``basis_elements`` / ``check_completeness`` — the
  completeness check of spec section 3 / C099-2 (TC-099-02):
  every checkable element of a filed basis is covered by a
  log item citing it, and every log item cites only what the
  basis (or a spec-named supplementary record) states.
- ``audit_log`` — the Q3 graph audit of spec section 4
  (removal, class recomputation under both treatments,
  strongly connected components, open ends). A pure function
  of the log (TC-099-03).

CLI (payload verdicts are the process's own exit code plus
the printed PAYLOAD VERDICT line):

    python3 inference_log.py validate LOG.json [--full]
    python3 inference_log.py completeness LOG.json ROWS.json
    python3 inference_log.py audit LOG.json [--out OUT.json]

ROWS.json is a list of {"sign": ..., "basis_as_filed": ...}
objects (the filed basis rows the log was built from).
"""

from __future__ import annotations

import json
import re
import sys

# Kind -> type, per spec section 3.3.
KIND_TYPE = {
    "corpus_count": "a",
    "positional_statistic": "a",
    "dictionary_entry": "a",
    "published_proposal": "a",
    "comparative_lexical": "a",
    "motif_association": "a",
    "iconographic_interpretation": "a",
    "crosswalk_identity": "a",
    "corrected_validation": "a",
    "literary_parallel": "a",
    "interpreted_anchor": "b",
    "slot_label": "b",
    "self_assertion": "b",
    "internal_label": "b",
    "consistency_score": "ambiguous",
}

CLASSES = {"E", "I", "R", "P", "U"}
Q4_FLAGS = {"S", "N", "M", "A"}
SIGN_RE = re.compile(r"^M\d{3}$")

# Records the spec names as legitimate sources for a target
# that the entry's own basis does not name (spec sections 2
# and 5: the slot markers of record for M267).
TARGET_SOURCES = {
    "standings-supplement-2026-11-21.md",
    "dependency-record-2026-11-21.md",
    "coscientist-audit-94-adjudication-2026-11-21.md",
    "standings-relabel-execution-2026-11-21.md",
}


# ---------------------------------------------------------------- schema


def validate_log(log: dict, expect_full: bool = False) -> list[str]:
    """Return a list of schema violations (empty = valid)."""
    errs: list[str] = []
    if not isinstance(log, dict):
        return ["log is not a JSON object"]
    if log.get("artifact") != "inference-log":
        errs.append("artifact is not 'inference-log'")
    entries = log.get("entries")
    if not isinstance(entries, list):
        return errs + ["entries is not a list"]
    if expect_full and len(entries) != 94:
        errs.append(f"expected 94 entries, found {len(entries)}")
    seen: set[str] = set()
    for entry in entries:
        sign = entry.get("sign")
        where = f"entry {sign!r}"
        if not isinstance(sign, str) or not SIGN_RE.match(sign):
            errs.append(f"{where}: sign missing or malformed")
            continue
        if sign in seen:
            errs.append(f"{where}: duplicate sign")
        seen.add(sign)
        if not entry.get("reading"):
            errs.append(f"{where}: reading missing")
        if entry.get("executed_class") not in CLASSES:
            errs.append(f"{where}: executed_class not in vocabulary")
        if entry.get("q4_flag") not in Q4_FLAGS:
            errs.append(f"{where}: q4_flag not in vocabulary")
        basis = entry.get("basis_as_filed")
        if not isinstance(basis, str) or not basis:
            errs.append(f"{where}: basis_as_filed missing")
            basis = ""
        items = entry.get("items")
        if not isinstance(items, list) or not items:
            errs.append(f"{where}: items missing or empty")
            continue
        ids: set[str] = set()
        for item in items:
            iid = item.get("id")
            iwhere = f"{where} item {iid!r}"
            if not iid or not iid.startswith(sign + "-"):
                errs.append(f"{iwhere}: id missing or not sign-prefixed")
            if iid in ids:
                errs.append(f"{iwhere}: duplicate item id")
            ids.add(iid)
            kind = item.get("kind")
            if kind not in KIND_TYPE:
                errs.append(f"{iwhere}: kind not in vocabulary")
                continue
            if item.get("type") != KIND_TYPE[kind]:
                errs.append(
                    f"{iwhere}: type {item.get('type')!r} does not "
                    f"match kind {kind!r} (expects {KIND_TYPE[kind]!r})"
                )
            if not item.get("statement"):
                errs.append(f"{iwhere}: statement missing")
            span = item.get("basis_span")
            if not span or span not in basis:
                errs.append(
                    f"{iwhere}: basis_span missing or not a "
                    "verbatim clause of basis_as_filed"
                )
            if item.get("type") in ("b", "ambiguous") and not item.get("reason"):
                errs.append(f"{iwhere}: reason required for (b)/ambiguous items")
            targets = item.get("targets")
            if not isinstance(targets, list) or any(
                not isinstance(t, str) or not SIGN_RE.match(t) for t in targets
            ):
                errs.append(f"{iwhere}: targets malformed")
                targets = []
            if item.get("type") == "b" and not targets and not item.get("target_note"):
                errs.append(
                    f"{iwhere}: (b) item with no named target "
                    "requires a target_note"
                )
            for t in targets:
                if t not in basis and not item.get("target_source"):
                    errs.append(
                        f"{iwhere}: target {t} not named in the "
                        "basis and no target_source given"
                    )
                if item.get("target_source") and (
                    item["target_source"] not in TARGET_SOURCES
                ):
                    errs.append(
                        f"{iwhere}: target_source "
                        f"{item['target_source']!r} is not a "
                        "spec-named record"
                    )
    return errs


# ---------------------------------------------------------- completeness

_DEDR_RE = re.compile(r"DEDR\s+(\d{1,4})")
_DICTREF_RE = re.compile(r"Dictionary reference as recorded:\s*(?:DEDR\s*)?(\d{1,4})")


def basis_elements(basis: str, own_sign: str) -> list[dict]:
    """Extract the checkable elements of one filed basis.

    Each element is {"family", "key", "anchor"}: the anchor is
    the verbatim text an item's basis_span must contain (for
    families whose coverage is span-based), and the key is
    what a covering item must name (for target-based
    families). Families follow spec section 3: dictionary
    citations, collocate premises, pattern targets, slot
    constructs, consistency scores, motif clauses, counts,
    self-assertions, published mentions, crosswalk steps.
    """
    out: list[dict] = []
    seen: set[tuple] = set()

    def add(family: str, key: str, anchor: str) -> None:
        sig = (family, key)
        if sig not in seen:
            seen.add(sig)
            out.append({"family": family, "key": key, "anchor": anchor})

    for m in _DEDR_RE.finditer(basis):
        add("dedr", m.group(1).lstrip("0") or "0", m.group(0))
    for m in _DICTREF_RE.finditer(basis):
        add("dedr", m.group(1).lstrip("0") or "0", m.group(0))
    for m in re.finditer(r"collocates with HIGH anchor (M\d{3})", basis):
        add("collocate", m.group(1), m.group(0))
    for m in re.finditer(r"HIGH-anchor collocate (M\d{3})", basis):
        add("collocate", m.group(1), m.group(0))
    for m in re.finditer(r"(?i)patterns?\s*[:=][^;.]*", basis):
        for tok in re.findall(r"M\d{3}", m.group(0)):
            if tok != own_sign:
                add("pattern_target", tok, m.group(0))
    if "slot" in basis.lower():
        m = re.search(r"[^;.]*slot[^;.]*", basis, re.IGNORECASE)
        add("slot_construct", "slot", m.group(0) if m else "slot")
    for m in re.finditer(r"SA-cons=([\d.]+)", basis):
        add("consistency_score", m.group(1), m.group(0))
    for m in re.finditer(r"(?:Exclusive to|appears on) [^;]*seals", basis):
        add("motif", m.group(0), m.group(0))
    for m in re.finditer(r"freq=(\d+)", basis):
        add("count", m.group(1), m.group(0))
    for m in re.finditer(r"\(freq (\d+)\)", basis):
        add("count", m.group(1), m.group(0))
    for m in re.finditer(r"\(n=(\d+)\)", basis):
        add("count", m.group(1), m.group(0))
    for m in re.finditer(r"frequency \((\d+)\)", basis):
        add("count", m.group(1), m.group(0))
    if "has specific PDR reading" in basis:
        add("self_assertion", "pdr", "has specific PDR reading")
    for m in re.finditer(r"mentions across sources:\s*([^)]+)\)", basis):
        add("published_mentions", m.group(1).strip(), m.group(0))
    if "mahadevan_parpola_crosswalk" in basis or (
        "crosswalk evidence" in basis
    ):
        add("crosswalk", "crosswalk", "crosswalk")
    return out


def _element_covered(element: dict, entry: dict) -> bool:
    items = entry.get("items", [])
    family = element["family"]
    if family == "dedr":
        num = element["key"]
        for item in items:
            span = item.get("basis_span", "")
            stmt = item.get("statement", "")
            if re.search(rf"DEDR\s+0*{num}\b", span) or re.search(
                rf"DEDR\s+0*{num}\b", stmt
            ):
                return True
            if item.get("kind") == "dictionary_entry" and re.search(
                rf"\b0*{num}\b", span
            ):
                return True
        return False
    if family in ("collocate", "pattern_target"):
        return any(
            item.get("kind") == "interpreted_anchor"
            and element["key"] in item.get("targets", [])
            for item in items
        ) or (
            family == "pattern_target"
            and any(
                item.get("kind") == "slot_label"
                and element["key"] in item.get("targets", [])
                for item in items
            )
        )
    if family == "slot_construct":
        return any(item.get("kind") == "slot_label" for item in items)
    if family == "consistency_score":
        return any(
            item.get("kind") == "consistency_score"
            and element["anchor"] in item.get("basis_span", "")
            for item in items
        )
    if family == "motif":
        return any(
            item.get("kind") == "motif_association"
            and element["anchor"] in item.get("basis_span", "")
            for item in items
        )
    if family == "count":
        return any(element["anchor"] in item.get("basis_span", "") for item in items)
    if family == "self_assertion":
        return any(item.get("kind") == "self_assertion" for item in items)
    if family == "published_mentions":
        return any(
            item.get("kind") == "published_proposal"
            and element["key"].split()[0] in item.get("basis_span", "")
            for item in items
        )
    if family == "crosswalk":
        return any(item.get("kind") == "crosswalk_identity" for item in items)
    return False


def check_completeness(log: dict, rows: list[dict]) -> list[str]:
    """Return completeness violations (empty = complete).

    ``rows`` are the filed basis rows the log was built from.
    Checks both directions of C099-2 over the checkable
    families: every element of every filed basis is covered,
    and every item cites a span its entry's basis contains
    and names no target the basis and the spec-named records
    do not state.
    """
    errs: list[str] = []
    by_sign = {e["sign"]: e for e in log.get("entries", [])}
    row_signs = set()
    for row in rows:
        sign = row["sign"]
        row_signs.add(sign)
        entry = by_sign.get(sign)
        if entry is None:
            errs.append(f"{sign}: row present but no log entry")
            continue
        if entry.get("basis_as_filed") != row["basis_as_filed"]:
            errs.append(f"{sign}: log basis differs from the filed row")
        for element in basis_elements(row["basis_as_filed"], sign):
            if not _element_covered(element, entry):
                errs.append(
                    f"{sign}: filed element {element['family']}:"
                    f"{element['key']} not covered by any item"
                )
    for sign in by_sign:
        if sign not in row_signs:
            errs.append(f"{sign}: log entry present but no filed row")
    return errs


# ---------------------------------------------------------------- audit


def _outcome(executed_class: str, items: list[dict], remove_types: set) -> dict:
    removed = [i for i in items if i["type"] in remove_types]
    remaining = [i for i in items if i["type"] not in remove_types]
    weakened = bool(removed)
    if executed_class == "I" and not remaining:
        return {
            "class_outcome": "would_change",
            "destination": "U",
            "weakened": weakened,
            "lost_items": [i["id"] for i in removed],
        }
    return {
        "class_outcome": "unchanged",
        "destination": None,
        "weakened": weakened,
        "lost_items": [i["id"] for i in removed],
    }


def _tarjan_scc(nodes: list[str], edges: dict) -> list[list[str]]:
    index_counter = [0]
    stack: list[str] = []
    lowlink: dict = {}
    index: dict = {}
    on_stack: dict = {}
    result: list[list[str]] = []

    def strongconnect(v: str) -> None:
        index[v] = index_counter[0]
        lowlink[v] = index_counter[0]
        index_counter[0] += 1
        stack.append(v)
        on_stack[v] = True
        for w in edges.get(v, []):
            if w not in index:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack.get(w):
                lowlink[v] = min(lowlink[v], index[w])
        if lowlink[v] == index[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                comp.append(w)
                if w == v:
                    break
            result.append(sorted(comp))

    sys.setrecursionlimit(10000)
    for v in nodes:
        if v not in index:
            strongconnect(v)
    return result


def audit_log(log: dict) -> dict:
    """The Q3 graph audit (spec section 4) as a pure function."""
    entries = log["entries"]
    signs = [e["sign"] for e in entries]
    sign_set = set(signs)
    outcomes: dict = {}
    edges: dict = {s: set() for s in signs}
    open_ends: list[dict] = []
    census = {"a": 0, "b": 0, "ambiguous": 0, "items": 0}
    for entry in entries:
        items = entry["items"]
        for item in items:
            census[item["type"]] += 1
            census["items"] += 1
            if item["type"] == "b":
                if item.get("targets"):
                    for t in item["targets"]:
                        if t in sign_set:
                            edges[entry["sign"]].add(t)
                else:
                    open_ends.append(
                        {
                            "sign": entry["sign"],
                            "item": item["id"],
                            "kind": item["kind"],
                            "target_note": item.get("target_note", ""),
                        }
                    )
        primary = _outcome(entry["executed_class"], items, {"b"})
        sensitivity = _outcome(entry["executed_class"], items, {"b", "ambiguous"})
        outcomes[entry["sign"]] = {
            "reading": entry["reading"],
            "executed_class": entry["executed_class"],
            "primary": primary,
            "sensitivity": sensitivity,
            "divergent": primary != sensitivity,
        }
    sccs = _tarjan_scc(signs, {k: sorted(v) for k, v in edges.items()})
    cycles = [c for c in sccs if len(c) > 1]
    self_loops = [s for s in signs if s in edges[s]]
    headline = {
        "readings": len(entries),
        "class_changes_primary": sum(
            1 for o in outcomes.values() if o["primary"]["class_outcome"] == "would_change"
        ),
        "weakened_primary": sum(1 for o in outcomes.values() if o["primary"]["weakened"]),
        "class_changes_sensitivity": sum(
            1
            for o in outcomes.values()
            if o["sensitivity"]["class_outcome"] == "would_change"
        ),
        "weakened_sensitivity": sum(
            1 for o in outcomes.values() if o["sensitivity"]["weakened"]
        ),
        "divergent_readings": sum(1 for o in outcomes.values() if o["divergent"]),
    }
    return {
        "artifact": "q3-graph-audit",
        "spec": "099-inference-log",
        "edge_census": census,
        "headline": headline,
        "outcomes": outcomes,
        "scc_cycles": cycles,
        "self_loops": self_loops,
        "open_ends": open_ends,
    }


# ------------------------------------------------------------------ CLI


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, path = argv[1], argv[2]
    with open(path, encoding="utf-8") as fh:
        log = json.load(fh)
    if cmd == "validate":
        errs = validate_log(log, expect_full="--full" in argv)
        for e in errs:
            print("VIOLATION:", e)
        ok = not errs
        print(
            f"PAYLOAD VERDICT: {'PASS' if ok else 'FAIL'} "
            f"(entries={len(log.get('entries', []))}, violations={len(errs)})"
        )
        return 0 if ok else 1
    if cmd == "completeness":
        if len(argv) < 4:
            print("usage: completeness LOG.json ROWS.json")
            return 2
        with open(argv[3], encoding="utf-8") as fh:
            rows = json.load(fh)
        errs = validate_log(log) + check_completeness(log, rows)
        for e in errs:
            print("VIOLATION:", e)
        ok = not errs
        print(
            f"PAYLOAD VERDICT: {'PASS' if ok else 'FAIL'} "
            f"(rows={len(rows)}, violations={len(errs)})"
        )
        return 0 if ok else 1
    if cmd == "audit":
        result = audit_log(log)
        text = json.dumps(result, ensure_ascii=False, indent=1, sort_keys=True)
        if "--out" in argv:
            out_path = argv[argv.index("--out") + 1]
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(text + "\n")
        h = result["headline"]
        print(
            "PAYLOAD VERDICT: DONE "
            f"(class_changes_primary={h['class_changes_primary']}, "
            f"weakened_primary={h['weakened_primary']}, "
            f"cycles={len(result['scc_cycles'])}, "
            f"open_ends={len(result['open_ends'])})"
        )
        return 0
    print(f"unknown command {cmd!r}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
