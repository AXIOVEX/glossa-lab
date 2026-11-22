# Spec 100 — Test-Case Execution and Custody Proof (2026-11-22)

Executed on tower-compute in the registration clone
`~/glossa-work/s100-motif-rerun-2026-11-22`, at registration,
before the package landed. Every verdict below is the
payload's own exit code; no wrapper state is used as a
verdict.

## Pipeline of record (SHA-256 at registration)

- `tools/motif_rerun.py`:
  `5d8d79ddf012ef617aa671b97c531bd935d6e321553fc87e824794d9503be226`
- `tools/deposit_extract.py`:
  `8edaa84ca6e980de891b214f8a08eeff2c256214c3e999d6e2d22e64a0eff07a`

## Test cases (TC-100-01..TC-100-06)

Command (from the repository root):
`~/glossa-work/venvs/glossa-ci/bin/python -m pytest specs/100-motif-claims-rerun/tests/ -q`

**Payload verdict: exit 0 — 6 passed.** The suite covers:
the gate refusal (TC-01: record mode without a deposit
exits 3, GATE CLOSED, no outcome written; a nonexistent
deposit path likewise); fixture arithmetic including the
strict > 5.0 boundary at lift exactly 5.0 (TC-02); the
frozen lift formula reproducing M063's filed 4.35 from the
filed fragment's own numbers (TC-03); the marginals
replication over the real tracked population files, both
paths, all 13 signs equal to PR #634's counts (TC-04);
missing-label handling and the join defect (TC-05); the
extractor's pin refusal and schema extraction on a
synthetic source (TC-06). No real iconography label is
read by any test.

## End-to-end proof run (proof mode, synthetic labels)

Command: `python3 specs/100-motif-claims-rerun/tools/motif_rerun.py --mode proof --root . --out ~/glossa-custody/spec100/proof-run-2026-11-22.json`

**Payload verdict: exit 0 (EXIT_OK).** The full path
executed in custody: both population representations
loaded (1,670 seals each), deterministic synthetic labels
generated in memory over the real seal ids, the join
applied, all 13 claims computed on both paths with exact
agreement (no disagreement raised), verdicts emitted
under the banner "PROOF - NOT A RESULT (synthetic
labels)". The proof's output and log are held in custody
at `~/glossa-custody/spec100/` on tower-compute; they are
not repo records and not results. As a machinery check
only, the proof's sign marginals (a+b per claim) reproduce
PR #634's replicated counts for all 13 signs (15, 23, 23,
18, 24, 18, 20, 28, 18, 15, 13, 25, 19).

## Gate refusal against the real root

Command: `python3 specs/100-motif-claims-rerun/tools/motif_rerun.py --mode record --root .`

**Payload verdict: exit 3** — "GATE CLOSED: record mode
requires an existing deposit file and its record
citation. The deposit is held under flag F-1 (Spec 100,
claim C100-1); nothing has been computed."

## What was not run

No record-mode computation over any real label set; no
extraction from any Holdat source (the extractor ran
only inside TC-100-06 on a synthetic fixture); no
deposit. The pinned Holdat corpus build (SHA-256
`62d14d2b…`) is not held on this venue at registration
time — the same state the F-4 package recorded on
2026-11-22 — so no custody copy was joined, read for
labels, or copied anywhere by this package. (A CSV
answering to the source's filename exists in an archived
pytest scratch tree on this host; its SHA-256 is
`253f7569…`, not the pin, so it is not the build of
record and was not used.)
