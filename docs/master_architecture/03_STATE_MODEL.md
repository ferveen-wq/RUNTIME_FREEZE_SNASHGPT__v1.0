# STATE MODEL
Status: DRAFT
Source Policy: Active runtime files win over legacy, tests, drafts, and archive notes.
Scope: Runtime states, control flags, session rules, and allowed transitions only. No customer-facing wording. No business persuasion logic.

## 0. Purpose

This document defines the runtime state model that controls:
- when runtime may start
- when runtime may continue
- when runtime must stop
- how silence control fields are managed
- how terminal conversation outcomes affect session lifecycle

Primary authority sources:
- `RUNTIME_STATE_MACHINE.md`
- `RUNTIME_EXECUTION_FLOW.md`
- `SILENCE_HANDLING_ENGINE.md`
- `CLOSING_HANDOVER_ENGINE.md`
- `PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md`

---

## 1. Runtime Lifecycle States

[FROM: RUNTIME_STATE_MACHINE.md]

### S0 — BOOT
- system started
- nothing loaded yet

### S1 — LOAD_MANIFEST
- load and validate Runtime Manifest

### S2 — LOAD_COMPONENTS
- load doctrine, routing, engines, ops helpers in execution-flow order

### S3 — VALIDATE_RUNTIME
- final validation gate
- required files present
- locks respected
- checklist expectations satisfied
- dependencies consistent

### S4 — ACTIVE
- runtime is ready
- customer messages may be processed
- ACTIVE execution must follow `RUNTIME_EXECUTION_FLOW.md`

### S5 — DEGRADED
- runtime can still respond, but with reduced capability
- allowed only for execution-time issues

### S6 — HALT
- runtime stopped
- no customer message processing allowed

---

## 2. Allowed Transitions

[FROM: RUNTIME_STATE_MACHINE.md]

Allowed transitions:
- BOOT → LOAD_MANIFEST
- LOAD_MANIFEST → LOAD_COMPONENTS
- LOAD_COMPONENTS → VALIDATE_RUNTIME
- VALIDATE_RUNTIME → ACTIVE
- ACTIVE → DEGRADED
- DEGRADED → ACTIVE
- ANY STATE → HALT

No other transitions are allowed.

---

## 3. Hard Stop Conditions

[FROM: RUNTIME_STATE_MACHINE.md]

Transition immediately to HALT if:
- manifest missing / unreadable
- any required file missing at load-time
- lock conflict with locked doctrine
- checklist not passed for current build
- validation gate fails in S3

HALT behavior:
- stop runtime
- emit internal error only
- no customer-facing text

---

## 4. ACTIVE-State Enforcement

[FROM: RUNTIME_STATE_MACHINE.md]

Inside ACTIVE:
- apply Intake
- then call Qualification
- enforce Intake → Qualification ordering on every inbound customer turn
- do not call Negotiation unless `QUALIFICATION_STATUS = READY_FOR_NEGOTIATION`
- if `QUALIFICATION_STATUS` is missing / incomplete / not-ready:
  - route to clarification or graceful exit
  - no forward progression into negotiation, pricing, objection handling, or closing

Do not execute any engine if:
- `CONVERSATION_STATUS != OPEN`
- `AUTOMATION_TERMINATED_FLAG == TRUE`

If `HANDOVER_REQUIRED_FLAG == TRUE`:
- set `AGENT_TAKEOVER_FLAG = TRUE`
- stop automation immediately
- no further system actions

---

## 5. Silence Control Fields

[FROM: RUNTIME_STATE_MACHINE.md]
[FROM: RUNTIME_EXECUTION_FLOW.md]
[FROM: SILENCE_HANDLING_ENGINE.md]
[FROM: PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md]

### LAST_COUNTED_OUTBOUND_TIMESTAMP
Meaning:
- timestamp of the last outbound message that expects customer reply

Writer:
- Runtime Orchestrator

Reader:
- Silence Handling Engine

### LAST_CUSTOMER_SIGNAL_TIMESTAMP
Meaning:
- timestamp of last explicit new customer communication signal

Writer:
- Intake / Orchestrator

Reader:
- Silence Handling Engine

Update only when:
- new customer message
- new screenshot with customer message
- call / visit / audio note summary confirming customer interaction

Do not update for:
- re-pasted old transcript
- internal drafting / translation / planning
- assistant-only notes

### FOLLOW_UP_COUNT
Meaning:
- number of silence-permitted follow-up actions actually sent in current silence cycle

Writer:
- Orchestrator / Dispatcher

Reader:
- Silence Handling Engine

### INPUT_MODE
Allowed:
- LIVE
- BACKFILL_BATCH

Writer:
- Intake / Orchestrator

### SILENCE_SUPPRESSED
Allowed:
- TRUE
- FALSE

Writer:
- Orchestrator

### SILENCE_SUPPRESSION_REASON
Writer:
- Orchestrator only

Canonical values from wiring addendum:
- NONE
- PIM_THINKING
- PIM_CHECK_WITH_PARTNER
- PIM_TRAVELLING
- PIM_CAR_NOT_AVAILABLE
- PIM_TIMING_LATER
- VISIT_SCHEDULED
- MANUAL_HOLD
- AGENT_TAKEOVER
- CONVERSATION_NOT_OPEN

### SILENCE_TERMINATED
Allowed:
- TRUE
- FALSE

Writer:
- Orchestrator and/or Silence Engine output application

---

## 6. Governance Flags

[FROM: RUNTIME_STATE_MACHINE.md]

### AGENT_TAKEOVER_FLAG
Allowed:
- TRUE
- FALSE

Meaning:
- human takeover
- blocks silence actions

### CONVERSATION_STATUS
Allowed:
- OPEN
- CLOSED
- DISQUALIFIED

Writer:
- Orchestrator

Rule:
- non-OPEN blocks silence actions
- non-OPEN blocks further engine execution

---

## 7. Terminal Conversation Control Signals

[FROM: RUNTIME_STATE_MACHINE.md]
[FROM: CLOSING_HANDOVER_ENGINE.md]

### FINAL_CONVERSATION_STATE
Allowed:
- CLOSED_SUCCESSFULLY
- CLOSED_NO_DECISION
- CLOSED_DISQUALIFIED
- ESCALATED_TO_HUMAN
- TERMINATED_BY_SYSTEM
- TERMINATED_BY_CUSTOMER

### AUTOMATION_TERMINATED_FLAG
Allowed:
- TRUE
- FALSE

Meaning:
- stop immediately
- no engines
- no phrasing
- no follow-ups
- no resume in same session

### HANDOVER_REQUIRED_FLAG
Allowed:
- TRUE
- FALSE

Meaning:
- human takeover required
- automation must stop

### HANDOVER_REASON
- emitted by closing/handover layer

### SESSION_CLOSE_REASON
- emitted by closing/handover layer

---

## 8. Terminal-State Mapping

[FROM: RUNTIME_STATE_MACHINE.md]

If `FINAL_CONVERSATION_STATE == CLOSED_DISQUALIFIED`
- `CONVERSATION_STATUS = DISQUALIFIED`

If `FINAL_CONVERSATION_STATE` is one of:
- CLOSED_SUCCESSFULLY
- CLOSED_NO_DECISION
- ESCALATED_TO_HUMAN
- TERMINATED_BY_SYSTEM
- TERMINATED_BY_CUSTOMER

Then:
- `CONVERSATION_STATUS = CLOSED`

Hard rules:
- once `CONVERSATION_STATUS != OPEN`, silence actions are blocked
- once `AUTOMATION_TERMINATED_FLAG == TRUE`, no automation may resume in same session

---

## 9. Session Re-Engagement Rule

[FROM: RUNTIME_STATE_MACHINE.md]

If customer sends a new message after:
- `AUTOMATION_TERMINATED_FLAG == TRUE`
or
- `CONVERSATION_STATUS != OPEN`

Then:
- prior session remains terminal and immutable
- orchestration must open a new session context
- new session may import context snapshot for continuity

Session continuity rule:
- A new session may import a context snapshot for continuity only from explicit carried-forward context.
- Valid continuity sources are:
  - pasted transcript history
  - approved context snapshot
  - structured carry-forward fields produced by runtime/orchestration
- Hidden chat memory or reconstruction assumptions must not be treated as runtime session state.

Implication:
- prior session remains terminal
- continuity in a new session is explicit and imported, not implicitly resumed
- prior outcomes must not be reversed

---

## 10. Execution-Critical Runtime Signals

[FROM: RUNTIME_STATE_MACHINE.md]

Runtime must support these signals when applicable:
- `QUALIFICATION_STATUS`
- `negotiation_state`
- `price_ladder_state`
- `objection_signal`
- `objection_repeat_count`
- `customer_response_latency`
- decision object
- silence outputs
- terminal conversation outputs

This state model validates their existence as runtime contracts.
It does not implement engine logic or business logic.

