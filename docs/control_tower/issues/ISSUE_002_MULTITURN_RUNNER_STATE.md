# ISSUE_002 — Runner does not preserve multi-turn conversation state

## Type
Runtime Bug (Test Harness)

## Affected Surface
runner/run_uat.py

## Problem
For cases using `turns`, the runner sends each turn as a fresh request:
- system prompt
- current user turn only

It does not include prior user/assistant messages.

## Actual Behavior
Multi-turn cases lose context.
The report input also reflects only the first turn, which can make failures misleading.

## Impact
Phase 3B and Phase 4 tests that depend on prior qualification state are not reliable.

## Scope Constraint
- ONLY modify runner/run_uat.py
- DO NOT modify runtime files

## Acceptance Criteria
For a case with:
- `ppf camry 2022 front`
- `city`
- `how much`

The third turn must be evaluated with prior context preserved.

## Status
CLOSED — raw runner state preservation fixed

Closure note — 2026-04-25:
`runner/run_active_uat_raw.py` now preserves parsed state into next-turn context via `STATE_SNAPSHOT_FOR_NEXT_TURN`. `tools/audit/runner_health_check.py` verifies this before multi-turn trust.
