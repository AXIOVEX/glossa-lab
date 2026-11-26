# Glossa-Lab tree and data discipline — 2026-11-24

Owner's order (2026-11-24 07:50 ET): fix the broken things from the daily sweep, including the missing corpus; no needed data may live in a tree that looks like an orphan; every repository gets a protected primary home plus secondary trees for branch work; settle the terminology; cleanups keep happening, but never again delete data we need.

## 1. Terminology (settled)

Git's own vocabulary is **main worktree** vs **linked worktrees**: several checkouts sharing one repository object store. That is not what this fleet mostly does. Our trees are **full clones** (each with its own object store), plus a small number of bare mirrors. Calling a clone a "worktree" invites the exact mistake that keeps costing data: treating a clone as disposable scratch when it is in fact the only copy of something. The program's terms, from today:

- **Primary tree** — the one designated tree of record for a repository on a host. It is the analogue of git's main worktree, but it is a clone, so the precise word is *primary clone*. A primary tree is protected (section 3) and is never used for task work.
- **Secondary tree** — any other clone, linked worktree, or mirror of the same repository, created for a task, a branch, a build, or a recovery. Secondaries are disposable, but only under the proof rule (section 4).
- **Primary data home** — the designated home for a body of data that git does not carry (corpora, state files, archives, custody material). Data bodies do not live "in a tree" at all; they live in a data home, and trees that need them hold *operational copies* whose hashes are verified against the data home or against a registered pin.

One sentence version: **repos have primary and secondary clones; data has primary data homes; nothing needed lives only in a secondary.**

## 2. Why this exists — the Holdat loss, with its mechanism named

The Holdat LLC Indus Corpus is gitignored (`.gitignore`: `corpora/`). No clone, move, or checkout ever carries it. The loss chain, from the records:

1. The corpus lived in the desktop checkout's `corpora/` and was lost in the desktop wipe — a loss of gitignored bytes that no git operation could see or prevent.
2. The backend was re-stood-up on the mini-server (2026-11-09) from a fresh checkout, which of course had no `corpora/`. On 2026-11-12 the foundation check failed (13 pass / 1 fail / 2 warn) on exactly the two missing Holdat files, and the corpus was restored into the serving checkout from the VM's then-protected checkout, hashes verified (memory record 2026-11-12: HOLDAT FIX + FOUNDATION PASS).
3. The restore went into the serving checkout only. Every other tree on every host kept lacking the corpus, so any foundation check run from a non-serving tree reports "corpus missing" — the 2026-11-24 sweep's WARN (23/24, "Corpus files missing") is that structural defect surfacing again, not a second loss. Verified 2026-11-24: the serving checkout's `indus_corpus 2.csv` hashes to `62d14d2b…`, exactly the Spec 100 pin, and the live backend foundation check passes 17/17.

The general lesson: **gitignored bytes are invisible to every protection git offers.** They need a data home and a hash, or they will be lost again at the next wipe, move, or cleanup.

## 3. Primary registry (census of 2026-11-24)

### Mini-server (live venue)
| Tree / home | Role | State at census |
|---|---|---|
| `~/glossa-lab` | **PRIMARY — serving tree** (live backend's checkout; origin) | main at 910b137a (through Spec 097 by design); 5 modified runtime outputs (anchor staging, loop sessions, foundation report) — runtime state, not work |
| `~/glossa-data/` | **PRIMARY DATA HOME** (created 2026-11-24) | Holdat corpus, both files, pin-verified, read-only, with CUSTODY.md |
| `~/.syncyard/worktrees/glossa-lab/ui081-build` | Secondary — MCP server tree (Stage D home; Spec 083) | clean, branch feat/083-identity at 81f10bd5; Holdat convenience copy placed and pin-verified 2026-11-24 |
| `~/.syncyard/worktrees/glossa-lab/paper-v11-deposit-repo` | Secondary — v11 deposit tree | clean, branch preprint-v11-deposit at 3ba22206, in sync with origin |
| `~/glossa-work/paper-adjudication/repo` | Secondary — paper adjudication clone | clean, main at bd921ec9; holds a PARTIAL Holdat copy (indus_corpus only, pin-verified; no roles file) |
| `~/glossa-work/recovery-2026-11-17/glossa-lab-mirror.git` | Secondary — bare recovery mirror (2026-11-17) | recovery artifact; retain until the discipline's retention review |
| `~/glossa-work/adopt095/`, `~/glossa-work/paper-v11-deposit/` | Record bundles / stubs, not trees | evidence logs and a closing-commit bundle; the paper-v11-deposit repo was moved out by the worktree-keeper 2026-11-22 |
| `~/glossa-work/tools/`, `~/glossa-work/venvs/` | Tooling (node runtime, venvs) | not data |
| `~/data/glossa.db` | **Classified 2026-11-26** (see section 8): backend seed/initialization artifact of 2026-11-19, NOT the live database and not live program data | retained in place; NOT moved and NOT deleted |

### This VM (coordination venue)
| Tree / home | Role | State at census |
|---|---|---|
| `~/workspace/glossa-lab` | was the protected VM checkout | **ABSENT** — lost in a VM replacement; the repo is safe on GitHub; its Holdat copy had already been restored to the mini-server on 2026-11-12, before the loss |
| `~/workspace/goals/glossa-lab-…/` (this goal workspace) | **PRIMARY — program record home** on the VM (PROGRAM-STATE, goal files, cron state files) | live |
| `~/workspace/research_notes/` | **PRIMARY — articles home** (485 MB) | live |
| `~/workspace/glossa-run/` | Retired state + publish records | historical; the tower state files supersede its state copies |
| `~/workspace/glossa-wt-029*`, `~/workspace/glossa-029I-*`, `~/workspace/glossa-test-data-029H` | Legacy secondaries (Spec 029 era, October) | untouched by this pass; governed by the checklist in section 5 before any future deletion |
| `~/workspace/axiovex-website` | **Not ours** — the Axiovex Systems chat's shared working clone | staging at eef1399, 43 uncommitted entries from other chats; the articles job no longer depends on it (section 6) |

### Tower-compute — PENDING its return
Tower-compute was unreachable throughout this pass (SSH stalled; a separate owner-ordered recovery is in flight). Its rows are carried from the program record and must be verified on its return: the archive + state files under `/home/tpierson/Development/glossa-archive/glossa-run/` (primary data home for program state), worker clones under `~/.syncyard/worktrees/glossa/`, and `glossa-custody` in the home root. **No tower census claim in this document is verified yet.**

## 4. Rules

**Primaries.**
1. A primary tree or data home is never deleted, moved, or cleaned by any cleanup pass. Cleanup tooling (including the worktree-keeper) must exclude primaries **by name**; "it looked unused" is never a deletion ground for a primary.
2. A primary tree is never used for task work: no branches, no edits, no builds in it. The serving tree serves.
3. Every body of needed data has exactly one primary data home, named in this registry or its successor. Operational copies in trees are verified against the home or a registered pin by hash, and a copy is never the only copy.

**Secondaries.**
4. Secondaries are created only under the designated work homes: mini-server `~/glossa-work/` or `~/.syncyard/worktrees/glossa-lab/`; tower-compute `~/.syncyard/worktrees/glossa/`; on the VM, only inside a named run directory. Never in a host's home root.
5. A secondary is deleted only after proof, recorded in the landing or run record: working tree clean **and** every commit pushed (or a salvage bundle filed in the primary record home), **and** a gitignored-content sweep (rule 6) with any needed bytes first copied to their primary data home and hash-verified.
6. **The Holdat rule:** before any tree on any host is deleted, and before any host is wiped, replaced, or retired, sweep it for gitignored content (`git status --ignored`, plus `corpora/`, `data/`, and state-file paths by name). Gitignored bytes are presumed needed until a census row in this registry says otherwise.

**Checks.**
7. A corpus or foundation verdict is valid only from the serving backend's API surface or from inside a primary tree. A "corpus missing" result from a secondary tree is a defect of that tree, not a corpus loss, and is reported as such.

## 5. Pre-deletion checklist (any cleanup, any host)

1. Is the target a primary (section 3)? If yes, stop — primaries are excluded by name.
2. `git status` clean? If not, is every change pushed, or salvaged as a bundle/filed copy in the primary record home?
3. Every local branch pushed or explicitly abandoned on the record?
4. Gitignored sweep done (rule 6)? Every needed file copied to its primary data home and hash-verified after the copy?
5. Any state files, corpora, archives, or custody material in the tree? Each one has a primary home and a verified copy there?
6. The deletion, the proofs, and the checklist answers are written into the run or landing record **before** the delete runs.

## 6. Applied in this pass (2026-11-24)

- **Holdat corpus:** primary data home created at `~/glossa-data/corpora/holdatllc_indus/` on the mini-server; both files copied from the serving checkout and hash-verified (`indus_corpus 2.csv` = the Spec 100 pin `62d14d2bebf7c2c80d98a2958e75ec52bff3f240ff3f5e85d1f7f40cbe28218e`; `all_symbol_semantic_roles 2.csv` = `eb6d3b6ae195a2570e098dc6779dbd6c7bea97da5c4714bf406c3bb98f9d2aaf`); files set read-only; CUSTODY.md filed beside them. A pin-verified convenience copy was also placed in the MCP work tree so checks run there stop false-flagging. Foundation check re-run on the serving backend: **17 pass / 0 fail / 0 warn, overall PASS** ("Holdat corpus: 1,670 seals / 7,002 tokens / 390 signs — pass"). The MCP-tool route itself is tower-bound (Stage E) and is re-verified when the tower returns.
- **Articles job:** the daily article job's publish step depended on the shared `~/workspace/axiovex-website` clone — a secondary being used as a primary, and another chat's working tree besides. Its failures of 2026-11-22 (git write refused in that clone) and 2026-11-23 (clone stale and dirty; fresh clone timed out; the completed sparse clone was stopped by an execution-risk flag) are this defect, not article defects: both articles were written and their state advanced. The job now publishes from a fresh clone made in its own run directory, under the standing clone-processing approval for AXIOVEX/axiovex-website (owner, 2026-11-22). The two unpublished page entries (2026-11-22 and 2026-11-23) are handed to the Axiovex Systems chat with the shared clone's state.
- **Reply watch:** its failed 2026-11-24 07:13 run is tower-caused (state file unreachable with the tower), already covered by the owner-ordered tower recovery; no separate fix.
- **Zenodo PRED-2026-003:** the record resolves; contents unverified (403) — noted, not forced; still a candidate, never scored.

## 7. Pending the tower's return

1. Tower census rows verified against section 3, including the archive/state primary data home and `glossa-custody`.
2. Holdat copy in the tower archive (if any) hash-checked against the pin; the tower MCP tree's corpora checked and, if absent, supplied from the primary data home.
3. MCP foundation check re-run through the Stage E MCP route and its verdict recorded verbatim.
4. Any needed data found living in tower secondaries moved or copied to its primary home under rule 5's proof standard.

## 8. Addendum — 2026-11-26 (owner-approved data-home actions)

Executed 2026-11-26 under the owner's approval in the Glossa-Lab chat (2026-11-26 ~01:54 ET: "For everything else, execute now to your recommendations"), closing the two census flags this document carried: the unclassified `~/data/glossa.db` and the tower secondaries holding Spec 097 / Spec 098 data with no primary home.

### 8.1 `~/data/glossa.db` (mini-server) — CLASSIFIED, retained in place

- **What it is:** a Glossa backend database at schema version 27 holding **seed and initialization content only**, created in a single window on 2026-11-19 (every content timestamp falls between 2026-11-19T20:48:22Z and 20:52:58Z, matching the file's mtime 2026-11-19 15:52:59 EST). Populated tables: `corpus_catalogue` 39 rows (the backend's built-in corpus catalogue), `studies` 13 (built-in study definitions: Beam Decipherment Suite, the Fuls suites, Indus Structural Atlas, and peers), `texts` 7 (seed texts), `report_templates` 12, `model_scores` 82 (seed-time scoring), `discovery_items` 85 (one discovery fetch, 2026-11-19T20:49:00Z), `projects` 10 (the Indus Script Decipherment project shell plus test-fixture projects — Empty Scope, No Position, No Question, Position, Question — and remediation bundle/probe projects), `jobs` 2 (one failed discovery fetch; one report-generator job left in "running"), `job_results` 1. Every table that would carry real program work is empty: `anchor_sets`, `canonical_signs`, `citations`, `correspondences`, `hypotheses`, `notebooks`, `research_goals`, `research_loop_state`, `sign_cluster_assignments` all hold 0 rows.
- **What it is not:** it is NOT the live program database. The serving backend's database is `~/glossa-lab/backend/data/glossa.db` (7,528,448 bytes, SHA-256 `659491f02ddf6e9a62866924b681580378de590eadc009e9959ab69e2beedbae`, mtime 2026-11-25, actively written; 748 discovery items, 16 jobs) — a different file with different content, so this file is not a stray copy of it and no hash-identical primary exists. No process held `~/data/glossa.db` at inspection.
- **Inspection proof:** the file was opened read-only and immutable (`mode=ro&immutable=1`); SHA-256 before and after inspection identical: `f3d4747bb9c2d9d9d68a9f361ba9523b69c3bd28309afa1c94a51f5a09c53cb5` (2,617,344 bytes; mtime unchanged).
- **Determination:** classified as a **backend seed/initialization artifact (2026-11-19)**. It is not live program data, so no primary data home is designated for it; it is retained in place under this census row, and it is not deleted. Any future cleanup treats it under section 5 with this classification on the record.

### 8.2 Tower-compute Spec 097 / Spec 098 data — primary data home designated, data moved

- **Designation:** `~/.syncyard/worktrees/glossa/glossa-custody/` is the primary data home for this material: `glossa-custody/spec097/` (created 2026-11-26) and `glossa-custody/spec098/` (already holding `heldout-clusters-v1.txt`).
- **Sweep (Holdat rule):** neither source folder was a git repository and neither held subdirectories, symlinks, or dotfiles; the full inventory was 6 files, all unversioned study data, all moved. Nothing else was in either tree to sweep.
- **Spec 097** (from `s097-data/`, 3 files, 54,566,631 bytes) → `glossa-custody/spec097/`: `forms.csv` (51,272,436 bytes, SHA-256 `4ee30b771a2cba59e7e904587f7f60dc3d823824a7b9aae9dd6f73a960139321`), `languages.csv` (3,292,247 bytes, `647174df2eb812eff370355b02b6843d76bfb2b082147bc263e5ccd4cc628be5`), `parameters.csv` (1,948 bytes, `2ed306c24552ea61e48ad6dc067859d8b70029abfc1d36668246214a5a1183ec`).
- **Spec 098 Stage 3 runs** (from `s098-stage3-runs/`, 3 files, 65,719 bytes) → `glossa-custody/spec098/`: `release-log.json` (597 bytes, `492de273454d1600c5077447409cfb25855e0e5b3ad8f2e16a196cf9e3a4b2f5`), `study-20261122T163036Z-d32312-release.json` (597 bytes, same hash — byte-identical to `release-log.json`), `study-20261122T163043Z-c6e811-score-raw.json` (64,525 bytes, `a5943966a38bdf160461c8de0517e9dbd7a07ddfb840b552ab37981c83cae7f1`). The pre-existing `heldout-clusters-v1.txt` (9,244 bytes, `1974d83a5f667b71dbd53ecdb2e42a8221c6d4b91bdd32202b2a80579bf96cf9`) was not touched and re-verified unchanged after the move.
- **Move proof:** every file's SHA-256 was taken before the move and re-taken at the destination after it; all 6 match exactly. The moves were renames on the same filesystem (no copy-then-delete). Both source folders were confirmed empty after the move and the empty folders removed. Nothing was deleted. A `MOVE-RECORD-2026-11-26.md` stands in each custody folder with the same hashes.
