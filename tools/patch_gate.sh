#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

print_section() {
  printf '\n%s\n' "============================================================"
  printf '%s\n' "$1"
  printf '%s\n' "============================================================"
}

show_file_if_exists() {
  local file="$1"
  if [ -f "$file" ]; then
    sed -n '1,220p' "$file"
  else
    printf '[MISSING] %s\n' "$file"
  fi
}

print_section "SNASH PATCH GATE"

printf 'Repo: %s\n' "$ROOT"
printf 'Date: %s\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')"

print_section "1) ACTIVE WORKING MEMORY CHECK"
show_file_if_exists "docs/control_tower/07_ACTIVE_WORKING_MEMORY.md"

print_section "2) REQUIRED PRE-PATCH QUESTIONS"
cat <<'RULES'
Before any patch, you MUST answer these in writing:

1. DEFECT_BUCKET:
   - RUNTIME_AUTHORITY_DEFECT
   - HARNESS_DEFECT
   - TEST_FIXTURE_DEFECT
   - ARCHITECTURE_GAP

2. TARGET_FILE_ROLE:
   - runtime authority
   - engine authority
   - harness / runner
   - governance / control tower
   - test fixture only

3. EXECUTABLE_OWNER:
   - exact file that currently executes or enforces the behavior

4. RAW_DEFECT_EVIDENCE:
   - failing report snippet
   - raw output
   - debug block
   - or equivalent written defect proof

5. TOOLING_RULE_OUT_CHECK:
   - runner injection checked
   - prompt forcing checked
   - test-helper behavior checked

6. FAILING_TEST_BEFORE_PATCH:
   - exact failing pack / focused case / equivalent reproducible failure

7. ADJACENT_FILES_CHECKED:
   - list nearby authority files inspected before patching

8. DUPLICATE_LOGIC_CHECK:
   - confirm similar logic does not already exist elsewhere

9. NARROWEST_PATCH_TARGET_REASON:
   - explain why this file is the smallest correct owner

10. VALIDATION_METHOD:
   - UAT pack / focused case / grep / manual trace / governance check
RULES

print_section "3) SOURCE-OF-TRUTH CHECK"
printf '%s\n' "--- source of truth order ---"
grep -n "Layer A\|Layer B\|Layer C\|Layer D\|Layer E\|Core Rule\|Hard Prohibitions" \
  docs/control_tower/01_SOURCE_OF_TRUTH_ORDER.md 2>/dev/null || true

printf '\n%s\n' "--- governance / change control key lines ---"
grep -n "Runtime Patch Mode\|Testing / Observation Mode\|Audit-Before-Change Rule\|No-Duplicate-Authority Rule\|Defer-vs-Patch Rule\|Hard Prohibitions" \
  docs/control_tower/04_GOVERNANCE_AND_CHANGE_CONTROL.md 2>/dev/null || true

printf '\n%s\n' "--- drift classification key lines ---"
grep -n "Runtime Behavior Issue\|Test / Harness Issue\|Context / Session Issue\|Project Instruction Drift\|Phrase / Message Construction Issue\|Governance / Process Issue\|Unknown / Unclassified" \
  docs/control_tower/03_DRIFT_AND_FAILURE_CLASSIFICATION.md 2>/dev/null || true

print_section "4) HOTSPOT WARNING CHECK"
printf '%s\n' "--- runner prompt hotspot summary ---"
grep -n "HARD OVERRIDE\|PHASE 3\|PHASE 5\|selected_phrase_id\|QUALIFICATION_STATUS\|price_ladder_state" \
  runner/context_reset_prompt.txt 2>/dev/null | sed -n '1,120p' || true

printf '\n%s\n' "--- legacy runner/run_uat.py hotspot summary (not rollout-proof) ---"
grep -n "inject_readonly_runtime_signals\|strict_raw\|expect_debug\|price_ladder_state\|quote_required" \
  runner/run_uat.py 2>/dev/null | sed -n '1,120p' || true

print_section "5) BLOCK / DEFER CHECK"
printf '%s\n' "--- blocked / deferred references ---"
grep -RIn "BLOCKED\|DEFERRED\|Do NOT patch\|Do NOT continue" \
  docs/control_tower \
  docs/master_architecture/10_ROLLOUT_ALIGNMENT_NOTES.md \
  notes/patch_sessions \
  2>/dev/null | sed -n '1,220p' || true

print_section "6) DIRTY STATE / NOISE CHECK"
git status --short 2>/dev/null || true

printf '\n%s\n' "--- suspicious untracked ---"
git status --short 2>/dev/null | grep -E '^\?\?' | sed -n '1,220p' || true

print_section "7) PATCH GATE DECISION"
cat <<'DECISION'
STOP PATCHING if ANY is true:
- executable owner is unclear
- runtime vs harness distinction is unresolved
- target area is blocked or deferred
- similar logic already exists in another file
- issue is docs-only with no executable owner
- patch would create parallel authority
- patch is being proposed from memory rather than current repo evidence

ONLY PROCEED if ALL are true:
- defect bucket classified
- raw defect evidence captured
- runner/tooling/test-helper influence ruled out where relevant
- reproducible failing test or equivalent focused failure exists first
- correct owner identified
- adjacent files checked
- duplicate logic check passed
- narrowest patch target justified
- validation method defined
- blocked/deferred check passed
DECISION

printf '\n[OK] patch gate completed\n'
