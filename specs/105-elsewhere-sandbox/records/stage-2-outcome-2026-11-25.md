# Stage 2 outcome record — Spec 105 (the ELSEWHERE sandbox), 2026-11-25

Stage 2 as registered (`records/stage-2-registration-2026-11-25.md`, committed before any derivation ran): ladder rung L2 only — counting and frequency derived from recurrence — in all three sandboxes. Executed by `records/stage-2-execution.py` on tower-compute; the script's raw output is filed at `records/stage-2-output-2026-11-25.json`. The datasets stand in custody at `~/.syncyard/worktrees/glossa/glossa-custody/spec105/` on tower-compute (relocated 2026-11-25 under the owner's home-root governance) and are not committed (decision D-105-8). Every dataset hash was re-verified before use at this stage and is unchanged from Stage 1's filing. All outputs of this stage are sandbox-internal (claim C105-5): nothing here is a decipherment claim, and no anchor standing, verdict, or tally in any program moves.

## Derivation log for this stage (registration §3, with the run's inputs)

- **S1 — Tally.** Inputs: each sandbox's derivation dataset (hashes below) and P-4 (recurrence). Each token occurrence incremented its mark's tally, in recorded order.
- **S2 — Totals.** Inputs: the same datasets' recorded artifact, line, and group structure (P-3, P-5). The derived totals reproduce Stage 1's filed censuses exactly in all three sandboxes.
- **S3 — Frequency.** Inputs: S1's counts and S2's token totals. Frequencies are filed as exact reduced fractions; no decimal approximation appears anywhere in the stage's outputs.
- **S4 — Derived ordering.** Inputs: S3's tables. Ordered by count descending, ties by mark ascending in byte order, identically in both implementations.
- **S5 — Shape.** Inputs: S3's tables. Singleton and recurring marks counted; cumulative top-1, top-5, and top-10 token shares computed as exact fractions.

No step took any other input. The Indus reserve was opened only by the hashing function and was read by no derivation (TC-105-09).

## Result per sandbox

**Indus — COMPLETED.** Derivation dataset SHA-256 `84476daa3a1d9ded33ee7c3eeaffb29fac0290ecf3507873206d4d60ac8b948b` verified at run time. Derived totals: 1,336 artifacts, 1,336 lines, 1,336 groups, 5,611 tokens. Frequency structure over the 372 derived marks: the most frequent mark recurs 472 times (472/5611 of all tokens); the top 5 marks carry 1,602/5611; the top 10 carry 2,470/5611; 83 marks are singletons and 289 recur. The unigram baseline for G-IND is built from this derivation set alone and filed at `records/stage-2-indus-unigram-baseline-2026-11-25.json`: 372 parameters whose counts sum to the token total, 5,611, under the probability rule P(m) = count(m) / 5,611 over the derivation inventory. Marks outside the derivation inventory carry no filed mass; the gate stage registers its unseen-mark rule and freezes its margin before unsealing, and no scoring of the reserve took place at this stage.

**Eteocypriot — COMPLETED.** Dataset SHA-256 `2799d1034e8af50a110e7df69d6f79ab931cbc13db480ebbc8d4dfcf589421fe` verified. Derived totals: 2 artifacts, 3 lines, 14 groups, 69 tokens, reproducing Stage 1 exactly. Frequency structure over the 35 derived marks: the most frequent mark recurs 5 times (5/69); the top 5 marks carry 21/69 (7/23); the top 10 carry 36/69 (12/23); 18 of the 35 marks are singletons — over half the inventory occurs exactly once in the whole corpus. The thinness registered at §3.2 of the spec is now quantified at this rung; nothing in the stage cures or hides it.

**Meroitic — COMPLETED.** Dataset SHA-256 `a8f551e5cc5264decbc2c01d7ee924740245ce8cbeca6b4b7f776e88a3920fb7` verified. Derived totals: 376 artifacts, 376 lines, 5,195 groups, 29,843 tokens, reproducing Stage 1 exactly. Frequency structure over the 32 derived marks: no mark is a singleton; the most frequent mark carries 4,484/29843 of all tokens; the top 5 carry 15,229/29843, just over half; the top 10 carry 21,657/29843. The rarest marks in the table are the recorded digits, at counts of 5 to 7; they stand in the table as recorded, uninterpreted, as they did in the inventory.

## Test cases executed at this stage

- TC-105-08 (L2 purity and agreement) — PASS. Implementation A (a Python tally over the parsed dataset) and implementation B (a jq mark stream over the raw bytes through sort and uniq -c, with an awk tally and fraction reduction, sharing no code with A) produced identical ordered (mark, count, reduced frequency) tables and identical corpus totals in all three sandboxes, and the derived totals and inventory sizes reproduce Stage 1's filed censuses and inventories exactly (372 / 35 / 32).
- TC-105-09 (reserve seal at Stage 2) — PASS. The reserve dataset's SHA-256 at this stage is `bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff`, the hash filed at build; the Stage 2 script opens the reserve only inside its hashing function and never parses it; the baseline's inputs contain no reserve artifact.
- TC-105-10 (standing discipline at Stage 2) is executed over this landing's diff at pull-request time and reported there.

## What this stage establishes, and what it does not

Counting and frequency now exist inside each sandbox as derived notions, earned from recurrence at this rung rather than assumed at the floor, and each sandbox's frequency structure is filed in the raw output. The G-IND baseline's parameters are built and filed from the derivation set alone, in the form the gate will consume. That is the whole of it. No rung above L2 has run; no gate has been approached; the reserve remains sealed; the frequency tables are filed in this spec's records, beside and never merged into the programs' working sign lists. The next stage (L3, order structure) requires its own commission under the spec.
