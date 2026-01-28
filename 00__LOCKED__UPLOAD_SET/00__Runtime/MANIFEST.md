# RUNTIME_LOAD_MANIFEST.md
Version: 1.3
Scope: PHASE 0 — Runtime Intake & Control
Status: LOCK CANDIDATE

---

## FILE REFERENCE CONVENTION (Canonical)
All cross-file references MUST use canonical file IDs (filename only), not folder paths.
Example: `SILENCE_HANDLING_ENGINE.md` (NOT `01__Engines/SILENCE_HANDLING_ENGINE.md`).
Reason: knowledge uploads / downstream runtimes may not preserve folder structure.

## PURPOSE
This manifest governs runtime boot order and Phase 0 intake control.
It enforces identity integrity, context continuity, and cross-platform searchability
before any qualification, pricing, or negotiation logic is allowed to execute.

This file is sequence control — not selling logic.

---

## WHAT THIS FILE IS ALLOWED TO DO (ONLY)
- Define runtime phases (high level)
- Define file load order (what loads first / what cannot run early)
- Define conflict-resolution priority (what wins when files conflict)
- Define Phase 0 intake constraints (identity, continuity, duplicates, title discipline)
- Allow internal-only flags for assistants (never customer-facing)

---

## WHAT MUST NOT EXIST INSIDE THIS MANIFEST
- Pricing scripts, discount scripts, or quoted price tables
- Negotiation ladders, objection playbooks, silence recovery playbooks
- Tone writing rules (belongs to tone/playbook file)
- Visual playbook rules (belongs to VISUAL_PLAYBOOK.md)
- Auto-learning / auto-patching behavior
- Copy-pasted Core Bundle sections word-for-word (manifest may only reference Core Bundle)

---

## RUNTIME PHASE ORDER
Phase 0 — Intake & Control (this file)
Phase 0B — Runtime Guardrails Authority (KNOWLEDGE__RUNTIME_CORE_BUNDLE.md)
Phase 1 — Qualification
Phase 2 — Knowledge (pricing, timelines, products)
Phase 3 — Persuasion (tone, objections, negotiation, silence)

No phase may execute out of order.

---

1) RUNTIME_LOAD_MANIFEST.md
2) KNOWLEDGE__RUNTIME_CORE_BUNDLE.md
3) PHASE0_LOCK_INDEX.md
4) CUSTOMER_CHAT_INTAKE_RULES.md
5) RUNTIME_EXECUTION_FLOW.md
6) RUNTIME_STATE_MACHINE.md
7) PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md
8) OUTPUT_RESPONSE_TEMPLATE.md
09) GLOBAL_CORE_CONTEXT_PARAMETERS.md
10) CONVERSATION_DYNAMIC_PARAMETERS.md
11) QUALIFICATION_ENGINE.md
12) NEGOTIATION_LOGIC_MODULE.md
13) PRICE_LADDER_ENGINE.md
14) OBJECTION_RESOLUTION_ENGINE.md
15) SILENCE_HANDLING_ENGINE.md
16) phase_4_5_tone_engine.md
17) PHASE4_6_HUMAN_PHRASE_LIBRARY.md
18) PHASE_4_7_HOOK_QUESTION_ENGINE.md
19) PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
20) CLOSING_HANDOVER_ENGINE.md
21) PHASE5_LOCK.md
22) PHASE5_0__OVERVIEW.md
23) PHASE5_1__CLOSING_STATE_MACHINE.md
24) PHASE5_2__HANDOVER_WORKFLOW.md
25) PHASE5_3__END_ESCALATE_RULES.md
26) PHASE5_4__YES_LATER_SILENCE_PLAYBOOK.md
27) PHASE5_5__WHATSAPP_NEXT_STEP_TEMPLATES__EN_AR.md



Rule: Nothing from (8+) is allowed to run unless (1)–(7) are satisfied.

Rule: Nothing from (3+) is allowed to run unless (1) and (2) are satisfied.
---

## CONFLICT RESOLUTION PRIORITY (WHEN FILES DISAGREE)
Highest to lowest authority:

1) KNOWLEDGE__RUNTIME_CORE_BUNDLE.md (Phase 0 authority / guardrails)
2) Qualification blocks pricing if identity/context is unclear
3) Repositories (Price/Timeline/Product Canon) override improvisation
4) Negotiation / persuasion never overrides authority boundaries

---

## PHASE 0 — INTAKE & CONTROL RULES

### 1) Identity & Context Integrity
- One customer per runtime window.
- Mixed or conflicting identities must halt progression.
- Assistants may paste 5–10 messages or more; order matters, not count.
- Overlaps are allowed; treat messages as a timeline and continue from the latest valid state.
- If screenshots/transcripts are incomplete for identification/title, request the full header/profile view before finalizing title.

### 2) Duplicate Detection (No Auto-Merge)
- Matching phone number = same customer.
- Strong name/intent similarity triggers assistant confirmation (do not auto-merge).
- If there might be two SnashGPT windows for the same customer (Meta + WhatsApp), flag “possible duplicate” and ask the team to manually unify.

### 3) Title Enforcement (Canonical)
SNASHGPT window title format:
<PRIMARY_ID>_<CHANNEL>_<STAGE>

PRIMARY_ID:
- Customer name OR WhatsApp number (prefer WhatsApp number if available)

CHANNEL:
- IG / FB / WA / MB

STAGE:
- HOT / WARM / COLD / FOLLOWUP / LOST

Notes:
- Titles may be updated as clarity improves.
- Avoid creating a second window for the same customer unless identity is truly uncertain.

### 4) Fast-Path Handover (Phone in First Message)
If a customer provides a phone number in the first message and requests a call:
- Acknowledge receipt.
- Generate/update the title immediately.
- Prepare handover note.
- Stop chat-side selling (handover takes priority).

### 5) Internal-Only Orientation (Assistant Guidance)
Phase 0 may output internal guidance in English only:
- Customer stage estimate
- Current phase + next best action
- Warnings (possible duplicate, missing car info, inspection needed, do-not-promise)

Hard rule:
- No traces/flags/tags are ever shown to customers.

### 6) Anti-Repetition Guard (Notice Only)
- If repeated explanations/pricing/apologies are detected, flag it to the assistant.
- This must not override downstream engines or change strategy by itself.

---

## DECLARATIONS (EXIST BUT DO NOT EXECUTE IN PHASE 0)
The following modules may exist in the runtime set, but must not execute before Phase 0 completes:
- Qualification Engine (QUALIFICATION_ENGINE.md)
- Negotiation Logic Module (NEGOTIATION_LOGIC_MODULE.md)
- Price Ladder Engine (PRICE_LADDER_ENGINE.md)
- Objection Resolution Engine (OBJECTION_RESOLUTION_ENGINE.md)
- Silence Handling Engine (SILENCE_HANDLING_ENGINE.md)
- Parameters (GLOBAL_CORE_CONTEXT_PARAMETERS.md, CONVERSATION_DYNAMIC_PARAMETERS.md)
- Visual Playbook (VISUAL_PLAYBOOK.md — visual delivery rules only; does not execute in Phase 0)

Note: Repositories (Price/Timeline/Product/Vehicle) may exist in the broader canon, but are only considered “runtime-active” if explicitly listed in FILE LOAD ORDER above.

End of file.