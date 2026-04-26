
# ISSUE 016 — FALSE PASS VALIDATION GAP (DEBUG vs OUTPUT MISMATCH)

## Pattern Name
Debug-State / Output Mismatch (False Pass)

## Description
System passes UAT based on internal debug state (e.g., price_ladder_state = FINAL_PRICE_REACHED)
without validating that the required customer-facing output (e.g., actual price text) is present.

## Observed In
- Phase 3B — Price Exposure (PPF)
- Case: ppf_price_exposure_after_full_qualification

## Root Cause
UAT runner validates debug fields only, not actual assistant message content.

## Fix Applied
- Added expect_contains / expect_not_contains support in runner
- Updated UAT cases to enforce price presence in output

## Risk Scope
- Phase 3A (qualifier wording)
- Phase 3B (price exposure)
- Phase 4 (objection handling)
- Phase 5 (deepening responses)

## Enforcement Rule
UAT must validate BOTH:
1. Internal debug state
2. Customer-facing output content

## Status
ACTIVE — Validation Layer Fixed

