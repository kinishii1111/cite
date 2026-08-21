"""Eval — roda golden.json via grafo; imprime PASS/FAIL; exit 0 se >=70% pass."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from cite.graph import build_graph

GOLDEN = Path(__file__).resolve().parent / "golden.json"
THRESHOLD = 0.70
REFUSE_MARK = "não encontrei essa informação na base kinsolo"


def _classify(state: dict) -> str:
    if state.get("skip_retrieve"):
        return "skip_retrieve"
    gen = (state.get("generation") or "").lower()
    if REFUSE_MARK in gen:
        return "refuse"
    return "cite"


def run_eval() -> int:
    cases = json.loads(GOLDEN.read_text())
    graph = build_graph()
    passed = 0
    for case in cases:
        result = graph.invoke(
            {"question": case["question"], "messages": []},
            config={"configurable": {"thread_id": f"eval-{case['id']}"}},
        )
        got = _classify(result)
        ok = got == case["expect"]
        passed += int(ok)
        print(f"{'PASS' if ok else 'FAIL'} {case['id']}: {case['question']} "
              f"(expect={case['expect']}, got={got})")

    total = len(cases)
    score = passed / total
    print(f"\n{passed}/{total} pass ({(score * 100):.0f}%)")
    return 0 if score >= THRESHOLD else 1


if __name__ == "__main__":
    sys.exit(run_eval())
