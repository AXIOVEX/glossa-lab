# Spec 112 — Revision Execution Freeze (2026-11-28)

The revision execution is frozen at this record. The harness and
the independent verifier were committed with this record before any
computation ran; nothing in the frozen design changes after this
commit.

## Corpus pins (re-verified by the harness `pins` command at freeze)

- Kovetsky build commit `145af0836c071e7c9796d37d4b36add00d347c8a`
  (the kovetsky-src worktree HEAD read back at freeze equals this
  commit); `data/inscriptions.jsonl` SHA-256
  `1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`;
  `data/gold_morphology.json` SHA-256
  `c5dc8f3479e81a270a3ee68a9f602c125dcc1211c5fa8b1f8091e56b4bf8a5b8`.
- Otten corpus at custody pin
  `c9158f6865325877112b6b9ceef83b3c80a93c56`;
  `Data/mero-corpus.txt` SHA-256
  `b7f3350c2f2118a8223854462a8e881c424cba6b26c01ebfb676efa92ea253ce`.
- Census at freeze: 368 distinct Kovetsky texts, 335 development;
  210 funerary development texts of 4+ tokens; 18,090 Otten lines,
  16,176 distinct development lines; distinct development forms
  2,015 (Kovetsky) / 1,734 (Otten) / 3,532 pooled — all equal to the
  first execution's filed census.

## Ground truth (carried, byte-identical)

The revision harness's `extract` output was compared to the filed
`records/ground-truth-sets.json` before this freeze: SHA-256
`a9e30b54a6f477683e9ac9dc352b7c51390803b536fbbb91a3b2620f67a0149a`
on both files, 1,719 forms. The preflight is judged against the
filed sets.

## Floors (carried unchanged, restated)

- P-1: median boundary F1 at least 0.80 over the 1,719 forms.
- P-2: slot-sequence match at least 90% of the 95 labeled texts,
  and the presentation (name) slot is the highest-entropy slot.
- P-3: partial precision at least 0.80 AND shuffle yield at most
  20% of the real yield.

## The P-3 shuffle leg, as frozen (construction stated on its face)

The first execution's P-3 shuffle leg was measured on the slot
yield (the first harness's P-3 block borrowed the slot yield; the
filed result was slot shuffle yield 0 against real 2). The revision
registration (section 2.2, item 6) carries that leg as the shuffle
leg's statistic, and section 2.3 additionally registers a
character-shuffle proposal leg for P-3. The frozen construction
therefore requires P-3 to pass on the conservative conjunction:
precision at least 0.80 AND the character-shuffle proposal ratio at
most 0.20 AND the slot-yield ratio at most 0.20. No leg is weakened
relative to either text.

## Frozen machinery

- Harness: `records/execution-harness-rev.py`, SHA-256
  `3fc79e2c2f09141a8350310e1ab89ba7be9ceda088b7b42edd73ff3cb85575c8`.
  Subcommands: `pins`, `extract`, `fixtureproofs`, `preflight`,
  `induce`. The `preflight` subcommand refuses to run unless the
  fixture proofs (TC-112-10) pass in full; the `induce` subcommand
  refuses to run unless the filed revision preflight verdict record
  contains PASS IN FULL.
- Verifier: `records/execution-verify-rev.py`, SHA-256
  `cdb9b45e6ec0354a2b66375e55b424554530130dda6bf2e0a7f25d1d29e2b661`
  (TC-112-11; independent implementations, no shared code with the
  harness beyond the corpus pins).
- Seeds: 20261128 (token shuffle, P-3 character-shuffle null);
  20261129 (P-3 independent character-shuffle leg); 20261130
  (fixtures). Segmenter: inventory support floor 2 distinct host
  forms; classes I/F/M only; add-0.1 smoothing; boundary penalty
  2.0 nats; K_BEST 5; tie-break (−score, segmentation tuple).
  Grammar and P-3 parameters exactly as registered in
  `records/revision-registration-2026-11-28.md` section 2 and
  encoded in the harness header.
- Fixture proofs (TC-112-10) run after this freeze and before the
  preflight; their output is filed at
  `records/fixture-proofs-rev.json`. If any proof fails, the
  preflight does not run and the revision closes as filed.

## Discipline

The preflight runs once. If any leg fails, the revision closes as
filed under the revision kill criterion; no third design is run
under this registration. Corpus induction runs only on a full pass,
and its outputs carry no assigned meanings (KC-3).
