# M047 (min/mīn) — F-9 itemization adjudication and execution

**Date: 2026-11-22. Filed under Red Team Round 4, finding
RT4-01, flag F-9. Authority: the owner's adoption, in the
Glossa-Lab chat on 2026-11-22, of the Round 4 adjudication's
recommendation (goal record
`RED-TEAM-ROUND-4-ADJUDICATION.md` §2(d)). This record
states the adopted rule, executes the directed
re-examination of M047's inference-log entry, applies the
consequence, and is the owner-facing summary of the act.**

## The adopted rule (the itemization test), stated prospectively

From this act forward, class E requires the
external-support claim to appear in the reading's
inference-log entry as an external-support item — a
published proposal, dictionary entry, or comparative leg
entered as such under Spec 099 §3.3 — so that the class
and the derivation cannot silently diverge. The
register-level definition of E (external-support claims on
file, unverified, NOT IDENTIFIABLE) is unchanged as a
description of what the class means; the test governs what
a filed basis must contain to hold the class. A reading
leaving E under this test is reclassed on its remaining
filed basis under the addendum rule's form
(`records/standings-relabel-execution-2026-11-21.md` §4):
class I if a filed internal candidate motivation remains,
class U if none remains. The rule is prospective. It does
not rewrite any dated filing, and it does not disturb the
addendum's strike rule (a claim contradicted by its named
source is struck) or its neighbouring arms (partial
verification and non-verifiability do not strike).

## The directed re-examination

**Question.** Should M047's inference-log entry carry the
Parpola 1994 §10.1 proposal as a `published_proposal`
item, on the same evidentiary standard M330-01 was
itemized under?

**The standard.** Under Spec 099 §§3.2–3.3, an item is
entered for each distinct evidence element the filed basis
states, and a `published_proposal` item is extracted where
the filed basis itself asserts a named published
attribution or literature attestation of the reading, the
verbatim clause standing as the item's `basis_span`.
M330's basis states "reading 'can' found in literature
(4 mentions across sources: Parpola_1994)"; M330-01 was
entered on that clause, with status NOT VERIFIABLE.
Verification outcome is no part of the itemization
standard; what the basis states is.

**Evidence, first-hand.**

1. M047's filed basis (the audit package appendix row,
   carried verbatim into the log and into
   `specs/099-inference-log/records/basis-rows-2026-11-21.json`)
   states two elements: the distributional assignment
   'par' (LOW, Round 2), overridden by the 2026-05-11
   fact-check correction; and the crosswalk identity
   "M047 = P47 = 'fish (plain)' per
   mahadevan_parpola_crosswalk.json (sourced from Parpola
   1994a + Mahadevan", at which clause the filing truncates
   mid-parenthetical. No clause of the filed basis asserts
   that Parpola, or any named source, proposed or attested
   the value mīn for this sign or for the fish signs.
2. The Parpola name in the basis is the crosswalk's
   sourcing. The crosswalk's own citation block (read
   first-hand in `research/indus/mahadevan_parpola_crosswalk.json`)
   is Mahadevan 1977, Parpola 1994a/b (the sign list,
   fig. 5.1), and Wells 2015: catalogue sources for the
   sign correspondence. Spec 099 §3.3 types that item a
   crosswalk identity — a sign identity at most, never a
   value.
3. The crosswalk's M047 entry (read first-hand) maps M047
   to Parpola 47 and Wells W008, iconic "fish (plain)",
   and carries a phoneme field, "miin". The crosswalk is a
   program-compiled, hand-curated file (Glossa-Lab
   Phase-28); its method note describes entries as ID
   mappings with cross-references; the phoneme field is
   attributed per entry to no publication or passage, and
   the filed basis does not cite it (it cites the identity
   and the gloss). The re-verification record's closing
   register adds that the filed Mahadevan citation is
   incomplete and no Mahadevan text proposing the value
   was retrieved. A program-compiled, per-entry-unattributed
   field is not a named published attribution; entering it
   as a `published_proposal` item would make the program's
   own curation the external support — the divergence the
   adopted test exists to prevent.
4. The proposal itself is real. The re-verification record
   (`records/external-support-reverification-2026-11-21.md`),
   the program's engagement with the held Parpola 1994
   text, establishes that §10.1 (pp. 179–182) proposes the
   mīn value family for the fish signs, the plain fish
   sign identified pictorially at pp. 179–180, and returned
   VERIFIED AS FILED as a prior proposal. Its two stated
   limits stand: the proposal is class-level for the
   fish-sign family and does not single out this catalogue
   sign, and the step from the crosswalk's sign identity
   to Parpola's class-level proposal is the program's own
   step. The proposal is therefore on the record as
   provenance; it is not stated in M047's filed basis as
   an attestation of this reading, and it reaches this
   sign only through the program's own step.
5. The truncation cannot be completed by inference. Spec
   099 §3.4: a basis element truncated in the filing is
   recorded as truncated, and no later act re-types or
   completes it without new filed evidence; §3.2 binds
   every item to a verbatim span of the basis as filed.
   No span in M047's basis states the proposal.

**Determination: the Parpola proposal is not entered as a
`published_proposal` item in M047's entry.** On the
standard M330-01 was itemized under, M047's basis asserts
an identity and its catalogue sourcing, and nothing more.
M047's entry therefore contains no external-support item —
its two items are a superseded positional assignment and a
crosswalk identity — and M047 does not satisfy class E
under the adopted test.

## The other three E readings under the adopted test

Verified from the landed inference log, entry by entry:

- **M124 (kuTam)** — `dictionary_entry` item (DEDR 1651)
  and two `comparative_lexical` items (Elamite 'kun',
  MC-18; Sanskrit 'kona', SL-04). Satisfies the test. Its
  re-verification outcome (PARTIALLY VERIFIED, DEDR legs
  only) is untouched.
- **M329 (poṉ)** — `dictionary_entry` item (DEDR 4524) and
  two `comparative_lexical` items (Elamite 'bur/pur',
  MC-21; Sanskrit 'pura', SL-14). Satisfies the test. The
  pura leg's failure on its checkable part stands under
  the addendum's partial-verification arm, which the
  itemization test does not disturb.
- **M330 (can)** — `published_proposal` item (M330-01, the
  literature attestation as filed). Satisfies the test. It
  would fall only under a further rule requiring partial
  verifiability of the itemized claim; that rule was not
  adopted, and M330's NOT VERIFIABLE outcome continues to
  be governed by the addendum (non-verifiability does not
  strike).

## Outcome

**M047 takes class U.** Reclassed on its remaining filed
basis under the addendum form: the 'par' assignment is a
superseded assignment of a different value, overridden
within the filed basis itself, and is not a motivation for
mīn; the crosswalk identity is a sign identity, not a
motivation for the value (the M044 adjudication's
reasoning, `records/m044-addendum-adjudication-2026-11-21.md`
finding 4). No filed internal candidate motivation for mīn
remains. The executed partition becomes **3 E + 65 I + 4 R
+ 3 P + 19 U = 94**; Arm E is M124, M329, M330.

Nothing about the re-verification outcome changes:
Parpola's §10.1 proposal stands verified as filed as a
prior proposal for the fish-sign family, and this act does
not strike it, contradict it, or decide what value, if
any, M047 carries. What changes is the class, because the
class now requires the support to be itemized in the
derivation and M047's derivation holds none.

## Downstream effects recorded

- **Spec 099.** The log's executed class for M047 follows
  the amended standings (a builder amendment arm asserted
  on the F-9 amendment's text in the standings record); no
  item is added, removed, or re-typed, and the census is
  unchanged (296 items: 210 (a) / 61 (b) / 25 ambiguous).
  The Q3 audit regenerated over the amended log returns
  every outcome unchanged (0 class changes under both
  treatments; weakened 44 / 63; acyclic): M047's outcome
  is "class unchanged" as U, as it was as E, because no
  (b) or ambiguous item stands in its entry. Record:
  `specs/099-inference-log/records/inference-log-amendment-2026-11-22.md`.
- **Spec 098.** The identifiability population (the 65
  class I readings plus the class E arm) falls from 69 to
  68 for any future stage. Stage 1's executed records
  stand as history at the populations they state; no Stage
  1 result is restated.
- **Public wording in this repo.** The root README's
  "Where the 94 stand now" paragraph and the anchor-model
  README's standings blockquote are updated in this act
  (three readings in E; M047 named among the nineteen in U
  with the reason stated; the M044 sentences untouched).
  The tracker site's corresponding correction is a
  separate publish act, not this one.

## Reopen clause

This act rests on the filed basis as it stands, including
its truncation. If the untruncated basis text, or another
filed record of the basis, is produced showing the filed
basis itself stating the Parpola proposal as an
attestation of this reading, the itemization question
reopens and M047's class is re-adjudicated on the
completed filing.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.

## Amendment, 2026-11-22 — the reopen clause broadened (OD-1)

**Authority: the owner's adoption in the Glossa-Lab chat
on 2026-11-22 (11:21 ET) of item OD-1 of the Co-scientist
refresh adjudication
(`records/coscientist-refresh-adjudication-2026-11-22.md`,
unit I-10). This amendment broadens the reopen clause
above, prospectively only. It does not rewrite the act it
amends, and it changes no current standing.**

From this amendment forward, a reading struck under the
itemization test may be reopened not only on production
of the untruncated basis, but also by entering a verified
prior proposal as a dated, source-linked basis amendment
for that sign; verification means the proposal is read in
its named source and shown to propose the reading for
that sign, and a family-level or class-level proposal
does not qualify for a sign-specific entry.

Applied to this act: no entry is made for M047 under the
broadened clause. The Parpola 1994 §10.1 proposal stands
verified as filed as a prior proposal for the fish-sign
family (the directed re-examination, item 4 above); it is
class-level for the family and does not single out this
catalogue sign, so it does not qualify as a sign-specific
entry for M047. **M047 remains class U.**

**AI disclosure:** this amendment was executed by an AI
agent (Muse, via Muse) at the direction of Tristen
Pierson, per constitution sec. VI.
