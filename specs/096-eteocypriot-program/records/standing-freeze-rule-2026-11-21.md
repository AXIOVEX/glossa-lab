# Eteocypriot Program — Standing Freeze Rule: Decomposition and Severability

**Date: 2026-11-21. Filed under Red Team Round 1 (findings
RT1-06, RT1-23), adjudicated APPLY on 2026-11-21. This rule
binds every future freeze in Spec 096, and is recommended to
the program's other specs by the same adjudication.**

## The rule

1. **Decompose at freeze, or do not run.** A conjunctive
   claim with a conjunct that is TOO THIN at freeze must be
   decomposed, or re-registered without that conjunct, in the
   freeze record itself, before any run. A decomposition
   produced after a verdict — however correct on the record's
   own terms — is post-hoc repair and is labelled as such
   wherever the verdict is cited.

2. **Severability.** A floor closes the smallest unit the
   claim's own registered structure assigns it to. Where a
   claim is a conjunction over legs, a leg's floor failure
   closes the claim's pass and is decomposed at freeze under
   rule 1. Where a claim is single-leg, its floor closes its
   experiment. The two treatments are not interchangeable
   within one study: Spec 096's own E1/E2 asymmetry (E2's
   floor closed its experiment; E1's leg floor closed only
   the leg while the parent claim was scored on the full
   conjunction) is the instance this rule exists to forbid.

3. **The freeze contains the whole procedure.** Every table,
   default, and threshold the executing code implements is
   registered in the freeze or its amendments before the run.
   A rule discovered in the driver after the run is a
   deviation, recorded as one — never absorbed silently into
   "the frozen procedure."

## The instance

C096-1 (Spec 096): the Androkles conjunct was TOO THIN at
freeze; freeze §6 itself stated "P1 cannot pass as
registered, whatever the ICS 196 leg scores"; the claim was
nevertheless run and scored on the full conjunction, and its
decomposition arrived after the verdict, on red-team
prompting. Recorded in full in
`records/outcome-record-amendment-2-2026-11-21.md` §§2, 5.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
