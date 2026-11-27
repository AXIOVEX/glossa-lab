#!/usr/bin/env python3
"""Spec 093 Stage 4 — T401 site pass administration.

Administers exactly what
`specs/093-material-context-channel/records/stage4-site-freeze-v1.md`
freezes: sequence behavior (Q1 inscription length, Q2
sign choice) conditioned on site over P-site's adjudged
sites, on a seeded discovery/held-out split, against
2,000-draw permutation batteries and a pseudo-site
negative control. Every constant below is the freeze's;
the tool takes no parameter that could move a result.

Each execution is a Spec 089 run on the `study` surface
(run-defs v2), minted and written through
`backend/glossa_lab/run_records.py`. A refusal the
freeze names (a pin mismatch, a frozen count not
reproducing) writes an absence record (kind `refused`)
under the minted id and exits 1.

Usage (from anywhere; the repo root is derived from
this file's location):

    python3 tools/spec093/run_stage4_site.py run-administration --store <dir>
    python3 tools/spec093/run_stage4_site.py run-controls --store <dir>

Deterministic: comparable runs' result blocks agree
byte-for-byte. Statistics are computed in exact rational
arithmetic and emitted as floats (the Stage 2 lesson:
float summation order does not guarantee agreement
between independent implementations).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "backend"))

from glossa_lab import run_records as rr  # noqa: E402

TOOL = "run_stage4_site.py"
TOOL_VERSION = "1.0.0"
SPEC_DIR = "specs/093-material-context-channel"

SNAPSHOT_REL = "glossa-corpus/indus/exports/indus_research.jsonl"
SNAPSHOT_SHA256 = (
    "08fc96c8dbc22a37effb65e789b22b144f4baf22be1da55dc3d84db5dc44505e"
)
FREEZE_REL = f"{SPEC_DIR}/records/stage4-site-freeze-v1.md"
STAGE2_REL = f"{SPEC_DIR}/records/stage2-record-2026-11-19.md"
COUNTS_REL = f"{SPEC_DIR}/records/t201-counts-2026-11-19.json"

SITE_FLOOR = 50
POPULATION_TOTAL = 966
SITE_COUNTS = {
    "Mohenjo-daro": 839, "Harappa": 110, "Chanhu-Daro": 7,
    "Sutkagen-Dor": 6, "Lothal": 3, "Kalibangan": 1,
}
ADJUDGED = {"Harappa": 110, "Mohenjo-daro": 839}
ARM_SIZES = {
    "Harappa": {"discovery": 77, "held_out": 33},
    "Mohenjo-daro": {"discovery": 587, "held_out": 252},
}
SPLIT_SEED = 20261127
DISCOVERY_BATTERY_SEED = 20261128
HELDOUT_BATTERY_SEED = 20261129
PSEUDO_SEED = 20261130
N_PERMUTATIONS = 2000
N_PSEUDO = 200
P99_INDEX = 1979
P95_INDEX = 1899
PSEUDO_P95_INDEX = 189

SENTINELS = {"", "None", "-", "--"}


class Refusal(Exception):
    """A refusal the freeze names (run-defs v2 §3.2)."""


def _progress(msg: str) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"PROGRESS {now} {msg}", flush=True)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def is_empty(v) -> bool:
    if v is None:
        return True
    if isinstance(v, (list, dict)):
        return len(v) == 0
    if isinstance(v, str):
        return v.strip() in SENTINELS
    return False


def verify_pins() -> dict:
    snap_sha = sha256_file(ROOT / SNAPSHOT_REL)
    if snap_sha != SNAPSHOT_SHA256:
        raise Refusal(
            f"snapshot pin mismatch: computed {snap_sha}, "
            f"frozen {SNAPSHOT_SHA256}"
        )
    return {
        "spec": "093",
        "stage": "4",
        "freeze_record": FREEZE_REL,
        "freeze_record_sha256": sha256_file(ROOT / FREEZE_REL),
        "stage2_record": STAGE2_REL,
        "stage2_record_sha256": sha256_file(ROOT / STAGE2_REL),
        "counts_record": COUNTS_REL,
        "counts_record_sha256": sha256_file(ROOT / COUNTS_REL),
        "snapshot": {"path": SNAPSHOT_REL, "sha256": snap_sha},
    }


def population() -> list[dict]:
    items: list[dict] = []
    with (ROOT / SNAPSHOT_REL).open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            seq = rec.get("canonical_grapheme_ids")
            if not seq or is_empty(rec.get("site_name")):
                continue
            items.append({
                "id": rec["glossa_id"],
                "sequence": [str(c) for c in seq],
                "label": str(rec["site_name"]),
            })
    counts = Counter(it["label"] for it in items)
    if len(items) != POPULATION_TOTAL or dict(counts) != SITE_COUNTS:
        raise Refusal(
            f"P-site does not reproduce the freeze: total {len(items)}, "
            f"counts {dict(sorted(counts.items()))}"
        )
    return items


def adjudged(items: list[dict]):
    kept = {c: n for c, n in Counter(it["label"] for it in items).items()
            if n >= SITE_FLOOR}
    excluded = {c: n for c, n in Counter(it["label"] for it in items).items()
                if n < SITE_FLOOR}
    if kept != ADJUDGED:
        raise Refusal(f"adjudged sites {kept} do not reproduce the freeze")
    adj = [it for it in items if it["label"] in kept]
    return adj, dict(sorted(kept.items())), dict(sorted(excluded.items()))


def split(items: list[dict]):
    """Freeze §4: one Random(SPLIT_SEED) stream, sites in
    ascending label order, ids ascending, shuffled; the
    first floor(0.7n) of each site is the discovery arm."""
    rng = random.Random(SPLIT_SEED)
    by_site: dict[str, list[dict]] = {}
    for it in items:
        by_site.setdefault(it["label"], []).append(it)
    arms: dict[str, list[dict]] = {"discovery": [], "held_out": []}
    for label in sorted(by_site):
        group = sorted(by_site[label], key=lambda it: it["id"])
        ids = [it["id"] for it in group]
        rng.shuffle(ids)
        n_disc = (7 * len(ids)) // 10
        disc_ids = set(ids[:n_disc])
        for it in group:
            arms["discovery" if it["id"] in disc_ids else "held_out"].append(it)
    for label, sizes in ARM_SIZES.items():
        for arm, want in sizes.items():
            got = sum(1 for it in arms[arm] if it["label"] == label)
            if got != want:
                raise Refusal(
                    f"arm size mismatch: {label}/{arm} is {got}, frozen {want}"
                )
    return arms


def ks_statistic(a_lengths: list[int], b_lengths: list[int]) -> Fraction:
    """Two-sample KS distance, exact rational arithmetic."""
    ca, cb = Counter(a_lengths), Counter(b_lengths)
    na, nb = len(a_lengths), len(b_lengths)
    run_a = run_b = 0
    best = Fraction(0)
    for v in sorted(set(ca) | set(cb)):
        run_a += ca.get(v, 0)
        run_b += cb.get(v, 0)
        d = abs(Fraction(run_a, na) - Fraction(run_b, nb))
        if d > best:
            best = d
    return best


def tv_statistic(a_seqs: list[list[str]], b_seqs: list[list[str]]) -> Fraction:
    """Total variation distance between unigram
    distributions, exact rational arithmetic."""
    ca: Counter = Counter()
    cb: Counter = Counter()
    for s in a_seqs:
        ca.update(s)
    for s in b_seqs:
        cb.update(s)
    ta, tb = sum(ca.values()), sum(cb.values())
    total = Fraction(0)
    for g in set(ca) | set(cb):
        total += abs(Fraction(ca.get(g, 0), ta) - Fraction(cb.get(g, 0), tb))
    return total / 2


def arm_statistics(arm_items: list[dict]) -> dict:
    md = [it for it in arm_items if it["label"] == "Mohenjo-daro"]
    ha = [it for it in arm_items if it["label"] == "Harappa"]
    md_len = [len(it["sequence"]) for it in md]
    ha_len = [len(it["sequence"]) for it in ha]
    q1 = ks_statistic(md_len, ha_len)
    q2 = tv_statistic([it["sequence"] for it in md],
                      [it["sequence"] for it in ha])
    mean_md = Fraction(sum(md_len), len(md_len))
    mean_ha = Fraction(sum(ha_len), len(ha_len))
    return {
        "n_mohenjo_daro": len(md),
        "n_harappa": len(ha),
        "q1_ks": float(q1),
        "q2_tv": float(q2),
        "mean_length_mohenjo_daro": float(mean_md),
        "mean_length_harappa": float(mean_ha),
    }


def _git_head() -> str:
    proc = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
        capture_output=True, text=True, timeout=30, check=False,
    )
    sha = proc.stdout.strip()
    return sha if proc.returncode == 0 and sha else "unknown"


def _write(store: Path, command: str, seed: int,
           started: datetime, make_result) -> int:
    run_id = rr.mint_run_id("study", now=started)
    pins: dict = {}
    try:
        result = make_result(pins)
    except Refusal as exc:
        finished = datetime.now(timezone.utc).replace(microsecond=0)
        header = rr.build_header(
            surface="study", tool=TOOL, tool_version=TOOL_VERSION,
            command=command, code_version=_git_head(), input_pins=pins,
            seed=seed, environment_class="tower-compute/linux",
            started=started, finished=finished, run_id=run_id,
        )
        record = rr.build_record(
            header, absence={"kind": "refused", "detail": str(exc)})
        path = rr.write_run_record(store, record)
        print(f"refused: {exc}", file=sys.stderr)
        print(f"absence run record: {path} ({run_id})")
        return 1
    finished = datetime.now(timezone.utc).replace(microsecond=0)
    header = rr.build_header(
        surface="study", tool=TOOL, tool_version=TOOL_VERSION,
        command=command, code_version=_git_head(), input_pins=pins,
        seed=seed, environment_class="tower-compute/linux",
        started=started, finished=finished, run_id=run_id,
    )
    record = rr.build_record(header, result=result)
    path = rr.write_run_record(store, record)
    print(f"run record: {path} ({run_id})")
    return 0


def run_administration(store: Path) -> int:
    started = datetime.now(timezone.utc).replace(microsecond=0)

    def make(pins: dict):
        pins.update(verify_pins())
        items = population()
        adj, kept, excluded = adjudged(items)
        arms = split(adj)
        return {
            "spec": "093", "stage": "4", "task": "T401",
            "kind": "administration",
            "population": len(items),
            "adjudged_classes": kept,
            "excluded_classes": excluded,
            "adjudged_total": len(adj),
            "arms": {name: arm_statistics(arms[name])
                     for name in ("discovery", "held_out")},
        }

    return _write(store, "run-administration", SPLIT_SEED, started, make)


def _battery(arm_items: list[dict], seed: int, tag: str):
    """Permutation battery over one arm: labels shuffled
    in id order under one stream; both statistics per
    draw. Returns sorted exact values as floats plus the
    frozen percentile reads."""
    ids_sorted = sorted(it["id"] for it in arm_items)
    by_id = {it["id"]: it for it in arm_items}
    labels = [by_id[i]["label"] for i in ids_sorted]
    rng = random.Random(seed)
    q1_vals: list[Fraction] = []
    q2_vals: list[Fraction] = []
    for draw in range(N_PERMUTATIONS):
        permuted = list(labels)
        rng.shuffle(permuted)
        md = [by_id[i] for i, lab in zip(ids_sorted, permuted)
              if lab == "Mohenjo-daro"]
        ha = [by_id[i] for i, lab in zip(ids_sorted, permuted)
              if lab == "Harappa"]
        q1_vals.append(ks_statistic([len(it["sequence"]) for it in md],
                                    [len(it["sequence"]) for it in ha]))
        q2_vals.append(tv_statistic([it["sequence"] for it in md],
                                    [it["sequence"] for it in ha]))
        if (draw + 1) % 500 == 0:
            _progress(f"battery {tag}: {draw + 1}/{N_PERMUTATIONS} draws")
    q1_sorted = sorted(q1_vals)
    q2_sorted = sorted(q2_vals)
    return {
        "n_permutations": N_PERMUTATIONS,
        "q1_values": [float(v) for v in q1_sorted],
        "q2_values": [float(v) for v in q2_sorted],
        "q1_p99_index1979": float(q1_sorted[P99_INDEX]),
        "q1_p95_index1899": float(q1_sorted[P95_INDEX]),
        "q2_p99_index1979": float(q2_sorted[P99_INDEX]),
        "q2_p95_index1899": float(q2_sorted[P95_INDEX]),
    }


def run_controls(store: Path) -> int:
    started = datetime.now(timezone.utc).replace(microsecond=0)

    def make(pins: dict):
        pins.update(verify_pins())
        items = population()
        adj, kept, _excluded = adjudged(items)
        arms = split(adj)
        disc = _battery(arms["discovery"], DISCOVERY_BATTERY_SEED, "discovery")
        held = _battery(arms["held_out"], HELDOUT_BATTERY_SEED, "held-out")
        # Pseudo-site negative control (freeze §5): within
        # the Mohenjo-daro discovery records only.
        md_disc = sorted(
            (it for it in arms["discovery"] if it["label"] == "Mohenjo-daro"),
            key=lambda it: it["id"],
        )
        rng = random.Random(PSEUDO_SEED)
        pq1: list[Fraction] = []
        pq2: list[Fraction] = []
        for draw in range(N_PSEUDO):
            pool = list(md_disc)
            rng.shuffle(pool)
            pseudo_ha, pseudo_md = pool[:77], pool[77:]
            pq1.append(ks_statistic(
                [len(it["sequence"]) for it in pseudo_md],
                [len(it["sequence"]) for it in pseudo_ha]))
            pq2.append(tv_statistic(
                [it["sequence"] for it in pseudo_md],
                [it["sequence"] for it in pseudo_ha]))
            if (draw + 1) % 50 == 0:
                _progress(f"pseudo-site control: {draw + 1}/{N_PSEUDO} draws")
        pq1_sorted, pq2_sorted = sorted(pq1), sorted(pq2)
        return {
            "spec": "093", "stage": "4", "task": "T401",
            "kind": "permutation-controls",
            "adjudged_classes": kept,
            "discovery_battery": disc,
            "held_out_battery": held,
            "pseudo_site_control": {
                "n_draws": N_PSEUDO,
                "pseudo_harappa_size": 77,
                "q1_values": [float(v) for v in pq1_sorted],
                "q2_values": [float(v) for v in pq2_sorted],
                "q1_p95_index189": float(pq1_sorted[PSEUDO_P95_INDEX]),
                "q2_p95_index189": float(pq2_sorted[PSEUDO_P95_INDEX]),
            },
        }

    return _write(store, "run-controls", DISCOVERY_BATTERY_SEED, started, make)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Spec 093 Stage 4 (T401): the frozen site pass.")
    sub = parser.add_subparsers(dest="subcommand", required=True)
    for name in ("run-administration", "run-controls"):
        p = sub.add_parser(name)
        p.add_argument("--store", required=True, type=Path)
    args = parser.parse_args(argv)
    if args.subcommand == "run-administration":
        return run_administration(args.store)
    return run_controls(args.store)


if __name__ == "__main__":
    raise SystemExit(main())
