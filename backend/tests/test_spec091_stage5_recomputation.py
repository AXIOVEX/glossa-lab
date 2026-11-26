"""Tests for backend/scripts/spec091_stage5_recomputation.py.

Scope: run-id minting only. Run-defs v3 section 2 (D-089-1) requires a
run id of the form <surface>-<yyyymmddThhmmssZ>-<6 lowercase hex>, with
the trailing component drawn from a cryptographic random source at
minting time: an id names an execution, never its content, and two
executions with identical inputs carry different ids. The script's
earlier minting derived the suffix from a hash of the input pins, so
identical inputs at the same second would have collided; these tests
pin the corrected behaviour.
"""
import importlib.util
import pathlib
import re
from datetime import datetime, timezone

SCRIPT = (pathlib.Path(__file__).resolve().parents[1]
          / "scripts" / "spec091_stage5_recomputation.py")

_spec = importlib.util.spec_from_file_location(
    "spec091_stage5_recomputation", SCRIPT)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)

RUN_ID_RE = re.compile(r"^study-\d{8}T\d{6}Z-[0-9a-f]{6}$")
FIXED_START = datetime(2026, 11, 24, 9, 45, 45, tzinfo=timezone.utc)


def test_mint_run_id_format():
    run_id = mod.mint_run_id(FIXED_START)
    assert RUN_ID_RE.match(run_id), run_id
    assert run_id.startswith("study-20261124T094545Z-"), run_id


def test_mint_run_id_suffixes_are_distinct_at_a_fixed_timestamp():
    ids = {mod.mint_run_id(FIXED_START) for _ in range(50)}
    assert len(ids) == 50
    for run_id in ids:
        assert RUN_ID_RE.match(run_id), run_id
