# Spec 099 — Inference log amendment: the F-9 standings act (M047 to class U)

Filed 2026-11-22 under the owner's adoption of the Red
Team Round 4 adjudication's recommendation (flag F-9). The
governing act is
`specs/091-anchor-comparison-integrity/records/f9-itemization-adjudication-2026-11-22.md`:
the itemization test is adopted prospectively, the
directed re-examination entered no `published_proposal`
item for M047 (its filed basis states no published
proposal of the value), and M047 was reclassed from E to U
on its remaining filed basis. The standings record carries
the rule and the outcome as its F-9 amendment
(`records/standings-relabel-execution-2026-11-21.md`).

## The change

No item is added, removed, or re-typed, and no basis text
changes. Two things move:

1. The builder (`tools/build_inference_log.py`) gains an
   F-9 amendment arm on the form of the Round 2 arm: where
   the standings text carries its F-9 amendment, the build
   asserts the amendment's outcome text ("M047 takes
   class U") and applies executed class U to M047, so a
   standings text that loses the amendment fails the build
   rather than silently restoring the superseded class.
   The log's `sources.standings` provenance string is
   extended to name the F-9 amendment and its act record.
2. M047's `crosswalk_identity` item gains a status note
   recording the act (no item entered; no internal
   motivation remains; class U follows the amended
   standings), on the form of M044's landed annotation.

The log and the Q3 audit were rebuilt and regenerated from
the same inputs (the audit package appendix and the
relabel execution record as amended).

## Verification payloads (this clone, before commit)

- Baseline reproduction, before any change: the builder
  over the unamended inputs reproduced the committed log
  byte-for-byte (JSON and rendering), and the audit
  regeneration reproduced the committed audit JSON
  byte-for-byte.
- Builder: `built 94 entries; census a=210 b=61
  ambiguous=25` — census unchanged (296 items).
- Log diff against the pre-act log: exactly one entry
  changes (M047: executed class E → U, the status note
  above) plus the `sources.standings` provenance string.
- Audit regeneration: **PAYLOAD VERDICT: DONE
  (class_changes_primary=0, weakened_primary=44, cycles=0,
  open_ends=38)** — identical to the pre-act payload. A
  field-by-field diff of the old and new audit JSONs shows
  exactly one differing field: M047's `executed_class`
  (E → U). Every per-reading outcome, both weakened counts
  (44 primary / 63 sensitivity), the component result and
  the open-end census are unchanged, because M047's entry
  holds no (b) or ambiguous item under either class.
- Fixture suite `tests/test_inference_log.py`:
  **15 passed**.
- TC-099-01 — `inference_log.py validate
  records/inference-log.json --full`: **PAYLOAD VERDICT:
  PASS (entries=94, violations=0)**.
- TC-099-02 — `inference_log.py completeness
  records/inference-log.json
  records/basis-rows-2026-11-21.json`: **PAYLOAD VERDICT:
  PASS (rows=94, violations=0)**.

## Non-effects

No other standing, class, anchor, or register entry is
altered. No audit outcome changes. The completion record's
headline stands, and both copies of it carry an appended
F-9 note recording this act (appended identically; the two
copies remain byte-identical).

## Amendment: the M048 re-adjudication (M048 to class I)

Filed 2026-11-22 under the owner's commission of the
re-adjudication that Red Team Round 2 finding RT2-08
attached to M048's corrected battery result. The
governing act is
`specs/091-anchor-comparison-integrity/records/m048-readjudication-2026-11-22.md`:
the result, produced under the F-4 commission, scored 2
at the corrected battery's 2-point promotion threshold,
and M048 was reclassed from U to I on the parity with
M089 stated in the standings supplement. The standings
record carries the outcome as its M048 re-adjudication
amendment
(`records/standings-relabel-execution-2026-11-21.md`).

### The change

No item is added, removed, or re-typed, and no basis
text changes. Two things move:

1. The builder (`tools/build_inference_log.py`) gains an
   M048 re-adjudication amendment arm on the form of the
   Round 2 and F-9 arms: where the standings text
   carries its M048 re-adjudication amendment, the build
   asserts the amendment's outcome text ("M048 takes
   class I") and applies executed class I to M048, so a
   standings text that loses the amendment fails the
   build rather than silently restoring the superseded
   class. The log's `sources.standings` provenance
   string is extended to name the M048 re-adjudication
   amendment and its act record.
2. M048's entry gains a note recording the act (the
   filed result; the RT2-08 re-adjudication; class I
   follows the amended standings), on the form of the
   Round 2 amendment notes this entry and M089's entry
   already carry.

The log and the Q3 audit were rebuilt and regenerated
from the same inputs (the audit package appendix and
the relabel execution record as amended).

### Verification payloads (this clone, before commit)

- Baseline reproduction, before any change: the builder
  over the unamended inputs reproduced the committed log
  byte-for-byte (JSON and rendering), and the audit
  regeneration reproduced the committed audit JSON
  byte-for-byte.
- Builder: `built 94 entries; census a=210 b=61
  ambiguous=25` — census unchanged (296 items).
- Log diff against the pre-act log: exactly one entry
  changes (M048: executed class U → I, the note above)
  plus the `sources.standings` provenance string.
- Audit regeneration: **PAYLOAD VERDICT: DONE
  (class_changes_primary=0, weakened_primary=44,
  cycles=0, open_ends=38)** — identical to the pre-act
  payload. A field-by-field diff of the old and new
  audit JSONs shows exactly one differing field: M048's
  `executed_class` (U → I). Every per-reading outcome,
  both weakened counts (44 primary / 63 sensitivity),
  the component result and the open-end census are
  unchanged: M048's outcome is "unchanged" and weakened
  under both treatments under either class, its entry's
  item shape being the same as M089's, whose class I
  rests on a filed corrected-battery result at the same
  threshold.
- Fixture suite `tests/test_inference_log.py`:
  **15 passed**.
- TC-099-01 — `inference_log.py validate
  records/inference-log.json --full`: **PAYLOAD VERDICT:
  PASS (entries=94, violations=0)**.
- TC-099-02 — `inference_log.py completeness
  records/inference-log.json
  records/basis-rows-2026-11-21.json`: **PAYLOAD VERDICT:
  PASS (rows=94, violations=0)**.
- Map mirror: `tools/ledger/generate_map.py --check`
  returns CHECK: MATCH — the map data is generated from
  the claims ledger, which this act does not amend; the
  mirrors are read under the C099-1 pointer as amended.

### Non-effects

No other standing, class, anchor, or register entry is
altered. No audit outcome changes. The completion
record's headline stands, and both copies of it carry
an appended M048 note recording this act (appended
identically; the two copies remain byte-identical).
