# External Replay of the Spec 097 Benchmark Claims — OD-C-4 Commissioned (Spec 097)

**Date:** 2026-11-23. **Program:** Spec 097 — Meroitic
Reproduction Benchmark. **Authority:** owner decision
OD-C-4 of the Co-scientist Round C assessment
adjudication
(`specs/091-anchor-comparison-integrity/records/coscientist-release-round-c-assessment-adjudication-2026-11-23.md`,
unit C-M-23, §5 OD-C-4), **decided and commissioned by
the owner, Tristen Pierson, on 2026-11-23 at ~08:28 ET**.
This record files the commission, the replay protocol in
outline, the custody scoping the replay is built under,
and the candidate routes proposed for the owner's word.
**It changes no verdict, no tally and no custody
posture, and it sends nothing:** the hand-off is
prepared, no candidate has been contacted, and engaging
a replayer remains the owner's separate act naming the
person and the destination.

## 1. What was commissioned

Co-scientist Round C recommendation C-M-23 (Meroitic
rank 3): obtain an external replay of the published
benchmark claims — an independent reproducer running the
count procedures and alignment summary from an immutable
package, with its own lawful access to required inputs,
including the bases behind "exact" (especially A1) and
the reproduced 662-text pipeline result. The
assessment's overall verdict gave the benchmark
moderate, claim-specific weight **pending independent
replay**; this commission is the act that seeks it.

## 2. The hand-off

The full hand-off package is filed at the goal's
`hidden_files/od-c4-replay-handoff-2026-11-23/`
(cover SHA-256 `c16dc8cb…`; protocol `fc6b8156…`;
custody scoping `2d6c5fe2…`; candidates `dc6de807…`).
In outline:

- **Claims under test, four groups.** R-A: the Leg A
  census — the ten counts A1–A10 and the seven Table 2
  dictionary sizes, on the frozen counting bases, with
  the bases behind "exact" expressly in scope and A1's
  distinct-headword basis named first. R-B: the
  662 distinct-texts reproduction, stage by stage
  (pools 178/11; 2,168 skeletons; 1,019 collapsed;
  662 texts / 18,075 tokens final; copy-count sum
  18,090). R-C: the Stage 4.2 outcomes — R1 and R2
  vocabulary S and permutation p against their
  registered bars, the R1 formative leg, the R2
  phonotactic leg — the verdict under test being the
  bar application that yields UNDECIDABLE AT THIS
  POWER. R-D: the Stage 4.4 held-out scores for the
  six candidates against their frozen predictions, and
  the anchor-control behaviour; the PARTIALLY
  SUPPORTED label itself is a judgment and is not
  under replay. Legs B and C are outside this
  commission.
- **Assembly, not transfer.** The replayer assembles
  the working package from public sources: this
  repository at a pinned commit, the program's own code
  (`pipeline-v2.py`, identity by its filed SHA-256
  `74b831da…`), the benchmark paper, the Kovetsky
  corpus and ASJP lists under their licences, and the
  Otten corpus acquired by the replayer directly from
  the authors' public repository at pin `c9158f68…`,
  verified against the step-0 pin manifest (§3).
- **Sealing.** The program's reproduced values are
  withheld from the working extract; the replayer files
  first, and comparison runs against the filed records.
  The seal is procedural and unverifiable by
  construction, and the protocol carries that sentence
  with the replay's weight, in freeze v2 §6's terms.
- **Tracks.** Track A, re-execution of the program's
  code, is the commissioned minimum; Track B,
  independent reimplementation from the freeze texts,
  is preferred for R-A and R-C where capacity allows.
  The report states the track per group.
- **Comparison rules.** Counts: exact integer equality
  is CONFIRMED; any other value DISCREPANT, both values
  and the basis reported; a count that cannot be
  administered is NOT REPLAYABLE with its cause. R-C:
  S exact; p exact under Track A with the registered
  seed, and under Track B on the same side of the bar
  within ±0.005; phonotactic rates within ±0.001 on
  identical denominators. R-A classifications are
  independently re-derived per count, and a
  classification disagreement on an agreeing number is
  reported as a basis dispute.
- **The return.** A per-claim table, a methods note, the
  sealing declaration, and a coverage statement. The
  program files the report unedited and adjudicates it
  on the record, whatever its outcome.

## 3. Custody scoping — the reconciliation

Reconciled against the F-6 restatement
(`records/citation-gloss-addendum-2026-11-22.md` §4),
the OD-14 programme (§§1–2, 5), and the OD-19 packet's
own terms. The full scoping is §2 of the hand-off
package; its verdict:

- **May be shared:** everything already public in this
  repository (all Spec 097 records, including the filed
  results JSONs — the aggregate statistics F-6 permits
  publishing); the program's own code, `pipeline-v2.py`
  included; the licensed public corpora (Kovetsky, MIT /
  CC BY 4.0; ASJP, CC BY 4.0) taken from their sources;
  pins, hashes, and the OD-19 manifest record as the
  package index. Structurally: 40 of the packet's 43
  items are verbatim copies of public repository files,
  and the remaining three are the program's own code and
  executed outputs whose filed counterparts are the
  versions of record. Nothing the replay needs exists
  only inside the packet.
- **May not be shared:** the Otten corpus bytes in any
  form (custody copy, working copies, run scratch) and
  Otten-derived text in any form, the 932 example
  phrases as text included — F-6 sharing is paused and
  derived artifacts are aggregate-only; and the OD-19
  packet as a bundle, which its own terms keep on the
  custody host and which the replay does not need.
- **The form that follows:** the program sends an index
  and a protocol, not data. R-A, R-B, and R-D are fully
  replayable in that form; R-C is replayable in full by
  a replayer who acquires the per-scholar files from the
  same public repository, and to the filed aggregates
  (arithmetic and bar application) by one who does not.
  The hand-off discloses the corpus's licensing state —
  no licence, permission requested 2026-11-20 and
  unanswered, held under owner risk-acceptance — in the
  same paragraph as the pointer, so the replayer's own
  lawful-access judgment is informed.
- **Stated plainly:** a replay of the form "the program
  ships its corpus copy" is barred while sharing is
  paused; nothing in this commission requires it, and
  lifting that bar is the OD-14 clarification
  programme's business, not this record's. If a refusal
  lands before or during the replay, OD-14 §4 governs
  and the Otten-dependent groups stop with everything
  else.

## 4. Candidates — proposed, awaiting the owner's word

Full entries, with approach routes and caveats, are §3
of the hand-off package.

1. **CODECHECK** (codecheck.org.uk; led by Stephen
   Eglen, University of Cambridge, with Daniel Nüst,
   University of Münster) — independent re-execution is
   its entire function; a community codechecker issues a
   public certificate of reproducible computation.
   Structurally the most independent route; covers
   Track A, not Track B.
2. **Alex de Voogt** (Drew University; co-author with
   Claude Rilly of *The Meroitic Language and Writing
   System*, 2012) — the domain checker for the count
   bases, A1 first. Two caveats on the face of the
   proposal: he declined the OD-11 Spec 096 check on
   2026-11-22, and as a program correspondent he is
   independent of the benchmark's authorship but not at
   arm's length from the program.
3. **ReScience C** (rescience.github.io) — the
   replication journal; Track B is its house form. Not a
   commission the program can place: the journal bars
   replicating or suggesting one's own work, so the
   route is an independent replicator authoring the
   submission, with this hand-off made available.

Excluded on the record: Otten and Anastasopoulos (the
claims' authors, and the custody rights holders);
Rilly (the pending Stage 4.5 respondent — no second,
conflated channel while his reply is awaited); the
Academia Co-scientist (the recommender of this act, not
an external replayer of record).

## 5. State after this record

OD-C-4 stands **decided and commissioned**; the hand-off
is prepared; custody scoping as §3; candidates proposed
and awaiting the owner's word on whom. The ledger row
C-M-23 moves open → accepted with this filing (accepted,
in the ledger's vocabulary: decided by the owner, the
execution it calls for recorded but not itself
complete). No packet or corpus material moved; no
external contact was made; no standing, verdict, or
tally in any program changed.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
