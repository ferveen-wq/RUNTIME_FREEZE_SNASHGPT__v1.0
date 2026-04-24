# SILENCE_HANDLING_ENGINE.md
Version: 1.0
Phase: 3
Window: C
Status: DRAFT → READY FOR LOCK
Scope: Deterministic silence handling (time-based only)

===============================================================================
0) PURPOSE
===============================================================================
This engine governs system behavior when a customer is silent after a counted
outbound message that expects a reply.

This engine:
- Uses time-based thresholds only
- Enforces follow-up caps
- Emits stage + allow/stop flags (no language generation)

This engine does NOT:
- Generate customer-facing language
- Decide tone, persuasion, visuals, hooks, or negotiation actions
- Interpret customer intent (handled elsewhere)

Silence is evaluation phase, not rejection. (legacy principle) [reference only]

## PHASE 0 GUARD — SILENCE HANDLING SCOPE

Rules:
- Silence handling MUST NOT modify pricing, services, or scope
- Silence handling MUST NOT reopen Price Ladder execution
- Silence handling MUST NOT resolve objections (delegated to Objection Engine)
- Silence handling MAY pause, recover, or escalate only
- All inspection, suitability, and service concerns remain upstream or human-handled

===============================================================================
1) ENGINE INTERFACE CONTRACT (UPLOAD-SAFE)
===============================================================================

1.1 INPUTS (READ-ONLY)
- CURRENT_TIMESTAMP
- LAST_COUNTED_OUTBOUND_TIMESTAMP          # outbound that expects customer reply
- LAST_CUSTOMER_SIGNAL_TIMESTAMP           # updates ONLY on real customer signal
- FOLLOW_UP_COUNT                          # increments ONLY when follow-up actually SENT
- INPUT_MODE                               # LIVE | BACKFILL_BATCH
- SILENCE_SUPPRESSED                       # True | False (e.g., PIM/Visit/Manual hold)
- CONVERSATION_STATUS                      # OPEN | CLOSED | DISQUALIFIED
- AGENT_TAKEOVER_FLAG                      # True | False
- NEGOTIATION_ACTIVE                       # True | False (read-only blocker)
- VISIT_SCHEDULING_ACTIVE                  # True | False (read-only blocker)

1.2 OUTPUTS (WRITE)
- SILENCE_STAGE                            # NONE | S1 | S2 | S3
- SILENCE_ACTIVE                           # True | False
- ALLOW_ACTION                             # True | False
- EXIT_FLAG                                # True | False

1.3 HARD BLOCKERS (NO ACTION)
If any is true → ALLOW_ACTION=False, EXIT_FLAG=False, SILENCE_ACTIVE=False:
- CONVERSATION_STATUS != OPEN
- AGENT_TAKEOVER_FLAG == True
- SILENCE_SUPPRESSED == True
- INPUT_MODE == BACKFILL_BATCH
- NEGOTIATION_ACTIVE == True
- VISIT_SCHEDULING_ACTIVE == True

1.4 COUNTER + TIMESTAMP INTEGRITY (NON-NEGOTIABLE)
- LAST_CUSTOMER_SIGNAL_TIMESTAMP updates ONLY on explicit new customer communication signal
  (new customer message / new screenshot with customer message / call-note / visit-note / audio summary).
- Re-pasted transcripts, internal drafting, translation, planning, or “should we follow up?”
  MUST NOT update LAST_CUSTOMER_SIGNAL_TIMESTAMP.
- FOLLOW_UP_COUNT increments ONLY when a follow-up is actually SENT to customer.
  Drafting/approval/rewriting MUST NOT increment FOLLOW_UP_COUNT.

===============================================================================
2) PARAMETERS (READ FROM PARAM TABLE)
===============================================================================
This engine reads its thresholds/caps from a parameter table.

PARAM KEYS (required):
- SILENCE_S1_HOURS              # default 6
- SILENCE_S2_HOURS              # default 24
- SILENCE_S3_HOURS              # default 72
- SILENCE_MAX_FOLLOWUPS         # default 2
- SILENCE_ROTATION_MAX_S1       # default 99 (rotation index ceiling)
- SILENCE_ROTATION_MAX_S2       # default 99

If params missing → use defaults above.

===============================================================================
3) STAGE DEFINITIONS (TIME-BASED)
===============================================================================

Let:
- OUTBOUND_AGE_HOURS = hours(CURRENT_TIMESTAMP - LAST_COUNTED_OUTBOUND_TIMESTAMP)

Precondition for any silence stage evaluation:
- LAST_COUNTED_OUTBOUND_TIMESTAMP exists
- CURRENT_TIMESTAMP >= LAST_COUNTED_OUTBOUND_TIMESTAMP
- No new customer signal since LAST_COUNTED_OUTBOUND_TIMESTAMP:
    LAST_CUSTOMER_SIGNAL_TIMESTAMP <= LAST_COUNTED_OUTBOUND_TIMESTAMP
  (or LAST_CUSTOMER_SIGNAL_TIMESTAMP is null)

If precondition fails → SILENCE_STAGE=NONE, SILENCE_ACTIVE=False.

Stage mapping (parameterized):
- If OUTBOUND_AGE_HOURS < SILENCE_S1_HOURS → NONE
- If SILENCE_S1_HOURS <= OUTBOUND_AGE_HOURS < SILENCE_S2_HOURS → S1
- If SILENCE_S2_HOURS <= OUTBOUND_AGE_HOURS < SILENCE_S3_HOURS → S2
- If OUTBOUND_AGE_HOURS >= SILENCE_S3_HOURS → S3

===============================================================================
4) FOLLOW-UP ALLOWANCE (CAPS)
===============================================================================

Global cap:
- If FOLLOW_UP_COUNT >= SILENCE_MAX_FOLLOWUPS → force S3 behavior (stop).

Allowance rule:
- If SILENCE_STAGE in {S1,S2} AND FOLLOW_UP_COUNT < SILENCE_MAX_FOLLOWUPS
  → ALLOW_ACTION=True
- Else → ALLOW_ACTION=False

Notes:
- Engine does not send messages; it only permits a single action.
- Downstream dispatcher decides templates/tone.

===============================================================================
5) ROTATION COUNTERS (STAGE-SCOPED)
===============================================================================

Engine exposes rotation guidance (no content):

State (stored outside engine):
- SILENCE_ROTATION_INDEX_S1 (int)
- SILENCE_ROTATION_INDEX_S2 (int)

Rules:
- If SILENCE_STAGE==S1 and ALLOW_ACTION==True:
    increment SILENCE_ROTATION_INDEX_S1 by 1 (wrap to 1 after SILENCE_ROTATION_MAX_S1)
- If SILENCE_STAGE==S2 and ALLOW_ACTION==True:
    increment SILENCE_ROTATION_INDEX_S2 by 1 (wrap to 1 after SILENCE_ROTATION_MAX_S2)
- Rotation resets to 0 when a NEW customer signal arrives.

===============================================================================
6) TERMINAL RULES (STOP / EXIT)
===============================================================================

If SILENCE_STAGE==S3 OR FOLLOW_UP_COUNT >= SILENCE_MAX_FOLLOWUPS:
- EXIT_FLAG=True
- ALLOW_ACTION=False
- SILENCE_ACTIVE=False
- Set external state: SILENCE_TERMINATED=True

No further silence actions allowed until a NEW customer signal arrives.

===============================================================================
7) BACKFILL BATCH HANDLING (HISTORICAL)
===============================================================================

If INPUT_MODE == BACKFILL_BATCH:
- This engine MUST NOT permit actions.
- ALLOW_ACTION=False, EXIT_FLAG=False
- SILENCE_STAGE may be computed for audit only, but must not drive outbound sends.

===============================================================================
8) AUDIT LOG (APPEND-ONLY)
===============================================================================

Each evaluation that changes any of these must log:
- Conversation_ID
- CURRENT_TIMESTAMP
- LAST_COUNTED_OUTBOUND_TIMESTAMP
- LAST_CUSTOMER_SIGNAL_TIMESTAMP
- OUTBOUND_AGE_HOURS
- SILENCE_STAGE
- FOLLOW_UP_COUNT
- SILENCE_ROTATION_INDEX_S1 / S2 (if applicable)
- ALLOW_ACTION
- EXIT_FLAG
- BLOCKER_TRIGGERED (if any; which blocker: CLOSED | TAKEOVER | SUPPRESSED | BACKFILL | OTHER)
- PARAMS snapshot (S1/S2/S3 hours, max followups)
- CONVERSATION_STATUS
- AGENT_TAKEOVER_FLAG
- SILENCE_SUPPRESSED
- INPUT_MODE
- SILENCE_TERMINATED

### AUDIT-ONLY ANALYTICS TAGS (no behavior impact)
- SILENCE_CYCLE_ID (increment per new counted outbound that expects reply)
- SILENCE_ORIGIN_PHASE (QUALIFICATION | NEGOTIATION | PRICING | OBJECTION)
- SILENCE_ORIGIN_ENGINE (engine name)
- SILENCE_STAGE_MAX_REACHED (NONE | S1 | S2 | S3)

===============================================================================
9) LOCK CONDITIONS
===============================================================================

Engine may be LOCKED when:
- Parameter keys confirmed
- Blockers confirmed (PIM suppression + backfill + takeover + closed)
- Counters/timestamps integrity rules accepted
- Outputs match runtime needs (stage/allow/exit)

END OF SILENCE_HANDLING_ENGINE.md v1.0

---
LOCK STATUS: LOCKED
LOCK VERSION: v1.0
LOCK DATE: 2026-01-08
LOCK SCOPE: Phase 3 — Silence Handling
LOCK NOTES:
- Runtime wiring verified
- State machine fields verified
- Execution flow integration verified
- Audit-only analytics tags verified
- No customer-facing phrasing
- No pricing, negotiation, or objection logic present
---