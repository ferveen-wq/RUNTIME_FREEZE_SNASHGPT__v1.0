Status: Locked
Version: v1.0.0
Last Updated: 2026-01-06
Lock Reason: Orchestration stage sealed (Qualification gate enforced; no bypass; no pricing logic)

# CUSTOMER_CHAT_INTAKE_RULES.md
Status: LOCKED (customer input authority)
Role: Defines how customer chats are received, interpreted, normalized, and prepared for execution.
Scope: Input handling only (no pricing, no logic decisions, no output formatting).

---

## 0) Purpose
This file defines:
- What counts as valid customer input
- How to handle Arabic, English, and mixed-language chats
- How screenshots, pasted chats, emojis, and short messages are treated
- What information must be extracted before qualification starts

This file does NOT:
- Decide pricing
- Decide final answers
- Format the customer reply
- Override qualification or runtime sequencing

## OUTPUT SIGNALS (EMITTED TAGS ONLY)

This file MUST emit the following internal signals for downstream engines.
These are tags, not customer-facing text.

### Emitted Signals

- objection_signal: ENUM
  - Meaning: classification label for the objection detected in the customer message (or silence state).
  - Note: the Objection Resolution Engine consumes this and does not parse raw text.

- objection_repeat_count: INTEGER
  - Meaning: count of repeats of the SAME objection signal within the session after pricing exposure.
  - Range: 0, 1, 2+
  - Note: used by repeat guardrails to prevent loops.

- customer_response_latency: ENUM
  - Meaning: how quickly the customer responded after price exposure.
  - Values: IMMEDIATE | DELAYED | SILENT

### Emission Rules (High-Level)

- If the customer message contains an objection pattern after pricing exposure:
  - set objection_signal accordingly
  - increment objection_repeat_count when the same objection_signal repeats

- If there is no customer response after pricing exposure:
  - customer_response_latency = SILENT
  - objection_signal = SILENCE_AFTER_PRICE
  - objection_repeat_count increments if silence repeats

- Otherwise:
  - customer_response_latency = IMMEDIATE or DELAYED (based on your runtime timer)
  - objection_signal = UNKNOWN_OR_AMBIGUOUS (only if you cannot classify)

---

## 1) Accepted Input Types
The system may receive customer input as:
1) Plain text chat (Arabic / English / mixed)
2) Screenshot of chat conversation
3) Pasted chat history (partial or full)
4) Short messages (e.g. “hi”, “price?”, “ppf?”)
5) Emojis combined with text

Voice notes, images of cars, or videos:
- Are acknowledged
- But must be converted into text intent before processing

---

## 2) Language Handling Rules
### 2.1 Language Detection
For every input:
- Detect primary language:
  - Arabic
  - English
  - Mixed (Arabic + English)

### 2.2 Working Language
- Internal processing language: English
- Customer-facing language: Match the customer’s language preference

If mixed:
- Prefer Arabic for customer reply unless English dominance is clear

---

## 3) Screenshot & Pasted Chat Handling
When input is a screenshot or pasted conversation:
1) Read only the customer messages
2) Ignore system / agent replies unless context is required
3) Preserve original wording (do not correct yet)
4) Extract:
   - Customer intent
   - Car details (if any)
   - Service requested
   - Questions asked
   - Emotional tone (normal / confused / upset)

If critical context is missing:
- Mark it as “missing”
- Do NOT assume

---

## 4) Emoji & Short Message Rules
### 4.1 Emojis
- Emojis do NOT change intent
- Emojis may indicate tone only (friendly / frustrated)

### 4.2 Very Short Messages
Examples:
- “hi”
- “price?”
- “ppf”
- “السلام عليكم”

Handling:
- Treat as valid input
- Respond with welcome + 1–2 clarifying questions max

---

## 5) Required Information Extraction


### 5.1 Numeric-only model token guard (HARD — global)
If the customer provides a brand + a token that is digits-only (e.g., "Jetour 52", "Jetour 90"):
- Do NOT treat the digits-only token as vehicle_model.
- Mark vehicle_model as missing (do NOT guess).
- Downstream must treat this as clarification-required (one question only).

Digits-only definition:
- A token containing only digits (e.g., "52", "90", "300") with no letters.

Notes:
- This does not block SAFE aliases that include digits but are not digits-only (e.g., "lc300", "f150", "t2").

### 5.2 Ambiguous alias guard (HARD — global)
If the customer provides an alias that is listed as AMBIGUOUS in GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md (Section 4.2) (e.g., "x90", "s90", "cx", "lc", "v6", "gt", "rs", "amg", "bmw x", "toyota suv", "nissan suv"):
- Do NOT auto-normalize to any brand/model.
- Mark vehicle_model as missing (do NOT guess).
- Downstream must ask exactly ONE clarification question to confirm the exact brand/model before mapping.
From every customer input, try to extract:
- Car brand
- Car model
- Year
- Service requested (PPF, ceramic, polishing, etc.)
- Scope (full body / partial / unknown)
- Urgency (if mentioned)
- Location (if relevant)

If something is not present:
- Mark as missing
- Do NOT guess

---

## 6) Intent Classification (input-side only)
Classify intent into one primary category:
- Price inquiry
- Service explanation
- Comparison
- Booking / availability
- Complaint / issue
- Greeting / conversation start

Only ONE primary intent per message.

---

## 7) Ambiguity Rules
If input is ambiguous:
- Do not interpret aggressively
- Ask clarification questions in output stage
- Limit to 1–2 questions max

Never stack multiple assumptions in intake.

---

## 8) Emotional Tone Detection
Detect tone as:
- Neutral
- Curious
- Confused
- Frustrated / upset

Tone affects response tone later but does NOT change facts or rules.

---

## 9) Intake → Handoff Rule
Once intake is complete:
- Pass normalized intent + extracted info to the Qualification Stage (engine defined by the Runtime Manifest)
- Do NOT modify customer meaning
- Do NOT inject suggestions
---

## 10) Definition of Done
This file is correct when:
- All input types are covered
- Language handling is unambiguous
- No assumptions are allowed
- Intake stops exactly where qualification begins

---
End.