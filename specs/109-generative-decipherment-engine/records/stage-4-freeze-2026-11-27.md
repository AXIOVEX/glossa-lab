# Spec 109 — Stage 4 Freeze (T401, Part 5)

**Date:** 2026-11-27. **Stage frozen:** Stage 4 —
Eteocypriot reading candidates (Part 5), under
registration §6 (`records/registration-2026-11-27.md`),
before any Stage 4 computation. This record fixes
every constant registration §6 marks FREEZE, states
the comparanda determination, and restates the
component drop. Nothing in this stage's records
carries licensing language, resolves or presumes
OD-O-2, or states or implies that any check has been
passed for the Eteocypriot program as a whole
(registration §6; claim C109-6).

## 1. Comparanda determination (registration §6)

The registered comparanda are (a) the bilingual's two
scored Greek name anchors and (b) the E1 derivation
tables, when filed complete under Spec 101's
precondition P-3.

**Determination: (b) is not filed complete at this
freeze; the comparanda are (a) alone, and the
reduction is stated here on the freeze record's
face.** Evidence: Spec 101's precondition P-3
requires that where the E1 machinery is reused, the
freeze addendum reproduce the E1 driver's tables
verbatim (the vowel map, the consonant stems, the ξ
expansion, the diacritic and final-sigma handling,
the R3 dead-vowel default), because Spec 096's
freeze §5 rules R1–R3 were found to underdetermine
the executed derivation (OD-8 finding F-4). Spec
101's freeze addendum
(`specs/101-eteocypriot-next-claim/records/freeze-addendum-2026-11-27.md`)
states on its face that its scoring "uses no E1
driver machinery" and files only its own three
tables (its candidate set, its position definition,
its extraction rule); the E1 tables were therefore
never reproduced under P-3, and the design queue's
E-3 entry, whose precondition is the filed complete
tables, has not executed. The E1 driver's tables
exist in code (pin §5 below) and are reproduced in
§3 of this freeze for this study's own run; code is
not a P-3 filing, and this freeze does not treat it
as one.

**Comparanda (a), in full.** The two scored
correspondences of ICS 196, as filed in Spec 096's
corpus record's `ground_truth_correspondences` and
Spec 096's freeze §5: Ἀρίστωνα (Greek word 5) ↔
segment 6, *a-ri-si-to-no-se*; Ἀριστώνακτος (Greek
word 6) ↔ segment 7, *a-ra-to-wa-na-ka-so-ko-o-se*
(segments numbered 1–11 over the flattened ICS 196
stream, lines in order). The pairings are the
generator's inputs only through the variant
derivations of §2; the ground-truth pairings
themselves are scoring material for the preflight's
name-anchor control (§6) and are never a procedure
input (Spec 096 freeze §5's own discipline).

## 2. The comparanda mapping variants (closed set)

Three variants, each a mechanical derivation of a
comparanda mapping from (a), each registered in a
prior filing:

- **A1 — strict segment-parallel** (Spec 096 freeze
  §5, as executed): the k-th Greek word pairs with
  the k-th Eteocypriot segment, in order. The names
  are Greek words 5 and 6, so A1 pairs Ἀρίστωνα with
  segment 5 and Ἀριστώνακτος with segment 6.
- **A2 — name-anchored free** (Spec 096 freeze §5, as
  executed): each Greek name pairs with the segment
  maximizing LCCS(D(name), segment), ties broken by
  earliest segment.
- **J — joint one-to-one** (Spec 104's registered
  formulation of this same instance): the pairing of
  the two names to two distinct segments maximizing
  the sum of LCCS(D(name), segment) over the pair;
  ties broken by the lexicographically smallest
  pairing (segment of name 1, then segment of
  name 2).

No other variant enters. The variant set is closed
at this freeze.

## 3. The derivation, complete tables (this run)

D(name) is computed by the filed E1 procedure
(Spec 096 freeze §5; driver pin §5), reproduced here
in full so this run uses no unstated table:

- **Vowel map (R1):** α→a, ε→e, η→e, ι→i, ο→o, υ→u,
  ω→o.
- **Consonant stems:** β→p, γ→k, δ→t, ζ→s, θ→t, κ→k,
  λ→l, μ→m, ν→n, π→p, ρ→r, σ→s, τ→t, φ→p, χ→k
  (15 entries).
- **ξ expansion:** ξ expands to the consonant
  sequence k+s before stemming.
- **Diacritics and final sigma:** polytonic
  diacritics are stripped to letter identity; final
  sigma ς is sigma.
- **R2:** a consonant followed by a vowel maps to
  the CV sign (stem + that vowel); the vowel is
  consumed and does not also emit a standalone sign.
- **R3:** a consonant not followed by a vowel
  (cluster member or word-final) maps to stem + a
  dead vowel copying the *preceding* vowel of the
  name (default a, before any vowel).

**Alignment.** For a pairing (name, segment), the
alignment is the longest common contiguous
subsequence (LCCS) between D(name) and the segment;
among alignments achieving the maximum length, the
one at the smallest D-index, then the smallest
segment-index (the filed driver's first-maximum
behaviour).

**Anchored map M_V.** For variant V, over its two
pairings: for each matched position k of an
alignment (D-index i, segment-index j, length L),
the segment sign at j+k is anchored to the value
D[i+k]. A sign receiving two different anchored
values across the pairings is excluded from M_V
and the exclusion is filed; a sign receiving the
same value twice is anchored once.

**Implied endings E_V.** For each pairing, the
ending part of the paired segment: the signs after
the matched subsequence (positions j+L to the
segment's end) when the match ends before the
segment's final sign; when the match reaches the
segment's final sign, the ending part is that final
sign alone. E_V is the set of ending parts over the
two pairings, as sign sequences.

## 4. The ranking (registration §6, mechanized)

**Item set.** The ICS texts as filed in Spec 096's
corpus state (pin §5): ICS 196, the one continuous
text (11 segments); ICS 194/195 at form level and
ICS 193's one form enter as the held-out forms, their
registered role in §6 — no continuous text for them
exists in the corpus state to rank, and none is
constructed. The Androkles A intake is development-
stream material under its own intake record and is
not enumerated in registration §6's item set; it is
not a ranking target. Effective N is per-text sign
count, stated in the outcome record (ICS 196: the
harness's count over the pinned file).

**Candidates.** For ICS 196, one candidate per
variant of §2: the text's segments with each sign
labelled by M_V where defined (unanchored signs
carry no value), and the candidate's implied endings
E_V.

**Component (1) — held-out form prediction (the
E-4 count, mechanized).** key1(V) = the number of
the 8 held-out forms (the 7 ICS 194/195 forms,
45 signs, and the ICS 193 form, as filed in the
corpus record's `attested_forms_only`) whose sign
sequence has some member of E_V as a suffix.

**Component (2) — comparanda coverage.**
key2(V, T) = the share of text T's tokens whose sign
is in the domain of M_V.

**Component (3) — distributional fit: DROPPED**,
restated from registration §6: the E-2 control
calibration (Spec 107 cycle 2, gated on C-E-15,
which returned STOP) did not execute, so no
calibration exists; the ranking runs on components
(1) and (2) only.

**Lexicographic rule.** Candidates for a text are
ranked by key1 descending, then key2 descending,
then variant order A1, A2, J (determinism on a full
tie, filed where it binds).

**Context term: none.** Stage 2's channel verdict
was CHANNEL NULL and the context term is withdrawn
from this study's scoring (Stage 2 close record §4);
Part 5 runs without it, as registered.

## 5. The permutation null (registration §6)

The ranking is recomputed under permuted comparanda
mappings: a uniform random permutation π of the
35-sign development inventory, applied to the
comparanda mapping (M_V becomes {π(s) → M_V(s)}) and
elementwise to every sequence in E_V; key1 and key2
recomputed for all variants; the null statistic is
the maximum key1 over the three variants under π.
**B = 999 permutations; seed 109401** (integer seed
of the harness's PRNG, fixed here). The top rank is
distinguishable iff the observed top key1 exceeds
the 99th percentile of the null statistic's
distribution; a tie at the top of the observed
ranking on both keys is also null-indistinguishability
of the top ranks.

**Verdict rule (registration §6, mechanical form).**
RANKED SET FILED — the observed top key1 exceeds
the null's 99th percentile and the top rank is
unique. RANKING NULL — the top ranks are
null-indistinguishable under either test above.
NOT EXECUTED — the preflight of §6 fails or an input
precondition is unmet, filed with the reason. No
positive or negative decipherment verdict exists for
this part, and none may be filed under it.

## 6. The preflight (registration §2; plan T401)

The Eteocypriot generator's preflight clauses are
the two T401 names: **(S) synthetic syllabary-profile
corpora** and **(N) the name-anchor control**.
Registration §2's remaining clauses are disposed of
on this record's face: clause (ii)'s penalized-margin
form does not apply to this generator, whose
registered scoring is the lexicographic ranking and
its permutation null (§§4–5), not a margin — the
separation test is executed at the part's run under
§5, not in the preflight; clause (iii)'s Latin and
Meroitic R1 controls do not apply, this generator
having no R1 predictor form — its known-truth control
on real material is clause (N), the bilingual's own
ground truth. The positional limitation of
registration §2 is restated: this generator has no
positional clause; the Latin and Meroitic controls'
positional ground-truth sets hold 1 mark and 0 marks
against the measurability floor of 5, and no
positional figure is claimed from them anywhere in
this stage.

**Clause (S) — synthetic corpora.** Five synthetic
corpora (seeds `spec109-s4-synth-{1..5}`, the seed
string's SHA-256 supplying the PRNG seed), each
built to the filed Eteocypriot profile shape: a
35-sign syllabary; a development stream of 11
segments at the real skeleton lengths
[2, 3, 5, 4, 3, 6, 9, 7, 7, 2, 5]; a planted language
of stems and an ending inventory, composed so the
planted instance mirrors the real instance's
alignment shape exactly — LCCS(D1, S6) = 4,
LCCS(D2, S6) = 4, LCCS(D2, S7) = 2, and LCCS of
either planted derived spelling against every other
segment ≤ 2 — with planted name pairings (6, 7),
planted derived spellings D1 (5 signs) and D2
(8 signs, D1 + 3), and 8 planted held-out forms
(finals: the S6 tail ×3, the S7 tail ×2, a third
planted ending ×2, bare ×1). The planted anchored
map is the map the joint variant J derives from the
planted pairings; the construction guarantees every
planted anchored sign carries ≥ 5 tokens in the
synthetic development stream (asserted per corpus),
so registration §2's recovery form — the share of
≥ 5-token planted signs assigned their planted
values — is measurable over the planted anchored
set in full. A corpus failing any construction
assertion is rejected and rebuilt under the next
seed suffix (`-try1`, `-try2`, …), each rejection
filed (the G1-R admission-gate pattern). The
generator of §§2–4, unchanged, runs on each corpus:
recovery = the share of the planted anchored signs
whose planted value the top-ranked candidate's map
assigns. **Floor (FREEZE): median recovery over the
five corpora ≥ 0.80.** Shuffle control: the same run
with the planted derived spellings' sign labels
permuted by a fixed derangement per corpus; **the
shuffle median must be < 0.5 × the right median**
(a generator whose shuffle recovery approaches its
right recovery has measured itself, and fails —
registration §2).

**Clause (N) — name-anchor control.** The harness's
derivation and alignment machinery, run on the
pinned real bilingual, must reproduce the filed
anchor facts exactly: D(Ἀρίστωνα) =
[a, ri, si, to, na]; D(Ἀριστώνακτος) =
[a, ri, si, to, na, ka, to, so]; LCCS(name 1, seg 6)
= 4, LCCS(name 2, seg 6) = 4, LCCS(name 2, seg 7) =
2; A1 pairings (5, 6); A2 pairings (6, 6); the joint
one-to-one optimum = 6 (Spec 104's certified value,
stage-1 outcome record 2026-11-25); ground-truth
pairings (6, 7) used for scoring only. Any mismatch
is a preflight STOP, filed.

**Two implementations.** Every preflight figure is
produced by two independent implementations in exact
agreement (the harness, and the TC-109-07
verification script's independent recomputation); a
disagreement is a preflight STOP, filed.

**Preflight verdict.** PASSED (both clauses at their
floors) — the ranking of §4 may run. FAILED (any
measurable clause below its floor) — Part 5 files
NOT EXECUTED and produces no candidate ranking; the
design, not any criterion, is what a later
registration revises.

## 7. Data pins

| Input | Pin (SHA-256) |
|---|---|
| Spec 096 corpus (`specs/096-eteocypriot-program/corpus/corpus.json`) | `2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597` |
| Androkles intake (development-stream provenance only; not a ranking target) | `8ca9b23c2f455e1e2cd0dbfecebf844f3d904fe95c33a346b2edb38ded139e5a` |
| E1 driver (`specs/096-eteocypriot-program/records/eteocypriot-e1-driver.py`) | `9ec475fd419150e7d07a6a36f3e306eadc62b0427cdb2a4924825870116c9c95` |

Custody for this stage: `glossa-custody/spec109/stage-4/`
on tower-compute (synthetic corpora, candidate
records, raw outputs), never committed; the filed
records carry the pins.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
