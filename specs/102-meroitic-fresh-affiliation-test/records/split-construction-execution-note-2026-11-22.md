# Spec 102 — Split-Construction Execution Note (2026-11-22)

**Date:** 2026-11-22. **Filed in the Red Team Round 6
correction round (finding RT6-H6).** Execution note
only: the §3.6 split construction as amended
(spec.md §3.6 amendment of 2026-11-22) was run over
the fixed examples registered in test case
TC-102-07, on tower-compute, with Python `hashlib`
(SHA-256), the digest read as a big-endian integer
(`int.from_bytes(digest, "big")`), assignment =
value mod 10. Salt (UTF-8 bytes):
`spec102-split-example-salt-2026-11-22`. Separator:
a single 0x00 byte between the salt bytes and the
UTF-8 text bytes. Residue 0 denotes the development
side (the derivation side); residues 1–9 denote the
held-out side.

| Text | SHA-256 digest | Residue | Side |
|---|---|---|---|
| `ato` | `1f3924e248a2b980d52b2377dcb6a526e7d2953b04513ccfc2edf0ff15c74e2d` | 7 | held-out side |
| `mk lb` | `dc3d011961afa4289598b90d308e39a8a5f34813f5f7d4af475d12c4321e3147` | 3 | held-out side |
| `qore kdi ste` | `39832e505bdfc025077c1f7aafe47d76e40de22471f148b242beb69088e90bb8` | 0 | development side (derivation side) |
| `REM 1003 Akinidad stela text` | `39716c8af11f898ffb36de94eb501ffe5953b03d2ed0970898f018d2bf034e83` | 9 | held-out side |
| `bedewi ato mk` | `6aa442f449ca7fd04e478e36feef2ff2ae3020977107ccf9278276247b0adc54` | 0 | development side (derivation side) |

Result: the recomputation at filing reproduced every
digest, residue, and side in the TC-102-07 table
exactly; no text falls on both sides. This note
executes no part of Spec 102's study: no corpus
material was split, scored, or ingested.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
