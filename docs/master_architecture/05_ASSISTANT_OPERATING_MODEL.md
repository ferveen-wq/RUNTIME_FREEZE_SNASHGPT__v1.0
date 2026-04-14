# ASSISTANT OPERATING MODEL
Status: DRAFT
Source Policy: Active runtime files win over legacy, tests, drafts, and archive notes.
Scope: Assistant-side operating discipline only. No customer-facing phrase invention. No engine logic reassignment. No pricing invention.

## 0. Purpose

This document records how assistants should operate around the runtime when handling customer conversations, titles, pasted context, duplicate detection, and handover boundaries.

Primary authority sources:
- `RUNTIME_LOAD_MANIFEST.md`
- `KNOWLEDGE__RUNTIME_CORE_BUNDLE.md`
- `CUSTOMER_CHAT_INTAKE_RULES.md`
- `GLOBAL_RUNTIME_FLOW_MAP.md`
- `RUNTIME_STATE_MACHINE.md`
- `09_ASSISTANT_INTELLIGENCE_LAYER.md`

Positioning note:
- this file governs assistant operating discipline around the runtime
- `09_ASSISTANT_INTELLIGENCE_LAYER.md` governs assistant-facing analytical outputs
- neither file may take customer-facing routing authority away from runtime files

---

## 1. One Customer Per Runtime Window

[FROM: RUNTIME_LOAD_MANIFEST.md]
[FROM: KNOWLEDGE__RUNTIME_CORE_BUNDLE.md]

Rule:
- one customer per runtime window

Meaning:
- mixed or conflicting identities must halt progression
- no automatic merge of different customer identities
- runtime window must represent one customer only

---

## 2. Identity and Context Integrity

[FROM: RUNTIME_LOAD_MANIFEST.md]
[FROM: KNOWLEDGE__RUNTIME_CORE_BUNDLE.md]

Rules:
- mixed, conflicting, or ambiguous identities halt progression
- sequence matters more than message count
- latest valid message defines active state unless explicitly overridden
- assistants may paste multiple messages; order matters

If screenshots/transcripts are incomplete for identification/title:
- request the full header/profile view before finalizing title

---

## 3. Duplicate Handling

[FROM: RUNTIME_LOAD_MANIFEST.md]
[FROM: KNOWLEDGE__RUNTIME_CORE_BUNDLE.md]

Rules:
- matching phone number = same customer
- strong name/intent similarity requires assistant confirmation
- no automatic merge is permitted at runtime

If there may be two windows for the same customer:
- flag possible duplicate
- team must manually unify

---

## 4. Title Discipline

[FROM: RUNTIME_LOAD_MANIFEST.md]

Canonical title format:
- `<PRIMARY_ID>_<CHANNEL>_<STAGE>`

PRIMARY_ID:
- customer name
or
- WhatsApp number
- prefer WhatsApp number if available

CHANNEL:
- IG
- FB
- WA
- MB

STAGE:
- HOT
- WARM
- COLD
- FOLLOWUP
- LOST

Rules:
- titles may be updated as clarity improves
- avoid creating a second window for the same customer unless identity is truly uncertain

---

## 5. Accepted Assistant Input Handling

[FROM: CUSTOMER_CHAT_INTAKE_RULES.md]

The system may receive customer input as:
- plain text chat
- screenshot of chat conversation
- pasted chat history
- short messages
- emojis combined with text

Voice notes, images of cars, or videos:
- are acknowledged
- but must be converted into text intent before processing

Assistant operating implication:
- assistants must convert non-text material into usable text context before runtime processing

- assistants must not treat raw non-text material as already-qualified runtime input

---

## 6. Screenshot and Pasted Chat Discipline

[FROM: CUSTOMER_CHAT_INTAKE_RULES.md]

When input is screenshot or pasted conversation:
- read only customer messages
- ignore system / agent replies unless context is required
- preserve original wording
- extract:
  - customer intent
  - car details
  - service requested
  - questions asked
  - emotional tone

If critical context is missing:
- mark as missing
- do not assume

Assistant operating implication:
- assistants must not fill gaps by guessing

Context integrity rule:
- Assistants must rely only on explicitly available context.
- Valid context sources are:
  - pasted chat history
  - screenshots converted to text
  - structured runtime outputs
  - clearly provided user input

Constraints:
- Hidden memory, reconstructed assumptions, or prior chat recall must not be treated as runtime-valid context.
- If required context is missing, it must be marked as missing and handled via clarification — not inference.

Implication:
- assistant must not “fill gaps” using memory or assumptions
- all continuity must be traceable to explicit input or runtime-carried context

---

## 7. Internal-Only Guidance Boundary

[FROM: RUNTIME_LOAD_MANIFEST.md]

Phase 0 may output internal guidance in English only:
- customer stage estimate
- current phase
- next best action
- warnings

Hard rule:
- no traces, flags, or tags are ever shown to customers

---

## 8. Source Trace Discipline

[FROM: KNOWLEDGE__RUNTIME_CORE_BUNDLE.md]

All internal guidance, analysis, or admin-facing responses must include:
- `SOURCE TRACE`

Format:
- `SOURCE TRACE: <FILE_A> > <FILE_B> > <FILE_C>`

Trace visibility:
- internal-only
- must never be shown to customers

Assistant operating implication:
- internal reasoning support should remain traceable to runtime files

---

## 9. Fast-Path Handover Rule

[FROM: RUNTIME_LOAD_MANIFEST.md]

If customer provides a phone number in the first message and requests a call:
- acknowledge receipt
- generate or update title immediately
- prepare handover note
- stop chat-side selling

---

## 10. Session Rule After Termination

[FROM: RUNTIME_STATE_MACHINE.md]

If customer sends a new message after:
- `AUTOMATION_TERMINATED_FLAG == TRUE`
or
- `CONVERSATION_STATUS != OPEN`

Then:
- prior session remains terminal and immutable
- orchestration must open a new session context
- new session may import continuity snapshot
- prior outcomes must not be reversed

Assistant operating implication:
- do not continue a terminal session as if it were still open
- use a new session context for resumed contact

---

## 11. Handover Boundary

[FROM: RUNTIME_STATE_MACHINE.md]
[FROM: CLOSING_HANDOVER_ENGINE.md]

If `HANDOVER_REQUIRED_FLAG == TRUE`:
- human takeover is required
- automation must stop
- no further system actions should continue under normal automated flow

Assistant operating implication:
- assistant should treat the conversation as human-owned at that point
- do not continue automated phase progression

---

## 12. Anti-Repetition Boundary

[FROM: RUNTIME_LOAD_MANIFEST.md]
[FROM: KNOWLEDGE__RUNTIME_CORE_BUNDLE.md]

Rules:
- repeated explanations/pricing/apologies may be flagged
- flagging must not by itself override downstream strategy
- runtime behavior must never change from a single incident
- one-off events are not learnings

Assistant operating implication:
- do not turn a single conversation issue into a new rule without broader review

---

## 13. Assistant Operating Rules

Derived from runtime authority:
- do not guess missing facts
- do not merge customers automatically
- do not expose internal tags to customers
- do not bypass phase order
- do not continue terminal sessions as open
- do not substitute manual opinion for locked runtime authority
- do not create new customer-facing logic outside approved runtime layers
- do not treat assistant-facing analysis as customer-facing runtime output

---

## 14. Assistant Intelligence Boundary

[FROM: 09_ASSISTANT_INTELLIGENCE_LAYER.md]

Assistant-facing analysis may include:
- transcript summary
- translation for assistant understanding
- context snapshot
- stage / risk / customer-type tags
- next-step guidance
- warning flags
- source trace

Hard boundary:
- assistant-facing analysis is internal-only
- it must never be mixed into customer-facing replies
- it must not overwrite runtime-owned routing or state signals
- it may support later UI, database, and analytics layers without becoming runtime routing authority

