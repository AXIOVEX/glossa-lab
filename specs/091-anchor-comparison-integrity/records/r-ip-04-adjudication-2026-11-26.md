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

## Item 1 refinement — Rendering rule for the 1,051 (ruled and confirmed, 2026-11-27)

**Ruling, in the owner's words:** "Refine item 1:
rendering rule for the 1,051, standing for true
absences."

**Provenance:** ruled by the owner in the VEXA chat,
2026-11-27 02:37 ET; relayed to the Glossa-Lab chat; and
confirmed by the owner in the Glossa-Lab chat,
2026-11-27 03:09:53 ET ("Confirm and record the item 1
refinement").

**Scope.** The 1,051 list-shaped falsifiers are
adjudicated by a list-to-string rendering rule, stated
in the import profile and checked by the verbatim
audit; they are not recorded as absences. The
standing-divergence ruling of item 1 applies only to
the true absences: the 9 null falsifiers and the
annotation entries' falsifier share (the C6 line of
each annotation entry, 31 in all).

**Effect and supersession.** This refinement supersedes
the unrefined item 1 wording ("Record all falsifier
absences as standing divergences") for the 1,051. The
item 1 landing above carried the 1,051 as their own
line, present content in list shape, with their
disposition expressly subject to this pending
refinement; that refinement-carrying form is now
settled by this ruling. Item 1 as it applies to the
true absences stands unchanged.

## Item 4 — Status mappings confirmed as recorded (ruled and confirmed, 2026-11-27)

**Ruling, in the owner's words:** "Confirm all four
status mappings as recorded."

**Provenance:** ruled by the owner in the VEXA chat,
2026-11-27 02:37 ET; relayed to the Glossa-Lab chat; and
confirmed by the owner in the Glossa-Lab chat,
2026-11-27 03:09:54 ET ("Confirm and record item 4").

**Scope.** The four judgement calls stand as recorded
in the import profile's mapping file
(`specs/011-import-path/glossa/glossa-mapping.json` in
AXIOVEX/vexa): draft → UNJUDGED,
partially_supported → INCONCLUSIVE,
unsupported → INCONCLUSIVE, superseded → UNJUDGED. The
full mapping (8 statuses; kind annotation → Evidence,
claim → Claim) is unchanged.

**Effect.** With this ruling, all four R-IP-04 items
are ruled and confirmed. Nothing in the mapping
changes; the item closes the adjudication's open
questions.

## Application on the VEXA side — The applied state (2026-11-27)

Recorded from the VEXA chat's completion report. The
four rulings were applied at AXIOVEX/vexa main
`b78c07bd` (application commit `961227b`, record commit
`b78c07b`), remote-verified there.

- **Item 1 as refined.** The falsifier census at the
  source head found 1,051 lists carrying 1,107
  elements, all strings, no empty lists, no element
  containing a newline, so the rendering rule is a
  newline join (single-element lists render as their
  element), implemented as a profile-gated capability
  in import_ledger 1.2.8 (field_renderings,
  list_to_string; one implementation serves the
  converter and the coverage audit). The list-shaped
  C6 leg cleared on its merits (D-RENDER ×1,051). The
  true absences stand: 9 null claims and 31
  annotations.
- **Item 2.** The shipped positional projection did not
  fit this ledger's shape (source_of_record sits at
  position 0 on 343 claims, position 1 on 717), so a
  sibling form was implemented under the same
  discipline: member-value select with exactly-one
  match required, the date taken from the entry itself
  (the source record carries no date; the basis is
  stated in the profile). C7 ×1,091 cleared on their
  merits.
- **Item 3.** Annotations convert under their own kind
  profile (statement and status omitted rather than
  nulled; falsifier absence rendered as the explicit
  null, standing under item 1; provenance projected
  from the sidecar). C2 ×31 and C4 ×31 remain E2 lines
  because the validator is kind-blind and no statement
  or status was derived (deriving one was not the
  ruling); they stand as the named population's declared
  shape under its own profile.
- **Item 4.** No change; the regenerated mapping file
  is byte-identical to the E5-cited hash, and the
  honesty counts match on both sides.

**New E2 state.** The converted ledger fails with
exactly 102 lines (C6 ×40, C2 ×31, C4 ×31), down from
2,244. The verbatim audit passes 24,752 comparisons
with 0 mismatches; coverage accounting is identical to
E5; E3 still refuses the converted ledger; the
comparison verdict is unchanged. TC-IP-15 (the new
capabilities' regression case) passes 8/8; all standing
gates clear.

**What remains.** E6 for this study now turns on two
matters on this side of the record: falsifier text for
the 40 entries standing as true absences in this
study's own source ledger, and the annotation shape as
a profile matter. R-IP-04 itself is complete: all four
items ruled, confirmed, and applied.
