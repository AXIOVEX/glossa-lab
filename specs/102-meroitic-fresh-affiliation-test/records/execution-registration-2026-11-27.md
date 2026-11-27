# Spec 102 — Execution Registration and Armed State (2026-11-27)

## 1. What this record is

This record files the execution registration of Spec 102
under the owner's commission of 2026-11-27, states the
gate sequence exactly as the spec registers it, files the
book 1 digitisation protocol, records the machinery built
in preparation, and records the study's ARMED state. It
alters no gate, threshold, definition, or vocabulary in
spec.md. It is not a freeze: no concept list is frozen by
it, no seed is registered by it, no power figure is
computed by it, and nothing is scored by it.

## 2. The commission and its provenance

- The owner, Tristen Pierson, commissioned the Spec 102
  affiliation test in the Glossa-Lab chat on 2026-11-27
  (04:05 ET: "Yes do all these things now or take my
  approval now to do at the best time"), answering the
  status report that named the test among the items
  awaiting his commission. This is the fresh owner
  commission spec.md §6 requires for execution; the
  registration of 2026-11-22 (OD-21) authorized design
  and registration only and expressly did not supply it.
- The S-1 acquisition the spec separately owner-gated
  was executed under the owner's acts of 2026-11-26
  (acquisition record, §§10–11): book 2 acquired and its
  Appendix held in custody; book 1 ordered and in
  transit.
- The S-1 preparation record
  (`records/s1-preparation-record-2026-11-27.md`, PR
  #776, merge 51a3cfb2) measured the source state this
  registration rests on. Its statement that the test is
  "NOT commissioned" was true when filed and is
  superseded by this record; the preparation worker's
  PROGRAM-STATE text is corrected in the same motion as
  this landing.

## 3. The measured state this registration rests on

From the preparation record, verbatim in substance:

- The Rilly & de Voogt 2012 Appendix is the concept
  frame and NES-side apparatus of S-1 only. It prints
  no Meroitic form for any of its 200 concepts, so
  usable scored concepts from the Appendix alone are
  **0**, and **G-1 is NOT MET from book 2 alone** —
  short by 40 scored concepts in each family test and
  by 20 outside-the-twelve concepts in each test. That
  is a pre-freeze measurement, not the gate: by
  registration the gate is computed at the freeze
  (TC-102-01).
- The Appendix covers **82 of the 100 ASJP concepts**
  (79 at the label tier, 3 more by enumerated loose
  synonyms), **all 12 of the Stage 4.2 twelve** among
  them, and does not cap G-1: if book 1's digitisation
  yields attested Meroitic forms for at least 40 of
  those 82 concepts, at least 20 of them outside the
  twelve, G-1's arithmetic is satisfiable.
- The Meroitic side of S-1 is book 1: Rilly 2010,
  *Le méroïtique et sa famille linguistique* (Peeters,
  ISBN 978-90-429-2237-2), print copy in transit
  (order reference 6b0851920a66f, €55.00 total, ordered
  2026-11-26; Peeters gave no delivery date or
  estimate). Its load-bearing contents are the lexique
  (pp. 114–147), the 200-term NES apparatus
  (pp. 420–529), and Chapter III's comparison of 43
  Meroitic words (pp. 59–156).

## 4. The gate sequence, exactly as registered

The sequence below is spec.md's own, restated without
alteration. Where the preparation brief's summary and
the spec's text could differ, the spec governs; no
conflict between them was found.

1. **Stage 1 completion — S-1 digitised (T101).** Book
   1 digitised under the protocol of §5 below; book
   2's Appendix material already extracted in custody
   (preparation record). Per-entry source apparatus
   (author, year, pages) is carried, in the gold
   lexicon's form. TC-102-05 (custody sweep) applies.
2. **Stage 2 — vocabulary build and attestation
   (T201).** The digitised wordlist is mapped under a
   complete gloss→ASJP-concept table; every Meroitic
   form in the digitised S-1 wordlist whose gloss maps
   to an ASJP concept enters the candidate vocabulary,
   spelling variants kept as distinct forms (no
   spelling normalization; only case-folding and the
   registered diacritic fold, spec §3.2). The
   attestation filter then runs against the S-2
   corpus (Kovetsky build, pin `145af083…`): a form
   enters the scored vocabulary only if attested as a
   token in S-2; forms failing attestation are
   excluded, counted, and listed in the freeze. Any
   corpus-derived work uses the §3.6 split
   construction as amended (exact-text deduplication
   first; SHA-256(salt ‖ 0x00 ‖ UTF-8(text)) mod 10;
   residue 0 is the development/derivation side),
   under a study-specific salt registered in the
   freeze.
3. **Stage 3 — freeze and gates (T301).** The freeze
   files, in full, before any scoring (spec §3.8): the
   complete mapping table; the per-concept
   denominators for each test (Meroitic forms,
   comparator forms, attesting S-2 texts per concept);
   every gloss label verified against ASJP
   `parameters.csv` under its pinned hash; and a
   single integer seed registered before any scoring,
   from which all simulation streams derive
   deterministically (§4 amendment, RT6-M11 (d)).
   On the frozen material the gates are computed and
   filed before any scoring:
   - **G-1 (material), TC-102-01:** the frozen
     attestation-filtered vocabulary scores at least
     **40 concepts in each family test**, of which at
     least **20 lie outside the Stage 4.2 twelve** in
     each test (spec §3.7). Concept sets are per-test
     (spec §3.2).
   - **G-2 (power):** the freeze's design-time
     simulation, by the method of spec §4 as amended
     (RT6-M11) — injection over the actual frozen
     lists by the registered construction (for each
     scored concept independently, designation as
     corresponding with probability θ, and with
     probability d the appending of one comparator
     form built from a Meroitic skeleton of that
     concept with a trailing "a"), **4,000 replicates
     per (θ, d) cell**, the bar at the permutation
     null's **99th percentile**, the prospective
     binomial bound (q0 = 0.1255, per-test α ≤ 0.005)
     stated alongside — shows at least **80% power
     at θ = 0.30, d = 0.75** for the primary statistic
     T in **each** family test.
   - **A gate failure at G-1 or G-2 closes the study
     NOT ADMINISTERED** at this stage, with the
     failing gate and the counted shortfall on the
     record (spec §3.7; claim C102-3). A NOT
     ADMINISTERED closure is not a verdict on
     affiliation and may not be cited as one. No gate
     may be lowered by amendment at any point after
     the 2026-11-22 registration (§3.7 amendment,
     RT6-L4); a design needing lower gates is a new
     registration. TC-102-01, TC-102-02, TC-102-04
     apply at this stage.
4. **Stage 4 — scoring (T401), only on both gates
   passing.** Leg A scored as registered (spec §3.2):
   primary statistic T per family test (R1 Nubian/
   Nara set; R2 Afroasiatic set), the joint
   permutation null at 100,000 permutations under the
   freeze's seed, pass bar Holm-adjusted permutation
   p below 0.01 across the two-test family; the Stage
   4.2 twelve scored and reported as the comparability
   subset under both T and the frozen binary S,
   carrying no verdict of its own (spec §3.3); Arm R
   computed and filed separately as exploratory, never
   decisive, never pooled (spec §3.4); the run
   executed twice with byte-identical outcomes and an
   independent recomputation (TC-102-03). Leg B is
   recorded as executed only on a filed OD-14
   clarification covering the use, and otherwise as
   NOT ADMINISTERED (custody gate) at Stage 5; Leg A's
   verdict stands alone either way (spec §3.5).
5. **Stage 5 — outcome (T501).** The outcome stated
   only in spec §5's vocabulary (SUPPORTED / NOT
   SUPPORTED at its registered bar / NOT
   ADMINISTERED; R3 only as not displaced), with the
   consistency boundary in numbers; the adjudication
   package prepared for the owner's approval act. No
   ledger standing for C102-1..C102-5 is set by any
   stage of this study except through a recorded
   adjudication by a named human approver (spec §6).

## 5. Book 1 digitisation protocol

Filed here, executed when the trigger of §7 fires.

1. **Custody on arrival.** The print volume goes to
   the Spec 102 custody home on tower-compute
   (`~/.syncyard/worktrees/glossa/glossa-custody/spec102/`)
   on arrival. The arrival is recorded in the custody
   note and appended to the acquisition record:
   delivery date, the volume's bibliographic identity
   checked against the order (Rilly 2010, Peeters,
   ISBN 978-90-429-2237-2, order reference
   6b0851920a66f), and its physical completeness
   (the lexique, apparatus, and Chapter III pages
   present).
2. **Page imaging.** The lexique (pp. 114–147), the
   NES apparatus (pp. 420–529), and Chapter III's
   compared-word pages (pp. 59–156) are imaged in
   custody. Images and every digitisation product
   stay in custody and are never committed: the
   compilation is the program's own work over
   published sources under OD-14 Element 7, with no
   redistribution of the lexicon text and
   scoring/aggregate use only.
3. **Checked transcription (the load-bearing step).**
   Raw text extraction is NOT character-reliable for
   this material: the Appendix extraction proved it
   (199 of 200 entry blocks carried extraction-
   corrupted glyphs — diacritic substitution,
   private-use-area glyphs, column interleaving;
   preparation record §4). The Meroitic forms
   therefore require a **checked transcription pass
   against the page images**:
   - a first transcription of each in-scope page,
     entry by entry, carrying per-entry source
     apparatus (page, entry position);
   - an independent check pass over every Meroitic
     form against its page image, character by
     character, with attention to the diacritic and
     special glyphs the extraction corrupted;
   - the digitisation record names the transcriber
     and the checker (a form whose transcription and
     check were performed by the same pass is marked
     as such, not silently passed), and records the
     **error state**: the number of forms corrected
     at check, the classes of correction, and every
     reading that remains unresolved, listed per
     form. A form with an unresolved character is
     flagged in the vocabulary file; whether a
     flagged form enters the scored vocabulary is
     decided and stated in the freeze, not here.
4. **Vocabulary file.** The digitised wordlist is
   written in the gold lexicon's form (per-entry
   Meroitic form(s), gloss, source apparatus,
   transcription flag), held in custody. Book 2's
   Appendix apparatus joins it as the concept frame
   and NES-side material, under the same terms.
5. **Attestation.** Forms then pass the attestation
   filter against the S-2 corpus exactly as spec
   §3.2 registers it (Stage 2 of the sequence in §4
   above), under the §3.6 split construction for any
   corpus-derived derivation work.

## 6. Machinery built now, and what remains freeze-time

Built and fixture-verified in this landing
(`tools/execution_machinery.py`, with
`tools/test_execution_machinery.py`; verification
record at `records/machinery-verification-2026-11-27.md`):

- the per-concept graded score and primary statistic
  T (spec §3.2), and the frozen binary S for the
  comparability subset;
- the joint permutation null (comparator forms
  shuffled across concepts, per-concept counts
  preserved) and the permutation p-value in freeze
  v2's form, (1 + #{perm ≥ obs}) / (1 + nperm);
- the Holm adjustment across the two-test family;
- G-1's arithmetic in TC-102-01's recomputation form;
- G-2's operative simulation exactly as RT6-M11 pins
  it (registered injection construction, 4,000
  replicates per cell, bar at the null's 99th
  percentile in the design-stage form, streams derived
  deterministically from the single freeze seed);
- the prospective binomial bound of spec §4
  (q0 = 0.1255, per-test α ≤ 0.005);
- the §3.6 split construction as amended, verified
  against TC-102-07's filed table.

The machinery works at skeleton level and was
exercised **only on synthetic fixtures**. Reserved to
the freeze, and NOT decided here, because the
registered text reserves them or does not fix them:
the skeleton implementation (the ASJPcode mapping and
the diacritic fold are registered as Spec 097 pipeline
code, freeze v2 §7; the freeze pins that implementation,
imported unchanged as the design stage imported it);
the operative integer seed; the complete mapping table
and per-concept denominators (they do not exist until
the vocabulary is built); and the flagged-form
decision of §5.3 above. One precondition is added by
this record, as machinery discipline and nothing
else: **before the freeze is filed, the fixture suite
is re-run on tower-compute and its result filed with
the freeze** (the reason is stated in the verification
record).

**Hard limits observed in this landing:** no real
concept list was frozen; no real power figure was
computed (the only power figures anywhere in the
machinery's verification are spec §4's own printed
design-stage table, recomputed as a fixture check);
no Meroitic form was scored; nothing was compared
against any family hypothesis.

## 7. The ARMED state and its trigger

**State: COMMISSIONED and ARMED.** On book 1's
arrival and completed digitisation under §5, the
sequence of §4 runs — vocabulary build, freeze, G-1,
G-2, then the test, or the NOT ADMINISTERED closure a
gate failure registers — **without further
commission**. A gate failure is recorded as the
test's outcome under the registered discipline; it is
never worked around, and no gate is lowered.

**How arrival will be known.** Peeters gave no
delivery date or estimate, so the armed state waits
on one of two triggers, whichever fires first: (a) a
Peeters shipping or delivery notice for order
6b0851920a66f appearing in the owner's Gmail (the
mailbox the order confirmation was sent to; the
program's reply watch reads that mailbox), or (b) the
owner's word that the volume has arrived. **The armed
state persists until one of those fires**; it does
not lapse, and no part of the sequence runs before
the trigger and the completed digitisation.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
