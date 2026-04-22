#!/usr/bin/env bash
set -euo pipefail

REPORT_PATH="${1:-tests/reports/uat_report_20260422_051123.json}"

printf '\n===== PRE-PATCH GATE =====\n'

printf '\n--- branch / head / worktree ---\n'
git branch --show-current
git log --oneline -n 12
git status --short

printf '\n--- active gate file ---\n'
sed -n '1,220p' docs/control_tower/09_PRE_PATCH_GATE.md

printf '\n--- latest real failing report ---\n'
python3 - "$REPORT_PATH" <<'PY'
import json, sys
from pathlib import Path

path = Path(sys.argv[1])
if not path.exists():
    raise SystemExit(f"Report not found: {path}")

data = json.loads(path.read_text(encoding="utf-8"))
print("report:", path)
print("summary:", data["summary"])

for r in data["results"]:
    if not r["pass"]:
        d = r.get("debug", {})
        print("\n---", r["case_id"], "---")
        print("input:", r["input"])
        print("phase:", d.get("phase"))
        print("request_type:", d.get("request_type"))
        print("objection_signal:", d.get("objection_signal"))
        print("selected_phrase_id:", d.get("selected_phrase_id"))
        print("qualification:", d.get("QUALIFICATION_STATUS"))
        print("ladder:", d.get("price_ladder_state"))
        print("failures:", r.get("failures"))
PY

printf '\n--- tracker truth snapshot ---\n'
grep -nEi 'broader regression|deferred-family|36/40|38/40|35/40|resolved|remaining failures|phase4|phase5|ceramic|polish|tint|ppf' \
  docs/control_tower/06_PHASE_AUDIT_BOARD.md \
  docs/control_tower/07_ACTIVE_WORKING_MEMORY.md \
  docs/control_tower/08_GAP_REGISTER.md 2>/dev/null | sed -n '1,360p'

printf '\n--- recent commits touching runner/prompt ---\n'
git log --oneline -- runner/run_uat.py runner/context_reset_prompt.txt | head -n 25

printf '\n--- current dirty diff for runner/prompt ---\n'
git diff -- runner/run_uat.py runner/context_reset_prompt.txt | sed -n '1,320p'

printf '\n--- api / credit discipline reminder ---\n'
printf '1) no repeated trace without new code change\n'
printf '2) no repeated pack rerun without new information target\n'
printf '3) smallest unresolved lane first\n'
printf '4) broader rerun only after local proving pack passes\n'
printf '5) reuse latest valid gate evidence when possible\n'

printf '\n===== GATE END =====\n'
printf '\nRULE: no patch before this output is pasted and reviewed.\n'
