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

## Phase 0-3 Ownership Scan — 2026-04-24

Owner-map scan across service and qualifier terms found:

### service_intent
Multiple writer candidates surfaced:
- `CUSTOMER_CHAT_INTAKE_RULES.md`
- `PHASE0_2_LOCK_INDEX.md`
- `QUALIFICATION_ENGINE.md`
- Phase 0-2 reference contract

Risk:
- service intent ownership is not fully clean from a tooling perspective.
- Needs classification between runtime writer vs governance/reference statement.

### active_service_context
Cleaner ownership:
- `QUALIFICATION_ENGINE.md` surfaced as the active writer.
- Other files mostly read or document continuity.

### PPF qualifiers
Split ownership:
- `CUSTOMER_CHAT_INTAKE_RULES.md`
- `QUALIFICATION_ENGINE.md`

### Ceramic/Tint qualifiers
Cleaner ownership:
- `QUALIFICATION_ENGINE.md` appears to own qualifier selection.
- No Intake writer surfaced for the scanned Ceramic/Tint qualifier terms.

### Polishing / Wrap
No matches found for:
- `POLISHING_GOAL`
- `WRAP_INTENT`

Risk:
- Polishing and Wrap may not yet have full Phase 3A qualifier ownership defined.
- Wrap may require manual/handover route rather than automated qualifier flow.

Conclusion:
Before broad Phase 0-3 rollout, ownership must be normalized service-by-service:
PPF, Ceramic, Tint, Polishing, Wrap.
