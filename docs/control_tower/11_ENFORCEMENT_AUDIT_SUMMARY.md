# ENFORCEMENT AUDIT SUMMARY — 2026-04-26

## KEEP (ACTIVE + SAFE)
- .git/hooks/pre-commit
- .pre-commit-config.yaml
- tools/control_tower.py
- tools/audit/active_rollout_guard.py
- tools/audit/run_active_uat_controlled.sh
- tools/audit/pre_uat_guard.py
- tools/audit/runner_health_check.py
- tools/audit/report_analyzer.py
- tools/audit/owner_map.py

## ADJUST
- tools/runtime_guardian.py
Reason:
- Writes directly to PHRASE_LIBRARY
- Runs during governance + patch
- Causes silent drift risk

## DEPRECATE
- runner/apply_patch.py
Reason:
- Auto git add .
- Auto push to main
- Calls runtime_guardian (unsafe)

## RULE GOING FORWARD
- Always use controlled UAT runner
- No direct patch execution scripts
- No auto-writing enforcement tools

