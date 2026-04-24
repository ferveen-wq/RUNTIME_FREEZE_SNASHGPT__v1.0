# ISSUE_007 — Create raw active UAT runner for rollout truth

## Type
Test Harness / Rollout Validation

## Problem
`runner/run_uat.py` contains many post-processing force functions that can reshape model output after runtime execution.

This means active UAT may not represent pure runtime behavior.

## Risk
- False passes
- False failures
- Wrong runtime patches
- API credit waste
- Phase 0–3 stability claims based on polluted evidence

## Decision
Create a separate raw active UAT runner.

## Requirements
The raw runner must:
- use `00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime`
- support `input` and `turns`
- preserve multi-turn state
- extract debug output
- enforce strict expectations
- reject weak active UAT cases
- perform contradiction guards
- NOT run any `_force_*`, `_enforce_*`, `_sanitize_*`, or `_rebuild_*` post-processing

## Status
OPEN
