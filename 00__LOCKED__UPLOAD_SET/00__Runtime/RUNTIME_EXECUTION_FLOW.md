Status: Locked
Version: v1.0.0
Last Updated: 2026-01-06
Lock Reason: Orchestration stage sealed (Qualification gate enforced; no bypass; no pricing logic)

# RUNTIME_EXECUTION_FLOW.md
Status: LOCKED (sequencing authority)
Role: Defines the only allowed runtime load + execution order.
Scope: Sequencing only (no customer phrasing, no marketing content, no examples).

## Authority Boundary (non-negotiable)
This file defines sequencing only.

This file may:
- Reference other stages by name (Manifest / Qualification Stage / Output Formatting Stage)
- State preconditions and failure handling at a sequencing level

This file must NEVER:
- Implement business logic, pricing logic, or qualification criteria
- Override the Runtime Manifest, State Machine, Decision Matrix, or Output Template
- Add customer-facing wording or examples

---

## Runtime Execution Sequence (Strict)

The following sequence is mandatory and deterministic.
Any failure at any step MUST immediately stop execution.

### Step 1 — Load Version Contract (Gatekeeper)
- Load `RUNTIME_VERSION_CONTRACT.md`
- Validate:
  - All required runtime files exist
  - All required versions match exactly
- If validation fails:
  - STOP execution
  - Return version mismatch report
- No fallback, no partial execution allowed

### Step 2 — Load Runtime Manifest
- Load `RUNTIME_LOAD_MANIFEST.md`
- Confirm runtime load order
- Confirm runtime file count and categories
- If mismatch with Version Contract:
  - STOP execution

### Step 3 — Initialize Runtime State Machine
- Load `RUNTIME_STATE_MACHINE.md`
- Set initial runtime state
- Prepare allowed state transitions

### Step 4 — Load Runtime Core Bundle
- Load `KNOWLEDGE__RUNTIME_CORE_BUNDLE.md`
- Lock runtime knowledge snapshot for this execution
### Step 4.5 📚 Load Customer Knowledge Bundle
- Load `bundles/customer_knowledge/KNOWLEDGE__CUSTOMER_KNOWLEDGE_BUNDLE.md`
- Merge into active runtime knowledge snapshot (read-only)

### Step 5 — Intake Processing
- Apply `CUSTOMER_CHAT_INTAKE_RULES.md`
- Extract structured inputs from raw customer message

### Step 6 — Qualification & Routing
- Apply `QUALIFICATION_ENGINE.md` (as defined/loaded via the Runtime Manifest)
- Qualification MUST produce an explicit status signal (e.g., QUALIFICATION_STATUS)
- Runtime MUST NOT proceed to Negotiation unless QUALIFICATION_STATUS = READY_FOR_NEGOTIATION

- Qualification output MUST include (for downstream routing/assembly):
  - active_service_context
  - detected_service_intent_in_message
- These two fields MUST be forwarded into the Phase 4.8 Assembly Input set without mutation.

Order of operations (MANDATORY):
1) Compute detected_service_intent_in_message from current message.
2) Preserve active_service_context from conversation state (last confirmed service).
3) Run Phase 4.8 Service Context Continuity Gate BEFORE any update to active_service_context.
3A) Service Context Continuity Gate — HARD STOP (MANDATORY)
- If the Phase 4.8 Service Context Continuity Gate triggers:
  - STOP the pipeline for this turn (do not execute Phase 6, Phase 3, Phase 7, or hooks).
  - Output MUST be ONLY:
    PHASE4_6_HUMAN_PHRASE_LIBRARY.md → L.3 SERVICE CONTEXT CLARIFIER (ONE QUESTION)
  - Do NOT include any service explanations, pricing, or technical answers in the same turn.
  - Do NOT mutate active_service_context on this turn.
- Resume normal routing ONLY on the next customer reply.
4) Only after customer explicitly confirms switching services may active_service_context be updated.

### Phase 3A (Qualifier-First) — REQUIRED BEFORE Phase 3B

Order rule (HARD):
- After Phase 0–2 has produced READY state (vehicle_model + vehicle_year present)
- And Phase 3 begins (price/scope/objection/compare flows)
- Run Phase 3A Qualifier-First Gate BEFORE Phase 3B pricing/SKU logic.

If phase3a_required == true:
- Assembly must output exactly one Phase 3A qualifier question and STOP.
- Phase 3B must not execute until the customer replies (phase3a_complete == true).

If phase3a_complete == true:
- Proceed to Phase 3B pricing/SKU selection and subsequent Phase 4 responses.

### Step 0.5 — Global Silence Gate (Phase-Agnostic)

Purpose:
- Silence handling applies in ALL phases (Qualification, Negotiation, Pricing, Objection).
- Silence is time-based only and must not be tied to post-pricing.

Required Runtime State (must exist in State Machine / runtime store):
- LAST_COUNTED_OUTBOUND_TIMESTAMP
- LAST_CUSTOMER_SIGNAL_TIMESTAMP
- FOLLOW_UP_COUNT
- SILENCE_SUPPRESSED (bool)
- INPUT_MODE (LIVE | BACKFILL_BATCH)
- CONVERSATION_STATUS (OPEN | CLOSED | DISQUALIFIED)
- AGENT_TAKEOVER_FLAG (bool)

Customer Signal Gate (non-negotiable):
- Update LAST_CUSTOMER_SIGNAL_TIMESTAMP ONLY when there is explicit NEW customer communication:
  - new customer text
  - new screenshot containing customer message
  - confirmed call / visit / whatsapp audio summary containing customer response
- Do NOT update LAST_CUSTOMER_SIGNAL_TIMESTAMP for:
  - re-pasted old transcripts
  - internal drafting / translation / planning / “should we follow up?”

Counted Outbound Rule:
- Update LAST_COUNTED_OUTBOUND_TIMESTAMP ONLY when the system sends an outbound message
  that expects a customer reply (quote/question/booking/confirmation request).

Blockers (if any true → do not run silence actions):
- CONVERSATION_STATUS != OPEN
- AGENT_TAKEOVER_FLAG == TRUE
- SILENCE_SUPPRESSED == TRUE (e.g., PIM / visit scheduled / manual hold)
- INPUT_MODE == BACKFILL_BATCH

Execution:
- Invoke `SILENCE_HANDLING_ENGINE.md` to compute:
  - SILENCE_STAGE
  - ALLOW_ACTION
  - EXIT_FLAG

Outcomes:
- If EXIT_FLAG == TRUE → stop outbound actions; mark SILENCE_TERMINATED and exit.
- If ALLOW_ACTION == TRUE → allow ONE follow-up action via dispatcher.
- If SILENCE_STAGE == NONE → proceed with normal phase engine selection (Step 6.1+).


### Step 6.1 — Negotiation Logic (Phase 2)
- Execute `NEGOTIATION_LOGIC_MODULE.md`
- Purpose: determine negotiation stage, pressure signals, and whether a pricing-ladder response is required
- No customer phrasing is generated here (logic only)

### Step 6.2 — Price Ladder Execution (Phase 3)
- If Phase 2 indicates pricing response is required:
  - Execute `PRICE_LADDER_ENGINE.md`
- The ladder governs pricing expression and escalation only (no solution steering)

### Step 6.3 ▶ Objection Resolution (Post-Pricing)

- Execute `OBJECTION_RESOLUTION_ENGINE.md`
- Trigger condition:
  - Price has been exposed via PRICE_LADDER_ENGINE
- Inputs consumed:
  - objection_signal
  - objection_repeat_count
  - customer_response_latency
  - price_ladder_state
  - negotiation_state
- Purpose:
  - Decide whether to CONTINUE, PAUSE, ESCALATE, or EXIT
  - Enforce repeat guardrails (silence handled globally in Step 0.5)
- Output:
  - decision object only (no customer-facing text)

  ### Step 6.4 — Closing & Handover (Phase 4)
- Execute `CLOSING_HANDOVER_ENGINE.md`
- Trigger condition:
  - Phase 3 engines have concluded (pricing/objections/silence/PIM outputs are normalized)
- Inputs consumed (canonical only):
  - qualification_status
  - negotiation_state
  - price_ladder_state
  - objection_signal
  - quote_required_flag
  - automation_allowed_flag
  - objection_repeat_count
  - customer_response_latency
  - commitment_artifact_status
- Output (control only; no customer-facing text):
  - final_conversation_state
  - handover_required_flag
  - handover_reason
  - automation_terminated_flag
  - session_close_reason
- Enforcement:
  - If AUTOMATION_TERMINATED_FLAG == TRUE → stop ALL automation immediately (no further engines, no phrasing)

### Step 7 — Execute Runtime Flow
- Follow `RUNTIME_EXECUTION_FLOW.md` (this file)
- Respect state transitions defined in State Machine

### Step 8 — Output Formatting
- Apply `OUTPUT_RESPONSE_TEMPLATE.md`
- Enforce output structure and constraints

### Step 9 — Completion
- Return final output
- End runtime execution cleanly

## 0) Purpose
This file defines:
- The exact runtime ordering from startup → response output
- The separation between load-time and execution-time
- The gating rules (what must be present before the system can answer)
- The failure modes and what happens when something is missing

This file does NOT:
- Implement logic
- Contain customer-facing phrases
- Redefine any locked doctrine
- Duplicate the manifest (manifest is the inventory source of truth)

---

## 1) Hard Preconditions (must be true before runtime starts)
Runtime can begin only if all are true:
1. `RUNTIME_LOAD_MANIFEST.md` exists and is LOCKED
2. `ARCHITECTURE_INTEGRITY_CHECKLIST.md` is PASSED for the current build
3. All required files listed as REQUIRED in the manifest are accessible
4. No “draft” or “partial” runtime files are being loaded as active doctrine

If any precondition fails → runtime stops with a single system error message (internal only).

---

## 2) Load vs Execution (strict separation)
### 2.1 Load-Time
Load-time is:
- Reading and validating the runtime file inventory
- Loading doctrine/engines into memory
- Establishing runtime guards (locks, priority, allowed overrides)

Load-time must complete successfully before any customer message is processed.

### 2.2 Execution-Time
Execution-time is:
- Processing the customer message through the active runtime stack
- Producing a structured output response
- Applying the final output wrapper rules (tone, clarity, language, timestamp)

---

## 3) Single Source of Truth for Inventory
Inventory is not defined here.
Inventory is defined only in:
- `RUNTIME_LOAD_MANIFEST.md`

This file references inventory by categories and required ordering only.

---

## 4) Runtime Load Order (authoritative)
Load order is deterministic and must follow this sequence:

### Phase A — Bootstrap Guards
1. Load `RUNTIME_LOAD_MANIFEST.md`
2. Validate manifest format + required sections
3. Apply LOCK rules from manifest (locked means: cannot be overridden at runtime)

### Phase B — Architecture Control Layer
4. Load architecture control coordination rules (if present as an active file in manifest)
5. Enforce “no new files / no drift” constraints where declared

### Phase C — Doctrine Core
6. Load all CORE doctrine files (in manifest order)
7. Validate each file against checklist rules (format + role boundaries)

### Phase D — Routing / Sequencing Rules
8. Load routing rules that decide which engines run and in what order
9. Validate there is exactly one allowed execution chain (no ambiguous branches unless explicitly defined)

### Phase E — Engines
10. Load engines in this order (unless manifest defines a stricter order):
    a) Qualification / intent detection
    b) Constraint / policy guards
    c) Response composition / assembly
    d) Tone / style normalization
    e) Output structure formatter

### Phase F — Operations / Shadow / Observability
11. Load operational helpers (logging rules, shadow testing toggles, safe fallbacks)
12. Confirm shadow mode status (if enabled) does not change customer-facing meaning

### Phase G — Final Validation Gate
13. Run final “runtime ready” validation:
    - all required components loaded
    - no missing dependencies
    - locks respected
    - checklist assumptions satisfied

If Phase G passes → runtime is ACTIVE.

---

## 5) Execution Flow (what happens per customer message)
For every incoming customer chat:

### Step 1 — Input Capture
- Capture raw customer message
- Preserve original text (no edits)
- Detect language (Arabic / English / mixed)

### Step 2 — Interpretation Layer
- Translate (if needed) into working language for internal processing
- Extract intent and key entities (car, model, year, service, budget, urgency, location, etc.)
- Identify missing info required to quote or proceed

### Step 3 — Qualification Engine
- Run qualification logic via the Qualification Stage (engine defined by the Runtime Manifest)
- Decide:
  - Can we answer now?
  - Do we need a question?
  - Do we need to propose options?

  ### Step 3.5 — Negotiation Gate (routing only)
- If QUALIFICATION_STATUS = READY_FOR_NEGOTIATION → call `NEGOTIATION_LOGIC_MODULE.md`
- If QUALIFICATION_STATUS is missing / incomplete / not-ready → do NOT call negotiation
  - Route to clarification (ask what’s missing) or gracefully exit

### Step 4 — Guardrails / Policy Checks
- - Apply any constraints from doctrine (warranty rules, scope limits, safety constraints)
- Enforce “no hallucination” rule:
  - If we do not know a fact → we ask or we present a range with clear conditions

### Step 5 — Response Assembly
- Build the response content in plain language
- Keep it human, natural, non-robotic
- Prefer short messages that move the chat forward

### Step 6 — Output Formatting
- Produce:
  1) What customer said (interpretation summary)
  2) English translation (if Arabic)
  3) Assessment (what they want + what’s missing)
  4) Suggested reply (Arabic + English, easy to copy)
- Apply final tone and clarity normalization

### Step 7 — Final Output Wrapper
- Append timestamp at the end (required)
- Ensure customer-facing output contains no internal file names or architecture references

---

## 6) Fallback & Failure Modes
### 6.1 Missing Required File at Load-Time
If a REQUIRED file is missing:
- Runtime does not start
- Return internal error with:
  - missing file name
  - manifest section where it was required
  - last successful phase

### 6.2 Engine Failure at Execution-Time
If an engine fails during message processing:
- Do not crash the full runtime
- Use safe fallback response:
  - Ask 1 clarifying question
  - Confirm what we understood
  - Keep customer engaged

### 6.3 Drift Detection
If a file content conflicts with locked doctrine:
- Locked doctrine wins
- Log drift internally
- Continue only if drift does not affect safety or core sequencing

---

## 7) Change Control
Any change to sequencing in this file requires:
1. Checklist re-run
2. Manifest version bump (if ordering impacts load categories)
3. Explicit lock confirmation

---
## 1) Runtime States (minimal control states)

- INIT
- LOAD_MANIFEST
- LOAD_COMPONENTS
- VALIDATE_RUNTIME
- ACTIVE
- INTAKE
- QUALIFICATION
- NEGOTIATION_LOGIC
- PRICE_LADDER
- OUTPUT_FORMAT
- COMPLETE
- DEGRADED
- HALT

## 2) Allowed Transitions (deterministic)

Startup / load-time:
- INIT → LOAD_MANIFEST
- LOAD_MANIFEST → LOAD_COMPONENTS
- LOAD_COMPONENTS → VALIDATE_RUNTIME
- VALIDATE_RUNTIME → ACTIVE
- VALIDATE_RUNTIME → HALT (if hard validation fails)

Execution-time:
- ACTIVE → INTAKE
- INTAKE → QUALIFICATION

Qualification gate:
- QUALIFICATION → OUTPUT_FORMAT (if QUALIFICATION_STATUS != READY_FOR_NEGOTIATION)
- QUALIFICATION → NEGOTIATION_LOGIC (if QUALIFICATION_STATUS == READY_FOR_NEGOTIATION)

Negotiation / pricing ladder:
- NEGOTIATION_LOGIC → PRICE_LADDER (if pricing response is required)
- NEGOTIATION_LOGIC → OUTPUT_FORMAT (if pricing response is not required)

Output / completion:
- PRICE_LADDER → OUTPUT_FORMAT
- OUTPUT_FORMAT → COMPLETE

Failure handling:
- Any state → HALT (hard stop conditions)
- ACTIVE → DEGRADED (only if explicitly allowed elsewhere)
- DEGRADED → HALT (if recovery not allowed)


## 8) Definition of Done
This file is correct when:
- It matches the manifest categories without duplicating inventory
- It defines one deterministic load order
- It defines one deterministic per-message execution chain
- It clearly states what happens when something is missing or fails

---
End.