# MESSAGE CONSTRUCTION MODEL
Status: DRAFT
Source Policy: Active runtime files win over legacy, tests, drafts, and archive notes.
Scope: Message selection, phrase writing, hook/tone constraints, assembly, and output formatting only. No pricing invention. No intake or state ownership.

## 0. Purpose

This document records how a customer-facing message is constructed from runtime decisions, phrase blocks, tone constraints, hook permissions, assembly rules, and final output formatting.

Primary authority sources:
- `AUTHORITY_INDEX.md`
- `PHASE4_6_HUMAN_PHRASE_LIBRARY.md`
- `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
- `phase_4_5_tone_engine.md`
- `PHASE_4_7_HOOK_QUESTION_ENGINE.md`
- `OUTPUT_RESPONSE_TEMPLATE.md`
- `PHRASE_GOVERNANCE_STANDARD.md`
- `PHRASE_INDEX.md`

---

## 1. Three-Layer Customer-Facing Construction Rule

[FROM: AUTHORITY_INDEX.md]

Customer-facing message content:
- WRITER: `PHASE4_6_HUMAN_PHRASE_LIBRARY.md`
- SELECTOR: `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
- FORMATTER: `OUTPUT_RESPONSE_TEMPLATE.md`

Rule:
- phrase library writes text only
- assembly selects only
- output template formats only

Construction boundary:
- phrase library does not encode routing logic
- assembly does not rewrite classification or routing ownership
- output template does not decide what to ask

---

## 2. Human Phrase Library

[FROM: PHASE4_6_HUMAN_PHRASE_LIBRARY.md]
[FROM: AUTHORITY_INDEX.md]

Owns:
- customer-facing EN/AR phrase content

Rules:
- every phrase block must include EN and AR
- phrase blocks are selected by phrase ID
- phrase library must not encode routing logic

Governance:
- bilingual integrity must pass lint
- placeholder parity between EN and AR must match

---

## 3. Tone Engine

[FROM: phase_4_5_tone_engine.md]

Purpose:
- define how messages should feel
- not what they say

Tone engine:
- selects conversational tone
- enforces emotional and behavioral boundaries
- governs urgency, softness, neutrality, and restraint

Does not:
- generate phrases or sentences
- change phrase wording
- reorder message structure
- override safety rules

Interaction with assembly:
- may allow or suppress hooks
- may limit block types selectable in Phase 4.8
- may enforce softness or neutrality

---

## 4. Hook Question Engine

[FROM: PHASE_4_7_HOOK_QUESTION_ENGINE.md]

Purpose:
- govern whether an optional engagement question may appear

Rules:
- hooks are always optional
- hooks are fully suppressible
- no new customer-facing language may be authored here
- all hook phrasing must originate from Phase 4.6
- hooks must respect tone permissions
- hooks must respect output limits and ordering from Phase 4.8
- hooks must never escalate after resistance or silence
- maximum question count must never exceed architecture-defined limits

If suppressed:
- no question is generated
- message proceeds without acknowledgment

---

## 5. Message Assembly

[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]
[FROM: AUTHORITY_INDEX.md]

Purpose:
- define how a single customer-facing message is assembled from internal blocks

Controls:
- block selection
- ordering
- caps
- hook slot wiring
- suppression precedence

Writes:
- `selected_phrase_id`

Does not:
- create or rewrite customer-facing phrases
- introduce new tone logic
- modify phrase wording intent
- modify hook logic

Assembly output contract:
- customer sees one coherent message only

---

## 6. Assembly Inputs

[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]

Assembly reads:
1. phrase blocks
2. tone constraints
3. hook output
4. suppression signals
5. service context signals

Assembly evaluates:
- `active_service_context`
- `detected_service_intent_in_message`
- silence state
- objection state
- price tension
- closing lock
- repetition risk

Phase 0–2 assembly note:
- early-phase message construction must stay within locked Phase 0–2 response surfaces
- qualification-not-ready behavior must suppress hooks, extras, and non-minimum additions
- assembly may read runtime signals, but must not mutate classification ownership

---

## 7. Assembly Block Model

[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]

Block types:
- B0: Presence / Opening
- B1: Context Acknowledgement
- B2: Core Value / Explanation
- B3: Neutral Transition / Soft Next Step
- H1: Hook Slot

Rules:
- blocks are optional unless required for clarity
- hooks are never required

Ordering:
1. B0
2. B1
3. B2
4. B3
5. H1

Hard rules:
- hooks may only appear after core content
- hooks may never replace core content

Caps:
- max blocks per response: 3
- max questions per response: 1

Phase 0–2 locked minimal surfaces:
- L0 browsing-safe surface for browsing/generic discovery
- L1 qualification clarifiers for vehicle details
- model-only / year-only variants when missing fields narrow
- greeting/service-list fixed surfaces where runtime explicitly routes them

---

## 8. Bilingual Rendering Rule

[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]
[FROM: OUTPUT_RESPONSE_TEMPLATE.md]

Display format:
1. render full customer message in ENGLISH first
2. then render full customer message in ARABIC
3. do not alternate languages per block
4. separate the two language sections with exactly one blank line
5. timestamp is always the final line

---

## 9. Output Response Template

[FROM: OUTPUT_RESPONSE_TEMPLATE.md]

Role:
- defines the only allowed customer-facing response structure and formatting

May:
- format answers produced by earlier stages
- adjust tone simplicity and copy-paste friendliness
- apply timestamp and layout rules

Must never:
- make decisions
- reopen qualification logic
- introduce pricing logic
- override decision matrix, execution flow, or runtime state machine

Output hygiene:
- no emojis
- no decorative symbols
- no bullet lists
- short sentences
- plain-text WhatsApp style
- max 1 question total in whole message

Documentation caution:
- live runtime output authority is real, but active runtime files also show mixed output-shape expectations
- this document should preserve the authority boundary without pretending the live output layer is fully reconciled

---

## 10. Special Construction Rules

[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]
[FROM: OUTPUT_RESPONSE_TEMPLATE.md]

Rules include:
- silence response may become the full message when silence is active
- greeting-only routes may force one fixed phrase path
- re-entered continue routes may force one fixed phrase path
- direct price request handling must respect read-only gate logic
- qualification-not-ready states must not add decorative acknowledgments before the question

---

## 11. Phrase Governance

[FROM: PHRASE_GOVERNANCE_STANDARD.md]
[FROM: PHRASE_INDEX.md]

Phrase governance role:
- maintain phrase discipline
- track available phrase IDs
- support phrase integrity and selection safety

This layer is governance support for:
- phrase consistency
- phrase lookup
- phrase maintenance discipline

