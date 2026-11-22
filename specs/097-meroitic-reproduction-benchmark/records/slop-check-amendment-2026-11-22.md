# Spec 097 — AI slop / hallucination check: Meroitic amendment (2026-11-22)

**Date:** 2026-11-22. **Check:** owner-queued AI slop /
hallucination check (2026-11-22 14:53 ET), Meroitic portion.
**Base:** origin/main 33cb761a1384e32c747b3d5c22de97bc35892540,
re-read first-hand; fresh clone on tower-compute. **Bookkeeping
only:** this amendment changes no verdict, standing, tally, or
score. Deposited paper text is NOT edited by this record; exact
corrected passages are prepared below for the coordinator's
deposit chain (PAPER-CORRECTION-PREPARED).

## A. Release record §5 (ResearchGate) — CORRECTED by addendum

§5 as filed (PENDING / not attempted) is superseded by the
later completion of 2026-11-22 (~17:05 ET): ResearchGate
publication 418214318 was added with DOI
10.5281/zenodo.24449454 and the conforming PDF attached, and
verified on its live public page (goal PROGRAM-STATE,
2026-11-22 RESEARCHGATE COMPLETE entry). A dated addendum
appended to the release record states this; §5 original text
is preserved.

## B. Paper corrections prepared (not deposited)

1. **NUMBER — soreyi adjacency rate.** Stage 4.4 reassessment
paragraph: "wosi-adjacent at a rate of 0.8832 per occurrence"
conflates two raw values in
od20-soreyi-baseline-results-2026-11-22.json (SHA filed in
that record): wosi neighbour count 120/137 = 0.8759;
theonym-set / wos-family adjacency 121/137 = 0.8832. This is
the same conflation the OD-20 record corrected under
RT6-L8. Corrected passage: "its development occurrences are
wosi-adjacent at a rate of 0.8759 per occurrence (120 of
137); its theonym-set adjacency rate is 0.8832 (121 of 137)".
All other soreyi quantities in the paper verify against the
raw JSON (137 dev occurrences; sorey 0 in 368 texts;
P(soreyi|wosi)=0.833 held funerary; P(soreyi|no wosi)=0.0;
expected 8.9 of 16 vs 10 observed).
2. **CITATION — Otten & Anastasopoulos venue ordinal.**
Bibliography reads "Proceedings of the 4th Workshop on
Ancient Language Processing"; ACL Anthology
(2025.alp-1.11, pp. 208-219, DOI 10.18653/v1/2025.alp-1.11)
records the Second Workshop on Ancient Language Processing
at NAACL 2025. Corrected passage: "Proceedings of the
Second Workshop on Ancient Language Processing (ALP) at
NAACL 2025".
3. **CITATION (minor, internal) — Griffith date range.**
Abstract and Scope read 1907-1911; Introduction reads
1909-1911 for the fixing of the sign values. One form
should be used throughout in the next deposit version.

## C. Brief / appendix dispositions (filed note, no re-send)

- The Co-scientist brief and appendix cite version DOI
10.5281/zenodo.24449062 (superseded first version), not the
concept DOI 10.5281/zenodo.24449061. The release record §4
sentence "the concept DOI resolves to the current version"
is therefore imprecise as a disposition of the brief: the
cited version DOI resolves to the superseded version, whose
text differs from the current version only in DOI line,
file name, and version label (conformance record). The
brief was accurate at submission (before the conformance
version existed). Disposition: DRIFT, filed by this note;
no follow-up sent, per the standing supersession note.
- Brief and appendix describe the power-audit d values
(1.0 / 0.75 / 0.5) as "standardised effects". In the raw
power-simulation-audit-2026-11-22.json, d is the detection
rate on a truly corresponding concept; the paper states
this correctly. Disposition: DRIFT (wording), filed here.

## D. Verified clean (spot-recomputed from raw JSONs)

Stage 4.2 S=4/12, p=0.0326 (stage-4-2-results.json);
chance rates 0.1255 / 0.1164 and MDE theta R1
0.43/0.57/0.85, R2 0.44/0.58/0.87
(power-simulation-audit-2026-11-22.json); split 335/33,
0 overlap (OD-17 audit); multiplicity 0.0652 / 0.0978;
Leg A Exact 4 / Contradicted 1 (A9, "discrepant under the
documented reproduction procedure") / Untestable 3 /
Basis-unstated 2 (leg-a-results.json); 662 distinct texts,
18,075 tokens; freeze v3 179 forms, matching concepts
(21, 46, 72, 75); OD-22 canonical wording in the paper
matches the adjudication record §12 addendum (PR #701)
verbatim; custody caveat matches the OD-14 programme
record (Otten pin c9158f68..., no licence, owner risk
acceptance, 2026-11-20 permission request unanswered,
aggregate-only).

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson.
