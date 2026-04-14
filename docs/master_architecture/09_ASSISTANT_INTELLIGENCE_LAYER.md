# ASSISTANT INTELLIGENCE LAYER
Status: DRAFT
Scope: Assistant-facing intelligence and analysis layer. Non-customer-facing. No direct runtime control.

---

## 0. Purpose

This document defines the assistant-facing intelligence layer that operates alongside the runtime.

It provides:
- conversation understanding
- customer psychology analysis
- decision support for assistants
- structured internal summaries

This layer must never directly generate customer-facing messages.

---

## 1. Position in Architecture

This layer sits:

- ABOVE runtime (analysis only)
- PARALLEL to customer output (not inside it)
- FEEDS human assistants and future UI systems

It does NOT:
- modify runtime state directly
- override qualification logic
- inject phrases into customer output

---

## 2. Input Sources

- Pasted chats (full / partial / screenshots)
- Runtime state (phase, qualification status)
- Conversation history
- Detected signals (silence, repetition, objections)

---

## 3. Output Types (Internal Only)

### 3.1 Conversation Analysis
- current phase (0–5)
- stage (HOT / WARM / COLD / FOLLOWUP / LOST)
- closability (HIGH / MEDIUM / LOW)

### 3.2 Customer Psychology Signals
- intent level (high / medium / low)
- price sensitivity
- technical awareness
- trust level
- negotiation behavior

### 3.3 Risk & Loss Detection
- why customer dropped or went silent
- friction points
- confusion signals
- assistant mistakes (if any)

### 3.4 Suggested Actions (Assistant Support Only)
- safe response
- persuasive response (if allowed by phase)
- recovery response
- re-entry strategy

### 3.5 Reasoning Layer
- why this state is detected
- what triggered current behavior
- what should be avoided next

---

## 4. Internal Output Format (Reference)

When producing assistant-facing analysis:

1. TRANSLATION (if needed)
2. CONTEXT SNAPSHOT
3. STAGE TAG
4. CUSTOMER TYPE TAGS
5. CLOSABILITY SCORE
6. NEXT BEST ACTION
7. WARNINGS (if any)
8. SOURCE TRACE

---

## 5. Hard Separation Rule

This layer must never:
- appear in customer-facing output
- mix with bilingual response templates
- inject explanations into runtime messages

Customer output remains governed by:
- OUTPUT_RESPONSE_TEMPLATE.md
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md

---

## 6. Relationship to Phase Architecture

- Phase 0–2 → may trigger basic internal summaries
- Phase 3–5 → consumes signals for pricing / negotiation
- Phase 10 → integrates with assistant UI
- Phase 11 → evolves into conversation intelligence system

---

## 7. Future Integration

This layer will power:

- Assistant dashboard
- Conversation viewer
- CRM integration
- Analytics and reporting
- AI-assisted decision support

---

## 8. Governance Rules

- No duplicate logic with runtime files
- No independent decision authority
- No pricing or negotiation execution
- Analysis only, recommendation only

---

## 9. Validation Scope

Validation will be done via:
- manual assistant usage (UAT)
- conversation replay testing
- comparison against real chat outcomes

---

END OF FILE
