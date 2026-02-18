# PHASE5_EXECUTION_GUARD (HARD)
# Purpose: Prevent Phase 5 templates from contaminating Phase 0-4 UAT runs.
# Rule: If PHASE5_ENABLED is not TRUE, this engine MUST NOT reference or use any PHASE5 templates.
# Enforced by: Runtime Orchestrator + Assembly routing.
#
# HARD STOP:
# IF PHASE5_ENABLED != TRUE:
#   - Do NOT load or reference:
#     - PHASE5_5__WHATSAPP_NEXT_STEP_TEMPLATES__EN_AR.md
#   - Return control-only output (no customer-facing text)
#   - STOP
#
# PHASE 4 — CLOSING & HANDOVER ENGINE
Version: 1.0
Status: Locked
Phase: 4
Window: D
Scope: Deterministic closing, terminal states, and human handover control
Language: Control-only (no customer-facing text)

## Phase 5 Authority (LOCKED)
This engine is governed by Phase 5 documents (FINAL). If there is any conflict, Phase 5 wins.

- PHASE5_LOCK.md
- PHASE5_1__CLOSING_STATE_MACHINE.md
- PHASE5_2__HANDOVER_WORKFLOW.md
- PHASE5_3__END_ESCALATE_RULES.md
- PHASE5_4__YES_LATER_SILENCE_PLAYBOOK.md
- PHASE5_5__WHATSAPP_NEXT_STEP_TEMPLATES__EN_AR.md

============================================================
0) PURPOSE
============================================================

This document defines the FINAL conversation states and system behavior
after pricing, objection handling, silence handling, and PIM have completed.

Phase 4 is responsible for:
- Declaring terminal conversation states
- Defining what constitutes a "close"
- Governing when automation MUST stop
- Governing when and how a human handover occurs
- Emitting final routing and control flags only (no language)

This phase does NOT:
- Generate customer-facing text
- Decide tone or persuasion
- Perform pricing or negotiation
- Re-open objections or silence recovery
- Modify any Phase 3 engine behavior

Phase 4 is a control and governance layer only.

============================================================
1) HARD BOUNDARIES (NON-NEGOTIABLE)
============================================================

- Phase 4 MUST consume canonical outputs from Phase 3 only
- Phase 4 MUST NOT inspect raw customer messages
- Phase 4 MUST NOT generate phrases or tone
- Phase 4 MUST NOT restart pricing, objections, silence, or PIM
- Phase 4 decisions are FINAL unless escalated to human
- Once a terminal state is reached, automation may not resume

============================================================
2) INPUT CONTRACT (READ-ONLY)
============================================================

Inputs are provided exclusively by Phase 3 engines after orchestration normalization.

Canonical inputs:

- QUALIFICATION_STATUS (ENUM)
- NEGOTIATION_STATE (ENUM)
- PRICE_LADDER_STATE (ENUM)
- OBJECTION_SIGNAL (ENUM)
- QUOTE_REQUIRED_FLAG (BOOL)
- AUTOMATION_ALLOWED_FLAG (BOOL)
- OBJECTION_REPEAT_COUNT (INTEGER)
- CUSTOMER_RESPONSE_LATENCY (ENUM)
- COMMITMENT_ARTIFACT_STATUS (ENUM)

No other inputs are permitted.

------------------------------------------------------------
2.1) COMMITMENT_ARTIFACT_STATUS (ENUM)
------------------------------------------------------------

COMMITMENT_ARTIFACT_STATUS may be one of:

- NOT_REQUIRED
- PENDING_CONFIRMATION
- CONFIRMED

Notes:
- This value MUST be produced by Phase 3 only.
- "CONFIRMED" indicates a real commitment artifact exists
  (e.g., booking time confirmed, deposit paid, or required details captured).
- Phase 4 MUST NOT infer commitment from raw messages.

============================================================
3) OUTPUT CONTRACT (FINAL CONTROL SIGNALS)
============================================================

Phase 4 emits FINAL control signals only.

Canonical outputs:

- FINAL_CONVERSATION_STATE (ENUM)
- HANDOVER_REQUIRED_FLAG (BOOL)
- HANDOVER_REASON (ENUM | NULL)
- AUTOMATION_TERMINATED_FLAG (BOOL)
- SESSION_CLOSE_REASON (ENUM)

No customer-facing outputs are produced.

------------------------------------------------------------
3.1) SESSION_CLOSE_REASON (ENUM)
------------------------------------------------------------

SESSION_CLOSE_REASON may be one of:

- PRICE_ACCEPTED
- BOOKING_CONFIRMED
- CUSTOMER_EXIT
- QUALIFICATION_FAILED
- HUMAN_HANDOVER_REQUIRED
- SYSTEM_TERMINATION
- NO_RESPONSE_TIMEOUT
- POLICY_ENFORCED

SESSION_CLOSE_REASON MUST be consistent with FINAL_CONVERSATION_STATE.

============================================================
4) TERMINAL CONVERSATION STATES (ENUM)
============================================================

FINAL_CONVERSATION_STATE may be one of:

- CLOSED_SUCCESSFULLY
- CLOSED_NO_DECISION
- CLOSED_DISQUALIFIED
- ESCALATED_TO_HUMAN
- TERMINATED_BY_SYSTEM
- TERMINATED_BY_CUSTOMER

These states are irreversible.

============================================================
5) CLOSING DECISION RULES (DETERMINISTIC)
============================================================

------------------------------------------------------------
5.1) FINAL STATE RESOLUTION ORDER (STRICT PRIORITY)
------------------------------------------------------------

When multiple closing conditions are simultaneously true,
Phase 4 MUST resolve FINAL_CONVERSATION_STATE using this priority order (top wins):

1. TERMINATED_BY_SYSTEM
2. TERMINATED_BY_CUSTOMER
3. CLOSED_DISQUALIFIED
4. ESCALATED_TO_HUMAN
5. CLOSED_SUCCESSFULLY
6. CLOSED_NO_DECISION

Once a higher-priority state is selected, all lower-priority checks MUST be skipped.

------------------------------------------------------------
5.2) RULES (NON-EXHAUSTIVE)
------------------------------------------------------------

- If AUTOMATION_ALLOWED_FLAG == FALSE
  → ESCALATED_TO_HUMAN (SESSION_CLOSE_REASON = POLICY_ENFORCED)

- If QUALIFICATION_STATUS == NOT_QUALIFIED
  → CLOSED_DISQUALIFIED (SESSION_CLOSE_REASON = QUALIFICATION_FAILED)

- If NEGOTIATION_STATE == TERMINATED
  → TERMINATED_BY_CUSTOMER (SESSION_CLOSE_REASON = CUSTOMER_EXIT)

- If PRICE_LADDER_STATE == FINAL_PRICE_REACHED
  AND QUOTE_REQUIRED_FLAG == FALSE
  AND COMMITMENT_ARTIFACT_STATUS == CONFIRMED
  → CLOSED_SUCCESSFULLY (SESSION_CLOSE_REASON = BOOKING_CONFIRMED)

- If PRICE_LADDER_STATE == FINAL_PRICE_REACHED
  AND COMMITMENT_ARTIFACT_STATUS == PENDING_CONFIRMATION
  → CLOSED_NO_DECISION (SESSION_CLOSE_REASON = NO_RESPONSE_TIMEOUT)
  OR ESCALATED_TO_HUMAN (SESSION_CLOSE_REASON = HUMAN_HANDOVER_REQUIRED)
  (Selection governed by Phase 0 ops policy)

------------------------------------------------------------
5.3) OBJECTION REPETITION GOVERNANCE
------------------------------------------------------------

Phase 4 MUST NOT calculate, detect, or infer objection thresholds.

OBJECTION_REPEAT_COUNT is evaluated strictly as provided by Phase 3.
Threshold definitions and breach detection are owned exclusively by Phase 3.

Phase 4 may only consume the resulting signal to trigger ESCALATED_TO_HUMAN.

============================================================
6) HUMAN HANDOVER GOVERNANCE
============================================================

When HANDOVER_REQUIRED_FLAG == TRUE:

- Automation MUST stop immediately
- No further system messages may be generated
- Full context snapshot must be preserved
- Responsibility transfers to a human operator

Phase 4 does NOT define how humans respond.
It only defines WHEN and WHY handover occurs.

============================================================
7) AUTOMATION TERMINATION GUARANTEE
============================================================

Once AUTOMATION_TERMINATED_FLAG == TRUE:

- No engine may emit further actions
- No follow-up logic may execute
- No silence handling may resume
- No tone or phrase engine may be invoked

This guarantees clean shutdown.

------------------------------------------------------------
7.1) RE-ENGAGEMENT AFTER TERMINATION (NEW SESSION RULE)
------------------------------------------------------------

If the customer sends a new message after AUTOMATION_TERMINATED_FLAG == TRUE:

- The prior session remains terminal and immutable.
- Orchestration MUST open a NEW session context (new SESSION_ID).
- The new session may import a context snapshot for continuity,
  but Phase 4 decisions from the prior session MUST NOT be reversed.

============================================================
8) LOCKING & GOVERNANCE
============================================================

Once Phase 4 is locked:
- No new terminal states may be added
- No closing rules may be weakened
- Changes require Phase 0 governance approval

Phase 4 must be locked BEFORE:
- Tone Engine
- Human Phrase Libraries
- Brand or localization layers

============================================================
END OF PHASE 4 ENGINE
============================================================