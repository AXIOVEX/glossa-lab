# R-IP-04 Adjudication — Owner Rulings (2026-11-26)

R-IP-04 is the owner's adjudication of the standing
divergences from the VEXA Spec 011 E5 shadow import of this
study's claims ledger. The import ran in shadow and landed
at AXIOVEX/vexa commit `41c283ae`, reading the ledger of
record (`glossa-indus/ledger/claims.jsonl`) at glossa-lab
main `eaf5a62c` through the GitHub API; nothing in this
repo was edited by the import. Conversion was faithful
(23,661 verbatim comparisons, 0 mismatches, no falsifier
text fabricated) and the comparison verdict was
EQUIVALENT-WITH-RECORDED-DIVERGENCES. The converted ledger
stands at 1,091 entries (1,060 claims + 31 annotations)
with 2,244 recorded standing divergences; until R-IP-04 is
ruled, the converted ledger's E2 FAILS, E3 keeps refusing
it, and no E6 reproduction can run.

**The two groupings reconcile exactly.** One FAIL line is
one (entry, check) failure pair. By check: C6 ×1,091,
C7 ×1,091, C2 ×31, C4 ×31. The 1,060 claim entries carry
exactly 2 failures each (C6, C7); the 31 annotation
entries carry exactly 4 each (C2, C4, C6, C7), 124 in all.
The adjudication-item partition used below: C6 list-shaped
falsifiers ×1,051; C6 null falsifiers ×9; C7 provenance
×1,060 claims; the 31 annotation entries ×124. The bridge
is exact (C6 1,091 = 1,051 + 9 + 31; C7 1,091 = 1,060 +
31). Both partitions were verified against the recorded
`glossa-divergences.json` committed with the import and a
fresh re-run of validate_ledger 1.0.4 against the
committed converted ledger, producing the identical 2,244
pairs.

This record carries the owner's rulings on R-IP-04 as
they land. Each ruling was given by the owner in the VEXA
chat and confirmed by the owner in the Glossa-Lab chat;
both acts are recorded per item. Items not yet ruled are
recorded as pending and are not pre-decided here.

## Item 1 — Falsifier absences stand (ruled)

**Ruling, in the owner's words:** "Record all falsifier
absences as standing divergences."

**Provenance:** ruled by the owner in the VEXA chat,
2026-11-26 22:37 ET; relayed to the Glossa-Lab chat; and
confirmed by the owner in the Glossa-Lab chat, 2026-11-26
22:38 ET ("Confirm and record item 1").

**Scope and structure.** Item 1 covers the C6 falsifier
group, which is not homogeneous, and the record carries
its parts distinctly:

- **True absences — standing as ruled.** The 9 null
  falsifiers on the claim entries, and the annotation
  entries' falsifier share of their 124 failures (the C6
  line of each annotation entry, 31 in all). These are
  absences: no falsifier text exists for them in the
  ledger of record. By the ruling they stand as recorded
  divergences, and no falsifier text is to be authored
  after the fact.
- **The 1,051 list-shaped falsifiers — present content,
  carried as their own line.** These are not absences:
  the falsifier content is present in the ledger, in list
  shape (this study's schema makes the falsifier a list),
  where the core's field is a single string. Item 1 was
  prompted with this group lumped under the absence
  heading. On a precision re-reading of the Spec 011
  record (VEXA chat, 2026-11-26), the group is carried
  here as its own line, distinct from the true absences:
  its disposition is subject to the owner's pending
  refinement ruling (see Pending below) and is not
  settled by item 1's absence language. The ruling itself
  is not rewritten or softened by this structure; its
  provenance record stands as given.

**Effect.** The converted ledger's E2 remains FAILS on
these standing divergences. E3 and E6 are unaffected by
this item; they wait on the remaining R-IP-04 items.

## Item 2 — Provenance projected as a named history event (ruled)

**Ruling, in the owner's words:** "Project provenance as
a named history event."

**Provenance:** ruled by the owner in the VEXA chat,
2026-11-26 22:38 ET, and confirmed by the owner in the
Glossa-Lab chat, 2026-11-26 22:39 ET.

**Scope.** This is the C7 item: provenance on the 1,060
claim entries and the annotation entries alike (C7
×1,091) is projected as a named history event in the
shared vocabulary, not carried as a profile extension.
The ruling matches the owner's RCPH ruling on the same
question, given the same evening.

## Item 3 — Annotations are their own kind (ruled)

**Ruling, in the owner's words:** "Annotations stand as
their own kind, under their own profile."

**Provenance:** ruled by the owner in the VEXA chat,
2026-11-26 22:38 ET, and confirmed by the owner in the
Glossa-Lab chat, 2026-11-26 22:39 ET.

**Scope.** The 31 annotation entries are their own kind,
judged under their own profile, not carried as defective
claims. Their 124 recorded failures are read under that
kind's standing, per this ruling and item 1's structure
above.

## Pending — not ruled, not pre-decided

- **The four status-mapping judgement calls** in the
  import profile. These are being prompted in the VEXA
  chat; no ruling has landed.
- **The item-1 refinement:** a list-to-string rendering
  rule for the 1,051 list-shaped falsifiers, which would
  clear those on their merits since the content exists,
  versus keeping item 1 exactly as ruled. This question
  is in front of the owner in the VEXA chat; no ruling
  has landed.

Until R-IP-04 is fully ruled, the converted ledger's E2
stands as FAILS on the recorded divergences as qualified
by the rulings above, E3 keeps refusing it, and E6
(external reproduction, currently 0 of 3) cannot run.
