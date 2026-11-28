# Spec 110 — Revision execution (verdicts under the revised battery)

Filed 2026-11-27, after the revision gate
(`records/revision-control-validation-2026-11-27.md`). Only the
families and patterns the gate licensed at each profile render
verdicts; gate-failed families file no verdict, and the unscored
figures are shown for transparency, labelled as unscored. Raw
output in custody: `glossa-custody/spec110-rev/raw-output-rev2.json`,
SHA-256 `64e21aa9fee930d4b9fd351a5e1c997d8033d5e859afbfab37e7fb6da46a3e79`.
Independent recomputation: **TC-110-08 PASS** (same verification run
as TC-110-07; every filed verdict and every filed absence of a
verdict reproduces).

**The two PRESENTs below are candidate findings for adjudication.
They proclaim nothing about intent.** The survey's cautions stand on
this record: a cipher device can exist without a secrecy function,
and a secrecy regime can exist with no textual signature — so no
ABSENT here disproves a secrecy regime, and no PRESENT proves one.
A whole corpus under one fixed substitution remains invisible to
this battery by construction.

## Indus (1,336 sequences, 5,611 tokens, 372 types)

Statistics against the Indus-profile band: A1 0.7337 (band
[0.8837, 0.9002], below), A2 0.0841 ([0.0250, 0.0542], above),
A3 0.5971 ([0.4295, 0.4541], **above**), A4 2.5245 ([4.0246, 4.2679],
**below**), V 372 ([316, 325], above), fixed-rank tail 0.0570
([0.0738, 0.0838], below).

- **Family A — SIGNATURE PRESENT (structure pattern).** A3 above
  the band maximum and A4 below the band minimum: the corpus's
  sequential constraint is far weaker than the registered natural
  model produces at this profile. The flattening pattern was not
  scoreable (gate), and in any case points the other way (A2 sits
  above the band; the corpus's distribution is *more* concentrated
  than the model's, not flatter). Registered alternative
  explanations, in the order the registration files them: the
  corpus's sign sequences are not fixed-word-like in the
  generator's stem sense (a deciphered fixed-word corpus, Latin,
  sits at the top of its own band; the Indus sequences do not
  repeat sign tuples the way words repeat); genre and text-length
  effects (the corpus is short inscribed texts, mean length 4.2);
  editorial sequence construction in the derivation build. A
  deliberate structure-destroying practice (a T-SHUF-like regime)
  is the reading the pattern is named for, and it is one candidate
  among these, not the conclusion.
- **Family B — SIGNATURE ABSENT.** Observed omnibus JSD 0.1214
  against null p99 0.1373 (B = 999, seed 11999) and the genre
  baseline maximum 0.1494: below both. The site strata (Mohenjo-daro,
  Harappa, Dholavira, Kalibangan, Lothal) are as homogeneous as the
  natural model's own site splits. No per-stratum signature.
- **Family C — SIGNATURE PRESENT (C1).** C1's clause (A3 above band
  OR A4 below band) fires on both disjuncts. This is the same
  measurement as family A's structure pattern under a more
  sensitive, less specific rule — it is filed as C1's verdict
  because the registration keeps the families separate, but it is
  **not an independent second finding**, and it inherits the
  structure pattern's alternative explanations in full. It is also
  filed with C1's gate history on the record: C1 false-fired on
  2 of 12 in the first battery, and its re-registration here was
  met exactly at the at-most-1 rule (1 of 12, Latin q2).
- **Family D — NO VERDICT (gate failure, G-D 3/5).** For
  transparency, the unscored figures: D1 would fire (V 372 above
  the band maximum 325) and D2 would not (fixed-rank tail 0.0570,
  below the band minimum 0.0738 — the corpus's top 186 types carry
  94.3% of its tokens; its rare tail is numerous but light). The
  joint rule would therefore have filed ABSENT had it been
  scoreable. No verdict is filed.

## Meroitic (376 sequences, 28,734 tokens, 31 types)

- **Families A, C, D — NO VERDICT (gate failure at this profile:
  G-INV 3/5; see the gate record for the measured band-coverage
  mechanism).** Unscored transparency figures against the
  Meroitic-profile band (A1 [0.7025, 0.7377], A2 [0.1206, 0.1729],
  A3 [0.8549, 0.9023], A4 [0.3463, 0.5238], V [28, 31], tail
  [0.0064, 0.0154]): the corpus reads A1 0.8190 (above band), A2
  0.1561 (in band), A3 0.7581 (below band), A4 0.9817 (above band),
  V 31 (at the band maximum, not above), tail 0.1050 (above band).
  Applied informally, no family's rule fires: flattening needs A2
  below the band; structure and C1 need A3 above or A4 below; D
  needs V above the band maximum, which 31 does not reach. These
  are not verdicts and are not filed as ABSENT; the gate did not
  license verdicts at this profile.
- **Family B — NOT TESTABLE AT THIS POWER** (the corpus build
  carries no stratum metadata).

## Eteocypriot (11 sequences, 54 tokens, 32 types)

- **All families — NOT TESTABLE AT THIS POWER.** Every registered
  floor fails (families A, C, D require N ≥ 1,000 tokens against
  54; family B requires two qualifying strata against a single
  stratum), as both registrations anticipated.

## Standing

No standing, verdict, or tally in any program moves. The Indus
structure-pattern and C1 candidates go forward as candidates for
adjudication through the program's existing gates, with their
alternative explanations attached; nothing in this record is a
decipherment claim or evidence for one.
