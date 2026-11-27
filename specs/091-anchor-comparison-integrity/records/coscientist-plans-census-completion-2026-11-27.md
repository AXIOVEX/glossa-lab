# Co-scientist Plans Census — Completion Record (2026-11-27)

**Kind:** CENSUS AND APPLICATION RECORD. **Actor:** the
Glossa-Lab chat's census coordinator and the landing worker,
under the owner's instruction of 2026-11-27 (09:31 ET):
"Look at coscientist plans for all our work in academia and
apply every single plan we haven't applied yet."

**BOOKKEEPING ONLY:** this record compiles the census of the
Co-scientist recommendations ledger's unapplied rows and the
application of the applicable ones. It adjudicates nothing
and changes no standing, class, verdict, or tally. Where a
row's status changes in the ledger, it changes because the
act the row called for is verified complete on the record
cited, under the ledger's own rule that nothing is marked
done from a summary.

## 1. Authorization chain

- Owner's blanket approval of 2026-11-27 (04:05 ET), covering
  the program's outstanding commissions.
- Owner's instruction of 2026-11-27 (09:31 ET), quoted above:
  the commission for this census and application.
- Census completed 2026-11-27 (09:37 ET) against main
  `3b8503f0` (merge of PR #794).
- The application phase's first fresh clone
  (`coscientist-apply-20261127`) tripped the runtime
  execution-risk flag at creation; the owner cleared work
  inside that clone by name, after its trip, on 2026-11-27
  (09:58 ET). Both application landings executed inside it
  under that clearance.

## 2. The census

Source of record: the Co-scientist recommendations ledger
(`records/coscientist-recommendations-ledger.md`). A sweep
for unledgered recommendation lists found none: every
Co-scientist adjudication record in this spec's records
corresponds to a ledger section, the three programs' records
folders (Specs 096, 097, 101) hold program-internal
adjudications rather than unledgered Co-scientist lists, and
the Round P owner decisions (OD-P-1..4) carry no rows by the
standing precedent that owner decisions are not
recommendations.

**Recount reconciliation.** The census's interim count read
159 rows (107 done / 31 accepted / 0 open / 21 rejected).
Before the application landing, the ledger was recounted
from its data rows on the main the landing stands on:
**158 rows — 106 done / 31 accepted / 0 open / 21 rejected**,
agreeing with the ledger's own last stated totals (after
Round P) and with its git history, which shows no change to
the ledger between the Round P landing and this census. The
interim count's one extra done row was a counting artifact
of the census, not a concurrent landing; the recount from
the data rows governs, and all figures below stand on it.

The 31 accepted rows, classified:

### (A) Already applied in substance — the ledger correction is the only act owed (6)

- **A-9** (Indus bridge = top gap). A direction item; its
  adoption is its complete act. Adopted in the Round A
  adjudication §5 point 1 and restated as standing priority
  by OD-2 (PR #678).
- **B-I-18** (OD-2 priority). Same substance as A-9; OWNER
  DECISION OD-2 adopted 2026-11-22 (PR #678 addendum);
  carried as the standing gap ordering in the World
  Language Graph gap register (PR #783).
- **C-E-16** (confusable-name discrimination). Filed
  verbatim as a binding amendment in
  `records/coscientist-release-round-c-assessment-adjudication-2026-11-23.md`:
  an amendment to the conditions, binding on any future
  registration of an E1-form test. The filing was the act.
- **C-E-18** (Spec 101 uncertainty/selection transparency).
  The one surviving gap, damaged/restored treatment at
  counting, was closed by
  `specs/101-eteocypriot-next-claim/records/freeze-addendum-2026-11-27.md`
  Table 3 (the unread marker counts as no candidate's final
  sign; changed-reading flags do not alter a sign's label),
  filed under cycle 1 before any scoring; execution landed
  PR #770.
- **B-M-19** (OD-22 canonical wording). Adoption recorded
  2026-11-22 (PR #697, merge `bb890fda`). The adoption is
  the act; the wording takes effect only when release
  conditions are satisfied, and the internal-use ruling
  stands meanwhile — that condition is noted on the row,
  not outstanding work.
- **C-M-22** (semantic-discrimination calibration
  direction). "Accepted as the direction for a future
  registration; no study is commissioned by this
  adjudication" (Round C assessment adjudication). Adoption
  as standing direction is the complete act the item calls
  for.

### (B) Applicable now — applied by this landing (4)

- **C-M-9** (refusal protocol: dissemination copies). Filed
  as a supplement to the OD-14 protocol:
  `specs/097-meroitic-reproduction-benchmark/records/custody-clarification-refusal-protocol-supplement-2026-11-27.md`,
  naming the deposited paper's dissemination copies (Zenodo
  versions, Academia listing, supplementary material,
  public summaries) and the linked-notice /
  repository-notification route where a version cannot be
  removed. Row closed done on that filing.
- **C-M-20** (Rilly-challenge five-step protocol). The five
  steps filed verbatim from the Round C adjudication as a
  supplement to the OD-18 preparation record:
  `specs/097-meroitic-reproduction-benchmark/records/od18-expert-verification-preparation-supplement-2026-11-27.md`.
  Row closed done on that filing.
- **C-M-14** (Spec 102 power calibration under
  heterogeneity). Verified gap at census: the armed
  execution registration (PR #786,
  `specs/102-meroitic-fresh-affiliation-test/records/execution-registration-2026-11-27.md`)
  contained no heterogeneity or missingness provision.
  Applied as a freeze-stage addendum to that registration,
  binding G-2 to also run under heterogeneous per-concept
  detection rates and a stated missingness pattern, filed
  with the power statement; gates unchanged, none lowered.
  The runs themselves execute at the Spec 102 freeze; the
  row's ledger note cites the addendum as the binding
  instrument and the row stays accepted.
- **C-M-21** (effective evidential units: 652 / 396 / 368).
  Applied as a registration of the combined study in Spec
  097's records:
  `specs/097-meroitic-reproduction-benchmark/records/effective-evidential-units-registration-2026-11-27.md`,
  with its falsifiers stated at registration. Registration
  is the discipline-correct application step; the
  computation itself is the registered study and is not
  claimed as done. The row's ledger note cites the
  registration and the row stays accepted.

### (C) In flight under another running commission (2)

- **C-E-15** (alignment-line feasibility decision). Cycle
  2's E-2 leg (complete C-E-15 to proceed/stop); its
  registration landed as PR #794 (merge `3b8503f0`). Not
  duplicated.
- **B-M-18** (register a fresh affiliation test after the
  preceding checks, OD-21). Spec 102: registered, execution
  registration landed PR #786, test ARMED. Trigger is the
  arrival of Rilly 2010 (Peeters order `6b0851920a66f`) and
  its digitisation. C-M-14's addendum attaches to this same
  freeze.

### (D) Gated on a reserved category — not applied (19)

Paper-text items, packaged for the papers' next owner-ruled
revision round (the owner rules on paper text):

- Eteocypriot package: C-E-1 (E-P1), C-E-4 (E-P2), C-E-5
  (E-P3 — its title element is already closed by the owner's
  2026-11-26 ruling retaining the title; the abstract
  element remains), C-E-7 (E-P4 — record half already
  resolved by the OD-8 audit, finding F-4), C-E-8 (E-P5 —
  citation form adopted in the adjudication; carrying it
  into the paper remains), C-E-11 (E-P7).
- Meroitic package: C-M-3 (M-P1), C-M-5 (M-P2), C-M-6
  (M-P3), C-M-7 (M-P4), C-M-16 (M-P5 — its design-rule half
  is already filed in the adjudication), C-M-18 (M-P6),
  C-M-19 (M-P7).

Gated on the Spec 100 / Miller track (the deposit is held
until Miller's reply on the Holdat F-1 track; Spec 100
execution is separately owner-gated):

- A-13 and B-I-21 — the remedy for both is Spec 100
  (deposit the per-seal join, rerun the 13 motif claims).

Gated on an external scholar's outstanding work:

- A-14 — program side complete (letters sent 2026-11-19;
  Kobayashi's coding received and compared at T501,
  producing M047); Kolichala's coding remains outstanding
  and rests with the scholar.
- C-E-19 (OD-C-3) — the Androkles second-reader letter to
  Professor Philippa Steele was sent 2026-11-23; the check
  rests with her reply. The ICS 196 half is in motion
  through the interlibrary route.

Gated on a pending owner decision (the owner's pick of a
person):

- B-E-9 (OD-11 replacement checker) — the check stands
  declined by de Voogt; the owner decided the replacement
  route (a fresh external epigrapher) on 2026-11-23, and
  the row stands pending the owner's pick of the person
  (candidates in
  `specs/096-eteocypriot-program/records/od-11-replacement-checker-decision-2026-11-23.md`).
- C-M-23 (OD-C-4 external replay) — commissioned
  2026-11-23, hand-off prepared, candidates proposed
  (CODECHECK; de Voogt; ReScience C); engaging the
  reproducer is an external engagement awaiting the owner's
  word on whom. Nothing sent.

### (E) Superseded or moot (0)

None of the 31. The three direction-only items (A-9, B-I-18,
C-M-22) are classified (A) rather than (E) because their
adoption is on the record and is the whole of what they call
for.

**Postscript (same day).** While this application was
landing, cycle 2's execution landed as PR #796: C-E-15's
leg executed and its outcome — STOP, no candidate set
satisfies all four registered conditions — is recorded on
its ledger row by that landing. The classification above
stands as of the census (09:37 ET), when the leg was in
flight; nothing in this record is altered by the outcome,
and the row's own evidence now carries it.

## 3. Resulting ledger state

After this application landing, recounted from the data
rows: **158 rows — 114 done / 23 accepted / 0 open / 21
rejected**. The eight rows closed done are the six (A) rows
and C-M-9 and C-M-20; the two (B) instrument rows (C-M-14,
C-M-21) stay accepted with their notes citing the binding
instruments; the two (C) rows and nineteen (D) rows are
unchanged.

**AI disclosure:** this record was compiled by an AI agent
(Muse, via Muse) at the direction of Tristen Pierson,
per constitution sec. VI. It compiles a census and its
application; it adjudicates nothing and changes no standing,
class, verdict, or tally.
