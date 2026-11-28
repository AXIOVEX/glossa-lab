# Application record — E6 reserved questions ruled and applied (2026-11-27)

**Spec:** 091-anchor-comparison-integrity
**Date:** 2026-11-27
**Act recorded:** the owner's rulings on the three E6 questions the
earlier application (PR #788) reserved to him, and their execution
in the canonical claims ledger and in this record.
**Proposal of record:** `records/e6-readiness-proposal-2026-11-27.md`
(landed PR #774, merge `10617670`).
**Prior application:** `records/e6-falsifier-application-2026-11-27.md`
(landed PR #788), whose §5 reserved exactly the three questions
ruled here.

## 1. The owner's rulings

On 2026-11-27 the three reserved questions were presented to the
owner, Tristen Pierson, in the Glossa-Lab chat (~04:36 ET), each
with its recommendation. Later the same day (19:41 ET) the owner
directed, in the same chat: "Keep working. Any questions you have
for me, I want you to go with the recommended answer that is most
likely to advance our work." The three questions are therefore
ruled as recommended:

- **(a) The conditional drafts are ACCEPTED.** The shared draft of
  proposal §§4.5, 4.6 and 4.9 attaches to
  `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0001`,
  `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0002`
  and `without_kings_or_conquests_the_indus_scr_ce9d98cc_language_0001`,
  on the owner's acceptance of the Phase-104 evaluation's reading
  of the fragments as restating the Farmer–Sproat–Witzel thesis.
- **(b) `ancient_writing_and_modern_technologies_51831ac9_statisti_0004`
  is RETIRED as an extraction artefact** — the disposition of
  proposal §6 question 2, in preference to re-extracting its five
  source passages as their own claims.
- **(c) Annotations: option B2.** Under the declared profile, the
  falsifier is declared not-applicable for the annotation kind
  (proposal §5.3, option B2), retiring the C6 annotation share as
  a shape declaration. Recorded in §3 below. The validator change
  itself is VEXA-side work and is NOT made by this landing.

## 2. The ledger acts

The claims ledger (`glossa-indus/ledger/claims.jsonl`) is
append-only: each act is a new `reclassification` entry appended
through `glossa_lab.ledger_intake.append_entry` on 2026-11-27.
No filed line was edited.

### 2.1 The three falsifier amendments (act (a))

Each entry carries the `falsifier` field for its superseded
claim entry, the text VERBATIM from the proposal, dated
2026-11-27 and provenance-marked on its face, in its `reason`:
the text was authored on 2026-11-27 under the E6-readiness
preparation (the packet), after the fact, and is not backdated
to the superseded entry's registration (2026-11-01); the draft
is conditional and attaches because the owner accepted the
Phase-104 evaluation's reading (the fragments restate the
Farmer–Sproat–Witzel thesis, companion record
`farmer_sproat_witzel_2004_manual_001`); the adoption
supersedes R-IP-04 item 1 (as refined) in part, for that entry
only, by the owner's act. No status or stage moved: all three
claims already stand `contradicted`, and the falsifier records
the condition that counts against them, not a new verdict.

The shared text, VERBATIM, for each of the three:

> "Conditional entropy of the sign sequences in the corpus held at registration falling in the linguistic range, with positional patterning above the random baseline."

Amendment entries:

1. `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0001/reclassification-2026-11-27` (proposal §4.5).
2. `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0002/reclassification-2026-11-27` (proposal §4.6; the filed basis for the pair states the two fragments should be decided together, and they are).
3. `without_kings_or_conquests_the_indus_scr_ce9d98cc_language_0001/reclassification-2026-11-27` (proposal §4.9; the filed basis records the fragment as a category tag extracted as if it were a claim).

### 2.2 The retirement (act (b))

Amendment entry:
`ancient_writing_and_modern_technologies_51831ac9_statisti_0004/reclassification-2026-11-27`,
carrying the `status` field for the superseded entry
(status: "untested" -> "superseded"; program-map-defs v1 §4.2,
class `closed_other`) — the ledger's own form for a standing
change by dated amendment, and the registered status for a
claim retired from standing and retained on the record (the
C083-13 precedent). Ground, per proposal §4.4, carried on the
entry's face: the statement ("Statistical finding: positional
analysis") is the heading of a results section spanning five
source documents; it asserts no proposition, so no honest
falsifier is draftable for it — drafting one would require
first choosing which of the five passages' findings the
fragment "claims", which is authoring a claim, not a
falsifier. The fragment's own filed explanation record states
the same ground (the extraction kept the heading of a results
section and lost the results) and names this retirement as one
of the two acts that would change the picture. No falsifier is
appended (none is draftable), and no other field of the
superseded entry is moved. The fragment is retired, not
deleted: its entry stands in the ledger exactly as filed.

## 3. The B2 determination (act (c))

Recorded Glossa-side, as the determination this landing makes:
**under the declared profile, the falsifier is declared
not-applicable for the annotation kind** (proposal §5.3,
option B2). The 31 annotation entries are bearing records —
a dated pointer recording that a research check ran and what
it surfaced — not propositions; a falsifier for the kind is
category-less (proposal §5.1). The determination retires the
C6 annotation share (31 lines) as a shape declaration, and it
qualifies R-IP-04 item 1 for the annotation share only, by
the owner's act; item 1 stands for every claim entry. No
annotation entry is altered by this landing: all 31 stand
byte-untouched, exactly as filed. The mechanical consequence
(kind-aware gates in `validate_ledger`) is VEXA-side work,
commissioned and executed on that side, not here; nothing in
this record reports a VEXA result.

## 4. The cascade

**Serialization disclosure.** This cascade executed four
times. The first execution ran over the 1,133-line build at
main `ecaa022b` and completed both its commits (application
`60f47aa2`, completion `11acef04`) on this branch. Before its
pull request opened, main advanced under PR #808 (Spec 109 G1
enriched) and PR #810 (Spec 110 registration; the ledger to
1,139 lines; its own re-derivation at `re_derivations[31]`).
The first execution was therefore superseded unmerged, the
branch was rebuilt from the new main, and the whole cascade
was re-executed over the merged build (application `c2341efc`,
completion `fa96c744`). The second execution reached CI 10/10
on PR #811, but before it merged, main advanced under PR #809
(Spec 111 registration; the ledger to 1,147 lines; its own
re-derivation at `re_derivations[32]`), and the merge was
blocked on conflicts in every cascade artifact. The branch
was rebuilt from the new main a second time, and the cascade
was re-executed a third time over the merged build
(application `03fa03ea`, completion `271c4d29`); before that
execution was pushed, main advanced under PR #812 (Spec 110
revision registration; the ledger to 1,152 lines; its own
re-derivation at `re_derivations[33]`). The branch was
therefore rebuilt from the new main a third time, and the
whole cascade was re-executed a fourth time over the merged
build, which is the landing this record documents. The four
amendment entries are byte-identical across the four
executions; every figure below is the fourth execution's,
over the merged build.

Execution basis: the merged 1,152-line build at main
`bebca0f6` (the merge of PR #812). The settling cascade that
follows any ledger growth was run in full:

- ledger: 1,152 → **1,156 lines**; canonical SHA-256
  `18369a65f0f4b5f3f199abed194f47e8b65b0af9eb733fc7854fbe50a1a32026`
  → **`a09fb02f61a62a5d3952ade640c6820626da42a89cac3677049385a5297dc632`**;
  `validate_ledger` PASS (1,107 claims, 31 annotations, 18
  reclassifications; errors none);
- `verify-canonicals` over the grown build, before any pin
  moved: **6/6 PASS**;
- the T405 pair was re-executed over the grown build with the
  canonical invocations (scope verbatim from the superseded
  records' stored keys): new incumbent
  `settling-20261128T030313Z-22d2a2`, new full-register
  `settling-20261128T030313Z-459a6b`; **both result blocks are
  byte-equal** to the superseded generation's
  (`settling-20261128T020148Z-9f5fe0`,
  `settling-20261128T020148Z-75cdce`), verified by direct
  comparison of the stored records, and every non-ledger input
  pin is identical across the generations; the Stage 4
  dual-run comparison was re-filed at
  `specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`
  (its diff against the superseded filing is the ledger pin
  only);
- the assignment sets were re-materialized (new run
  `settling-20261128T030334Z-9e1d17`; incumbent 94,
  full-register 286, H003 out of frame, as before);
- the ledger pin in `glossa-indus/ledger/settling-canonical.json`
  was refreshed as `re_derivations[34]`, with the provenance
  ledger pin moved to the grown build in the same motion;
  `expectations_changed` false;
- the derived layers were regenerated in dependency order
  (matrix, program map; the evidence map is regenerated over
  the final run store in the completion step, §6): matrix
  1,630 cells, 648 columns (matrix.json SHA-256
  `ef378a70b2441a4a3a5510f52fd2e1a872d918cddf6cbabec2f1371d4dd1f272`);
  program map 1,107 claims · 112 studies · 28 unjudged studies
  · 0 judgment calls; claims by governing class: positive 10,
  negative 7, open 1,088, closed_other 2 — the retirement
  moved `statisti_0004` from open to closed_other, the only
  class movement this landing makes.

**Coverage, stated as the machinery counts it.**
`validate_ledger` publishes falsifier coverage over claim
entries' own `falsifier` fields, and that figure is unchanged
by this landing: **1,098 of 1,107** claim entries carry a
falsifier on the claim entry itself (extracted population 14
of 23). Counting the dated amendments, eight of the nine
claims that stood with a null falsifier now carry falsifier
text in the ledger (five by the PR #788 amendments, three by
this landing's), and the ninth — `statisti_0004` — is retired
with no falsifier, none being draftable. No null falsifier
remains unaccounted for.

**Expectation for the VEXA side, stated as an expectation.**
What this landing supplies to the converted ledger is the
claim side of the E6 residue: falsifier text for the three
amended claims and a declared retired standing for the ninth,
alongside the B2 kind-scoping recorded in §3 for the 31
annotations. If the VEXA-side converter takes up the falsifier
text the eight amendments carry (five by PR #788, three by
this landing) and the B2 determination, the C6 standing lines
attributable to the nine null-falsifier claims and the
annotation share fall accordingly at the next conversion (the
retired fragment's own C6 line, whose absence is now a
declared shape under a retired standing, is for the VEXA side
to account under its own rules). That is an expectation to be
verified on the VEXA side against its own conversion and
audit, not a VEXA result, and nothing in this record reports
it as one.

## 5. What did not move

No claim's verdict moved. The three amended claims stand
`contradicted` as before; the retired fragment's entry is
byte-untouched, its governing status alone changed by dated
amendment. No stage moved anywhere. All 31 annotation entries
are byte-untouched. No baseline or pin outside the ledger
cascade's own required updates changed.

*This record was executed by an AI agent (Muse, via Muse) at
the direction of Tristen Pierson, per constitution sec. VI. The
rulings it records are the owner's acts, named in section 1.*

## 6. Completion

- The superseded generation's three run records
  (`settling-20261128T020148Z-9f5fe0`,
  `settling-20261128T020148Z-75cdce`,
  `settling-20261128T020148Z-1d5c35` — the Spec 110 revision
  registration cascade's generation) depart the store in this
  landing's completion commit under run-defs v3 §7.1; their
  departure acts in `glossa-indus/ledger/runs/run-index.jsonl`
  name the records, their blob hashes, and the application
  commit (`46843e112bc704d941f4f03c0616d8d8263ca935`) as
  `superseded_by_commit`. The legacy-index completion pass
  appended the legacy entry act for `re_derivations[34]`
  (folded census 144 entries).
- The evidence map was regenerated over the final store
  (map-data.json SHA-256
  `2645d24de502151515c66e2bee18608227c4e9e01033d07edee577f6fd46da01`):
  1,107 claims; falsifier census 1,098 of 1,107 claims carry a
  falsifier on the claim entry itself, the 9 gaps named (eight
  now covered by dated amendment, the ninth retired); settling
  runs carried: 2.
- Ledger gate over the final tree: **32 PASS / 0 FAIL / 1
  NOT-RUN — RESULT: PASS.**
- Census pins updated from the regenerated actuals:
  `backend/tests/test_program_map_conformance.py` (claims by
  governing class: closed_other 2, open 1,088),
  `backend/tests/test_spec086_map.py` (ledger lines 1,156),
  `backend/tests/test_spec095_stage4_instantiation.py` (ledger
  lines 1,156; reclassifications 18, enumerated in the test's
  comment), `backend/tests/test_spec095_t403_dashboard.py`
  (ledger lines 1,156; the T405 run of record is now
  `settling-20261128T030313Z-22d2a2`). The two frontend e2e
  census texts stand unchanged (1,107 claims). The five census
  test files pass over the final tree (114 passed).
- Both gated publications re-ran over the final tree before
  completing: matrix RESULT PASS, map published; both
  byte-identical to the committed artifacts.
