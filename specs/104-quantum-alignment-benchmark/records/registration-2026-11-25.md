# Spec 104 — Registration Record (2026-11-25)

**Commission.** The owner's order of **2026-11-25**
(Glossa-Lab chat): "do the quantum alignment benchmark
after the program doc" — the program doc being his
decipherment gap analysis of the same day, which
identified the Eteocypriot bilingual alignment as the
one well-posed quantum-testable subproblem in the
program. The act commissions registration **and**
execution in one act, in two landings: this
registration first, the execution second, as its own
record.

- **Number decision (D-104-1).** At the check of
  2026-11-25 the highest landed spec package on
  origin/main was 103
  (`specs/103-meroitic-source-witness-check/`); no
  104 directory existed and no branch carried 104.
  This package takes 104. The branch was cut from
  origin/main `1bd778a0` (the PR #733 merge, the v3
  release records landing).

## 1. What was registered

`specs/104-quantum-alignment-benchmark/` — spec.md,
claims.md, aee-claims.json, plan.md, tasks.md,
test-cases.md (TC-104-01..TC-104-07), this record,
and the AEE assessment below. The benchmark: the
joint one-to-one alignment of the two scored ICS 196
name correspondences under Spec 096's E1 pilot
scoring, formulated as a QUBO (spec.md §3, penalty
P = 1 + Σ s, with the soundness lemma), solved by
three arms — EXACT (exhaustive enumeration + ILP to
zero MIP gap), SA (registered parameters), and QAOA
through the program's IBM Quantum connector route —
on the real instance and on six synthetic sizes to
n = 576, returning the preregistered verdicts
V-104-A and V-104-B about the solvers only. The
claims under registration (claims.md): C104-1
(instance and formulation fidelity), C104-2
(classical results are the registered procedures'
actual outputs), C104-3 (the quantum outcome is
exactly what the connector route returns), C104-4
(no standing moves).

**Route state, on the record at registration
(spec.md §4, D-104-2).** The connector doc for
`custom.ibm-quantum` documents that the registered
connection cannot complete IBM's IAM token exchange
(the key belongs in a form-encoded body at
`iam.cloud.ibm.com`; the registration's hosts and
placement do not offer that route). The
registration-day probe, run before this package was
written (2026-11-25, the connector's
`bin/ibm_quantum_probe2.py` through the registered
surrogate path, Qiskit-style user agent, redirects
refused), returned: GET /api/v1/backends — **HTTP
401, error code 1219, "Error authenticating user"**;
GET /api/v1/accounts/014f444c351f4ecbb720d173b3778b85
— **HTTP 401, error code 1219**; GET /api/v1/instances
— HTTP 404 (a stale-guide endpoint, as the connector
doc records). The route is therefore registered as
dead, NOT EXECUTED — ROUTE DEAD is in the arm's
registered outcome vocabulary, and no substitute
route is permitted under this registration. Execution
re-probes once and files the response (TC-104-06).

## 2. The AEE outcome at registration

`records/aee-assessment-2026-11-25.json` — run_aee.py
assess --phase after_plan (aee 1.5.3) over the
bundle's aee-claims.json: outcome **iterate**; 4
claims assessed, all 4 draft-capped below the 0.70
confidence threshold — the expected shape for draft
claims at registration, the same shape Specs 101,
102, and 103 returned. The assessment's own ledger
entries were written by the tool under
`.specify/extensions/aee/` and are carried in this
landing. (Venue note: the tower's relocated
`glossa-ci` venv's console scripts carry stale
shebangs from the 2026-11-23 home cleanup, so the
assessment ran through a PATH shim invoking the
venv's interpreter directly; the tool and version
are the program's own.)

## 3. Registration cascade (executed figures)

- Taxonomy: Spec 104 added to the program-map
  taxonomy under Program infrastructure /
  Governance, lifecycle & generated layers (decision
  D-104-3); studies 104 → 105.
- Intake: the bundle's 4 claims appended through
  tools/ledger/import_bundle.py, dated 2026-11-25
  (4 appended, 0 already canonical). Ledger 1,076 →
  1,080 lines; claims 1,045 → 1,049; canonical
  SHA-256 `14c925e8750701976c7befb106f033e74f949379134820b3a25772a40584d576`
  → `0a086ecd91e816584346e6f400fc050e9c80e687b510764b14856c5f1043ffc3`.
  verify-canonicals over the grown build, before
  any pin moved: **6/6 PASS**.
- Settling layer: both T405 scenarios re-executed
  over the grown build (runs
  `settling-20261125T143521Z-6c100f` incumbent,
  `settling-20261125T143521Z-0b89c3` full-register,
  same 286-sign full-frame scope, same registered
  scenario ids); both result blocks byte-equal to
  the superseded generation's, verified by direct
  comparison of the stored records, and the pair's
  input pins identical to the superseded generation's
  except the ledger pin itself. The Stage 4 dual-run
  comparison re-filed from the new pair (its diff
  against the previous filing is the ledger pin
  only). Assignment sets re-materialized unchanged
  (run `settling-20261125T143602Z-d9ba61`; incumbent
  94, full-register 286, H003 out of frame). The
  canonical pin refreshed as re_derivations[20] of
  settling-canonical.json. The superseded generation
  (settling-20261123T222738Z-c1c0ef,
  settling-20261123T222739Z-741a2f,
  settling-20261123T222752Z-fbc1dc) departed the run
  store in this landing; their departure acts are
  appended to the run index in the landing's
  completion commit, naming the registration commit
  as `superseded_by_commit` and each record's blob
  hash from the pre-landing tree.
- Generated layers, regenerated in dependency
  order: matrix 1,572 cells (supports 1,565,
  opposes 7) over 1,049 rows; map-data 1,693
  elements, 1,572 edges, settling runs carried 2;
  program map: 1,049 claims, 105 studies. Falsifier
  census 1,040 of 1,049 claims, the same 9 gaps.
- Census pins updated from the regenerated actuals
  in test_program_map_conformance.py (including the
  Program infrastructure domain census 25 → 26),
  test_spec086_ledger_gate.py,
  test_spec086_map.py,
  test_spec095_stage4_instantiation.py,
  test_spec095_t403_dashboard.py (including the
  T405 run of record, re-pinned to
  settling-20261125T143521Z-6c100f, whose quantities
  are the superseded generation's, byte-equal), and
  the frontend e2e census texts
  (frontend/e2e/system-graph.spec.ts,
  frontend/e2e/researcher-dashboard.spec.ts):
  claims 1,045 → 1,049; bundle population 1,022 →
  1,026; open class 1,036 → 1,040; falsifier-present
  1,036 → 1,040; draft status 1,021 → 1,025; ledger
  lines 1,076 → 1,080; studies 104 → 105; matrix
  cells and map edges 1,568 → 1,572; map elements
  1,689 → 1,693; supports edges 1,561 → 1,565;
  claims untouched by any run 1,044 → 1,048.
- Recommendations ledger: no row added (D-104-4 —
  the study's provenance is the owner's direct
  order, not a Co-scientist recommendation).

## 4. Standing

Spec 104 is REGISTERED. Its execution is commissioned
by the same owner act and lands as the second landing
under this registration, filing its outcome record in
this spec's records/ and returning V-104-A and V-104-B
exactly as registered. No standing, verdict, or tally
is changed by this registration.

**Venue.** All work for this package ran on
tower-compute in the fresh clone
`~/.syncyard/worktrees/glossa/spec104-reg` (branch
`spec-104-quantum-alignment-benchmark`). Nothing ran
in the coordination VM or on the mini-server, except
the connector route probe of §1, which runs through
the Muse credential-surrogate path by construction
and computes nothing.

**AI disclosure:** executed by an AI agent (Muse,
via Muse) at the direction of Tristen Pierson, per
constitution sec. VI.

## Completion pass (2026-11-25, same landing)

- **Departure acts appended.** The three superseded
  settling records named in §3 departed the run store
  in this landing; their departure acts were appended
  to the run index through `run_records.append_act`
  in this completion commit, naming the registration
  commit `42d61527006fa0efb7302c96825bc96ed5e5b504`
  as `superseded_by_commit` and each record's blob
  hash from the pre-landing tree, as §3 anticipated.
  The run-index completion pass (build_legacy_index.py)
  entered the legacy event for re_derivations[20] and
  named the departed records post-spec skips (folded
  census 85 entries).
- **Final-tree verification.** The ledger gate on
  the final tree, both modes, run standalone:
  **default 29 PASS / 0 FAIL / 1 NOT-RUN (RESULT:
  PASS)** and **--regen 32 PASS / 0 FAIL / 0 NOT-RUN
  (RESULT: PASS)**. (The single NOT-RUN in default
  mode is the V7 lossless-regeneration check, which
  runs under --regen.) The five affected backend
  suites were run on the final tree: **114 tests,
  all passed**.
