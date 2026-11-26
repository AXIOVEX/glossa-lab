#!/usr/bin/env python3
"""Spec 103, Stage 2 execution (witness completion for asoreyi),
executed 2026-11-26 under records/stage-2-registration-2026-11-26.md.

What this script does, in order:
  1. Verifies the three custody REM tome PDFs against the SHA-256
     values registered in the Stage 2 registration (TC-103-12).
  2. Control: re-runs the conformance addendum's filed script
     untouched (staging the two input files at the repo path the
     script hardcodes, from its original execution clone) and
     asserts its regenerated results are deep-equal to the filed
     addendum results, byte for byte (Step 1 equality, the 41
     witness-covered loci under the corrected checker, and the
     corrected Step 4 table all reproduce).
  3. Applies the corrected checker to the six loci filed WITNESS
     UNAVAILABLE in Stage 1, with the Stage 2 witness set: the REM
     witness data (records/stage-2-witness-data-2026-11-26.json),
     which records that none of the eight REM entries prints a
     transliteration, so the REM witness token stream is empty for
     every one of the eight texts.
  4. Completeness scan (registration section 4.5): operates on the
     transcribed REM token streams; there are none, so the scan is
     vacuous and the extraction-side census stands untouched.
  5. Restates the six-form table whole and reads the kill check.
  6. Writes records/stage-2-results-2026-11-26.json.

Progress: timestamped progress lines with step counters are printed
as the run proceeds (fleet rule, 2026-11-26). The final line is the
payload verdict.
"""
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
CUSTODY = Path.home() / ".syncyard/worktrees/glossa/glossa-custody/spec103"
SCRATCH = Path.home() / ".syncyard/worktrees/glossa/s103-stage2-scratch/control-replay"
TOTAL_STEPS = 6

CUSTODY_HASHES = {
    "rem-tome-1-rem0001-0387.pdf":
        "f20d9f955ff2a74d391d894f65958c3d2848d5282a26a5c5ba5ae70dd591afce",
    "rem-tome-2-rem0401-0851.pdf":
        "55b13325bad738b8e2e53b3fc41f8340162625c8c5a2a3e982da811115dff167",
    "rem-tome-3-rem1001-1278.pdf":
        "cc24ffe691c6522b71cc56cc812554c41786fe0654742abed4238bbcb5ebe6a1",
}

REM_OF_TEXT = {
    "Sh. 9": "REM 0376", "Sh. 16": "REM 0383", "Meroe 40": "REM 0440",
    "F.O. 7": "REM 0557", "F.O. 17": "REM 0567", "F.O. 29": "REM 0579",
    "F.O. 39": "REM 0589", "B.O. 1": "REM 0591",
}


def progress(step, msg):
    ts = time.strftime("%H:%M:%SZ", time.gmtime())
    print(f"[{ts}] progress {step}/{TOTAL_STEPS}: {msg}", flush=True)


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    results = {"stage": "Spec 103 Stage 2 (witness completion)",
               "date": "2026-11-26",
               "registration": "records/stage-2-registration-2026-11-26.md"}

    # ---- Step 1: custody hashes -------------------------------------
    progress(1, "verifying custody tome hashes against the registration")
    got = {name: sha256(CUSTODY / name) for name in CUSTODY_HASHES}
    assert got == CUSTODY_HASHES, f"custody hash mismatch: {got}"
    results["custody_hashes_verified"] = got
    progress(1, "custody hashes verified (3/3 match)")

    # ---- Step 2: control replay of the corrected checker ------------
    progress(2, "control: replaying the conformance addendum script")
    # The filed addendum script hardcodes the repo path of the clone it
    # was executed in (sw103-addendum, since deleted) and reads two
    # input files from it. The replay therefore stages those two inputs,
    # byte-copied from this clone, at that exact path, runs the filed
    # script untouched from this records directory, and removes the
    # staging afterwards. The script rewrites its own results file in
    # place; the filed bytes are captured first and the regenerated
    # results must be deep-equal to them.
    repo_stage = Path.home() / ".syncyard/worktrees/glossa/sw103-addendum"
    assert not repo_stage.exists(), "sw103-addendum staging path already exists"
    clone_root = BASE.parents[2]
    for rel in ("specs/097-meroitic-reproduction-benchmark/records/"
                "stage-4-4-results.json",
                "specs/103-meroitic-source-witness-check/records/"
                "stage-1-results-2026-11-23.json"):
        dst = repo_stage / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(clone_root / rel, dst)
    filed_path = BASE / "conformance-addendum-results-2026-11-25.json"
    filed_bytes = filed_path.read_bytes()
    filed = json.loads(filed_bytes)
    try:
        proc = subprocess.run(
            [sys.executable, str(BASE / "conformance-addendum-script.py")],
            capture_output=True, text=True)
        assert proc.returncode == 0, \
            f"addendum replay failed: {proc.stderr[-2000:]}"
    finally:
        shutil.rmtree(repo_stage)
    replayed = json.loads(filed_path.read_text())
    assert filed_path.read_bytes() == filed_bytes, \
        "addendum replay changed the filed results bytes"
    assert replayed == filed, "control replay differs from the filed addendum results"
    all_loci = [l for r in replayed["forms"].values()
                for l in r["counted_loci"] + r["near_form_census"]]
    covered = [l for l in all_loci
               if l["corrected_classification"] != "WITNESS UNAVAILABLE"]
    assert len(all_loci) == 47 and len(covered) == 41, \
        f"control locus census off: {len(all_loci)} total, {len(covered)} covered"
    assert replayed["diff"] == [] and replayed["control_mismatches"] == []
    results["control"] = {
        "addendum_replay_deep_equal_to_filed": True,
        "addendum_replay_bytes_identical": True,
        "loci_reproduced": len(all_loci),
        "witness_covered_loci_reproduced": len(covered),
        "step1_equality_asserted_inside_replay": True,
    }
    progress(2, f"control PASS: replay deep-equal; {len(covered)}/47 loci "
                "reproduced under the corrected checker")

    # ---- Step 3: the six loci under the Stage 2 witness set ---------
    progress(3, "applying the corrected checker to the six WITNESS UNAVAILABLE loci")
    chk = load_module(BASE / "conformance-addendum-script.py", "checker103")
    stage1 = json.loads((BASE / "stage-1-results-2026-11-23.json").read_text())
    witness_data = json.loads(
        (BASE / "stage-2-witness-data-2026-11-26.json").read_text())
    wd = {t["short_name"]: t for t in witness_data["texts"]}
    assert len(wd) == 8
    assert all(t["transliteration_printed_in_entry"] is False
               and t["witness_token_stream"] is None for t in wd.values()), \
        "witness data must record no printed transliteration for all eight texts"

    loci_out = []
    for form, fr in stage1["forms"].items():
        for kind, key in (("counted", "counted_loci"),
                          ("near", "near_form_census")):
            for loc in fr[key]:
                if loc["classification"] != "WITNESS UNAVAILABLE":
                    continue
                text = loc["rem"]
                token = form if kind == "counted" else loc["token"]
                # The REM witness verdict set for this text is empty:
                # the entry prints no transliteration, so there is no
                # REM token stream and no witness verdict (witness
                # data, step 3 input). The corrected checker's
                # aggregation over an empty witness set is WITNESS
                # UNAVAILABLE, as filed in Stage 1.
                if kind == "counted":
                    cls = chk.classify_counted_corrected({}, form)[0]
                else:
                    cls = chk.classify_near_corrected({}, form, token)[0]
                loci_out.append({
                    "form": form, "kind": kind, "text": text,
                    "token": token,
                    "rem_entry": REM_OF_TEXT[text],
                    "rem_transliteration_printed": False,
                    "classification_stage2": cls,
                    "classification_stage1": "WITNESS UNAVAILABLE",
                })
    assert len(loci_out) == 6, f"expected 6 in-scope loci, got {len(loci_out)}"
    assert all(l["classification_stage2"] == "WITNESS UNAVAILABLE"
               for l in loci_out)
    results["stage2_loci"] = loci_out
    progress(3, "six loci classified under the completed witness set: "
                "all six remain WITNESS UNAVAILABLE (no REM transliteration exists)")

    # ---- Step 4: completeness scan ----------------------------------
    progress(4, "completeness scan over the REM token streams")
    results["completeness_scan"] = {
        "streams_scanned": 0,
        "note": "No REM transliteration token streams exist for any of the "
                "eight texts (no entry prints one), so the section 4.5 scan "
                "has nothing to scan; the extraction-side census stands "
                "exactly as filed.",
    }
    progress(4, "scan vacuous: 0 streams; extraction census untouched")

    # ---- Step 5: restated table and kill check ----------------------
    progress(5, "restating the six-form table; reading the kill check")
    results["step4_restated"] = {
        form: {"frozen_counts": r["frozen"],
               "corrected_counts": r["corrected_step4"],
               "outcome_stage2": r["corrected_outcome"]}
        for form, r in replayed["forms"].items()}
    assert results["step4_restated"]["asoreyi"]["outcome_stage2"] == \
        "NOT CHECKED - INCOMPLETE COVERAGE"
    assert all(v["outcome_stage2"] == "CLAIM STANDS"
               for k, v in results["step4_restated"].items() if k != "asoreyi")
    results["kill_check"] = {
        "discrepancies_demonstrated_stage2": 0,
        "claim_killed_for_any_form": False,
        "reading": "No discrepancy is demonstrated at any locus under "
                   "Stage 2: the six open loci received no witness "
                   "evidence, because the witness does not exist in the "
                   "registered form. For asoreyi the claim is neither "
                   "stood nor killed; the input-error explanation is not "
                   "retired for asoreyi, and the outcome is NOT CHECKED - "
                   "INCOMPLETE COVERAGE on the new ground that the held "
                   "edition of record carries no transliteration witness "
                   "for Sh. 9 or Sh. 16.",
    }
    results["test_cases"] = {
        "TC-103-11": "PASS (registration commit precedes this execution "
                     "commit in the branch history)",
        "TC-103-12": "PASS (custody hashes match; addendum replay "
                     "deep-equal to the filed results)",
        "TC-103-13": "PASS with two annotations filed in the outcome "
                     "record (REM 0440 chapter label; plate pages)",
        "TC-103-14": "NOT APPLICABLE (no locus classification rests on a "
                     "REM token; no REM transliteration exists)",
        "TC-103-15": "PASS (no pooling; no corrections of any kind)",
        "TC-103-16": "PASS (one section-4 outcome per form; no Stage 4.4 "
                     "score, verdict, or tally stated or changed)",
    }
    progress(5, "table restated: 5 CLAIM STANDS; asoreyi NOT CHECKED - "
                "INCOMPLETE COVERAGE; kill check: not fired")

    # ---- Step 6: write results --------------------------------------
    progress(6, "writing stage-2 results")
    out = BASE / "stage-2-results-2026-11-26.json"
    out.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    progress(6, f"wrote {out.name}")
    print("PAYLOAD VERDICT: STAGE 2 EXECUTED - asoreyi NOT CHECKED - "
          "INCOMPLETE COVERAGE (witness held, no transliteration in the "
          "edition for Sh. 9 / Sh. 16); five forms CLAIM STANDS unchanged; "
          "kill check not fired", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
