# Co-scientist sweep adjudication — Round O (2026-11-27)

Round O of the standing Co-scientist loop, run under the owner's
keep-working directive. Scope: the records and standings only;
the papers are excluded (they take their own review rounds after
the owner's text approval, under his 2026-11-27 rule). All three
briefs were pinned at `80484f4d054ef867bb7545db26215bb13b9cccd5`
(the PR #772 merge) and stated what changed since Round N: the
Spec 107 cycle-1 registration and execution (E-1 NOT SUPPORTED,
M-1 POSITIVE, I-1 INDETERMINATE), the C101-1 reclassification
(PR #772), and the R-IP-04 completion (PR #771).

Briefs (filed at the goal's
`hidden_files/coscientist-sweep-2026-11-27-round-o/`; character
length and FNV-1a over the brief text with one trailing newline
stripped, verified in the composer in the same invocation as the
fill and again in the guarded send): Indus 4,915 chars,
`afc24f91`; Eteocypriot 5,159 chars, `50798ec2`; Meroitic 4,798
chars, `714007e3`. Each session's composer was checked before
filling: the Indus composer was empty (Send disabled); no stray
draft was found in any of the three (the Round N stray-draft
incident did not recur; the Meroitic composer's pre-fill content
was not separately captured before the fill, and that is stated
here rather than smoothed over).

Captures (the sessions' own filed output documents, downloaded
through the tower automation profile and hash-verified at
transfer):

- Indus: `indus/OUTPUT-round-o.md`, 19,959 bytes, SHA-256
  `8ba1758eff0c26afda78989a95ecd54dd83be4c16c867644deafe72ced55a4cf`.
  Disposition stated by the session: non-null.
- Eteocypriot: `eteocypriot/OUTPUT-round-o.md`, 21,309 bytes,
  SHA-256
  `e1bfaff021a584cc07347e167ecbfbfc428abb83514ae98c2540c499ecd8f30c`.
  Non-null: two conformance findings; the numerical outcome and
  the reclassification both check out.
- Meroitic: `meroitic/OUTPUT-round-o.md`, 14,295 bytes, SHA-256
  `084cf3fb85a57b38050123b7fda5d3a8aff31c121855dd449e3a3f2d1610817a`.
  Non-null: two record-only units; M-1's POSITIVE survives the
  session's fresh aggregate checks.

No session returned a null this round. (For the run record:
Indus brief-level nulls ran D–K, eight consecutive, broken by
Round N; Meroitic's Round N was an explicit null.)

Every load-bearing figure below was independently recomputed or
read at the pin by the coordinator before adjudication; the
checks are named in each unit. Nothing in this round moves a
standing, verdict, or tally. Two criterion-5 questions are
referred to the owner (§5) and are recorded, not decided, here.

## 1. Indus

### O-I-1 — APPLY WITH MODIFICATION (record act applied; integrity consequence referred to the owner as OD-O-1)

The session's finding, sustained in full on the coordinator's
own recomputation: the cycle-1 registration (§2) requires the
generator's achieved duplication rate to match target
d = 20/1670 = 0.011976048 within ±0.01. From the filed
`i1-raw-output.json` rows, achieved d = (A′ − U)/A′ is, at 1×,
median 0.393713 for Meroitic (U range 970–1,057) and 0.232934
for Latin (U range 1,258–1,310), against an allowed distinct
count interval of 1,634–1,666; the session's all-scales
computation finds 120 of 120 replications outside the
tolerance. The coordinator recomputed the 1× cells exactly
(both medians and ranges agree to the filed digit) and read the
registration's tolerance text directly. The generator injects
copies into naturally duplicated donor samples; scorer agreement
cannot test the requirement because both scorers see the same
sample. The modification to the session's candidacy: the record
act (conformance annotation, license qualification, trace
qualification) is applied in this landing; the criterion-5
consequence is not the coordinator's to rule and is referred
(§5). Discharged by
`specs/107-active-decipherment-loop/records/round-o-conformance-annotations-2026-11-27.md`
§§1 and 4. I-1's INDETERMINATE stands as the mechanical
consequence of the filed figures; IND-1 is not rescored and its
Round N qualification is untouched.

### O-I-2 — APPLY WITH MODIFICATION

Sustained: the registration (§1, read directly) describes I-1's
outcomes as discriminating among all five Indus hypotheses at
once, while the registered computation (§2) takes shape
parameters only and its statistic is identical in every
target-language world. I-1 is indirect method calibration, not
five-hypothesis discrimination, and supplies no target-family or
linguistic/non-linguistic update by itself. Discharged by the
same annotations record, §2: the ranking language is qualified
going forward, the registration bytes preserved, the
donor-control measurements retained at the narrower license.

### O-I-3 — APPLY (joint with O-M-1; single landing)

The M-1 outcome's pooling-flag explanation ("absent as a class
in funerary, where every digit has a successor somewhere") is
false as stated: the five marks never occur in funerary. Raised
independently by the Indus and Meroitic sessions; adjudicated
once, under the Meroitic unit (§3), and discharged by the same
correction record. This row records the Indus session's raising
of it.

### O-I-4 — DO NOT APPLY (concurred; no row)

The session's own disposition against substituting
POSITIVE/NEGATIVE or moving any Indus standing from this audit
is concurred in and recorded here, carrying no ledger row (the
Round N N-I-4 precedent). The registered R2-unmeasurable branch
gives INDETERMINATE on the filed statistics; a sample-generation
nonconformance is not a registered NEGATIVE; the canonical
anchor and inference files are unchanged.

The session's confirmations are recorded without act: the filed
medians mechanically give INDETERMINATE; the null-yield minimum
is an advance disjunction met by the two decided verdicts alone;
the R-IP-04 arithmetic reconciles (2,244 − 1,051 − 1,091 = 102;
residual C6 ×40, C2 ×31, C4 ×31 as entry/check pairs, not 102
distinct entries); the ledger at the pin is 1,098 lines =
1,066 claims + 31 annotations + 1 reclassification, canonical
SHA-256 `fd4d12e7…` as filed. Its single highest-value next
step — a conformance-and-ground-truth preflight for the freshly
registered I-2, before any further simulation grid — is recorded
as a priority judgment and is carried into OD-O-1's context; it
commissions nothing here.

## 2. Eteocypriot

### O-E-1 — APPLY

Sustained on direct inspection at the pin: the Spec 101 records
contain no `outcome-record-2026-11-27.md`, while the Spec 101
history ledger names it as the outcome record and the cycle-1
trace cites it as E-1's license; T401 stands checked complete;
the scoring commit `be6c5f41` carried the scorer and
`scoring-outcome.json` only; and `scoring-outcome.json` (SHA-256
`6e22675e…`, recomputed by the coordinator) contains counts,
floors, Q, the verdict, and the enrichment qualification but no
C101-2 exposure statement, which TC-101-04 requires verbatim in
the outcome record. The cycle registration's §1/§4 "unseen
Eteocypriot text" phrasing (read directly, lines 34 and 445)
conflicts with the study's postdictive license under Spec 101
§3.3. Discharged by: the late, explicitly dated narrative outcome
record now filed at
`specs/101-eteocypriot-next-claim/records/outcome-record-2026-11-27.md`
(carrying the canonical exposure statement verbatim, the counts
against floors, the enrichment-only interpretation, and the
TC-101-01..06 crosswalk, and naming `scoring-outcome.json` as
the preserved numerical artifact); the Spec 101 history-ledger
entry appended in this landing, which corrects the dangling
citation on the record; and the scope clarification carried in
the Round O annotations (§4 of the Spec 107 annotations record
covers the trace; the registration's bytes are preserved). No
backdating; no figure changes; the adjudication arithmetic basis
was independently reproduced by the session (floors 33/25/25/25
at the strict threshold; Q = 0.031153) and is not disturbed.

### O-E-2 — APPLY WITH MODIFICATION

Sustained on direct reading: TC-101-06 (binding amendment)
requires the TOO THIN closure path to be exercised, with the
closure, the scoring suppression, and C101-1 standing NOT TESTED
as its pass conditions; the filed probe in
`freeze-computation.py` (lines 79–86, read directly) is a
constructed dictionary asserting `"instantiable": False` and a
literal `"checker_result"` string; no closure routine is invoked
and no registered effect is observed; the freeze addendum's
"exercised, not merely read" therefore overstates the filed
evidence. The modification: the qualification is recorded and
the behavioral coverage gap stands explicitly, per
`specs/101-eteocypriot-next-claim/records/tc101-06-qualification-2026-11-27.md`;
the isolated fixture that would close the gap is named there as
a later verification, not fabricated in this landing and not
back-credited to the historical run. The study itself is
untouched: its four candidates instantiated, and no rescore or
re-closure is made or implied.

The session's §3/§4 confirmations (filing order, intake census
331 signs / 84 segments, floors, double-scoring reproduction,
the reclassification mechanics and cascade, the adequacy of the
two disclosures) are recorded as confirmations, not rows, per
the session's own statement. Its highest-value next step —
finish the already accepted C-E-15 feasibility decision to an
explicit proceed/stop — is a priority judgment about existing
accepted work, not a new unit.

## 3. Meroitic

### O-M-1 — APPLY WITH MODIFICATION (joint with O-I-3)

Sustained on the coordinator's read of the filed raw tables:
in population S, the five pooled never-successor digits occur
only in the document stratum (0: 7, 5: 12, 6: 10, 8: 5, 9: 7;
41 occurrences, none with a successor) and are absent from
funerary and every other stratum; the only funerary digit is 4,
once, group-initial. The outcome record's explanation is
corrected of record to a document-supported positional
observation (untestable elsewhere by absence), not a funerary
counterexample and not a pooling artifact. Discharged by
`specs/107-active-decipherment-loop/records/round-o-conformance-annotations-2026-11-27.md`
§3. Counts, conformance figures, and the M-1 POSITIVE verdict
are untouched; the session's fresh aggregate checks of M-1
(376 artifacts, 5,195 groups, 29,843 tokens; a 725/737;
i 2,857/2,880; document i-conformance exactly 0.95, passing the
inclusive threshold) are recorded as confirmations.

### O-M-2 — APPLY

Sustained: Spec 107 `spec.md` §6 (lines 318–319) and C107-5 in
`claims.md` (line 125) and `aee-claims.json` name
`cycle-1-outcome-2026-11-26.md` and `cycle-1-trace-2026-11-26.md`;
neither file exists; the completed records are dated 2026-11-27.
Discharged by the completion crosswalk at §5 of the same
annotations record; the registration-era texts and the AEE
assessment snapshot are preserved unedited.

The session's Spec 102 check found no current-state conflict
(acquisition §11 and the latest history entry agree: book 2
Appendix in custody, book 1 in transit, test uncommissioned at
the pin) and is recorded as a confirmation. (The owner's blanket
approval of 2026-11-27 04:05 ET, after the briefs were filed,
commissioned the Spec 102 test; that act is recorded in its own
program records, not here.) Its highest-value next step — a
feasibility-first M-2 registration — is a priority judgment for
the cycle-2 registration already in flight, not a unit.

## 4. What this round does not do

No standing, verdict, or tally moves. No paper is edited. The
historical records named above are preserved unedited; every
correction lands as a dated record or annotation. The trace's
kill-criteria items 1–4 stand as evaluated.

## 5. Owner decisions recorded (not decided here)

- **OD-O-1 (Indus, from O-I-1).** Spec 107 §4 criterion 5
  reserves registration breaches for recording and owner ruling.
  The I-1 duplication nonconformance is recorded (§1 of the
  Spec 107 annotations record). The owner is asked to rule on
  its treatment: whether cycle 2 — commissioned by his blanket
  approval of 2026-11-27 04:05 ET and in registration — proceeds
  with the conformance-and-ground-truth preflight the Indus
  session recommends built into I-2's registration, or halts
  pending a corrected I-1 simulation registered prospectively.
- **OD-O-2 (Eteocypriot, from O-E-1 and O-E-2).** The same
  criterion-5 question for the E-1 conformance gaps: the missing
  outcome record (now filed late) and the unexercised closure
  path (gap standing on the record). The owner is asked to rule
  on their treatment before "all checks passed" is used to
  license continuation on the Eteocypriot side.

## 6. Tallies

Units raised: 8 (Indus 4, Eteocypriot 2, Meroitic 2; O-I-3 and
O-M-1 are one correction raised by two sessions). Dispositions:
APPLY 2 (O-E-1, O-M-2), APPLY WITH MODIFICATION 4 (O-I-1, O-I-2,
O-E-2, O-M-1/O-I-3 counted once per raising program's row),
DO NOT APPLY 1 (O-I-4, concurred, no row), OWNER DECISION 2
(OD-O-1, OD-O-2, recorded inside the O-I-1 and O-E-1/O-E-2
rows). Seven rows are added to the recommendations ledger, all
done at landing: totals **146 rows — 94 done, 31 accepted,
0 open, 21 rejected (Indus 45, Eteocypriot 43, Meroitic 58)**.
Nothing was published in Round O, so no post-publication wait
runs.

Landing: PR #784.

## 7. Owner ruling on OD-O-1 (2026-11-27)

Ruled by the owner in the Glossa-Lab chat on
2026-11-27 (08:27 ET): cycle 2 proceeds, with the
conformance-and-ground-truth preflight built into
I-2's registration. The ruling is given effect in the
cycle-2 registration landing (Spec 107,
`records/cycle-2-registration-2026-11-27.md` §3): the
preflight is a registered gate executed and filed
before any I-2 scoring, and a preflight failure is
I-2's filed outcome, returning no verdict. The
alternative — halting cycle 2 pending a prospectively
registered corrected I-1 simulation — is not taken.
OD-O-2 (§5) remains unruled at this entry; the E-1
conformance qualifications stand as filed. This entry
records the ruling; it decides nothing else, and no
standing, verdict, or tally moves under it.
