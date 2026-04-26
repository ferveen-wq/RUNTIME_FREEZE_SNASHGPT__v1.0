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


## UPDATED ENFORCEMENT RESULT — 2026-04-26

### Now Enforced
- `.pre-commit-config.yaml` is now actually invoked by `.git/hooks/pre-commit`.
- `.snash_patch_gate_reviewed` is now created by `tools/start_lane.sh`.
- Important architecture/governance surfaces now require patch-gate marker before commit.
- `ARCH_CHANGELOG.md` is now enforced for:
  - `00__LOCKED__UPLOAD_SET/`
  - `runner/`
  - `tests/`
  - `docs/control_tower/`
  - `tools/`
  - `.github/`

### Investigation vs Trust Rule
Investigation may be fast and lightweight:
- grep
- inspect files
- read reports
- run focused UAT
- create temporary notes

But trust/promotion requires:
- patch gate review
- scoped patch
- controlled UAT when applicable
- ARCH_CHANGELOG entry
- pre-commit checks
- branch push

### Credit Discipline
UAT/API credit use is advisory, not hard-blocked:
- prefer focused case before broad pack
- avoid rerunning full packs without a new reason
- use controlled active UAT runner for trusted evidence
