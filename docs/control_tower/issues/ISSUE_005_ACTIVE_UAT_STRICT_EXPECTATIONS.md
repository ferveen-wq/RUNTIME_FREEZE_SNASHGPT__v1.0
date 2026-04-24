# ISSUE_005 — Active UAT must not pass without strict expectations

## Type
Test Harness / UAT Discipline

## Problem
A Phase 3A Ceramic smoke test passed even though the output jumped directly to Phase 3B pricing.

Reason:
The test case only provided input/turns and did not assert:
- expected phase
- expected selected_phrase_id
- expected QUALIFICATION_STATUS
- forbidden premature price route

## Risk
False positive UAT results can mark Phase 0–3 as stable while runtime behavior is wrong.

## Rule
No Phase 0–3 active UAT test may be considered valid unless it checks at least:
- phase
- selected_phrase_id
- QUALIFICATION_STATUS

For price-entry tests, also check:
- price_ladder_state
- READY_FOR_NEGOTIATION

For qualifier tests, also forbid:
- premature PHASE3B_* route

## Status
OPEN
