# Spec 100 — Claims

Every claim carries at least one falsifier (a concrete
observation that would show it false) and a "does not
establish" line (the over-reading it forbids), per the
program's claims discipline. The same set, normalized into
`aee-claims.json` without substantive change, is the claims
bundle of record for this package, intaken into the
canonical ledger at adoption. The design every claim binds
was frozen before the deposit exists and before any label
was joined (`records/preregistration-2026-11-22.md`).

**C100-1**

Nothing is computed for the record before the deposit: the rerun executes only over a per-seal iconography deposit that is itself a tracked record in this repository, stating its provenance and permission basis on its face; while the deposit is held under flag F-1, the pipeline of record refuses record-mode execution, and no rerun table, lift, or odds ratio for any of the 13 claims exists as a program result.

*Falsifier:* A rerun outcome record, table, or figure dated before the deposit record's landing; a record-mode pipeline run exiting 0 without a deposit file present; a deposit record that does not state provenance and permission basis.
*Does not establish:* That the gate's closure says anything about whether the claims are true; it governs only when they may be tested.

**C100-2**

The rerun replays the 13 animal-motif claims exactly as filed: the 1,670-seal population of the tracked corpus files, the filed motif for each sign (backend/reports/INDUS_FINAL_ANCHORS.json: "Exclusive to <animal> seals (lift > 5.0)"), the filed threshold lift > 5.0, and the frozen motif-match and lift definitions of spec section 3; no revised threshold, revised motif assignment, or exploratory test is part of the rerun of record, and M063's filed corrected figures (3 of 18 gharial-motif seals, lift 4.35 against the 5.0 threshold) remain visible as a failed specification whatever the rerun finds.

*Correction note (2026-11-22, Red Team Round 6, RT6-M7; original claim text above preserved):* the phrase "3 of 18 gharial-motif seals" mislabels the denominator: 18 is the sign total (a+b), and the gharial-motif total (a+c) is 64. Corrected wording: "3 of its 18 seals carry the gharial motif (gharial-motif seals total 64)".

*Falsifier:* A rerun table computed on a different population, threshold, or motif assignment; a revised-threshold figure presented as the rerun's verdict; the M063 row omitting its filed 4.35.
*Does not establish:* That a reproduced association would pick the right word among competing readings for the same animal; the tables test association only.

**C100-3**

Every number in the rerun outcome is a mechanical count over the deposited join and the tracked sign files, computed by the pipeline of record (tools/motif_rerun.py): the full 2x2 cells per claim, lift = a*N / ((a+b)(a+c)), odds ratio = ad/bc (reported as undefined where b or c is zero), computed independently over the phase100 and phase114 representations, and the outcome stands only where the two paths agree exactly, cell for cell.

*Falsifier:* A cell, lift, or odds ratio not derivable from the deposit plus the tracked files by the registered formulas; a path disagreement carried into the outcome without being the reported result.
*Does not establish:* That mechanical reproducibility makes the underlying labels correct; label accuracy is the deposit's provenance question, not this claim's.

**C100-4**

The rerun reports motif association only: it establishes no phonetic reading, supports no anchor, and changes no standing, ledger entry, or register value by itself; any consequence for a reading's class goes through a separate adjudication act citing this study's outcome record.

*Falsifier:* A standing, ledger, or register change citing this spec's outcome without its own subsequent act.
*Does not establish:* Anything about the 13 readings' phonetic values, in either direction.

**C100-5**

Missing-label handling is frozen before the deposit exists: a population seal with no row in the deposit is missing, is excluded from every cell, and the outcome restates its denominator as the labeled population; a deposit row with an empty iconography string is a recorded no-motif label and counts as motif-absent; no label is imputed, inferred, or carried from any other source.

*Falsifier:* An imputed label in the deposit or the computation; an outcome table whose cells sum to 1,670 while the deposit covers fewer seals, without the restated denominator on its face.
*Does not establish:* That missingness is random; the outcome reports the labeled population it actually covers.

**C100-6**

The deposit's trigger of record is William Miller Sr's reply to the program's 2026-11-20 permission letter (Gmail 1a1fb36478ee78e4), as reported by the indus-reply-watch under flag F-1: a reply granting the statistics-and-deposit basis opens the gate; a refusal closes this study as GATE REFUSED with no execution on Holdat-derived labels; silence leaves the gate closed. Any substitute basis (a fresh iconography coding under a measurement basis meeting its own gates) is a new study, not an execution of this one.

*Falsifier:* Execution on Holdat-derived labels before a granting reply is on record, or after a refusal; a GATE REFUSED closure recorded while a granting reply stands unexecuted without its own act.
*Does not establish:* That Miller's reply, either way, judges the corpus's scholarly quality; it governs permission only.

**C100-7**

The pipeline of record is the committed implementation in this package's tools/, proven before the deposit exists by the test cases of record executed on tower-compute (records/tc-execution-2026-11-22.md) and by an end-to-end proof run over synthetic labels keyed to the real population; the proof computes no claim's cells, lift, or odds ratio from real labels, and its outputs are marked PROOF - NOT A RESULT wherever they persist.

*Falsifier:* A proof output containing any claim's statistics computed from real iconography labels; a pipeline behaviour in the rerun that the test cases do not exercise.
*Does not establish:* That a proven pipeline makes the future rerun's outcome correct; it makes it mechanical.
