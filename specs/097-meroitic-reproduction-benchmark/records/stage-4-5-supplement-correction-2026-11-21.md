# Stage 4.5 supplement — correction record (Red Team Round 2)

Filed 2026-11-21. This record corrects
`records/stage-4-5-supplement-2026-11-21.md` (the supplement),
which Red Team Round 2 found defective in its statement of the
stages' computation bases (RT2-01, CRITICAL), its tranche gate
(RT2-05 / RT1-12), and its filing of the anchor tranche's reply
(RT2-06 / RT1-11). The supplement is not edited; this record
governs where the two differ. Adjudication:
`RED-TEAM-ROUND-2-ADJUDICATION.md` (goal record), Part A
(RT2-01, RT2-05, RT2-06) and Part C (RT1-11, RT1-12, RT1-32).

## 1. What Stages 4.2, 4.3 and 4.4 computed on (RT2-01)

The supplement §4 states that Stage 4.2 ran on "not the
acquired corpus", that Stage 4.3 used "the repository-fixture
corpus (551 tokens)", and that "the acquired corpus entered at
Stage 4.4". Each statement is false on the stages' own outcome
records, and the sentence "Stage 4.2 is therefore unaffected by
the corpus-license question" is **withdrawn**.

The bases as executed, per the outcome records and freeze v2
§1:

- **Stage 4.2** computed on the freeze v2 development partition
  — 335 distinct texts of the acquired corpus (the Kovetsky
  build; code MIT, data CC BY 4.0) — and the 932 distinct
  example phrases, which are the per-scholar files' example
  material, including the Otten step-0 material.
- **Stage 4.3** computed on the development partition only (335
  distinct inscription texts of the acquired corpus).
- **Stage 4.4** computed on the acquired corpus's held-out
  partition (33 distinct texts).

The custody position follows from the bases as they are: the
acquired corpus is openly licensed, so Stages 4.2–4.4 carry no
license exposure from it; the Otten-derived material inside the
932 example phrases is governed by the custody record
(`records/custody-record-2026-11-20.md`) and the custody
supplement as corrected by the custody erratum of this date.

**Per-stage assessment against de Voogt's non-confirmation
(RT1-32).** De Voogt's reply (filed in the supplement §1)
declines to confirm the benchmark's Meroitic translations and
redirects to Rilly. Against each stage: Stage 4.2's outcome is
an internal-consistency result (registered affiliation R3 not
displaced) computed on the acquired corpus; Stage 4.3's outcome
is a candidate ranking on the same basis; Stage 4.4's outcome
is a blind test on the held-out partition, capped by the seal
rule. None of the three stages' records claims external
confirmation, and none of their standings depends on the anchor
tranche's answer. The non-confirmation therefore changes no
stage outcome; it closes the external-confirmation route the
tranche was sent to open, and the tranche's standing is
ANSWERED-BY-REDIRECT / NOT CONFIRMED.

## 2. The tranche gate (RT2-05 / RT1-12)

The supplement §3 quotes a custody condition — "Candidate-
tranche work derived from this corpus may not be prepared
until that permission question is closed or the owner accepts
the risk in writing" — that occurs nowhere in the custody
record or anywhere else in this spec, and attributes a repo
gate to "freeze v2 §6 and design §6", neither of which states
one. Both are **withdrawn**. The supplement §2's "design's
registered trigger" is likewise withdrawn: no such trigger is
registered in the design, the send record, or any other record
of this spec.

The governing position is the Round 1 adjudication's statement,
restated exactly: **the repo gate governs and was satisfied
when Stage 4.4 landed (PR #621); the anchor tranche is
separately adjudicated ANSWERED-BY-REDIRECT, so the tranche is
not dead-locked under either reading; the candidate tranche MAY
be prepared, as a separate commission, on anchors recorded NOT
CONFIRMED.** The repo gate's actual sources are the send
record's Held section ("Candidate tranche … will not be
prepared until the Stage 4.4 blind [test]") and the Stage 4.4
outcome record ("The candidate tranche may now be prepared for
the owner's approval"). The custody record's §2 terms are
custody, non-redistribution, and the same-sentence caveat; they
contain no candidate-tranche condition, and nothing in this
record re-locks tranche work behind the Otten permission. No
tranche is prepared by this record.

**Waiting-period rule (RT1-32).** Registered here, superseding
the supplement §3's weaker wait-or-disclose alternative: *any
later candidate tranche is adjudicated on its own anchors; no
later tranche is held dead behind an unanswered earlier one.*

## 3. The tranche filing (RT2-06 / RT1-11)

The supplement §1's "Claude Rilly has never replied" and §2's
"not confirmed by either named author" are corrected: **Rilly
was not sent a letter** — the send record records Rilly and
Rowan as "Named targets not sent — no verified address". The
tranche is one letter sent (de Voogt, 2026-11-20) and one reply
received (2026-11-20 23:39 ET, declining to confirm and
redirecting to Rilly). Rilly is named-not-sent, not a
non-respondent, and no record of this program may file him as
one.

## 4. Governed-file references (RT2-06)

The supplement's header cites two files that do not exist:
`records/stage-4-5-anchor-tranche-design-2026-11-20.md` and
`records/corpus-custody-and-license-2026-11-20.md`. The records
that govern are: the campaign design
(`records/decipherment-campaign-design-2026-11-20.md`, §6) and
the send record for the tranche; and
`records/custody-record-2026-11-20.md` for custody. The custody
supplement's header carries the same wrong custody filename;
it is corrected by the same erratum (see the custody erratum
record of this date).

## 5. Round 3 note: the Stage 4.2 gloss in §1 (RT3-21)

Section 1's per-stage assessment calls Stage 4.2's outcome
"an internal-consistency result (registered affiliation R3
not displaced)". That gloss is softer than its source and is
not to be quoted without the outcome record's verdict head.
The Stage 4.2 outcome record's verdict reads, verbatim:
**"UNDECIDABLE AT THIS POWER. R3 (isolate / null) is
recorded as not displaced, and as nothing more"** — with
freeze v2's power statement forbidding any reading of the
double failure as a positive classification. Citations of
Stage 4.2 follow the outcome record's wording. The §1
characterizations of Stages 4.3 and 4.4 stand as filed; they
match their records.
