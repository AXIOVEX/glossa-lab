# Spec 100 — Preregistration and Design Freeze (2026-11-22)

This record freezes the motif-claims rerun before the
deposit exists and before any per-seal iconography label
has been joined to any sign under this study. Everything
the rerun will compute, and the exact rules it will
compute by, are stated here and in spec.md section 3;
execution (Stages 1–2) is gated (section 4 below) and any
change to a frozen parameter is a new registration
version, recorded, never a silent edit.

## 1. Registration act

Adjudication unit I-21 of the Co-scientist refresh
adjudication (PR #673, landed 2026-11-22) proposed the
deposit and the rerun. The owner's OD-5 act (2026-11-22
11:36 ET, Glossa-Lab chat) disposed it in two parts: the
rerun is **authorised**; the per-seal iconography deposit
is **held** until Miller's reply. This package is the
registration that act ordered (D-100-1: at the check of
2026-11-22, the highest landed spec package on origin/main
was 099, no 100 directory existed, and no branch or open
pull request carried 100; this package takes 100).

## 2. The frozen population and claims

Population: the 1,670 seals of
`outputs/phase100_full_corpus.json` (path A) and
`outputs/phase114_full_seal_translations.json` (path B),
keyed by `cisi_id`, as replicated by PR #634.

The 13 claims, exactly as filed (sign, reading, filed
motif, replicated sign marginals):

| Sign | Reading | Motif | Sign seals |
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

Filed threshold for every claim: **lift > 5.0** (the
anchor file's "Exclusive to <animal> seals (lift > 5.0)").
M063's filed corrected figures (3 of 18 gharial-motif
seals, lift 4.35; also 4 unicorn and 3 zebu-bull seals)
are carried on the face of the outcome record beside its
recomputed row, whatever the rerun finds.

## 3. The frozen definitions

- **Join key:** `cisi_id`. A deposit row keyed outside
  the population is a defect; the run's outcome is the
  defect (pipeline exit 5).
- **Motif match:** the claim's motif token (`tiger`,
  `gharial`, `elephant`, `zebu`, `rhinoceros`) appears in
  the seal's iconography string, lowercased — the
  historical scripts' rule.
- **Cells:** a = sign present, motif present; b = sign
  present, motif absent; c = sign absent, motif present;
  d = sign absent, motif absent; over the labeled
  population only.
- **Lift:** a·N / ((a+b)·(a+c)), N the labeled
  population; null when a+b or a+c is zero.
- **Odds ratio:** ad/bc; null ("undefined (zero cell)")
  where b or c is zero.
- **Missing labels:** no deposit row → excluded from
  every cell, denominator restated as the labeled
  population on the outcome's face; empty iconography
  row → recorded no-motif label (motif-absent); no
  imputation.
- **Two paths:** all quantities computed over both
  representations; the outcome stands only on exact
  agreement, cell for cell; disagreement is the outcome
  (pipeline exit 4).
- **Verdicts:** REPRODUCED when lift > 5.0, otherwise
  NOT REPRODUCED (including an undefined lift). One
  verdict per claim, from this vocabulary only.
- **Deposit format:** CSV, columns `cisi_id,iconography`,
  one row per covered seal, iconography as the source
  records it (stripped, lowercased), produced by
  `tools/deposit_extract.py` from the pinned corpus
  build (SHA-256 `62d14d2b…`, the T303 build), the full
  pin verified at extraction or the extractor refuses
  (exit 2).
- **Pipeline of record:** `tools/motif_rerun.py` and
  `tools/deposit_extract.py` as committed in this
  package; their SHA-256s at registration are recorded
  in `records/tc-execution-2026-11-22.md`.

## 4. The gate statement (verbatim, as registered)

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

## 5. State at registration

- Registered: the spec package, its seven claims
  (C100-1..C100-7, intaken at adoption), this freeze.
- Proven in custody: the six test cases and the
  end-to-end proof run (synthetic labels), payload
  verdicts in `records/tc-execution-2026-11-22.md`.
- Not done, by design: no deposit (no deposit file
  exists in this package), no join of real labels, no
  rerun result of any kind.
- Not held on the venue: the pinned Holdat corpus build
  (see spec.md section 3.1); the deposit act begins by
  producing and pin-verifying those bytes in custody.
- The trigger is watched: the indus-reply-watch already
  covers Miller/Holdat correspondence under flag F-1;
  its report of the reply is the gate event of record.
