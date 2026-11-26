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

### 2026-11-25 — ITERATION (Meroitic baseline template version 2, Round G unit G-M-1)

**Kind:** ITERATION. **Actor:** the Round G adjudication worker, under the Co-scientist loop's standing discipline.

The Round G Meroitic session found an input inconsistency in this study's Meroitic baseline template: MER-ENV-01 (K) confined Meroitic writing "only during the Kingdom of Meroe, c. 300 BCE – 350 CE", while the template's own MER-ENV-03 records the script outliving the kingdom (the latest known text, REM 0094 at Kalabsha, re-dated to 410/450 CE) and MER-MOV-08 calls that inscription "the last Meroitic text". Sustained APPLY at adjudication, with the session's kill check (a binding scope rule confining the axiom to a kingdom-period subset) run against the template, the framework, and the study records and not met. The template is amended to version 2 (MER-ENV-01 in the attested-and-continued form, source unchanged; census unchanged; axiom-line SHA-256 `eeadf46e…` → `ecabd227…`, recomputed by the census-audit method, TC-106-02..05 passing in full); the seed record stands as filed, the amendment is recorded in the template's Template amendment section, and Iteration 1 stands in the seed-and-iteration log. No instance has been spawned from either version, so no result is affected.

**Rests on:** `templates/meroitic-baseline.md` (Template amendment — version 2); `records/elsewhere-seed-and-iteration-log.md`, Iteration 1; `specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-25-round-g.md` §3.1.

### 2026-11-26 — DECISION (Stage 1 commissioned; first ensemble seeded)

**Kind:** DECISION. **Actor:** the owner (Tristen Pierson), Glossa-Lab chat, 2026-11-26 ~01:54 ET; executed by the Stage 1 worker under that order.

Spec 106's Stage 1 (first ensembles), uncommissioned since registration, was commissioned by the owner's order "For everything else, execute now to your recommendations", approving the recommendation as presented to him: the first ensemble on the framework's worked example, one claim, fully logged, before any wider set. The ensemble (ETE-ENS-1) is seeded from the Eteocypriot baseline template version 1 (axiom-line pin recomputed at the seeding, `fca1cc8a…`, TC-106-02..TC-106-05 PASS): the claim "The long Amathus text is a royal dedication" enters the baseline's claim queue as ETE-Q-1 (status UNTESTED at entry), and four instances are declared over the politics variation — an added commissioning-norm hypothesis in its royal (ETE-POL-H1) and civic (ETE-POL-H2) forms, a baseline control, and a declared sensitivity run dropping the named (K) axiom ETE-POL-11. The seed is filed before any derivation runs; the pass's outcome is the VERDICT entry following this one.

**Rests on:** `records/ensemble-1-seed-2026-11-26.md`; `records/elsewhere-seed-and-iteration-log.md`, Iteration 2.

### 2026-11-26 — VERDICT (ETE-ENS-1: ETE-Q-1 REFUTED-IN-ENSEMBLE)

**Kind:** VERDICT. **Actor:** the Stage 1 worker, under the commission recorded in the DECISION entry above.

The ensemble ran as seeded. In all four instances the claim did not derive — the gap is the same in each: no axiom connects ICS 196 to a royal dedicator, and the royal-norm instance's general hypothesis (ETE-POL-H1) does not distribute to a text whose filed content names the city as the honouring party — and in all four the claim's negation derived, from ETE-CON-03 with the seed's declared translation (the inscription's dedicator of record is the city of the Amathusians; its honorand is Ariston, son of Aristonax, a named private citizen). No instance contradicted the evidence set and none died; all four retired with the queue exhausted. Read under framework §8.1, ETE-Q-1 is **REFUTED-IN-ENSEMBLE**: it fails identically under the royal commissioning norm, the civic norm, the unamended baseline, and the kingship-unended sensitivity corner, so its fate does not track the politics variation at all; the load-bearing item is the filed content of the text itself. Nothing is called a solution, no anchor standing, program verdict, or tally moves, and the Eteocypriot paper is untouched. The outcome record names the next evidence that could bear: not a politics premise but the outstanding edition-of-record check on ICS 196's filed content (ETE-ENV-04).

**Rests on:** `records/ensemble-1-outcome-2026-11-26.md`; `records/elsewhere-seed-and-iteration-log.md`, Iteration 2.

### 2026-11-26 — DECISION (methods paper published, v1)

**Kind:** DECISION. **Actor:** the owner (Tristen Pierson), Glossa-Lab chat, 2026-11-26 15:49 ET (approval of the exact text and the publish order); executed the same day.

The framework's methods paper, "Elsewhere: A Framework for Testing Claims About Worlds That Cannot Be Observed, Built and Exercised on Three Undeciphered Scripts", is published as v1. Before any venue was touched, every number in the approved text was re-verified against the filed records at main head `0b377f6f` under the standing slop-check rule (gate figures, census, inventories, frequencies, the M220 positional row read from the stage-3 output, substitution partitions, role counts, positional-gate conformance, the ensemble tallies, and the three cited DOIs, each resolving); no mismatch was found and nothing in the text was altered. Zenodo first: new record 24571025, DOI 10.5281/zenodo.24571025 (concept 10.5281/zenodo.24571024), the deposited file's size and MD5 verified identical to the rendered PDF (8 pages, SHA-256 `a85e749d…`). Academia second: new work 182066190, verified live on the public profile and on its own page, which displays the Zenodo DOI. ResearchGate last and not attempted: the day's account-wide budget was spent, so the listing trails to a later day. The paper claims no decipherment and moves no standing, verdict, or tally in any program.

**Rests on:** `records/release-record-2026-11-26.md`.
