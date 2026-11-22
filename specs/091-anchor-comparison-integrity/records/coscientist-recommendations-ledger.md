# Co-scientist recommendations ledger — Glossa-Lab (Indus, Eteocypriot, Meroitic)

Purpose (owner's order, 2026-11-22 17:42 ET, generalized to all
Axiovex research): the standing loop for this program is
Co-scientist recommendations → red team → fix and update the
paper and the work → update the Academia paper → further
Co-scientist rounds. This ledger is the check-off record for
that loop: every recommendation is logged once, carries a
status, and is briefed into the next Co-scientist round as
already done / accepted / open, so completed work stops being
re-recommended. It mirrors the Riemann program's ledger of the
same name and discipline.

Statuses, in the owner's vocabulary: **open** (not started) ·
**adjudicating** (verdict being established from the records) ·
**accepted** (adjudicated sustained or decided by the owner;
the act or execution it calls for is recorded but not itself
complete, or is a standing direction) · **done** (verified
from the record, with the evidence pointer) · **rejected**
(with the reason). Nothing is marked done from a summary; the
evidence pointer is the record that proves it. Where a
disposition could not be established from the record, the row
is left open and says so.

## Rounds

- **Round A — Audit of the 94 strict-core Indus readings,
  2026-11-21.** One Academia Co-scientist session; findings
  filed at the goal's
  `hidden_files/delegated-package-2026-11-20/coscientist-audit-94/coscientist-audit-94-findings-2026-11-21.md`
  (SHA-256 `c1b7b83ca33caa59df604f0000d4a550cd4f392a61042342d8d3c2f7917bd2fe`,
  verified before reliance). Adjudication:
  `records/coscientist-audit-94-adjudication-2026-11-21.md`
  (PR #636, merge `21c05151`). Rows A-1 to A-15 below. The
  audit covered the Indus program only.
- **Round B — Refresh, 2026-11-22.** Three Academia
  Co-scientist sessions, submitted ~10:40 ET through the
  tower-compute desktop browser route: Indus
  `5b21c544-e030-4e8e-986b-8053819d500f`, Eteocypriot
  `e213fa07-13b6-44d8-8d7c-a40618c5411d`, Meroitic
  `a3591b6e-aad6-48f2-be46-9a5ecb09b350`. Outputs captured
  the same day at the goal's
  `hidden_files/weekend-iteration-2026-11-21/coscientist-refresh-2026-11-22-outputs/`
  (Indus `indus/indus-refresh-reassessment-2026-11-22.md`,
  SHA-256 `1687ed29…`; Eteocypriot `eteocypriot/RESPONSE.md`,
  inline capture, no separate output file; Meroitic
  `meroitic/meroitic-independent-assessment.md`, SHA-256
  `2edec1b7…`). Adjudication:
  `records/coscientist-refresh-adjudication-2026-11-22.md`
  (PR #673, merge `7a1e2174`), 53 units: Indus I-1 to I-24,
  Eteocypriot E-1 to E-10, Meroitic M-1 to M-19; dispositions
  20 APPLY / 8 APPLY WITH MODIFICATION / 3 DO NOT APPLY /
  22 OWNER DECISION (OD-1 to OD-22, all decided 2026-11-22,
  addenda §8 to §11 of that record). Rows B-I-*, B-E-*,
  B-M-* below carry the adjudication's unit numbers.
- **Round C — Release round, 2026-11-22.** Submissions made
  with the two preprint releases: Eteocypriot
  `34ae4c8f-bdb4-40ec-9989-2e24cd0697e1`, Meroitic
  `fed03c92-dea7-4238-ab3b-40f6073cafc0`. Outputs not yet
  captured; no rows yet. Indus's release-round equivalent
  is Round B's Indus session, already captured and
  adjudicated above.

## Indus rows

### Round A — audit of the 94 (2026-11-21)

Source for all Round A rows: the audit findings file above;
adjudication `records/coscientist-audit-94-adjudication-2026-11-21.md`.

| ID | Recommendation (one line) | Status | Evidence / reason |
|---|---|---|---|
| A-1 | Replace the two positive class labels: the six "independently supported" become E (external-support claims on file; unverified; NOT IDENTIFIABLE), the 65 "internal-only supported" become I (internally motivated candidate; support not demonstrated; identifiability untested); R, P, U retained | done | Adjudication §1 (PR #636, merge `21c05151`); executed in `records/standings-relabel-execution-2026-11-21.md` (PR #637, merge `dc9be167`); executed partition 5 E + 65 I + 4 R + 3 P + 17 U after the M202 addendum (A-12) |
| A-2 | "Supported" is not defensible unqualified for the internal-only 65; keep the inference layers separate (crosswalk ≠ sound value; dictionary ≠ sign assignment; position ≠ lexeme; motif ≠ denotation; expert opinion ≠ identification) | done | Adjudication §2 points 1–3 (PR #636); vocabulary carried in the relabel execution (PR #637) |
| A-3 | Treat the corrected promotion battery as a structural screen, not reading validation (19 re-promoted signs: positional + bigram pass, DEDR not run; score-one signs' missing and failed components not to be conflated) | done | Adjudication §2 point 4 (PR #636) |
| A-4 | Counted evidence lines are not demonstrated independence (multiple labels or repeated runs do not establish independent information; four mentions of one publication are one source) | done | Adjudication §2 point 5 (PR #636); `records/source-diversity-requirement-2026-11-21.md` |
| A-5 | File a per-reading falsifier, with an advance decision rule, for every one of the 94 (none was filed at audit time) | done | Adjudication §2 point 6, APPLY WITH MODIFICATION (same-day credit): `records/per-reading-falsifiers-2026-11-21.md`, 93 of 94 specific, M099 too thin and flagged |
| A-6 | Remove the obsolete HIGH-anchor and reading-dependent premises named in Q3 (M005/M030/M068 → M342; M089 → M342, M267, M176; M037/M075 → M267; M347's slot interpretation; M374 → M328, M073; M375 → M342, M176; M267's interpreted AGENT/TITLE slots; M222/M362 slot credit; M398 → M267, M342; the already-U dependency checks) | done | Adjudication §3 items 1–12 (PR #636); basis notes executed with the relabels (PR #637) |
| A-7 | Run the required dependency graph audit: obtain the inference log for every reading, label edges (raw observation / semantic assumption / score inheritance), compute strongly connected components, rerun dependency-aware | done | Adjudication §3 (registered, blocked there for want of the log); executed as Spec 099 (`specs/099-inference-log/`; PRs #649, #651, #654), completion record `records/q3-graph-audit-completion-2026-11-21.md`: stripping all reading-on-reading premises changes no class (0 of 94), 44 of 94 weakened |
| A-8 | File single-lineage / single-source flags for all 94 as documentation, not grades (no S flag alone demotes; no M flag alone promotes) | done | Adjudication §4 (PR #636): 75 S + 13 N + 5 M + 1 A = 94; flags carried per sign in the relabel execution (PR #637) |
| A-9 | An independently fixed sign-to-language bridge, evaluated against alternatives, ranks first among what would change the standings | accepted | Adjudication §5 point 1, adopted as the standing top gap (a research outcome, not a task; no such object is established); restated as the program's top research priority by Round B OD-2 (row B-I-18) |
| A-10 | Run a locked, genuinely out-of-sample predictive comparison with serious alternatives, plus identifiability testing over the 65 I and rerun identifiability for the six E | done | Adjudication §5 point 2; executed as Spec 098 (`specs/098-identifiability-over-the-65/`): Stage 2 outcome 48 UNDECIDABLE / 17 NOT IDENTIFIABLE / 4 PROCEED / 0 DISCRIMINATED over the population of 69; Stage 3 executed under Round B OD-3 (PR #679, merge `96c1ce52`) |
| A-11 | Dependency-aware reruns in priority order (M342 and M176 first; then M005, M030, M068, M089, M347, M375, M398, M037, M075, M267, M374; for M063 rerun the actual motif claim) | done | Tranche 1 (PR #635, merge `f50dc4e9`): M342 and M176 REPRODUCE EXACTLY, both confirmed U. Tranches 2–3 (PR #638, merge `660cd8a3`): M267 NOT EXECUTABLE AS SPECIFIED; M089's filed upgrade counts internally inconsistent; M063's motif claim FAILS as specified (lift 4.35 < 5.0). M267 dependency-aware retest, F-4 package 2026-11-22: GENITIVE_MARGINAL, not promoted (`records/m267-dependency-aware-retest-2026-11-22.md`) |
| A-12 | Verify the external-support claims against the primary publications (the six E passages and crosswalks; Elamite/Sanskrit forms; M047, M202, M330 attributions; DEDR proto-forms; commodity mismatches) | done | Re-verification record `records/external-support-reverification-2026-11-21.md` (PR #633, merge `9738af59`): M047 VERIFIED AS FILED (provenance only); M124, M329 PARTIALLY VERIFIED; M330 NOT VERIFIABLE; M202 struck to U under the addendum rule. Remainder finished under Round B OD-4 (PR #684, merge `343cd52a`; PR #686, merge `066ef591`); two source items remain open by design (a clean text of Parpola 1994; the full *Elamisches Wörterbuch*) |
| A-13 | Replicate the motif and numerical evidence with full contingency tables and competing-attribute controls | accepted | Adjudication §5 point 5; the motif/numerical record (PR #634, merge `7b91a9be`) found all 13 motif claims NOT REPRODUCIBLE FROM THE RECORDS and all 3 numerical claims WEAKENED for want of the per-seal deposit; the remedy (deposit, then rerun) is Spec 100 under Round B OD-5 (row B-I-21), gated on Miller's reply |
| A-14 | Complete the three expert referrals and resolve version conflicts (for M222, reconcile public kur against canonical min first) | accepted | Adjudication §5 point 6, APPLY WITH MODIFICATION: the program-side acts are done (Stage 4 engagement letters 2026-11-19; Chevillard declined; Kobayashi and Kolichala engaged as T401 blind coders; M222's register value verified as "min"); the codings themselves rest with the scholars and are outstanding |
| A-15 | Adopt the overall verdict: the standings are a candid research-management register, not a calibrated scale of reading correctness; never describe the 71 E+I readings as established, identified, or independently validated | done | Adjudication §6 (PR #636), honest public formulation quoted there; superseded in form by the canonical Indus wording adopted at Round B OD-7 (row B-I-24) |

### Round B — refresh (2026-11-22), Indus units I-1 to I-24

Source for all Round B rows: the captured outputs above;
adjudication `records/coscientist-refresh-adjudication-2026-11-22.md`.
APPLY and APPLY WITH MODIFICATION units landed in the §5
landing plan: L-1 (PR #674, merge `d5eed9ef`), L-2 (PR #677,
merge `17b43e67`).

| ID | Recommendation (one line) | Status | Evidence / reason |
|---|---|---|---|
| B-I-1 | M330's NOT VERIFIABLE outcome must travel with its class E label wherever the label appears | done | APPLY; L-1 register-wording addendum (PR #674) |
| B-I-2 | M124's and M329's DEDR-leg successes must not be summarized as partial verification of the readings | done | APPLY; L-1 (PR #674) |
| B-I-3 | M329's failed pura (Sanskrit) leg must cease contributing to its basis; the class rests on what survives | done | APPLY WITH MODIFICATION (annotate the basis; no strike, no class change); L-2 inference-log amendment (PR #677); completed by the OD-4 remainder (PR #686) |
| B-I-4 | Repair M329's DEDR citation 4524 → 4570 with an amendment trail | done | APPLY; L-2 (PR #677) |
| B-I-5 | Split class E's gloss: external-claim status and per-study identifiability outcome are separate fields, stated per sign, never as a class-wide intrinsic | done | APPLY WITH MODIFICATION; L-1 (PR #674) |
| B-I-6 | Class I's gloss "identifiability untested" is stale after Stage 2; carry the executed outcomes individually | done | APPLY; L-1 (PR #674) |
| B-I-7 | Keep the two 69s distinct: the Stage 2 execution population and the current 69 E/I entries are different memberships | done | APPLY; L-1 membership crosswalk note (PR #674) |
| B-I-8 | Qualify the 17 NOT IDENTIFIABLE as "under the filed prediction model"; state that low power for the 48 is neither corroboration nor refutation | done | APPLY; L-1 (PR #674) |
| B-I-9 | M047's downgrade is documentary, not evidential; preserve the verified prior-proposal provenance in a separate field; do not silently repair the historical log | done | APPLY; L-1 and L-2 (PRs #674, #677) |
| B-I-10 | Broaden the F-9 reopen clause so a verified prior proposal can be entered as a dated, source-linked basis amendment for any sign (OD-1) | done | OWNER DECISION OD-1, ADOPTED 2026-11-22 11:21 ET; F-9 amendment landed with PR #678 (merge `8c272479`); prospective only, M047 remains U |
| B-I-11 | Class R gloss: revalidation is a task status, not a formerly valid reading awaiting routine renewal | done | APPLY; L-1 (PR #674) |
| B-I-12 | Class P gloss: "expert review needed; no reviewer documented" in place of "expert-pending" | done | APPLY; L-1 (PR #674) |
| B-I-13 | Class U gloss: the retained basis is insufficient, not proved false; exact reproduction of M342's and M176's counts is not reproduction of their readings | done | APPLY; L-1 (PR #674) |
| B-I-14 | M048: publish the check beside the move (leg composition, the 2-point rule, the source-diversity note) | done | APPLY WITH MODIFICATION (the check was of record; a summary gap, not a record gap); L-1 (PR #674) |
| B-I-15 | M099: mark insufficiently specified in register surfaces; invent no falsifier | done | APPLY; L-1 (PR #674) |
| B-I-16 | Gloss the 93-of-94 falsifier coverage: falsifiers are drafted statements; specificity and execution determine evidential value | done | APPLY; L-1 (PR #674) |
| B-I-17 | Retain the contradicted-claim rule, applied at the level the contradiction reaches | rejected | DO NOT APPLY: no change; the assessment confirms the adopted addendum rule and its execution (M202 and M044 strikes; M330's nonverification is not a contradiction) |
| B-I-18 | Priority 1: independently fixed sign-to-language evidence is the top gap (OD-2) | accepted | OWNER DECISION OD-2, ADOPTED 2026-11-22 11:25 ET (PR #678 addendum): the bridge search is the program's top research priority; a direction act that commissions no study by itself |
| B-I-19 | Priority 2: conditional go for Spec 098 Stage 3, with the eligibility reconciliation and the M267 and M089 checks as prerequisites (OD-3) | done | OWNER DECISION OD-3, COMMISSIONED 2026-11-22 11:19 ET; executed and landed PR #679 (merge `96c1ce52`): M375 DISCRIMINATED ON PSEUDO-HELD-OUT (the design's ceiling outcome, not an identification); M347, M089, M267 NOT IDENTIFIABLE; no standing changed |
| B-I-20 | Priority 3: finish source checking where it can change a live basis (M330 targeted inspection; M124/M329 outside-proposal legs; Elamite forms and the Mahadevan citation mapped, finished, or retired) (OD-4) | done | OWNER DECISION OD-4, COMMISSIONED 2026-11-22 11:26 ET; executed PR #684 (merge `343cd52a`), remainder completions PR #686 (merge `066ef591`); outcomes in `records/reverification-remainder-2026-11-22.md`; no standing changed |
| B-I-21 | Priority 4: deposit the per-seal iconography join and rerun the 13 motif claims at their original thresholds (OD-5) | accepted | OWNER DECISION OD-5, AUTHORISED IN SPLIT FORM 2026-11-22 11:36 ET: the rerun is authorised and Spec 100 is registered (PR #685, merge `639eb613`); the deposit is held until Miller's reply on the F-1 Holdat track, so execution stands gated |
| B-I-22 | Priority 5 (citation maintenance): state which current E memberships the class rules protect; the 44 and 63 weakened totals are alternatives, not additive; "acyclic" covers the encoded graph only; the 296-item census is an item-type census, not 296 confirmations | done | APPLY; L-1 (PR #674) |
| B-I-23 | Priority 5: inspect Spec 099's 25 ambiguous items for unstated inputs and publish a basis-survival view (OD-6) | done | OWNER DECISION OD-6, COMMISSIONED 2026-11-22 11:37 ET; executed PR #683 (merge `7b8fc4dd`): unstated inputs found for 25 of 25; bases surviving intact 2, citation-only 1, not surviving as filed 22; no class consequence |
| B-I-24 | Adopt the assessment's strongest public formulation as the canonical Indus wording (OD-7) | done | OWNER DECISION OD-7, ADOPTED 2026-11-22 11:40 ET (PR #680, merge `28cabd4b`); canonical text quoted verbatim in adjudication §9 |

## Eteocypriot rows

### Round B — refresh (2026-11-22), units E-1 to E-10

Source: `eteocypriot/RESPONSE.md` (Round B capture);
adjudication as above. APPLY and APPLY WITH MODIFICATION
units landed at L-3 (PR #675, merge `ec07f7c1`).

| ID | Recommendation (one line) | Status | Evidence / reason |
|---|---|---|---|
| B-E-1 | Retain the original Spec 096 registration; do not retrospectively substitute the narrower ICS 196 question | rejected | DO NOT APPLY: no change; the adjudication record already retains the registered claim with its decomposition; a separate registration, if ever pursued, is future work under B-E-8 |
| B-E-2 | C096-1: carry the two-grounds explanation with the verdict (an evidential closure and an observed failure differ in kind; the verdict does not show alignment is worse than chance) | done | APPLY WITH MODIFICATION (the gloss is adopted; the verdict and its adjudicated citation form unchanged); L-3 audit-package completeness note (PR #675) |
| B-E-3 | C096-2: make the continuous-text floor's rationale assessable in audit-facing packages | done | APPLY; L-3 (PR #675) |
| B-E-4 | C096-3: repair the omission — include all four claim texts verbatim in audit-facing packages | done | APPLY; L-3 (PR #675) |
| B-E-5 | C096-4: gloss summary surfaces with the adjudication record's scope sentence (self-assessed process claim; not independently verified) | done | APPLY WITH MODIFICATION (the adjudicated citation form is the owner's and is not changed); L-3 (PR #675) |
| B-E-6 | Rank 1: independent audit and rerun of the frozen A2 implementation before interpreting the one-name recovery (OD-8) | done | OWNER DECISION OD-8, COMMISSIONED 2026-11-22 11:41 ET; executed PR #681 (merge `a0c1b4cf`): the frozen driver reproduces the filed run record byte-for-byte and an independent reimplementation agrees on every verdict-bearing quantity; finding F-2 (fresh-checkout reproducibility) flagged for adjudication |
| B-E-7 | Pursue the missing editions: the Androkles syllabic sides and Perna 2019, keeping acquired material outside the old freeze (OD-9) | done | OWNER DECISION OD-9, COMMISSIONED 2026-11-22 11:42 ET; executed PR #682 (merge `9684d542`): both items openly and lawfully available (Persée, DOI 10.3406/bch.1982.1914; OpenEdition, DOI 10.4000/books.efa.3031); no ILL placed, no fee |
| B-E-8 | Ranks 3–4: A2 baselines and negative controls, then specify a realistic next Eteocypriot claim (OD-10) | done | OWNER DECISION OD-10, COMMISSIONED 2026-11-22 12:23 ET; executed PR #687 (merge `a16bd0b9`): Androkles intake executed (Dedication A, 15 signs in 3 segments; B prints no sign-level transcription), controls landed (sequence score 4 never reached under either null), Spec 101 registered, not executed |
| B-E-9 | Rank 5: an independent human should check Spec 096's reporting completeness against the records (OD-11) | accepted | OWNER DECISION OD-11: deferred 2026-11-22 12:32 ET until the owner named the person; Alex de Voogt named 2026-11-22 14:49 ET and the invitation sent 2026-11-22 15:31 ET (Gmail Sent id `1a204f4784995c21`; `records/od11-naming-and-send-record-2026-11-22.md` in Spec 091's folder); the check itself stands open pending his reply |
| B-E-10 | Adopt the assessment's honest public description as the canonical Eteocypriot wording (OD-12) | done | OWNER DECISION OD-12, ADOPTED 2026-11-22 12:58 ET (PR #680, merge `28cabd4b`); adoption publishes nothing |

## Meroitic rows

### Round B — refresh (2026-11-22), units M-1 to M-19

Source: `meroitic/meroitic-independent-assessment.md`
(Round B capture); adjudication as above. APPLY and APPLY
WITH MODIFICATION units landed at L-4 (PR #676, merge
`79829e88`).

| ID | Recommendation (one line) | Status | Evidence / reason |
|---|---|---|---|
| B-M-1 | Leg A: scope the word "incomplete" — it means incomplete for reproducing the specified published quantities, not a breached deposition commitment | done | APPLY; L-4 citation-gloss addendum (PR #676) |
| B-M-2 | The A9 label: use "discrepant under the documented reproduction procedure" rather than "positively contradicted" (OD-13) | done | OWNER DECISION OD-13, DECIDED 2026-11-22 13:09 ET; landed PR #688 (merge `21e1050e`) as dated amendments preserving the original form; tallies unchanged |
| B-M-3 | State the Table 2 name-list discrepancy (22 reproduced vs 18 published) with its counting rule and provenance wherever the tally is cited | done | APPLY; L-4 (PR #676) |
| B-M-4 | Assemble a claim-by-claim reconciliation table for Leg A from the filed records, the 662 result stated as additional to the ten items | done | APPLY WITH MODIFICATION (filed records only; fixture dependency as far as they show); L-4 (PR #676) |
| B-M-5 | Custody is risk mitigation, not a permission basis (no licence is not a grant; an unanswered request and the owner's risk acceptance are not consent) | rejected | DO NOT APPLY: no change; the assessment confirms the custody record's own position of 2026-11-20 (a risk acceptance by the owner, not a licensing finding; silence recorded as not permission) |
| B-M-6 | Replace F-6's wording with an explicit permitted/paused list (retention, computation, derived artifacts, sharing, publication) matching the custody record | done | APPLY WITH MODIFICATION (restatement only; the posture itself unchanged); L-4 (PR #676) |
| B-M-7 | Clarify custody authority institutionally where permission is unresolved, and adopt a refusal protocol in advance (OD-14) | done | OWNER DECISION OD-14, ADOPTED 2026-11-22 13:12 ET; landed PR #689 (merge `3f3b28f5`): clarification programme and refusal protocol of record; current posture unchanged |
| B-M-8 | Affiliation wording: non-rejection is not isolation (UNDECIDABLE AT THIS POWER is not proof low power is the sole explanation; R3 "not displaced" is non-rejection only; the result must not be rescued at p < 0.05 after the fact) | done | APPLY; L-4 gloss rules (PR #676) |
| B-M-9 | Assess the affiliation test itself: a power/simulation audit of what effects this design could reliably detect (OD-15) | done | OWNER DECISION OD-15, COMMISSIONED 2026-11-22 13:18 ET; executed PR #690 (merge `1173b975`): minimum detectable effect θ ≈ 0.43 / 0.57 / 0.85 at detection 1.0 / 0.75 / 0.5; the two failures are asymmetric; verdict stands |
| B-M-10 | Soreyi's narrow reading must travel with it (frequency in 10 of 16 funerary texts does not distinguish an offering term from a divine-name variant; the result risks rediscovering the anchor) | done | APPLY; L-4 (PR #676); reassessed at B-M-17 |
| B-M-11 | Disclose the seal rule, the cap reasons, and the candidate definitions and falsifiers in campaign summaries | done | APPLY WITH MODIFICATION (the "uncapped score" element is not applicable: the Stage 4.4 machinery has no numeric score to uncap, adjudication §4 item C-1); L-4 (PR #676) |
| B-M-12 | Freeze v2/v3 equivalence needs an executable comparison of scoring inputs, scores, and null results (OD-16) | done | OWNER DECISION OD-16, COMMISSIONED 2026-11-22 13:23 ET; executed PR #691 (merge `c402e816`): executable equivalence proven through the frozen pipeline (identical scores, pairs, and 10,000-draw null histograms) |
| B-M-13 | Audit the freeze split at the dependency level (formulae, monument and textual-family dependence), with candidate-wise denominators and multiplicity treatment (OD-17) | done | OWNER DECISION OD-17, COMMISSIONED 2026-11-22 13:27 ET; executed PR #692 (merge `969cc9b5`): split independence proven; verdict unchanged under every correction; the audit raised finding F-A, corrected PR #696 (merge `0cb34a0c`) |
| B-M-14 | Keep "only Rilly could answer" attributed to the correspondent, not treated as a methodological restriction | done | APPLY; L-4 attribution discipline (PR #676) |
| B-M-15 | Next expert procedure: a verified channel to Rilly (or an introduction via de Voogt), bounded itemised questions, answers recorded by kind (OD-18) | done | OWNER DECISION OD-18, preparation AUTHORISED 2026-11-22 13:33 ET and EXECUTED PR #693 (merge `366b44fb`): verified channel claude.rilly@cnrs.fr from primary institutional sources; six-item question set prepared; Draft A approved by the owner and sent 2026-11-22 13:53 ET (Gmail Sent id `1a2049acfc2feb52`); his reply is outstanding |
| B-M-16 | Rank 2: assemble the inspectable reproduction and adjudication packet under controlled access (OD-19) | done | OWNER DECISION OD-19, COMMISSIONED 2026-11-22 13:37 ET; executed PR #694 (merge `6a009779`): packet assembled in custody on tower-compute, 43 indexed items, 43 of 43 hash-verified; a supplement is the recorded route for the OD-16/17/18 records |
| B-M-17 | Rank 3: reassess soreyi against anchor-only and genre/formula baselines (OD-20) | done | OWNER DECISION OD-20, COMMISSIONED 2026-11-22 13:44 ET; executed PR #695 (merge `fdccc763`): PARTIALLY SUPPORTED survives both baselines in exactly the bounded anchor-variant sense; no verdict changed |
| B-M-18 | Rank 6: register a genuinely fresh discriminating affiliation test only after the preceding checks (OD-21) | accepted | OWNER DECISION OD-21, COMMISSIONED 2026-11-22 13:51 ET; Spec 102 registered, not executed (PR #698, merge `ac6e2ddf`); its S-1 acquisition is owner-gated and was not authorised by the registration |
| B-M-19 | Adopt the assessment's proposed public wording as canonical, effective only when release conditions are satisfied (OD-22) | accepted | OWNER DECISION OD-22, ADOPTED 2026-11-22 13:53 ET, recorded in the closing addendum (PR #697, merge `bb890fda`); adoption publishes nothing and the internal-use ruling stood at adoption |

## Counts

| Section | Rows | done | accepted | adjudicating | open | rejected |
|---|---|---|---|---|---|
| Indus, Round A | 15 | 12 | 3 | 0 | 0 | 0 |
| Indus, Round B | 24 | 21 | 2 | 0 | 0 | 1 |
| Eteocypriot, Round B | 10 | 8 | 1 | 0 | 0 | 1 |
| Meroitic, Round B | 19 | 16 | 2 | 0 | 0 | 1 |
| **Total** | **68** | **57** | **8** | **0** | **0** | **3** |

Round B cross-check against the adjudication record's §7
counts (53 units: 20 APPLY / 8 APPLY WITH MODIFICATION /
3 DO NOT APPLY / 22 OWNER DECISION): the 28 APPLY-family
units are all done at L-1 to L-4; the 3 DO NOT APPLY units
are the 3 rejected rows; of the 22 OWNER DECISION units, 17
are done and 5 stand accepted (OD-2 a standing direction;
OD-5 execution gated on Miller's reply; OD-11 the named
check awaiting de Voogt's reply; OD-21 registered, not
executed; OD-22 adopted, effective on release conditions).
No unit's disposition could not be established from the
record, so no row is left open on that ground; the accepted
rows name the specific act or reply each still awaits.

## Briefing rule (closing note)

Every future Co-scientist brief for any of the three
programs (Indus, Eteocypriot, Meroitic) attaches this
ledger's current state, or a checked-off extract of it, so
that work already done, accepted, or rejected is not
re-recommended. New recommendations are logged once, here,
with the round they came from, and take their status from
the recorded adjudication that answers them. A
recommendation is never marked done from a summary: the
evidence pointer in its row is the record that proves it.

**AI disclosure:** this ledger was compiled by an AI agent
(Muse, via Muse) at the direction of Tristen Pierson,
per constitution sec. VI. It compiles dispositions of
record; it adjudicates nothing and changes no standing,
class, verdict, or tally.
