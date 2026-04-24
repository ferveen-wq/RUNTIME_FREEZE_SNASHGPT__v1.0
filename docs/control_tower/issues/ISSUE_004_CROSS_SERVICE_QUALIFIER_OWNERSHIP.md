# ISSUE_004 — Normalize Phase 3A qualifier ownership across services

## Type
Architecture Authority Cleanup

## Problem
Phase 3A qualifier ownership is not uniform across services.

Observed:
- PPF qualifier fields have multiple writers:
  - `CUSTOMER_CHAT_INTAKE_RULES.md`
  - `QUALIFICATION_ENGINE.md`
- Ceramic/Tint qualifier flow appears more centralized under `QUALIFICATION_ENGINE.md`
- Polishing and Wrap are not yet fully reviewed in this authority model

## Risk
- Same customer input may produce unstable behavior
- Runtime may jump phases or lose qualifier sequence
- Future Phase 0–8 rollout can loop due to scattered ownership

## Intended Authority Model
- `CUSTOMER_CHAT_INTAKE_RULES.md`
  - Extracts same-message hints only
  - Does not decide Phase 3A readiness
- `QUALIFICATION_ENGINE.md`
  - Final owner for:
    - qualifier state
    - missing qualifier detection
    - phase3a_required
    - phase3a_complete
    - QUALIFICATION_STATUS
- `PHASE3A_QUALIFICATION_DECISION_MATRIX.md`
  - Contract/reference only
- `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
  - Phrase selection only

## Scope
Review and normalize ownership for:
- PPF
- Ceramic
- Tint
- Polishing
- Wrap

## Wrap Note
Wrap may require manual handover / controlled escalation rather than normal automated qualifier flow.

## Status
OPEN
