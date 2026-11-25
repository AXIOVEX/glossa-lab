# Spec 106 — ELSEWHERE as a Formal Framework, and the Baseline
World-Model Templates for the Indus, Eteocypriot, and Meroitic Programs

**Status: REGISTERED 2026-11-25 — methodology, framework
specification, and baseline templates only. No instance is
spawned, no claim is tested, and no standing moves under this
registration. Instance spawning is a later stage and needs its
own commission.**

**Provenance.** The owner's orders in the Glossa-Lab chat of
2026-11-25: at 12:27 ET, an ELSEWHERE sandbox for the three
languages (registered separately as Spec 105, the
language-internal floor); at 12:39 ET, the correction and
expansion — claims are made outside an instance and tested
inside it, multiple instances may be spawned to explore and to
brute force declared hypothesis spaces, and an instance models
the whole known world of its period (geography, politics, people
movement, DNA, and the other bearing domains), not language
alone; at 12:44 ET, the order that ELSEWHERE be made a formal
framework, program-agnostic, with its mechanics and history
documented. This spec registers all three orders' common
deliverable: the framework and the templates.

## 1. What this spec is

Three things, in one package:

1. **The ELSEWHERE Framework Specification, Version 1**
   (`framework.md` in this package; standalone program copy at
   the goal workspace). Program-agnostic: precise definitions of
   the moving parts (baseline template, axiom and kind label,
   instance, seed, claim, translation, derivation, evidence set,
   checker, verdict, ensemble, iteration, retirement, solution),
   the seeding protocol, the iteration protocol, the solution
   criterion with its exact status vocabulary, and the provenance
   standard (the seed-and-iteration log). Glossa specifics are
   kept out of the framework core.
2. **Three baseline templates** (`templates/`), one per
   language program, each the spawn-ready baseline for that
   program's instances: eight domains under one shared schema,
   Domain 1 (language-internal) carried by reference to
   Spec 105, Domains 2–8 censused for this study (235 axioms in
   total across the three templates), and each template carrying
   its own seed record in the framework's provenance format.
3. **Spec 106's own seed-and-iteration log, opened**
   (`records/elsewhere-seed-and-iteration-log.md`), with the
   seed entry for this study. No iteration has run. The
   framework also carries the history-ledger standard for
   every study (framework §10: a first-class ledger opened at
   registration and written as the work happens, the
   separation rule, and the BACKFILLED marking rule), of
   which the ELSEWHERE log is the ELSEWHERE-specific form;
   this study's log serves in that dual role.

## 2. The framework in brief

The full text is `framework.md`; this section is a map, not a
substitute. Claims are stated at the reasoning level, in plain
language. An instance is a closed model world built from a
declared axiom set; every axiom carries a kind label — (F) floor
fact, (K) period knowledge with its source named, (H) hypothesis
declared openly — and an assumption enters only as a labeled
axiom of specific instances, with siblings carrying its
alternatives or its negation. Evidence is not an axiom: the
corpora and the fixed record are the checker data every instance
is scored against at registered contact points, and an axiom set
that derives a contradiction with the evidence dies. An ensemble
reads three ways — robust, axiom-tracking (which names the next
evidence to hunt), or dead. A claim is a SOLUTION only when it
derives in every surviving instance of its ensemble and has
passed the adopting program's ordinary boundary gates; anything
less carries its exact status label. Every study keeps a
seed-and-iteration log from which the whole path from seed to
any claim's status can be reconstructed.

Adoption note (framework §10): the RCPH / Ladder Ring Theory
program, the Riemann program, and VEXA are directed separately,
in their own chats, to adopt this framework; they point to
`framework.md`. Nothing in the Glossa templates binds them.

## 3. The templates and how the census was built

Each template follows one schema: eight domains in fixed order;
one axiom per numbered line, `ID (kind) — statement. Source:
named source`, with the UNSOURCED flag in place of a source only
on (H) lines. Period frames: Indus, the mature Harappan world
and its external contacts, c. 2600–1900 BCE and the centuries
around it; Eteocypriot, Iron Age Cyprus of the city-kingdoms;
Meroitic, the Kingdom of Kush in its Napatan-to-Meroitic span as
the texts require.

Census method: the program's own records first (the 2026-11-25
gap analysis; the Spec 096 and Spec 097 scope records), then
scholarly sources opened for the purpose, each axiom citing a
source actually opened. Where a source could not be opened in
full (Rilly 2010 and Rilly & de Voogt 2012, purchase-gated — the
access gap Spec 102 already names), its content is cited only as
summarised in opened sources, and the census says so. Counts as
filed, verified mechanically at registration (TC-106-02):

| Template | Axioms | (F) | (K) | (H) | Lines mentioning UNSOURCED |
|---|---|---|---|---|---|
| Indus | 88 | 4 | 74 | 10 | 0 |
| Eteocypriot | 71 | 3 | 58 | 10 | 3 |
| Meroitic | 76 | 4 | 62 | 10 | 2 |

Of the UNSOURCED mentions, the lines whose sourcing is the flag
itself (no source named, (H) only) are: Eteocypriot 2
(ETE-DNA-05, ETE-CON-14), Meroitic 1 (MER-DNA-08). The remaining
mentions (ETE-MOV-09, MER-ECO-10) are (H) lines with named
sources that flag a part of their own statement as unsourced in
the opened record.

Thin domains, stated plainly in the templates themselves: DNA
for Meroitic (no published Meroitic-period genome-wide ancient
DNA exists in the opened record; the domain censuses the gap and
one Christian-period Nubian study at its own resolution); DNA for
Eteocypriot (no published Iron Age Cypriot ancient DNA in the
opened record); Meroitic weights, measures, and prices; Indus
internal people movement; fine-resolution Iron Age Cypriot
climate.

## 4. Decisions

- **D-106-1 (number).** At the check of 2026-11-25 the highest
  landed spec on origin/main was 104, with 105 in flight in its
  own worker's branch (`spec-105-elsewhere-sandbox`, package
  `specs/105-elsewhere-sandbox/`). No 106 directory or branch
  existed. This package takes 106.
- **D-106-2 (taxonomy).** Spec 106 sits under Program
  infrastructure / Governance, lifecycle & generated layers,
  with Spec 104: it is program method, not a language study.
- **D-106-3 (no recommendations-ledger row).** The study's
  provenance is the owner's direct orders, not a Co-scientist
  recommendation; as with Spec 104 (D-104-4), no row is added.
- **D-106-4 (framework home).** The framework specification
  lives in this package as `framework.md` so that adoptions
  point at a versioned record in the repo; the standalone
  program copy in the goal workspace is a copy, and the repo
  text governs.
- **D-106-5 (Spec 105 untouched).** Spec 105's package is a
  separate worker's in-flight work. This spec references it
  (Domain 1 of every template) and does not edit it. If
  Spec 105's registration lands after this one, nothing here
  changes; the reference is by package path as filed by that
  worker.

## 5. Stages

- **Stage 0 — Registration (this landing).** The framework
  specification, the three templates with their seed records,
  the opened log, the claims intake, and the mechanical audits
  of TC-106-02..TC-106-05.
- **Stage 1 — First ensembles (NOT commissioned).** Spawning
  instances from a template and testing a claim queue is a
  later stage under its own commission, run under the
  framework's protocols and logged in the adopting study's log.
  Nothing in this registration pre-authorizes it.

## 6. Standing

No anchor standing, claim verdict, or tally in any program
changes by anything this study files. No instance result exists.
The templates' (H) axioms are declared hypotheses of future
instances, not program positions; the census's (K) axioms are
the cited scholarship's positions, at the resolution cited.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
