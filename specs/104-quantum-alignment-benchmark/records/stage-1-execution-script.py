#!/usr/bin/env python3
"""Spec 104 — Stage 1 execution script.

Implements exactly the protocol registered in
specs/104-quantum-alignment-benchmark/spec.md:

- the instance is built from Spec 096's freeze-pinned
  corpus by the E1 driver's own derivation and LCCS
  functions, development records only, and checked
  against the filed E1 run record before any solving
  (TC-104-02; a mismatch stops the execution);
- the QUBO of spec.md section 3 (penalty P = 1 + the
  sum of all scores) is optimized by the EXACT arm
  (exhaustive enumeration where n <= 25; ILP to zero
  MIP gap at every size, TC-104-03 / TC-104-04) and
  by the SA arm under the registered parameters
  (spec.md section 4), with the determinism check
  TC-104-05 on the real instance;
- the synthetic instances are produced by the
  registered generator of spec.md section 5.

The corpus ground truth is used only to identify
which Greek words are the pilot's scored
correspondences (their names and Greek-side indices,
as the E1 driver reads them). The ground-truth
segment assignments are never read by this script:
no solver, score, or certification sees them.

Proposal distribution for SA (the implementation of
the registered "single-bit-flip proposals"): one bit
index drawn uniformly at random per proposal from
the restart's seeded Random; the initial point is
uniform-random bits from the same Random.

Stdlib + numpy + scipy. Prints the run record as
JSON on stdout; the caller files it as the dated raw
output. Deterministic in every value except wall
times, which are reported as measured.

Deviation F-104-1 (filed in the Stage 1 outcome
record): at execution the corpus file's SHA-256 did
not equal the freeze pin. The blob history shows the
pin names the corpus as frozen at Spec 096 Stage 1
(commit 173882a2) and that Red Team correction rounds
of 2026-11-21 changed the file afterwards (current
blob d0047041) without refreshing the pin; a semantic
diff of the two blobs touches only translation
glosses, status and sealing metadata, and the corpus
version field — never the Eteocypriot lines or the
ground-truth correspondences this study consumes.
The script therefore records the pin result in the
run record and lets the registered content gate (the
recomputed matrix against the filed E1 run record)
decide: an exact match proceeds, any difference
stops the execution (exit 4) exactly as registered.
"""
import hashlib
import importlib.util
import json
import math
import random
import statistics
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

ROOT = Path(__file__).resolve().parents[3]
SPEC096 = ROOT / "specs" / "096-eteocypriot-program"
CORPUS = SPEC096 / "corpus" / "corpus.json"
DRIVER = SPEC096 / "records" / "eteocypriot-e1-driver.py"
RUN_RECORD = SPEC096 / "records" / "eteocypriot-e1-run-2026-11-20.json"
EXPECTED_CORPUS_SHA256 = (
    "5077285e8eac4b21785ca29cb151d47407f780998d85fa1eea27ef9d7e04f2dd"
)

SYNTHETIC_SIZES = [(3, 14), (4, 18), (6, 24), (8, 32), (10, 40), (12, 48)]
SYNTHETIC_VALUES = [0, 1, 2, 4]
SYNTHETIC_WEIGHTS = [7, 12, 1, 2]


def load_driver():
    spec = importlib.util.spec_from_file_location("e1_driver", DRIVER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_real_instance(driver):
    """TC-104-02: pin check + recompute + compare to the filed record."""
    raw = CORPUS.read_bytes()
    file_sha = hashlib.sha256(raw).hexdigest()
    pin_match = file_sha == EXPECTED_CORPUS_SHA256
    if not pin_match:
        # Deviation F-104-1 (see module docstring): the pin is
        # stale, not the material. Record and let the content
        # gate below decide; it remains a hard stop.
        print(f"DEVIATION F-104-1: corpus sha256 {file_sha} != "
              f"freeze pin {EXPECTED_CORPUS_SHA256}; proceeding "
              f"to the registered content gate", file=sys.stderr)
    corpus = json.loads(raw.decode("utf-8"))
    dev = [r for r in corpus["inscriptions"] if r.get("split") == "development"]
    by_id = {r["id"]: r for r in dev}
    ics = by_id["ICS196"]
    segments = []
    for line in ics["eteocypriot_lines"]:
        segments.extend([[driver.bare(t) for t in seg] for seg in line["segments"]])
    # The pilot's scored correspondences: names + Greek-side
    # indices only. The ground-truth segment_index fields are
    # never read here.
    names = [(c["greek_word"], c["greek_word_index"])
             for c in ics["ground_truth_correspondences"]]
    matrix = []
    derived = []
    for word, _idx in names:
        d = driver.derive_cv(word)
        derived.append(d)
        matrix.append([driver.lccs(d, seg) for seg in segments])
    filed = json.loads(RUN_RECORD.read_text(encoding="utf-8"))
    filed_names = {n["greek_word"]: n for n in filed["legs"]["ics196"]["names"]}
    checks = {"corpus_sha256_actual": file_sha,
              "freeze_pin": EXPECTED_CORPUS_SHA256,
              "pin_match": pin_match,
              "deviation": None if pin_match else "F-104-1",
              "names": [w for w, _ in names],
              "derived_spellings": ["-".join(d) for d in derived],
              "matrix": matrix,
              "matches_filed_record": True}
    for (word, _idx), row, d in zip(names, matrix, derived):
        f = filed_names[word]
        if f["lccs_by_segment"] != row or f["derived_spelling"] != "-".join(d):
            checks["matches_filed_record"] = False
    if not checks["matches_filed_record"]:
        print("STOP: recomputed matrix != filed E1 run record",
              file=sys.stderr)
        sys.exit(4)
    return matrix, checks


def qubo_F(x, S, w, s, P):
    """F as registered (spec.md section 3), direct evaluation."""
    score = 0
    rowsum = [0] * w
    colcount = [0] * s
    for i in range(w):
        for j in range(s):
            if x[i * s + j]:
                score += S[i][j]
                rowsum[i] += 1
                colcount[j] += 1
    pen = sum((r - 1) ** 2 for r in rowsum)
    pen += sum(c * (c - 1) // 2 for c in colcount)
    return score - P * pen


def feasible(x, w, s):
    rowsum = [0] * w
    colcount = [0] * s
    for i in range(w):
        for j in range(s):
            if x[i * s + j]:
                rowsum[i] += 1
                colcount[j] += 1
    return all(r == 1 for r in rowsum) and all(c <= 1 for c in colcount)


def exhaustive(S, w, s, P):
    """Exhaustive QUBO enumeration (n <= 25), numpy-chunked."""
    n = w * s
    sflat = np.array([S[i][j] for i in range(w) for j in range(s)],
                     dtype=np.int64)
    best = None
    n_argmax = 0
    argmax_all_feasible = True
    max_infeasible = None
    chunk = 1 << 16
    for start in range(0, 1 << n, chunk):
        idx = np.arange(start, min(start + chunk, 1 << n), dtype=np.uint64)
        bits = ((idx[:, None] >> np.arange(n, dtype=np.uint64)) & 1)
        X = bits.astype(np.int64).reshape(-1, w, s)
        score = X.reshape(len(idx), n) @ sflat
        rowsum = X.sum(axis=2)
        colcount = X.sum(axis=1)
        pen = ((rowsum - 1) ** 2).sum(axis=1) \
            + (colcount * (colcount - 1) // 2).sum(axis=1)
        F = score - P * pen
        feas = (rowsum == 1).all(axis=1) & (colcount <= 1).all(axis=1)
        cmax = int(F.max())
        if best is None or cmax > best:
            best = cmax
            sel = F == cmax
            n_argmax = int(sel.sum())
            argmax_all_feasible = bool(feas[sel].all())
        elif cmax == best:
            sel = F == cmax
            n_argmax += int(sel.sum())
            argmax_all_feasible = argmax_all_feasible and bool(feas[sel].all())
        if (~feas).any():
            mi = int(F[~feas].max())
            max_infeasible = mi if max_infeasible is None else max(max_infeasible, mi)
    return {"max_F": best, "n_argmax": n_argmax,
            "argmax_all_feasible": argmax_all_feasible,
            "max_infeasible_F": max_infeasible}


def ilp_certify(S, w, s, P):
    """ILP on the hard-constraint assignment formulation, zero MIP gap."""
    n = w * s
    c = -np.array([S[i][j] for i in range(w) for j in range(s)], dtype=float)
    rows = []
    lb = []
    ub = []
    for i in range(w):
        row = np.zeros(n)
        row[i * s:(i + 1) * s] = 1.0
        rows.append(row)
        lb.append(1.0)
        ub.append(1.0)
    for j in range(s):
        row = np.zeros(n)
        for i in range(w):
            row[i * s + j] = 1.0
        rows.append(row)
        lb.append(-np.inf)
        ub.append(1.0)
    A = np.array(rows)
    t0 = time.perf_counter()
    res = milp(c, integrality=np.ones(n),
               bounds=Bounds(np.zeros(n), np.ones(n)),
               constraints=LinearConstraint(A, lb, ub),
               options={"mip_rel_gap": 0.0})
    wall = time.perf_counter() - t0
    assert res.success, f"ILP failed: {res.message}"
    x = [int(round(v)) for v in res.x]
    value = int(round(-res.fun))
    return {"value": value, "wall_s": wall, "x": x,
            "feasible": feasible(x, w, s),
            "qubo_F_at_x": qubo_F(x, S, w, s, P)}


def sa_run(S, w, s, P, optimum, seed):
    """One SA restart under the registered parameters (spec.md section 4)."""
    n = w * s
    rng = random.Random(seed)
    K = max(50_000, 1_000 * n)
    T0 = float(P)
    Tend = 0.01
    x = [rng.randrange(2) for _ in range(n)]
    rowsum = [0] * w
    colcount = [0] * s
    score = 0
    for i in range(w):
        for j in range(s):
            if x[i * s + j]:
                rowsum[i] += 1
                colcount[j] += 1
                score += S[i][j]
    pen = sum((r - 1) ** 2 for r in rowsum) \
        + sum(c * (c - 1) // 2 for c in colcount)
    curF = score - P * pen

    def is_feasible():
        return all(r == 1 for r in rowsum) and all(c <= 1 for c in colcount)

    best_F = curF
    best_feasible = score if is_feasible() else None
    reach_step = None
    reach_time = None
    t0 = time.perf_counter()
    if best_feasible is not None and best_feasible >= optimum:
        reach_step = 0
        reach_time = 0.0
    for k in range(K):
        T = T0 * (Tend / T0) ** (k / K)
        idx = rng.randrange(n)
        i, j = divmod(idx, s)
        if x[idx] == 0:
            d_score = S[i][j]
            # rowsum[i] -> rowsum[i]+1 changes the row term by
            # rowsum^2 - (rowsum-1)^2; the segment's pair count
            # grows by colcount[j].
            d_pen = (rowsum[i] ** 2 - (rowsum[i] - 1) ** 2) + colcount[j]
            dF = d_score - P * d_pen
        else:
            d_score = -S[i][j]
            d_pen = ((rowsum[i] - 1 - 1) ** 2 - (rowsum[i] - 1) ** 2) \
                - (colcount[j] - 1)
            dF = d_score - P * d_pen
        if dF >= 0 or rng.random() < math.exp(dF / T):
            if x[idx] == 0:
                x[idx] = 1
                rowsum[i] += 1
                colcount[j] += 1
            else:
                x[idx] = 0
                rowsum[i] -= 1
                colcount[j] -= 1
            score += d_score
            curF += dF
            if curF > best_F:
                best_F = curF
            if is_feasible():
                if best_feasible is None or score > best_feasible:
                    best_feasible = score
                if reach_step is None and score >= optimum:
                    reach_step = k + 1
                    reach_time = time.perf_counter() - t0
    wall = time.perf_counter() - t0
    return {"seed": seed, "proposals": K, "best_F": best_F,
            "best_feasible": best_feasible,
            "final_feasible_score": score if is_feasible() else None,
            "reached_optimum": best_feasible is not None
            and best_feasible >= optimum,
            "reach_step": reach_step, "reach_time_s": reach_time,
            "wall_s": wall}


def run_instance(label, S, w, s, do_exhaustive):
    total = sum(sum(row) for row in S)
    P = 1 + total
    out = {"label": label, "w": w, "s": s, "n": w * s,
           "scores": S, "sum_s": total, "P": P}
    cert = ilp_certify(S, w, s, P)
    out["ilp"] = cert
    if do_exhaustive:
        t0 = time.perf_counter()
        ex = exhaustive(S, w, s, P)
        ex["wall_s"] = time.perf_counter() - t0
        out["exhaustive"] = ex
    restarts = [sa_run(S, w, s, P, cert["value"], 104000 + r)
                for r in range(1, 11)]
    out["sa_restarts"] = restarts
    bfs = [r["best_feasible"] for r in restarts
           if r["best_feasible"] is not None]
    reached = [r for r in restarts if r["reached_optimum"]]
    out["sa_summary"] = {
        "best_feasible_overall": max(bfs) if bfs else None,
        "median_best_feasible": statistics.median(bfs) if bfs else None,
        "restarts_reaching_optimum": len(reached),
        "median_reach_time_s": (sorted(r["reach_time_s"] for r in reached)
                                [len(reached) // 2] if reached else None),
    }
    return out


def main():
    driver = load_driver()
    matrix, checks = build_real_instance(driver)
    record = {"run": "spec104-stage1", "date": "2026-11-25",
              "program": "Spec 104 - Quantum Alignment Benchmark",
              "tc104_02_instance_fidelity": checks, "instances": []}
    real = run_instance("real-ics196", matrix, 2, 11, do_exhaustive=True)
    record["instances"].append(real)
    # TC-104-05: SA determinism — a second, identical SA pass on the
    # real instance must reproduce every value (wall times excepted).
    again = [sa_run(matrix, 2, 11, real["P"], real["ilp"]["value"],
                    104000 + r) for r in range(1, 11)]
    det_ok = all(
        a["best_F"] == b["best_F"]
        and a["best_feasible"] == b["best_feasible"]
        and a["reach_step"] == b["reach_step"]
        for a, b in zip(real["sa_restarts"], again))
    record["tc104_05_sa_determinism"] = {"identical_values": det_ok}
    for m, (w, s) in enumerate(SYNTHETIC_SIZES, start=1):
        rng = random.Random(20261100 + m)
        flat = rng.choices(SYNTHETIC_VALUES, weights=SYNTHETIC_WEIGHTS,
                           k=w * s)
        S = [flat[i * s:(i + 1) * s] for i in range(w)]
        record["instances"].append(
            run_instance(f"synthetic-{m}-{w}x{s}", S, w, s,
                         do_exhaustive=False))
    print(json.dumps(record, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
