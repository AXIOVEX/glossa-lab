# Paper erratum (2026-11-26) — the §5.2 consonant-stem count (Round N unit N-E-3)

**Program:** Spec 096 — Eteocypriot Program. **Date:**
2026-11-26. **Authority:** the Round N adjudication,
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-26-round-n.md`
§3.3 (APPLY).

**Paper:** "Too Thin to Test: A Preregistered Pilot Study
of Eteocypriot Bilingual Alignment, Its Registered
Verdicts, and the Corrections They Required", v4, Zenodo
record 24545017, DOI 10.5281/zenodo.24545017.

**Location:** §5.2, p. 7 — "a consonant-stem table
(sixteen entries, plus a special case in its letter
handling)".

**Correction:** "sixteen entries" should read **"fifteen
entries"**. The special-case clause stands as written:
the ξ → k+s handling lives in the driver's `letters_of`,
outside the STEMS dictionary.

**Basis.** The pinned E1 driver
(`records/eteocypriot-e1-driver.py`, SHA-256
`9ec475fd419150e7d07a6a36f3e306eadc62b0427cdb2a4924825870116c9c95`,
the driver identified in the A2 audit) carries a literal
STEMS dictionary of 15 entries: β, γ, δ, ζ, θ, κ, λ, μ, ν,
π, ρ, σ, τ, φ, χ. The program already corrected this exact
count in the Round 5 correction RT5-05, appended to
`records/outcome-record-amendment-2-correction-2026-11-21.md`,
which gives 15 and explains the earlier double-counting of
ξ. The correction never propagated into the paper text;
Round N's fresh paper/source cross-check found the residue.

**Disposition.** The deposited v4 is NOT silently
replaced. This erratum is the correction of record; the
corrected wording is carried into the next authorized
paper version, which requires the owner's approval of the
actual text. No numerical result, verdict, or standing in
Spec 096 rests on the sentence, and none changes.

**Kill check.** The finding falls to a hash-matching
executed driver with 16 actual STEMS entries, or to
deposited wording whose "sixteen" demonstrably counts a
different, explicitly defined object. Neither condition
holds in the inspected artifacts.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
