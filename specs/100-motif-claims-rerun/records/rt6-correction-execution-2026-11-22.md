# Spec 100 — Red Team Round 6 Correction Execution Record (2026-11-22)

This record executes the Round 6 correction round for
findings RT6-C2, RT6-H3, RT6-M7, and RT6-M8. It changes
enforcement and text only: no standing, verdict, or tally
changes; no deposit exists and none was created; the
study remains gated on Miller's reply.

## Gate state today (explicit confirmation)

- Record mode against the real repository root with no
  deposit: **payload exit 3, GATE CLOSED** — nothing was
  computed. The gate is closed today.
- Record mode with a foreign CSV and any citation string:
  **payload exit 3, GATE CLOSED** (RT6-C2).
- Proof mode against the real root: **payload exit 0**,
  synthetic labels only, banner "PROOF - NOT A RESULT"
  verified present in its output. The proof output filed
  with this package (`records/proof-run-2026-11-22.json`
  and `records/proof-run-2026-11-22.log`, copied from
  custody at `~/glossa-custody/spec100/` on tower-compute,
  the path stated in `records/tc-execution-2026-11-22.md`)
  carries the banner (verified present in both files);
  synthetic data only. The .log file is force-added past
  the repo's `*.log` ignore rule so both files persist.

## Pin of record (RT6-H3)

Full pin: `62d14d2bebf7c2c80d98a2958e75ec52bff3f240ff3f5e85d1f7f40cbe28218e`
(64 hex characters), extracted from the primary in-tree
record `reports/phase422_results.json` (the T303 build
record; the pin also appears in `reports/phase422_report.md`
and `reports/phase409_results.json`). It is now embedded
as `PIN_OF_RECORD` in `tools/deposit_extract.py`.

## Test executions (tower-compute, payload exit codes)

Each pytest case was run individually; the pytest process
exit code is the payload verdict. All exit 0 (pass):

| Case | Exit |
|---|---|
| TC-100-01 gate closed without deposit | 0 |
| TC-100-01 RT6-C2 foreign deposit + bogus citation refused | 0 |
| TC-100-02 fixture arithmetic | 0 |
| TC-100-03 filed lift calibration | 0 |
| TC-100-04 marginals replication | 0 |
| TC-100-05 missing-label handling | 0 |
| TC-100-06 extractor pin and schema (incl. own-hash refusal) | 0 |
| TC-100-07 no standing change without adjudication act | 0 |
| TC-100-08 proof banner + synthetic label set only | 0 |
| TC-100-09 Miller-reply trigger states (grant/refusal/silence) | 0 |
| Full suite (10 tests) | 0 |

Direct CLI payload verdicts:

| Invocation | Exit |
|---|---|
| `motif_rerun.py --mode record --root .` (no deposit) | 3 (GATE CLOSED) |
| `motif_rerun.py --mode record` with foreign CSV + any citation | 3 (GATE CLOSED) |
| `motif_rerun.py --mode proof --root .` | 0 |
| `deposit_extract.py` wrong `--pin` | 2 (PIN MISMATCH) |
| `deposit_extract.py` with the source's own hash as `--pin` | 2 (PIN MISMATCH) |
| `deposit_extract.py` with no `--pin` on a non-pinned source | 2 (PIN MISMATCH) |

The grant leg of TC-100-09 was exercised only in a
temporary simulated tree (header-only deposit at the
registered path, fixture record stating its SHA-256 and
a granting `Permission basis:` line); no real deposit
was landed and no real label was read.
