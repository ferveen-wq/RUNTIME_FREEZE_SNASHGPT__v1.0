# CONVERSATION_DYNAMIC_PARAMETERS.md
Version: v1.0
Status: LOCKED (v1.0)

## LOCK NOTE
- This file defines **dynamic, conversation-time parameters** (signals).
- Values must be **UPPERCASE_SNAKE_CASE** (no symbols).
- Engines may **read** these parameters but must NOT invent new values.
- Any change requires a version bump (v1.1, v1.2...) and review.
- This file contains **NO pricing**, **NO phrasing**, **NO negotiation scripts**.

---

## PURPOSE
This file standardizes conversation-time signals so the system can:
- prevent silence drop-offs
- avoid over-explaining
- manage price pressure safely
- pre-empt objections without annoying the customer
- decide when to escalate / handoff

These parameters are **dynamic** (can change turn-to-turn).
Core customer + vehicle context lives in:
- GLOBAL_CORE_CONTEXT_PARAMETERS.md

---

## GLOBAL RULES
- Parameter names: UPPERCASE_SNAKE_CASE
- Parameter values: UPPERCASE_SNAKE_CASE only
- Always support UNKNOWN when unclear
- Detection does NOT force action (signals tune posture; engines decide next step)

---

# CATEGORY 5 — COMPETITOR & MARKET INFLUENCE SIGNALS

### PARAMETER: COMPETITOR_INFLUENCE_LEVEL
Description: General level of competitor/social-media influence shaping the customer’s thinking.
Allowed Values:
- NONE
- LOW
- HIGH
- UNKNOWN

Used By:
- Pricing Ladder Engine (timing control)
- Tone / Phrase Engine (education depth)
- Negotiation Logic

---

### PARAMETER: MARKET_TERM_INFLUENCE
Description: Presence of market-driven terms (signals confusion/comparison risk).
Allowed Values:
- NONE
- PRESENT
- HEAVY
- UNKNOWN

Notes:
- Includes terms like: FULL_PPF, FRONT_PPF, HALF_PPF, TPU, THICKNESS, MICRONS, SELF_HEALING, WARRANTY_YEARS, MANUAL_VS_PRECUT.
- Detection does NOT require education; it only adjusts posture/timing.

Used By:
- Pricing Ladder Engine
- Tone / Phrase Engine
- Negotiation Logic

---

### PARAMETER: COMPETITOR_QUOTE_STATUS
Description: Whether the customer has external pricing in mind.
Allowed Values:
- NONE
- MENTIONED
- HAS_QUOTE_DETAILS
- UNKNOWN

Notes:
- If HAS_QUOTE_DETAILS, avoid long education; keep it tight and move to controlled anchoring or handoff.

Used By:
- Negotiation Logic
- Pricing Ladder Engine
- Handoff Strategy

---

# CATEGORY 6 — BUDGET & PRICE SENSITIVITY

### PARAMETER: BUDGET_SIGNAL
Description: Customer’s sensitivity to cost (coarse).
Allowed Values:
- LOW_SENSITIVITY
- UNCLEAR
- HIGH_SENSITIVITY
- UNKNOWN

Notes:
- Sensitivity ≠ affordability. Do not judge.

Used By:
- Pricing Ladder Engine
- Negotiation Logic
- Tone / Phrase Engine (softness)

---

### PARAMETER: PRICE_PRESSURE_LEVEL
Description: How aggressively the customer is pushing for numbers right now.
Allowed Values:
- LOW
- MEDIUM
- HIGH
- UNKNOWN

Notes:
- HIGH often shows as repeated “how much?” or ignoring answers and re-asking.
- Used to decide whether to anchor range vs escalate to quote/human.

Used By:
- Pricing Ladder Engine
- Negotiation Logic
- Handoff Strategy

---

### PARAMETER: DISCOUNT_EXPECTATION_RISK
Description: Likelihood customer expects discounting immediately.
Allowed Values:
- LOW
- MEDIUM
- HIGH
- UNKNOWN

Notes:
- Prevents proactive discounting.
- Routes to boundary / quote stage if persistent.

Used By:
- Negotiation Logic
- Pricing Ladder Engine

---

# CATEGORY 7 — CONVERSATION DYNAMICS & SILENCE STATES

### PARAMETER: CUSTOMER_SILENCE_STATE

### PARAMETER: SILENCE_S1_HOURS
Description: Hours since LAST_COUNTED_OUTBOUND_TIMESTAMP to enter Early Silence.
Default: 6

### PARAMETER: SILENCE_S2_HOURS
Description: Hours since LAST_COUNTED_OUTBOUND_TIMESTAMP to enter Extended Silence.
Default: 24

### PARAMETER: SILENCE_S3_HOURS
Description: Hours since LAST_COUNTED_OUTBOUND_TIMESTAMP to enter Terminal Silence (stop).
Default: 72

### PARAMETER: SILENCE_MAX_FOLLOWUPS
Description: Maximum number of silence-permitted follow-up actions that may be SENT per silence cycle.
Default: 2

### PARAMETER: CUSTOMER_SILENCE_STATE

Description: Customer response latency AFTER assistant message.
Allowed Values:
- ACTIVE
- S1
- S2
- S3
- UNKNOWN

Notes:
- Silence ≠ rejection.

Used By:
Silence Handling Engine
Runtime Orchestration controls
(Future) Tone / Phrase layer (if added later)

---

### PARAMETER: ASSISTANT_RESPONSE_LATENCY_STATE
Description: Assistant response timing BEFORE replying to customer.
Allowed Values:
- IMMEDIATE
- DELAYED
- EXTENDED_DELAY
- UNKNOWN

Notes:
- Long assistant delays require softer re-entry and optional acknowledgement.
- Must not be misread as customer disinterest.

Used By:
- Tone / Phrase Engine
- Orchestration controls

---

### PARAMETER: MOMENTUM_STATE
Description: Overall rhythm/flow quality.
Allowed Values:
- STRONG
- NORMAL
- WEAK
- STALLED
- UNKNOWN

Used By:
- Orchestration controls
- Tone / Phrase Engine
- Silence Recovery Engine

---

### PARAMETER: FRICTION_LEVEL
Description: Coarse indicator of irritation/resistance (non-psychological).
Allowed Values:
- LOW
- MEDIUM
- HIGH
- UNKNOWN

Notes:
- High friction: repeated objections, short replies, impatience, “just price”, “why expensive”.
- When HIGH, reduce education depth and move toward clear next action/handoff.

Used By:
- Tone / Phrase Engine
- Negotiation Logic
- Handoff Strategy

---

### PARAMETER: OBJECTION_DENSITY
Description: Frequency of objections in recent turns.
Allowed Values:
- LOW
- MEDIUM
- HIGH
- UNKNOWN

Used By:
- Pricing Ladder Engine (ladder down / simplify)
- Negotiation Logic
- Tone / Phrase Engine

---

### PARAMETER: QUESTION_LOAD_STATE
Description: How “question-heavy” the assistant has been recently.
Allowed Values:
- LOW
- MEDIUM
- HIGH
- UNKNOWN

Notes:
- Protects against interrogation feel.
- When HIGH, prefer summarizing and offering options.

Used By:
- Orchestration controls
- Tone / Phrase Engine

---

### PARAMETER: INFO_COMPLETENESS
Description: Whether enough info exists to give a useful range/next step without more probing.
Allowed Values:
- LOW
- MEDIUM
- HIGH
- UNKNOWN

Notes:
- When LOW: max 1–2 clarifying questions (not more).
- When MEDIUM/HIGH: summarize + offer range or move to quote.

Used By:
- Pricing Ladder Engine
- Orchestration controls

---

### PARAMETER: BOOKING_READINESS
Description: Observed readiness to take next step (visit/booking/quote).
Allowed Values:
- NOT_READY
- MAYBE
- READY
- UNKNOWN

Used By:
- Closing/Handoff Strategy
- Tone / Phrase Engine (call-to-action strength)

---

### PARAMETER: FOLLOWUP_OK
Description: Whether follow-up is welcome (prevents annoyance in GCC/Bahrain contexts).
Allowed Values:
- YES
- NO
- UNKNOWN

Used By:
- Follow-up strategy
- Handoff strategy

---

## CATEGORY 8 — SYSTEM INTENT & CONTROL (REFERENCE ONLY)
System intent (modes, ladder stage, question budget, escalation eligibility) is controlled in:
- RUNTIME_EXECUTION_FLOW.md
- RUNTIME_STATE_MACHINE.md
- Negotiation / Qualification engines

This file does NOT duplicate system-control fields to avoid drift.

---

## END OF FILE