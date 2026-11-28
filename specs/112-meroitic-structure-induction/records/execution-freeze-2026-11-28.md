# Spec 112 — Execution Freeze (2026-11-28)

This record is the preflight freeze of spec.md §6 step 1,
committed before any computation under this registration.
It verifies the corpus pins, extracts and pins the
ground-truth sets, restates the floors, registers the
seeds, and fixes the induction design in mechanical form.
The machinery is records/execution-harness.py (SHA-256
`95a3ecd8bcaa420c57ffd5923fe42b33964ede524493abf0ac342641a7086038`);
the independent recomputation of TC-112-06 is
records/execution-verify.py (SHA-256
`a5c3f2aebc7535bf3ed9dac88e533aa99afd3fbf643cb3605d04e31a2866b143`),
written and frozen alongside the harness, before the
preflight runs.

## 1. Corpus pins (TC-112-02, recomputed from the objects)

- Kovetsky build: commit
  `145af0836c071e7c9796d37d4b36add00d347c8a`;
  `data/inscriptions.jsonl` SHA-256
  `1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`
  — both recompute to the values spec.md §2 registers.
- Gold morphology (Kovetsky `data/gold_morphology.json`,
  26 entries) SHA-256
  `c5dc8f3479e81a270a3ee68a9f602c125dcc1211c5fa8b1f8091e56b4bf8a5b8`
  — the pin spec.md §4 leaves to this freeze.
- Otten corpus: source pin
  `c9158f6865325877112b6b9ceef83b3c80a93c56`;
  `Data/mero-corpus.txt` SHA-256
  `b7f3350c2f2118a8223854462a8e881c424cba6b26c01ebfb676efa92ea253ce`,
  equal to the Spec 097 step-0 manifest value; 18,090
  lines. Held in custody at
  `glossa-custody/spec097/otten-corpus/` under the custody
  terms of record (owner risk acceptance; never
  redistributed; aggregate statistics only). Nothing in
  this execution redistributes it: outputs file counts,
  profiles, and candidate structures over forms, and the
  induction outputs are mirrored to custody, not published
  from the corpus text.

## 2. Corpus construction (of record, not invented here)

- Kovetsky stream: the build's `text` field,
  exact-text deduplication first — 368 distinct texts,
  the construction of Spec 097 freeze v2 §1. Partition
  of record: a distinct text is held out iff
  SHA-256(text) mod 10 == 0 (335 development / 33 held
  out). Derivation work uses the development side only.
  (The "396 inscriptions" of spec.md §2 is the build's
  own census of inscriptions machine-readable under an
  open licence, per the Spec 097 citation-discipline
  record; the working corpus is the 368 distinct texts,
  as in every prior execution on this build.)
- Otten stream: the Spec 097 split of spec.md §2 — a
  line is held out iff SHA-256(full line) mod 10 == 0
  (16,265 development lines / 1,825 held out), then
  exact-text deduplication before any counting
  (16,176 distinct development lines).
- Tokenization (registered here): split on whitespace
  and `.`; keep tokens that are purely alphabetic.
  Distinct development forms: Kovetsky 2,015, Otten
  1,734, pooled 3,532. The two streams are pooled in
  their filed spellings, not folded into one another;
  the ground-truth extraction handles each stream with
  its own gold list (§3). The Otten file's name-swap
  augmentation is part of the pinned corpus as filed;
  all counting in this study is over distinct forms or
  distinct texts, never over raw token occurrences in
  that file, so the augmentation multiplicity does not
  enter any statistic.

## 3. Ground-truth sets (TC-112-03)

Extracted mechanically from their records of origin by
the harness's `extract` command and filed at
records/ground-truth-sets.json, SHA-256
`a9e30b54a6f477683e9ac9dc352b7c51390803b536fbbb91a3b2620f67a0149a`.
The filed set recomputes byte-identically from the
pinned objects. Rules, per stream, over distinct
development forms of length at least 5:

- **Gold-suffix rule.** Gold suffix strings are the
  gold morphology's suffix entries (form with a
  leading '-') that carry a corpus form: the entry's
  `corpus_form` plus its `corpus_variants`, in the
  stream's spelling (the Kovetsky stream writes the
  o-sign 'o' where the Otten spelling writes 'E', per
  the build's transliteration map of record, so its
  list is the E→o fold). A form carries a boundary at
  the onset of the LONGEST gold suffix that leaves a
  stem of at least 3 characters.
- **Filiation rule (Class B).** A form containing a
  filiation form (`tedxe`, `tdxe`, `terike`, `yerike`)
  beginning at position 2 or later carries a boundary
  at its first such onset (the name + filiation-form
  fusion the anchor inventory pins).
- **Theonym rule (Class B).** The exact theonym-plus-
  suffix forms (Otten `wESi`, `SEreyi`, `aSEreyi`;
  Kovetsky `woSi`, `Soreyi`, `aSoreyi`) carry a
  boundary before the final -i.

Composition of the set: 1,719 forms (Kovetsky 1,059,
Otten 660); 1,703 forms with one boundary, 16 with
two; the gold-suffix rule fired on 1,718 forms, the
filiation rule on 14, the theonym rule on 3.
Disclosure, on the record: the anchor inventory
freeze carries the theonym suffix as debated and not
frozen; spec.md §4 names the theonym-plus-suffix
forms as P-1 ground truth, and this freeze follows
Spec 112's registration. The theonym forms are 3 of
1,719 and cannot carry the median.

## 4. The induction design (registered, mechanical)

**Segmentation.** A positional-class unigram dynamic-
programming segmenter over the distinct development
forms. Segment statistics are counted over the
distinct forms (each form contributes its substrings
once), by positional class: I (form-initial), F
(form-final), M (medial), W (whole form). The segment
inventory is every substring with support at least 3
distinct host forms, plus every single character, plus
the whole form itself as a fallback segment.
P(segment | class) is the class count with add-0.1
smoothing over the class vocabulary. A segmentation's
score is the sum of log P(segment | class) over its
segments minus a boundary penalty of 2.0 nats per
boundary. Ranked candidates are the 5 best
segmentations per form; the margin is the top-1 minus
top-2 score. Length floor: forms of length at least 5
(spec.md §3).

**Recurrent partials.** Every substring of length
2..8 with support at least 10 distinct host forms,
counted over the distinct development forms. The
positional profile counts each occurrence within a
host form once (initial / medial / final mass);
an occurrence spanning a whole form counts toward
support only, not toward the profile. A partial is
filed as a distributional object with its support,
profile, and host-form set.

**Formula-slot structure.** Over the Kovetsky
funerary development distinct texts with at least 4
cleaned tokens (210 texts). Each token type carries a
positional profile: its occurrences' relative
positions (index / (length - 1)) in 6 equal bands,
its modal band, its modal mass, its centroid. A type
is concentrated iff it has at least 10 occurrences
and modal mass at least 0.60. The slot yield of a
run is the number of bands holding at least 5
concentrated types. A token's slot is the slot its
type's modal band maps to (types with fewer than 3
occurrences take their occurrence's band).

## 5. The preflight, operationalized (spec.md §4)

Floors restated, unmoved: P-1 median boundary F1 at
least 0.80; P-2 slot-sequence match at least 90% with
the name slot the highest-variance slot; P-3 partial
precision at least 0.80 and shuffle yield at most 20%
of the real yield.

- **P-1.** For each ground-truth form, the
  segmenter's top-1 boundary set against the pinned
  boundary set, boundary F1 per form (exact rational
  arithmetic), the median over the 1,719 forms.
- **P-2.** The labeled set: funerary development
  texts with at least 8 cleaned tokens whose opening
  zone carries the invocation pair (a `woSi` token at
  index at most 3 and a `Soreyi`/`aSoreyi` token at
  index at most 4, in that order) and at least one
  filiation token. Labels are extracted from the
  pinned forms only: invocation (the opening span);
  presentation (a non-empty span between the
  invocation and the first filiation or offering
  token); filiation 1 / 2 (the first token containing
  a teɖe-form / a terike-form after the invocation);
  offering (the first `ato` token, or `ato`-initial
  token of length at most 7, after the invocation);
  closing (any token after the last anchor token).
  The comparison maps bands to template slots by the
  pinned forms, mechanically: the invocation slot is
  the modal band of the type `woSi`; filiation 1 the
  modal band of the most frequent teɖe-containing
  type; filiation 2 likewise for terike; offering the
  modal band of `ato`; of the unmapped bands,
  presentation is the earliest by band centroid after
  the invocation band, and closing the latest. A
  text matches iff its induced slot sequence
  (distinct slots in order of first occurrence;
  tokens in unmapped bands are skipped) equals the
  Class B template order restricted to its labeled
  slots, with every labeled slot induced. The
  highest-variance leg is read as filler-class
  entropy: the presentation slot's filler-type
  entropy (bits, over the funerary development
  corpus) must be strictly the greatest of the
  mapped slots'.
  Disclosure: the band count, 6, is a design
  parameter of the positional discretization,
  registered here; the Class B template's forms,
  labels, and order are not inputs to any induction
  computation — they enter only at this comparison,
  as C112-5 requires. If two pinned slots' types
  share one modal band, the mapping cannot separate
  them and the leg fails on that fact, honestly.
- **P-3.** The induced partial set's suffixal
  proposals — partials whose final mass is at least
  0.80 — are the set over which precision is
  computed: precision is the fraction of proposals
  that are gold suffixal partials (exact string
  equality against the union of both streams' gold
  suffix lists of §3). The recall of the gold
  suffixal partials is filed alongside, for
  transparency; the verdict follows the registered
  precision. The shuffle control: the funerary
  texts' tokens are permuted within each text
  (inventory and text lengths preserved), seed
  20261128, and the identical slot induction runs;
  its yield must be at most 20% of the real run's
  yield (a real yield of 0 fails the leg).
- **TC-112-05 fixture.** A synthetic corpus of 120
  texts generated with seed 20261128 from a planted
  six-slot formula (fixed invocation pair, a
  40-name presentation pool, fused filiation forms,
  offering and closing fillers) verifies the slot
  machinery and the shuffle construction: the
  ordered run must recover the structure (mapping
  found, sequence match at least 90%, name slot the
  maximum-entropy slot) and the shuffled run's
  yield must fall to at most 20% of the ordered
  run's.
- **Judgement.** The preflight figures are recomputed
  by the independent implementation (TC-112-06):
  rational figures must agree exactly, entropies to
  1e-9 with the same argmax. The verdict is filed
  before any corpus run begins. TC-112-04: at this
  freeze the study's record tree contains no
  corpus-output file, and none is produced unless
  the filed verdict is a full pass.

## 6. Seeds and provenance

One seed, 20261128, registered for the shuffle
control and the fixture; every other computation is
deterministic given the pins. Every filed candidate
carries the provenance block: harness SHA-256, the
corpus pins of §1, the seed, and this freeze's commit.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) under the owner's 2026-11-28 direction.
