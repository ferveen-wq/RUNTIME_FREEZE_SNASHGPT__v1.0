Status: Locked
Version: v1.0.1
Last Updated: 2026-01-10
Lock Reason: Orchestration stage sealed (Qualification gate enforced; no bypass; no pricing logic)

# RUNTIME_STATE_MACHINE.md
Status: LOCKED (runtime state authority)
Role: Defines runtime states, transitions, and failure handling.
Scope: Control states only (no customer phrasing, no business logic, no pricing).

---

## 0) Purpose
This file defines:
- The allowed runtime states
- The only allowed transitions between states
- What happens when something fails (load-time vs execution-time)
- Recovery rules and when to halt

This file does NOT:
- Define file inventory (manifest owns that)
- Define response formatting (OUTPUT_RESPONSE_TEMPLATE owns that)
- Implement engine logic

## RUNTIME STATE — SILENCE CONTROL FIELDS (Phase 3)

These fields are required to support the Global Silence Gate (Execution Flow Step 0.5)
and `SILENCE_HANDLING_ENGINE.md`.

### Timestamps
- LAST_COUNTED_OUTBOUND_TIMESTAMP
  - Meaning: Timestamp of the last outbound message that EXPECTS a customer reply.
  - Writer: Runtime Orchestrator (on counted outbound send)
  - Reader: Silence Engine (time delta computation)

- LAST_CUSTOMER_SIGNAL_TIMESTAMP
  - Meaning: Timestamp of last explicit NEW customer communication signal.
  - Writer: Intake / Orchestrator (ONLY when new customer signal is detected)
  - Reader: Silence Engine (silence reset condition)

### Counters
- FOLLOW_UP_COUNT
  - Meaning: Number of silence-permitted follow-up actions actually SENT in the current silence cycle.
  - Writer: Orchestrator / Dispatcher (ONLY when follow-up is sent)
  - Reader: Silence Engine (cap enforcement)

### Mode / Suppression
- INPUT_MODE
  - Allowed: LIVE | BACKFILL_BATCH
  - Meaning: Whether current processing is live customer interaction or backfilled transcript batch.
  - Writer: Intake / Orchestrator
  - Reader: Silence Engine (backfill must not permit actions)

- SILENCE_SUPPRESSED
  - Allowed: TRUE | FALSE
  - Meaning: If TRUE, silence actions are blocked (e.g., PIM / visit scheduled / manual hold).
  - Writer: Orchestrator (based on upstream signals)
  - Reader: Silence Engine (hard blocker)

- SILENCE_TERMINATED
  - Allowed: TRUE | FALSE
  - Meaning: Terminal stop flag after S3 or follow-up cap reached.
  - Writer: Orchestrator (on EXIT_FLAG) and/or Silence Engine output application
  - Reader: Orchestrator (prevents repeated silence actions until new customer signal)

### Governance Flags (already used elsewhere, but required for silence gating)
- AGENT_TAKEOVER_FLAG
  - Allowed: TRUE | FALSE
  - Meaning: Human agent takeover; blocks silence actions.
  - Writer: Runtime / Ops
  - Reader: Orchestrator + Silence Engine (blocker)

- CONVERSATION_STATUS
  - Allowed: OPEN | CLOSED | DISQUALIFIED
  - Meaning: Conversation lifecycle state; non-OPEN blocks silence actions.
  - Writer: Orchestrator
  - Reader: Orchestrator + Silence Engine (blocker)

------------------------------------------------------------
0.6) Phase 4 Terminal Governance (Conversation-Level)
------------------------------------------------------------

Phase 4 is the only authority that may set terminal outcomes.

Required control flags (produced by Phase 4; enforced by Orchestrator):

- FINAL_CONVERSATION_STATE (ENUM)
  - Allowed:
    - CLOSED_SUCCESSFULLY
    - CLOSED_NO_DECISION
    - CLOSED_DISQUALIFIED
    - ESCALATED_TO_HUMAN
    - TERMINATED_BY_SYSTEM
    - TERMINATED_BY_CUSTOMER

- AUTOMATION_TERMINATED_FLAG (BOOL)
  - Allowed: TRUE | FALSE
  - Meaning: If TRUE, automation must stop immediately (no engines, no phrasing, no follow-ups)

- HANDOVER_REQUIRED_FLAG (BOOL)
  - Allowed: TRUE | FALSE
  - Meaning: If TRUE, human takeover is required and automation must stop

Mapping rule (Phase 4 → CONVERSATION_STATUS):

- If FINAL_CONVERSATION_STATE == CLOSED_DISQUALIFIED
  → CONVERSATION_STATUS = DISQUALIFIED

- If FINAL_CONVERSATION_STATE IN (
    CLOSED_SUCCESSFULLY,
    CLOSED_NO_DECISION,
    ESCALATED_TO_HUMAN,
    TERMINATED_BY_SYSTEM,
    TERMINATED_BY_CUSTOMER
  )
  → CONVERSATION_STATUS = CLOSED

Hard rule:
- Once CONVERSATION_STATUS != OPEN, silence actions are blocked.
- Once AUTOMATION_TERMINATED_FLAG == TRUE, no automation may resume in the same session.
---

## 1) States (authoritative)
### S0 — BOOT
System started, nothing loaded yet.

### S1 — LOAD_MANIFEST
Load and validate the Runtime Manifest.

### S2 — LOAD_COMPONENTS
Load doctrine, routing, engines, ops helpers in the order defined by the Execution Flow.

### S3 — VALIDATE_RUNTIME
Run final validation gate:
- required files present
- locks respected
- checklist expectations satisfied
- dependencies consistent

#### Required Orchestration Signals (Validation Only)
During VALIDATE_RUNTIME, confirm the runtime set contains engines/contracts that guarantee these signals can exist when applicable:

- QUALIFICATION_STATUS (from QUALIFICATION_ENGINE)
- negotiation_state (from NEGOTIATION_LOGIC_MODULE)
- price_ladder_state (from PRICE_LADDER_ENGINE)
- objection_signal, objection_repeat_count, customer_response_latency (from CUSTOMER_CHAT_INTAKE_RULES)
- decision object (from OBJECTION_RESOLUTION_ENGINE)

Note:
- This state machine does NOT implement these signals.
- It only validates that the runtime bundle contains the required files/contracts so these signals are possible at execution time.

### S4 — ACTIVE
Runtime is ready and can process customer messages.
ACTIVE execution must follow `RUNTIME_EXECUTION_FLOW.md` for every inbound customer message.

Enforcement inside ACTIVE:
- Apply Intake (`CUSTOMER_CHAT_INTAKE_RULES.md`) → then call Qualification (`QUALIFICATION_ENGINE.md`)
- Do NOT call Negotiation unless: QUALIFICATION_STATUS = READY_FOR_NEGOTIATION
- If QUALIFICATION_STATUS is missing / incomplete / not-ready → route to clarification or graceful exit (no forward progression)

- Do NOT execute any engine if: CONVERSATION_STATUS != OPEN
- Do NOT execute any engine if: AUTOMATION_TERMINATED_FLAG == TRUE
- If HANDOVER_REQUIRED_FLAG == TRUE:
  - Set AGENT_TAKEOVER_FLAG = TRUE
  - Stop automation immediately (handover to human; no further system actions)


### S5 — DEGRADED
Runtime can still respond, but with reduced capability (safe mode).
Allowed only for execution-time issues, not load-time missing required files.


### S6 — HALT
Runtime stopped. No customer message processing allowed.

---

## 2) Allowed Transitions (only these)
BOOT → LOAD_MANIFEST  
LOAD_MANIFEST → LOAD_COMPONENTS  
LOAD_COMPONENTS → VALIDATE_RUNTIME  
VALIDATE_RUNTIME → ACTIVE  

ACTIVE → DEGRADED  
DEGRADED → ACTIVE (only after recovery validation passes)

Any state → HALT (only when a hard stop condition is met)

No other transitions are allowed.

---

## 3) Hard Stop Conditions (must HALT)
If any of the following occurs, transition immediately to HALT:
1) Manifest missing / unreadable
2) Any REQUIRED file missing at load-time
3) Lock conflict with locked doctrine (sequencing-impacting conflict)
4) Checklist is not PASSED for current build
5) Validation gate fails in S3

HALT behavior:
- Stop runtime
- Emit internal error only (no customer-facing text)

------------------------------------------------------------
3.1) Customer Re-Engagement After Termination (Session Rule)
------------------------------------------------------------

If the customer sends a new message after:
- AUTOMATION_TERMINATED_FLAG == TRUE
or
- CONVERSATION_STATUS != OPEN

Then:
- The prior session remains terminal and immutable
- Orchestration MUST open a NEW session context (new SESSION_ID)
- The new session may import a context snapshot for continuity
- Phase 4 outcomes from the prior session MUST NOT be reversed

---

## 4) Degraded Mode Conditions (execution-time only)
ACTIVE → DEGRADED is allowed only if:
- A non-critical engine fails during message processing
- A non-required support component fails
- Minor drift detected that does NOT impact locks or safety

DEGRADED rules:
- Never guess facts
- Ask 1 clarifying question max
- Keep response short and safe
- Continue logging internal errors

## Authority Boundary (non-negotiable)
This file defines runtime states and allowed transitions only.

This file may:
- Reference other stages by name (Runtime Manifest / Execution Flow / Output Formatting Stage)
- Declare hard-stop vs degraded behavior at a control level

This file must NEVER:
- Implement business logic, pricing logic, or qualification criteria
- Override the Runtime Manifest, Execution Flow, Decision Matrix, or Output Template
- Add customer-facing wording or examples

If DEGRADED encounters a hard stop condition → HALT.

---

## 5) Recovery Rules
### 5.1 DEGRADED → ACTIVE
Allowed only if:
- The next execution cycle passes a lightweight validation:
  - required files still present
  - locks still respected
  - engines responding normally

### 5.2 HALT Recovery
HALT cannot auto-recover.
Only a full restart can return to BOOT.

---

## 6) Per-Message State Handling
When in ACTIVE or DEGRADED:
- Each customer message is processed using the Execution Flow
- Output must follow the Output Formatting Stage

If execution fails:
- ACTIVE → DEGRADED (if allowed)
- Otherwise → HALT (if hard stop)

---

## 7) Definition of Done
This file is correct when:
- States are explicit and minimal
- Transitions are deterministic
- Hard-stop vs degraded is clearly separated
- Recovery is strict and non-ambiguous

---
End.