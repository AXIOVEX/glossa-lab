# Spec 100 — The Motif-Claims Rerun: Recomputing the 13 Animal-Motif Claims From a Deposited Per-Seal Iconography Join

**Status: REGISTERED 2026-11-22 — EXECUTION GATED.** The design
in section 3 and the preregistration record
(`records/preregistration-2026-11-22.md`) are frozen as of
this package's landing. Execution (Stages 1–2 of `tasks.md`)
does not begin until the gate of section 4 opens; any change
to a frozen parameter is a new registration version,
recorded, never a silent edit.

**Provenance.** The Co-scientist refresh adjudication of
2026-11-22 (PR #673;
`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`),
unit I-21, proposed: deposit the per-seal iconography labels
for the 1,670-seal population with provenance, missing-label
handling and the seal-ID join; replay the 13 claims at their
original thresholds before any revised exploratory tests;
keep M063's failed specification visible. The owner's OD-5
act (2026-11-22 11:36 ET) disposed it: **the rerun is
authorised; the per-seal iconography deposit is held until
William Miller Sr's reply** on the program's 2026-11-20
Holdat permission letter (Gmail 1a1fb36478ee78e4), which the
hourly indus-reply-watch monitors under flag F-1. This
package is the registration that act ordered: the study is
registered, its pipeline is built and proven in custody, and
its execution waits on the gate.

## 1. What this spec is

A single recomputation study over one frozen population.
The motif/numerical evidence record of 2026-11-21 (PR #634;
`specs/091-anchor-comparison-integrity/records/motif-numerical-evidence-2026-11-21.md`)
found all 13 animal-motif claims **NOT REPRODUCIBLE FROM THE
RECORDS**: every historical motif script read the Holdat
corpus's `iconography` column, that file is gitignored and
absent from the repository, and no tracked file joins
per-seal sign sequences to per-seal motif labels over the
population, so the contingency cells, lifts, and odds ratios
behind the claims were never computable from the record.
That record named the closing act: deposit, as a tracked
repo record, the per-seal iconography labels for the
1,670-seal population joined on the same seal ids the sign
files use, after which every table is a mechanical count.
This spec registers that closing act's study: the deposit
(Stage 1, gated) and the rerun over it (Stage 2, gated on
Stage 1).

The rerun reports, per claim, exactly one verdict from the
frozen vocabulary of section 3.5. It changes no standing, no
anchor, and no other program record (claim C100-4).

## 2. The grounding, as measured at registration time

From PR #634's record, replicated there by two independent
paths over two corpus representations with exact agreement:

- Population: 1,670 seals (`outputs/phase100_full_corpus.json`
  and `outputs/phase114_full_seal_translations.json`, both
  keyed by `cisi_id`).
- The 13 claims, their filed motifs, and their replicated
  sign marginals (seals bearing the sign):

  | Sign | Reading | Filed motif | Sign seals |
  |---|---|---|---|
  | M006 | puli | tiger | 15 |
  | M013 | nakaram | gharial | 23 |
  | M016 | kaḷiṟu | elephant | 23 |
  | M039 | āṉai | elephant | 18 |
  | M045 | yānai | elephant | 24 |
  | M057 | māṭu | zebu | 18 |
  | M060 | kāṇṭāmirukam | rhinoceros | 20 |
  | M062 | erutu | zebu | 28 |
  | M063 | mutalai | gharial | 18 |
  | M067 | kōṭṭāṉ | rhinoceros | 15 |
  | M068 | maṟi | rhinoceros | 13 |
  | M073 | kōṉ | zebu | 25 |
  | M080 | vēṅkai | tiger | 19 |

- The filed basis for 12 of the 13 is the anchor file's
  summary assertion "Exclusive to <animal> seals
  (lift > 5.0)" (`backend/reports/INDUS_FINAL_ANCHORS.json`);
  no contingency table was ever filed behind it. The claims'
  own filed threshold is therefore **lift > 5.0**.
- **M063's filed correction stands separately:** the anchor
  basis (2026-05-11) states M063 appears on 3 of 18
  gharial-motif seals with lift 4.35 against the original
  5.0 threshold (and also 4 unicorn and 3 zebu-bull seals).
  The 18 (the sign total) is replicated; the 3/4/3 split and
  the 4.35 could be neither confirmed nor contradicted from
  the records. T302 confirmed as not rerunning the motif
  claim. In this study M063 is replayed like the other 12,
  and its filed 4.35 stays visible as a failed specification
  whatever the rerun finds (claim C100-2). The filed figures
  also calibrate the frozen lift formula: with a = 3,
  a+b = 18, a+c = 64, N = 1,670, lift = aN/((a+b)(a+c)) =
  4.35 to two places — the only filed lift value in the
  record, reproduced by TC-100-03.

  *Correction note (2026-11-22, Red Team Round 6, RT6-M7;
  original text above preserved):* the phrase "3 of 18
  gharial-motif seals" in this section mislabels the
  denominator: 18 is the sign total (a+b), and the
  gharial-motif total (a+c) is 64. Corrected wording:
  "3 of its 18 seals carry the gharial motif (gharial-motif
  seals total 64)".
- The competing-word structure stands as filed and is
  untouched: an association table tests motif association
  only, not which word is right (PR #634, section 3).

## 3. The frozen design

### 3.1 The deposit

The deposit is a tracked CSV at
`specs/100-motif-claims-rerun/records/iconography-deposit-v1.csv`,
columns `cisi_id,iconography`, one row per covered seal,
produced by `tools/deposit_extract.py` from the Holdat
corpus build of record and landed with its own deposit
record stating, on its face: the source build's identity
and SHA-256, the permission basis (Miller's reply, cited),
the coverage (rows for how many of the 1,670 population
seals), and the extraction's date and venue. The deposit
record is a Stage 1 landing; it does not exist at
registration.

**Pin.** The corpus build of record is the build the T303
run used, SHA-256 `62d14d2b…` as pinned in the program's
records. The extractor refuses any source whose full
SHA-256 does not equal the pin supplied from the deposit
record (TC-100-06). At registration time the pinned build
is **not held on the execution venue** (the F-4 study
package of 2026-11-22 records the same: the pinned Holdat
corpus was not held on tower-compute, and its from-raw
permutation leg could not be recomputed there). The
deposit act therefore begins by producing the pinned bytes
in custody and verifying the pin; if the pinned bytes
cannot be produced, the deposit cannot be made under this
spec and that failure is itself recorded.

  *Amendment (2026-11-22, Red Team Round 6, RT6-H3;
  original text above preserved, the one sentence noted
  below superseded):* the full pin of record is
  `62d14d2bebf7c2c80d98a2958e75ec52bff3f240ff3f5e85d1f7f40cbe28218e` (64 hex characters). Its source is the program's
  records, the T303 build record carried in
  `reports/phase422_results.json`, and NOT the deposit
  record, which is created after extraction and cites the
  pin. The sentence above stating that the extractor
  refuses a source whose SHA-256 "does not equal the pin
  supplied from the deposit record" is superseded: the pin
  is embedded as a constant in `tools/deposit_extract.py`;
  a supplied `--pin` must equal that constant or the tool
  refuses, and with no `--pin` the tool uses the constant
  (TC-100-06 as amended).

### 3.2 The join

The join key is `cisi_id`, the identifier both tracked
population files and the historical Holdat-derived scripts
use (`cisi_number` in the source CSV). The join is exact:
a deposit row joins the population seal of the same id; a
population seal with no row is missing (section 3.4); a
deposit row for an id outside the population is a deposit
defect, reported by the deposit record's coverage check,
and the pipeline raises on it at execution (the run's
outcome is the defect, not a table).

### 3.3 Motif match, lift, odds ratio

- **Motif match** (the historical scripts' rule, frozen):
  a seal carries motif M when M's token — one of `tiger`,
  `gharial`, `elephant`, `zebu`, `rhinoceros` — appears in
  the seal's iconography string, lowercased.
- **Cells.** For claim (sign S, motif M) over the labeled
  population: a = S present, M present; b = S present,
  M absent; c = S absent, M present; d = S absent, M absent.
- **Lift** = a·N / ((a+b)·(a+c)), N the labeled population.
  Undefined (reported as null) when a+b or a+c is zero.
- **Odds ratio** = ad/bc, reported as undefined (null)
  where b or c is zero.
- **Two paths.** Every quantity is computed independently
  over the phase100 (path A) and phase114 (path B)
  representations. The outcome stands only where the two
  paths agree exactly, cell for cell; a disagreement is
  itself the reported outcome (pipeline exit 4).

### 3.4 Missing labels

Frozen before the deposit exists (claim C100-5): a
population seal with no deposit row is missing, excluded
from every cell, and the outcome restates its denominator
as the labeled population on its face. A deposit row with
an empty iconography string is a recorded no-motif label
and counts as motif-absent for every motif. No label is
imputed, inferred, or carried from any other source.

### 3.5 Verdict vocabulary

Per claim, exactly one of:

- **REPRODUCED** — the recomputed lift exceeds the filed
  threshold (lift > 5.0) over the labeled population.
- **NOT REPRODUCED** — any other recomputed result,
  including an undefined lift.

The verdicts judge the filed assertions as computations.
They are evidence records; consequences for any reading's
class go through a separate adjudication act (C100-4).

## 4. The gate

Execution is gated on the per-seal iconography deposit.
The deposit is HELD on the owner's order (OD-5 act,
2026-11-22 11:36 ET) until William Miller Sr's reply to
the program's 2026-11-20 Holdat permission letter (flag
F-1) is reported by the indus-reply-watch. On a reply
granting the basis, the deposit is made as a tracked
record and the rerun then executes under this
registration. On a refusal, this study closes as GATE
REFUSED and no execution on Holdat-derived labels occurs
under it. While the gate is closed, the pipeline of
record refuses record-mode execution (exit 3, GATE
CLOSED) and no rerun result is computed for the record.

## 5. Execution protocol (when the gate opens)

1. **Deposit act (Stage 1).** Produce the pinned corpus
   bytes in custody; verify the full SHA-256 against the
   pin of record; run the extractor; land the deposit CSV
   with its deposit record (provenance, permission basis,
   coverage, the join-defect check of section 3.2) by pull
   request under the program's CI discipline.
   The deposit record's permission basis takes the
   labelled form defined here (RT6-C2 amendment,
   2026-11-22): a line beginning `Permission basis:`
   followed by a statement naming a granting Miller reply
   as its basis, and the record must also state the
   deposit CSV's SHA-256. `tools/motif_rerun.py` enforces
   this mechanically in record mode: the basis line must
   contain a granting term (for example "grants",
   "granted", "granting", or "confirms permission") and
   must contain no refusal term (for example "refus",
   "deni", "silence", "silent", "no reply", "not
   granted", or "withheld"); a line recording refusal or
   silence does not satisfy the gate.
2. **Rerun (Stage 2).** Run `tools/motif_rerun.py` in
   record mode against the landed deposit, on
   tower-compute, in a fresh clone. The run's own exit code
   is its payload verdict. Land the outcome record
   (full tables for all 13 claims, both paths' agreement
   stated, the labeled-population denominator on its face,
   M063's filed figures carried beside its recomputed row)
   by pull request.
3. **Consequences (Stage 3).** None in this spec. Any
   adjudication the outcome informs is a separate act.

## 6. What this spec does not do

It does not deposit anything, compute any claim's cells
from real labels, or produce any rerun result at
registration. It does not touch the three numerical claims
of PR #634 (computed and WEAKENED there; not motif
claims). It does not revive the Spec 024 motif arm (closed
2026-10-09) or use the Phase-134/135 pilot codings, which
cannot be joined to signs. It authorises no external send:
the only correspondence in its gate is the 2026-11-20
letter already sent, whose reply is Miller's move.
