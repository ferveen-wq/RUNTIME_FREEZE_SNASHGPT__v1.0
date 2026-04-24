# PHASE 3 — WIRING ADDENDUM (Silence ↔ Follow-Up ↔ PIM) — v1.0

## A) STATE OWNERSHIP (single source of truth)
OWNED BY ORCHESTRATOR (write authority):
- LAST_COUNTED_OUTBOUND_TIMESTAMP
- LAST_CUSTOMER_SIGNAL_TIMESTAMP
- FOLLOW_UP_COUNT
- INPUT_MODE (LIVE | BACKFILL_BATCH)
- SILENCE_SUPPRESSED (bool) + SILENCE_SUPPRESSION_REASON (enum)

## SILENCE_SUPPRESSION_REASON — ENUM VALUES (LOCKED CATALOG)

Purpose:
- Standardize why silence follow-ups are blocked.
- Orchestrator is the single authority that sets SILENCE_SUPPRESSED + SILENCE_SUPPRESSION_REASON.
- Silence Engine remains unchanged (it only blocks when SILENCE_SUPPRESSED == TRUE).

Allowed values:
- NONE
- PIM_THINKING              # “I’ll think about it / let me decide / I will get back to you”
- PIM_CHECK_WITH_PARTNER     # “I’ll check with my wife/husband/family”
- PIM_TRAVELLING             # “I am travelling / out of country / busy days”
- PIM_CAR_NOT_AVAILABLE      # “Car is in garage / not with me / not received yet”
- PIM_TIMING_LATER           # “Next month / after salary / later this year”
- VISIT_SCHEDULED            # visit scheduling already active
- MANUAL_HOLD                # internal hold by ops/agent
- AGENT_TAKEOVER             # human takeover in progress
- CONVERSATION_NOT_OPEN      # closed/disqualified

Notes:
- PIM_* reasons are used when customer intent is still positive/neutral but timing is deferred.
- If multiple reasons apply, choose the strongest blocker in this order:
  VISIT_SCHEDULED > MANUAL_HOLD > AGENT_TAKEOVER > PIM_* > NONE

## A.2) SILENCE SUPPRESSION REASON (ENUM) (LOCKED)

SILENCE_SUPPRESSED is owned by ORCHESTRATOR.
When SILENCE_SUPPRESSED == TRUE, ORCHESTRATOR MUST also set SILENCE_SUPPRESSION_REASON.

Allowed enum values (canonical):
- PIM_TRAVELLING                 # customer travelling / out of country / not available
- PIM_CHECKING_WITH_SPOUSE       # "I'll check with my wife/husband"
- PIM_CAR_UNAVAILABLE            # car in garage / workshop / not with customer
- PIM_TIMING_NOT_READY           # "not now", "later", "next month"
- VISIT_SCHEDULED                # visit booking or scheduling active
- MANUAL_HOLD                    # internal manual hold / ops hold
- OTHER                          # last resort, must be explainable in notes

Rules:
- This enum is for audit + governance only.
- Silence Engine reads only SILENCE_SUPPRESSED (boolean) as a hard blocker.

- CONVERSATION_STATUS (OPEN/CLOSED/DISQUALIFIED)
- AGENT_TAKEOVER_FLAG

OWNED BY SILENCE_ENGINE (write authority):
- SILENCE_STAGE (NONE|S1|S2|S3)
- SILENCE_ACTIVE (bool)
- ALLOW_ACTION (bool)
- EXIT_FLAG (bool)

## A.1) PHASE 3 CANONICAL KEYS + MAPPING LAYER (LOCKED)

Purpose:
- Prevent cross-engine key mismatches (case/spelling) from breaking routing.
- Engines may emit their native keys, but the ORCHESTRATOR must normalize into canonical keys.

Non-negotiable rules:
- Do NOT rename keys inside locked engines to “make it match”.
- The ORCHESTRATOR performs normalization once, immediately after reading engine outputs.
- After normalization, ONLY canonical keys are used for routing/state decisions.

### Canonical keys (Phase 3)
Canonical keys use SHOUT_CASE for cross-file consistency:

- QUALIFICATION_STATUS
- NEGOTIATION_STATE
- PRICE_LADDER_STATE
- OBJECTION_SIGNAL

Control flags (canonical):
- QUOTE_REQUIRED_FLAG
- AUTOMATION_ALLOWED_FLAG

Analytics / safety counters (canonical):
- OBJECTION_REPEAT_COUNT
- CUSTOMER_RESPONSE_LATENCY

### Engine → Canonical mappings (single source of truth)
Apply these mappings immediately after reading outputs:

Objection Resolution Engine (native → canonical):
- qualification_status        → QUALIFICATION_STATUS
- negotiation_state           → NEGOTIATION_STATE
- price_ladder_state          → PRICE_LADDER_STATE
- objection_signal            → OBJECTION_SIGNAL
- quote_required              → QUOTE_REQUIRED_FLAG
- automation_allowed          → AUTOMATION_ALLOWED_FLAG
- objection_repeat_count      → OBJECTION_REPEAT_COUNT
- customer_response_latency   → CUSTOMER_RESPONSE_LATENCY

Price Ladder Engine (already canonical / no-op):
- QUALIFICATION_STATUS        → QUALIFICATION_STATUS
- NEGOTIATION_STATE           → NEGOTIATION_STATE
- PRICE_LADDER_STATE          → PRICE_LADDER_STATE
- QUOTE_REQUIRED_FLAG         → QUOTE_REQUIRED_FLAG

Objection Resolution Engine (native → canonical):
- qualification_status        -> QUALIFICATION_STATUS
- negotiation_state           -> NEGOTIATION_STATE
- price_ladder_state          -> PRICE_LADDER_STATE
- objection_signal            -> OBJECTION_SIGNAL
- quote_required              -> QUOTE_REQUIRED_FLAG
- automation_allowed          -> AUTOMATION_ALLOWED_FLAG

Silence Handling Engine (separate domain; no quote flag required):
- SILENCE_STAGE / SILENCE_ACTIVE / ALLOW_ACTION / EXIT_FLAG remain as-is in this file.

### Normalization precedence rule
If both native + canonical versions exist at the same time:
- Canonical wins.
- Native is ignored after mapping.

STATUS: LOCKED
LOCK_REASON:
- Prevents hidden cross-file bugs due to key naming mismatch
- Avoids modifying locked engines (Phase 3 engines remain untouched)

## B) CUSTOMER SIGNAL GATE (non-negotiable)
Update LAST_CUSTOMER_SIGNAL_TIMESTAMP ONLY when:
- new customer message OR
- new screenshot that contains customer message OR
- call/visit/audio note summary that confirms customer interaction

Do NOT update timestamps for:
- re-pasted old transcript
- internal drafting / translation / “should we follow up?”
- assistant-only notes without new customer interaction

## C) CALL TRIGGERS
Call SILENCE_ENGINE when:
1) runtime_tick
2) outbound_sent AND outbound_is_counted == TRUE
3) inbound_customer_signal (for reset evaluation)

## D) HARD BLOCKERS (must be checked before calling)
If any is true → do not allow silence actions:
- CONVERSATION_STATUS != OPEN
- AGENT_TAKEOVER_FLAG == TRUE
- INPUT_MODE == BACKFILL_BATCH
- SILENCE_SUPPRESSED == TRUE
- NEGOTIATION_ACTIVE == TRUE
- VISIT_SCHEDULING_ACTIVE == TRUE

## E) FOLLOW-UP ENGINE PRECEDENCE (must not conflict)
FOLLOW_UP_ENGINE may run ONLY IF:
- explicit_followup_request == TRUE
- AND silence_active == FALSE
- AND silence_window != S3_LONG
(aligns with Follow-Up engine blockers)