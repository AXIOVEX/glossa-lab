# Spec 112 — Revision registration (the revised Meroitic structure induction)

Filed 2026-11-28, after the first execution's conformance preflight
FAILED all three legs (`records/preflight-2026-11-28.md`, PR #814,
merge `63408e1c`) and the study closed as filed under kill criterion
KC-1. KC-1 and claim C112-7 prescribe the response: a revised search
design under a new registration, never a lowered bar. This is that
registration. It is filed **inside Spec 112**, not as a successor
spec, following the program's own discipline for kill-criterion
revisions: Spec 110's revision was registered inside Spec 110
(`records/revision-registration-2026-11-27.md`, claims C110-7..11 as
a second bundle), and Spec 109's G1-R and G1-E revisions stayed
inside Spec 109. A successor number marks a new study (Spec 112
itself succeeded Spec 109 Part 2 on a new corpus and a new ground
truth); here the study, the corpus, the floors, and the ground truth
carry over and only the search design changes.

Worker worktree `~/.syncyard/worktrees/glossa/spec112-rev-wt-20261128`,
branch `spec-112-revision`, off main `63408e1c` (the merge of
PR #814). The landing base is re-checked at landing time; the intake
cascade is re-executed over the merged build if main has moved, and
the cascade record says so on its face.

## 1. What does not change

- **Every floor, verbatim.** P-1: median boundary F1 ≥ 0.80 over the
  1,719 ground-truth forms. P-2: slot-sequence match ≥ 90% of the 95
  labeled texts AND the presentation (name) slot the
  highest-variance (filler-entropy) slot. P-3: partial precision
  ≥ 0.80 AND shuffle yield ≤ 20% of the real yield.
- **The ground-truth sets, byte-identical.** The revision's freeze
  re-extracts them under the carried construction and requires the
  filed sets' SHA-256 (`a9e30b54a6f477683e9ac9dc352b7c51390803b536fbbb91a3b2620f67a0149a`)
  before any computation; the gold suffix union (24 strings), the
  filiation strings, and the theonym forms are exactly as filed.
- **The scoring rules.** P-1: top-1 boundaries against the pinned
  boundaries, exact rational arithmetic. P-2: the comparison side is
  carried verbatim — the labeled-set construction, the Class B
  template order (invocation, presentation, filiation 1, filiation
  2, offering, closing), and the match rule's form (the induced
  sequence equals the template order restricted to the labeled
  slots, with every labeled slot induced). P-3: precision is
  proposals ∩ the gold union over proposals, as filed.
- **The corpus, the partitions, the tokenization, the streams.**
  Same pins (Kovetsky build `145af083…`, source SHA-256
  `1e91e3a0…`; Otten custody pin `c9158f68…`, corpus SHA-256
  `b7f3350c…`), same development/held-out rule, same pooled-stream
  handling, same funerary stream (210 texts), same labeled set
  (95 texts). The carried shuffle constructions keep seed 20261128.
- **The kill criteria KC-1..KC-3**, applied to the revision: if any
  leg of the revision's preflight fails, the revision closes as
  filed. This registration commissions no second revision.
- **Claims C112-1..C112-7 stand unamended.** The revision adds four
  claims, C112-8..C112-11 (§5), intaken through the full cascade.

## 2. The three filed mechanisms and the design answers

### 2.1 P-1 — the whole-form degeneracy, and the inventory floor beneath it

Filed mechanism: the whole-form fallback was scored under its own
positional class (W), whose smoothed log-probability is the same
constant (≈ −8.17 nats) for every form, so the unsegmented candidate
beat every genuine segmentation on all 1,719 forms (median F1 = 0).

Design answer, in two parts:

1. **Class W is abolished.** The segment inventory is uniform: every
   substring with support ≥ the registered floor in distinct host
   forms, plus every single character. There is no whole-form
   fallback segment and no inventory bypass. Candidate
   segmentations are restricted to **two or more segments** — a
   segmentation is a decomposition, and the one-piece candidate
   does not exist as a scored object, so no whole-span
   classification question arises. The effective fallback is the
   all-single-character segmentation, scored by the same rule as
   every other candidate.
2. **The inventory support floor is 2 distinct host forms** (the
   first design carried 3). Development (§3) found the second half
   of the filed failure: at floor 3 the gold segmentation was
   *unreachable* for most hard-fixture forms — the stem side of the
   true segmentation is a string recurring in fewer than 3 forms,
   so the dynamic program could not select it at any score
   (measured: on three inspected forms the gold segmentation
   outscored the returned one, −17.30/−14.89/−16.46 against
   −18.47/−21.68/−16.56, and was absent from the inventory).
   Floor 2 is the smallest floor that still requires recurrence —
   the study's founding notion — and §3 measures the alternatives:
   floor 3 leaves the median at 0.667 on the hard fixture, floor 1
   admits every hapax string and the median collapses to 0.

Everything else about the segmenter carries: positional classes
I/F/M counted over distinct development forms, add-0.1 smoothing,
boundary penalty 2.0 nats per boundary, K_BEST 5 ranked
segmentations per form with margins, scored forms of length ≥ 5.
No EM recount is registered: hard EM and soft EM were both measured
in development and neither improves the design (hard EM degrades
it, §3); the counts are the raw substring counts.

**Fixture proof (registered as an execution precondition, TC-112-10).**
Before the preflight runs, the frozen harness must show, on the
registered fixtures: (a) no one-segment candidate appears in any
top-5; (b) on the easy fixture the planted segmentation outscores
the all-character fallback on the planted forms; (c) the median
boundary F1 on both fixtures is ≥ 0.80. If any fixture proof fails,
the preflight does not run and the revision closes as filed.

### 2.2 P-2 — band collision replaced by a sequence-anchored grammar

Filed mechanism: the filiation forms are positionally diffuse
(`tedxelowi` 88 occurrences and `terikelowi` 97 spread across all
six positional bands), so the band model mapped both filiation
slots to one band and the slot sequence matched on 1 of 95 labeled
texts. The name-slot sub-leg held (presentation entropy strictly
greatest) and carries over.

Design answer: the positional-band slot model is retired. The
revision induces a **sequence grammar** anchored on the text's
frames, in this registered order:

1. **Invocation frame.** t0 = the modal first token type over the
   funerary development texts; t1 = the modal second type among
   texts opening with t0. (Development measurement: t0 = `woSi`,
   136 of 210 texts; the pair covers 101 of 210, 0.481.)
2. **Offering anchor.** Among token types of length 3–4 with ≥ 50
   occurrences, ≤ 1.25 occurrences per containing text, and ≥ 75%
   of occurrences at relative position ≥ 0.4 in their texts, the
   anchor is the type covering the most texts. Its family adds the
   types having the anchor as a proper prefix with total length
   ≤ 7. (Development: `ato`, 150 occurrences in 144 texts, 1.04 per
   text, 82.0% late; the nearest competitor `at` covers 137 texts;
   `mXe` is excluded by the per-text cap at 1.79.)
3. **Filiation paradigms.** Candidate strings of length 4–6; a
   candidate's hosts are the funerary token types containing it;
   its zone fraction is the share of its occurrences, in texts
   where the frame pair is found, falling strictly after the frame
   pair and before the first offering-family token; its
   initial-share is the share of its host occurrences in which it
   heads the token. A candidate qualifies at ≥ 10 host types,
   ≥ 50 occurrences, zone fraction ≥ 0.70, initial-share ≥ 0.50.
   Marker A is the qualifying candidate with the most occurrences;
   marker B is the qualifying candidate with the most occurrences
   among those neither substring nor superstring of A whose host
   set overlaps A's by less than half of the smaller set. A token
   belongs to a paradigm iff it contains the paradigm's marker; a
   token containing both markers belongs to the paradigm whose
   marker occurs first in it. (Development: A = `tedx`, 23 hosts,
   172 occurrences, zone 0.77, initial-share 0.971; B = `teri`,
   16 hosts, 130 occurrences, zone 0.75, initial-share 0.985. The
   stacked complexes are excluded by the initial-share rule —
   `lowi` heads 0.022 of its host occurrences, `qowi` 0.114 — and
   the closing fragments `pSoX` and `yetm` by the zone rule.)
   Known limitation, disclosed: the spelling variant `tdxe`
   (3 host types, 8 occurrences) is not a substring variant the
   rule can reach; 3 of the 95 labeled texts rest their filiation 1
   on `tdxe` spellings alone. The floor tolerates 9 failures.
4. **Slot order, induced.** Pairwise precedence majorities among
   the anchor classes, over texts containing both, decide
   filiation 1 before filiation 2 and the filiations before the
   offering; invocation is first and closing last by construction;
   presentation is the zone between the frame and the first anchor.
   The grammar's slot sequence is the induced order. If the
   majorities induce an order different from the Class B template,
   the match test fails on the order — the comparison keeps its
   teeth. (Development: filiation precedence majority 0.786 for the
   tedxe paradigm over 56 labeled texts carrying both; offering
   after first filiation 0.981 over 107 texts.)
5. **Parse.** Frame types, wherever they occur, and any tokens
   before the first frame token → invocation. Non-anchor tokens
   after the frame span and before the first filiation or offering
   token → presentation fillers. Paradigm tokens → filiation 1 /
   filiation 2. Offering-family tokens → offering. Tokens after
   the last anchor token → closing fillers. Remaining non-anchor
   tokens → fillers of the most recent anchor slot. A text's
   induced sequence is its induced slots in the grammar's slot
   order. Slot entropies are computed over each slot's filler-type
   set across the funerary development corpus, exactly as carried.
6. **Yield (the shuffle leg's statistic).** A slot yields iff:
   invocation — the frame pair covers ≥ 1/3 of the funerary texts;
   presentation — the presentation zone is non-empty in ≥ 1/3 of
   texts carrying the frame and at least one later anchor;
   filiation 1 and filiation 2 — the paradigm is found and the
   pair's precedence majority is ≥ 2/3; offering — the anchor is
   found and the offering-after-filiation majority is ≥ 2/3;
   closing — tokens follow the last anchor in ≥ 1/3 of anchored
   texts. The shuffle control permutes token order within texts
   (carried construction, seed 20261128) and the same induction
   runs over the shuffled texts; the ratio cap is as carried.

### 2.3 P-3 — partials proposed by the segmenter, not by a mass threshold

Filed mechanism: a raw final-mass threshold selects the endings of
frequent forms generally — 36 proposals, 4 gold (precision 1/9 as
filed against the scored subset) — because stacked complexes reach
final mass 0.96 (`owi` complex) and 0.73 (`Ewi` complex) while short
gold suffixes are diluted by medial occurrences. Development (§3)
measured that no positional-mass or nesting statistic separates
the gold inventory from the complexes: the gold inventory is itself
nested (`lowi` contains the `owi` tail), and a dominance rule that
removes the complexes removes gold `lowi` with them.

Design answer: **a partial is proposed iff it is the final segment,
of length ≥ 2, of the revised segmenter's top-1 segmentation** of a
pooled development form whose residual (the form minus its final
segment) has length ≥ 3, **and its distinct-residual support
reaches τ_st**, where τ_st is re-derived on the development
partition only: τ_st is the maximum distinct-residual support
attained by any length ≥ 2 final segment when the same segmenter
runs over a character-shuffled null corpus (each development
form's characters permuted, seed 20261128). The proposal must
recur across distinct stems and stand in the suffixal position
class as the segmenter — whose scoring the P-1 preflight validates
against the gold morphology — actually cuts it; the full-form
score, stem side included, arbitrates the stacked complexes
instead of a final-class count. The full induced partial set
(every length ≥ 2 substring at the carried support floor, with its
statistics) is filed alongside the proposals, as in the first
execution. Precision is computed as carried, against the same gold
union. **Shuffle leg:** the frozen proposal rule, τ_st included,
is applied to a second, independent character-shuffled corpus
(seed 20261129); its proposal count is the shuffle yield, against
the carried 20% cap.

## 3. Development evidence (disclosed; no verdict figure computed)

Design choices were made on synthetic fixtures and on corpus
statistics that are not verdict figures, following the program's
G1-E precedent: design on development material, disclose, freeze,
then run the preflight once. The real ground-truth median F1, the
real slot match rate, the real slot entropies, and the real
precision were **not** computed in development.

- **P-1 fixtures.** Easy fixture (2,400 forms, planted stems and
  suffixes, seed 20261130): revised design median F1 = 1.000; the
  planted segmentation outscores the all-character fallback on
  2,376 of 2,400 forms; zero one-segment candidates in any top-5.
  Hard fixture (2,600 forms; stems built from 130 recurrent root
  pieces under Zipf weights so stem-internal recurrence competes;
  the planted suffix inventory is the actual 24 gold strings; 62%
  stem+suffix, 26% stem+suffix+suffix stacks, 12% bare stems, 6%
  defective spellings; seeds 20261130 and 20261201): support ≥ 3 →
  median F1 0.667 on both seeds; support ≥ 2 → median 1.000
  (exact-match share 0.592 / 0.581); support ≥ 1 → median 0.000.
  Hard EM (25 rounds) at support ≥ 2 degrades the exact share
  (0.557 / 0.571); soft EM at support ≥ 3 leaves the median at
  0.667; the boundary penalty λ ∈ {2, 3, 4, 5, 6} moves nothing.
  Failure anatomy at support ≥ 3: exact 49.4%; the dominant class
  is the returned final segment absorbing stem-final characters,
  and margin inspection showed the gold segmentation outscoring
  the returned one while absent from the inventory (§2.1).
- **P-2 statistics** (development funerary stream; design
  statistics only): frame coverage, anchor competition, paradigm
  candidate table, precedence majorities, and the `tdxe` exposure,
  as quoted in §2.2. The presentation zone is non-empty in 0.949
  of anchored texts.
- **P-3 statistics** (development partition): the full candidate
  table of the first execution stands (36 suffixal proposals under
  the retired rule, 4 gold); the complexes' statistics are as
  quoted in §2.3. No distributional statistic tried in development
  — final mass, suffixal-class mass, stack ratios, residual
  final-character concentration, dominance over proper suffixes —
  separates gold from complexes; that negative result is the
  reason the proposal rule is segmenter-based.

## 4. Execution sequence (registered)

1. Freeze commit: this registration as landed; the revised harness
   and the independent verifier, hash-frozen in the freeze record;
   corpus pins re-verified; ground-truth sets re-extracted and
   checked byte-identical to the filed sets.
2. Fixture proofs (TC-112-10) — a precondition gate: any failure
   closes the revision as filed without a preflight run.
3. The preflight, run once, judged by independent recomputation
   (TC-112-11) against the carried floors.
4. Corpus induction **only** on a preflight PASS IN FULL: ranked
   segmentations with margins and full generation provenance for
   the pooled forms; the partial proposals and the full partial
   set; the sequence grammar with per-text slot assignments. No
   meanings are assigned to anything (KC-3).
5. Close record, landing by pull request under the standing
   discipline; PROGRAM-STATE updated at each landing.

## 5. The revision's claims

Four claims, C112-8..C112-11, filed in `claims.md` as the
revision's claims and intaken as the bundle `claims-revision.json`:

- **C112-8** — the revised design is the design this registration
  specifies (corrected segmentation scoring with no whole-form
  class and a support floor of 2; the sequence-anchored slot
  grammar; segmenter-based partial proposals under a null-derived
  threshold), and no leg of the revision runs under any other
  design.
- **C112-9** — the revision's preflight gates the revision's
  output, judged by independent recomputation against the same
  floors, ground-truth sets, and scoring rules as the first
  execution.
- **C112-10** — the revision's outcome is the filed outcome: a
  pass licenses the revision's induction and nothing else; a
  failure closes the revision as filed, and a further revision is
  outside this registration.
- **C112-11** — non-interference carries: the revision writes
  nothing into Spec 102's or Spec 109's trees, changes no gate,
  source rule, or pin of either, supplies no vocabulary to
  Spec 102, and assigns no gloss or meaning to any Meroitic form.

Test cases TC-112-09 (revision package form), TC-112-10 (fixture
proofs), and TC-112-11 (revision two-implementation agreement) are
added to `test-cases.md`; TC-112-04 and TC-112-08 apply to the
revision unchanged.

*This record was executed by an AI agent (Muse, via Muse) at the
direction of Tristen Pierson, per constitution sec. VI.*
