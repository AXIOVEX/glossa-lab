"""Spec 100 — test cases TC-100-01..TC-100-06.

Implemented against the pipeline of record
(`tools/motif_rerun.py`, `tools/deposit_extract.py`).
Fixtures are synthetic, except TC-100-04, which runs the
marginals leg over the repository's real tracked population
files (no labels of any kind are read by any test; TC-100-04
computes sign marginals only, replicating PR #634's counts).

Run from the repository root:
    python3 -m pytest specs/100-motif-claims-rerun/tests/ -q
The pytest process exit code is the payload verdict.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

SPEC_DIR = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[3]
TOOLS = SPEC_DIR / "tools"


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mr = _load("motif_rerun")
de = _load("deposit_extract")

# PR #634's replicated sign marginals (seals bearing the sign,
# population 1,670), the values TC-100-04 must reproduce.
MARGINALS_634 = {
    "M006": 15, "M013": 23, "M016": 23, "M039": 18, "M045": 24,
    "M057": 18, "M060": 20, "M062": 28, "M063": 18, "M067": 15,
    "M068": 13, "M073": 25, "M080": 19,
}


def test_tc100_01_gate_closed_without_deposit(tmp_path):
    """C100-1: record mode without a deposit refuses, exit 3,
    GATE CLOSED, and writes no outcome."""
    out = tmp_path / "outcome.json"
    proc = subprocess.run(
        [sys.executable, str(TOOLS / "motif_rerun.py"),
         "--mode", "record", "--root", str(ROOT), "--out", str(out)],
        capture_output=True, text=True)
    assert proc.returncode == 3
    assert "GATE CLOSED" in proc.stdout
    assert not out.exists()
    # A deposit path that does not exist is equally closed.
    proc = subprocess.run(
        [sys.executable, str(TOOLS / "motif_rerun.py"),
         "--mode", "record", "--root", str(ROOT),
         "--deposit", str(tmp_path / "no-such-deposit.csv"),
         "--deposit-record", "fixture", "--out", str(out)],
        capture_output=True, text=True)
    assert proc.returncode == 3
    assert "GATE CLOSED" in proc.stdout
    assert not out.exists()


def test_tc100_02_fixture_arithmetic():
    """C100-2/C100-3: cells, lift, odds ratio and verdicts on a
    hand-computed fixture, including the strict > 5.0 boundary."""
    pop = {f"U{i:02d}": [] for i in range(1, 21)}
    for cid in ("U01", "U02"):
        pop[cid].append("M006")          # M006: a=2,b=0,c=2,d=16
    for cid in ("U01", "U02", "U03", "U05"):
        pop[cid].append("M080")          # M080: a=3,b=1,c=1,d=15
    for cid in ("U01", "U02"):
        pop[cid].append("M013")          # M013: a=2,b=0,c=0,d=18
    labels = {cid: "" for cid in pop}
    for cid in ("U01", "U02", "U03", "U04"):
        labels[cid] = "tiger"
    for cid in ("U01", "U02"):
        labels[cid] = "tiger and gharial"

    row = mr.compute_claim(pop, labels, mr.CLAIMS[0])   # M006 tiger
    assert (row["a"], row["b"], row["c"], row["d"]) == (2, 0, 2, 16)
    assert row["lift"] == 5.0            # exactly at the bar
    assert row["verdict"] == "NOT REPRODUCED"   # the bar is strict: > 5.0
    assert row["odds_ratio"] is None     # b == 0

    row = mr.compute_claim(pop, labels,
                           next(c for c in mr.CLAIMS if c["sign"] == "M080"))
    assert (row["a"], row["b"], row["c"], row["d"]) == (3, 1, 1, 15)
    assert row["lift"] == 3.75
    assert row["odds_ratio"] == 45.0
    assert row["verdict"] == "NOT REPRODUCED"

    row = mr.compute_claim(pop, labels,
                           next(c for c in mr.CLAIMS if c["sign"] == "M013"))
    assert (row["a"], row["b"], row["c"], row["d"]) == (2, 0, 0, 18)
    assert row["lift"] == 10.0
    assert row["verdict"] == "REPRODUCED"
    assert row["odds_ratio"] is None     # b == c == 0


def test_tc100_03_filed_lift_calibration():
    """C100-2: the frozen lift formula reproduces the only filed
    lift value in the record — M063's corrected fragment
    (3 of 18 gharial seals, lift 4.35 against the 5.0 bar)."""
    pop = {f"F{i:04d}": [] for i in range(1, 1671)}
    labels = {cid: "" for cid in pop}
    sign_seals = [f"F{i:04d}" for i in range(1, 19)]          # 18 seals
    gharial = sign_seals[:3] + [f"F{i:04d}" for i in range(19, 80)]  # 64
    for cid in sign_seals:
        pop[cid].append("M063")
    for cid in gharial:
        labels[cid] = "gharial"
    row = mr.compute_claim(pop, labels,
                           next(c for c in mr.CLAIMS if c["sign"] == "M063"))
    assert (row["a"], row["b"], row["c"], row["d"]) == (3, 15, 61, 1591)
    assert round(row["lift"], 2) == 4.35
    assert row["verdict"] == "NOT REPRODUCED"


def test_tc100_04_marginals_replication():
    """C100-3: over the real tracked population files, both paths
    give the 1,670-seal population and PR #634's replicated sign
    marginals for all 13 signs. No labels are read."""
    pop_a = mr.load_population_a(ROOT / "outputs" / "phase100_full_corpus.json")
    pop_b = mr.load_population_b(
        ROOT / "outputs" / "phase114_full_seal_translations.json")
    assert len(pop_a) == 1670 and len(pop_b) == 1670
    for sign, expected in MARGINALS_634.items():
        ma = sum(1 for s in pop_a.values() if sign in s)
        mb = sum(1 for s in pop_b.values() if sign in s)
        assert ma == expected and mb == expected, sign


def test_tc100_05_missing_label_handling():
    """C100-5: seals with no deposit row are excluded from every
    cell and the denominator is restated; an empty iconography
    row is a recorded no-motif label; nothing is imputed."""
    pop = {f"V{i}": (["M006"] if i <= 4 else []) for i in range(1, 11)}
    labels = {f"V{i}": "" for i in range(1, 8)}       # V8..V10 missing
    labels["V1"] = "tiger"
    labels["V2"] = "tiger"
    row = mr.compute_claim(pop, labels, mr.CLAIMS[0])
    assert row["n_labeled"] == 7
    assert row["a"] + row["b"] + row["c"] + row["d"] == 7
    assert (row["a"], row["b"], row["c"], row["d"]) == (2, 2, 0, 3)
    assert row["n_population"] == 10
    # A deposit row keyed outside the population is a defect,
    # and the run's outcome is the defect, not a table.
    bad = dict(labels)
    bad["V99"] = "tiger"
    try:
        mr.run(pop, pop, bad, mode="record", deposit_record="fixture")
    except mr.DepositDefect:
        pass
    else:
        raise AssertionError("out-of-population deposit row not raised")


def test_tc100_06_extractor_pin_and_schema(tmp_path):
    """C100-1/C100-6: the deposit extractor refuses a source
    whose SHA-256 is not the pin (exit 2, nothing written) and
    extracts a schema-correct source under its true pin, one
    row per seal, iconography from the seal's first row."""
    src = tmp_path / "source.csv"
    src.write_text(
        "cisi_number,position,letters,iconography,site\n"
        "X-0002,0,M006,Tiger,Harappa\n"
        "X-0002,1,M080,Tiger,Harappa\n"
        "X-0001,0,M013,,Mohenjo-daro\n",
        encoding="utf-8")
    out = tmp_path / "deposit.csv"
    proc = subprocess.run(
        [sys.executable, str(TOOLS / "deposit_extract.py"),
         "--source", str(src), "--pin", "0" * 64, "--out", str(out)],
        capture_output=True, text=True)
    assert proc.returncode == 2
    assert "PIN MISMATCH" in proc.stdout
    assert not out.exists()

    pin = hashlib.sha256(src.read_bytes()).hexdigest()
    proc = subprocess.run(
        [sys.executable, str(TOOLS / "deposit_extract.py"),
         "--source", str(src), "--pin", pin, "--out", str(out)],
        capture_output=True, text=True)
    assert proc.returncode == 0
    rows = out.read_text(encoding="utf-8").strip().splitlines()
    assert rows[0] == "cisi_id,iconography"
    assert rows[1] == "X-0001,"
    assert rows[2] == "X-0002,tiger"
