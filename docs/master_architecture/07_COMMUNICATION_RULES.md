# COMMUNICATION RULES
Status: DRAFT
Source Policy: Active runtime files win over legacy, tests, drafts, and archive notes.
Scope: Customer-facing communication constraints only. No engine routing logic. No pricing invention. No state ownership.

## 0. Purpose

This document records the customer-facing communication rules enforced by runtime-controlled output layers.

Primary authority sources:
- `OUTPUT_RESPONSE_TEMPLATE.md`
- `phase_4_5_tone_engine.md`
- `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
- `PHASE_4_7_HOOK_QUESTION_ENGINE.md`
- `KNOWLEDGE__RUNTIME_CORE_BUNDLE.md`

---

## 1. Core Customer-Facing Output Rules

[FROM: OUTPUT_RESPONSE_TEMPLATE.md]

Core rules:
- simple human language
- English then Arabic must be easy to copy on mobile
- keep it short and actionable
- if info is missing, ask only 1 question max
- never mention internal file names, engines, or architecture in customer-facing text
- always include timestamp at end

Output hygiene:
- no emojis
- no icons
- no decorative symbols
- no reaction marks
- no bullet lists in customer-facing output
- use short sentences
- plain-text WhatsApp style

---

## 2. Bilingual Rule

[FROM: OUTPUT_RESPONSE_TEMPLATE.md]
[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]

Bilingual order:
- English full message first
- Arabic full message second

Rules:
- do not interleave languages
- separate language sections cleanly
- timestamp must be final line

---

## 3. Question Limit Rule

[FROM: OUTPUT_RESPONSE_TEMPLATE.md]
[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]
[FROM: PHASE_4_7_HOOK_QUESTION_ENGINE.md]

Rules:
- max 1 question total in the whole message
- if hook is a question, the rest of the message must contain 0 questions
- Phase 3A also follows one-question maximum

---

## 4. Tone Rules

[FROM: phase_4_5_tone_engine.md]

Tone must:
- feel human
- feel calm
- feel adaptive
- never feel scripted

Core principles:
- tone influences selection, not wording
- tone must never override phrase library constraints
- tone cannot introduce urgency unless explicitly allowed
- tone selection must be reversible until closing lock

Hard safety rules:
- tone may never combine urgency and persuasion
- tone may never escalate after resistance
- tone may never contradict phrase intent
- tone may never bypass assembly constraints

---

## 5. Hook Rules

[FROM: PHASE_4_7_HOOK_QUESTION_ENGINE.md]

Hooks:
- are optional
- are suppressible
- must never be mandatory
- must never escalate after resistance or silence
- must respect tone permissions
- must respect output caps
- must never interrupt explanations, value delivery, or confirmations

---

## 6. No-Invention Rule

[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]
[FROM: OUTPUT_RESPONSE_TEMPLATE.md]
[FROM: KNOWLEDGE__RUNTIME_CORE_BUNDLE.md]

Customer-facing text must not:
- invent phrases outside phrase library
- invent routing logic inside message text
- invent pricing logic
- invent unsupported signals
- violate output hygiene constraints

If routed signal has no supported phrase coverage:
- test mode may suppress response
- production mode must use fallback routing

---

## 7. Special Customer-Facing Cases

[FROM: OUTPUT_RESPONSE_TEMPLATE.md]

Angry / complaining:
- start with empathy
- confirm issue
- offer next step
- ask 1 question max if needed

Price ask with missing details:
- do not guess final price
- ask required details
- do not present ranges from template layer

Greeting only:
- welcome
- ask required first detail according to routed path

---

## 8. Timestamp Rule

[FROM: OUTPUT_RESPONSE_TEMPLATE.md]
[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]

Timestamp:
- always last line
- always after both language sections
- included in final formatted output

