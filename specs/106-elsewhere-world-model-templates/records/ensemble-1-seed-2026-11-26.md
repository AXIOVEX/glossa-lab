# Ensemble 1 Seed — Spec 106 Stage 1 (First Ensemble)

## Eteocypriot baseline; one claim: "The long Amathus text is a royal dedication"

**This record is the seed of the first ELSEWHERE ensemble run
under Spec 106. It is written and committed before any
derivation runs; the landing's git history is the proof of
that order. The ensemble's outcome is filed separately
(`records/ensemble-1-outcome-2026-11-26.md`), and the pass is
entered in the study's seed-and-iteration log
(`records/elsewhere-seed-and-iteration-log.md`, Iteration 2).**

---

## 1. Study identity (framework §4 field 1)

Glossa-Lab, Spec 106 (`specs/106-elsewhere-world-model-templates/`),
Stage 1 — first ensembles (spec.md §5), ensemble **ETE-ENS-1**:
the first study seeded from the Eteocypriot baseline template.
Framework adopted: ELSEWHERE Framework Specification,
Version 1 (2026-11-25), `../framework.md`, including the
clarifications at §8.1 (Round E, 2026-11-25) and §8.2
(Round F, 2026-11-25).

## 2. Baseline template (framework §4 field 2)

`templates/eteocypriot-baseline.md`, version 1 (2026-11-25),
in this package. Axiom census as seeded: 71 axioms in
domains 2–8 (GEO 11, POL 12, MOV 9, DNA 5, ECO 10, ENV 10,
CON 14), plus Domain 1 (language-internal) carried by
reference to Spec 105, as the template declares. By kind:
(F) 3, (K) 58, (H) 10. Lines whose sourcing is the
UNSOURCED flag itself: 2 (ETE-DNA-05, ETE-CON-14); one
further (H) line (ETE-MOV-09) carries a named source with a
partial-unsourced caveat. SHA-256 over the axiom lines as
filed: `fca1cc8a238631b0c6df8b2901daa5e84dc4cb2387dcdad560285c6e95beec4f`.
The pin was recomputed at this seeding, 2026-11-26, by
`records/census-audit.py` over the template as it stands on
origin/main at `b396a50a`: 71 axioms, (F) 3, (K) 58, (H) 10,
the hash above reproduced exactly, TC-106-02..TC-106-05
PASS. The seeded set is the template as pinned, unamended:
the Eteocypriot template has never been amended (the
version-2 amendment of Iteration 1 touched the Meroitic
template only).

## 3. The full axiom set as seeded (framework §4 field 3)

The template itself, incorporated by the exact reference of
§2: the file `templates/eteocypriot-baseline.md` in this
repository, whose axiom lines hash to the pin above, together
with Domain 1 by its Spec 105 reference as the template
declares. Each instance's set is this set with the declared
differences of §7 below, written out there in full; nothing
else enters any instance (framework §3, the no-smuggling
rule).

## 4. The claim queue as opened (framework §4 field 4)

The baseline's claim queue opened empty at the template's
seeding, claims entering only by an authorizing act at the
reasoning level recorded in the log. This ensemble's queue
opens with exactly one claim, entered by the authorizing act
of §9, verbatim:

> **ETE-Q-1 — "The long Amathus text is a royal dedication."**

This is the framework's worked example: the claim the owner
was shown at the framework's presentation on 2026-11-25,
across instances varying the politics axioms. Status at
entry: **UNTESTED**. No other claim is in this ensemble's
queue, and no wider set is commissioned: one claim, fully
logged, before any wider set (the terms of the authorizing
act).

## 5. Study-level declarations: identification and translation

Two renderings are carried by every instance of this
ensemble. Under framework §3 rule 3 they are declared here
as study-level assumptions of the seed, not smuggled into
any derivation.

**Identification (study-level assumption).** "The long
Amathus text" is ICS 196, the Amathus bilingual. Basis in
the baseline: ETE-ENV-02 (the Eteocypriot corpus comprises
about 20 to 30 inscriptions, most from Amathus), ETE-ENV-03
(ICS 196: a black marble slab from the Amathus acropolis,
late fourth century BCE, the Eteocypriot text in the
syllabary above a shorter Greek text), ETE-CON-03 (ICS 196
is the sole complete Eteocypriot bilingual; its Eteocypriot
text is roughly twice as long as its Greek). No other text
in the filed corpus answers to "the long Amathus text".

**Translation.** "Royal dedication" is rendered in instance
terms as: an inscription whose dedicator is the king of
Amathus (basileus, ETE-POL-01) or the royal house acting in
its royal capacity, and whose act is a dedication. The
category is the record's own: ETE-POL-09 (the syllabary
"was used for royal inscriptions, dedications, epitaphs and
coin legends") and ETE-CON-04 (Amathus dedications naming
King Androkles). The contrasting category in the same
record is the civic honorific: the city honouring a named
citizen (ETE-CON-03). The translated claim is therefore:

> **ETE-Q-1, translated: ICS 196's dedicator is the king
> (or royal house) of Amathus, and its act is a dedication.**

The claim's terms are carried by baseline axioms present in
every instance (ETE-POL-01, ETE-POL-09, ETE-CON-03,
ETE-CON-04, ETE-ENV-03), so the claim is translatable in
every instance as declared; an instance returning
UNTRANSLATABLE would be recorded as such, and §8.2's
coverage rule would then govern the reading.

**The test, fixed in advance.** The claim DERIVES in an
instance only if a chain of steps, each citing that
instance's axioms or prior steps, reaches the translated
claim with no added premise; a derivation that needs a
premise the set does not contain stops and names the gap
(verdict DOES-NOT-DERIVE, with the gap). The claim's
negation DERIVES in an instance only if such a chain
reaches "ICS 196's dedicator is not the king or the royal
house". No other outcome is available to the pass.

## 6. The declared variation (chosen at the reasoning level, before the pass)

The baseline's POL domain carries no (H) axioms: its twelve
lines are (F) or (K). The politics variation is therefore
declared in the two forms the framework permits (framework
§5): one added POL hypothesis in two alternative forms, one
per instance, varied one at a time; and one declared
sensitivity run dropping a named (K) axiom.

**The added hypothesis.** The record attests both practices
at Amathus — royal dedications (ETE-CON-04) and a civic
honorific (ETE-CON-03) — but no opened source settles which
was the norm for substantial public inscriptions in the
text's period. That unsettled norm is the hypothesis this
ensemble varies, declared here in its two forms. Each is an
(H): the practices it generalises are attested at
ETE-CON-03 and ETE-CON-04; the general norm itself is
UNSOURCED in the opened record.

- **ETE-POL-H1 (H)** — In the period of ICS 196, substantial
  public inscriptions at Amathus were normally commissioned
  by the king or the royal house.
- **ETE-POL-H2 (H)** — In the period of ICS 196, substantial
  public inscriptions at Amathus were normally commissioned
  by the city as a civic body.

**The sensitivity run.** Named (K) axiom **ETE-POL-11**
(the kingdom system ended politically in the late fourth
century: Alexander took Cyprus in 333 BCE, Androkles was
the last king of Amathus, the Ptolemies abolished the
kingdoms between about 312 and 310/294 BCE) is dropped in
instance ETE1-D only. Dropping it leaves the Amathusian
kingship's end undated and unended inside that instance:
the maximal room the declared space gives a royal reading
of a late-fourth-century text.

**Why this shape (the study's thinking, framework §5).**
The claim turns on who commissions public stone at
Amathus. The commissioning norm is the one politics
question the record leaves open that bears directly on it,
so it is the honest hypothesis to vary; the POL-11
sensitivity tests whether the claim's fate depends on the
kingship's end-date. One hypothesis is varied at a time;
the sensitivity corner (H1 with POL-11 dropped) is the
declared extreme of the space.

## 7. The instances, declared in full (framework §5 step 1)

Each instance carries the full seeded set of §3 (baseline
version 1 entire, including Domain 1 by its Spec 105
reference) with exactly the difference named. The (F)
axioms are identical in all four (framework §3 rule 4).

- **ETE1-A ("royal norm").** Baseline entire + ETE-POL-H1.
- **ETE1-B ("civic norm").** Baseline entire + ETE-POL-H2.
- **ETE1-C ("baseline control").** Baseline entire, no
  addition and no drop.
- **ETE1-D ("royal norm, kingship unended — sensitivity").**
  Baseline entire + ETE-POL-H1, with ETE-POL-11 dropped
  (declared sensitivity run over a named (K)).

## 8. The evidence set and the checker (framework §4 field 5)

As the template's seed record declares: the Spec 096
corpus (the Eteocypriot token streams as frozen by that
study) and the fixed epigraphic record of Iron Age Cyprus.
Registered contact points:

1. **Spec 105's G-ETE validation gate** — the registered
   contact point for language-internal derivations
   (`specs/105-elsewhere-sandbox/records/stage-6-outcome-2026-11-25.md`:
   ETE-1 GOOD, ETE-2 GOOD as filed, landed PR #751, with
   the Round J qualifications on their record — J-E-1, the
   reference table's provenance UNRESOLVED with verified
   nil impact; J-E-2, the zero-opportunity certificate —
   landed PR #752). This claim requires no language-internal
   derivation: nothing in the pass derives from the Spec 105
   ladder. Contact point 1 is registered for this study but
   is **not exercised** by this pass, and no G-ETE score is
   claimed from it.
2. **The filed Eteocypriot record** — the baseline's
   epigraphic lines on the texts themselves (ETE-CON-03,
   ETE-CON-04, ETE-ENV-03), resting on the Spec 096 record.
   This is the scoring contact point this pass exercises:
   each instance's derivations are scored against it, and
   an instance whose derivations contradict it dies
   (framework §6), its death filed.

## 9. Date and authorizing order (framework §4 field 6)

Seeded 2026-11-26. Authorizing order: the owner's order in
the Glossa-Lab chat, 2026-11-26 ~01:54 ET — "For
everything else, execute now to your recommendations" —
the recommendation so approved being, in the form presented
to him: commission the first ensemble on the framework's
worked example, the claim that the long Amathus text is a
royal dedication, run across the Eteocypriot politics
variants; one claim, fully logged, before any wider set.
This order is the commission for Spec 106 Stage 1
(spec.md §5: "Instance spawning is a later stage and needs
its own commission"). The claim's entry into the queue (§4)
is recorded under this act in the study's log, Iteration 2.

## 10. Protocol of the pass and rails

Per instance, in order: the claim's derivation is attempted
under §5's fixed test; the negation's derivation is
attempted likewise; both are scored at contact point 2;
deaths, if any, are filed with the contradicting derivation
and the evidence item struck. Surviving instances retire at
the close of the pass with the queue exhausted, their
records kept. The ensemble is read under framework §8.1 as
clarified by §8.2, in the exact status labels of §8, and
the per-claim verdict table and the status change are
entered in the log's Iteration 2 entry and its solution
register.

Rails: no decipherment claim arises from any outcome of
this ensemble; no anchor standing, program verdict, or
tally in any program moves; the Eteocypriot paper is not
edited by this work; a derivation inside an instance is
valid relative to its axioms and is never reported as a
fact about the real world (framework §8).

*AI disclosure: prepared by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per standing
disclosure practice.*
