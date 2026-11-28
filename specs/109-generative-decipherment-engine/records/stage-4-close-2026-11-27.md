# Spec 109 — Stage 4 close record (Part 5: Eteocypriot candidate ranking)

Filed 2026-11-27. Stage 4 executed Part 5 under
registration §6, in the worktree the owner cleared
for this stage. The stage's filings:
`records/stage-4-freeze-2026-11-27.md` (committed
before any computation),
`records/stage-4-preflight-2026-11-27.md`,
`records/stage-4-outcome-2026-11-27.md`,
`records/stage-4-harness.py`,
`records/stage-4-verify.py`,
`records/stage-4-raw-output-2026-11-27.json`, this
close record, `tasks.md`, and the history ledger.

## 1. Outcome

Part 5's preflight was met in full (clause N 9/9;
clause S median recovery 1.000 against the 0.80
floor, shuffle control 0.167). The ranking ran on
comparanda (a) alone, the variant set closed at
{A1, A2, J}, components (1) and (2) only, no
context term. Three candidates were generated and
ranked for ICS 196 — A1 (key1 2, key2 0.2593),
J (key1 0, key2 0.3148), A2 (key1 0, key2 0.1852) —
and the permutation null (B = 999, seed 109401)
returned a 99th percentile of 2 against the top
candidate's key1 of 2. **Verdict: RANKING NULL**
(registration §6's form): the ranked set is filed
as candidates with margins and full generation
provenance; the top rank is not distinguishable
from the null at the frozen bar. The preflight
record carries the disclosure of the first
execution's fail-closed stop and its correction;
every figure in this stage comes from the second,
complete execution (payload exit 0).

## 2. Test cases

- **TC-109-07 — Part 5 ranking conformance: PASS.**
  The independent verification
  (`records/stage-4-verify.py`, SHA-256
  `152c945d61b07c537676b20911676ade7ee57abaebdceec693727e92545ae898`;
  substring-enumeration alignment, derivation tables
  re-entered from the freeze) recomputed the ranking
  for ICS 196 from the filed candidate records under
  the registered lexicographic rule: exact agreement
  on pairings, anchored maps, implied endings, and
  both keys for all three candidates. The
  permutation null recomputes exactly (the full
  sorted distribution of the null maximum, and its
  99th percentile of 2), and the verdict is §6's
  mechanical consequence over the recomputed
  figures. The comparanda set equals the registered
  closed set with the (b) reduction stated on the
  freeze's face. The scan of Part 5's records for
  licensing language, any blanket statement that
  every check passed, and any resolution or
  presumption of OD-O-2 returned zero hits.
- **TC-109-03 — Replay conformance: PASS.** The
  stage's filed candidate records were selected
  from custody by their pins; the generation was
  replayed from the records (generator pin, null
  seed, data pins, constraint-set version), and the
  replayed candidate set and margins equal the
  filed ones exactly, for all three candidates.
  Together with the clause-S recomputation from the
  custody synthetic corpora (recoveries and shuffle
  recoveries reproduced per replication), the
  verification ran 31 of 31 checks PASS, payload
  exit 0.

## 3. TC-109-09 — Trace and standing discipline

The landing diff is confined to this spec's records
(the freeze, harness, verification script, raw
output, preflight, outcome, and this close record),
`tasks.md`, the history ledger, and PROGRAM-STATE.
No file of Specs 091, 093, 096, 098, 101, 102, 104,
105, 107, or any other study is touched; no gate is
altered; no standing, verdict, tally, anchor, or
ledger row in any program changed; no claim moved —
the stage's outcomes are recorded by these filings,
not by claims-ledger motion. The candidates filed
are candidates for no gate; no gate was run.
Nothing was deposited or published. OD-O-2 stands
where it stood: this stage's records neither
resolve nor presume it, and carry no licensing
language for Eteocypriot continuation.

## 4. TC-109-10 — Kill criteria evaluated (spec.md §9)

1. **Null yield at the frozen bar. Fired for Part 5
   in its registered form:** the part's best
   self-generated candidate (A1, key1 2) cannot beat
   the permutation null at the frozen bar (99th
   percentile 2) on the genuinely held-out forms.
   The outcome is filed (RANKING NULL); any revised
   search design — for example a ranking under the
   (b) comparanda, if those tables are ever filed
   complete — is a later registration; the bar was
   not revised.
2. **Preflight failure.** Not fired for Part 5:
   clauses N and S were met at the unchanged
   floors. (The criterion's Stage 1 and G1-revision
   firings stand where filed; Part 1 remains
   blocked at its generator.)
3. **Control failure.** Not fired: the preflight's
   shuffle control returned median recovery 0.167
   against 1.000 on the planted labels, and the
   permutation null is the ranking's own bar
   (criterion 1), not a control succeeding.
4. **Gate dependence.** Not engaged for Part 5,
   which has no registered input gate. It stands
   for Part 4 (Spec 102, unchanged) and for Part
   3's iconography sub-channel (Spec 100,
   unchanged).
5. **Integrity tripwire.** Not fired. All pins were
   verified fail-closed before use; the one harness
   defect (the inventory recomputation) was caught
   by the harness's own assertion before any ranking
   ran on it, and is disclosed on the preflight
   record's face; no unregistered analysis entered
   the record; custody terms held throughout
   (custody files uncommitted, statistics and
   records only).

## 5. Part states after Stage 4

- **Part 1 (assignment search): OPEN, BLOCKED at
  its generator** (unchanged by this stage; G1 and
  G1-R both stand failed at their re-preflights on
  the record, and the scale study's MIXED outcome
  stands; Stage 3 remains blocked).
- **Part 2 (structure induction): EXECUTED for the
  licensed families; verdict POSITIVE** (unchanged).
- **Part 3 (context channel): EXECUTED; verdict
  CHANNEL NULL; the term is withdrawn from this
  study's scoring** (unchanged; Part 5 ran without
  it, as registered).
- **Part 4 (gloss induction): GATED** (unchanged;
  Spec 102's G-1).
- **Part 5 (candidate ranking): EXECUTED; verdict
  RANKING NULL.** The ranked candidate set for
  ICS 196 is filed with margins and provenance.
  The part's registered outcome at comparanda (a)
  is complete; any further ranking requires a new
  freeze under the registration's discipline.

## 6. Custody table

Custody root: tower `glossa-custody/spec109/stage-4/`
(never committed).

| file | SHA-256 |
|------|---------|
| candidate-records.jsonl | `5fca69634b698673f892bf0e962ef074e0a3145632906bad9b7cebd26de5680a` |
| stage-4-raw-output-2026-11-27.json | `41b04510c956665ad8626f5243e21d000273a21d0653874a1dedb226fee3c474` |
| synth-1.json | `eceb00529f27f3603e41f353c21deb3f45c96282afa2c4c9ec383371995ecbf7` |
| synth-2.json | `a649eaa9151b8fdb873ef37457030b614abb2a0938d016e6b5c760acadf987b7` |
| synth-3.json | `f12626dda3777efe277fbc769114df43a1ba3b273b91dc3dfba28bcf30ce5f70` |
| synth-4.json | `4f1bcafcd9ee518d6cfc15e3c0cdd8dd75017efe1235d9c1579f6638db604012` |
| synth-5.json | `ffce817e22e19525b85b6f3912fe56afaf505ba9264633556af3869a8513e340` |

The raw output's copy in `records/` is byte-identical
to the custody original (SHA-256 verified at filing).
