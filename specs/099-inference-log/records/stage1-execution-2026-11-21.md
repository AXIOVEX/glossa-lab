# Spec 099 Stage 1 — the inference log, execution record

Filed 2026-11-21. Venue: tower-compute, fresh clone
`~/glossa-work/s099-stage1-log`, branch
`spec/099-inference-log-stage1-2026-11-21`, first built on
main `6ec2cb94` (the Spec 099 adoption merge, PR #649) and
rebased onto main `2d718071` before merge, for the
standings amendment described below. All test payloads ran
under the tower-compute venv interpreter
(`~/glossa-work/venvs/glossa-ci`); verdicts below are the
payloads' own.

## What landed

- `records/inference-log.json` — the log itself, the record
  of record: 94 entries, one per strict-core reading, each
  carrying its basis as filed (verbatim), its items typed
  (a) / (b) / ambiguous with basis spans, and the landed
  status annotations.
- `records/inference-log.md` — the human-readable rendering,
  generated from the JSON by the builder; never edited
  separately.
- `records/basis-rows-2026-11-21.json` — the 94 appendix
  rows the log was built from, so TC-099-02 is reproducible
  from the repo alone (the audit package appendix itself
  lives in the goal workspace).
- `tools/build_inference_log.py` — the builder: template
  rules propose items over the checkable basis families;
  per-sign curation carries the specials (the Phase-276
  packages, the substrate matches, the pattern readings,
  the thin rows).
- One amendment to `tools/inference_log.py` (below).

## Edge census

299 items over 94 entries: **213 (a)** primary evidence,
**61 (b)** other-reading / candidate-system premises,
**25 ambiguous** — every ambiguous item is a
candidate-system score (SA-cons values, the Phase-95
expansion scores, the Phase-64 score, the staging score)
whose inputs the filed basis does not state; each carries
that reason on its row, per spec section 3.4. No ambiguous
case was resolved silently.

## Verification payloads (this clone, before commit)

- Fixture suite `tests/test_inference_log.py`:
  **15 passed**.
- TC-099-01 at Stage 1 — `inference_log.py validate
  records/inference-log.json --full`:
  **PAYLOAD VERDICT: PASS (entries=94, violations=0)**.
- TC-099-02 at Stage 1 — `inference_log.py completeness
  records/inference-log.json records/basis-rows-2026-11-21.json`:
  **PAYLOAD VERDICT: PASS (rows=94, violations=0)**.
- Falsifiers-annex cross-check (spec section 2's promised
  check): the sign set of
  `specs/091-anchor-comparison-integrity/records/per-reading-falsifiers-2026-11-21.md`
  equals the log's sign set exactly — 94 = 94, no sign on
  either side missing from the other. **PASS.**
- Read-through: the full human-readable rendering was read
  entry by entry against the filed bases before landing;
  every (b) item was verified against its basis clause in
  that pass. Three builder defects were found and fixed in
  that pass (below); the log was rebuilt and both checks
  re-run after the fixes.

## Stage 1 corrections (recorded, per the fix-and-prove rule)

1. **Reference-tool crosswalk extractor narrowed.**
   `basis_elements` in `tools/inference_log.py` fired a
   crosswalk element on any basis containing the word
   "crosswalk", including the audit's own CROSSWALK_CORPUS
   evidence-line label — the audit's counting, not a basis
   step. Entering crosswalk items for it would have
   violated C099-2's second direction (no item the basis
   does not state). The extractor now fires only on
   `mahadevan_parpola_crosswalk` or "crosswalk evidence".
   The fixture tests do not cover this family distinction;
   the amendment is recorded here as a Stage 1 execution
   correction.
2. **M124 status notes reassigned by kind.** The first
   build attached the "leg inherited from M044" note to the
   entry's first two items by position, which put it on a
   dictionary item and left one comparative leg unnoted.
   The notes now attach by kind: comparative legs carry the
   inherited note, dictionary items carry the PARTIALLY
   VERIFIED note.
3. **Entry-level status notes completed; battery outcome
   ordered last.** M044's DEDR-1638 FAILS note and M329's
   4524 numbering note now appear on every dictionary item
   citing that entry (both items in each entry cite it).
   Corrected-battery / site-statistics items — the appendix
   rows' trailing sentence — now render last in each entry,
   with item ids renumbered after the stable sort.

## Filed-basis truncations

Eight-plus appendix basis cells truncate mid-clause (among
them M202, M330, M336, M367, M347, M351, M362, M398,
M010, M023, M025, M089). Each truncation is recorded on
its entry; no item is entered for text the basis does not
state. M336's third collocation premise is entered as a
(b) item with its target recorded as unrecoverable from
the filed text; M367's M267 collocation count is entered
with the truncation noted.

## Standings amendment during this PR (Round 2, M044)

While this PR was in CI, the Red Team Round 2 execution
landed on main (tip `2d718071`, PRs #647/#648/#650/#652).
Its Indus act adjudicated M044 under the WS2 addendum rule
(`records/m044-addendum-adjudication-2026-11-21.md`): the
DEDR leg is struck, no leg stands verified as filed, and
M044 takes class U — the partition is now 4 E + 65 I +
4 R + 3 P + 18 U. The log was updated to the amended
standings before merge:

- M044's executed class is U; its dictionary items carry
  the adjudicated outcome, not the pre-adjudication
  "stands as executed" wording. The builder applies the
  standings record's appended Round 2 amendment explicitly
  and asserts on it, so a standings text that loses the
  amendment fails the build.
- M329's dictionary note now follows the amendment's
  formulation: the leg is verified at the print entry
  cited; the restored tree's entry 4524 is a different
  entry and the divergence is unresolved.
- M089's collocation count and premise items carry the
  Round 2 unreliability annotation (contradictory pairs
  filed in the Tranche 2 rerun record), with an entry note
  that its class rests on the corrected-battery result;
  M048's entry notes that no corrected battery result is
  filed for it. Both counts and classes are otherwise as
  filed.

The edge census is unchanged (the amendment moves one
class label and annotates; it adds and removes no items).
Both TC payloads were re-run on the rebuilt log and on
the rebased tree: PASS and PASS, as above.

## What Stage 1 does not do

No standing, class, or register entry is altered. The
audit (Stage 2) runs from this log alone under TC-099-03.

## Amendment pointer (2026-11-21, Red Team Round 4 — RT4-08)

The edge census stated in this record (299 items: 213 (a) /
61 (b) / 25 ambiguous) is the census of the log as first
landed. The log has since been rebuilt under
`records/inference-log-amendment-2026-11-21.md`: three
readings (M044, M124, M329) each cited one DEDR entry as
two items, against spec section 3.2, and the repaired log
counts **296 items: 210 (a) / 61 (b) / 25 ambiguous** over
the same 94 entries. The verification payloads above were
re-run against the repaired log and pass; the payloads are
recorded in the amendment record.

## Amendment pointer (2026-11-22, F-9)

The standings this log carries have since moved once more:
the owner adopted the itemization test (Red Team Round 4,
flag F-9) and M047 was reclassed from E to U on 2026-11-22
(`specs/091-anchor-comparison-integrity/records/f9-itemization-adjudication-2026-11-22.md`).
The log as amended carries executed class U for M047; no
item changed and the census stands at 296 items (210 (a) /
61 (b) / 25 ambiguous). Record:
`records/inference-log-amendment-2026-11-22.md`.

## Amendment pointer (2026-11-22, M048 re-adjudication)

The standings this log carries have since moved once
more: M048's corrected battery result, produced under
the F-4 commission, scored at the corrected battery's
2-point promotion threshold, and the re-adjudication
RT2-08 attached to that outcome reclassed M048 from U
to I on 2026-11-22
(`specs/091-anchor-comparison-integrity/records/m048-readjudication-2026-11-22.md`).
The log as amended carries executed class I for M048;
no item changed and the census stands at 296 items
(210 (a) / 61 (b) / 25 ambiguous). Record:
`records/inference-log-amendment-2026-11-22.md`.
