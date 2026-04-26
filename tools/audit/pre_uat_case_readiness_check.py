import json
import os
import sys
from pathlib import Path

CASES_FILE = os.environ.get("UAT_CASES_FILE")

if not CASES_FILE:
    print("[SKIP] No UAT_CASES_FILE set")
    sys.exit(0)

p = Path(CASES_FILE)
if not p.exists():
    print(f"[FAIL] Cases file not found: {p}")
    sys.exit(1)

cases = json.loads(p.read_text())

violations = []

for c in cases:
    case_id = c.get("case_id", "<unknown>")
    expect_phrase = c.get("expect_selected_phrase_id", "")

    # Validate turns shape before API spend
    if "turns" in c:
        for idx, turn in enumerate(c.get("turns", [])):
            role = turn.get("role")
            if role not in {"user", "assistant", "system"}:
                violations.append((case_id, f"turn {idx} has invalid role: {role}"))
            if "content" not in turn:
                violations.append((case_id, f"turn {idx} missing content"))
            elif not isinstance(turn.get("content"), str):
                violations.append((case_id, f"turn {idx} content must be string"))

    # Detect Phase3B expectation
    if expect_phrase.startswith("PHASE3B_"):
        # Check if multi-turn
        if "turns" not in c:
            violations.append((case_id, "Phase3B expected but case is single-turn (no turns)"))

if violations:
    print("[FAIL] UAT readiness check failed:")
    for cid, msg in violations:
        print(f" - {cid}: {msg}")
    sys.exit(1)

print(f"[OK] UAT readiness check passed: {len(cases)} cases")
