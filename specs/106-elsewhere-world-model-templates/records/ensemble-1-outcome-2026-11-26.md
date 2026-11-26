# Ensemble 1 Outcome — Spec 106 Stage 1

## ETE-ENS-1: claim ETE-Q-1, "The long Amathus text is a royal dedication"

**Seed:** `records/ensemble-1-seed-2026-11-26.md`, committed
before any derivation ran (the seed commit precedes this
outcome in the landing's history). **Date of the pass:**
2026-11-26. **Authorizing act:** the owner's order of
2026-11-26 ~01:54 ET, recorded at §9 of the seed. **Reading
rule:** framework §8.1 as clarified by §8.2; status labels
exactly as framework §8.

---

## 1. The pass as run

Four instances, declared in full at §7 of the seed, each
carrying the Eteocypriot baseline template version 1 entire
(71 axioms, pin `fca1cc8a…`, recomputed at the seeding)
with its declared difference: ETE1-A + ETE-POL-H1 (royal
commissioning norm, added (H)); ETE1-B + ETE-POL-H2 (civic
commissioning norm, added (H)); ETE1-C the baseline control;
ETE1-D + ETE-POL-H1 with the named (K) axiom ETE-POL-11
dropped (declared sensitivity run). In each instance the
claim's derivation was attempted under the seed's fixed
test, then the negation's, then both were scored at the
exercised contact point. The derivations are logged below
with their inputs; the core chain is common to all four
instances and is written once, with each instance's own
steps and verdicts recorded separately.

## 2. The derivation core (all four instances)

**Step 0 — translation (seed §5).** The claim under test is
the translated claim: "ICS 196's dedicator is the king (or
royal house) of Amathus, and its act is a dedication."

**Step 1 — the text's filed content (ETE-CON-03).** ICS
196's Greek text reads: "The city of the Amathusians
[honoured] Ariston, son of Aristonax, of noble birth." The
Eteocypriot text gives the same names with non-Greek
endings and is roughly twice as long; the two are broadly
corresponding versions, not an exact translation. Hence,
inside every instance: the act ICS 196 performs is the
city of the Amathusians' honouring of Ariston; the agent
of the act is the city; the person honoured is Ariston,
identified by patronymic (son of Aristonax) and by noble
birth, and by no royal title.

**Step 2 — the record's own contrast class (ETE-CON-04).**
Where the Amathus record presents royal dedications, it
names the king: a statue dedication for the son of King
Androkles, a dedication to Cypriot Aphrodite naming the
same king, and Androkles's own dedications. The complete
census of axioms speaking to ICS 196 itself is ETE-ENV-03
(the object: black marble slab, Amathus acropolis, late
fourth century BCE), ETE-CON-03 (its content, Step 1), and
ETE-ENV-04 (the program's frozen census of it: 11
segments, 54 signs). No axiom names any king in connection
with ICS 196.

**Step 3 — the claim attempt stops (all four instances).**
Deriving the translated claim requires a premise of the
form "ICS 196's dedicator is the king (or royal house)".
By Step 2's census, no axiom in any instance's set
supplies it, and Step 1 supplies the contrary assignment.
The derivation stops here. **The gap, named: no axiom
connects ICS 196 to a royal dedicator.** Verdict on the
claim, every instance: **DOES-NOT-DERIVE**, with this gap.

**Step 4 — the negation derives (all four instances).**
From Step 1 and the translation: ICS 196's dedicator is
the city, and a royal dedication requires a royal
dedicator; therefore ICS 196 is not a royal dedication.
In the record's own categories the inscription is a civic
honorific. The chain cites only ETE-CON-03 and the seed's
declared translation, both present in all four sets.
Verdict on the negation, every instance: **DERIVES**.

## 3. Per-instance records

### ETE1-A — baseline + ETE-POL-H1 (royal commissioning norm)

The one step A adds to the core is the test of H1 against
Step 3. H1 states a general norm: substantial public
inscriptions at Amathus in the period were *normally*
commissioned by the king or the royal house. Moving from
H1 to "ICS 196's dedicator is the king" requires the
further premise that ICS 196 falls under the norm
notwithstanding its filed content — equivalently, that its
filed content does not name its dedicator. That premise is
not in A's set, and Step 1 contradicts it. A norm does not
distribute over a filed exception, so A's claim attempt
stops at the same gap as the core. The negation derives by
the core chain, which nowhere cites H1. **Checker:** H1
derives no contradiction with the evidence set — it is a
norm framed against the two attested practices (seed §6),
and the evidence item it is scored against, ETE-CON-03, is
one of those practices; the instance does not die.
**Verdicts: claim DOES-NOT-DERIVE (gap as Step 3);
negation DERIVES. Retired at the close of the pass, queue
exhausted.**

### ETE1-B — baseline + ETE-POL-H2 (civic commissioning norm)

H2 is consonant with Step 1 and adds no premise bearing on
a royal dedicator; B's claim attempt stops at the same
gap. The negation derives by the core chain. **Checker:**
no contradiction with the evidence set is derived; the
instance does not die. **Verdicts: claim DOES-NOT-DERIVE
(gap as Step 3); negation DERIVES. Retired at the close
of the pass, queue exhausted.**

### ETE1-C — baseline control

The core chain is the whole of C's record: the claim
attempt stops at Step 3's gap; the negation derives at
Step 4. **Checker:** no contradiction with the evidence
set is derived; the instance does not die. **Verdicts:
claim DOES-NOT-DERIVE (gap as Step 3); negation DERIVES.
Retired at the close of the pass, queue exhausted.**

### ETE1-D — baseline + ETE-POL-H1, ETE-POL-11 dropped (sensitivity)

Dropping ETE-POL-11 removes the end-of-kingdom chronology:
D's world leaves the Amathusian kingship's end undated and
unended, and ETE-CON-04's Androkles dedications stand in
it with no closing date. Tested against the claim: the
attempt still stops at Step 3's gap — ETE-POL-11 never
spoke to ICS 196's dedicator, so its absence creates no
premise that does, and H1's step fails in D exactly as in
A. The negation chain nowhere cites ETE-POL-11 and derives
unchanged. **Checker:** no contradiction with the evidence
set is derived; the instance does not die. **Verdicts:
claim DOES-NOT-DERIVE (gap as Step 3); negation DERIVES.
Retired at the close of the pass, queue exhausted.**

## 4. Checker summary

Contact point 2, the filed Eteocypriot record
(ETE-CON-03, ETE-CON-04, ETE-ENV-03), was exercised for
every instance: each negation derivation agrees with the
filed record it is built from; no instance derived any
statement contradicting the evidence set; **no instance
died**. Contact point 1, Spec 105's G-ETE gate, was not
exercised: the pass ran no language-internal derivation,
and no G-ETE score is claimed from this pass.

| Claim | ETE1-A | ETE1-B | ETE1-C | ETE1-D |
|---|---|---|---|---|
| ETE-Q-1 | DOES-NOT-DERIVE; negation DERIVES | DOES-NOT-DERIVE; negation DERIVES | DOES-NOT-DERIVE; negation DERIVES | DOES-NOT-DERIVE; negation DERIVES |

## 5. The ensemble reading

Tallies over the ensemble: surviving instances 4 of 4 (no
deaths; the four retirements are queue-exhausted closings
after verdicts were returned). Translatable in 4 of 4.
Claim derived in 0 of 4. Negation derived in 4 of 4.

Framework §8.1's aggregation row for exactly this tally —
*no survivor derives the claim, and at least one survivor
derives its negation* — returns:

> **ETE-Q-1 — REFUTED-IN-ENSEMBLE.**

Framework §8.2 governs §8.1's positive row only; the
positive row is not in play here, and translation coverage
was in any case complete (4 of 4), so no scoped subset
reporting arises. Framework §8's SOLUTION conditions are
not met and the word is not used: the claim is refuted in
its ensemble, not robust in it. Status change, entered in
the log's solution register: **ETE-Q-1, UNTESTED →
REFUTED-IN-ENSEMBLE** (Iteration 2, 2026-11-26).

## 6. What this does and does not establish

Inside the declared ensemble the claim is dead, and the
manner of its death is the informative part: it does not
track the politics variation. At every corner of the
declared space — royal norm, civic norm, unamended
baseline, kingship unended — the claim fails on the same
step, because the load-bearing item is not a politics
premise but the filed content of the text itself
(ETE-CON-03), which every instance carries and the checker
holds fixed. An ensemble identifies what a claim rides on;
this claim rides on nothing political, and is killed by
the evidence item itself.

It establishes nothing new about the real Amathus.
ETE-CON-03 is the scholarship's reading of the bilingual's
Greek half and was already the program's filed position;
the ensemble adds the tested status of the contrary claim
under declared variations. No anchor standing, program
verdict, or tally in any program moves (framework §8), the
Eteocypriot paper is not edited, and no decipherment claim
arises: the pass ran no language-internal derivation and
says nothing about what the Eteocypriot text means beyond
the filed correspondence of its Greek half.

The next evidence that could bear on this claim is
therefore not a politics premise but a change to the filed
content of ICS 196 itself. ETE-ENV-04 names that content's
weakest point: the program holds the text from secondary
reproductions, not from Masson's edition of record (ICS
pp. 206–209) or the Sittig 1914 photograph, and the
program's interlibrary-loan request for that portion copy
is outstanding and unanswered. If that check ever revises
ETE-CON-03's content, ETE-Q-1 can be re-run as a new
iteration on the revised record; on the record as filed,
the claim is closed.

*AI disclosure: prepared by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per standing
disclosure practice.*

---

## Conformance note (2026-11-26, Round N unit N-E-1)

Appended at the landing of the Round N adjudication
(`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-26-round-n.md`
§3.1). Nothing above is altered.

Contact point 2, as exercised in this pass, named the
baseline's own ETE-CON-03, ETE-CON-04, and ETE-ENV-03 as
its evidence items. All three are axioms in every declared
instance, and the negation derivations' load-bearing
factual premise is ETE-CON-03 itself. The framework's §2
definition states that the evidence set "is not an axiom
of any instance", and §6 states that no instance "treats
a checker item as derivable". The contact therefore
checked agreement with inherited premises: it is an
inherited-premise consistency check, not a separate
evidentiary test of those statements, and its agreement
adds no evidentiary support to the premise the answer was
derived from. This dual role does not satisfy the
framework's literal evidence/axiom separation rule without
an explicit exception or clarification, and none is
created by this note.

The verdict stands, at its corrected scope: ETE-Q-1 is
REFUTED-IN-ENSEMBLE as a conditional logical result —
under the seed's declared translation, the claim does not
derive and its negation derives in every declared
instance, identically at every corner of the declared
politics variation. What this note withdraws is any
reading of the pass as an independent evidentiary test of
ETE-CON-03's content. The next evidence that could bear
remains what §6 above names: the outstanding
edition-of-record check on ICS 196's filed content
(ETE-ENV-04). If consistency-only contacts of this kind
are to be framework-conformant, the distinction between
them and genuinely separate evidentiary contacts is a
prospective registration matter; it is not created here,
and no new ensemble is commissioned by this note.

