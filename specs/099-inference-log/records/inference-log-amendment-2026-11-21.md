# Spec 099 — Inference log amendment: the DEDR double-citation repair

Filed 2026-11-21 under Red Team Round 4 finding RT4-08
(adjudicated APPLY WITH MODIFICATION), discharging the
census arm of Round 3 findings RT3-18 and RT3-02. The
Stage 1 execution record's census is superseded by this
record where the two differ; a dated pointer is appended
there.

## The defect

Spec section 3.2 states the counting rule expressly:
"Restatements of one observation inside a single basis (…
a DEDR entry cited in the basis and again as the row's
dictionary reference) are one item citing both spans'
clauses in its statement." Three entries in the log as
first landed violated it, each in the same form — the
basis's Phase-276 external-corroboration leg and its
"Dictionary reference as recorded" line entered as two
items citing one DEDR entry:

- **M044**: M044-01 / M044-04, DEDR 1638.
- **M124**: M124-01 / M124-04, DEDR 1651. (The Round 4
  attack charged M044 and M329 only; the adjudication's
  first-hand recount found this third pair, and the repair
  covers it.)
- **M329**: M329-02 / M329-05, DEDR 4524.

The mechanism was in the builder
(`tools/build_inference_log.py`): the template's
dictionary-reference arm runs before the per-sign curation
adds the Phase-276 leg, so its "when no DEDR item yet
covers the same number" check could not see the leg it was
duplicating. The duplication was disclosed on the items'
status notes in the landed log; disclosure mitigated
deception, not arithmetic.

## The repair

The builder's Phase-276 arm now merges into an existing
dictionary-reference item citing the same entry: one item
whose statement cites both clauses (the external
corroboration leg and the dictionary reference), per
section 3.2. The log was rebuilt from the same inputs
(the audit package appendix and the relabel execution
record) with the amended builder, and the Q3 audit was
regenerated over the repaired log.

**Census, before → after:** 299 items → **296 items**
(213 (a) → **210 (a)**; 61 (b) and 25 ambiguous unchanged)
over the same 94 entries. The log diff is exactly the
three entries above, each losing one item; item ids in
those entries renumber by position, as the builder assigns
them.

## Verification payloads (this clone, before commit)

- Builder: `built 94 entries; census a=210 b=61
  ambiguous=25`.
- Audit regeneration: **PAYLOAD VERDICT: DONE
  (class_changes_primary=0, weakened_primary=44, cycles=0,
  open_ends=38)** — identical to the pre-repair payload.
  A field-by-field diff of the old and new audit JSONs
  shows exactly two differing fields: `edge_census.a`
  (213 → 210) and `edge_census.items` (299 → 296). Every
  per-reading outcome, both weakened counts (44 primary /
  63 sensitivity), the component result and the open-end
  census are unchanged, because every merged item is an
  (a) item and no removal outcome turns on one.
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

No standing, class, anchor, or register entry is altered.
No audit outcome changes. The completion record's headline
stands, now citable in the Round 4 scope-note form appended
to it.
