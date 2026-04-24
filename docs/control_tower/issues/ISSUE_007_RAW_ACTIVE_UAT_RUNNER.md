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

## Legacy Runner Argument Risk — 2026-04-24

Inspection found `runner/run_uat.py` does not use:
- `argparse`
- `sys.argv`
- `--runtime-dir`
- `--output`

This means command-line flags previously passed to `runner/run_uat.py` may have been ignored.

Risk:
- Tests believed to be using `00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime` may not have been using that folder directly.
- Reports believed to be written to custom `--output` paths may instead be written only to default `tests/reports`.
- Prior active rollout validation may be partially untrusted until verified by a raw active runner.

Decision:
- `runner/run_uat.py` must not be treated as rollout truth.
- `runner/run_active_uat_raw.py` must explicitly load the active runtime folder and explicitly write its report path.
