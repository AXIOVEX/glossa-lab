# Spec 112 — Meroitic Structure Induction:
Segmentation, Recurrent Partials, and Formula-Slot
Structure over the Pinned Corpus

**Status: REGISTERED 2026-11-28 — registration and
preflight design only. No induction has been executed
under this spec, and no corpus output of any kind
exists. The owner's directive of 2026-11-28 in the
Glossa-Lab chat (Meroitic is the sole active front;
doing nothing on the data in hand is not an option)
commissions this registration. Execution of the
induction itself is a separate, later act under this
registration's own sequence (§6), and no output is
scoreable until the conformance preflight of §4
passes in full.**

**Provenance.** The owner's discovery governance of
2026-11-27 (research programs exist to solve, not
only to find mistakes; generation and adjudication
stay separate; every generator passes a conformance
preflight on known ground truth before its output is
scoreable; ranked candidates are never proclaimed
results; kill-criterion discipline revises the search
design, never the bar). Spec 109 registered structure
induction as Part 2 of the generative engine and its
Stage 1 preflight licensed two output kinds on
synthetic controls while its segmentation family
failed and was closed as filed. This spec is the
Meroitic-native successor to that part: where Spec
109's preflight ran on synthetic ground truth,
Meroitic uniquely supplies REAL ground truth — the
pinned anchor inventory and the known funerary
formula — and this study's preflight runs on that.

## 1. The study

This study induces corpus-internal structure over the
pinned Meroitic corpus: (a) segmentation of long
forms into recurrent constituent parts; (b) recurrent
partials — affix-like substrings with positional
profiles; (c) formula-slot structure over the
funerary texts, as a slot grammar. Its outputs are
ranked candidate structures with full generation
provenance (search state, seed, data pins), filed as
candidates for the program's existing adjudication
gates. An induced segmentation is not a reading, an
induced partial is not a morpheme identification,
and an induced slot is not a translation. Nothing in
this study assigns a meaning to any Meroitic form.

## 2. The corpus, pinned

- **Kovetsky build (S-2 of Spec 102, reused as a
  corpus, not as a vocabulary):** commit `145af083…`,
  source SHA-256 `1e91e3a0…`; the in-corpus
  inscriptions (396 inscriptions, 368 distinct texts
  after exact-text deduplication).
- **The REM-derived text set in custody:** the Otten
  corpus `mero-corpus.txt` (18,090 lines, custody at
  `glossa-custody/spec097/otten-corpus/`, source pin
  `c9158f6865325877112b6b9ceef83b3c80a93c56`), held
  under the custody terms of record (owner risk
  acceptance; never redistributed; aggregate
  statistics only).
- Corpus-derived work respects the partitions
  already of record: Spec 097's split for
  `mero-corpus.txt` (SHA-256 of the full line mod 10
  == 0 is held out; derivation work uses the
  development side only) and exact-text
  deduplication before any counting, everywhere.
- The custody extraction of 2026-11-28 (Spec 102
  custody home) is a vocabulary-side measurement and
  is not an input to this study.

## 3. The three induction targets

- **Segmentation.** A boundary model over word forms:
  for each form above a registered length floor, a
  ranked set of candidate segmentations, each with
  its score and the search state that produced it.
- **Recurrent partials.** Substrings recurring above
  a registered support floor, each with its
  positional profile (initial / medial / final mass)
  and its host-form set. A partial is filed as a
  distributional object only.
- **Formula-slot structure.** Over funerary texts, a
  slot grammar: an ordered slot sequence with
  per-slot filler classes, induced from the text
  stream. The known template (anchor inventory
  Class B: invocation, presentation, filiation 1,
  filiation 2, offering, closing) is the preflight's
  ground truth (§4), NOT an input to the induction:
  the induction runs blind to it, and the preflight
  compares.

## 4. The conformance preflight (registered floors)

The preflight runs before any corpus output is
scoreable, on ground truth that exists independently
of this study's machinery:

- **P-1, segmentation recovery.** Ground truth: the
  segmentations pinned by the anchor inventory's
  formula forms (the filiation forms and the
  theonym-plus-suffix forms of Class B) together
  with the gold morphology of record (Kovetsky
  `data/gold_morphology.json`, pin to be filed at
  the preflight freeze). Floor: median boundary F1
  at least **0.80** over the ground-truth set, the
  floor Spec 109's G1 clause (i) registers for
  recovery.
- **P-2, formula-slot recovery.** Ground truth: the
  Class B slot sequence over a labeled set of
  funerary texts drawn from the development side.
  Floors: the induced grammar's slot sequence
  matches the template order on at least **90%** of
  labeled texts, and the presentation (name) slot is
  the induced grammar's highest-variance slot.
- **P-3, partial validity and the shuffle control.**
  The induced partial set must recover the known
  suffixal partials of the gold morphology at
  precision at least **0.80**; and the identical
  induction run on a token-shuffled corpus (token
  order destroyed within texts, inventory and text
  lengths preserved, seed registered) must yield
  slot structure at no more than **20%** of the real
  run's yield. A shuffle that produces the structure
  anyway falsifies the induction, not the corpus.
- The preflight is judged by an independent
  recomputation from the filed outputs (the
  program's two-implementation discipline), and its
  figures are filed before any corpus run begins.

**No corpus output is scoreable until P-1, P-2, and
P-3 all pass.** A preflight failure closes this
study as filed (§7); it is a finding about the
induction design at this corpus, and it moves no
standing anywhere.

## 5. Relation to Spec 102 and Spec 109 Stage 5

This study is corpus-internal structure only. It
neither consumes nor alters any gate of Spec 102
(the affiliation test's G-1/G-2 and its registered
source discipline stand exactly as registered; this
study's corpus is not a vocabulary source for it),
and it neither consumes nor alters Spec 109 Stage 5
(Meroitic gloss induction, still gated on Spec 102
unchanged). If this study's induced structures are
ever proposed as inputs to either, that proposal is
a new registration under the standing rule, decided
on its own record. This study assigns no gloss to
any form, so by construction it cannot feed the
gloss-induction gate.

## 6. Execution sequence (registered, not yet run)

1. Preflight freeze: corpus pins verified, ground-
   truth sets extracted and pinned to their records
   of origin, floors restated, seeds registered.
2. Preflight run and independent recomputation;
   verdict filed (PASS in full, or the study closes
   under §7).
3. Only on a full pass: the induction runs over the
   pinned corpus, per target (§3), with full
   generation provenance per candidate.
4. Outputs filed as ranked candidate sets with
   margins, for adjudication through the program's
   existing gates. No standing moves in this study.

## 7. Kill criteria

- **KC-1.** Any preflight leg fails its floor: the
  study closes as filed. The response to a failure
  is a revised search design under a new
  registration, never a lowered floor.
- **KC-2.** The shuffle control yields structure
  above its cap: the induction is falsified as a
  measurement, whatever the real run produced, and
  no output is filed as a candidate.
- **KC-3.** A candidate structure is presented
  anywhere as a reading, a morpheme identification,
  or a translation: that presentation is out of
  scope of this registration and the study's record
  is corrected to say so.

## 8. What this study does not do

It does not decipher anything. It does not test
affiliation (Spec 102's province, under its own
gates). It does not extend the vocabulary, score a
concept, or compare Meroitic with any other language.
Its strongest possible product is a set of candidate
structures that survive a real-ground-truth
preflight — the precondition, under the owner's
governance, for any later generation work on
Meroitic to be worth adjudicating at all.
