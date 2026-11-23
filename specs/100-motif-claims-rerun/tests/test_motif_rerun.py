"""Spec 100 — test cases TC-100-01..TC-100-10.

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
import os
import shutil
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



def _record_run(root, deposit=None, record=None, out=None):
    cmd = [sys.executable, str(TOOLS / "motif_rerun.py"),
           "--mode", "record", "--root", str(root)]
    if deposit is not None:
        cmd += ["--deposit", str(deposit)]
    if record is not None:
        cmd += ["--deposit-record", str(record)]
    if out is not None:
        cmd += ["--out", str(out)]
    return subprocess.run(cmd, capture_output=True, text=True)


def _simulated_tree(tmp_path):
    """A temp repo tree: real population files symlinked in,
    a header-only deposit at the registered path, and a
    deposit record stating its hash + a granting basis."""
    root = tmp_path / "repo"
    (root / "outputs").mkdir(parents=True)
    for name in ("phase100_full_corpus.json",
                 "phase114_full_seal_translations.json"):
        os.symlink(ROOT / "outputs" / name, root / "outputs" / name)
    dep_rel = Path("specs/100-motif-claims-rerun/records/iconography-deposit-v1.csv")
    dep = root / dep_rel
    dep.parent.mkdir(parents=True)
    dep.write_text("cisi_id,iconography\n", encoding="utf-8")
    digest = hashlib.sha256(dep.read_bytes()).hexdigest()
    rec_rel = "specs/100-motif-claims-rerun/records/deposit-record-fixture.md"
    rec = root / rec_rel
    return root, dep, rec_rel, rec, digest


def _write_record(rec, digest, basis_line):
    rec.write_text(f"# fixture deposit record\nSHA-256: {digest}\n{basis_line}\n",
                   encoding="utf-8")


GRANT_LINE = ("Permission basis: Miller reply of record grants "
              "permission for the statistics-and-deposit basis.")


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



def test_tc100_01_foreign_deposit_and_bogus_citation_refused(tmp_path):
    """RT6-C2: an existing foreign CSV + any citation string does
    NOT open the gate; neither does a registered-path deposit
    with a bogus citation / hash-less / refusal record."""
    out = tmp_path / "outcome.json"
    foreign = tmp_path / "foreign.csv"
    foreign.write_text("cisi_id,iconography\nX-1,tiger\n", encoding="utf-8")
    proc = _record_run(ROOT, deposit=foreign, record="any citation string", out=out)
    assert proc.returncode == 3 and "GATE CLOSED" in proc.stdout
    assert not out.exists()

    root, dep, rec_rel, rec, digest = _simulated_tree(tmp_path)
    # bogus citation: no such in-tree record file
    proc = _record_run(root, deposit=dep, record="specs/100-motif-claims-rerun/records/nope.md", out=out)
    assert proc.returncode == 3 and "GATE CLOSED" in proc.stdout and not out.exists()
    # record file without the deposit's SHA-256
    _write_record(rec, "0" * 64, GRANT_LINE)
    proc = _record_run(root, deposit=dep, record=rec_rel, out=out)
    assert proc.returncode == 3 and "GATE CLOSED" in proc.stdout and not out.exists()
    # record file with correct hash but a refusal basis line
    _write_record(rec, digest, "Permission basis: Miller reply refuses permission.")
    proc = _record_run(root, deposit=dep, record=rec_rel, out=out)
    assert proc.returncode == 3 and "GATE CLOSED" in proc.stdout and not out.exists()


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
    refuses a non-pinned source even under its own hash
    (RT6-H3); the schema leg is checked via extract()."""
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

    # RT6-H3: a non-pinned source is refused even with its own
    # hash as --pin (the pin is no longer caller-supplied).
    own = hashlib.sha256(src.read_bytes()).hexdigest()
    assert own != de.PIN_OF_RECORD and len(de.PIN_OF_RECORD) == 64
    proc = subprocess.run(
        [sys.executable, str(TOOLS / "deposit_extract.py"),
         "--source", str(src), "--pin", own, "--out", str(out)],
        capture_output=True, text=True)
    assert proc.returncode == 2
    assert "PIN MISMATCH" in proc.stdout
    assert not out.exists()
    # No --pin: the embedded constant is used; same refusal.
    proc = subprocess.run(
        [sys.executable, str(TOOLS / "deposit_extract.py"),
         "--source", str(src), "--out", str(out)],
        capture_output=True, text=True)
    assert proc.returncode == 2
    assert "PIN MISMATCH" in proc.stdout
    assert not out.exists()
    # Schema leg as a direct extract() unit check.
    seals = de.extract(src)
    assert seals == {"X-0002": "tiger", "X-0001": ""}


def test_tc100_07_no_standing_change_without_adjudication(tmp_path):
    """C100-4: a gate-opening rerun outcome carries no standing,
    ledger, or register change, and mutates no package file."""
    watched = [SPEC_DIR / "claims.md", SPEC_DIR / "spec.md"]
    before = {f: hashlib.sha256(f.read_bytes()).hexdigest() for f in watched}
    root, dep, rec_rel, rec, digest = _simulated_tree(tmp_path)
    _write_record(rec, digest, GRANT_LINE)
    out = tmp_path / "outcome.json"
    proc = _record_run(root, deposit=dep, record=rec_rel, out=out)
    assert proc.returncode == 0, proc.stdout
    outcome = json.loads(out.read_text(encoding="utf-8"))
    flat = json.dumps(outcome).lower()
    for forbidden in ("standing", "ledger", "register"):
        assert forbidden not in flat
    after = {f: hashlib.sha256(f.read_bytes()).hexdigest() for f in watched}
    assert before == after


def test_tc100_08_proof_banner_and_synthetic_labels(tmp_path):
    """C100-7: proof mode carries the banner and uses only the
    deterministic synthetic label set."""
    out = tmp_path / "proof.json"
    proc = subprocess.run(
        [sys.executable, str(TOOLS / "motif_rerun.py"),
         "--mode", "proof", "--root", str(ROOT), "--out", str(out)],
        capture_output=True, text=True)
    assert proc.returncode == 0
    assert "PROOF - NOT A RESULT" in proc.stdout
    assert "PROOF - NOT A RESULT" in out.read_text(encoding="utf-8")
    pop = mr.load_population_a(ROOT / "outputs" / "phase100_full_corpus.json")
    labels = mr.synthetic_labels(pop)
    assert set(labels.values()) <= set(mr.PROOF_ICONS)
    assert all(v.startswith("synthetic-") for v in labels.values())


def test_tc100_09_miller_reply_trigger_states(tmp_path):
    """C100-6: grant opens the mechanical gate; refusal and
    silence keep it closed (exit 3)."""
    out = tmp_path / "outcome.json"
    # grant -> gate opens, record mode proceeds
    root, dep, rec_rel, rec, digest = _simulated_tree(tmp_path / "grant")
    _write_record(rec, digest, GRANT_LINE)
    proc = _record_run(root, deposit=dep, record=rec_rel, out=out)
    assert proc.returncode == 0, proc.stdout
    # refusal -> gate closed
    root, dep, rec_rel, rec, digest = _simulated_tree(tmp_path / "refusal")
    _write_record(rec, digest, "Permission basis: Miller reply refuses permission.")
    proc = _record_run(root, deposit=dep, record=rec_rel, out=out)
    assert proc.returncode == 3 and "GATE CLOSED" in proc.stdout
    # silence -> gate closed (basis line recording silence)
    root, dep, rec_rel, rec, digest = _simulated_tree(tmp_path / "silence")
    _write_record(rec, digest, "Permission basis: silence to date; no reply received.")
    proc = _record_run(root, deposit=dep, record=rec_rel, out=out)
    assert proc.returncode == 3 and "GATE CLOSED" in proc.stdout
    # silence -> no basis line at all
    root, dep, rec_rel, rec, digest = _simulated_tree(tmp_path / "none")
    rec.write_text(f"# fixture\nSHA-256: {digest}\n", encoding="utf-8")
    proc = _record_run(root, deposit=dep, record=rec_rel, out=out)
    assert proc.returncode == 3 and "GATE CLOSED" in proc.stdout


def test_tc100_10_negated_grant_refused(tmp_path):
    """RT7-L1: a negation-bearing basis line is refused even
    when it contains a granting term (Round 7 case E:
    "Miller grants nothing in this reply." opened the gate
    before this hardening). The gate must refuse, exit 3,
    GATE CLOSED, and write no outcome."""
    out = tmp_path / "outcome.json"
    # Round 7 case E, verbatim
    root, dep, rec_rel, rec, digest = _simulated_tree(tmp_path / "neg1")
    _write_record(rec, digest,
                  "Permission basis: Miller grants nothing in this reply.")
    proc = _record_run(root, deposit=dep, record=rec_rel, out=out)
    assert proc.returncode == 3 and "GATE CLOSED" in proc.stdout
    assert not out.exists()
    # granted-to-no-one variant
    root, dep, rec_rel, rec, digest = _simulated_tree(tmp_path / "neg2")
    _write_record(rec, digest,
                  "Permission basis: permission is granted to no one "
                  "pending review.")
    proc = _record_run(root, deposit=dep, record=rec_rel, out=out)
    assert proc.returncode == 3 and "GATE CLOSED" in proc.stdout
    assert not out.exists()
