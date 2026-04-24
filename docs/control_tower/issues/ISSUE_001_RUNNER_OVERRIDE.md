# ISSUE_001 — Runner overriding Qualification Engine

## Type
Runtime Bug (Test Harness)

## Affected Surface
runner/run_uat.py

## Problem
Runner forces request_type = PRICE_REQUEST when:
- service keyword present (ppf, ceramic, etc)
- AND year present

This overrides QUALIFICATION_ENGINE.

## Expected Behavior
- QUALIFICATION_ENGINE should be the ONLY writer of request_type

## Actual Behavior
- Runner pre-classifies input and forces pricing flow
- Skips Phase 3A control logic

## Impact
- Inconsistent behavior across tests
- Phase 3A validation unreliable
- False failures / false passes

## Scope Constraint
- ONLY modify runner/run_uat.py
- DO NOT modify runtime files

## Acceptance Criteria
Input:
ppf camry 2022 front city

Expected:
- Should NOT auto-trigger PRICE_REQUEST
- Should follow qualification → controlled flow

## Status
OPEN
