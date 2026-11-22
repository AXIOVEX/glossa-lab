# Eteocypriot Program — Outcome Record Amendment 2

**Date:** 2026-11-21. **Program:** Spec 096 — Eteocypriot
Program. **Amends:** the outcome record of 2026-11-20
(`records/eteocypriot-outcome-record-2026-11-20.md`) and its
amendment of the same date
(`records/outcome-record-amendment-2026-11-20.md`). Filed
under Red Team Round 1 (findings RT1-05, RT1-06, RT1-07,
RT1-22, RT1-23, RT1-24, RT1-25, RT1-26, RT1-27, RT1-42,
RT1-43, RT1-55), adjudicated 2026-11-21.

This is a record-only amendment. It alters no filed text, no
run record, and no ledger standing. Where it corrects a
citation form, the corrected form governs citation from this
record onward.

> **Adjudication pointer (2026-11-22):** the condition §6
> states is discharged. The approver named there, the
> program owner, Tristen Pierson, adjudicated the four
> verdicts as proposed on 2026-11-22
> (`records/adjudication-record-2026-11-22.md`). §6's
> discipline ("proposed verdicts, unadjudicated; ledger
> standings unchanged") no longer applies as to the
> verdicts' status; ledger standings remain unchanged. §6
> stands as the history of the naming and of the wait.

## 1. A1 relabelled; C096-1's citation form corrected (RT1-05)

The outcome record reports "A1 (strict segment-parallel):
0 of 2 recovered." Verified at the driver source
(`records/eteocypriot-e1-driver.py`, lines 165–167): A1
recovery is computed as `greek_word_index == segment_index`.
No segment content is consulted. Against the frozen ground
truth (Greek words 5/6 ↔ segments 6/7), the 0/2 outcome was
predetermined by the indices alone, for any bilingual: the
leg as implemented is a pure index-offset check, and its
result states only that the frozen correspondence is offset
by one position.

From this record onward A1 is cited only in that form:
**"A1 (index-offset check): 0 of 2 — predetermined by the
frozen indices; not evidence about the alignment
procedure."** C096-1's NOT SUPPORTED verdict stands, and its
citation form is corrected: the verdict rests on A2 (1 of 2)
and on the floors as decomposed in the 2026-11-20 amendment,
not on A1 as a test of derivation.

Recorded as a deviation: A2 as executed is not the
preregistration §5 test. The preregistration's A2 is
"name-anchored"; the freeze and the driver score an unanchored
argmax-LCCS. The substitution was nowhere recorded as a
deviation before the run. It is recorded here, after it.

## 2. The decomposition is post hoc, stated plainly (RT1-06)

Freeze §6 states on its own face: "P1 cannot pass as
registered, whatever the ICS 196 leg scores" — the Androkles
conjunct of C096-1 was TOO THIN at freeze, so the claim's pass
was impossible before E1 ran. The decomposition of C096-1
that states this was produced after the verdict, on red-team
prompting, and filed as the 2026-11-20 amendment, whose own
Authority paragraph cites the red-team findings (F-04, F-10)
that specified it. The decomposition is correct on the
record's own terms. It is also post-hoc repair, and both
facts travel with it wherever the verdict is cited. A
standing freeze rule against the recurrence is filed the same
day as this amendment
(`records/standing-freeze-rule-2026-11-21.md`).

## 3. C096-4: qualifier on the verdict line; falsifier
## adjudicated (RT1-07)

The verdict line, wherever C096-4 is stated from this record
onward, carries its qualifier: **"C096-4 SUPPORTED — process
claim, self-assessed, pending named-human adjudication."**
The outcome record §4's bare "SUPPORTED" is superseded as a
citation form by this line.

The finding's second leg is adjudicated explicitly. C096-4's
falsifier has an arm for a leg recorded TOO THIN being scored
as a result. The Androkles leg was recorded TOO THIN and was
never scored as a result in its own right: **the falsifier's
arm is NOT FIRED in its letter.** But the leg's TOO THIN
status did verdict-work, as a constituent ground of C096-1's
NOT SUPPORTED: **the arm is ENGAGED in its substance.**
Accordingly C096-4's SUPPORTED is narrowed on the record to
what it can honestly cover: **the pilot's reporting of its
administrable leg (the ICS 196 leg: records filed, floors
stated, run byte-identically reproducible) and of its
closures.** It does not cover the correctness of the
procedure the pilot administered — §1 and §4 of this
amendment are the counterexamples.

## 4. Binding conditions on any E1 re-run (RT1-22)

Verified at the driver source: the derivation the driver
implements contains a consonant-stem table (lines 35–40) and
a dead-vowel default "a" (line 71) that appear nowhere in
freeze §5's rules R1–R3; the derived spellings diverge from
the text's actual correspondent spellings (derived
a-ri-si-to-na-ka-to-so vs segment 7's
a-ra-to-wa-na-ka-so-ko-o-se); the two test items are a name
and its own patronymic, not independent items; and no
chance/control battery exists against which 1-of-2 or 0-of-2
could be read.

No re-run of E1 is commissioned by this record. Any future
E1 re-run is bindingly conditioned on all four of:

1. a registered chance/control battery, fixed before the run;
2. independent test items (not a name and its patronymic);
3. derivation rules cited to the literature, rule by rule;
4. a freeze containing the full derivation table the driver
   implements — every table and default the code uses,
   registered before the run.

## 5. Severability, applied retrospectively (RT1-23)

The principle (stated generally in
`records/standing-freeze-rule-2026-11-21.md`): a floor closes
the smallest unit the claim's own registered structure
assigns it to; where a claim is a conjunction over legs, a
leg's floor failure closes the claim's pass and must be
decomposed at freeze; a single-leg claim's floor closes its
experiment.

Applied to Spec 096 in words: E2's floor closed its
experiment because P2 is single-leg. E1's leg floor was
treated as closing only the leg while the parent claim was
scored on the full conjunction. That asymmetry is what the
standing rule now forbids prospectively; the Spec 096
verdicts themselves stand as filed, read through §2 above.

## 6. The approver is named; adjudication outstanding (RT1-24)

No record in this spec named the adjudication approver. It
is named here: **the approver is the program owner, Tristen
Pierson** — spec.md Stage 3 prepares the adjudication package
"for the owner's approval act," and decision D-096-5 reserves
the external acts to the owner's approval. Adjudication of
the four proposed verdicts has been outstanding since
2026-11-20.

Until the owner adjudicates, every statement of the C096
verdicts carries the discipline: **"proposed verdicts,
unadjudicated; ledger standings unchanged"** — the ledger
carries C096-1..4 at draft/created, and nothing in the
outcome record, its amendments, or this amendment changes a
ledger standing. The same discipline is carried onto the
LEDGER's Spec 096 entry by the same landing as this
amendment.

## 7. Seal language downgraded; F-E2 restated (RT1-26)

Verified at the driver source (lines 110–121): the driver
parses the whole corpus file, then filters by the `split`
field. The outcome record's "held-out records loaded: 0 — the
seal was never broken" is therefore cited only in its
corrected form: **"procedural exclusion over a public corpus;
no mechanism against prior exposure; 'held-out records
loaded: 0' means excluded by the driver's split filter after
the whole file was parsed."**

Floor F-E2 is likewise cited only in its frozen form. The
floor concerns held-out **continuous text: 0 legible signs
are held.** The form-level holdings stand beside it, stated
exactly: ICS 194/195 — 45 signs in attested forms (43 legible
+ 2 damaged); ICS 193 — 5 signs; **48 legible held-out form
signs in total, and no continuous held-out text.** Any
summary that quotes F-E2 without both halves misstates the
floor in one direction or the other.

## 8. Preregistration strength; the ICS 217 control (RT1-27)

(a) The freeze's strength is stated at its limit: **the
freeze is repo-filed only, timestamped by the program's own
git history and nothing external** (freeze committed 14:48
ET, outcome 14:56 ET, 2026-11-20). Future freezes in this
program either use an external timestamped filing or do not
claim preregistration strength.

(b) The ICS 217 Greek syllabic control (66 signs, excerpt of
the Idalion tablet) was assembled as E2's comparison-rate
control. E2 closed at freeze, so the control was never used.
Its disposition, recorded here: **NOT ADMINISTERED.**

## 9. Census provenance disclosed (RT1-42)

The outcome record states that all computation ran on the
mini-server. One exception is now disclosed: **an early
census/pin computation ran in the Muse VM during corpus
assembly; it was re-computed on the mini-server and verified
identical before the freeze was filed.** The E1 run itself
ran on the mini-server, as the outcome record states; the
assembly census is the exception, and the freeze's and
outcome's unqualified venue statements are corrected by this
note. The ICS 196 census itself stands as the freeze's table:
**51 legible + 1 restored + 2 damaged = 54 signs** (freeze
§6's F-E1a line, which drops the 2 damaged signs from its
arithmetic, is corrected by this statement).

## 10. C096-2 and C096-3 citation note (RT1-43)

C096-2 (TOO THIN) and C096-3 (NOT ENGAGED) are cited with
their distinction stated out loud: **"closed / unengaged at
freeze on census grounds; falsifier never engaged."** C096-3's
NOT ENGAGED is the right label; what was missing was the
distinction, for both claims, between a floor disposition and
a tested result. Neither claim was tested. Neither standing
is a result.

## 11. Execution notes (RT1-25, RT1-55)

**RT1-25.** The corpus licensing basis as filed called
Duhoux 2009 (Kadmos 48) "public-domain scholarship," and both
Androkles records carried attalus.org SEG
`translation_of_record` strings while the same basis asserted
that no copyrighted translation is reproduced. Both are
corrected in corpus.json by the same landing as this
amendment (see `records/ics196-custody-correction-2026-11-21.md`
for the custody half): Duhoux 2009 is in-copyright scholarship
consulted via an academia.edu posting; the two translation
strings are replaced by the program's own paraphrase, marked
as such, with attalus.org SEG 32.1318 pointed to and not
reproduced; the ICS 196 `sense` field is marked as the
program's rendering; a CC BY-SA attribution note is added for
the Wikipedia-derived transcriptions. It is noted here that
the two strings were present in the corpus at E1 execution
and that **no E1 computation consumed them** — with one
fact-level exception, recorded next.

**RT1-55.** Three clarifications the finding's close
condition provides for. (i) The Hermary & Masson 1982 page
ranges: the article runs pp. 235–244; the syllabic
transcriptions stand at pp. 236–238. (ii) The Androkles
ground truth rests on **translation-level foreknowledge**:
the names as listed in the SEG translation via attalus.org;
the verbatim Greek was never held. "Androkles correspondence"
in P1 is read as a correspondence for the dedications' names
as there listed — nothing stronger was ever in hand.
(iii) The step-0 closure wording — naming a gap treated as
resolving the closure classes the preregistration defined as
closing conditions — is recorded as a defect of form; its
licensing leg is governed by the custody correction filed
the same day as this amendment.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
