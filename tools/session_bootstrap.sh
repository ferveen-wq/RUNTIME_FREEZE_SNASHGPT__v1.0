#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

print_section() {
  printf '\n%s\n' "============================================================"
  printf '%s\n' "$1"
  printf '%s\n' "============================================================"
}

safe_show() {
  local file="$1"
  if [ -f "$file" ]; then
    sed -n '1,220p' "$file"
  else
    printf '[MISSING] %s\n' "$file"
  fi
}

print_section "SNASH PROJECT BOOTSTRAP"

printf 'Repo: %s\n' "$ROOT"
printf 'Date: %s\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')"

print_section "1) BRANCH / REPO STATE"
git branch --show-current 2>/dev/null || true
printf '\n'
git status --short 2>/dev/null || true
printf '\n'
git log --oneline -n 12 2>/dev/null || true

print_section "2) ACTIVE WORKING MEMORY"
safe_show "docs/control_tower/07_ACTIVE_WORKING_MEMORY.md"

print_section "3) CONTROL-TOWER OPERATING MODEL"
safe_show "docs/control_tower/07_CONTROL_TOWER_OPERATING_MODEL.md"

print_section "4) SOURCE OF TRUTH ORDER"
safe_show "docs/control_tower/01_SOURCE_OF_TRUTH_ORDER.md"

print_section "5) DRIFT / FAILURE CLASSIFICATION"
safe_show "docs/control_tower/03_DRIFT_AND_FAILURE_CLASSIFICATION.md"

print_section "6) GOVERNANCE / CHANGE CONTROL"
safe_show "docs/control_tower/04_GOVERNANCE_AND_CHANGE_CONTROL.md"

print_section "7) CURRENT ARCHITECTURE / RUNTIME WARNING SNAPSHOT"
printf '%s\n' "--- rollout alignment key lines ---"
grep -RIn "Status:\|BLOCKED\|DEFERRED\|authority conflict\|runtime-blocked\|temporary execution authority\|runner prompt\|harness" \
  docs/master_architecture/10_ROLLOUT_ALIGNMENT_NOTES.md \
  docs/master_architecture/11_TEMP_EVIDENCE_COMPILATION.md \
  docs/master_architecture/02_OWNERSHIP_MODEL.md \
  2>/dev/null | sed -n '1,220p' || true

print_section "8) SERVICE / PHASE MEMORY SNAPSHOT"
printf '%s\n' "--- active working memory service lines ---"
grep -n "### Ceramic\|### Tint\|### PPF\|### Polishing\|### Wrap\|Status:" \
  docs/control_tower/07_ACTIVE_WORKING_MEMORY.md 2>/dev/null || true

printf '\n%s\n' "--- phase audit board key lines ---"
grep -RIn "BLOCKED\|DEFERRED\|TAGGED_CHECKPOINT\|stable\|phase" \
  docs/control_tower/06_PHASE_AUDIT_BOARD.md 2>/dev/null | sed -n '1,220p' || true

print_section "9) EXECUTION LAYER HOTSPOTS"
printf '%s\n' "--- runner prompt hard overrides ---"
grep -n "HARD OVERRIDE\|selected_phrase_id\|QUALIFICATION_STATUS\|price_ladder_state" \
  runner/context_reset_prompt.txt 2>/dev/null | sed -n '1,220p' || true

printf '\n%s\n' "--- runner harness ownership signals ---"
grep -RIn "inject_readonly_runtime_signals\|RUNTIME_SIGNALS (READ-ONLY\|strict_raw\|expect_debug\|quote_required\|price_ladder_state" \
  runner/run_uat.py 2>/dev/null | sed -n '1,220p' || true

print_section "10) FILE NOISE / RISK WARNINGS"
printf '%s\n' "--- suspicious untracked files ---"
git status --short 2>/dev/null | grep -E '^\?\?' | sed -n '1,260p' || true

printf '\n%s\n' "--- temp / backup / scratch footprint ---"
find runner tests/uat docs/master_architecture notes -type f \
  \( -name '*.bak_*' -o -name 'tmp_*' -o -name '*.broken_*' -o -name '*.pre_rebuild_*' \) \
  2>/dev/null | sort | sed -n '1,260p' || true

print_section "11) LATEST REPORT SNAPSHOT"
latest_report="$(ls -1t tests/reports/uat_report_*.json 2>/dev/null | head -n 1 || true)"
if [ -n "${latest_report:-}" ] && [ -f "$latest_report" ]; then
  printf 'Latest report: %s\n' "$latest_report"
  python3 - <<'PY'
import json, glob, os
files = sorted(glob.glob("tests/reports/uat_report_*.json"), key=os.path.getmtime)
if not files:
    print("[NO REPORTS]")
    raise SystemExit(0)
latest = files[-1]
data = json.load(open(latest, encoding="utf-8"))
results = data.get("results", [])
print(f"Cases in latest report: {len(results)}")
for item in results[:8]:
    dbg = item.get("debug", {})
    print(
        f"- {item.get('case_id')} | pass={item.get('pass')} | "
        f"phase={dbg.get('phase')} | phrase={dbg.get('selected_phrase_id')} | "
        f"qual={dbg.get('QUALIFICATION_STATUS')} | ladder={dbg.get('price_ladder_state')}"
    )
PY
else
  printf '[NO REPORTS FOUND]\n'
fi

print_section "12) BOOTSTRAP DECISION RULES"
cat <<'RULES'
DO NOT PATCH until all are true:
- defect bucket is classified
- executable owner is identified
- adjacent authority files are inspected
- validation method is defined

PATCH BUCKETS:
- RUNTIME_AUTHORITY_DEFECT
- HARNESS_DEFECT
- TEST_FIXTURE_DEFECT
- ARCHITECTURE_GAP

STOP CONDITIONS:
- runtime vs harness ownership unresolved
- competing authority files detected
- issue is only described in docs but has no executable owner
- active working memory marks the area blocked/deferred

NEXT:
- run: bash tools/patch_gate.sh
- only then continue
RULES

printf '\n[OK] session bootstrap completed\n'
