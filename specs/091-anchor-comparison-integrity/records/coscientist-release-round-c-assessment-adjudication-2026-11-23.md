# Co-scientist Release Round (Round C) 2026-11-23 — Adjudication of the Delivered Assessments

**Date of adjudication:** 2026-11-23.
**Programs:** Spec 096 (Eteocypriot), Spec 097 (Meroitic).
**Relation to the prior record:** this record is the follow-on
to `records/coscientist-release-round-c-adjudication-2026-11-23.md`
(PR #712), which adjudicated the capture state as it then stood:
the release briefs' text had never entered either session, and
no assessment existed. The briefs were subsequently delivered
into the same two sessions on 2026-11-23, both sessions produced
full assessments, and this record adjudicates those assessments.
Nothing in the PR #712 record is rewritten; its capture finding
stands as the history of the round's first pass.

**Filed under:** the Glossa-Lab loop's standing discipline
(owner directives 2026-11-21 and 2026-11-22): Co-scientist
findings are filed as artifacts and answered on the record;
every recommendation is logged once in
`records/coscientist-recommendations-ledger.md` with its
adjudication status; no standing, verdict, or tally changes
on a Co-scientist round alone.

## 0. Inputs and method

- **Eteocypriot:** session `34ae4c8f-bdb4-40ec-9989-2e24cd0697e1`.
  Brief delivered 2026-11-23 (filed as `MESSAGE-ROUND-C.md`);
  assessment captured the same day at the goal's
  `hidden_files/coscientist-release-2026-11-22/eteocypriot/OUTPUT-ROUND-C.md`,
  14,649 characters, SHA-256
  `e98996a18b47835cae675f8a80ca8675ebf9d7ba0c1435d9c8c70886b7e50901`;
  complete session record `SESSION-RAW-ROUND-C.json`, SHA-256
  `b114beb366c1c427b168f1461da2f94cbe46c2b36c16de9444eccef9967a9171`.
- **Meroitic:** session `fed03c92-dea7-4238-ab3b-40f6073cafc0`.
  Brief delivered 2026-11-23 (filed as `MESSAGE-ROUND-C.md`);
  assessment captured the same day at the goal's
  `hidden_files/coscientist-release-2026-11-22/meroitic/OUTPUT-ROUND-C.md`,
  15,437 characters, SHA-256
  `937559ccb3592cb948c99d1a6df0656861d064f281484235d09b60db3ee9a592`;
  complete session record `SESSION-RAW-ROUND-C.json`, SHA-256
  `413e557e0f25a89673df67742e850227968f983d6ca095ac82c4dfef8570394e`.

Each assessment was broken into discrete units (every distinct
finding, criticism, and recommendation) and each unit was
adjudicated against primary records only: the deposited v2
paper texts, the frozen artifacts and audit records in this
repository, Specs 101 and 102 as registered, and the OD
records. Where a unit quotes or characterises a paper
sentence, the sentence was read in the deposited v2 text
itself, not in the assessment's paraphrase.

Classifications: **APPLY** / **APPLY WITH MODIFICATION** /
**DO NOT APPLY** (reason stated) / **OWNER DECISION**.
Paper-text changes are adjudicated and specified exactly,
in §4, but are not executed by this record: a new paper
version requires the owner's approval of the actual text,
so every paper-affecting item is collected in §4 as one
package for that approval.

**Base of record:** this adjudication was prepared on a fresh
clone at origin/main `78e32fcf` (the PR #712 merge), verified
from the remote at the start of the work. No Round 7
correction landing had merged above that head at preparation
time; the ledger and records adjudicated against are the
files at that head.

## 1. Eteocypriot units (C-E-1 to C-E-20)

Paper of record: "Too Thin to Test", v2, Zenodo record
24449913, DOI 10.5281/zenodo.24449913.

| ID | Unit (assessment's point, compressed) | Classification | Adjudication against the primary records |
|---|---|---|---|
| C-E-1 | Failure to validate is established; falsification of the registered procedure is not cleanly established. §6's "The claim's falsifier is met: P1 fails under both A1 and A2" blurs this, because A1 supplies no content-based recovery evidence and A2 was not administered as preregistered; add the distinction immediately after that sentence. NOT SUPPORTED stands. | APPLY WITH MODIFICATION | Sustained. The §6 sentence stands verbatim in v2 §6. The paper's own §5.1 states A1 is a predetermined index-offset check, "not evidence about the alignment procedure", and that the verdict "rests on A2 and on the floors, not on A1 as a test of derivation"; §5.2 records that A2 as executed was an unanchored substitution for the registered name-anchored A2. The distinction the unit asks for is therefore already the record's position everywhere except the §6 summary sentence. The act is the §6 sentence's qualification (paper package, §4 item E-P1); the verdict is untouched — the assessment itself holds NOT SUPPORTED appropriate. |
| C-E-2 | The canonical public description (OD-12) softens the outcome by omission: it attributes non-establishment to unavailable material without saying the executable leg also missed its recovery criterion and deviated from the registered A2; "recovered one of two" can sound like a promising result blocked principally by access. | OWNER DECISION | The wording stands verbatim in the paper's Scope section and is the owner's adopted canonical wording (OD-12, PR #680). The omission the unit names is real on the wording's face: it says the broader claim "was not established: a required additional corpus was unavailable", and does not state that the administrable leg recovered 1 of 2 against a 2-of-2 criterion under a deviated assumption. Amending an owner-adopted canonical wording is the owner's act. Proposed addition at §5 (OD-C-1). |
| C-E-3 | The process verdict (C096-4) is a retrospective narrowing, not support for the original universal claim; owner adjudication authorises the program's verdict but does not independently validate it. | DO NOT APPLY | No change: the paper already carries exactly this. C096-4 is cited only in narrowed, self-assessed form (§6: "SUPPORTED, narrowed", with its qualifier; abstract: "SUPPORTED in a narrowed form, self-assessed"), and the paper's standing discipline states the approver's adjudication settles the verdicts' status on the record without any automated or external validation being claimed. The unit confirms the record; it asks for no act beyond the disclosure already present. |
| C-E-4 | Temporal inconsistency: §5.2 says "no chance or control battery exists", although §4.2 reports the later exploratory battery. Change to "At the original run, no chance or control battery existed", with a cross-reference to §4.2. | APPLY | Sustained on the v2 text: §5.2's sentence is present-tense ("the two test items are a name and its own patronymic, not independent items, and no chance or control battery exists against which 1-of-2 or 0-of-2 could be read"), and §4.2 reports the battery run on 2026-11-22. The proposed replacement is exact and is adopted (paper package, §4 item E-P2). |
| C-E-5 | The "preregistered" description needs its existing qualification (repository-filed, no external timestamp, execution departed from it) to travel with methodological summaries. | APPLY WITH MODIFICATION | Sustained in part. The qualification stands in the body (§2: "the freeze is repo-filed only, timestamped by the program's own git history and nothing external"), but the abstract and title use "preregistered" unqualified, and the abstract does not carry the departure either (it is stated later in the abstract's corrections sentence). The act is confined to summary surfaces (paper package, §4 item E-P3); the body text is not to be re-qualified at every occurrence. |
| C-E-6 | Weight framing for reproduction: byte-identical rerun supports faithful repetition of the recorded computation; neither it nor the reimplementation establishes transcription fidelity, appropriateness of the alignment assumptions, or compliance with the original registration. | DO NOT APPLY | No change: this is the paper's own scoping. §5.4 states the reproduction as a run "on the executed corpus bytes" and files the fresh-checkout finding (F-2) as flagged and undecided in the same section; nothing in the paper claims the reproduction validates the transcription, the assumptions, or registration compliance. The unit is a correct reading of the record, not a correction to it. |
| C-E-7 | Unresolved tension: §5.2 says the freeze omits an implemented consonant table; §5.4 says a reimplementation "written from the freeze alone" agrees. The audit should state which implementation features the reimplementation actually exercised. | APPLY WITH MODIFICATION | The tension is real on the paper's face and is already resolved in the audit record, which the paper does not quote on this point. The OD-8 audit record (`specs/096-eteocypriot-program/records/a2-audit-rerun-record-2026-11-22.md`, §2, finding F-4) states it plainly: the freeze's rules R1–R3 do not fix the consonant-stem table, but for the two ground-truth names the derivation is fully determined by R1–R3 plus letter identity (the only consonants occurring are ρ, σ, τ, ν, κ, whose stems are the letter identities), so the reimplementation borrowed none of the driver's charged mappings (β→p, γ→k, δ→t, θ→t, ζ→s, φ→p, χ→k, ξ→k+s) for any verdict-bearing quantity. The act is to carry that qualification sentence into the paper (paper package, §4 item E-P4); the record side is already complete. |
| C-E-8 | Do not weaken the hash guard or silently reset the historical pin; the release needs an explicit reconstruction route to the executed snapshot; until then describe reproduction as historical-input reproduction, not unqualified fresh-checkout reproducibility. | APPLY WITH MODIFICATION | The guard and pin position is already the record's (the pin names the executed bytes and was deliberately not re-set; the driver refuses a mismatched checkout, audit record §1.1). The reconstruction route exists on the record (freeze commit `173882a2`; hash chain verified end to end; Python 3.12.3; audit record §§1.1–1.3) but program summaries still say "reproduces byte-for-byte" without always carrying the executed-bytes condition. Adopted as this program's governing citation form from this record: the A2 reproduction is cited as **historical-input reproduction** (byte-for-byte on the executed bytes recovered from the freeze commit), and any summary omitting the condition misstates it. The paper-side residue is §4 item E-P5. |
| C-E-9 | "Specificity" must remain conditional on the two exploratory null models; the controls support only the bounded statement (in the reported exploratory controls, neither set of 999 null replicates produced an LCCS score reaching four; a recovery count of at least one occurred in 11.4% and 19.1% of replicates). | APPLY | Adopted as the governing gloss. The paper's §4.2 already labels the controls exploratory with no verdict resting on them, and the controls record (`a2-baselines-controls-record-2026-11-22.md`) gives the figures exactly as the unit quotes them. From this record, any program statement of the score's specificity is cited in the conditional form (specific against NC-1 and NC-2 as specified), not as a general specificity result. The abstract's unqualified "to be specific against both nulls" is carried into the paper package (§4 item E-P6). No verdict rests on the controls and none is touched. |
| C-E-10 | The controls do not establish name discrimination: the same segment receives score four for both Greek names, including the incorrectly assigned patronymic; the two names are not independent validation trials, and no above-chance general alignment accuracy is shown. | DO NOT APPLY | No change: the paper states both halves itself. §4.1 reports that Aristonaktos's best match is also segment 6 at LCCS 4, not its correspondent; §5.2 states the two test items "are a name and its own patronymic, not independent items". The controls record (§"A2's failure on Ἀριστώνακτος is a tie of substance") files the same point. The unit confirms the record. |
| C-E-11 | The paper needs enough information to judge whether the nulls reproduce the actual search: what was randomised, what was preserved, how ties were scored, whether each replicate repeated the maximisation over candidate segments; scrambling names may remove the shared-prefix difficulty that causes the observed error. | APPLY WITH MODIFICATION | Sustained in part. The specification exists in the controls record (NC-1 preserves every segment's length and token structure under sign relabelling; NC-2 preserves each name's letter multiset under scrambling; the tie behaviour is discussed expressly), but the paper's §4.2 compresses the nulls to their names and percentages, so a paper-only reader cannot judge the search-reproduction question. The act is paper-side specification sentences drawn from the controls record (§4 item E-P7). The shared-prefix caution is filed here as an interpretive note on NC-2: scrambling preserves the letter multiset but not the shared-prefix structure of the name pair, so NC-2 does not by itself test the difficulty that produced the patronymic error. |
| C-E-12 | Dedication A permits sign-level comparison, but a usable known-answer test depends on legibility, on a correspondence fixable independently of the matcher, and on robustness to the editors' uncertainty grades; 15 signs in 3 segments do not by themselves establish those conditions. | DO NOT APPLY | No change: this is already the registered position. Spec 101 §3.3 ("Why not the Androkles form") declines to rest the next study on the dedications, on the adjudication's own E-7 caution that the two dedications are related Amathus texts, not independent replications; the intake record carries each sign's editors' certainty grade and states the second pass was the same reader's. No Androkles known-answer test is registered or claimed. |
| C-E-13 | Perna's re-edition enables continuous-text occurrence and position analyses; acquisition alone does not establish that any legibility floor is met — that requires its own census. | DO NOT APPLY | No change: already registered. Spec 101 P-1 requires the Perna-side intake as a new corpus state with its census stated before any scoring, and §3.2 closes the study TOO THIN at its freeze if a candidate's positions cannot be instantiated against the intaken census. The floor discipline the unit asks for is the design's own. |
| C-E-14 | The next study (§7) is a postdictive recurring-ending occurrence test; restricting candidate generation to ICS 196 cannot erase prior human/agent exposure to Perna's text; recurrence alone will not establish that an ending is morphological or what it means. | DO NOT APPLY | No change: Spec 101 §3.3 states the exposure as the design's governing limit, registers the claim at postdictive strength in advance, requires the exposure statement on every outcome record (C101-2), and the claim itself is an occurrence claim carrying no morphological or semantic conclusion. The assessment's reading of §7 agrees with the registration. |
| C-E-15 | Rank 1: before another alignment run, establish whether any genuinely discriminating test is feasible — document which independently identifiable name correspondences remain, what information has already been exposed, and whether enough independent items exist to distinguish the method from simple matching baselines; the deliverable is a feasibility decision, including a stop decision if none exist. | APPLY | Sustained as new work. No such feasibility record exists: Spec 101 is an occurrence study and does not answer the alignment line's feasibility question, and the paper's own §7 conditions (independent items; a registered battery) presuppose an answer. Accepted as the Eteocypriot alignment line's next record: a feasibility memorandum over the held and obtainable bilingual material, ending in a proceed/stop decision for any further alignment validation. No study is commissioned by this adjudication and no standing is affected. |
| C-E-16 | Rank 2: test correct-versus-confusable-name discrimination, not just match strength — specify the contrast (correct assignment vs best incorrect assignment) from the existing patronymic failure; future controls must reproduce the full selection process and preserve relevant name dependencies; register before obtaining another confirmatory result. | APPLY | Sustained as a design requirement. The paper's §5.2 already bindingly conditions any future E1 re-run on a registered chance/control battery fixed before the run, independent test items, and literature-cited derivation rules; this unit adds the confusable-contrast specification and the selection-process/dependency-preservation requirements to those conditions. Filed here as an amendment to those conditions, binding on any future registration of an E1-form test. It extends the completed controls; it does not reopen them. |
| C-E-17 | Rank 3 (adjudication half): adjudicate the flagged process-verdict qualification — whether C096-4's narrowed scope sentence should be amended to state the executed-bytes condition (finding F-2). | OWNER DECISION | The paper itself reserves this question: §5.4 states the finding is "flagged for adjudication, and is not yet adjudicated: whether the narrowed scope sentence of the process verdict should be amended to state the executed-bytes condition is the approver's question". Amending an adjudicated verdict's scope sentence is the approver's act, not this record's. The reconstruction-documentation half of Rank 3 is answered at C-E-8. Presented at §5 (OD-C-2). |
| C-E-18 | Rank 4: make the registered occurrence study uncertainty-aware and selection-transparent before execution — publish the complete candidate list, permitted variants, positional rules, denominators, and treatment of damaged/restored signs; record prior exposure and retain the postdictive label. | APPLY WITH MODIFICATION | Sustained in part. Most of the unit is already registered: Spec 101 P-2 commits the candidate set — each candidate's sequence, predicted positions, and occurrence floor — to the repository before any scoring code loads the Perna-side state; P-3 requires complete tables in the freeze addendum; C101-2 requires the exposure statement and the postdictive label on every outcome. The surviving gap is real: Spec 101 as registered does not state how damaged or restored signs in the Perna-side census are treated at counting. That treatment is to be fixed in Spec 101's freeze addendum, before execution; the study remains unexecuted and no gate is lowered by adding it. |
| C-E-19 | Rank 5: obtain an independent epigraphic check of the consequential inputs — check the analysed ICS 196 sequences and segmentation against the pending edition material when it arrives; have a different reader check the uncertainty-bearing Androkles A intake. | OWNER DECISION | Split state. The ICS 196 half is already in motion and is not a new recommendation: the Masson edition verification request is outstanding through the interlibrary route (record `ics196-ill-request-2026-11-22.md`), and checking the analysed sequences against it on arrival is the act that request already contemplates. The Androkles half asks for a different human reader; engaging and naming an external checker is the owner's act under this program's discipline (the OD-11 pattern: the owner names the person). Presented at §5 (OD-C-3), confined to the Androkles second-reader question. |
| C-E-20 | Overall verdict and proposed honest public summary (moderate weight on the paper as a corrected account; low weight as validation of the method; none as decipherment evidence; summary text supplied). | DO NOT APPLY | No separate act: the weight framing is consistent with the record, and the summary's actionable content — stating the executed leg's failure and deviation in the program's public description — is C-E-2, which is the owner's decision. The program's canonical wording remains OD-12's until the owner amends it. |

**Eteocypriot totals:** 20 units — 4 APPLY (C-E-4, C-E-9,
C-E-15, C-E-16) / 6 APPLY WITH MODIFICATION (C-E-1, C-E-5,
C-E-7, C-E-8, C-E-11, C-E-18) / 7 DO NOT APPLY (C-E-3, C-E-6,
C-E-10, C-E-12, C-E-13, C-E-14, C-E-20) / 3 OWNER DECISION
(C-E-2, C-E-17, C-E-19).

## 2. Meroitic units (C-M-1 to C-M-26)

Paper of record: "Reproducing a Computational Meroitic Study,
Then Testing Its Corpus", v2, Zenodo record 24450095,
DOI 10.5281/zenodo.24450095.

| ID | Unit (assessment's point, compressed) | Classification | Adjudication against the primary records |
|---|---|---|---|
| C-M-1 | "Discrepant under the documented reproduction procedure" is the appropriate wording for the one discrepant count; it neither overstates nor understates. | DO NOT APPLY | No change: the unit confirms the governing citation form adopted at OD-13 (PR #688) and carried in v2 §3.1 with its dated amendment trail. |
| C-M-2 | The ten-count breakdown is not a reproducibility percentage; A1's "exact" is numerical agreement under a specified interpretation (175 rows with translations against the published description of translated entries); keep that distinction beside the four-exact headline. | DO NOT APPLY | No change: the distinction already stands where the unit asks for it. V2 §3.1 states "A1 is exact on the distinct-headword basis (the deposited file carries 195 data rows, 175 of them with translations, against the paper's label of translated words)", and the exact reproductions' bases are stated for A6, A8, and the Table 2 sizes in the same passage. No percentage of reproducibility is stated anywhere in the paper. |
| C-M-3 | "Fully independent" alignment arm (§3.3): Arm 2 still uses the authors' Egyptian embeddings; call it independently implemented with independently trained Meroitic-side embeddings, not fully independent. | APPLY | Sustained on the v2 text. §3.3 reads "Arm 2, the only fully independent arm, on program-trained Meroitic embeddings against the published Egyptian ones" — the same sentence states the dependence the label denies. The assessment's replacement wording is accurate to the record (Arm 2's Meroitic embeddings are program-trained; its Egyptian side is the published embeddings, held under the same custody). Paper package, §4 item M-P1. The Leg C citation form ("independent reimplementation — headline pattern") is unaffected. |
| C-M-4 | "Independent" splits: exact-text deduplication establishes non-overlap of strings only, not independence of inscriptions, formula families, provenance, or near-identical variants; multiplicity correction cannot establish that independence. | DO NOT APPLY | Not sustained against the paper: v2 makes no "independent splits" claim — the phrase does not occur, and the campaign's split is described by its construction (exact-text deduplication; hash assignment). The dependency question the unit raises was audited at the dependency level for the affiliation leg (OD-17, PR #692: the Stage 4.2 vocabulary inputs never pass through the corpus split at all; the executed partitions intersect in 0 texts), and the one held-out result's formula dependence was measured directly (OD-20). No paper sentence requires the correction. |
| C-M-5 | "Preregistered campaign": the qualifications (internally timestamped registration; post-hoc candidate-screen thresholds) should accompany the first campaign description rather than leave the abstract's unqualified "preregistered" to carry more authority than the record warrants. | APPLY WITH MODIFICATION | Sustained in part. Both disclosures stand in the body: §1 states once, plainly, that "the program's preregistrations are timestamped only by its own repository history" with every "frozen before computation" claim resting on intra-day ordering in a self-hosted record; the candidate stage discloses its screen parameters were "fixed at execution and registered only after the fact". The abstract's "a preregistered decipherment campaign" carries neither. The act is confined to the abstract / first description (paper package, §4 item M-P2); the body disclosures are not to be duplicated at every occurrence. |
| C-M-6 | "Validates a retrieval route": recovering a known anchor variant demonstrates the route can retrieve it; without improvement over the genre/formula baseline it does not validate the route's ability to discover unknown meanings. | APPLY WITH MODIFICATION | Sustained. The phrase stands in the abstract ("which validates a retrieval route, not a reading") and bolded in §5 ("The result validates a retrieval route, not a reading"), while the paper's own OD-20 reassessment (§5) shows the held-out pass "fully accounted for by genre and formula" — i.e., no demonstrated improvement over the baseline the unit names. The narrowing is to the demonstration verb (paper package, §4 item M-P3). The bounded sense and the citation caution otherwise stand; the OD-22 canonical wording does not use the verb and is unaffected. |
| C-M-7 | The abstract-level Afroasiatic exclusion is too broad: the defensible inference is model-conditional (under this detector, its sampled concepts, and the audit's assumed detection rates, the Afroasiatic result is inconsistent with some high-correspondence scenarios); the Clopper–Pearson interval for 4/12 is an interval for a binomial match probability under its assumptions, not for a proportion of inherited cognates or affiliation strength; exclusion bounds should remain explicitly model-conditional. | APPLY WITH MODIFICATION | Sustained for the abstract. The abstract reads "the Afroasiatic rival's failure excluding a strong affiliation". The body already states the exclusion in the model-conditional form the unit requires (power audit: "R2's S = 1 excludes θ above approximately [the stated bound] at [the stated detection rate]"; θ is the audit's correspondence parameter under its stated assumptions, OD-15 record). The act narrows the abstract sentence to that form (paper package, §4 item M-P4). UNDECIDABLE AT THIS POWER is untouched — the assessment itself holds the asymmetry "changes the interpretation of the test failures, not the classification verdict" (C-M-13). |
| C-M-8 | Custody: the position is defensible as a disclosed research-risk decision, not as an established legal entitlement; owner risk acceptance identifies responsibility, does not supply permission, and does not determine lawfulness; equally, absence of a licence does not by itself settle every question of research use. | DO NOT APPLY | No change: this is the custody record's own position, already adjudicated at Round B (B-M-5, DO NOT APPLY on the same ground). The record states a risk acceptance by the owner, not a licensing finding, and records silence as not permission. The unit confirms it, including its even-handed second half. |
| C-M-9 | Refusal protocol: the released paper and its dissemination copies need explicit treatment — "citations of them" should visibly include the Zenodo versions, Academia listing, supplementary material, and public summaries; where an immutable version cannot be removed, specify a linked withdrawal or correction notice and notification to the repository. | APPLY WITH MODIFICATION | Sustained in its narrow part. The OD-14 protocol (`custody-clarification-programme-and-refusal-protocol-2026-11-22.md`) §4.4 covers the benchmark outcome record, the two results files, "and citations of them", and states aggregate statistics already published carry the refusal annotation; §4.5 annotates every citing Spec 097 record. It does not name the deposited paper's dissemination copies (the Zenodo versions, the Academia listing, public summaries) and it specifies no notice route to a repository for a version that cannot be removed. Accepted act: a supplement to the OD-14 protocol naming those copies and the linked-notice / repository-notification route. Record-side only; no paper text is changed by it. |
| C-M-10 | Refusal scope must be dependency-governed: outputs resting on the Otten holding (including campaign use of example phrases derived from it) are to be identified individually; neither withdraw the whole campaign indiscriminately nor exempt it wholesale. | DO NOT APPLY | No change: already the protocol's form. §4.7 names the affected analyses individually (the Leg A census over the Otten corpus, the freeze vocabularies, and Stage 4.2's inputs insofar as they rest on Element 1) under the rebuild-only-from-authorised-sources rule; §4.9 limits an Otten refusal's scope to the material its own terms reach. The example-phrases dependency is traced on the record (OD-17 §1: the formative leg's counts were computed over the development partition plus the 932 distinct example phrases). |
| C-M-11 | The protocol's "deleted after review" needs an accountable timetable and a rule for any legally required preservation. | DO NOT APPLY | Not sustained in its main part: §4.8 sets the timetable (the stop is immediate; the withdrawal, deletion, and annotation motions complete within seven days of the trigger or on the timetable the §4.2 review sets), and §4.6 already preserves a non-infringing audit record "where permitted". The one clarifying residue — an express legally-required-preservation carve-out — is folded into the C-M-9 supplement's scope rather than treated as a separate defect. |
| C-M-12 | Voluntary withdrawal on objection is the program's undertaking, not proof that a rights holder necessarily controls publication of every aggregate fact; keep that distinction explicit. | DO NOT APPLY | No change: the protocol already frames withdrawal as the program's undertaking on objection (§4 trigger; §5's relation statement), not as an admission about the reach of any rights holder's control. The distinction the unit asks to keep explicit is the record's own framing. |
| C-M-13 | The power asymmetry changes the interpretation of the test failures, not the classification verdict; equal failure labels need not imply equal evidential weight. | DO NOT APPLY | No change: confirmation of the OD-15 outcome as landed (PR #690). UNDECIDABLE AT THIS POWER stands with the asymmetry measured; nothing in the unit asks for a different verdict. |
| C-M-14 | Fresh affiliation test (Spec 102): forty concepts is not itself a power guarantee; before execution, calibrate the actual statistic under plausible detection heterogeneity, missingness, and the registered correction; sourcing outside the current lexicon's framework dependence matters as much as increasing the denominator. | APPLY WITH MODIFICATION | Sustained in part. Spec 102 already registers the gates the unit's first half presupposes: G-1 (at least 40 concepts per family test, at least 20 outside the Stage 4.2 twelve) and G-2 (a design-time simulation showing at least 80% power at θ = 0.30, d = 0.75 for the primary statistic T on the frozen lists, filed before any scoring), under a no-lowering rule. The surviving gap is the heterogeneity point: G-2's registered method injects at stated detection rates and does not expressly model heterogeneous per-concept detection probabilities or missingness. Accepted act: at Spec 102's freeze, the G-2 simulation is also run under heterogeneous detection rates and a stated missingness pattern, and filed with the power statement; the gates themselves are unchanged and no gate is lowered by adding the runs. The sourcing point is already G-1's outside-the-twelve requirement plus the owner-gated S-1 acquisition. |
| C-M-15 | PARTIALLY SUPPORTED: preserve it in the historical scoring record (do not silently rewrite the adjudication), but its present scientific interpretation should lead with "known-anchor variant recovered; no demonstrated semantic gain beyond the genre/formula baseline", and the program's own titles, abstracts, tables, metadata, and publicity must not free-stand "one partially supported reading". | APPLY WITH MODIFICATION | The retention half is already this program's discipline and the assessment expressly endorses it; no verdict is rewritten. The presentation half is satisfied in the canonical wording (OD-22's text says "one received a partial rating under our scoring rubric… The partial result is not an independently established new translation") and is carried for the paper by the C-M-6 narrowing. Filed here as the governing citation gloss: in program summaries the partial result is cited in its bounded form (a corpus spelling of the anchored Osiris theonym, rediscovered by the distributional route; its held-out pass fully accounted for by genre and formula), never as a free-standing positive reading. No standing changes. |
| C-M-16 | §5's proposed next test — survival outside the funerary genre, with failure closing the candidate — is not presently a justified falsifier of the Osiris-variant interpretation: a correct theonym reading may have a restricted genre distribution; an out-of-genre test needs a separately justified prediction about where the form should occur and why. | APPLY WITH MODIFICATION | Sustained. The sentence stands in the paper's closing section ("the one partially supported candidate's next test is survival on texts outside the funerary genre where it earned its partial support; survival there would earn it a second look, and failure there would close it"). The paper's own reassessment supplies the ground for the objection: soreyi's distribution "is carried entirely as the second element of the wosi invocation" — an invocation form is genre-bound by construction, so non-survival outside the genre is predicted by the anchor-variant interpretation itself and cannot close it. Acts: (i) paper package, §4 item M-P5 (qualify the closing condition); (ii) a record-side design rule, filed here: no out-of-genre closing test for soreyi may be registered without a separately justified occurrence prediction. No such test is registered, and no standing is affected. |
| C-M-17 | ANSWERED-BY-REDIRECT / NOT CONFIRMED is the correct administrative standing for the anchor tranche; it neither weakens the anchors' published basis nor supplies fresh confirmation; no adverse inference from the awaited reply is warranted. | DO NOT APPLY | No change: confirmation of the standing as filed (Stage 4.5 supplement and correction records; v2 §"Stage 4.5"). |
| C-M-18 | "The field's practitioners cannot answer certainty questions in that form" overgeneralises: de Voogt's difficulty parsing the request establishes a problem with that request to that respondent, not a property of the field. | APPLY | Sustained on the v2 text. The Stage 4.5 passage states the question the program knows how to ask "is not a question the field's practitioners answer in that form, as the redirect and the parse objection together show" — a general claim resting on one respondent's redirect and parse objection. Paper package, §4 item M-P6 (narrow to the respondent and the request as put). |
| C-M-19 | "Rilly's answer would settle the anchors' standing" grants one reply excessive authority; a reply could materially revise the assessment, and the supporting evidence still matters. | APPLY | Sustained on the v2 text: the sentence stands verbatim in the closing section. Paper package, §4 item M-P7 (replace with the materially-revise form). The letter's six questions and the awaited-reply state are unaffected. |
| C-M-20 | If Rilly challenges an anchor, run a five-step protocol: (1) record whether the challenge concerns transcription, segmentation, gloss, certainty, or permitted use; (2) suspend claims that depend on the challenged interpretation; (3) trace the anchor into concept assignment, vocabulary selection, controls, candidate exclusions, and scoring; (4) recompute affected results under a documented amendment, preserving the original results; (5) if the anchor was a target or control, report the effect on that outcome, not merely on the inventory label. | APPLY | Sustained as new record. No challenge-response protocol is on record: the OD-18 preparation record covers the verified channel, the six-item question set, and answer kinds, but not the acts a challenge would trigger. Accepted act: the five steps as stated are adopted as the program's Rilly-challenge protocol, to be filed as a supplement to the OD-18 preparation record in Spec 097's records; this adjudication specifies it in full so the filing is mechanical. It executes only on a reply that challenges an anchor; the awaited-reply state is unchanged. |
| C-M-21 | Rank 1: establish the corpus's effective evidential units — reconcile the 652-index-row, 396-inscription, and 368-distinct-string counts, then examine cross-split dependencies by inscription identity, near-duplicate text, and formula family. | APPLY WITH MODIFICATION | Sustained in part. The reconciliation half is already an open item of the paper's own record ("No record reconciles the 652-row index against the 396-inscription census; that relation stands as an open reconciliation item against the source's documentation"). The dependency half extends OD-17, which was scoped to the Stage 4.2 leg, to the Stage 4.4 held-out basis. Accepted as next work in that combined form; no verdict is conditioned on it in advance. |
| C-M-22 | Rank 2: calibrate semantic discrimination, not just distributional persistence — on licensed material, test whether the candidate-generation route can recover deliberately masked known meanings and distinguish them from plausible rival meanings beyond genre/formula baselines, accounting for prior exposure to anchor spellings. | APPLY | Sustained as a design direction. The record supports the need in the assessment's terms: Leg B's calibration fixture was internally inconsistent and cannot be interpreted as calibration (paper §3, canonical wording), and soreyi's retrieval demonstrates retrievability of a known form, not discrimination among rival meanings (C-M-6). Accepted as the direction for a future registration; no study is commissioned by this adjudication. |
| C-M-23 | Rank 3: obtain an external replay of the published benchmark claims — an independent reproducer running the count procedures and alignment summary from an immutable package, with its own lawful access to required inputs, including the bases behind "exact" (especially A1) and the reproduced 662-text pipeline result. | OWNER DECISION | The inspectable-packet route exists (OD-19: 43 items assembled in custody, hash-verified; a supplement is the recorded route for later records), but engaging an external reproducer is an external-engagement act: under this program's discipline the owner names and authorises the person (the OD-11 pattern). Presented at §5 (OD-C-4). |
| C-M-24 | Rank 4: make targeted reporting and refusal-execution amendments (narrow the Q1–Q5 claims; specify action on the released paper if refusal arrives). | DO NOT APPLY | No separate act: the unit is the aggregate of C-M-3, C-M-5, C-M-6, C-M-7, C-M-9, C-M-18, and C-M-19, and is executed through them. Logged once here so the recommendation is not re-issued; it carries no work of its own. |
| C-M-25 | Rank 5: execute the already-registered affiliation study only after its gates pass; source acquisition, detector calibration, and prospective power assessment are prerequisites, not reasons to relax the freeze if coverage proves inadequate. | DO NOT APPLY | No change: already Spec 102's registered discipline (G-1/G-2 administration gates closing the study NOT ADMINISTERED on failure; the no-lowering rule as amended 2026-11-22). The unit confirms B-M-18's accepted state. |
| C-M-26 | Overall verdict and proposed honest public summary (moderate, claim-specific weight on the benchmark pending independent replay; little weight on the campaign as affiliation evidence; none as a new reading; summary text supplied). | OWNER DECISION | The program already carries an owner-adopted canonical Meroitic wording (OD-22, PR #697), adopted effective on release conditions. The assessment's summary differs from it materially in two places: it states the custody position inside the summary ("using material held without a licence under disclosed owner risk acceptance, with permission requested and unresolved") and phrases the partial result as "recovered a known theonym variant without demonstrated semantic gain beyond genre/formula baselines". Superseding an adopted canonical wording is the owner's act. Presented at §5 (OD-C-5), with the choice stated as adopt-in-whole, adopt-in-part, or retain OD-22. |

**Meroitic totals:** 26 units — 5 APPLY (C-M-3, C-M-18,
C-M-19, C-M-20, C-M-22) / 8 APPLY WITH MODIFICATION (C-M-5,
C-M-6, C-M-7, C-M-9, C-M-14, C-M-15, C-M-16, C-M-21) /
11 DO NOT APPLY (C-M-1, C-M-2, C-M-4, C-M-8, C-M-10, C-M-11,
C-M-12, C-M-13, C-M-17, C-M-24, C-M-25) / 2 OWNER DECISION
(C-M-23, C-M-26).

**Round C (delivered) totals:** 46 units — 9 APPLY /
14 APPLY WITH MODIFICATION / 18 DO NOT APPLY /
5 OWNER DECISION.

## 3. Standing, verdict, and tally check

No unit in either assessment compels a change to any
standing, verdict, or tally, and none is made. The two
closest cases were examined expressly:

- **C-E-1** attacks the §6 formulation of C096-1's
  falsifier, not the verdict: the assessment itself holds
  NOT SUPPORTED appropriate, and the paper's §5.1 already
  rests the verdict on A2 and the floors rather than on A1.
  The residue is a wording qualification (E-P1).
- **C-M-15 / C-M-16** concern the presentation and the
  proposed future test of PARTIALLY SUPPORTED: the
  assessment itself directs that the historical scoring
  outcome be preserved, and no out-of-genre test is
  registered. The residue is a citation gloss (filed at
  C-M-15), a paper qualification (M-P5), and a design rule
  for any future registration.

Every other APPLY-family unit is a wording narrowing, a
record supplement, a freeze-stage adequacy item, or new
future work. All four Spec 096 verdicts, the Spec 097
benchmark tallies (Exact 4 / Discrepant 1 / Untestable 3 /
Basis-unstated 2, in the OD-13 citation form), Stage 4.2's
UNDECIDABLE AT THIS POWER, Stage 4.4's PARTIALLY SUPPORTED
in its bounded sense, and Stage 4.5's
ANSWERED-BY-REDIRECT / NOT CONFIRMED stand exactly as
adjudicated before this round.

## 4. Paper-affecting items — the owner's text-approval package

Nothing in this section is deposited, rebuilt, or published
by this record. Each item states the exact change proposed
to the deposited v2 text; a next version of either paper
requires the owner's approval of the actual text, and the
items for each paper are to be taken to the owner as one
package per paper.

### Eteocypriot paper (v2, DOI 10.5281/zenodo.24449913)

- **E-P1 (from C-E-1).** In §6, immediately after "The
  claim's falsifier is met: P1 fails under both A1 and A2,
  read through the corrections of §5 (A1 a predetermined
  index-offset check; A2 as executed unanchored, 1 of 2)",
  add the distinction: what is established is failure to
  validate — the registered conjunction could not pass on
  the frozen holdings and the executed unanchored
  implementation failed the two-correspondence ICS 196
  criterion — not an uncontaminated experimental
  falsification of the registered alignment procedure,
  which was not faithfully tested in full.
- **E-P2 (from C-E-4).** In §5.2, replace "and no chance
  or control battery exists against which 1-of-2 or 0-of-2
  could be read" with "and at the original run no chance
  or control battery existed against which 1-of-2 or
  0-of-2 could be read (the exploratory battery reported
  in §4.2 was run later, on 2026-11-22)".
- **E-P3 (from C-E-5).** On summary surfaces (abstract;
  title if the owner wishes), carry the §2 qualification
  in compressed form: the registration was repository-filed
  without an external timestamp, and the execution departed
  from it in the A2 respect §5.2 records.
- **E-P4 (from C-E-7).** In §5.4, after the sentence
  reporting that the independent reimplementation "agrees
  with the filed record on every verdict-bearing quantity",
  add the audit record's qualification: the reimplementation
  exercised the derivation only as R1–R3 plus letter identity
  determine it for the two ground-truth names (consonants
  ρ, σ, τ, ν, κ); the driver's charged consonant-stem
  mappings, which appear nowhere in the freeze, are exercised
  by no verdict-bearing quantity.
- **E-P5 (from C-E-8).** In §5.4's summary of the audit's
  positive results, describe the rerun as historical-input
  reproduction: byte-for-byte on the executed bytes recovered
  from the freeze commit, with the reconstruction route
  (freeze commit, verified hash chain) named in the text.
- **E-P6 (from C-E-9).** In the abstract, qualify "to be
  specific against both nulls" as exploratory and
  null-conditional: specific against the two exploratory
  null models as specified in §4.2.
- **E-P7 (from C-E-11).** In §4.2, add the null-specification
  sentences from the controls record: NC-1 relabels signs,
  preserving every segment's length and token structure;
  NC-2 scrambles names, preserving each name's letter
  multiset; each replicate repeats the maximisation over
  candidate segments; ties are scored as reported in the
  controls record (including that the patronymic's failure
  is a tie at the shared maximum).

### Meroitic paper (v2, DOI 10.5281/zenodo.24450095)

- **M-P1 (from C-M-3).** In §3.3, replace "Arm 2, the only
  fully independent arm" with the independently-implemented
  form: Arm 2 is independently implemented, with
  independently trained Meroitic-side embeddings, against
  the published Egyptian embeddings.
- **M-P2 (from C-M-5).** In the abstract's first campaign
  description, qualify "preregistered" in compressed form:
  registered in the program's own repository history
  without an external timestamp, with the candidate-screen
  thresholds fixed at execution and registered after the
  fact (both as disclosed in the body).
- **M-P3 (from C-M-6).** In the abstract and in §5's bolded
  sentence, replace "validates a retrieval route" with
  "demonstrates a retrieval route" (the route retrieved a
  known anchor variant; no improvement over the
  genre/formula baseline is demonstrated).
- **M-P4 (from C-M-7).** In the abstract, replace "the
  Afroasiatic rival's failure excluding a strong
  affiliation" with the model-conditional form used in the
  body's power audit: under the audit's detector, sampled
  concepts, and assumed detection rates, the Afroasiatic
  rival's failure excludes correspondence above the stated
  θ bound, while the leading rival's failure remains fully
  consistent with a moderate correspondence.
- **M-P5 (from C-M-16).** In the closing section, qualify
  the soreyi next-test sentence: non-survival outside the
  funerary genre does not by itself close the candidate,
  because the form's distribution is carried by the wosi
  invocation and is genre-bound under the anchor-variant
  interpretation itself; an out-of-genre test closes the
  candidate only under a separately justified prediction
  of where the form should occur.
- **M-P6 (from C-M-18).** In the Stage 4.5 passage, narrow
  "is not a question the field's practitioners answer in
  that form" to the respondent and the request as put:
  the question, as put to that respondent, was not one he
  could answer in that form, as his redirect and parse
  objection show.
- **M-P7 (from C-M-19).** In the closing section, replace
  "Rilly's answer would settle the anchors' standing" with
  the materially-revise form: Rilly's answer could
  materially revise the assessment of the anchors'
  standing, on the evidence he gives.

## 5. Owner decisions presented by this round

Each is presented to the owner individually, in this
chat's one-decision-at-a-time discipline; none is taken by
this record.

- **OD-C-1 (from C-E-2).** Amend the OD-12 canonical
  Eteocypriot wording to state, in addition to the
  unavailable-corpus ground, that the executable leg
  recovered one of two correspondences against its
  two-correspondence criterion and was executed under a
  deviation from the registered A2. (The assessment's
  full replacement summary at C-E-20 is the alternative
  text if the owner prefers replacement to amendment.)
- **OD-C-2 (from C-E-17).** Adjudicate finding F-2: whether
  C096-4's narrowed scope sentence is amended to state the
  executed-bytes condition on the pilot's reproducibility.
- **OD-C-3 (from C-E-19).** Whether to commission an
  independent second-reader check of the Androkles
  Dedication A intake (15 signs, 3 segments, editors'
  certainty grades), and if so, whom. (The ICS 196 half of
  the unit is already in motion through the interlibrary
  route and is not part of this decision.)
- **OD-C-4 (from C-M-23).** Whether to commission an
  external replay of the Spec 097 benchmark claims from
  the OD-19 inspectable packet, and if so, whom.
- **OD-C-5 (from C-M-26).** Whether the assessment's
  proposed Meroitic public summary supersedes the OD-22
  canonical wording in whole or in part, or OD-22 is
  retained.

## 6. Ledger acts landed with this record

- The ledger's Round C rounds-header entry is corrected:
  the briefs were delivered into both sessions on
  2026-11-23 and full assessments were produced; the
  PR #712 null-round outcome stands as the round's first
  pass and this record as its adjudication of the delivered
  assessments.
- Round C subsections in the Eteocypriot and Meroitic row
  sections now carry rows C-E-1 to C-E-20 and C-M-1 to
  C-M-26, each logged once with its status taken from this
  record: APPLY-family units whose act is a paper-text
  change or future work stand **accepted** (adjudicated
  sustained; the act is specified here and not itself
  complete); the two units whose act is completed by this
  record itself (C-E-9's citation gloss, C-M-15's citation
  gloss) stand **done**; DO NOT APPLY units stand
  **rejected** with their reasons; OWNER DECISION units
  stand **open** pending the owner.
- Counts recomputed: 114 rows — 59 done, 28 accepted,
  6 open, 21 rejected.

**AI disclosure:** this record was compiled by an AI agent
(Muse, via Muse) at the direction of Tristen Pierson,
per constitution sec. VI. It adjudicates the two delivered
Round C assessments against the primary records cited in
each unit; it changes no standing, class, verdict, or
tally, and it deposits, rebuilds, and publishes nothing.
