#!/usr/bin/env python3
"""Spec 100 — Motif-claims rerun: pipeline of record.

Recomputes the 13 animal-motif claims of record
(`specs/091-anchor-comparison-integrity/records/motif-numerical-evidence-2026-11-21.md`,
PR #634) from a deposited per-seal iconography join: full 2x2
contingency cells per claim, lift and odds ratio, against the
claims' own filed threshold (lift > 5.0).

Frozen definitions (spec.md section 3):

- Population: the 1,670 seals of the tracked corpus files
  `outputs/phase100_full_corpus.json` (path A) and
  `outputs/phase114_full_seal_translations.json` (path B),
  keyed by `cisi_id`. Both paths are computed and must agree
  exactly, cell for cell, or the run's outcome is the
  disagreement.
- Deposit: a tracked CSV with columns `cisi_id,iconography`,
  one row per covered seal, produced by
  `tools/deposit_extract.py` from the pinned Holdat corpus
  build. A population seal with no row is missing: excluded
  from every cell, with the denominator restated as the
  labeled population. A row with an empty iconography string
  is a recorded no-motif label (motif-absent). No label is
  imputed.
- Motif match (the historical scripts' rule): a seal carries
  motif M when M's token appears in the seal's lowercased
  iconography string.
- lift = a*N / ((a+b) * (a+c)); odds ratio = (a*d) / (b*c),
  reported as null ("undefined (zero cell)") where b or c
  is zero. Verdict per claim: REPRODUCED when lift > 5.0,
  otherwise NOT REPRODUCED.

Modes:

- `record`: requires `--deposit FILE` and
  `--deposit-record PATH`. The gate is mechanical
  (RT6-C2, 2026-11-22): record mode refuses (GATE CLOSED,
  exit 3, computing nothing) UNLESS all of: (a) the deposit
  path resolves to the registered deposit path
  `specs/100-motif-claims-rerun/records/iconography-deposit-v1.csv`
  inside the repository rooted at `--root`; (b)
  `--deposit-record` names a repo-relative path to a file
  that exists in that tree; (c) that record file states the
  deposit CSV's SHA-256 and the stated hash matches the
  actual deposit file; (d) that record file carries a line
  beginning `Permission basis:` that states a granting
  Miller reply as its basis: the line must contain a
  granting term and no refusal term (see
  `gate_record_check`). Any other CSV, any other path, or
  any bare citation string does not open the gate. This is
  claim C100-1's mechanism, not a courtesy.
- `proof`: synthetic labels only, generated deterministically
  in memory from the real population's seal ids; never reads
  a deposit; every output carries the banner
  "PROOF - NOT A RESULT". The proof computes no claim's
  statistics from real labels (C100-7).

Exit codes: 0 = run completed and paths agree; 3 = GATE
CLOSED (record mode without a deposit); 4 = PATH
DISAGREEMENT; 5 = DEPOSIT DEFECT (a deposit row keyed
outside the population). A run's own exit code is its
payload verdict.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

THRESHOLD = 5.0

# The 13 claims exactly as filed (PR #634, section 3): sign,
# reading, filed motif. The filed basis for 12 of the 13 is
# the anchor file's summary assertion "Exclusive to <animal>
# seals (lift > 5.0)"; M063's filed corrected figures stand
# separately (spec.md section 2).
CLAIMS = [
    {"sign": "M006", "reading": "puli", "motif": "tiger"},
    {"sign": "M013", "reading": "nakaram", "motif": "gharial"},
    {"sign": "M016", "reading": "kaliṟu", "motif": "elephant"},
    {"sign": "M039", "reading": "āṉai", "motif": "elephant"},
    {"sign": "M045", "reading": "yānai", "motif": "elephant"},
    {"sign": "M057", "reading": "māṭu", "motif": "zebu"},
    {"sign": "M060", "reading": "kāṇṭāmirukam", "motif": "rhinoceros"},
    {"sign": "M062", "reading": "erutu", "motif": "zebu"},
    {"sign": "M063", "reading": "mutalai", "motif": "gharial"},
    {"sign": "M067", "reading": "kōṭṭāṉ", "motif": "rhinoceros"},
    {"sign": "M068", "reading": "maṟi", "motif": "rhinoceros"},
    {"sign": "M073", "reading": "kōṉ", "motif": "zebu"},
    {"sign": "M080", "reading": "vēṅkai", "motif": "tiger"},
]

PROOF_BANNER = "PROOF - NOT A RESULT (synthetic labels)"
PROOF_ICONS = [
    "synthetic-tiger",
    "synthetic-gharial",
    "synthetic-elephant",
    "synthetic-zebu",
    "synthetic-rhinoceros",
    "synthetic-unicorn",
    "synthetic-none",
]

REGISTERED_DEPOSIT_REL = Path(
    "specs/100-motif-claims-rerun/records/iconography-deposit-v1.csv")

# RT6-C2 gate rule for the `Permission basis:` line (spec
# section 5, deposit-landing step, as amended 2026-11-22):
# the line must contain a granting term and must contain
# no refusal term. A line recording refusal or silence
# therefore never satisfies the gate.
GRANTING_TERMS = (
    "grants", "granted", "granting", "grant of permission",
    "confirms permission", "permission confirmed",
    "permission is granted",
)
REFUSAL_TERMS = (
    "refus", "deni", "silence", "silent", "no reply",
    "not granted", "does not grant", "no permission",
    "withheld", "without permission",
)


def gate_record_check(root: Path, deposit: Path | None,
                      deposit_record: str | None) -> str | None:
    """Return None if the mechanical gate opens, else the
    refusal reason. Checks (a)-(d) of the module docstring,
    in order; every failure is GATE CLOSED."""
    if deposit is None or deposit_record is None or not str(deposit_record).strip():
        return "record mode requires a deposit file and its deposit record"
    # (a) deposit must resolve to the registered path in-tree
    registered = (root / REGISTERED_DEPOSIT_REL)
    try:
        if deposit.resolve() != registered.resolve():
            return ("deposit path is not the registered deposit path "
                    + str(REGISTERED_DEPOSIT_REL))
    except OSError:
        return "deposit path cannot be resolved"
    if not deposit.is_file():
        return "registered deposit file does not exist"
    # (b) deposit-record must be a repo-relative path in-tree
    rec_rel = Path(str(deposit_record))
    if rec_rel.is_absolute():
        return "--deposit-record must be a repo-relative path"
    rec_path = (root / rec_rel)
    try:
        rec_resolved = rec_path.resolve()
        root_resolved = root.resolve()
        if root_resolved not in rec_resolved.parents and rec_resolved != root_resolved:
            return "--deposit-record path escapes the repository tree"
    except OSError:
        return "--deposit-record path cannot be resolved"
    if not rec_path.is_file():
        return "deposit record file does not exist in the tree"
    text = rec_path.read_text(encoding="utf-8", errors="replace")
    # (c) record must state the deposit CSV's actual SHA-256
    actual = hashlib.sha256(deposit.read_bytes()).hexdigest()
    stated = {m.group(0).lower() for m in re.finditer(r"\b[0-9a-fA-F]{64}\b", text)}
    if actual not in stated:
        return "deposit record does not state the deposit CSV's SHA-256"
    # (d) Permission basis line: granting term, no refusal term
    basis_lines = [ln.strip() for ln in text.splitlines()
                   if ln.strip().startswith("Permission basis:")]
    if not basis_lines:
        return "deposit record carries no 'Permission basis:' line"
    basis = basis_lines[0].lower()
    if any(term in basis for term in REFUSAL_TERMS):
        return "'Permission basis:' line records refusal or silence, not a grant"
    if not any(term in basis for term in GRANTING_TERMS):
        return "'Permission basis:' line states no granting Miller reply"
    return None


class PathDisagreement(Exception):
    """The two corpus representations disagree on a count."""


class DepositDefect(Exception):
    """The deposit keys a seal outside the population."""


def load_population_a(path: Path) -> dict[str, list[str]]:
    """Path A: outputs/phase100_full_corpus.json."""
    data = json.loads(path.read_text(encoding="utf-8"))
    return {t["cisi_id"]: list(t["signs"]) for t in data["translations"]}


def load_population_b(path: Path) -> dict[str, list[str]]:
    """Path B: outputs/phase114_full_seal_translations.json."""
    data = json.loads(path.read_text(encoding="utf-8"))
    return {cid: list(t["signs"]) for cid, t in data["all_translations"].items()}


def load_labels(path: Path) -> dict[str, str]:
    """Deposit format: CSV with columns cisi_id,iconography.

    Values are lowercased and stripped, as the historical
    scripts read them. A row whose iconography is empty is a
    recorded no-motif label and is kept (it is not missing).
    """
    labels: dict[str, str] = {}
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or "cisi_id" not in reader.fieldnames \
                or "iconography" not in reader.fieldnames:
            raise ValueError(
                "deposit file lacks the frozen columns cisi_id,iconography")
        for row in reader:
            labels[row["cisi_id"]] = (row.get("iconography") or "").strip().lower()
    return labels


def synthetic_labels(population: dict[str, list[str]]) -> dict[str, str]:
    """Deterministic synthetic labels over the real seal ids.

    Proof mode only. The assignment is a hash rotation over a
    synthetic vocabulary; it carries no information about any
    seal's real iconography.
    """
    labels: dict[str, str] = {}
    for cid in population:
        digest = hashlib.sha256(f"100-proof-v1:{cid}".encode("utf-8")).hexdigest()
        labels[cid] = PROOF_ICONS[int(digest[:8], 16) % len(PROOF_ICONS)]
    return labels


def compute_claim(population: dict[str, list[str]],
                  labels: dict[str, str],
                  claim: dict) -> dict:
    """One claim's 2x2 over the labeled population."""
    sign, motif = claim["sign"], claim["motif"]
    a = b = c = d = 0
    n_labeled = 0
    for cid, signs in population.items():
        if cid not in labels:
            continue  # missing: excluded from every cell (C100-5)
        n_labeled += 1
        has_sign = sign in signs
        has_motif = motif in labels[cid]
        if has_sign and has_motif:
            a += 1
        elif has_sign:
            b += 1
        elif has_motif:
            c += 1
        else:
            d += 1
    n = a + b + c + d
    lift = None
    if (a + b) > 0 and (a + c) > 0 and n > 0:
        lift = a * n / ((a + b) * (a + c))
    odds_ratio = None
    if b > 0 and c > 0:
        odds_ratio = (a * d) / (b * c)
    verdict = "REPRODUCED" if (lift is not None and lift > THRESHOLD) \
        else "NOT REPRODUCED"
    return {
        "sign": sign,
        "reading": claim["reading"],
        "motif": motif,
        "a": a, "b": b, "c": c, "d": d,
        "n_labeled": n,
        "n_population": len(population),
        "sign_marginal_population": sum(
            1 for signs in population.values() if sign in signs),
        "lift": (round(lift, 6) if lift is not None else None),
        "odds_ratio": (round(odds_ratio, 6) if odds_ratio is not None else None),
        "odds_ratio_note": (None if odds_ratio is not None
                            else "undefined (zero cell)"),
        "threshold": THRESHOLD,
        "verdict": verdict,
    }


def run(pop_a: dict[str, list[str]], pop_b: dict[str, list[str]],
        labels: dict[str, str], mode: str,
        deposit_record: str | None = None) -> dict:
    """Compute all 13 claims on both paths; they must agree."""
    foreign = sorted(set(labels) - set(pop_a))
    if foreign:
        raise DepositDefect(
            f"deposit rows keyed outside the population: {foreign[:5]}"
            f" ({len(foreign)} in all)")
    rows_a = [compute_claim(pop_a, labels, claim) for claim in CLAIMS]
    rows_b = [compute_claim(pop_b, labels, claim) for claim in CLAIMS]
    for ra, rb in zip(rows_a, rows_b):
        keys = ("a", "b", "c", "d", "n_labeled", "n_population",
                "sign_marginal_population", "lift", "odds_ratio", "verdict")
        if any(ra[k] != rb[k] for k in keys):
            raise PathDisagreement(
                f"path disagreement on {ra['sign']}: A={ra} B={rb}")
    outcome = {
        "study": "100-motif-claims-rerun",
        "mode": mode,
        "proof": mode == "proof",
        "population": len(pop_a),
        "claims": rows_a,
    }
    if mode == "proof":
        outcome["banner"] = PROOF_BANNER
    if deposit_record is not None:
        outcome["deposit_record"] = deposit_record
    return outcome


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--mode", choices=["record", "proof"], required=True)
    parser.add_argument("--root", type=Path, required=True,
                        help="repository root (outputs/ is read from it)")
    parser.add_argument("--deposit", type=Path, default=None,
                        help="deposit CSV (record mode, required)")
    parser.add_argument("--deposit-record", default=None,
                        help="repo-relative path to the deposit record file (record mode, required)")
    parser.add_argument("--out", type=Path, default=None,
                        help="write the outcome JSON here (default: stdout only)")
    args = parser.parse_args(argv)

    if args.mode == "record":
        reason = gate_record_check(args.root, args.deposit,
                                   args.deposit_record)
        if reason is not None:
            print(f"GATE CLOSED: {reason}. The deposit is held "
                  "under flag F-1 (Spec 100, claim C100-1); nothing "
                  "has been computed.")
            return 3

    pop_a = load_population_a(args.root / "outputs" / "phase100_full_corpus.json")
    pop_b = load_population_b(
        args.root / "outputs" / "phase114_full_seal_translations.json")

    if args.mode == "proof":
        labels = synthetic_labels(pop_a)
        print(PROOF_BANNER)
    else:
        labels = load_labels(args.deposit)
    try:
        outcome = run(pop_a, pop_b, labels,
                      mode=args.mode,
                      deposit_record=args.deposit_record
                      if args.mode == "record" else None)
    except PathDisagreement as exc:
        print(f"PATH DISAGREEMENT: {exc}")
        return 4
    except DepositDefect as exc:
        print(f"DEPOSIT DEFECT: {exc}")
        return 5

    text = json.dumps(outcome, indent=1, ensure_ascii=False)
    print(text)
    if args.out is not None:
        args.out.write_text(text + "\n", encoding="utf-8")
    for row in outcome["claims"]:
        print(f"{row['sign']} {row['motif']}: a={row['a']} b={row['b']} "
              f"c={row['c']} d={row['d']} lift={row['lift']} "
              f"odds_ratio={row['odds_ratio']} verdict={row['verdict']}")
    print("EXIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
