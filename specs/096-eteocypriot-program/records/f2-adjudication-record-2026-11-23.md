# Eteocypriot Program — Adjudication of Finding F-2: C096-4's Scope Sentence Amended (OD-C-2)

**Date:** 2026-11-23. **Program:** Spec 096 — Eteocypriot
Program. **Question:** finding F-2 of the OD-8 audit record
(`records/a2-audit-rerun-record-2026-11-22.md` §5), flagged
there for adjudication and presented to the owner as OD-C-2
in the Round C assessment adjudication
(`specs/091-anchor-comparison-integrity/records/coscientist-release-round-c-assessment-adjudication-2026-11-23.md`,
unit C-E-17): whether C096-4's narrowed scope sentence
should be amended to state the executed-bytes condition on
the pilot's reproducibility. The paper itself reserves the
question to the approver (v2 §5.4: "whether the narrowed
scope sentence of the process verdict should be amended to
state the executed-bytes condition is the approver's
question").

**Decision:** the owner's act of 2026-11-23 in the
Glossa-Lab chat ("Amend the C096-4 scope sentence").
**F-2 is ADJUDICATED: the scope sentence IS amended.**
F-2 stands closed as of this record. No verdict and no
standing changes: C096-4 remains SUPPORTED in its narrowed
scope, and the amendment states the condition that scope
already rested on.

## 1. The original sentence (superseded)

The narrowed scope sentence of record is amendment 2 §3
(`records/outcome-record-amendment-2-2026-11-21.md`):

> C096-4's SUPPORTED is narrowed on the record to what it
> can honestly cover: **the pilot's reporting of its
> administrable leg (the ICS 196 leg: records filed, floors
> stated, run byte-identically reproducible) and of its
> closures.**

That sentence is preserved here verbatim and is marked
**superseded as a citation form** by §2 of this record,
in the same manner as amendment 2 superseded the outcome
record §4's bare "SUPPORTED" as a citation form. The filed
records themselves are not edited.

## 2. The amended sentence (of record from 2026-11-23)

> C096-4's SUPPORTED is narrowed on the record to what it
> can honestly cover: **the pilot's reporting of its
> administrable leg (the ICS 196 leg: records filed, floors
> stated, run byte-identically reproducible on the executed
> bytes recovered from the freeze commit — a
> historical-input reproduction, not a reproduction from a
> fresh checkout, against whose corpus file as it stands
> the frozen driver refuses to run) and of its closures.**

Wherever C096-4's narrowed scope is stated from this
record onward, it is stated in the amended form. The
amendment changes no number and no verdict: the audit
record establishes that the reproduction holds byte for
byte on the executed bytes (§1.3 of that record), that the
post-run corpus corrections touch no analysis-bearing
field (§1.2), and that every verdict-bearing quantity also
reproduces by independent recomputation (§2). What the
amendment removes is the unqualified reading of
"reproducible": a fresh checkout cannot rerun E1 as filed,
because the executed bytes survive only in git history
(freeze commit `173882a2`) and the frozen driver refuses
to run against the corrected corpus file at origin/main.

## 3. Effect on the papers

The v2 paper (DOI 10.5281/zenodo.24449913) stands as
deposited; this record governs citation of the scope
sentence, not the deposited text. The v3 candidate's
consistency with this amendment is checked and reported
in the landing record for this adjudication; any v3 text
change that follows from it is a separate, owner-approved
act.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
