# Spec 109 — The Generative Decipherment Engine: the
Discovery Side of the Program

**Status: REGISTERED 2026-11-27 — the discovery side
designed and registered by the owner's directive of
2026-11-27 ~13:54 ET in the Glossa-Lab chat, rejecting
a verification-only program and ordering the program
made capable of attempting decipherment, under his
standing blanket approval for Glossa work of 2026-11-27
04:05 ET and his keep-working directive. This landing
registers the engine and its five parts. Execution
follows in this study's Stages 1–5, in the order and
under the registrations filed here. Registration moves
no standing, verdict, or tally in any program, and
nothing in this package is a decipherment claim.**

**Provenance.** The owner's directive above; the
program's existing adjudication machinery as filed
(Spec 091 anchor comparison; Spec 098 identifiability
over the 65, with its frozen decide() rule; Spec 093
the material-context channel; Spec 102 the fresh
affiliation test and its gates G-1 and G-2; Spec 107
the active decipherment loop and its cycle records;
Spec 108 the World Language Graph, release WLG-R1);
the active decipherment design of 2026-11-26 (goal
workspace, `files/active-decipherment-design-2026-11-26.md`),
whose Part 2 queues and Part 1 registration discipline
this spec's parts are written to be lifted from and to
run under; and the multivariate signal inventory of
2026-11-26 (same folder), from which every custody and
data fact below is taken. The owner's governance
record of the same day (the discovery side as standing
program governance, extended to all research programs
and to the VEXA platform) names the five parts this
spec registers; this spec is Glossa-Lab's registered
instance of that governance. The method of work
follows VEXA as the source of truth for how the
programs work, in both directions as the owner stated
the same day: this study conforms to the stack rather
than diverging from it, and what its execution proves
in practice is filed in its records as evidence for
the stack's own change discipline.

## 1. What this spec is

The program's machinery today adjudicates hypotheses
proposed from outside it: anchor comparison tests
readings the literature or earlier specs proposed;
Spec 098 tests hand-built rival assignments; Spec 102
gates an affiliation test designed around a fixed
vocabulary. Candidate values enter only as rivals
inside tests. Nothing in the program generates
candidate readings, searches assignment space on its
own, or ranks self-generated hypotheses against
held-out data. This spec adds that side.

The engine has five parts (§3), one shared preflight
(§2), and one judging rule it does not own (§4):

1. **Assignment search (Indus first).** The program
   generates its own sign-value assignments: constraint
   propagation from the established anchors and the
   induced positional classes, plus stochastic search
   optimizing cross-validated predictive likelihood,
   adjudicated on genuinely held-out material under
   the frozen rule.
2. **Sign-class and structure induction.** Mechanized
   induction of positional classes, segmentation
   boundaries, and affix-like recurrent partials across
   the full corpus — the Ventris-grid move, generalized
   and mechanized — with the numerical and
   metrological subsystems as a separate induction
   target. Induced structure is filed as generated
   hypotheses and faces the existing gates.
3. **Context channel.** The Spec 093 outputs (site,
   material, find context) and seal iconography joined
   to sign-distribution analysis, so context scores
   candidates instead of only recording provenance.
4. **Meroitic gloss induction.** Distributional
   induction of candidate glosses against the surviving
   candidate families' lexicons, under the same
   held-out discipline, registered now — before
   Spec 102's digitisation lands — and gated on it.
5. **Eteocypriot reading candidates.** Corpus-level
   generation and ranking of candidate readings for
   the ICS texts, replacing the consumed-pair
   bottleneck with a ranked candidate set.

**Separation, registered.** Generation and
adjudication stay separate throughout: the engine
proposes, the existing frozen gates dispose. A
generator's output is a ranked candidate set with
margins against the permutation null, never a single
proclaimed reading. No output of this study is a
reading, a gloss, or a decipherment; standings move
only through the existing gates on filed outcome
records, exactly as Spec 107's trace discipline
(C107-5, C107-11) already provides. LLMs and general
AI tools are excluded as scorers, adjudicators, and
validators under this spec, as under Spec 107; they
may draft analysis code, which is then tested under
the registrations like any other code.

## 2. The conformance preflight (shared, OD-O-1 pattern)

No generator's output on an undeciphered system is
scored before that generator has passed its
conformance preflight: the generator must recover
known ground truth on controls whose truth is known,
before its output on a system whose truth is unknown
is scoreable. The pattern is OD-O-1's, built into
Spec 107's cycle-2 registration for I-2 and discharged
there (preflight passed in full: target shape exact;
achieved duplication exactly the registered rate in
120 of 120 replications; ground-truth sets in exact
two-implementation agreement).

The preflight has three clauses, each registered in
full at `records/registration-2026-11-27.md` §2:

- **(a) Synthetic ground truth.** The generator is run
  on ciphered synthetic corpora of known assignment,
  built to the target system's profile (artifact count,
  token count, length distribution, duplication rate)
  by the Spec 107 I-1/I-2 simulation machinery, and
  must recover the planted assignment at the registered
  floors.
- **(b) Deciphered controls.** The generator is run on
  the Latin and Meroitic controls of Spec 107, in the
  R1 predictor form in which cycle 2 measured both
  donors positive at 1× (Meroitic RIGHT 0.6822 /
  WRONG −0.0438 / SHUFFLE 0.2263; Latin 0.4338 /
  −0.5388 / 0.1019). The positional clause of the
  preflight is registered against the limitation
  cycle 2 filed: the re-specified positional
  ground-truth sets held 1 mark (Meroitic) and 0 marks
  (Latin) against the measurability floor of 5, so
  positional recovery on those two controls is NOT
  MEASURABLE as filed, and the preflight does not
  pretend otherwise — its positional clause runs on
  the synthetic controls of clause (a), whose ground
  truth is planted at adequate counts, and the
  Latin/Meroitic limitation is carried on the
  preflight record's face.
- **(c) Two-implementation agreement.** Every
  ground-truth set and every recovery figure is
  produced by two independent implementations in exact
  agreement, as in Spec 107's preflight.

A generator that has not passed its preflight produces
no scoreable output. A preflight failure is the leg's
filed outcome; the generator's design, not any bar, is
what gets revised.

## 3. The five parts

The full registrations — item sets, pins, method,
nulls, verdict rules, falsifiers, kill criteria, and
information requirements — are filed at
`records/registration-2026-11-27.md` §§3–7. In brief:

- **Part 1 — Assignment search (Indus).** Search space:
  the derivation set's 372 marks. Hard constraints:
  the values of anchors standing E in the register,
  held fixed, and the positional classes induced by
  Part 2 as filed. Value inventory: for each unanchored
  sign, the phonetic value-classes of the candidate
  families as filed in the World Language Graph's
  dossiers (release WLG-R1), plus a structural class
  (logographic / numerical / classifier) — the graph is
  the hypothesis space for language-side candidates,
  used as filed. Method: constraint propagation from
  the hard constraints, then simulated annealing with
  registered restarts and seeds, optimizing
  duplicate-aware cross-validated predictive likelihood
  under the frozen scoring rule's predictor form.
  Adjudication: the search's top-K candidates (K = 20,
  registered) are scored once on the sealed split of
  §5 under Spec 098's frozen decide() rule, against
  the permutation null (B = 999, seed 9801, frozen) and
  the structural-only rival. Output: the ranked set
  with penalized margins. Kill criterion: if the best
  candidate fails the frozen bar on the sealed split,
  the leg files SEARCH NEGATIVE AT THE FROZEN BAR; the
  bar is not lowered, and the search design — space,
  constraints, objective — is what a later registration
  revises.
- **Part 2 — Structure induction (Indus).** Mechanized
  induction over the full corpus (390 marks, 1,670
  artifacts): positional classes re-derived and
  extended; segmentation boundaries induced by the
  registered boundary statistics; affix-like recurrent
  partials (initial and final) extracted with their
  positional restrictions; and, as a separate target,
  the numerical/metrological subsystem (the counted
  and stroke-series contexts), tested for bounded
  range, positional restriction, and consistent
  combination by arithmetic self-checks. Every induced
  structure is filed as a generated structure
  hypothesis with full provenance, and then faces the
  existing gates (anchor comparison, identifiability);
  induction itself moves no standing.
- **Part 3 — Context channel (Indus).** Joins, as
  registered: the Spec 093 joined census (179 pairs:
  site, material, find context — with its filed limit,
  all Mohenjo-daro, single stratum, carried on the
  channel's face); the tracked population files'
  per-seal site field over the 1,670-seal population
  (phase100 / phase114, keyed by `cisi_id`); and the
  iconography sub-channel, which is GATED (§6) and
  inactive at registration. Context enters candidate
  scoring as a registered additive evidence term with
  its own context-label permutation null, so context
  can never lift a candidate beyond what the null
  allows.
- **Part 4 — Meroitic gloss induction.** Registered
  now; executes only when Spec 102's digitisation has
  landed and its freeze exists. Consumes Spec 102's
  frozen filtered vocabulary and family sets as filed;
  changes neither G-1 nor G-2; if Spec 102 closes
  NOT ADMINISTERED, this part files the same gated
  outcome rather than sourcing vocabulary elsewhere.
  Method: distributional profiles of Meroitic forms
  matched against the candidate families' lexicon
  entries, generating ranked gloss candidates per form,
  scored by prediction on the frozen partition's
  33 held-out texts, with permutation nulls and the
  wrong-family control of the M-2 design.
- **Part 5 — Eteocypriot reading candidates.**
  Generation at corpus level: for each ICS text,
  candidate readings composed from the transliteration
  and the registered comparanda (the bilingual name
  anchors; the E1 derivation tables when filed complete
  under Spec 101's precondition P-3), ranked by
  comparanda coverage, distributional fit, and
  prediction of the held-out forms (the 7 ICS 194/195
  forms and the ICS 193 form, at form level). This
  replaces the pair-by-pair route that cycle 2's
  C-E-15 decision closed as STOP with a ranked
  candidate set. It carries no licensing language and
  does not touch OD-O-2 (§7).

## 4. The judging rule (owned elsewhere, used as filed)

All adjudication under this spec uses Spec 098's
frozen decide() rule, verbatim: a candidate is
DISCRIMINATED only if its penalized margin over the
best rival is at least **10 nats**, exceeds the **99th
percentile** of the frozen permutation null
(**B = 999, seed 9801**), and rests on at least
**5 held-out tokens** per scored sign; every free
choice — each searched assignment, each gloss
alternation — is charged **2 nats** against the
candidate's margin, rivals charged identically; the
candidate must also beat the structural-only rival.
The outcome vocabulary is Spec 098's: DISCRIMINATED
ON PSEUDO-HELD-OUT where the material is in-corpus,
IDENTIFIABLE ON HELD-OUT only on a genuine holdout,
NOT IDENTIFIABLE and UNDECIDABLE AT THIS POWER as
there defined. This spec amends none of it. Where a
part's material cannot support the rule (a split below
its floors), the part files the rule's own
indeterminate outcome rather than a weaker substitute.

## 5. Held-out discipline

The Indus sandbox reserve's seal is spent (opened at
Spec 105 Stage 6 as registered); no part of this spec
pretends otherwise. Part 1's adjudication therefore
uses a fresh sealed split — the **109 reserve** — cut
duplicate-aware from the derivation set at Part 1's
freeze under this registration: its membership is
hash-committed in the freeze record before any search
run that could be scored against it, it is opened
exactly once, at scoring, and the opening is recorded.
The search's internal objective (cross-validated
predictive likelihood) is computed on the derivation
set only, by duplicate-aware folds; no sequence
appears on both sides of any fold or of the split.
If the 109 reserve's effective size falls below the
floors the frozen rule needs, Part 1 files
INDETERMINATE AT THIS POWER and does not fall back to
scoring on derivation material under a held-out label.
Meroitic uses its frozen partition (335 development /
33 held out) as filed; Eteocypriot uses its filed
form-level holdout. The five-rung preference order of
Spec 107 §2 Step 4 governs wherever a part must choose
a weaker design, and a part for which no rung is
available is not executed.

## 6. The iconography sub-channel: what exists, what does not

Stated exactly, from the signal inventory of
2026-11-26 and the Spec 091 custody statement:

- **Exists, in custody only:** per-seal iconography
  labels over the 1,670-seal population, in the Holdat
  corpus CSV's `iconography` column. The file is held
  only in the owner's custody and the mini-server
  origin tree (pin SHA-256 `62d14d2b…`); it is
  gitignored and unheld in every working clone. Terms
  on file: statistical derivatives only; the file's
  scans and rows are never redistributed; **no written
  permission is on file** (the confirmation letter of
  2026-11-20 is unanswered), and every Holdat-derived
  result is labelled "not reproducible from held
  records" at the register's face.
- **Exists, tracked, but unjoinable as filed:** the
  Phase-134/135 adjudicated motif codes for 100 + 100
  pilot objects (CISI ids, motif codes, object_type —
  no sign sequences, so they cannot be joined to signs
  without assembling a CISI-keyed sign table for those
  200 objects from the population files); and the
  Mayig CISI-layer corpus (179 seals, P-number sign
  ids, unicorn-only descriptions).
- **Does not exist:** any tracked per-seal sign × motif
  join over the population; any iconography coding for
  any Eteocypriot or Meroitic text; a population-level
  medium/support variable (the phase100 object_type is
  the literal `?`; there is no period field).
- **What a real iconography channel needs:** the
  tracked (cisi_id, iconography) join. The registered
  route to it is Spec 100 — deposit of a tracked
  per-seal iconography CSV extracted from the pinned
  Holdat build by an extractor that refuses any source
  whose hash differs from the pin — and Spec 100's
  gate opens only on Miller's reply to the 2026-11-20
  permission letter. This spec does not route around
  that gate: Part 3's iconography sub-channel is
  registered GATED, activates only when Spec 100's
  gate opens or an equivalent tracked join lands under
  its own registration, and until then every context
  score this study files is labelled as carrying no
  iconography component.

## 7. Relation to standing decisions and gates

- **OD-O-2** (Eteocypriot continuation under the
  O-E-1/O-E-2 conformance qualifications) stands
  unruled by the owner and untouched by this spec.
  Part 5 neither resolves it nor presumes it: its
  records carry no licensing language, and no "all
  checks passed" statement appears anywhere in this
  study's Eteocypriot records.
- **Spec 102's gates** (G-1: at least 40 scored
  concepts per family test, at least 20 outside the
  twelve; G-2: at least 80% injection power at
  θ = 0.30, d = 0.75; falsifier NOT ADMINISTERED, gates
  never lowered) are consumed by Part 4 as filed and
  are not changed, waived, or routed around. Part 4 is
  not the affiliation test and cannot return its
  verdict.
- **Spec 100's gate** is as §6 states. **Spec 103**
  is not reopened. **T502/T503** remain uncommissioned.
  The **Otten corpus** is not an input to any part of
  this spec; Part 4's lexicon input is the Rilly
  material under Spec 102's custody terms, not Otten.
- **Spec 107's loop** may rank this study's legs in
  future cycles under its own discipline, unchanged;
  this spec is not a Spec 107 cycle, because its
  claims and kill criteria are its own (D-109-5).

## 8. Provenance and replay

Every generated candidate — assignment, structure
hypothesis, context score, gloss candidate, reading
candidate — carries its full generation provenance in
its candidate record: the generator's identity and
version pin, the search state (for stochastic search,
the state hash and the point in the registered
schedule), the seed, the data pins of every input, and
the constraint-set version it was generated under. A
result is filed only if replay from its candidate
records reproduces the candidate set exactly
(TC-109-03). Candidate records and search
intermediates live in custody on tower-compute under
`glossa-custody/spec109/` and are never committed; the
filed outcome records carry the pins so any reader can
re-acquire the identical bytes and replay.

## 9. Kill criteria

Per leg, the kill criteria are registered with each
part (registration §§3–7). The study-level criteria,
any one of which closes the affected part on the
record, are:

1. **Null yield at the frozen bar.** A part's best
   self-generated candidate cannot beat the null at
   the frozen bar on genuinely held-out material. The
   outcome is filed; the search design is revised in a
   later registration; the bar is never revised.
2. **Preflight failure.** A generator fails its
   conformance preflight, or its preflight's
   measurable clauses return NOT MEASURABLE at the
   registered floors. The generator produces no
   scoreable output until a revised generator passes.
3. **Control failure.** A part's pipeline succeeds on
   its scramble or wrong-family control at the strength
   it claims on its target — it has measured itself,
   and the part closes until the pipeline is redesigned
   and re-registered.
4. **Gate dependence.** A part's registered input gate
   closes unmet (Spec 102 NOT ADMINISTERED for Part 4;
   Spec 100's gate still closed at Part 3's iconography
   stage). The part files its gated outcome and stops;
   it does not source its input elsewhere.
5. **Integrity tripwire.** Any breach of a custody
   term, a gate condition, or the registration
   discipline — an unregistered analysis entering the
   record, a seal mishandled, restricted bytes used
   beyond their terms — halts the study immediately,
   on the program's standing rule, until the breach is
   recorded and the owner rules.

## 10. Stages

- **Stage 0 — Registration (this landing).** The
  engine, the shared preflight, the five parts'
  registrations, the claims intake, and the mechanical
  audits of TC-109-01.
- **Stage 1 — Preflight.** The preflight harness built
  and run for the Indus generators (Parts 1–3 share
  the harness; Parts 4 and 5 run their own preflight
  clauses at their stages, before any of their output
  is scored). No undeciphered-system output is scored
  in this stage.
- **Stage 2 — Structure induction and the context
  channel (Parts 2 and 3).** Induction over the full
  corpus; the context joins built and validated; the
  generated-hypotheses register opened; induced
  structures filed to the existing gates.
- **Stage 3 — Assignment search (Part 1).** The 109
  reserve cut and sealed; the search run under its
  registration; the top-K adjudicated once, on the
  opened split; the ranked candidate set and the
  outcome filed.
- **Stage 4 — Eteocypriot reading candidates
  (Part 5).** Preflight clauses for the Eteocypriot
  generator; corpus-level candidate generation and
  ranking; the ranked sets filed.
- **Stage 5 — Meroitic gloss induction (Part 4).**
  Gated on Spec 102's digitisation and freeze, as
  registered; executes when its inputs exist, files
  its gated outcome if they close unmet.

The execution order is registered, with its reasoning,
at `records/registration-2026-11-27.md` §1: induction
before search, because the search propagates from the
induced classes; the context channel built in the same
stage, because it is independent and cheap; the search
only after both; Eteocypriot after the Indus legs,
because its generator reuses the harness at the
smallest corpus size; Meroitic last, because its input
does not yet exist.

## 11. Decisions

- **D-109-1 (number).** At the check of 2026-11-27 the
  highest landed spec package on origin/main was 108
  (`specs/108-world-language-graph/`); no 109 directory
  or open pull request carried 109 (the one open pull
  request, #799, carries Spec 107 material only). This
  package takes 109.
- **D-109-2 (taxonomy).** Spec 109 sits under Program
  infrastructure / Governance, lifecycle & generated
  layers, with Specs 104, 106, and 107: it is program
  method, not a language study. Its legs are executed
  for the three language programs but registered as
  this study's claims, in the pattern of Specs 106
  and 107.
- **D-109-3 (no recommendations-ledger row).** The
  study's provenance is the owner's direct directive,
  not a Co-scientist recommendation; as with Specs
  104, 106, and 107, no row is added.
- **D-109-4 (custody).** Candidate records and search
  intermediates are held in custody on tower-compute
  under `glossa-custody/spec109/`, never committed, in
  the pattern of D-105-8 and D-107-5. Holdat-derived
  material, if the iconography sub-channel ever
  activates, stays under the Holdat terms of §6 and is
  handled inside Spec 100's own discipline, not here.
- **D-109-5 (separate spec, not a cycle).** The engine
  is registered as its own spec rather than as a
  Spec 107 cycle: its claims, preflight, and kill
  criteria are its own, and its stages are gated on
  inputs (Spec 102's digitisation) the loop does not
  control. The loop's queues may cite this study's
  legs; neither study amends the other.

## 12. Standing

Registration moves no standing, verdict, or tally in
any program. The standings effects this study may ever
produce are exactly those its registrations license,
each through an existing gate on a filed outcome
record, and are stated part by part in the registration
(§8's information table): Parts 2, 3, and 5 rank and
file hypotheses only; Part 1 can put a candidate
before Spec 098's gate and no further; Part 4 can put
gloss candidates before the program's candidate
adjudication machinery and no further. No part of this
study converts its own output into a standing.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
