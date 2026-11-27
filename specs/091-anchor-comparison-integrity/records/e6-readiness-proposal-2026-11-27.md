# E6-Readiness Proposal — Falsifier Text for the 40 Standing Absences, and the Annotation Profile Question (2026-11-27)

**Status: PROPOSAL ONLY. Nothing in this record is applied.**
This record proposes; it does not adjudicate, author, or
amend. The claims ledger is untouched by this record (its
state is attested in §7), no entry in it is edited, and no
standing, verdict, or tally moves. The owner adjudicates
this packet before any change is made anywhere. Any
adoption would be executed afterwards, as its own landing,
under the ledger's append-only amendment discipline.

## 1. Where things stand

R-IP-04 is complete: all four items ruled by the owner,
confirmed in the Glossa-Lab chat, recorded (PRs #768 and
#771), and applied on the VEXA side (AXIOVEX/vexa main
`b78c07bd`). The converted ledger's E2 state is exactly
102 failing lines: C6 ×40 ("falsifier missing or empty"),
C2 ×31 ("statement missing or empty"), C4 ×31 ("status
missing or empty"). E3 still refuses the converted ledger.
E6 (external reproduction, currently 0 of 3) now turns on
two matters on this side of the record:

- **(a)** falsifier text for 40 entries in this study's
  own source ledger: the 9 claim entries whose falsifier
  is null, and the 31 annotation entries; and
- **(b)** the annotation shape as a profile matter: the 31
  annotations' C2 and C4 lines stand because the validator
  is kind-blind and no statement or status was derived
  (deriving one was not the item 3 ruling).

**Enumeration.** The 40 entries were enumerated two
independent ways, in exact agreement: (i) the standing
divergences record committed on the VEXA side
(`specs/011-import-path/glossa/glossa-divergences.json` at
vexa main `b78c07bd`), whose C6 set is 40 entries and whose
C2 and C4 sets are the same 31 annotation entries; and
(ii) a direct census of the source ledger
(`glossa-indus/ledger/claims.jsonl` at glossa-lab main
`80484f4d`): exactly 9 entries of kind `claim` carry a null
falsifier, and exactly 31 entries are of kind
`annotation`. The two sets are identical, entry for entry.

## 2. The 40 entries

### 2.1 The 9 claims (kind `claim`, falsifier null)

All nine are extraction fragments from the Phase-104
evaluation population, migrated into the ledger on
2026-11-01. Each carries a filed explanation record that
states, in terms, that the record carries no falsification
condition. Their statements, as filed:

| # | Entry | Status | Statement (as filed) |
|---|-------|--------|----------------------|
| 1 | `ancient_writing_and_modern_technologies_51831ac9_sign_val_0001` | untested | "Sign value: 900 / number six" |
| 2 | `ancient_writing_and_modern_technologies_51831ac9_sign_val_0002` | untested | "Sign value: 700 / a volumetric system with a unit of 40" |
| 3 | `ancient_writing_and_modern_technologies_51831ac9_sign_val_0003` | untested | "Sign value: 700 / a unit of 4" |
| 4 | `ancient_writing_and_modern_technologies_51831ac9_statisti_0004` | untested | "Statistical finding: positional analysis" |
| 5 | `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0001` | contradicted | "Critique: myth of a literate Harappan" |
| 6 | `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0002` | contradicted | "Critique: collapse of the Indus script thesis" |
| 7 | `the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0001` | untested | "Sign value: 821 / it is used in a variety of contexts (Figure 6" |
| 8 | `the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0002` | untested | "Sign value: 297 / the horned tiger, or perhaps just 'tiger' generically" |
| 9 | `without_kings_or_conquests_the_indus_scr_ce9d98cc_language_0001` | contradicted | "Language hypothesis: non-linguistic symbol" |

### 2.2 The 31 annotations (kind `annotation`)

Each annotation is a research-check bearing record: it
carries a target claim, a dated check (all 31 checked
2026-10-22 under the filed audit protocol), a bearing
summary (gaps found; neighbours surfaced; verdict null in
all 31), and a sidecar pointer to the check's own record
file. It carries no statement, no status, and no falsifier
— by kind, not by omission (see §5). Targets:

| Entry (suffix after `annotation/`) | Target claim |
|---|---|
| `ancient_writing_and_modern_technologies_51831ac9__ancient_writing_and_modern_technologies_51831ac9_sign_val_0001` | `ancient_writing_and_modern_technologies_51831ac9_sign_val_0001` |
| `ancient_writing_and_modern_technologies_51831ac9__ancient_writing_and_modern_technologies_51831ac9_sign_val_0002` | `ancient_writing_and_modern_technologies_51831ac9_sign_val_0002` |
| `ancient_writing_and_modern_technologies_51831ac9__ancient_writing_and_modern_technologies_51831ac9_sign_val_0003` | `ancient_writing_and_modern_technologies_51831ac9_sign_val_0003` |
| `ancient_writing_and_modern_technologies_51831ac9__ancient_writing_and_modern_technologies_51831ac9_statisti_0004` | `ancient_writing_and_modern_technologies_51831ac9_statisti_0004` |
| `farmer_sproat_witzel_2004__farmer_sproat_witzel_2004_manual_001` | `farmer_sproat_witzel_2004_manual_001` |
| `fuls2023_catalog_of_indussigns_searchins_1dbdecdb__fuls2023_catalog_of_indussigns_searchins_1dbdecdb_statisti_0001` | `fuls2023_catalog_of_indussigns_searchins_1dbdecdb_statisti_0001` |
| `indus_valley_script_deciphered_from_myth_65ff0a26__indus_valley_script_deciphered_from_myth_65ff0a26_critique_0001` | `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0001` |
| `indus_valley_script_deciphered_from_myth_65ff0a26__indus_valley_script_deciphered_from_myth_65ff0a26_critique_0002` | `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0002` |
| `indus_valley_script_deciphered_from_myth_65ff0a26__indus_valley_script_deciphered_from_myth_65ff0a26_manual_001` | `indus_valley_script_deciphered_from_myth_65ff0a26_manual_001` |
| `indus_valley_script_deciphered_from_myth_65ff0a26__indus_valley_script_deciphered_from_myth_65ff0a26_manual_002` | `indus_valley_script_deciphered_from_myth_65ff0a26_manual_002` |
| `indus_valley_script_deciphered_from_myth_65ff0a26__indus_valley_script_deciphered_from_myth_65ff0a26_manual_003` | `indus_valley_script_deciphered_from_myth_65ff0a26_manual_003` |
| `indus_valley_script_deciphered_from_myth_65ff0a26__indus_valley_script_deciphered_from_myth_65ff0a26_manual_004` | `indus_valley_script_deciphered_from_myth_65ff0a26_manual_004` |
| `parpola_2010_dravidian_solution__parpola_2010_dravidian_solution_manual_001` | `parpola_2010_dravidian_solution_manual_001` |
| `parpola_2010_dravidian_solution__parpola_2010_dravidian_solution_manual_002` | `parpola_2010_dravidian_solution_manual_002` |
| `positional_analysis_of_indus_signs_a2bedc93__positional_analysis_of_indus_signs_a2bedc93_statisti_0001` | `positional_analysis_of_indus_signs_a2bedc93_statisti_0001` |
| `the_archaeology_and_epigraphy_of_indus_w_27f45a68__the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0001` | `the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0001` |
| `the_archaeology_and_epigraphy_of_indus_w_27f45a68__the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0002` | `the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0002` |
| `the_archaeology_and_epigraphy_of_indus_w_27f45a68__the_archaeology_and_epigraphy_of_indus_w_27f45a68_statisti_0003` | `the_archaeology_and_epigraphy_of_indus_w_27f45a68_statisti_0003` |
| `without_kings_or_conquests_the_indus_scr_ce9d98cc__without_kings_or_conquests_the_indus_scr_ce9d98cc_critique_0003` | `without_kings_or_conquests_the_indus_scr_ce9d98cc_critique_0003` |
| `without_kings_or_conquests_the_indus_scr_ce9d98cc__without_kings_or_conquests_the_indus_scr_ce9d98cc_critique_0004` | `without_kings_or_conquests_the_indus_scr_ce9d98cc_critique_0004` |
| `without_kings_or_conquests_the_indus_scr_ce9d98cc__without_kings_or_conquests_the_indus_scr_ce9d98cc_language_0001` | `without_kings_or_conquests_the_indus_scr_ce9d98cc_language_0001` |
| `without_kings_or_conquests_the_indus_scr_ce9d98cc__without_kings_or_conquests_the_indus_scr_ce9d98cc_manual_001` | `without_kings_or_conquests_the_indus_scr_ce9d98cc_manual_001` |
| `without_kings_or_conquests_the_indus_scr_ce9d98cc__without_kings_or_conquests_the_indus_scr_ce9d98cc_manual_002` | `without_kings_or_conquests_the_indus_scr_ce9d98cc_manual_002` |
| `without_kings_or_conquests_the_indus_scr_ce9d98cc__without_kings_or_conquests_the_indus_scr_ce9d98cc_manual_003` | `without_kings_or_conquests_the_indus_scr_ce9d98cc_manual_003` |
| `without_kings_or_conquests_the_indus_scr_ce9d98cc__without_kings_or_conquests_the_indus_scr_ce9d98cc_manual_004` | `without_kings_or_conquests_the_indus_scr_ce9d98cc_manual_004` |
| `without_kings_or_conquests_the_indus_scr_ce9d98cc__without_kings_or_conquests_the_indus_scr_ce9d98cc_manual_005` | `without_kings_or_conquests_the_indus_scr_ce9d98cc_manual_005` |
| `without_kings_or_conquests_the_indus_scr_ce9d98cc__without_kings_or_conquests_the_indus_scr_ce9d98cc_statisti_0002` | `without_kings_or_conquests_the_indus_scr_ce9d98cc_statisti_0002` |
| `yadav_2009_arxiv__yadav_2009_arxiv_manual_001` | `yadav_2009_arxiv_manual_001` |
| `yadav_2009_arxiv__yadav_2009_arxiv_manual_002` | `yadav_2009_arxiv_manual_002` |
| `yadav_2010_ngrams__yadav_2010_ngrams_manual_001` | `yadav_2010_ngrams_manual_001` |
| `yadav_2010_ngrams__yadav_2010_ngrams_manual_002` | `yadav_2010_ngrams_manual_002` |

## 3. The decision this packet puts to the owner

Item 1, as ruled and refined, says of the true absences:
they stand as recorded divergences, and no falsifier text
is to be authored after the fact. E6 readiness, as the
applied record frames it, turns on falsifier text for
these entries. Both cannot be satisfied at once for the
same entry. This packet therefore does two things only:

- it drafts candidate falsifier texts for the 9 claims,
  to the program's drafting standard, so the owner can
  judge whether any of them deserves to exist; and
- it sets out the annotation profile options without
  deciding them.

Adopting any draft would supersede item 1 in part, for
that entry only, by the owner's own act. If adopted, a
falsifier would enter the record only as a dated,
append-only amendment under the ledger's own discipline,
provenance-marked as authored after the fact (2026-11-27),
never as an edit to the original entry and never
backdated. If the owner holds item 1, the drafts lapse
and the absences stand; E6's design on the VEXA side would
then have to treat the standing C6 divergences as a
declared input, or E6 stays blocked on them. The drafting
standard applied in §4: a proposed falsifier must
(a) be expressed in terms of evidence that was available
in principle when the claim was registered (2026-11-01;
the source documents and the held corpus predate it),
(b) state a condition that would have refuted the claim
had it obtained, and (c) not merely negate the statement.
Where no text meets that standard from the claim's filed
basis, §4 says so and does not force one.

## 4. The 9 claims, one by one

A structural fact governs most of what follows. Five of
the nine are single cells lifted by automatic extraction
from tables in published source documents, with the sign
list unnamed: on their filed basis, the sign a number
refers to cannot be identified, so no corpus-level test of
the value was ever possible from the record. For those,
the only falsifier honestly draftable is at the level the
record supports — the record's fidelity to its source —
and each draft says so. Three are headings or labels that
the program's Phase-104 evaluation read as restating one
identifiable thesis; their drafts are conditional on that
reading, and the condition is stated on each. One states
no proposition at all.

### 4.1 `ancient_writing_and_modern_technologies_51831ac9_sign_val_0001` — draft offered (extraction level)

Statement: "Sign value: 900 / number six". Filed basis:
an extraction fragment; the sign list is unnamed, no
matching entry exists in the repository's crosswalk
registry, and the record's own account says what would
change the picture: the source table re-extracted with
its sign list named, at which point the record would
become checkable against the corpus.

**Proposed falsifier:** "Re-extraction of the source
table in 'Ancient Writing and Modern Technologies' (the
table this fragment was extracted from, its sign list
identified) showing the entry numbered 900 does not carry
the value 'number six' — the cell absent, the number
unused, or a different value printed."

Level and caveat: this tests the record against its
source, not the value against the corpus. No corpus-level
falsifier is draftable from the filed basis, because the
basis does not identify which sign "900" is.

### 4.2 `ancient_writing_and_modern_technologies_51831ac9_sign_val_0002` — draft offered (extraction level)

Statement: "Sign value: 700 / a volumetric system with a
unit of 40". Filed basis: an extraction fragment, sign
list unnamed; the record carries an unresolved
contradiction with its sibling (§4.3), which assigns the
same sign number a unit of 4. Both cannot be right as
stated.

**Proposed falsifier:** "Re-extraction of the source
table (its sign list identified) showing the entry
numbered 700 carries no volumetric value, or carries the
unit of 4 stated by the sibling fragment sign_val_0003
instead of a volumetric system with a unit of 40."

### 4.3 `ancient_writing_and_modern_technologies_51831ac9_sign_val_0003` — draft offered (extraction level)

Statement: "Sign value: 700 / a unit of 4". Filed basis:
the other side of the same unresolved contradiction.

**Proposed falsifier:** "Re-extraction of the source
table (its sign list identified) showing the entry
numbered 700 carries no unit of 4, or carries instead the
volumetric system with a unit of 40 stated by the sibling
fragment sign_val_0002."

Pair note (§§4.2–4.3): a single re-extraction decides
both fragments, and at most one of the pair can survive
it. The drafts are mirror images because the filed
contradiction is.

### 4.4 `ancient_writing_and_modern_technologies_51831ac9_statisti_0004` — NO HONEST FALSIFIER DRAFTABLE

Statement: "Statistical finding: positional analysis".
Filed basis, in the record's own words: "There is no
claim here to explain. Phase-104's evaluation says it
exactly: an automatic-extraction fragment with no
falsification condition and no stated proposition — not
evaluable as stated. The extraction kept the heading of a
results section and lost the results."

Reason: a falsifier presupposes a proposition that
evidence could count against. This statement is a section
heading spanning five source documents; it asserts
nothing any evidence could refute. Drafting a falsifier
would require first choosing which of the five passages'
findings the fragment "claims" — that is authoring a
claim, not a falsifier, and it would fabricate the very
content the record states is absent. The remedy the
record itself names is a different act, put to the owner
in §6 as a disposition, not a falsifier: re-extract the
five source passages in full, each becoming its own claim
with its numbers attached, or retire this fragment as an
extraction artefact.

### 4.5 `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0001` — draft offered (conditional)

Statement: "Critique: myth of a literate Harappan".
Status: contradicted. Filed basis: the fragment is a
section heading, but the program's Phase-104 evaluation
read it as restating an identifiable claim — the Farmer,
Sproat and Witzel thesis that the signs do not encode
language — and that thesis stands in this same ledger as
a full proposition on the companion record
`farmer_sproat_witzel_2004_manual_001` ("The Indus script
is not a writing system encoding language but consists of
non-linguistic symbols"), which carries a filed falsifier
of the content drafted below.

**Proposed falsifier:** "Conditional entropy of the sign
sequences in the corpus held at registration falling in
the linguistic range, with positional patterning above
the random baseline."

Basis: the proposition is the same, so the falsifying
condition is the same in substance as the companion
record's filed falsifier; the evidence (corpus entropy
and positional statistics) was available in principle at
registration; had it obtained, it would refute the
thesis; and it names measurable quantities rather than
negating the statement. Condition: the draft attaches
only if the owner accepts the evaluation's reading as
this fragment's proposition. If he does not, the fragment
as filed states no proposition of its own and this claim
joins §4.4 as NO HONEST FALSIFIER DRAFTABLE. Note: the
claim already stands contradicted; the falsifier would
record the condition that counts against it, not change
any verdict.

### 4.6 `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0002` — draft offered (conditional)

Statement: "Critique: collapse of the Indus script
thesis". Status: contradicted. Filed basis: the same
evaluation reading, the same thesis, the same companion
record; the filed basis for the pair states the two
fragments should be decided together.

**Proposed falsifier:** "Conditional entropy of the sign
sequences in the corpus held at registration falling in
the linguistic range, with positional patterning above
the random baseline."

The condition and note of §4.5 apply identically.

### 4.7 `the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0001` — draft offered (extraction level only; value clause unfalsifiable)

Statement: "Sign value: 821 / it is used in a variety of
contexts (Figure 6". Filed basis: an extraction fragment,
sign list unnamed; and the filed evaluation's judgement
on the value clause itself: "'used in a variety of
contexts' states nothing that could fail: almost any
common sign is used in a variety of contexts."

**Proposed falsifier:** "Re-extraction of the source
table in 'The Archaeology and Epigraphy of Indus Writing'
(its sign list identified) showing the entry numbered 821
does not carry the note 'used in a variety of contexts' —
the cell absent, the number unused, or a different note
printed."

Caveat, on the face of the draft: it covers only the
record's fidelity to its source. For the value clause
itself, no honest falsifier is draftable, for the reason
the filed evaluation gives: as stated, it could not fail
on any evidence.

### 4.8 `the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0002` — draft offered (identification level)

Statement: "Sign value: 297 / the horned tiger, or
perhaps just 'tiger' generically". Filed basis: an
extraction fragment, but the filed evaluation singles
this one out: "this one is at least the kind of statement
that could be checked — sign identifications can be
compared against sign images — but not from this record:
with the sign list unnamed, the drawn sign cannot be
located."

**Proposed falsifier:** "Identification of the source's
sign list showing the sign numbered 297 is not a horned
tiger or a tiger: its drawn form in the identified list
depicts a different subject."

Level: this is a claim-level falsifier, not only an
extraction-level one — the identification is the claim —
conditional only on the identification step the record
itself names, against a source that existed at
registration.

### 4.9 `without_kings_or_conquests_the_indus_scr_ce9d98cc_language_0001` — draft offered (conditional)

Statement: "Language hypothesis: non-linguistic symbol".
Status: contradicted. Filed basis: a category tag
extracted as if it were a claim; the Phase-104 evaluation
read it as restating the same Farmer–Sproat–Witzel
thesis, on the same companion record.

**Proposed falsifier:** "Conditional entropy of the sign
sequences in the corpus held at registration falling in
the linguistic range, with positional patterning above
the random baseline."

The condition and note of §4.5 apply identically. The
filed basis raises one further question this packet does
not take up: whether other extraction labels are sitting
in the claim set as propositions in the same way. That
sweep, if wanted, is its own commission.

### 4.10 Summary of §4

Drafts offered for 8 of the 9 claims: three at extraction
level (§§4.1–4.3), one at extraction level with its value
clause expressly unfalsifiable (§4.7), one at
identification level (§4.8), and three conditional on the
owner accepting the Phase-104 evaluation's reading as the
fragment's proposition (§§4.5, 4.6, 4.9). One claim
(§4.4) has NO HONEST FALSIFIER DRAFTABLE, and the three
conditional drafts fall to the same verdict if their
condition is refused.

## 5. The annotation profile question

### 5.1 What an annotation is, on the record

An annotation entry carries exactly these fields: `id`,
`kind`, `date`, `migration`, `target_claim_id`,
`canonical_claim_id`, `bearing`, and `sidecar`. The
bearing records that an advisory research check ran
against the target claim on 2026-10-22 under the filed
audit protocol (`docs/paper-search-mcp.md#audit-protocol`),
how many gaps it found (1 in 28 of the 31; 2 in 3), how
many neighbours it surfaced (0 to 34), and a verdict
(null in all 31). The check's content lives in the sidecar
research-check file the entry points to, by path and
SHA-256. An annotation is therefore a bearing record — a
dated pointer recording that a check ran and what it
surfaced — not a proposition. It has no statement because
it asserts nothing; it has no status because it is not
the kind of thing that is supported or contradicted; and
a falsifier for it is not merely absent but category-less:
nothing could count "against" the fact that a check ran,
other than the check record itself being wrong, which is
what the sidecar's hash and the bearing's own fields are
there to show.

### 5.2 Why the 93 annotation lines stand

- C2 ×31 and C4 ×31 stand because `validate_ledger`
  applies claim-shape checks to every entry regardless of
  kind. The conversion profile already declares the
  annotation shape (statement and status omitted rather
  than nulled), but the validator is kind-blind, so the
  declared shape still fails its checks. The defect, on
  the record, sits in the validator's scope, not in the
  entries.
- C6 ×31 stands under item 1: the annotations' falsifier
  share was counted among the true absences, and the
  ruling stands them as recorded divergences.

### 5.3 Options

**Option A — annotations acquire claim-like fields.**
Author statement, status, and falsifier text for the 31
annotations so the kind-blind validator passes.
Consequences: E2 could pass on these lines, and E3/E6
would unblock on them — but by misdescribing the kind.
Item 3 ruled the annotations are not defective claims;
the application record states expressly that deriving a
statement or status "was not the ruling". A statement for
a bearing record would have to be manufactured (some form
of "a research check ran"), and a falsifier for it would
be decoration: text that no evidence could ever engage.
It also reverses the direction of the whole R-IP-04
exercise, which cleared lines on their merits or stood
them honestly, and never by redescribing a record.

**Option B — kind-aware gates under a declared profile.**
The annotation profile declares statement, status, and
falsifier not-applicable for the kind — a first-class
declared shape, pinned in the profile — and E2's
validator becomes kind-aware: C2, C4, and C6 apply to
claims; for annotations the gate checks what the kind
actually carries (target present, sidecar present and
hash-matching, bearing present, provenance projectable
from the sidecar). Consequences: E2 can pass or fail on
what the records actually are; E3's refusal lifts on a
truthful basis; E6 then reproduces the ledger including
its annotation kind as filed. Costs: the validator change
is VEXA-side work (`validate_ledger` is theirs), and the
kind-scoping must itself be pinned and auditable, so it
reads as a declared shape and not as a waiver list.
Sub-question on C6, which only the owner can settle,
because item 1 counted the annotations' falsifier share
among the standing true absences: **B1** scopes only C2
and C4 by kind, leaving the C6 annotation lines standing
under item 1 (E2 then still fails on C6 ×31 plus whatever
of the 9 claims remains unresolved); **B2** declares
falsifier not-applicable for the annotation kind as well,
retiring the C6 annotation lines as a shape declaration —
which qualifies item 1 for the annotation share and so
needs the owner's ruling in terms.

**Option C — annotations carried outside the gated
population.** Conversion carries the 31 annotations in a
separate annex not subject to E2's entry checks.
Consequences: E2's scope shrinks to 1,060 of 1,091
entries; the coverage accounting that currently matches
E5 exactly would change; and E6 would reproduce the gated
population with 31 records carried outside the gate —
a weaker reproduction claim, and one that sits badly with
item 3, which gave the annotations their own profile
inside the ledger, not exile from it.

### 5.4 Recommendation (not a decision)

**Option B**, with the C6 sub-question put to the owner
as B1 versus B2. Reasons: (1) It is the only option under
which E2, E3, and E6 pass or fail on what the records
actually are; A passes by misdescription and C by
exclusion. (2) It is item 3's ruling carried to its
mechanical conclusion: a kind that stands under its own
profile must be validated under its own profile; the
kind-blindness is a property of the validator, and the
program's standing practice is to fix the instrument
rather than redescribe the record. (3) It authors no
after-the-fact text into any entry, so it does not touch
item 1 for the claims; and for the annotations it forces
the item 1 question into the open as B1/B2 instead of
settling it by a tooling change. (4) The Glossa-side part
is small: the conversion profile already declares the
annotation shape; B adds the gate-scoping statement to
that declaration. The validator change itself is
commissioned and executed on the VEXA side, not here.

## 6. What is asked of the owner

1. **The 9 claims (§4), as a block or entry by entry:**
   hold item 1 for all (the drafts lapse; the absences
   stand), or adopt the drafts offered — and, for the
   three conditional drafts (§§4.5, 4.6, 4.9), rule
   whether the Phase-104 evaluation's reading is accepted
   as those fragments' proposition. Any adoption enters
   only as a dated, append-only, provenance-marked
   amendment; the mechanism and its landing are a separate
   execution, not part of this packet.
2. **§4.4's disposition** (independent of falsifiers):
   re-extract the five source passages as their own
   claims, retire the fragment as an extraction artefact,
   or leave it standing as filed.
3. **The annotation question (§5):** option A, B, or C —
   and under B, B1 or B2 on the C6 annotation share.

Nothing in this record is applied. Until the owner rules,
the converted ledger's E2 stands at exactly 102 lines, E3
keeps refusing it, and E6 cannot run.

## 7. Attestation — the ledger was not modified

This packet was prepared read-only against the ledger at
glossa-lab main `80484f4d`: `glossa-indus/ledger/
claims.jsonl`, 1,098 lines, content SHA-256
`fd4d12e73b0df3ad2d9311772b506b1f0a9e10da4ec156f9456d24fb109d7abc`
(blob `098d6fb74f91201f86dab94dd45a1db5d90c31e7`).
Falsifier coverage at that head: 1,057 of 1,066 claims
carry falsifier text; the 9 that do not are §2.1's. The
landing that files this record changes no ledger file;
the ledger's line count and hash were re-verified
identical after the landing, and the verification result
is carried in the landing's report and in PROGRAM-STATE.

Rests on: `records/r-ip-04-adjudication-2026-11-26.md`;
the source ledger at main `80484f4d`; the VEXA-side
divergence and profile records at AXIOVEX/vexa main
`b78c07bd` (`specs/011-import-path/glossa/
glossa-divergences.json`, `glossa-profile.json`); the nine
entries' filed explanation records in the ledger itself.
