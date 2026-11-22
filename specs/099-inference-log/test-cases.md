# Spec 099 — Test Cases

The test cases are implemented in
`tests/test_inference_log.py` against the reference
implementation in `tools/inference_log.py`, on synthetic
fixtures at adoption; TC-099-01 and TC-099-02 run again over
the real 94-entry log at Stage 1, and TC-099-03's independent
implementation runs over the real log at Stage 2. Payload
verdicts are recorded in the spec's records at each run.

## TC-099-01 — Schema validation (C099-1, C099-3)

A six-entry fixture log built to the schema of spec
section 3.2 validates clean. Each of the following mutations
is rejected: a duplicated sign; an executed class outside
the vocabulary; an item whose type does not match its kind;
an item whose `basis_span` does not occur verbatim in its
entry's `basis_as_filed`; a (b) item with no reason; a (b)
item with neither targets nor a target note; a (b) item
naming a target the basis does not name and no spec-named
`target_source`; and full mode (`expect_full`) applied to a
log of fewer than 94 entries. At Stage 1 the same validator
runs in full mode over the real log: 94 entries, no
violations.

## TC-099-02 — Completeness against the filed bases (C099-2)

The fixture's filed-basis rows check complete against the
fixture log: every checkable element the extractor finds in
each basis (dictionary citations, collocate premises,
pattern targets, slot constructs, consistency scores, motif
clauses, counts, self-assertions, published mentions,
crosswalk steps) is covered by an item. Deleting one item
(the M902 collocate premise) makes the checker fail on that
element; adding an uncovered dictionary citation to a filed
basis makes it fail on that citation; dropping a filed row
makes it fail on the unmatched entry. At Stage 1 the same
checker runs over the real bases (the appendix rows as
filed) against the real log.

## TC-099-03 — Audit determinism from the log alone (C099-4, C099-5, C099-6)

An independent implementation of spec section 4, written
from the spec text inside the test file (per-class
recomputation; strongly connected components by pairwise
reachability rather than the reference implementation's
Tarjan), recomputes the fixture audit and matches the
reference implementation's outcomes and components exactly.
The fixture plants, and the test asserts, each outcome the
rules can produce: an E reading unchanged and weakened by a
(b) removal; an I reading resting only on a (b) item, class
would change to U; an I reading with an (a) item and an
unnamed (b) slot, unchanged and weakened, the slot listed as
an open end; an I reading resting only on an ambiguous item,
unchanged under the primary treatment and class would change
to U under the sensitivity treatment (divergent); a U reading
unchanged and unweakened; an R reading unchanged; a two-node
cycle (M901 ↔ M902) found as the single component; and the
edge census counted exactly. At Stage 2 the same independent
implementation runs over the real log and must reproduce the
filed audit table without difference.
