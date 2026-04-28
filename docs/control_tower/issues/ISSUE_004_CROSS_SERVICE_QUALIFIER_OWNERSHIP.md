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

## Phase 0–2 Service Intent Ownership Finding — 2026-04-25

Active owner-map review found:

- `QUALIFICATION_ENGINE.md` defines and governs:
  - request_type
  - service_intent
  - active_service_context
  - detected_service_intent_in_message

- `PHASE0_2_LOCK_INDEX.md` is a contract / invariant file, not the active writer.
  It points service confirmed priority back to `QUALIFICATION_ENGINE.md`.

- `CUSTOMER_CHAT_INTAKE_RULES.md` contains a narrow roof-black exception:
  - sets product_alias_route = ROOF_PPF_BLACK_GLOSS
  - sets detected_product_sku = ROOF_PPF_BLACK_GLOSS
  - currently also sets service_intent = ppf

Ownership decision:
- Normal service_intent ownership remains with `QUALIFICATION_ENGINE.md`.
- Intake may extract same-message hints and product aliases.
- Intake should not become a broad service_intent writer.
- The roof-black exception should remain monitored as a narrow bridge unless it causes conflict.

Risk:
- Broadening service_intent writes inside Intake would create competing authority.
- detected_service_intent_in_message is defined in Qualification Engine but has no explicit active writer found by exact owner-map search, so this remains a follow-up audit item.

Status:
- ISSUE_004 remains OPEN.
- Next audit: confirm service_intent handling for ceramic, tint, polishing, and wrap under active UAT.

## Wrap Phase 0–2 Recognition Finding — 2026-04-25

Active UAT:
- File: tests/active_rollout_uat/phase0_2_wrap_recognition.json
- Case: wrap_basic_recognition
- Input: wrap camry 2022

Actual:
- phase = 0
- request_type = SERVICE_CONFIRMED
- selected_phrase_id = PHASE4_6_HUMAN_PHRASE_LIBRARY.md → PHASE4_WRAP_PRICE_PRESSURE_L1
- QUALIFICATION_STATUS = NOT_READY
- price_ladder_state = NONE

Assessment:
- Safe behavior: no price was given and qualification stayed NOT_READY.
- Incorrect routing: PHASE4_WRAP_PRICE_PRESSURE_L1 was selected even though no price pressure existed.
- Incorrect intake behavior: customer already gave Camry 2022, but response asked for model/year again.
- Wrap path is not yet aligned with PPF/Ceramic/Tint/Polishing recognition behavior.

Owner-map evidence:
- PHASE3A_Q_WRAP_FINISH exists in QUALIFICATION_ENGINE.md and PHASE4_8_MESSAGE_ASSEMBLY_MAP.md.
- handover_required_flag is referenced by PHASE4_8_MESSAGE_ASSEMBLY_MAP.md and QUALIFICATION_ENGINE.md, but active writer ownership is not cleanly surfaced.
- PHASE4_WRAP_PRICE_PRESSURE_L1 exists in PHASE4_6_HUMAN_PHRASE_LIBRARY.md, but owner-map did not show a clear active routing owner.

Classification:
- Wrap routing / handover ownership gap.
- Do not patch until exact owner is confirmed.

Status:
- ISSUE_004 remains OPEN.
- Next action: inspect QUALIFICATION_ENGINE wrap block and PHASE4_8 wrap routing before deciding whether wrap should ask PHASE3A_Q_WRAP_FINISH or route to specialist handover.

## Status Update — 2026-04-25
OPEN — GOVERNANCE / ARCHITECTURE TRACKING ONLY. Main Phase 3A service entries passed for PPF, Ceramic, Tint, Polishing, and Wrap handover is separately covered. Not blocking Phase 0–3A functional closeout.


## Mixed-Intent / Uncertainty Architecture Finding — 2026-04-25
Deep active-runtime audit found that mixed/uncertain customer communication handling is already factored across Intake, Phase 0–2 lock, Qualification, Assembly, Negotiation, Objection, and Phase 6 education.

Finding:
- Architecture exists, but ownership and priority wiring remain fragmented across multiple runtime files.
- Risk is not missing concept; risk is route precedence / wiring allowing one signal such as price, branch, discount, technical doubt, support, or service switch to interrupt a higher-priority gate.

Action:
- Keep ISSUE_004 open for ownership normalization.
- Validate mixed-intent paths service-by-service before rollout.
- Do not create a new parallel authority unless existing wiring proves insufficient.


## Polishing Phase3A Routing Failure — 2026-04-25

Observed:
- phase = PHASE_3
- request_type = PRICE_REQUEST
- QUALIFICATION_STATUS = NOT_READY
- selected_phrase_id = SERVICE CONFIRMED — PHASE 0–2

Expected:
- PHASE3A_Q_POLISHING_SCOPE

Suspicion:
- Phase3A qualifier_id exists in engine but not honored by assembly
- System falls back to Phase 0–2 SERVICE CONFIRMED route
- Possible causes:
  - qualifier_id not emitted to runtime output
  - qualifier_id not visible to assembly
  - competing route firing before Phase3A gate

Action:
- DO NOT patch
- Require debug exposure of:
  phase3a_qualifier_id, missing_fields, service_intent

---

### ADDITION — GLOBAL MID-FLOW CONTEXT PRESERVATION GAP

Observation:
Customer replies during an active flow may include:
- acknowledgements (ok / okay / 👍 / تمام / اوكي / زين)
- partial answers
- side questions
- objections
- unrelated or off-path messages

Current Risk:
- Runtime may reset:
  - service_intent → unknown
  - active_service_context → null
- This breaks conversation continuity and drops the user out of the active flow.

Expected Behavior:
- If prior context exists (active_service_context not null),
  the system MUST preserve:
  - service_intent
  - active_service_context
  - qualification state
  - phase continuity

- UNLESS there is:
  - explicit service switch
  - explicit new intent replacing previous flow

Clarification:
- Lack of service keywords in current message MUST NOT trigger reset.
- Short or ambiguous replies must be treated as mid-flow continuation, not new conversation.

Scope:
- Global across Phase 0–7
- Applies to all services and all conversation stages

Status:
OPEN — requires owner-level audit (Qualification Engine / Execution Flow / Assembly Map)



## M2 COMPLETION UPDATE — 2026-04-28

- M2 (Phase 0–2 ownership validation) completed across all services: PPF, Ceramic, Tint, Polishing, Wrap.
- Runtime behavior confirms Qualification Engine is the effective owner of:
  - service_intent
  - active_service_context
  - missing_fields
  - phase3a routing

- Wrap correctly operates as special-handling flow (no WRAP_SCOPE automation).

Remaining gap (non-blocking):
- detected_service_intent_in_message has no explicit writer definition (tooling/traceability gap only).
- Intake contains narrow override (roof-black), does not conflict currently.

Status Update:
- Behavioral risk: RESOLVED
- Governance clarity: PENDING (non-blocking)

Decision:
- ISSUE_004 remains OPEN for documentation/tooling clarity only.
