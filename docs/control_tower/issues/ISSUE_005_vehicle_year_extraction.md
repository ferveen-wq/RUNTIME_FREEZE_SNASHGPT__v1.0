# ISSUE_005 — VEHICLE YEAR EXTRACTION FAILURE

## Problem
System fails to detect vehicle_year when user provides clear 4-digit year in same message.

Example:
Input:
"ppf camry 2022"

Actual:
- vehicle_year treated as missing
- system asks for year again

Expected:
- vehicle_year = 2022
- Phase 3A should trigger directly

## Classification
Runtime bug — intake / extraction layer

## Impact
- Blocks Phase 3A entry
- Causes wrong Phase 0–2 behavior
- Breaks qualification flow

## Hypothesis
- 4-digit numeric tokens not reliably mapped to vehicle_year
- Intake rules missing explicit extraction rule

## Next Step
- Identify owner of vehicle_year extraction
- Confirm whether CUSTOMER_CHAT_INTAKE_RULES or QUALIFICATION_ENGINE owns parsing
- Patch ONLY extraction logic (not routing)

## Status
OPEN
