# History ledger — Spec 106

Study: Spec 106 — The ELSEWHERE Framework: Formal Specification, Baseline World-Model Templates, and the Axiom Census

**Opened 2026-11-25 at the Round F landing.** Spec 106 registered before the history-ledger backfill of the same day inventoried the program's studies, and its package carried the framework's own seed-and-iteration log (the ELSEWHERE form of the ledger, at `records/elsewhere-seed-and-iteration-log.md`) but no history ledger; the Round E landing amended the framework without opening one, and this file repairs that. Entries through the Round E clarification are **BACKFILLED 2026-11-25** from the filed records named at each entry, under the history-ledger convention of 2026-11-25 and section 10 of the framework specification itself. Where the filed record is silent, the entry marks a GAP rather than filling it. From the Round F entry on, entries are written as the work happens. This ledger narrates the study; it changes no result, verdict, or standing.

## Entries

### 2026-11-25 — COMMISSION

**Kind:** COMMISSION. **Actor:** the owner (Tristen Pierson), Glossa-Lab chat, 2026-11-25.

The owner commissioned ELSEWHERE as the program's alternative route after declining Spec 104's quantum arm, corrected the framing at 12:39 ET (claims are made outside an instance and tested inside it; multiple instances are spawned to explore and brute force ideas by varying declared hypothesis axioms; an instance models what we know about the world at the time, across language, geography, politics, people movement, DNA, material economy, environment and chronology, and language contact; evidence stays outside as the fixed checker), and at 12:44 ET ordered ELSEWHERE made a formal framework with visible mechanics and a seed-and-iteration provenance log for every study, the same formalization for the RCPH/Ladder Ring Theory and Riemann works, and ELSEWHERE assessed as a core component for VEXA. A further expansion arrived during registration, 12:51 ET, and was folded in before landing: the provenance standard generalises into a history-ledger standard for every study (framework §10).

**Rests on:** `records/registration-2026-11-25.md`; the owner's orders as recorded in the program record (goal workspace PROGRAM-STATE, 2026-11-25).

### 2026-11-25 — DECISION (registration landed, with the Spec 105 reconciliation)

**Kind:** DECISION. **Actor:** the study's registration worker, under the commission above; the reconciliation was forced by a parallel landing, not chosen.

Spec 106 registered as PR #738 and merged at `97c576658b18afe0974ffc0d3324dc93c9739243`, CI 10/10, while Spec 105's registration (PR #736) was in flight; the two cascades collided on every shared artifact and were reconciled by the Spec 105 landing, which re-executed the cascade over the combined build (claims ledger 1,060 claims, 107 studies at that point). The framework specification v1 landed with the three baseline world-model templates and their axiom census (235 axioms across the three programs, every one labeled floor fact, period knowledge, or hypothesis, with its source). No instance was spawned by the registration; the templates' claim queues opened empty, and Stage 1 (first ensembles) was not commissioned. The registration record also carries the package's number decision (D-106-1: the package takes 106; the branch was cut from origin/main `6a10019e`), its taxonomy decision (D-106-2: Program infrastructure / Governance, lifecycle & generated layers; studies 105 → 106), and D-106-3 (no recommendations-ledger row; the provenance is the owner's direct orders). The censuses as filed: Indus 88 axioms ((F) 4, (K) 74, (H) 10), Eteocypriot 71 ((F) 3, (K) 58, (H) 10), Meroitic 76 ((F) 4, (K) 62, (H) 10), each template carrying its seed record with its axiom-line SHA-256, verified by recomputation (TC-106-05); two Meroitic (F) lines (MER-GEO-01, MER-GEO-02) are flagged in the template itself as demotion candidates at first amendment. The AEE assessment at registration returned **iterate**, all 6 claims draft-capped.

**Rests on:** `records/registration-2026-11-25.md`; `framework.md`; `records/elsewhere-seed-and-iteration-log.md` (seed entry).

### 2026-11-25 — ITERATION (framework §8.1 clarification, Round E unit E-M-3)

**Kind:** ITERATION. **Actor:** the Round E adjudication worker, under the Co-scientist loop's standing discipline.

The Round E Meroitic session found that the framework's §7/§8 ensemble status aggregation was not mutually exclusive (the all-UNDERIVABLE, all-UNTRANSLATABLE, and zero-survivor cases all collapsed into §7's "dead" outcome mapped to REFUTED-IN-ENSEMBLE). Sustained APPLY at adjudication, a dated clarification was appended at framework §8.1 registering a mutually exclusive aggregation table, before any scored instance had run. No result was affected. Landed as PR #741.

**Rests on:** `framework.md` §8.1; `specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-25.md` §3.3.

### 2026-11-25 — ITERATION (framework §8.2 clarification, Round F unit F-M-1)

**Kind:** ITERATION. **Actor:** the Round F adjudication worker, under the Co-scientist loop's standing discipline.

The Round F Meroitic session flagged the one case §8.1's table did not address: its positive row awarded ROBUST-IN-ENSEMBLE when every translatable survivor derived a claim even if another surviving instance was UNTRANSLATABLE for it, turning partial translation coverage into full-ensemble support (two-instance counterexample: A derives under H; B, the declared alternative, survives but cannot translate the claim). Sustained APPLY at adjudication against the filed text, with the session's kill check run and not met; a dated clarification was appended at framework §8.2 governing the positive row's reading (full translation coverage required for ROBUST-IN-ENSEMBLE; mixed coverage logged with both denominators; subset results reportable only as explicitly scoped subset results). Row E-M-3 was annotated, not reopened; its three repaired cases stand closed. No instance has been spawned under this study at any point, so no result is affected. Stage 1 (first ensembles) remains uncommissioned.

**Rests on:** `framework.md` §8.2; `specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-25-round-f.md` §3.1.

### 2026-11-25 — CORRECTION (duplicate opening of this ledger, unioned)

**Kind:** CORRECTION. **Actor:** the Spec 103 conformance addendum worker, at that landing's rebase.

This ledger was opened twice on 2026-11-25: at the Round F landing (PR #744, the version that reached main) and, independently and in parallel, in the Spec 103 conformance addendum branch, which had been cut before the Round F landing and whose own scope included closing this gap. When the addendum branch was rebased onto the Round F merge, the two openings collided (both-added). The landed version governs as the base; the addendum version's additional registration detail (the 12:51 ET expansion, decisions D-106-1..D-106-3, the per-program census figures, and the demotion-candidate flags) was folded into the COMMISSION and DECISION entries above at the rebase, and nothing in either version was contradicted by the other. The addendum version's §8.1 entry is the ITERATION entry above in the landed version's form. No result, verdict, or standing is affected; the collision is recorded here rather than smoothed over, per the convention this ledger follows.

**Rests on:** the rebase record of PR #743 (Spec 103 conformance addendum); `records/registration-2026-11-25.md`.
