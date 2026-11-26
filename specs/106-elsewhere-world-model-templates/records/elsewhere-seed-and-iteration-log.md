# ELSEWHERE Seed-and-Iteration Log — Spec 106

**Study:** Glossa-Lab Spec 106 — ELSEWHERE as a formal
framework, and the baseline world-model templates for the
Indus, Eteocypriot, and Meroitic programs.
**Framework:** ELSEWHERE Framework Specification, Version 1
(2026-11-25), `../framework.md`. **Log standard:** framework
§9; this log is also this study's history ledger in its
ELSEWHERE form under framework §10. This log is the study's first-class provenance record; the
path from seed to any claim's status must be rebuildable from
it alone.

---

## Seed entry (2026-11-25)

- **Study identity.** Glossa-Lab, Spec 106
  (`specs/106-elsewhere-world-model-templates/`), registered
  2026-11-25. Framework adopted: ELSEWHERE Framework
  Specification, Version 1.
- **Baseline templates seeded.** Three, version 1
  (2026-11-25), each carrying its own seed record in the
  framework §4 format inside the template file:
  `templates/indus-baseline.md` (88 axioms, domains 2–8;
  (F) 4, (K) 74, (H) 10; UNSOURCED-flag lines 0; axiom-line
  SHA-256 in the template's seed record),
  `templates/eteocypriot-baseline.md` (71 axioms; (F) 3,
  (K) 58, (H) 10; UNSOURCED-flag lines 3),
  `templates/meroitic-baseline.md` (76 axioms; (F) 4,
  (K) 62, (H) 10; UNSOURCED-flag lines 2). Domain 1 of each
  is carried by reference to Spec 105.
- **The claim queue as opened.** C106-1..C106-6, the
  registration claims of this spec (about the framework and
  the templates themselves; tested mechanically at
  registration by TC-106-01..TC-106-06, not inside instances).
  The instance claim queues of the three baselines open
  EMPTY, per their seed records: claims enter only by an
  authorizing act at the reasoning level, recorded here.
- **The evidence set.** Per baseline, as stated in its seed
  record (the program's corpus and fixed record), with Spec
  105's boundary gates as the registered language-internal
  contact points.
- **Authorizing orders.** The owner's orders in the
  Glossa-Lab chat of 2026-11-25, 12:39 ET (world-model
  expansion) and 12:44 ET (formal framework).

## Iteration entries

### Iteration 1 (2026-11-25) — Meroitic baseline template version 2 (Round G unit G-M-1)

- **What changed.** One baseline axiom line, in
  `templates/meroitic-baseline.md` only: MER-ENV-01 (K).
  Version 1 read "The Meroitic language was written only
  during the Kingdom of Meroe, c. 300 BCE – 350 CE, though
  the language itself is attested earlier in Egyptian
  transcriptions of personal names from as early as the
  second millennium BCE." Version 2 reads "Meroitic
  writing is attested during the Kingdom of Meroe,
  c. 300 BCE – 350 CE, and continued after its fall
  (MER-ENV-03); the language itself is attested earlier
  in Egyptian transcriptions of personal names from as
  early as the second millennium BCE." Source unchanged.
  The template's seed record stands as filed for
  version 1; the amendment is recorded in the template's
  Template amendment section.
- **Why.** The version 1 line's exclusive clause
  contradicts the template's own MER-ENV-03 (the script
  outlived the fall of Meroe; REM 0094 at Kalabsha
  re-dated to 410/450 CE) and MER-MOV-08 ("the last
  Meroitic text"). The Round G Meroitic Co-scientist
  session flagged it (unit G-M-1); its kill check (a
  binding scope rule confining MER-ENV-01 to a
  kingdom-period subset) was run at adjudication against
  the template, the framework, and the study records and
  was not met; the unit was sustained APPLY.
- **Pins.** Census unchanged: 76 axioms, (F) 4, (K) 62,
  (H) 10, UNSOURCED-flag lines 2. Axiom-line SHA-256:
  version 1 `eeadf46e336fa80d09bcffa2538d3cf4c32c8756fdb6150c817ff0b19cdb4cf4`
  → version 2 `ecabd227f7e767a3a740ece3b355d8620db476b89ac482d7a8386b483a97f4f2`,
  recomputed by the method of `records/census-audit.py`
  (TC-106-05; the audit passes in full on the amended
  file).
- **Effect.** None on any derivation or result: no
  instance has been spawned under this study from either
  version; Stage 1 (first ensembles) is not commissioned
  (spec.md §5). The correction is filed before first
  instantiation, as the unit directed.
- **Rests on:**
  `specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-25-round-g.md`
  §3.1; `templates/meroitic-baseline.md` (Template
  amendment — version 2).

### Iteration 2 (2026-11-26) — First ensemble: ETE-ENS-1, Eteocypriot baseline, claim ETE-Q-1

- **Authorizing act.** The owner's order in the Glossa-Lab
  chat, 2026-11-26 ~01:54 ET ("For everything else,
  execute now to your recommendations"), approving the
  recommendation as presented: commission Spec 106's
  Stage 1 with the framework's worked example, one claim,
  fully logged, before any wider set.
- **Seed.** `records/ensemble-1-seed-2026-11-26.md`,
  committed before any derivation ran. Baseline: the
  Eteocypriot template, version 1, axiom-line SHA-256
  `fca1cc8a238631b0c6df8b2901daa5e84dc4cb2387dcdad560285c6e95beec4f`,
  recomputed at the seeding by `records/census-audit.py`
  (TC-106-02..TC-106-05 PASS). Evidence set and checker as
  the template's seed record declares (Spec 096 corpus and
  the fixed epigraphic record; contact points: Spec 105's
  G-ETE gate, and the filed Eteocypriot record).
- **Claim entered.** "The long Amathus text is a royal
  dedication" entered the Eteocypriot baseline's claim
  queue as **ETE-Q-1**, under the act above; the queue had
  opened empty at the template's seeding. Status at entry:
  UNTESTED. The seed declares the study-level
  identification ("the long Amathus text" = ICS 196) and
  the translation (a royal dedication is an inscription
  whose dedicator is the king or royal house of Amathus
  and whose act is a dedication).
- **Instances spawned, declared before the pass.** Four,
  each the baseline entire with exactly the named
  difference. The baseline POL domain carries no (H)
  lines, so the politics variation takes the two forms
  framework §5 permits: **ETE1-A** + ETE-POL-H1 (added
  (H): in ICS 196's period, substantial public inscriptions
  at Amathus were normally commissioned by the king or the
  royal house; the norm itself UNSOURCED in the opened
  record); **ETE1-B** + ETE-POL-H2 (the civic alternative:
  normally commissioned by the city as a civic body);
  **ETE1-C** the baseline control, no addition, no drop;
  **ETE1-D** + ETE-POL-H1 with the named (K) axiom
  ETE-POL-11 dropped (declared sensitivity run: the
  kingship's end left undated and unended).
- **Verdicts, per claim per instance.** ETE-Q-1 —
  ETE1-A: DOES-NOT-DERIVE (gap: no axiom connects ICS 196
  to a royal dedicator; ETE-POL-H1 is a general norm and
  does not distribute to a text whose filed content names
  another dedicator); negation DERIVES (ETE-CON-03 with
  the seed's translation). ETE1-B: DOES-NOT-DERIVE (same
  gap); negation DERIVES. ETE1-C: DOES-NOT-DERIVE (same
  gap); negation DERIVES. ETE1-D: DOES-NOT-DERIVE (same
  gap; dropping ETE-POL-11 adds no premise about ICS 196);
  negation DERIVES (the chain nowhere cites ETE-POL-11).
- **Evidence applied.** Contact point 2 (the filed
  Eteocypriot record: ETE-CON-03, ETE-CON-04, ETE-ENV-03)
  was exercised for every instance: each negation
  derivation agrees with it, and no instance derived a
  contradiction with the evidence set. Contact point 1
  (Spec 105's G-ETE gate) was not exercised — the pass ran
  no language-internal derivation — and no G-ETE score is
  claimed from this pass.
- **Retirements.** No instance died. All four retired at
  the close of the pass, claim queue exhausted, their
  records kept in the outcome record.
- **Ensemble reading.** Survivors 4 of 4; translatable in
  4 of 4; claim derived in 0 of 4; negation derived in 4
  of 4. Under §8.1's row for that tally: **ETE-Q-1 —
  REFUTED-IN-ENSEMBLE**. §8.2 governs the positive row
  only and is not engaged; coverage was complete in any
  case. The claim's fate does not track the politics
  variation: it fails identically at every corner of the
  declared space, killed by the filed content of the text
  itself (ETE-CON-03), not by any politics premise. The
  next evidence that could bear is the outstanding
  edition-of-record check on that content (ETE-ENV-04:
  the program holds ICS 196 from secondary reproductions,
  not Masson's edition or the Sittig 1914 photograph; the
  portion-copy request is unanswered).
- **Rests on:** `records/ensemble-1-seed-2026-11-26.md`;
  `records/ensemble-1-outcome-2026-11-26.md`.

### Conformance note on Iteration 2 (2026-11-26, Round N unit N-E-1)

Appended at the landing of the Round N adjudication
(Spec 091 records,
`coscientist-sweep-adjudication-2026-11-26-round-n.md`
§3.1). The ensemble's contact point 2 exercised
ETE-CON-03, ETE-CON-04, and ETE-ENV-03, which are axioms
in every declared instance of ETE-ENS-1, against the
framework's §2/§6 rule that the evidence set is not an
axiom of any instance and no instance treats a checker
item as derivable. The contact's agreement is therefore
recorded as an inherited-premise consistency check, not a
separate evidentiary test. ETE-Q-1's REFUTED-IN-ENSEMBLE
stands as a conditional logical result under the seed's
declared translation; the full note is appended to
`records/ensemble-1-outcome-2026-11-26.md` at the same
landing. Any consistency-only contact distinction is
prospective registration only.

## Solution register

No claim carries SOLUTION status. C106-1..C106-6 are
registration claims about this package, settled by their test
cases at registration; no instance-tested claim exists.

**Register update (2026-11-26, Iteration 2).** The first
instance-tested claim now exists. ETE-Q-1, "The long Amathus
text is a royal dedication" (Eteocypriot baseline claim
queue, ensemble ETE-ENS-1): **UNTESTED → REFUTED-IN-ENSEMBLE**.
No claim carries SOLUTION status.
