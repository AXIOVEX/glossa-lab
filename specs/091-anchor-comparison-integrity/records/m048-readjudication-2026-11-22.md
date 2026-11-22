# M048 (mu/muṉ) — class re-adjudication under RT2-08

**Date: 2026-11-22. Filed under Red Team Round 2,
finding RT2-08. Authority: the owner's commission, in
the Glossa-Lab chat on 2026-11-22, of the
re-adjudication RT2-08 attached to M048's corrected
battery result. This record states the question, the
governing rule, the examination of the filed basis, and
the decision, and is the owner-facing summary of the
act.**

## The question

M048 stands in class U. RT2-08's adjudication stated
the consequence in advance: if M048's corrected battery
result were produced and scored at the corrected
battery's promotion threshold, its class would have to
be re-adjudicated. The result has been produced (the
F-4 study package, commissioned by the owner on
2026-11-22) and it scores at the threshold. The
question is what class M048 takes on that result and
its filed basis, under the register's landed rules.

## The governing rule

Two landed statements govern, and together they decide
the act:

1. **The battery's own scoring rule** (the T301 design,
   executed by T302 over the `requires_revalidation`
   Phase-48 promotions): three tri-state checks; a
   `not_run` never counts; the score is the number of
   passes; promotion at score ≥ 2.
2. **RT2-08's adjudication** (Red Team Round 2
   execution, carried in the standings supplement's
   Round 2 amendment,
   `records/standings-supplement-2026-11-21.md`): M048
   and M089 "were judged by the corrected battery's
   2-point promotion threshold". M089 (class I) holds a
   filed corrected-battery result at that threshold
   (score 2: positional pass, DEDR not run, bigram
   pass), and "its class rests on that result, not on
   the collocation counts in its falsifier row". M048
   (class U) held "no corrected battery result at all;
   its class rests on the absence of a qualifying filed
   result". Producing the result was referred to the
   study-scale commission family, with the
   re-adjudication attached to a threshold score.

Neither the addendum rule nor the itemization test is
engaged. This is not a strike: no external-support
claim is contradicted, and none is filed for M048. It
is not an itemization case: no external support is at
issue. It is a threshold re-adjudication under a rule
stated in advance, executed when its named trigger
occurred.

## The trigger: the corrected battery result

`records/m048-corrected-battery-result-2026-11-22.md`
(run `study-20261122T075700Z-f40448`), produced by
battery v2's own code on inputs validated in that
record (the roles file agreeing with the WP5 support
audit's reconstruction on 30 of 30 promoted signs; the
DEDR dataset the restored tree, byte-identical to the
restore record's verification):

| check | outcome | detail |
|---|---|---|
| positional | **PASS** | role CASE_MARKER_SUFFIX; avg_position 0.627 ≥ 0.5, is_ending True, is_starter False |
| DEDR | **PASS** | `exact_match_3` — the battery's normalized reading ("mumu") has exactly 3 exact matches in the restored DEDR |
| bigram | **NOT_RUN** | the pinned Holdat corpus is not held on the execution venue; not executed, no substitute used |

**Score: 2. Promotion under the battery's rule: TRUE —
the threshold is met.**

The configuration point, stated because the
adjudication turns on it: under T302's input
configuration (the DEDR dataset not then held), the
DEDR leg would be `not_run` and the executed legs would
score 1. The filed result is the current-holdings one:
the dataset's restoration on 2026-11-19 is a fact of
the program's holdings, and T302's record named a
future run under a new commission, with the dataset
restored, as this leg's route. This is that run, and
this act adjudicates on its result as filed.

## Examination of the filed basis, item by item

M048's inference-log entry
(`specs/099-inference-log/records/inference-log.json`)
holds seven items over its basis as filed ("Positional
analysis; UPGRADED: high frequency (157); consistent
TERMINAL position (n=157); collocates with HIGH anchor
M342 (n=13); collocates with HIGH anchor M267 (n=7);
collocates with HIGH anchor M176 (n=5)", truncating at
"collocat;"):

- **M048-01** `positional_statistic` (a): the upgraded
  positional distribution — high frequency (157),
  consistent TERMINAL position. The battery's
  positional leg independently returns PASS on the
  validated roles row (above). The item and the leg
  agree.
- **M048-02 / M048-04 / M048-06** `corpus_count` (a):
  the raw co-occurrence counts with M342 (n=13), M267
  (n=7), M176 (n=5), entered as filed.
- **M048-03 / M048-05 / M048-07** `interpreted_anchor`
  (b): the same collocations as premises under the
  targets' interpreted readings and HIGH standings.

Findings:

1. **The class never rested on the (b) premises.** The
   Round 2 amendment states what each class of the pair
   rests on: M048's U rested on an absence (no
   qualifying filed result), and M089's I rests on its
   battery result, expressly not on its collocation
   counts. This act applies the same statement to M048:
   the class it takes rests on the filed corrected
   battery result, not on the collocation counts in its
   basis. The (b) premises are therefore not load
   bearing in either direction, and the Q3 graph
   audit's outcome for M048 — "unchanged" and weakened
   under both treatments — is the same before and after
   this act (see Downstream effects).
2. **The counts are in any case unreliable as filed.**
   The anchors record carries duplicated collocation
   counts for this sign (M342 at n=13 and n=17; M176 at
   n=5 and n=8; M267 at n=7), noted in the register
   reconciliation (section (h)) and in the F-4 result
   record. They are the anchors record's to correct;
   this act does not correct them, and nothing in the
   decision uses them.
3. **No other class is in question.** No
   external-support claim is filed for M048 (class E
   not engaged); no expert or referral is documented
   behind it (class P not engaged); it is not in the
   `requires_revalidation` population (class R not
   engaged — its Phase-48 promotion stands at
   `insufficient_evidence` under disposition rule R4,
   as one of the GR-088-27 pair with M367, which is why
   T302 never ran on it and why the F-4 commission had
   to produce its result separately).
4. **The parity with M089 is exact in the respect that
   matters.** M089's filed score of 2 is positional
   PASS + bigram PASS + DEDR not run. M048's is
   positional PASS + DEDR PASS + bigram not run. The
   battery counts passes and never counts a `not_run`;
   both readings meet the threshold on executed legs.
   M048's unexecuted leg is unexecuted for a named
   custody reason, and its historical pass (neighbour
   match 3/4, recorded in the WP5 audit reconstruction)
   is carried as an observation and not counted — the
   discipline the F-4 record applied, which this act
   adopts.

## Decision

**M048 takes class I.** The ground the Round 2
amendment made the class turn on — the absence of a
qualifying filed corrected-battery result — no longer
holds: the result is filed and it qualifies. On the
parity the register itself set up for this pair, the
reading stands where M089 stands. The executed
partition becomes **3 E + 66 I + 4 R + 3 P + 18 U =
94**.

What the decision does not do: it does not establish
the reading mu/muṉ — class I is an internally motivated
candidate, reading-level support not demonstrated,
identifiability untested, under the register's standing
definitions. It does not execute the bigram leg. It
does not correct the anchors record's duplicated
counts. It does not speak to M367, the pair's other
member, whose corrected battery result remains
unproduced.

## Downstream effects recorded

- **Spec 099.** The log's executed class for M048
  follows the amended standings (a builder amendment
  arm asserted on this act's amendment text in the
  standings record); no item is added, removed, or
  re-typed, and the census is unchanged (296 items:
  210 (a) / 61 (b) / 25 ambiguous). The Q3 audit
  regenerated over the amended log returns every
  outcome unchanged (0 class changes under both
  treatments; weakened 44 / 63; acyclic), and its JSON
  differs from the pre-act audit in exactly one field,
  M048's `executed_class`. TC-099-01 and TC-099-02
  PASS; the fixture suite passes 15. Record:
  `specs/099-inference-log/records/inference-log-amendment-2026-11-22.md`
  (the second amendment of this date, appended to the
  F-9 amendment record).
- **Spec 098.** The identifiability population (the
  class I readings plus the class E arm) is 69 for any
  future stage (66 I + 3 E). The number matches Stage
  2's executed population by coincidence of count only:
  Stage 2 executed over 65 I + 4 E, with M047 in the E
  arm and M048 outside the population. Stage 1's and
  Stage 2's executed records stand as history at the
  populations they state. Stage 3 is not commissioned
  by this act.
- **Public wording in this repo.** The root README's
  "Where the 94 stand now" paragraph and the
  anchor-model README's standings blockquote are
  updated in this act (sixty-six internally motivated
  candidates; eighteen with insufficient evidence;
  M044 and M047 named among the eighteen). The tracker
  site's corresponding correction is a separate publish
  act, not this one.

## Reopen clause

This act rests on the filed corrected battery result
as it stands. The unexecuted bigram leg cannot lower
the score under the battery's counting rule — a later
pass would raise it to 3, a later fail would leave it
at 2 — so no reopen arises from that leg's later
execution under a future commission. The act reopens
only if the filed result is withdrawn on the record,
or the battery's threshold rule is amended on the
record; in either case M048's class is re-adjudicated
on the amended record.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
