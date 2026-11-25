# Spec 105 — The ELSEWHERE Sandbox: Assumption-Free Derivation over the Three Corpora from a Declared Floor of Primitives

**Status: REGISTERED 2026-11-25 — registration and
Stage 1 execution both commissioned by the owner's
order of 2026-11-25 (Glossa-Lab chat: "use ELSEWHERE
and define the only primitives as things we know
without a doubt and derive our own mathematical and
language meaning systems. Assume nothing about the
real world, we do this in our ELSEWHERE sandbox for
all 3 languages"; the quantum arm of Spec 104 was
skipped by the same order's preceding word).**
Registration lands first; Stage 1 (the dataset builds
and the L0–L1 derivations, §6) follows in a separate
landing under the same commission, exactly as
registered here. Nothing has been built or derived at
registration.

**Provenance.** The owner's decipherment gap analysis
(program document, 2026-11-25) established that each
of the three programs is blocked by missing
information, not by method or compute, and the owner
then directed a different instrument: a sandbox in
the ELSEWHERE discipline, in which the inside derives
everything from a declared floor of primitives and
assumes nothing from outside, and the outside world
acts only as a checker at gates. The Riemann program
runs its own ELSEWHERE line (its Spec 018, hardware
primitives); this study is a separate line in this
repo, over corpus primitives. The shared element is
the discipline only; no content of the Riemann line
is imported (D-105-9).

## 1. What this spec is

Three sealed sandboxes, one per corpus — Indus,
Eteocypriot, Meroitic — in each of which a
mathematical and meaning system is to be **derived**
from a floor of primitives that are known without a
doubt about the recorded corpora (§2), up a
registered ladder of derivations (§5), and tested
only at boundary gates where an outside checker
returns GOOD / NOT-GOOD (§6 of the ladder, §7 here).
No result crosses between sandboxes. Nothing derived
inside a sandbox is a decipherment claim: sandbox
outputs are labelled sandbox-internal until a
boundary gate returns GOOD, and even a GOOD gate
licenses only the specific comparison it checked
(C105-5).

The two languages whose readings are independently
known outside the sandbox — Eteocypriot (the Cypriot
syllabary values) and Meroitic (the sound values) —
are the method's proving ground: an assumption-free
derivation that cannot recover structure consistent
with what is independently known has failed, whatever
it produces for Indus. Indus, which has no outside
reading, is tested by prediction against withheld
inscriptions instead (G-IND, §7).

## 2. The floor — the primitives census

The floor admits only what is known without a doubt
about the recorded corpora. The census is a
deliverable of this registration: every candidate
primitive is admitted or demoted, and every demotion
is recorded with its reason.

**The one admitted input assumption.** The recordings
themselves: the token streams as recorded in the
three source corpora at their pins (§3). The sandbox
takes the recorded streams as the given world. It
does not assert that a recording is correct, complete,
or faithful to any artifact in the world; it asserts
only what the recording contains.

**Admitted primitives.**

- **P-1 Distinction.** Two recorded marks are the
  same mark or different marks, as recorded. Sameness
  is identity of the recorded mark, nothing more: no
  similarity, no near-sameness, no normalization. (In
  the Meroitic streams, `S` and `s` are different
  marks; in the Eteocypriot streams, `[sa]` and `sa`
  are different marks; editorial characters embedded
  in a recorded mark stand as recorded, and their
  editorial meaning is not admitted.)
- **P-2 Sequence.** Marks occur in an order in the
  recording: before / after. The order is the
  recording's order. Any claim equating it with a
  physical reading direction on an artifact is not
  admitted.
- **P-3 Co-presence.** Marks share an artifact, and,
  where the recording records grouping or lines,
  share a group or a line. A recorded grouping is
  structure as recorded; it is not a word, a name, or
  any other unit of language.
- **P-4 Recurrence.** A pattern of marks occurs
  again. Recurrence is the bare fact of occurring
  again, not a count.
- **P-5 Boundary.** An artifact begins and ends;
  lines break where the recording breaks them; groups
  begin and end where the recording groups them.

**Demoted candidates** (considered for the floor and
refused; each is either derived up the ladder or
excluded from the sandbox entirely):

- **Counting and number** — demoted to derived (L2).
  Admitting arithmetic as a primitive would smuggle
  in what the sandbox must earn from recurrence.
  (Stage records report sizes and censuses as the
  program's bookkeeping about the sandbox, as every
  program record does; no derivation inside the
  sandbox uses a number before L2 earns it.)
- **Frequency and probability** — demoted to derived
  (L2 and above). Not doubt-free as primitives: they
  are counting wearing a ratio.
- **"Word"** — refused as a concept. Recorded
  groupings are admitted as structure (P-3, P-5);
  calling a group a word is an interpretation from
  outside.
- **Phonetic value, sign value, transliteration
  value** — refused. These exist outside the sandbox
  (the Cypriot syllabary values; the Meroitic sound
  values) and serve only as boundary-check material
  at the gates (§7). Inside, a mark is its recorded
  identity and nothing else.
- **Any sign list or sign inventory from
  scholarship** — refused as an input. An inventory
  is derived at L1 or it does not exist in the
  sandbox. The programs' working sign lists are never
  sandbox inputs and never receive sandbox outputs
  (§8).
- **Language family, lexicon, grammar, translation,
  gloss** — refused. All are outside knowledge or
  outside claims.
- **Word boundaries beyond the recorded grouping** —
  refused. Segmentation is derived at L3–L4 or not
  claimed.
- **Meaning from iconography, find context, or
  material** — refused. No context of any kind enters
  a sandbox; the build strips it (§3).
- **Mark similarity** — refused (see P-1).
- **Cross-corpus mark identity** — refused. No mark
  in one sandbox is ever identified with a mark in
  another; the sandboxes share a procedure, never a
  result (C105-4).

## 3. The three sandboxes and their builds

**Dataset schema (the only fields a sandbox dataset
may carry).** A dataset is a JSON object naming its
sandbox and listing its artifacts in recorded order.
Each artifact is an object with one field, `lines`:
a list of lines; each line is a list of groups; each
group is a list of marks (strings, exactly as
recorded). Nothing else: no identifiers, no metadata,
no annotation. Artifact identity inside a dataset is
positional (the artifact's index in recorded order).
The build record (§6) maps positions to source
identifiers **outside** the datasets, so a dataset
can be audited without carrying any annotation
itself. Where a corpus records no lines, an artifact
carries one line; where it records no grouping, the
line carries one group.

**Custody.** Datasets are held in custody on
tower-compute (`~/glossa-custody/spec105/`), never
committed to this repo: the Indus dataset is the
pinned Holdat corpus in stripped form and Holdat
custody rules are unchanged (D-105-8), and the same
treatment is applied to all three for uniformity.
The repo carries the build and derivation scripts,
the datasets' SHA-256 hashes, the recorded censuses,
and the derived inventories — never the streams.

### 3.1 Indus sandbox

- **Source.** The Holdat corpus file `indus_corpus
  2.csv`, SHA-256
  `62d14d2bebf7c2c80d98a2958e75ec52bff3f240ff3f5e85d1f7f40cbe28218e`
  (the Spec 100 pin), read from the primary data
  home on the mini-server
  (`~/glossa-data/corpora/holdatllc_indus/`); the
  operational copy on tower-compute is verified
  against the pin before the build reads it.
- **Strip rule (mechanical).** The file is one row
  per token. The build reads exactly four columns —
  `form` (the artifact key), `seal_id` (the artifact
  order), `position` (the token order), `letters`
  (the mark) — and no other column. Artifacts are
  ordered by `seal_id` ascending; each artifact's
  stream is its rows' `letters` values ordered by
  `position` ascending; one line, one group per
  artifact (the file records no lines and no
  grouping). Every other column the file carries —
  site, iconography, part-of-speech and morpheme
  annotations, semantic roles, counts — is annotation
  and is never carried.
- **Recorded census (counted at registration; the
  build must reproduce it or stop).** 1,670
  artifacts; 7,002 tokens; 390 distinct recorded
  marks; positions contiguous from 0 within every
  artifact.
- **Partition (for G-IND).** Artifact index i
  (0-based, recorded order): the reserve iff
  i mod 5 = 4 — 334 reserve artifacts; the derivation
  set is the remaining 1,336. Two dataset files are
  built (`indus-derivation`, `indus-reserve`). The
  reserve is sealed: its hash is filed at build, and
  no derivation at any stage reads it until the
  G-IND gate stage unseals it under its own
  registration (§7).

### 3.2 Eteocypriot sandbox

- **Sources.** Spec 096's corpus
  (`specs/096-eteocypriot-program/corpus/corpus.json`,
  SHA-256 of the current recorded bytes
  `2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597`)
  and its Androkles intake extension
  (`corpus-androkles-intake-2026-11-22.json`,
  SHA-256
  `8ca9b23c2f455e1e2cd0dbfecebf844f3d904fe95c33a346b2edb38ded139e5a`).
  This study pins the current recorded bytes, not
  Spec 096's freeze pin: that pin is stale (finding
  F-104-1 of Spec 104 — red-team rounds changed
  glosses, metadata, and the version field after the
  freeze; the Eteocypriot lines and correspondences
  were proven unchanged by semantic diff, and the
  recomputed scoring matrix matched the filed run
  record exactly). Refreshing Spec 096's pin is Spec
  096's housekeeping, not this study's act (D-105-5).
- **Strip rule (mechanical).** Records are selected
  by their recorded `split` and stream presence,
  and for each selected record the build reads only
  its recorded lines of segments of marks:
  ICS 196 from `corpus.json` (`eteocypriot_lines`)
  and Androkles Dedication A from the intake file
  (`eteocypriot_side.lines`), both split
  `development`. Lines, segments (as groups), and
  marks are carried exactly as recorded, including
  the recorded marks `[sa]` and `?` (P-1). The Greek
  sides, the ground-truth correspondences, the sign
  apparatus, translations, dates, and every other
  field are annotation or boundary-check material
  and are never carried.
- **Exclusions (by rule; the build does not read the
  excluded records' content).** ICS 193 and ICS
  194–195: split `heldout`, sealed under Spec 096 —
  excluded entirely, their content unread by the
  build; the sandbox's reserve for this corpus is
  that standing seal, held by Spec 096, and no
  reserve dataset is built. ICS 217: split
  `control`, and no Eteocypriot stream is recorded
  for it — excluded. Androkles B: no sign-level
  stream exists in the edition of record (established
  2026-11-22, OD-10) — excluded, there is nothing to
  strip.
- **Recorded census.** 2 artifacts; 3 lines; 14
  groups; 69 tokens (ICS 196: 54; Androkles A: 15).
  The thinness is the corpus's recorded state, stated
  plainly: this sandbox is small because the corpus
  is small, and no stage of this study inflates it.

### 3.3 Meroitic sandbox

- **Source.** The Kovetsky build at pin
  `145af0836c071e7c9796d37d4b36add00d347c8a` (the
  Spec 097 corpus build, as Spec 103 executed
  against), file `data/inscriptions.jsonl`, SHA-256
  `1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`.
- **Strip rule (mechanical).** One row per artifact,
  in file order. A row enters the sandbox iff it
  carries a recorded stream (its `text` field is
  present and non-empty); the stream is that field's
  character sequence exactly as recorded — marks are
  the recorded characters, the space character is
  the recorded grouping boundary (groups are the
  maximal non-space runs), one line per artifact. No
  lowercasing, no normalization, no reading of the
  row's `readings`, site, kind, or any other field:
  those are annotation and are never carried. (The
  `text` field is the same recorded stream Spec
  103's frozen basis used.)
- **Recorded census.** 652 rows in the source file;
  376 carry a recorded stream and enter as
  artifacts; 276 carry no stream (`text` null) and
  are excluded by the rule above, counted here so
  the exclusion is on the record. 29,843 character
  tokens; 5,195 groups; 34 distinct recorded
  characters (23 letters, the lacuna mark `.`, and
  the ten digits, which stand in the streams as
  recorded — 39 artifacts carry a digit).
- **No partition.** G-MER (§7) is a validation gate
  against outside readings and needs no reserve;
  Spec 097's development / held-out partition was
  consumed by its own stages (Spec 102's record:
  the 33 held-out texts were read by Stage 4.4 and
  are consumed as evidence), so no reserve is carved
  here (D-105-7).

## 4. What a derivation is, inside the sandbox

A derivation is a ladder rung: a named step whose
only inputs are the floor (§2) and the outputs of
lower rungs **of the same sandbox**, logged with its
inputs in the stage record. A step that needs
anything else is not a derivation; it is an import,
and imports are forbidden. The derivation scripts
read the sandbox datasets and nothing else
(TC-105-05).

## 5. The derivation ladder

- **L0 — Distinction and persistence.** The recorded
  streams as the given world: artifacts, lines,
  groups, tokens, each token a mark as recorded
  (P-1, P-2, P-3, P-5). Output: the sandbox's token
  streams, censused as recorded.
- **L1 — Equivalence and inventory.** Two marks are
  equivalent iff they are the same mark as recorded
  (P-1); the inventory is the set of equivalence
  classes over the derivation set, each class marked
  as recurring or singleton by P-4. Output: the
  derived inventory. It is filed beside the programs'
  working sign lists, never merged into them (§8).
- **L2 — Counting and frequency.** Number is derived
  from recurrence: a mark's count is its recurrences
  tallied; frequency is count against the whole.
  Registered, **not executed in Stage 1**.
- **L3 — Order structure.** Positional patterns from
  P-2 and P-5: which marks and classes begin, end,
  and neighbour; a derived combinatorics of the
  streams. Registered, not executed in Stage 1.
- **L4 — Substitution classes.** Marks that exchange
  in parallel contexts (same neighbours, P-3) form
  paradigms; groupings may be re-derived here if the
  classes earn them. Registered, not executed in
  Stage 1.
- **L5 — The derived meaning system.** A mark's
  meaning inside the sandbox **is** its derived
  structural role: its substitution class, its
  positions, its companions. Nothing more is claimed,
  and the claim is about the sandbox's system, not
  about any language in the world.
- **L6 — Boundary gates.** §7. The only point at
  which anything outside a sandbox is consulted, and
  then only by a checker returning GOOD / NOT-GOOD.

## 6. Stage 1 — what executes under this registration

Stage 1 executes the builds of §3 and the L0–L1
derivations of §5, per sandbox, in this order:
(i) source pins verified (a pin failure stops that
sandbox and is filed as its outcome); (ii) the
dataset built by the registered strip rule, its
SHA-256 filed; (iii) the stripping verification
(TC-105-04) and strip-fidelity checks (TC-105-02,
TC-105-03) pass before any derivation reads the
dataset; (iv) L0 and L1 run under two independently
written derivation implementations, whose inventories
must agree exactly (TC-105-05); (v) the outcome
record files, per sandbox: the source pins as
verified, the dataset hash, the recorded census as
reproduced by the build, the derived inventory (the
marks themselves, with each class's recurrence mark),
and the raw outputs. Stage 1's outcome vocabulary,
per sandbox: **COMPLETED** (build and derivations as
registered) / **STOPPED** (the step that failed,
named, with its evidence). No gate is executed in
Stage 1, and Stage 1 returns no verdict about any
language.

## 7. The boundary gates (registered; executed in later stages)

A gate is run by a **checker** that stands outside
the sandbox: the checker may see outside material;
the sandbox never does. The checker returns exactly
one word per registered comparison — **GOOD** or
**NOT-GOOD** — and the sandbox receives nothing else:
no values, no corrections, no hints. (Per the
ELSEWHERE rule of 2026-11-05, close-or-similar passes
the first gates: a comparison's tolerance is part of
its registration at gate stage, frozen before the
gate runs.)

- **G-ETE (validation, Eteocypriot).** The derived
  structure (L1 inventory and, when derived, the
  L3–L4 structure) is compared against the known
  Cypriot syllabary values by the checker. GOOD on a
  comparison licenses only that comparison: it says
  the assumption-free derivation recovered structure
  consistent with what is independently known, at
  that rung. NOT-GOOD at any rung is a failure of
  the method at that rung, filed as such.
- **G-MER (validation, Meroitic).** The same shape,
  against the known Meroitic sound values.
- **G-IND (prediction, Indus).** The derived Indus
  system (at L4–L5, in the gate's stage) must predict
  the sealed reserve's streams (§3.1): the checker
  unseals the reserve, scores the derived system's
  predictions of each reserve stream's marks in
  sequence against a registered baseline — the
  sandbox's own L2 frequency model, the most
  elementary predictor the ladder itself produces —
  by per-token log-loss, and returns GOOD only if
  the derived system beats the baseline by the
  margin the gate stage freezes in its registration
  **before** the reserve is unsealed. Otherwise
  NOT-GOOD, and the derived Indus meaning system
  stays sandbox-internal, permanently unless a later
  gate says otherwise.

## 8. Hard limits

- No standing, verdict, or tally in any program
  moves by anything this study files (C105-5). The
  derived inventories are filed in this spec's
  records, beside the programs' working sign lists,
  and are never merged into them, cited as sign
  lists, or used as evidence for or against any
  reading, anchor, or claim in any program.
- No cross-sandbox data or result is used anywhere
  (C105-4). The three Stage 1 derivations share the
  registered procedure and nothing else.
- Sealed material stays sealed: Spec 096's held-out
  inscriptions are not read by any part of this
  study, and the Indus reserve is not read by any
  derivation until G-IND's stage unseals it.
- Holdat custody is unchanged: the pinned bytes are
  read from their custody home, the operational copy
  is hash-verified, and no Holdat stream — raw or
  stripped — is committed to this repo or
  redistributed.
- All computation runs on tower-compute; none in the
  Muse VM. No external contact of any kind.
- Later stages (L2 and above, and every gate) execute
  only under their own registrations amending this
  spec; Stage 1's commission covers Stage 1 only.

## 9. Decisions

- **D-105-1 — number.** At the check of 2026-11-25
  the highest landed spec package on origin/main was
  104 (`specs/104-quantum-alignment-benchmark/`); no
  105 directory existed and no branch carried 105.
  This package takes 105.
- **D-105-2 — taxonomy.** This study is entered in
  the program-map taxonomy under Sign inventory &
  corpus / Signary & corpus models (with Specs 097,
  102, 103): its Stage 1 claims are about corpora and
  their derived inventories. Studies 105 → 106.
- **D-105-3 — no recommendations-ledger row.** The
  study's provenance is the owner's direct order of
  2026-11-25, not a Co-scientist recommendation; the
  recommendations ledger logs Co-scientist
  recommendations (the D-104-4 pattern). No row is
  added.
- **D-105-4 — commission.** The owner's order of
  2026-11-25 commissions registration **and** Stage 1
  execution in one act, in two landings: this
  registration first, the Stage 1 execution second,
  as its own record. L2 and above and all gates are
  **not** commissioned by that act.
- **D-105-5 — Eteocypriot source pin.** The build
  pins the current recorded bytes of Spec 096's
  corpus (§3.2), not the stale freeze pin (finding
  F-104-1, whose evidence — semantic diff confined
  to glosses, metadata, and version; recomputed
  matrix byte-equal to the filed run record — is
  adopted here). The freeze pin's refresh is Spec
  096's housekeeping.
- **D-105-6 — the Indus reserve rule.** No standing
  whole-inscription seal exists for the Holdat
  corpus, so G-IND's withheld set is created here by
  the registered deterministic rule of §3.1 (index
  mod 5 = 4), sealed by hash at build. A
  deterministic rule, fixed before any derivation,
  is used rather than a drawn sample so the build is
  exactly reproducible.
- **D-105-7 — Meroitic scope.** The sandbox takes
  the stream-carrying rows of the pinned build
  (376 of 652) and no partition (§3.3). The 276
  stream-less rows are not token streams and cannot
  enter a sandbox whose only admitted input is token
  streams; the exclusion is mechanical and counted,
  not editorial.
- **D-105-8 — datasets in custody.** All three
  datasets are held in custody on tower-compute and
  never committed (§3), so the Holdat strip and the
  other two strips receive one treatment and no
  stream leaves custody in this study's landings.
- **D-105-9 — the Riemann line.** The ELSEWHERE
  discipline is shared with the Riemann program's
  line by the owner's framework; this study imports
  none of its content, primitives, or results, and
  its gates are this study's own.

## 10. Proof map (one page)

| Step | Content |
|---|---|
| Floor | Five admitted primitives (distinction, sequence, co-presence, recurrence, boundary) over the recorded token streams, the recordings themselves the one admitted input assumption; every other candidate demoted with its reason (§2). |
| Builds | Three mechanical strips (§3): Indus from the pinned Holdat bytes (4 columns read), Eteocypriot from Spec 096's two corpus files (2 stream-carrying records; the sealed held-out records unread), Meroitic from the pinned build's `text` fields (376 of 652 rows). Schema admits marks, lines, groups, and nothing else; annotation survival is a test failure (TC-105-04). |
| Partitions | Indus reserve (334 artifacts, deterministic rule) sealed by hash for G-IND; Eteocypriot's reserve is Spec 096's standing seal, never built; Meroitic takes no partition (its gate is validation, not prediction). |
| Ladder | L0 distinction/persistence and L1 equivalence/inventory execute in Stage 1, under two independent implementations that must agree (TC-105-05); L2–L5 are registered designs only; meaning at L5 is structural role and nothing more (§5). |
| Gates | Checker outside, one word back (GOOD / NOT-GOOD): G-ETE and G-MER validate the method against independently known readings; G-IND tests prediction on the sealed reserve against the ladder's own L2 baseline, margin frozen before unsealing (§7). |
| Bounds | Sandbox-internal until a gate says GOOD, and then only for the comparison checked. No standing, verdict, or tally moves; no inventory merges into a working sign list (C105-5). |

The design is the most elementary the order allows:
the floor is five facts about recordings that no one
disputes, the strips are column-and-field selections
stated in one paragraph each, and every concept the
tradition usually assumes — number, word, value,
inventory — is either derived on the ladder or
refused at the floor. Anything simpler would have to
admit one of those concepts as a primitive, which is
exactly what the sandbox exists to avoid.
