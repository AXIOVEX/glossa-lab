# Spec 106 — Registration Record (2026-11-25)

**Commission.** The owner's orders of **2026-11-25** in the
Glossa-Lab chat: 12:39 ET (ELSEWHERE expanded — claims made
outside an instance and tested inside it; multiple instances;
whole-world modeling across geography, politics, people
movement, DNA, and the other bearing domains; a baseline
ELSEWHERE template per language program) and 12:44 ET
(ELSEWHERE made a formal framework, program-agnostic, with its
mechanics and history documented). A further expansion arrived
during registration, 12:51 ET, and was folded in before
landing: the provenance standard generalises into a **history
ledger standard for every study** (framework §10 — every study
carries a history ledger as a first-class record, opened at
registration and written as the work happens; the separation
rule, that papers and reports present results and cite the
ledger rather than retelling the story; and the BACKFILLED
marking rule, with gaps marked as gaps). The act commissions
registration of the framework and the templates only; instance
spawning is a later stage and is not commissioned (spec.md §5).

- **Number decision (D-106-1).** At the check of 2026-11-25
  the highest landed spec package on origin/main was 104
  (`specs/104-quantum-alignment-benchmark/`); 105 was in
  flight in a parallel worker's branch
  (`spec-105-elsewhere-sandbox`); no 106 directory or branch
  existed. This package takes 106. The branch was cut from
  origin/main `6a10019e` (the PR #735 merge, the Spec 104
  execution landing).

## 1. What was registered

`specs/106-elsewhere-world-model-templates/` — framework.md
(the ELSEWHERE Framework Specification, Version 1: definitions
of all moving parts, the seeding protocol, the iteration
protocol, the solution criterion with its exact status
vocabulary, the provenance standard, and the history-ledger
standard of §10), spec.md, claims.md, aee-claims.json,
plan.md, tasks.md, test-cases.md (TC-106-01..TC-106-06),
templates/ (three baseline templates, each carrying its seed
record in the framework §4 format), records/
(elsewhere-seed-and-iteration-log.md, opened with the seed
entry; census-audit.py and its filed output; this record; the
AEE assessment).

**The censuses as filed** (TC-106-02 audit, zero violations):
Indus 88 axioms ((F) 4, (K) 74, (H) 10; UNSOURCED-flag lines
0); Eteocypriot 71 ((F) 3, (K) 58, (H) 10; UNSOURCED-mention
lines 3, of which 2 are flag-sourced (H) lines, ETE-DNA-05 and
ETE-CON-14); Meroitic 76 ((F) 4, (K) 62, (H) 10;
UNSOURCED-mention lines 2, of which 1 is a flag-sourced (H)
line, MER-DNA-08). Total 235 axioms in domains 2–8, plus
Domain 1 by reference to Spec 105 in each template. Built from
the program's records first (gap analysis 2026-11-25; Spec 096
and Spec 097 scope records), then scholarly sources opened in
three research passes on 2026-11-25, each axiom citing its
opened source; search-result-depth readings are labeled as
such at the citation, and Rilly 2010 / Rilly & de Voogt 2012,
which could not be opened in full, are cited only as
summarised in opened sources (the Meroitic template's source
note discloses this). Two Meroitic (F) lines resting on
reference-grade sourcing (MER-GEO-01, MER-GEO-02) are flagged
in the template itself as demotion candidates at first
amendment. Thin domains are stated plainly in the templates:
DNA for Meroitic and for Eteocypriot, Meroitic weights and
measures, Indus internal movement, fine-resolution Iron Age
Cypriot climate.

**Seed records** (TC-106-05, verified by recomputation): each
template's seed record states the framework §4 fields and the
axiom-line SHA-256 of its census as filed — Indus
`eb0e1d6218fadf8eed06c78eeb92979163ebb37b1206eb3d151c9c0d23b501e6`,
Eteocypriot
`fca1cc8a238631b0c6df8b2901daa5e84dc4cb2387dcdad560285c6e95beec4f`,
Meroitic
`eeadf46e336fa80d09bcffa2538d3cf4c32c8756fdb6150c817ff0b19cdb4cf4`.

**Test cases at registration.** TC-106-01 PASS (claim ids and
order equal in claims.md and aee-claims.json; every claim
carries a falsifier and a does-not-establish line).
TC-106-02..TC-106-05 PASS in one audit run
(`records/census-audit-output-2026-11-25.txt`: zero
violations; all stated counts and hashes recompute).
TC-106-06 is the landing audit, §4 below.

## 2. The AEE outcome at registration

`records/aee-assessment-2026-11-25.json` — run_aee.py assess
--phase after_plan (aee 1.5.3) over the bundle's
aee-claims.json: outcome **iterate**; 6 claims assessed, all 6
draft-capped below the 0.70 confidence threshold — the
expected shape for draft claims at registration, the same
shape Specs 101–104 returned. The assessment's own ledger
entries were written by the tool under
`.specify/extensions/aee/` and are carried in this landing.
(Venue note: the tower's relocated `glossa-ci` venv's console
scripts carry stale shebangs from the 2026-11-23 home cleanup,
so the assessment ran through a PATH shim invoking the venv's
interpreter directly, as for Spec 104.)

## 3. Registration cascade (executed figures)

- Taxonomy: Spec 106 added to the program-map taxonomy under
  Program infrastructure / Governance, lifecycle & generated
  layers (decision D-106-2); studies 105 → 106; the Program
  infrastructure domain census 26 → 27.
- Intake: the bundle's 6 claims appended through
  tools/ledger/import_bundle.py, dated 2026-11-25 (6 appended,
  0 already canonical). Ledger 1,080 → 1,086 lines; claims
  1,049 → 1,055; canonical SHA-256
  `0a086ecd91e816584346e6f400fc050e9c80e687b510764b14856c5f1043ffc3`
  → `00d9b5e9ecdc54bf5f5e5f7ce755ae91504202d1be52eb8a63ec3c0c242b8822`.
  verify-canonicals over the grown build, before any pin
  moved: **6/6 PASS**.
- Settling layer: both T405 scenarios re-executed over the
  grown build (runs `settling-20261125T174854Z-15a33b`
  incumbent, `settling-20261125T174854Z-99f82a` full-register,
  same 286-sign full-frame scope, same registered scenario
  ids); both result blocks byte-equal to the superseded
  generation's, verified by direct comparison of the stored
  records, and the pair's input pins identical to the
  superseded generation's except the ledger pin itself. The
  Stage 4 dual-run comparison re-filed from the new pair (its
  diff against the previous filing is the ledger pin only;
  its result block byte-equal, verified). Assignment sets
  re-materialized unchanged (run
  `settling-20261125T174905Z-768fea`; incumbent 94,
  full-register 286, H003 out of frame). The canonical pin
  refreshed as re_derivations[21] of settling-canonical.json.
  The superseded generation
  (settling-20261125T143521Z-6c100f,
  settling-20261125T143521Z-0b89c3,
  settling-20261125T143602Z-d9ba61) departed the run store in
  this landing; their departure acts are appended to the run
  index in the landing's completion commit, naming the
  registration commit as `superseded_by_commit` and each
  record's blob hash from the pre-landing tree.
- Generated layers, regenerated in dependency order: matrix
  1,578 cells (supports 1,571, opposes 7) over 1,055 rows;
  map-data 1,699 elements, 1,578 edges, settling runs carried
  2; program map: 1,055 claims, 106 studies. Falsifier census
  1,046 of 1,055 claims, the same 9 gaps.
- Census pins updated from the regenerated actuals in
  test_program_map_conformance.py (including the Program
  infrastructure domain census 26 → 27),
  test_spec086_ledger_gate.py, test_spec086_map.py,
  test_spec095_stage4_instantiation.py,
  test_spec095_t403_dashboard.py (including the T405 run of
  record, re-pinned to settling-20261125T174854Z-15a33b,
  whose quantities are the superseded generation's,
  byte-equal), and the frontend e2e census texts
  (frontend/e2e/system-graph.spec.ts,
  frontend/e2e/researcher-dashboard.spec.ts): claims
  1,049 → 1,055; bundle population 1,026 → 1,032; open class
  1,040 → 1,046; falsifier-present 1,040 → 1,046; draft
  status 1,025 → 1,031; ledger lines 1,080 → 1,086; studies
  105 → 106; matrix cells and map edges 1,572 → 1,578; map
  elements 1,693 → 1,699; supports edges 1,565 → 1,571;
  claims untouched by any run 1,048 → 1,054.
- Recommendations ledger: no row added (D-106-3 — the study's
  provenance is the owner's direct orders, not a Co-scientist
  recommendation).

## 4. Standing

Spec 106 is REGISTERED. It spawns no instance, tests no
claim inside any instance, and moves no standing, verdict, or
tally (C106-6; TC-106-06: the landing diff is confined to
this package, the C106 claims' intake artifacts, the
taxonomy, the regenerated layers, the settling records of the
cascade, and the census pins they require). Stage 1 (first
ensembles) is not commissioned.

**Venue.** All work for this package ran on tower-compute in
the fresh clone `~/.syncyard/worktrees/glossa/spec106-reg`
(branch `spec-106-elsewhere-world-model-templates`). Nothing
ran in the coordination VM except the census research passes'
source reading and the package's drafting, which compute
nothing against program data.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.

## Completion pass (2026-11-25, same landing)

- **Departure acts appended.** The three superseded settling
  records named in §3 departed the run store in this landing;
  their departure acts were appended to the run index through
  `run_records.append_act` in this completion commit, naming
  the registration commit
  `30224293548478963adc1dbfda7e29fbd80bf48c` as
  `superseded_by_commit` and each record's blob hash from the
  pre-landing tree, as §3 anticipated. The run-index
  completion pass (build_legacy_index.py) entered the legacy
  event for re_derivations[21] and named the departed records
  post-spec skips (folded census 89 entries).
