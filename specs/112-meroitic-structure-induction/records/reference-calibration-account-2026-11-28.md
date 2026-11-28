# Spec 112 — Reference calibration account (2026-11-28)

Filed under Round Q of the Co-scientist loop, ledger row
Q-M-1 (APPLY WITH MODIFICATION; adjudication
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-28-round-q.md`
§3). This account states what the filed reference sets
establish and what they do not. Neither historical run is
rescored, no label is replaced, and neither closure is
converted into a pass. No new annotation exercise was
performed for this account.

## The construction rule

In the revised harness, `extract_ground_truth()` constructs
each reference boundary by longest-suffix matching: it finds
the longest inventory suffix matching the end of each
eligible form, provided at least three characters remain.
Other rules add filiation and exact theonym boundaries. The
function does not consult an independently witnessed
morphological analysis of the particular form.

## Provenance of the filed reference items

The filed 1,719 reference items carry these rule
provenances:

| Provenance | Items |
|---|---|
| Suffix rule alone | 1,703 |
| Suffix plus filiation rules | 12 |
| Suffix plus theonym rules | 3 |
| Filiation rule alone | 1 |
| **Total** | **1,719** |

## What the reference sets establish, and what they do not

- A valid suffix inventory does not by itself establish that
  every word ending in one of its strings contains that
  suffix as a morpheme. The construction identifies a missing
  inferential link between an operational reference
  construction and per-form morphological truth; it does not
  establish that any particular filed label is wrong.
- Per-form independent warrant — source-linked morphological
  analysis establishing the asserted boundary for the
  individual form — is **absent** from the filed record for
  the reference items, and is marked absent here rather than
  supplied. No new annotation exercise was performed.
- P-3 "precision" measures **membership in the reference
  suffix inventory**, not the proportion of proposals
  independently demonstrated to be genuine morphemes. An
  unlisted proposal is not thereby linguistically false.

## Conclusion limit

Both Spec 112 closures stand, read at their correct scope:
**failures of the specified designs on the pinned inputs and
operational references** — not a corpus-wide information
limit, and not a demonstration that no structure exists in
the corpus. The two designs share corpus and evaluation
material and are not independent demonstrations of a
corpus-wide limit. The repeated median F1 of 0 coexists with
real operational improvement in the revision (308 items at
perfect F1, against 1,342 of 1,719 still at zero; slot match
73 of 95 against the first design's 1 of 95); neither figure
meets its frozen floor, and the floors were never lowered.

Any successor that needs a different reference construction
requires a prospective owner-approved registration stating
the resulting comparability limit (see ledger row Q-M-2).

## Fallback correction (red-team finding, no row)

The brief for Round Q described the revised design as
beating "the whole-form fallback on all 2,193 planted
forms". That comparison is corrected of record: the
2,193-form comparison was against the **all-single-character
fallback**. Whole-form candidates were removed from the
revised search and occur **zero times** in its top-five
fixture candidates. Both constructed fixture medians are
1.0; that establishes the specified repair and constructed
recoverability, not transfer to the real corpus.
