# Spec 093 Stage 4 — T402 material pass freeze v1

**Frozen 2026-11-27, before any computation under it.**
This freeze states the material pass's population, its
field as recorded, its floors, and the rule that decides
whether the pass can be administered at all. A pass
whose frozen floors fire does not run: it records
CANNOT BE ADMINISTERED with the forcing counts
(C093-8), and no threshold in this record may be
adjusted to convert that stop into a pass.

## 1. Pins and premise

- Join output: `records/t103-join-pairs-v1.jsonl`,
  SHA-256 `7107f738832a4e3b04cff91d81073212bc0f3a77afed6f0ccc3cee4fce621703`
  (179 pairs; key family K2 accepted at precision 1.000
  against its freeze's 0.90 floor — D-093-4's join gate
  is met, `records/t103-join-audit-2026-11-06.md` §3).
- **The standing bound, stated as Stage 2's record
  directs:** material class carries **no independence
  standing** from Stage 2 — it was NOT ADMINISTERED
  there, at the forcing counts this freeze inherits
  (`records/stage2-record-2026-11-19.md` §4: "Stage 4's
  material pass (T402) inherits a field with no standing
  from this stage, and its own freeze must state that
  bound rather than borrow strength this stage did not
  establish"). Had this pass run, its statements would
  have been bookkeeping statements about the record
  system, not channel evidence (FR-093-04).

## 2. Population and field

Population: P-join, the 179 joined pairs. Field:
material class as recorded on the join output — the
CISI data list's material value (`material_raw`; 23
distinct raw values), in the class form Stage 2's
freeze counted: **Steatite 176, Clay 1, Faience 1, and
1 pair carrying no value, of 179.** (The T102 register
is bound to the snapshot's values and does not cover
the data list's; the field is taken as recorded, per
the T201 definition §2.2 and the T103 audit §5.)

## 3. Floors

- **Class floor: 10 records** (the Stage 2 freeze v1
  precedent for this same field on this same
  population).
- A material-conditioned pass — sequence behavior
  conditioned on material class, per plan.md Stage 4(b)
  — requires **at least 2 classes at or above the
  floor**: conditioning on a single class compares
  nothing.

## 4. The administration rule

Before any outcome is recorded, the §2 counts are
recomputed from the pinned join output by
`tools/spec093/count_stage4_material.py` (presence and
class counting only — no sequence property is computed)
and checked against this freeze. If the counts do not
reproduce, the administration refuses and no outcome is
taken. If they reproduce:

- if at least 2 classes meet the floor, the pass is
  administered under a successor freeze stating its
  quantities, controls, and bar (this freeze registers
  the gate, not the pass design, because the gate is
  what the filed counts put in question);
- if fewer than 2 classes meet the floor, the pass's
  outcome is **CANNOT BE ADMINISTERED**, with the
  forcing counts on the face of its outcome record:
  Steatite 176 alone at or above the floor of 10; Clay
  1 and Faience 1 below it; 1 pair empty; 179 total.
  The raw-value form agrees: of the 23 distinct raw
  values, only the steatite value's count reaches the
  floor.

## 5. Statement strength

The CANNOT BE ADMINISTERED outcome, if it fires, is a
finding about the record system's present contents:
the one audited join the program holds delivers a
material field with a single usable class, so no
material-conditioned sequence statement exists to be
tested — at any bar, under any controls. It asserts
nothing about material practice in the world.

*This does not establish:* anything about material
practice in the world if it stops — a stop is a finding
about the record system, stated at its counts. (T402's
line, carried verbatim.)
