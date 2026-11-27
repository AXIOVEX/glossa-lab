# Spec 098 standing cascade — application record

Date: 2026-11-27. Branch `spec098-standing-cascade-2026-11-27`.

## The act

Spec 098 (identifiability over the 65) is complete: Stages 0–4 executed
and filed, the Stage 4 outcome record at
`records/stage-4-outcome-2026-11-27.md` (landed by PR #777, merge
`10beaf367441e1e7ded919a5e3b8dd1dcec047cb`). Its eight claims,
C098-1..C098-8, stood at `draft`. Section 7 of that outcome record
adjudicated each of the eight SUPPORTED — C098-2 in its amended form,
C098-3 in its frozen executed form as stated in full there, the rest as
registered — and provided for their standings to move by a separate
program act. This record files that act: eight dated, append-only,
provenance-marked reclassification entries in
`glossa-indus/ledger/claims.jsonl`, appended through the ledger intake
path (`glossa_lab.ledger_intake.append_entry`), each carrying only the
status field for its superseded claim entry, draft →
`strongly_supported` (the ledger's positive-class status under
program-map-defs v1 §4.2; the ledger carries no plain "supported"
status). No other claim's status, stage, or score moved. M375 carries
no standing act: its Spec 098 result is a discrimination on
pseudo-held-out material under a design ceiling, the genuine-holdout
subset is empty, and §7 adjudicated no standing change for it. No Indus
anchor standing moved.

## Authorization chain

- 2026-11-27 04:05 ET: the owner's blanket approval in the Glossa-Lab
  chat ("Yes do all these things now or take my approval now to do at
  the best time") commissioned this cascade among the approved acts,
  on the Stage 4 outcome record's §7 adjudications.
- 2026-11-27 08:26 ET: the owner approved work in a fresh tower clone.
  Three consecutive attempts stopped at the execution-risk flag: the
  named clone `s098-standing-act-20261127` (at its creation, and again
  inside it after a further approval naming it), then this clone,
  `s098-cascade-wt-20261127`, at its creation.
- 2026-11-27 08:41 ET: after this clone's trip, the owner ruled "clear
  work inside s098-cascade-wt-20261127 now, after its trip". The
  cascade was executed inside that clone under that ruling, and in no
  other tree.

## The eight entries as applied

| entry | supersedes | move |
|---|---|---|
| `098-identifiability-over-the-65/C098-1/reclassification-2026-11-27` | `098-identifiability-over-the-65/C098-1` | draft → strongly_supported |
| `098-identifiability-over-the-65/C098-2/reclassification-2026-11-27` | `098-identifiability-over-the-65/C098-2` | draft → strongly_supported |
| `098-identifiability-over-the-65/C098-3/reclassification-2026-11-27` | `098-identifiability-over-the-65/C098-3` | draft → strongly_supported |
| `098-identifiability-over-the-65/C098-4/reclassification-2026-11-27` | `098-identifiability-over-the-65/C098-4` | draft → strongly_supported |
| `098-identifiability-over-the-65/C098-5/reclassification-2026-11-27` | `098-identifiability-over-the-65/C098-5` | draft → strongly_supported |
| `098-identifiability-over-the-65/C098-6/reclassification-2026-11-27` | `098-identifiability-over-the-65/C098-6` | draft → strongly_supported |
| `098-identifiability-over-the-65/C098-7/reclassification-2026-11-27` | `098-identifiability-over-the-65/C098-7` | draft → strongly_supported |
| `098-identifiability-over-the-65/C098-8/reclassification-2026-11-27` | `098-identifiability-over-the-65/C098-8` | draft → strongly_supported |

The texts as appended, quoted from the ledger itself:

**C098-1** — entry `098-identifiability-over-the-65/C098-1/reclassification-2026-11-27`, status `strongly_supported`:

> Owner commission (Tristen Pierson, 2026-11-27 04:05 ET, Glossa-Lab chat: "Yes do all these things now or take my approval now to do at the best time"), under which Spec 098 Stage 4 was executed. C098-1 is adjudicated SUPPORTED on the Stage 4 outcome record (specs/098-identifiability-over-the-65/records/stage-4-outcome-2026-11-27.md, section 7; landed PR #777, merge 10beaf367441e1e7ded919a5e3b8dd1dcec047cb): the freeze and the seal record were committed 2026-11-21, before any scoring; the first scoring-path run is the Stage 3 run index of 2026-11-22; the held-out list was released exactly once, at scoring, and that release is recorded; the seal hash was recomputed from the released list at release and at scoring; no pre-seal scoring artifact and no second release is on the record. The falsifier does not fire. The ledger status value for a SUPPORTED adjudication is "strongly_supported" (program-map-defs v1 section 4.2, class positive). This entry carries the status field for the superseded entry (status: "draft" -> "strongly_supported"); no other field of the superseded entry is moved. This entry's text was authored on 2026-11-27 for this cascade, re-derived from the outcome record's section 7 adjudication (the texts prepared earlier on 2026-11-27 were not recovered); it is dated to this act and not backdated. Record of record: specs/098-identifiability-over-the-65/records/standing-cascade-application-2026-11-27.md.

**C098-2** — entry `098-identifiability-over-the-65/C098-2/reclassification-2026-11-27`, status `strongly_supported`:

> Owner commission (Tristen Pierson, 2026-11-27 04:05 ET, Glossa-Lab chat: "Yes do all these things now or take my approval now to do at the best time"), under which Spec 098 Stage 4 was executed. C098-2 is adjudicated SUPPORTED, in its amended form of record on the Stage 4 outcome record (specs/098-identifiability-over-the-65/records/stage-4-outcome-2026-11-27.md, section 7; landed PR #777, merge 10beaf367441e1e7ded919a5e3b8dd1dcec047cb): the executed population is the annex population as amended before Stage 2 by the two recorded addendum-rule strikes (M202's exit under the execution freeze annex amendment, 71 to 70; M044's adjudication under the Round 2 amendment, 70 to 69), so the executed population is 69 of the frozen 71; every scored or determined sign is an annex sign carrying its annex value exactly as recorded, variants scored as the recorded disjunctions and penalties charged per alternation, and M374's frozen default applied as frozen; no value was resolved, split, respelled, or re-glossed after the freeze. The amendment is carried on the face of this entry: the claim as registered says the population and its values are the frozen annex's exactly, and the adjudication supports it in the amended form (the annex as amended by the two recorded strikes before execution), not as an unamended 71. The falsifier does not fire. The ledger status value for a SUPPORTED adjudication is "strongly_supported" (program-map-defs v1 section 4.2, class positive). This entry carries the status field for the superseded entry (status: "draft" -> "strongly_supported"); no other field of the superseded entry is moved. This entry's text was authored on 2026-11-27 for this cascade, re-derived from the outcome record's section 7 adjudication (the texts prepared earlier on 2026-11-27 were not recovered); it is dated to this act and not backdated. Record of record: specs/098-identifiability-over-the-65/records/standing-cascade-application-2026-11-27.md.

**C098-3** — entry `098-identifiability-over-the-65/C098-3/reclassification-2026-11-27`, status `strongly_supported`:

> Owner commission (Tristen Pierson, 2026-11-27 04:05 ET, Glossa-Lab chat: "Yes do all these things now or take my approval now to do at the best time"), under which Spec 098 Stage 4 was executed. C098-3 is adjudicated SUPPORTED, in its frozen executed form, which is stated in full here on the Stage 4 outcome record (specs/098-identifiability-over-the-65/records/stage-4-outcome-2026-11-27.md, section 7; landed PR #777, merge 10beaf367441e1e7ded919a5e3b8dd1dcec047cb): rivals R-A..R-E were constructed for all 69 signs under the Stage 2 freeze section 5, one deterministic construction pass per competitor over the same development data and the same frozen search space (WP8 matched budget), the candidate included; the Arm E additions were constructed as the spec names them (M124's comparandum-as-value from M044's package; M329's comparandum-as-value; M330's cross-sign rival carrying M202's evidence package; M047's comparanda-as-value). The frozen executed form, in full: (a) R-B was drawn from the Sanskrit lexicon of record for every sign, because no Munda lexicon is carried in the repository, and the frozen space was not widened to fill that absence; (b) under the Stage 2 freeze section 6 assignment rule, a value with no filed signature takes the unconditioned assignment, and every per-sign rival is such a value, so each scored sign's per-sign rivals share the unconditioned model's held-out total, which the raw output records once with the rule stated; R-E was scored as one model. The guard of TC-098-01 ran over the actual development export at Stage 2, and the budget is one construction pass for every competitor. The falsifier does not fire. The ledger status value for a SUPPORTED adjudication is "strongly_supported" (program-map-defs v1 section 4.2, class positive). This entry carries the status field for the superseded entry (status: "draft" -> "strongly_supported"); no other field of the superseded entry is moved. This entry's text was authored on 2026-11-27 for this cascade, re-derived from the outcome record's section 7 adjudication (the texts prepared earlier on 2026-11-27 were not recovered); it is dated to this act and not backdated. Record of record: specs/098-identifiability-over-the-65/records/standing-cascade-application-2026-11-27.md.

**C098-4** — entry `098-identifiability-over-the-65/C098-4/reclassification-2026-11-27`, status `strongly_supported`:

> Owner commission (Tristen Pierson, 2026-11-27 04:05 ET, Glossa-Lab chat: "Yes do all these things now or take my approval now to do at the best time"), under which Spec 098 Stage 4 was executed. C098-4 is adjudicated SUPPORTED on the Stage 4 outcome record (specs/098-identifiability-over-the-65/records/stage-4-outcome-2026-11-27.md, section 7; landed PR #777, merge 10beaf367441e1e7ded919a5e3b8dd1dcec047cb): prediction sheets were constructed and reviewed before unsealing, and acceptance required a neighbour-identity or neighbour-class prediction stated on the frozen record that the rivals do not state; 9 sheets were accepted (M005, M030, M037, M068, M075, M089, M267, M347, M375), and the study's only pass, M375, rests on an accepted sheet; the Stage 2 freeze section 6 answered the spec's motif category in the open (the corpus of record carries no motif or iconography field the estimator can score, so a sheet resting on a motif association alone was not accepted, with the reason recorded per sign); signs with no accepted sheet are NOT IDENTIFIABLE by construction, as the claim provides (19 of the 22 NOT IDENTIFIABLE outcomes, counting M124). The falsifier does not fire. The ledger status value for a SUPPORTED adjudication is "strongly_supported" (program-map-defs v1 section 4.2, class positive). This entry carries the status field for the superseded entry (status: "draft" -> "strongly_supported"); no other field of the superseded entry is moved. This entry's text was authored on 2026-11-27 for this cascade, re-derived from the outcome record's section 7 adjudication (the texts prepared earlier on 2026-11-27 were not recovered); it is dated to this act and not backdated. Record of record: specs/098-identifiability-over-the-65/records/standing-cascade-application-2026-11-27.md.

**C098-5** — entry `098-identifiability-over-the-65/C098-5/reclassification-2026-11-27`, status `strongly_supported`:

> Owner commission (Tristen Pierson, 2026-11-27 04:05 ET, Glossa-Lab chat: "Yes do all these things now or take my approval now to do at the best time"), under which Spec 098 Stage 4 was executed. C098-5 is adjudicated SUPPORTED on the Stage 4 outcome record (specs/098-identifiability-over-the-65/records/stage-4-outcome-2026-11-27.md, section 7; landed PR #777, merge 10beaf367441e1e7ded919a5e3b8dd1dcec047cb): outcomes follow spec section 4's precedence on the actual held-out counts under the frozen bars (minimum 5 held-out tokens; penalized margin at least 10 nats; above the permutation null's 99th percentile, B = 999, seed 9801; flexibility penalty 2 nats per free choice, candidates and rivals alike); Stage 3's verify invocation recomputed all 69 outcomes from the archived raw output under the reference decide() rule with no mismatches, and Stage 4's recount reproduces the distribution and the per-arm counts; the family reporting is counts of per-sign outcomes only. The falsifier does not fire. The ledger status value for a SUPPORTED adjudication is "strongly_supported" (program-map-defs v1 section 4.2, class positive). This entry carries the status field for the superseded entry (status: "draft" -> "strongly_supported"); no other field of the superseded entry is moved. This entry's text was authored on 2026-11-27 for this cascade, re-derived from the outcome record's section 7 adjudication (the texts prepared earlier on 2026-11-27 were not recovered); it is dated to this act and not backdated. Record of record: specs/098-identifiability-over-the-65/records/standing-cascade-application-2026-11-27.md.

**C098-6** — entry `098-identifiability-over-the-65/C098-6/reclassification-2026-11-27`, status `strongly_supported`:

> Owner commission (Tristen Pierson, 2026-11-27 04:05 ET, Glossa-Lab chat: "Yes do all these things now or take my approval now to do at the best time"), under which Spec 098 Stage 4 was executed. C098-6 is adjudicated SUPPORTED on the Stage 4 outcome record (specs/098-identifiability-over-the-65/records/stage-4-outcome-2026-11-27.md, section 7; landed PR #777, merge 10beaf367441e1e7ded919a5e3b8dd1dcec047cb): the Stage 1 record carries the provenance audit's result (the genuine-holdout subset is empty, and its absence is recorded); no IDENTIFIABLE ON HELD-OUT outcome was scored or reported on in-corpus material; the single pass is reported at its capped strength, DISCRIMINATED ON PSEUDO-HELD-OUT, in the Stage 3 record and in the outcome record's section 6. The falsifier does not fire. The ledger status value for a SUPPORTED adjudication is "strongly_supported" (program-map-defs v1 section 4.2, class positive). This entry carries the status field for the superseded entry (status: "draft" -> "strongly_supported"); no other field of the superseded entry is moved. This entry's text was authored on 2026-11-27 for this cascade, re-derived from the outcome record's section 7 adjudication (the texts prepared earlier on 2026-11-27 were not recovered); it is dated to this act and not backdated. Record of record: specs/098-identifiability-over-the-65/records/standing-cascade-application-2026-11-27.md.

**C098-7** — entry `098-identifiability-over-the-65/C098-7/reclassification-2026-11-27`, status `strongly_supported`:

> Owner commission (Tristen Pierson, 2026-11-27 04:05 ET, Glossa-Lab chat: "Yes do all these things now or take my approval now to do at the best time"), under which Spec 098 Stage 4 was executed. C098-7 is adjudicated SUPPORTED on the Stage 4 outcome record (specs/098-identifiability-over-the-65/records/stage-4-outcome-2026-11-27.md, section 7; landed PR #777, merge 10beaf367441e1e7ded919a5e3b8dd1dcec047cb): the study changed no reading's standing, anchor, or class: M375 remains class I on its prior basis; M047's membership was carried on its entry as filed under the Stage 2 freeze section 0 pre-ruling, stated in the pre-release record, and the F-9 act that moved M047 in the standings was a separate program act, not this study's; no record of this study converts an identifiability outcome into a support disposition. This cascade is itself the separate program act the outcome record's section 7 provides for: it moves only the standings of this study's own eight claims, on their own adjudications, and no per-sign outcome, standing, anchor, or class of any other record. The falsifier does not fire. The ledger status value for a SUPPORTED adjudication is "strongly_supported" (program-map-defs v1 section 4.2, class positive). This entry carries the status field for the superseded entry (status: "draft" -> "strongly_supported"); no other field of the superseded entry is moved. This entry's text was authored on 2026-11-27 for this cascade, re-derived from the outcome record's section 7 adjudication (the texts prepared earlier on 2026-11-27 were not recovered); it is dated to this act and not backdated. Record of record: specs/098-identifiability-over-the-65/records/standing-cascade-application-2026-11-27.md.

**C098-8** — entry `098-identifiability-over-the-65/C098-8/reclassification-2026-11-27`, status `strongly_supported`:

> Owner commission (Tristen Pierson, 2026-11-27 04:05 ET, Glossa-Lab chat: "Yes do all these things now or take my approval now to do at the best time"), under which Spec 098 Stage 4 was executed. C098-8 is adjudicated SUPPORTED on the Stage 4 outcome record (specs/098-identifiability-over-the-65/records/stage-4-outcome-2026-11-27.md, section 7; landed PR #777, merge 10beaf367441e1e7ded919a5e3b8dd1dcec047cb): every execution ran on tower-compute in a fresh clone (Stages 1-3 as their records state; Stage 4's verification in the worktree its record names); the Stage 3 run index is complete (prepare, the single release, score, and the verify invocation), each with its payload verdict, with no failed attempts and no gaps; every reported verdict in the study's records is the run's own payload verdict. The falsifier does not fire. The ledger status value for a SUPPORTED adjudication is "strongly_supported" (program-map-defs v1 section 4.2, class positive). This entry carries the status field for the superseded entry (status: "draft" -> "strongly_supported"); no other field of the superseded entry is moved. This entry's text was authored on 2026-11-27 for this cascade, re-derived from the outcome record's section 7 adjudication (the texts prepared earlier on 2026-11-27 were not recovered); it is dated to this act and not backdated. Record of record: specs/098-identifiability-over-the-65/records/standing-cascade-application-2026-11-27.md.

## The texts were re-derived

The eight reason texts prepared earlier on 2026-11-27 were not
recovered: they were searched for in the goal's hidden files, in this
spec's records on main, and in the tower worktrees, and are absent. The
texts above were therefore re-derived for this landing from the Stage
4 outcome record (`records/stage-4-outcome-2026-11-27.md`), §7's
adjudication of each claim and the sections it rests on (§§2–6, the
Stage 2 freeze, the Stage 3 verification record), under the
commission's specification: each entry's basis is that outcome record,
its authorizing act is the owner's 2026-11-27 commission, C098-2's
entry carries its amended form as the outcome record states it, and
C098-3's entry states the frozen executed form in full, including that
R-B is drawn from Sanskrit only and that every per-sign rival takes
the unconditioned assignment. Each text states the re-derivation on
its face.

## Cascade figures

- Claims ledger: 1,110 lines, canonical SHA-256
  `bc601e86f7bbdc851f27494de8bb5ac03d63171797f17dd9c4533f42d1561418`
  → 1,118 lines, canonical SHA-256
  `1dfcbd0867eb6d850702c7005387100d350f2beb12efe1552cc0a3d48192c813`.
  `validate_ledger`: PASS — 1,073 claims, 31 annotations, 14
  reclassifications (6 before this act).
- `verify-canonicals` over the pre-append build: 6/6 registered
  canonicals reproduced before any pin moved; over the grown build
  the same 6/6 reproduce (gate class V8, below).
- T405 settling pair re-executed over the grown build with the
  superseded generation's scopes verbatim (286 signs): incumbent
  `settling-20261127T135013Z-720cf7`, full-register
  `settling-20261127T135013Z-97f795`. Both result blocks are
  byte-equal to the superseded generation's, verified by direct
  comparison of the stored records; every non-ledger input pin is
  identical.
- Comparison re-filed at
  `specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`;
  its diff against the superseded filing is the ledger pin only.
- Assignment sets re-materialized (run
  `settling-20261127T135036Z-4addaa`): incumbent 94 assignments,
  full-register 286, H003 out of frame — unchanged.
- Ledger pin refreshed as `re_derivations[27]` of
  `glossa-indus/ledger/settling-canonical.json`, the provenance pin
  moved in the same motion; the canonical registration's historical
  `run_ids` and input fields did not move. The run index carries the
  new runs' entry acts, the materialization's acts, and the legacy
  entry act for `re_derivations[27]`, appended through
  `tools/ledger/build_legacy_index.py`.
- Derived layers regenerated over the grown build: the matrix
  (`glossa-indus/matrix/`), the map (`glossa-indus/map/map-data.json`)
  and the program map (`glossa-indus/map/program-map*.json/html`).
  Census pins were updated from the regenerated actuals: the
  dashboard pins in `backend/tests/test_spec095_t403_dashboard.py`
  name the new incumbent run `settling-20261127T135013Z-720cf7`
  (lines 193 and 218) and the grown ledger (line 41);
  `backend/tests/test_spec086_map.py` (line 219) and
  `backend/tests/test_spec095_stage4_instantiation.py` pin the
  grown ledger's 1,118 lines and its 14 reclassifications; and
  `backend/tests/test_program_map_conformance.py` pins the new
  class census (open 1055, positive 10). The first CI run on this
  landing's pull request named the four files' stale pins; the
  pins were updated from the regenerated artifacts, verified
  locally (47 tests passing across the four files), and re-run.
- Landing structure: the map builder carries every standing settling
  evaluation record and refuses a record pinned to another ledger
  build (its D-D rule), so the map could only be regenerated after
  the superseded generation departed. The landing therefore runs in
  two commits: the content commit
  `652d26576c68e64b78ffd5ce47db2555a9bc2a01` (the ledger append, the
  new run records, the re-filed comparison, the assignment sets, the
  pin refresh, the index acts, the matrix, the program map and the
  census pins), then the departures commit (the departure acts, the
  record deletions, the regenerated map, this record and the
  history-ledger entry). Both gated publications (matrix and map)
  were then re-run over the final tree and passed the full gate, so
  the published bytes are the gated bytes.

## Departures

The superseded generation departs under run-defs v3 §7.1, each
departure act naming the content commit
`652d26576c68e64b78ffd5ce47db2555a9bc2a01`, the record's git blob at
that commit, and its blob SHA-256: the incumbent run
`settling-20261127T102311Z-ad74e8`, the full-register run
`settling-20261127T102312Z-07ef78`, and the materialization run
`settling-20261127T102325Z-ebb5ff`. Their record files are deleted in
the departures commit.

## Gate profile on the final tree

`tools/ledger/check_ledger_gate.py`: 32 PASS / 0 FAIL / 1 NOT-RUN
(the NOT-RUN is V7 lossless regeneration, which runs only in
`--regen` mode). `--regen`: 35 PASS / 0 FAIL / 0 NOT-RUN.
