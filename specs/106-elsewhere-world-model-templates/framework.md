# ELSEWHERE — Framework Specification

**Version 1, 2026-11-25. A program-agnostic framework for testing
claims about worlds that cannot be observed directly. Commissioned
by Tristen Pierson in the Glossa-Lab chat, 2026-11-25 (12:39 ET,
framing; 12:44 ET, the order that ELSEWHERE be made a formal
framework). Registered for Glossa-Lab as Spec 106
(`specs/106-elsewhere-world-model-templates/` in AXIOVEX/glossa-lab),
which carries this specification as `framework.md` and the first
three baseline templates built under it. This document is the
reference text: other programs adopt ELSEWHERE by pointing to it,
unchanged.**

---

## 1. Purpose

ELSEWHERE tests claims. A claim about an unobservable world (a dead
language's society, a conjectured physical structure, a system's
behaviour under conditions that cannot be run) cannot be checked
against the world itself. It can be checked against *declared
models* of the world, built from premises that are written down,
labeled by how well they are known, and scored against fixed
evidence. ELSEWHERE is the discipline that keeps that checking
honest: every premise labeled, every model rebuildable from its
record, every verdict reported with the premises it depends on,
and the word *solution* reserved for claims that earn it under
§8.

The framework has two levels. **The reasoning level** is where
people state claims, choose what to vary, and read results.
**The instance level** is where models derive. Nothing crosses
from the instance level to the reasoning level except verdicts in
the form §7 prescribes, and nothing crosses down except claims and
declared axiom sets.

## 2. Definitions

Each term below is a moving part of the framework. A study that
uses a term in another sense is not using this framework.

- **Baseline template.** A program's declared starting axiom set
  for one subject world, organised in domains under a schema the
  program registers. The baseline is the common ancestor of a
  program's instances. It is never itself an instance and is never
  scored.
- **Axiom.** One content line of a template or an instance. An
  axiom is a single statement, numbered, carrying exactly one
  **kind label** and either a named source or the UNSOURCED flag.
- **Kind labels.** **(F)** floor fact: known without a doubt, where
  doubting it means doubting the record itself rather than an
  interpretation of it. **(K)** period knowledge: well supported by
  the record but revisable, source named. **(H)** hypothesis:
  declared openly as contested or unknown. An axiom flagged
  UNSOURCED may appear only as an (H); it names a variable, never a
  usable premise.
- **Instance.** A closed model world: one declared axiom set,
  the derivations it supports, and a queue of claims tested in it.
  An instance has no access to anything outside its axiom set
  except the checker (§6) at registered contact points.
- **Seed.** The act and record that bring an instance lineage into
  existence from a baseline template: the template version, the
  axiom set as seeded, the claim queue as opened, the date, and
  the authorizing order. Specified in §4.
- **Claim.** A statement at the reasoning level, in plain language,
  that a person can argue with, entered into a study's claim queue
  by an authorizing act at that level. Instances never originate
  claims.
- **Translation.** The rendering of a claim into an instance's
  derived terms so it can be derived or refuted inside. A claim
  that cannot be translated into an instance is returned
  UNTRANSLATABLE for that instance, which is a recorded outcome,
  not a silent skip.
- **Derivation.** A chain of steps inside an instance, each step
  citing the axioms and prior steps it uses, ending in a statement
  the instance supports. A derivation that needs a premise the
  axiom set does not contain stops and reports the gap.
- **Evidence set.** The fixed body of records a study scores
  against: corpora, excavation records, published data, the
  adopting program's fixed record. The evidence set is declared at
  registration and is not an axiom of any instance.
- **Checker.** The scoring of an instance's derivations against
  the evidence set at registered **contact points**. The checker
  returns agreement or contradiction per contact point. It does
  not return interpretations.
- **Verdict.** The recorded outcome for one claim in one instance:
  DERIVES, DOES-NOT-DERIVE, UNDERIVABLE (the axiom set does not
  settle it), or UNTRANSLATABLE, each with the derivation or the
  gap that produced it. Verdicts are always cited with the instance
  and its axiom set.
- **Ensemble.** The set of sibling instances spawned from one
  baseline to test one claim queue, differing systematically in
  their (H) axioms (and, in declared sensitivity runs, in named
  (K) axioms). The ensemble, not any instance, is the instrument.
- **Iteration.** One full pass of the lifecycle (§5) over an
  ensemble: declare, derive, test, score, retire or amend. Each
  iteration is one entry in the study's provenance log (§9).
- **Retirement.** The closing of an instance, with its record
  kept. An instance is retired when it dies (§6), when its claim
  queue is exhausted, or when the reasoning level supersedes it.
  Retired instances are never edited and never deleted.
- **Solution.** The reserved status of §8. Nothing else in the
  framework is called a solution.

## 3. Axiom discipline

1. Every content line of a template or instance is an axiom with a
   kind label. Unlabeled content does not enter an instance.
2. An assumption enters only as a labeled axiom of specific
   instances. It is never written into a derivation step, a
   dataset, a translation, or a checker. This is the framework's
   no-smuggling rule.
3. For every live hypothesis a program holds, some instance
   carries it as an (H), and siblings carry its alternatives or
   its negation. A hypothesis carried by every instance is a
   premise of the study, and must be promoted to (K) with its
   source or declared as a study-level assumption in the seed.
4. (F) axioms never vary inside a lineage. An "instance" that
   denies an (F) axiom is a different study's seed, not a sibling.
5. Census discipline: a baseline template is built from sources
   actually opened by its builders, program records first. A line
   whose source could not be opened is dropped or carried as (H)
   UNSOURCED.

## 4. The seeding protocol

A study begins with a seed. The seed record contains exactly:

1. **Study identity.** Program, study name, registration reference
   (for Glossa-Lab, the spec number), and the framework version
   adopted (this document, Version 1).
2. **Baseline template.** The template's identity and version, its
   file or record location, and its axiom census as seeded: counts
   by domain and by kind, the count of UNSOURCED flags, and a
   SHA-256 hash over the axiom lines as filed, so the seeded set
   can be verified byte-for-byte later.
3. **The full axiom set as seeded.** The template itself, carried
   or incorporated by an exact reference that resolves to the
   hashed content. A reference that can drift (a living document,
   an unpinned page) does not satisfy this field.
4. **The claim queue as opened.** The claims the study opens with,
   verbatim, or the explicit statement that the queue opens empty
   and the rule by which claims may enter (an authorizing act at
   the reasoning level, recorded in the log).
5. **The evidence set.** Its identity and location, and the
   registered contact points at which instances will be scored.
6. **Date and authorizing order.** The date of the seed and the
   order that authorized it, named so the log's first entry can be
   checked against it.

An instance is **rebuildable from its seed** when fields 2–5
suffice to reconstruct its axiom set, its claim queue, and its
scoring without asking anyone anything. A study whose instances
are not rebuildable from their seeds is not running this
framework, whatever it calls itself.

## 5. The iteration protocol

One iteration is one pass through five steps, in order:

1. **Declare.** Every instance in the pass has its full axiom set
   written out before any derivation runs.
2. **Derive.** Derivations are logged with their inputs.
3. **Test.** The claim queue is run: each claim translated,
   derived, refuted, or returned UNDERIVABLE or UNTRANSLATABLE.
4. **Score.** Derivations meet the evidence set at the registered
   contact points. Contradictions kill (§6).
5. **Retire or amend.** Dead instances retire with their deaths
   filed. Amendments are new instances with new declared sets;
   instances are never edited in place.

**What may change between iterations.** (H) axioms may be added,
removed, or replaced, each change declared with its reason.
Named (K) axioms may be dropped or varied in a declared
sensitivity run. The claim queue may gain claims by an authorizing
act at the reasoning level. The evidence set may grow by new
record entering the program (a new publication, a new excavation
report), and growth is logged with its source. The baseline
template may be amended, which starts a new template version and
is logged as such; instances already seeded keep the version they
were seeded from.

**What may not change.** (F) axioms. A retired instance's record.
A filed verdict. The checker results already returned. The seed.

**How variations are chosen.** At the reasoning level, and
declared before the pass runs: one hypothesis varied at a time
first, then combinations the reasoning level names. The choice of
what to vary is the study's thinking and is recorded with its
reasons in the log, so a later reader can see why the ensemble has
the shape it has.

**How verdicts accumulate.** Verdicts are appended, never
overwritten, in a per-claim table across instances and iterations.
A claim's current status (§8) is computed from the whole table,
never from the latest pass alone.

## 6. Evidence and the checker

Evidence is not an axiom. No instance assumes the evidence away,
selects the part of it that suits its axioms, or treats a checker
item as derivable. An axiom set that derives a contradiction with
the evidence at a contact point **dies**: the instance retires,
and the death is filed with the contradicting derivation and the
evidence item it struck. Contradiction detection is a result, not
an error; a study that never kills an instance is not testing
anything. Where an adopting program already has boundary gates
(registered tests a result must pass to enter the program's
record), those gates are contact points of the checker, named in
the seed.

## 7. Reading an ensemble

For one claim, across the surviving instances of an ensemble:

- **Robust in the ensemble.** The claim derives in every surviving
  instance. It depends on no contested premise in the varied set.
- **Axiom-tracking.** The claim derives exactly in the instances
  carrying a named axiom or combination, and fails in their
  siblings. The ensemble has identified the premise the claim
  rides on; the study's next move is to hunt real-world evidence
  about that premise.
- **Dead.** The claim derives in no surviving instance, or every
  instance deriving it has died. The claim retires at the
  reasoning level, with the ensemble as the record of why.

Brute force is legitimate in this framework in exactly the sense
of §5's declared variation: the hypothesis space is declared in
advance, the test is fixed, the failures are kept. Exhausting a
declared space against fixed evidence is a search; varying
undeclared premises until something fits is not, and is
prohibited by §3 rule 2.

## 8. The solution criterion and the status vocabulary

A claim may be called a **SOLUTION** only when all three hold:

1. It derives in every surviving instance of the ensemble spawned
   to test it, across the full declared variation of the relevant
   (H) axioms (robust in the ensemble, §7); and
2. No surviving instance contradicts it at any contact point; and
3. It has passed the adopting program's ordinary boundary gates:
   the registered evidentiary route by which that program admits
   any result into its record (for Glossa-Lab, Spec 105's boundary
   gates and the registered-study discipline).

Anything less carries its exact status label, and reports use the
label, not the word solution:

- **ROBUST-IN-ENSEMBLE** — conditions 1 and 2 hold; the boundary
  gates have not (yet) admitted it.
- **AXIOM-TRACKING (names the axiom set)** — §7's tracking
  outcome; the label names the premise it rides on.
- **UNDERIVABLE** — the tested axiom sets do not settle it.
- **REFUTED-IN-ENSEMBLE** — §7's dead outcome.
- **UNTESTED** — in a queue, not yet run, or run in no surviving
  instance.

A derivation inside an instance is valid relative to its axioms
and is never reported as a fact about the real world. Program
standings, verdicts, and tallies in the adopting program are
untouched by ensemble results until condition 3 is met through
that program's own route.

### 8.1 Aggregation precedence (clarification, Round E adjudication, 2026-11-25)

Section 7's three readings and the status vocabulary above
do not by themselves make the ensemble statuses mutually
exclusive: an ensemble in which no surviving instance
derives a claim satisfies §7's "dead" wording whether the
survivors returned UNDERIVABLE, UNTRANSLATABLE, or an
explicit negation. This clarification, appended 2026-11-25
under the Round E adjudication
(`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-25.md`,
unit E-M-3) and registered before any scored instance has
run, governs the reading of §§7–8. For one claim, tally the
surviving instances' outcomes first, then apply exactly one
row:

- **No surviving instance** → no ensemble status is
  returned. The ensemble is recorded as model exhaustion;
  exhaustion is not refutation, and the claim remains
  UNTESTED.
- **Every surviving instance UNTRANSLATABLE** → a coverage
  failure, recorded as such in the iteration log. No status
  is returned.
- **At least one survivor, and every translatable survivor
  derives the claim** → ROBUST-IN-ENSEMBLE (the SOLUTION
  gates of §8 then apply as written).
- **At least one survivor derives the claim and at least
  one does not, and a named axiom or combination
  discriminates the split exactly** → AXIOM-TRACKING,
  naming that axiom set.
- **No survivor derives the claim, and at least one
  survivor derives its negation** → REFUTED-IN-ENSEMBLE.
  Section 7's "dead" is read through this row: a claim is
  dead only when a surviving instance kills it, never
  merely because no instance derived it.
- **No survivor derives the claim or its negation** (the
  translatable survivors are UNDERIVABLE), **or a mixed
  split that no named axiom set discriminates exactly** →
  UNDERIVABLE, with the split tallied in the iteration log.

A positive or negative ensemble status therefore always
requires at least one surviving instance and derivation
coverage of the claim or its negation. The original text
of §§7–8 stands; this subsection governs its reading.

## 9. The provenance standard: the seed-and-iteration log

Every ELSEWHERE study keeps a **seed-and-iteration log** as a
first-class record, in its own record home, named at registration.
The log contains:

1. **The seed entry** — the seed record of §4, verbatim and
   complete.
2. **One entry per iteration**, each recording: the iteration's
   date and authorizing act; what changed and why (axioms varied,
   added, or removed; claims entering the queue; evidence-set
   growth; template amendments); which instances were spawned,
   with their declared axiom-set differences from the baseline;
   which instances were retired and why (including deaths, with
   the contradicting evidence item); the verdicts returned, per
   claim per instance; and the evidence applied at each contact
   point.
3. **The solution register** — every claim that reaches SOLUTION
   status under §8, with the date, the ensemble it survived, and
   the boundary-gate record that admitted it; and every claim
   whose status changed, with its old and new labels.

The test of the log is reconstruction: the whole path from seed to
any claim's current status must be rebuildable from the log alone,
without the memory of anyone who ran it. A study that cannot pass
that test has a record-keeping defect, filed as such, whatever its
results.

The seed-and-iteration log is the ELSEWHERE-specific form of the
history ledger (§10): for an ELSEWHERE study, this log is where
the study's story lives, and it satisfies §10 when it also carries
§10's general entry kinds (decisions, failures and corrections,
and the closing state) alongside its iteration entries.

**Where each adopting program keeps its log** is named in that
program's adoption record. For Glossa-Lab: the log lives in the
adopting study's spec package under `records/`, named
`elsewhere-seed-and-iteration-log.md`; Spec 106's own log is the
first, and the three baseline templates it ships carry their seed
records in the format of §4 inside the template files themselves,
so a template can be lifted into a new study with its seed intact.

## 10. The history ledger standard (all studies)

The provenance discipline of §9 generalises. **Every study, not
only an ELSEWHERE study, carries a history ledger**: a first-class
record, opened at registration and written as the work happens,
that tells the entire story of how the study started, what it
did, and how it ended. Result reports and papers present results;
they are not where the story lives (§10.3). When a study is done,
its ledger is the whole story, readable without anyone's memory.

### 10.1 Location and opening

The ledger lives in the study's own record home, named at
registration. In a spec-kit program the convention is
`specs/<spec-dir>/records/history-ledger.md`. For an ELSEWHERE
study, the seed-and-iteration log of §9
(`records/elsewhere-seed-and-iteration-log.md`) is the study's
history ledger in its ELSEWHERE-specific form, provided it
carries the entry kinds of §10.2 as well as its iteration
entries. The ledger opens at registration, with the commission
entry; a study with no ledger has a record-keeping defect from
its first day, not from its last.

### 10.2 Entries

Entries are appended as the work happens, never written
retrospectively in a batch (except under §10.4). Each entry
carries: **date**; **kind**, one of COMMISSION, DECISION,
ITERATION, FAILURE, CORRECTION, VERDICT, CLOSING, GAP;
**actor or authorizing act** (who decided, under what order);
**what happened and why**; and **references** (record paths,
commit hashes, run ids, PR numbers) sufficient to check the
entry against the underlying record. The ledger must carry, at
minimum:

- the commissioning order and the starting state (COMMISSION);
- each decision and who made it (DECISION);
- each iteration, what changed, and why (ITERATION);
- failures and corrections, owned in the entry where they
  happened, not smoothed over later (FAILURE, CORRECTION);
- verdicts as they landed, in the vocabulary of the study that
  returned them (VERDICT);
- the closing state (CLOSING).

### 10.3 The separation rule

Papers and result reports present results and cite the ledger;
they do not retell the story. The story, the sequence of
decisions, failures, and corrections that produced the results,
lives in the ledger and only there. A report that narrates the
study's history instead of citing its ledger is out of form, and
a ledger that argues for results instead of recording how they
were reached is out of form in the other direction.

### 10.4 The backfill rule

A ledger assembled later, from filed records, for a study that
predates this standard is marked **BACKFILLED** in its header,
with the date of assembly and its sources named (the records it
was reconstructed from). Spans the records cannot reconstruct
are entered as GAP entries naming what is missing and why it
cannot be recovered. A backfilled ledger is never narrated over:
a gap stated plainly is a true record; a smooth story over a gap
is a false one. Backfilled ledgers are legitimate records; the
marking, not the lateness, is what the standard requires.

### 10.5 Relation to existing tracking

The adopting program's existing tracking (for Glossa-Lab, AEE's
claims ledger, the spec records, and the filed verdicts) is the
raw material the history ledger draws on. The ledger is the
narrative layer above that material: it cites the claims, runs,
and records; it does not duplicate or replace them, and where
the ledger and the underlying record disagree, the underlying
record governs and the ledger is corrected by a CORRECTION
entry.

## 11. Adoption

A program adopts ELSEWHERE by: registering the adoption in its own
record system; naming its log home (§9); building its baseline
templates under §3's census discipline, in domains its subject
requires (the eight domains of the Glossa-Lab templates are that
program's choice, not the framework's); declaring its evidence set
and contact points; and seeding its first study under §4. The
framework's definitions, protocols, status vocabulary, and
solution criterion are adopted unchanged. Programs known to be
adopting, each by its own direction in its own chat: the
RCPH / Ladder Ring Theory program, the Riemann program, and VEXA,
where ELSEWHERE is a candidate core component. Their adoptions
point to this specification; nothing in their subject matter
belongs in it, and nothing in Glossa-Lab's templates binds them.

## 12. One-page map

```
REASONING LEVEL — claims in plain language; variations chosen;
                  statuses read; evidence hunts commissioned.
        │ claims down (queue)          ▲ verdicts up (§2 form)
        ▼                              │
INSTANCES — declared axiom sets (F floor · K background · H varied)
            derivations logged; gaps reported, never filled.
        │ derivations at registered contact points
        ▼
CHECKER — the evidence set; agreement keeps, contradiction kills.
        │
        ▼
ENSEMBLE READING — robust · axiom-tracking · dead (§7)
        │
        ▼
STATUS — exact label per §8; SOLUTION only when the ensemble is
         survived AND the program's own gates admit the claim.
        │
        ▼
PROVENANCE — every step above is an entry in the seed-and-
             iteration log (§9); the path rebuilds from the log.
```

*AI disclosure: prepared by an AI agent (Muse, via Muse) at the
direction of Tristen Pierson, per standing disclosure practice.*
