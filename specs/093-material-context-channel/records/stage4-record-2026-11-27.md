# Spec 093 Stage 4 — stage record (2026-11-27)

Stage 4 (First computed passes: T401, T402, T403)
executed 2026-11-27 under the owner's commission of
2026-11-27 in the Glossa-Lab chat, which commissioned
Stages 3–6 of this spec (the reconciliation is stated
in the Stage 3 record's §1 and is not repeated here).
Three tasks, three freezes committed before any
computation under them (PR #781), three outcomes
recorded below in spec.md §5's vocabulary. No claim's
status, stage, or score was changed by this stage
(C093-13).

## 1. State found on resumption, and its verification

The first execution pass at this stage ended on a
runtime infrastructure fault after the freezes and the
execution tools were committed (tools commit
`ed49c849`, the code version both T401 run records
pin). The state it left, found in the tower-compute
worktree and verified before anything was built on it:

- **T401:** both runs minted and indexed
  (`study-20261127T095820Z-2c776c`, run-administration;
  `study-20261127T095821Z-31eef3`, run-controls), the
  audit and adjudication files written, all uncommitted.
- **T403:** the counts file written, uncommitted.
- **T402:** the census tool committed; the census not
  yet run.
- **One tool repair, disclosed:** the committed auditor
  read the run records at the wrong key path (a
  `header` path where the run-defs v2 record shape
  carries `run.key`), so as committed it would have
  found no runs at all. The repair (two lines,
  `tools/spec093/audit_stage4_site.py`) stood
  uncommitted in the worktree; it is committed in this
  stage's execution landing, and the audit below is
  the repaired auditor's verdict. The runs themselves
  were produced by the committed runner and are
  untouched by the repair.

Verification on resumption, before any outcome was
taken from the found state: the repaired auditor
re-run reproduces the filed audit **byte-identical**
(verdict AGREE); the mechanical adjudication re-run
reproduces the filed adjudication **byte-identical**;
the T403 administration re-run reproduces the filed
counts **byte-identical**; the T402 census was then
run fresh (§3). The outcomes below are therefore the
verified outcomes of the administrations as frozen,
not summaries of a dead worker's files.

## 2. T401 — Site pass: NOT YET

Freeze: `records/stage4-site-freeze-v1.md`. Population
reproduced by the runner from the pinned snapshot:
P-site 966 (Mohenjo-daro 839, Harappa 110 adjudged;
the four sites below the freeze's 50-record floor —
Chanhu-Daro 7, Sutkagen-Dor 6, Lothal 3, Kalibangan 1 —
excluded and named in the freeze, as C093-8 requires).
Arms per the freeze's split: Mohenjo-daro 587
discovery / 252 held-out; Harappa 77 discovery / 33
held-out. Runs: `study-20261127T095820Z-2c776c`
(administration) and `study-20261127T095821Z-31eef3`
(permutation controls and pseudo-site battery), both
under run-defs v2 with the freeze and the §1 pins in
every run key. Independent audit
(`tools/spec093/audit_stage4_site.py`, which does not
import the runner): **AGREE** — both executions'
result blocks recompute and match
(`records/t401-audit-2026-11-27.json`). Mechanical
adjudication against freeze §6, gated on the audit
(`records/t401-adjudication-2026-11-27.json`):

| quantity | discovery stat vs p99 | held-out stat vs p95 | direction | pseudo-site control | verdict |
|---|---|---|---|---|---|
| Q1 length (KS) | 0.0702 vs 0.1649 — clause 1 FAILS | 0.1281 vs 0.2146 — clause 2 FAILS | +1 discovery, −1 held-out — clause 3 FAILS | behaves (p95 0.1260 < 0.1649) | NOT YET |
| Q2 sign choice (TV) | 0.3308 vs 0.3285 — clause 1 met | 0.4288 vs 0.4456 — clause 2 FAILS | (unsigned; no clause) | behaves (p95 0.3188 < 0.3285) | NOT YET |

**Pass outcome: NOT YET.** The machinery is not the
obstruction: both permutation batteries ran as frozen
and the pseudo-site negative control behaves for both
quantities, so the failures are the bars' verdicts on
the observed statistics, not control failures
(C093-6). Q2's discovery statistic clears its 99th
percentile narrowly and its held-out statistic does
not clear its 95th — the replication clause is where
Q2 falls. Q1 falls on every clause, and its
length-direction reverses between arms. No
re-administration under this freeze repairs a NOT
YET (C093-8); a successor attempt is a new freeze.
No statement from this pass is accepted, so nothing
is cited downstream at channel strength (C093-7).

*This does not establish:* why any accepted regularity
holds — the pass states a joint-distribution fact at
channel strength (C093-7), and no cause, function, or
reading may be read into it. (T401's line, carried
verbatim. No regularity was accepted; the line stands
as the bound on what an accepted pass could have
said.)

## 3. T402 — Material pass: CANNOT BE ADMINISTERED

Freeze: `records/stage4-material-freeze-v1.md`. The
join gate is met: the Stage 1 join (K2) was accepted
at precision 1.000 against its freeze's 0.90 floor
(D-093-4; `records/t103-join-audit-2026-11-06.md`
§3), so the pass's stop is not a join failure. The
administration rule (freeze §4) was executed:
`tools/spec093/count_stage4_material.py` recomputed
the §2 counts from the pinned join output (pin
verified, SHA-256 `7107f738…`; presence and class
counting only — no sequence property computed):

```
join pairs: 179
material census: {'Clay': 1, 'Faience': 1, 'Steatite': 176}; empty sentinel: 1
classes at or above floor 10: {'Steatite': 176} (1 class(es))
frozen counts reproduce: True
administrable under freeze §4: False
```

The frozen counts reproduce exactly, and **one**
class meets the floor of 10 where the freeze
requires **at least 2** for a material-conditioned
pass to compare anything. **Outcome: CANNOT BE
ADMINISTERED**, with the forcing counts on the face
of this record: Steatite 176 alone at or above the
floor; Clay 1 and Faience 1 below it; 1 pair carrying
the empty sentinel; 179 total. No threshold was
adjusted to convert the stop into a pass (C093-8).
The standing bound the freeze inherits is restated:
material class carries no independence standing from
Stage 2 (NOT ADMINISTERED there), so even had this
pass run, its statements would have been bookkeeping
statements about the record system, not channel
evidence (FR-093-04).

*This does not establish:* anything about material
practice in the world if it stops — a stop is a
finding about the record system, stated at its
counts. (T402's line, carried verbatim.)

## 4. T403 — Contact-context administration: E1–E4 MET

Freeze: `records/stage4-contact-freeze-v1.md`, citing
comparanda entries CR-093-01 and CR-093-02 (Stage 3)
and no others. Acceptance: human-as-oracle; the
counts are mechanical, adjudged by
`tools/spec093/run_stage4_contact.py` against the
freeze's §3 expectations (machine record:
`records/stage4-contact-counts-2026-11-27.json`,
reproduced byte-identical on resumption):

- **E1 (context-bearing): MET.** 14 of 14 seal rows
  carry a non-empty `find_period`; 12 of 14 carry an
  excavation find spot (freeze bar: at least 12).
- **E2 (deposition outside the Indus region): MET.**
  11 of 14 rows name a find spot outside the Indus
  region (bar: at least 10).
- **E3 (inscription-bearing): MET.** 11 of 14 rows
  carry a recorded `inscription_length` of 2 or more
  with `signs_confidence` other than "none" (bar: at
  least 10).
- **E4 (documentary shape under CR-093-02's window):
  MET.** The modal recorded period over the 1,462
  Meluhha hits is Ur III (850 hits); 1,155 hits carry
  a recorded period that is exactly one of the
  freeze's in-window labels (bar: at least 1,000);
  compound labels counted out-of-window, as the
  freeze directs. The recomputation agrees with the
  rebuild's filed aggregates (`filed_aggregates_agree:
  true`) — no disagreement outcome arose.

The licensed statements, in the freeze's §4 words,
are therefore in force: *the 14 excavated seals form
an evidence class whose find contexts are recorded,
predominantly outside the Indus region, over the
window CR-093-01 froze; Indus-type seals were
deposited in Mesopotamian, Elamite, Gulf, and
Iranian-plateau contexts in that window*; and *the
documentary record of the contact, inside CR-093-02's
frozen window, is concentrated in the Ur III period.*
The bounds travel with them: neither statement is a
population claim (n=14 is an evidence class); the
Meluhha counts describe the surviving textual record
as rebuilt, not trade volume; and the identification
of Meluhha with the Indus world is the mechanism's
premise — named in the register, not proven by this
administration. No reading, sign value, or
direction-of-influence claim beyond deposition is
licensed (C093-13).

*This does not establish:* a population claim of any
kind — n=14 is an evidence class, and this task's
record says so on its face. (T403's line, carried
verbatim.)

## 5. What this stage leaves standing

C093-1's standing is untouched by this stage and
stands as Stage 2 finally recorded it: **INDEPENDENT
IN PART for site and find context**, with the
closure-qualifier addendum's population sentence
(179 joined pairs, all Mohenjo-daro, single stratum;
no cross-site inference). Stage 4 adds no accepted
culture-side regularity: the site pass is NOT YET,
the material pass CANNOT BE ADMINISTERED, and the
contact administration licenses only its two bounded
evidence-class statements. The gaps this stage's
outcomes name — the material field's single usable
class, and site coverage beyond the two adjudged
sites — are carried to Stage 6's register entries.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
