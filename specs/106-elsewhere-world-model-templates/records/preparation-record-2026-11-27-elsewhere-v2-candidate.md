# Preparation record — 2026-11-27 — ELSEWHERE methods paper, version 2 candidate

Study: Spec 106 — The ELSEWHERE Framework: Formal Specification, Baseline World-Model Templates, and the Axiom Census

## Status

**CANDIDATE — NOT DEPOSITED, NOT SENT, NOT PUBLISHED.** Prepared
2026-11-27 for the owner's approval of the actual text. Under the
owner's rule of 2026-11-27, the paper iterates through Co-scientist
review after text approval and before any deposit finalizes; that
round has not run and is not part of this preparation. Version 1
stands as deposited (Zenodo record 24571025, DOI
10.5281/zenodo.24571025) and is untouched by this record.

## The candidate

- **File:** `elsewhere-methods-paper-v2-candidate-2026-11-27.pdf`,
  filed in the goal workspace
  (`files/elsewhere-methods-paper-v2-candidate-2026-11-27.pdf`).
- **Pages:** 8. **Bytes:** 132,081. **SHA-256:**
  `dd5aa034ccbd3b732f54709e4686db804784d4650a02e3ad3ab4736408e0b864`.
- **Source:** `elsewhere-framework-v2.tex`, built on tower-compute
  (TeX Live 2026, pdflatex, three passes, zero errors) in
  `~/.syncyard/worktrees/glossa/elsewhere-paper-v2/` from the
  deposited v1 source (tower `elsewhere-paper-v1/`, PDF SHA-256
  `a85e749dc5da107f55fc1ab2470a4baa14b5db51788cd74cf105e35c006c033b`).

## Change 1 — the normalization qualification (the reason for v2)

Authority: Round N unit N-I-1, landed PR #767; the qualification of
record is the conformance annotation appended to the Spec 105
Stage 6 outcome record
(`specs/105-elsewhere-sandbox/records/stage-6-outcome-2026-11-25.md`).

The Indus boundary-gate paragraph (section "The boundary gates")
previously read, in its result sentences:

> "The baseline's mean per-token log-loss was 4.557943 nats; the
> derived system's was 4.178289 nats; the difference, 0.379654
> nats per token, exceeds the margin of 0.05 frozen before
> unsealing. The gate licenses exactly this: the derived system
> predicts withheld recorded streams better than the sandbox's own
> simplest baseline, by the frozen margin, on this reserve. It
> assigns no value or meaning to any mark."

It now reads:

> "The baseline's mean per-token score under the frozen rule was
> 4.557943 nats; the derived system's was 4.178289 nats; the
> difference, 0.379654 nats per token, exceeds the margin of 0.05
> frozen before unsealing, and the gate's good outcome is the
> correct mechanical consequence of the rule exactly as
> registered. A qualification on what that difference means,
> established by later review, belongs in the statement of the
> result. The weights the frozen rule applies are not
> probabilities. For a given preceding mark, the rule's weights
> over that mark's attested successors already sum to one, and
> the rule then adds a further positive weight for every other
> known mark, with no step that returns the row to a total of
> one; in the filed tables, example rows total 1.152023,
> 1.279273, and 1.287293. The figures are therefore a comparison
> of the two systems under the frozen, unnormalized scoring rule
> as registered, and nothing more. They do not establish an
> advantage of 0.379654 nats per token in predictive log-loss
> under a normalized scoring, and that reading of the result is
> withdrawn. Whether a normalized scoring would preserve the
> outcome is a separate question, to be settled only by a test
> fixed in advance; it has not been run. The gate assigns no
> value or meaning to any mark."

No number changed. The gate figures, the reserve size (334
artifacts, 1,391 tokens), and the frozen margin stand exactly as
in v1; what changed is the interpretation stated for them, which
is withdrawn in the form the annotation prescribes.

## Change 2 — internal-language scrub (owner directive 2026-11-27)

One further change, found by a full-text scan for spec numbers,
requirement and test-case IDs, claim IDs, ledger and claim-status
vocabulary, and internal program labels:

- Closing references paragraph: "and are cited there by the
  history ledgers of the studies concerned" now reads "and are
  cited there in the records of the studies concerned." Reason:
  "history ledgers" is internal ledger vocabulary; the sentence
  now says the same thing in plain words.

Nothing else was changed. The framework's own terms (axiom,
instance, ensemble, verdict labels such as robust-in-ensemble)
are defined in the paper itself and are its public vocabulary;
they are not internal labels and stand as deposited in v1.

## Slop check

- Every number in the new qualification passage was verified
  against the annotation of record: baseline 4.557943, derived
  4.178289, difference 0.379654, frozen margin 0.05, and the three
  row-mass witnesses 1.152023 / 1.279273 / 1.287293 all match the
  annotation and the Stage 6 output exactly.
- A full-text diff against the deposited v1 source shows exactly
  two changed paragraphs (the gate paragraph and the closing
  references sentence above); every other number in the text is
  byte-identical to v1, whose figures were verified against the
  filed records at deposit (release record of 2026-11-26).
- The census figures were additionally re-verified against the
  census audit v2 output of 2026-11-26: 235 axioms (Indus 88 =
  F 4 / K 74 / H 10; Eteocypriot 71 = F 3 / K 58 / H 10; Meroitic
  76 = F 4 / K 62 / H 10), AUDIT PASS.
- The rendered candidate was text-extracted and checked: the
  qualification is present, and no internal-language pattern from
  the scan list appears in the rendered text.

## What does not happen on this record

No deposit, no venue action, no send. On the owner's approval of
the text, the paper goes to Co-scientist review; only after that
round is adjudicated does any deposit question return to the
owner.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
