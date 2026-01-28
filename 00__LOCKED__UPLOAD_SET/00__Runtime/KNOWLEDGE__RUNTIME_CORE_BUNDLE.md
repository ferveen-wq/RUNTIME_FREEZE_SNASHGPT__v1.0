# KNOWLEDGE__RUNTIME_CORE_BUNDLE.md

Version: 1.0  
Scope: Runtime Knowledge Guardrails (Pre-Execution)  
Phase: 0 – Intake & Control  
Status: LOCK CANDIDATE  

---

## PURPOSE

This document defines the **non-negotiable runtime guardrails** that govern
how knowledge, context, pricing references, and behavioral signals are handled
before any execution engine is allowed to run.

This file does **not** execute logic.  
It **gates**, **classifies**, and **protects** runtime flow integrity.

---

## POSITION IN ARCHITECTURE

Execution Order:

1. RUNTIME_LOAD_MANIFEST.md  
2. KNOWLEDGE__RUNTIME_CORE_BUNDLE.md  ← (this file)
3. Qualification Engine  
4. Knowledge / Pricing / Timeline Repositories  
5. Persuasion & Negotiation Engines  

No engine may bypass Phase 0.

---

## CORE PRINCIPLES

### 1. Phase Authority
- Phase 0 has absolute authority to **halt**, **gate**, or **delay** execution.
- No downstream engine may override Phase 0 decisions.

### 1.5. Output Hygiene Constraint

- Emoji usage is forbidden across all phases and engines.
- Output formatting rules defined in OUTPUT_RESPONSE_TEMPLATE.md are authoritative.
- No engine may override output hygiene constraints.

---

### 2. Identity & Context Integrity

- One customer per runtime window.
- Mixed, conflicting, or ambiguous identities halt progression.
- Assistants may paste any number of messages; **sequence matters, not volume**.
- The **latest valid message defines active state** unless explicitly overridden.

---

### 3. Duplicate & Continuity Handling

- Matching phone number = same customer.
- Strong name / intent similarity triggers **assistant confirmation**, not auto-merge.
- No automatic customer merging is permitted at runtime.

---

### 4. Anti-Repetition & Learning Protection

- Runtime behavior **must never change based on a single incident**.
- Corrections, one-off clarifications, or isolated objections are **not learnings**.
- Learning eligibility requires **repeated patterns across multiple customers**.
- Pattern recognition is observational, not automatic.

---

### 5. Safety Dominance (Non-Engine)

Safety is enforced as a **Phase 0 authority**, not as a runtime engine.

- Unknown, unsafe, or contradictory inputs halt execution.
- Safety overrides all engines, prices, and persuasion logic.
- Safety logic is referenced, not duplicated, in downstream systems.

---

### 6. Pricing Guardrails (Pre-Execution)

- Pricing output must **never open** with:
  “Original price is X, discounted price is Y.”
- Discount framing is prohibited at initial pricing disclosure.
- Discounts may only be surfaced **after pricing pressure is classified**.
- Discount logic is controlled by downstream pricing systems, not Phase 0.

---

### 7. Discount Control Boundary

- Phase 0 may **classify pricing pressure signals**.
- Phase 0 does **not** authorize, compute, or suggest discounts.
- All discount execution remains outside this bundle.

---

### 8. Silence & Negotiation Signals (Classification Only)

- Silence risk may be **flagged**, never resolved, in Phase 0.
- No silence recovery, persuasion, or follow-up logic executes here.
- Negotiation pressure is observed via:
  - Repeated price probing
  - Hesitation loops
  - Clarification cycling

---

### 9. Visual Usage Safety (High-Level)

- Visual assets may be used at **any phase**, subject to safety and clarity checks.
- Visuals are a **delivery format**, not a persuasion trigger by default.
- Visual strategy and sequencing are handled downstream.

---

### 10. Shadow Learning Boundary

- Shadow observations may be logged externally.
- Phase 0 does **not** adapt behavior based on shadow outcomes.
- Human review is required before doctrine updates.

---

## NON-GOALS (Explicit)

This file does NOT:
- Execute qualification logic
- Perform pricing calculations
- Apply discounts
- Recover silence
- Negotiate objections
- Learn or mutate behavior automatically

---

## LOCK RULE

Once locked:
- Any change requires:
  - Architecture review
  - Manifest compatibility check
  - Version increment

---

## 11. Internal Traceability & Source Attribution (Mandatory)

All **internal guidance**, analysis, or admin-facing responses must include a  
**SOURCE TRACE** indicating which files influenced the output.

Format:
SOURCE TRACE: <FILE_A> > <FILE_B> > <FILE_C>

Allowed files include (non-exhaustive):
- RUNTIME_LOAD_MANIFEST.md
- KNOWLEDGE__RUNTIME_CORE_BUNDLE.md
- PHASE0_LOCK_INDEX.md
- CUSTOMER_CHAT_INTAKE_RULES.md
- RUNTIME_EXECUTION_FLOW.md
- RUNTIME_STATE_MACHINE.md
- PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md
- OUTPUT_RESPONSE_TEMPLATE.md
- GLOBAL_CORE_CONTEXT_PARAMETERS.md
- CONVERSATION_DYNAMIC_PARAMETERS.md
- QUALIFICATION_ENGINE.md
- NEGOTIATION_LOGIC_MODULE.md
- PRICE_LADDER_ENGINE.md
- OBJECTION_RESOLUTION_ENGINE.md
- SILENCE_HANDLING_ENGINE.md
- phase_4_5_tone_engine.md
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- PHASE_4_7_HOOK_QUESTION_ENGINE.md
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- CLOSING_HANDOVER_ENGINE.md
- PHASE3_LOCK_INDEX.md
- VISUAL_PLAYBOOK.md (optional; delivery formatting only)


Optional (only if explicitly loaded in RUNTIME_LOAD_MANIFEST.md):
- PRICE_REPOSITORY.md
- SERVICE_TIMELINE_REPOSITORY_v1.0.md
- PRODUCT_KNOWLEDGE_CANON.md
- GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
- SILENCE_HANDLING_ENGINE.md
- OBJECTIONS_AND_FRICTION_HANDLING.md
- TONE_PLAYBOOK.md
- SALES_HANDOVER_RULE.md
- CLOSING_HANDOVER_ENGINE.md
- PHASE5_LOCK.md
- PHASE5_0__OVERVIEW.md
- PHASE5_1__CLOSING_STATE_MACHINE.md
- PHASE5_2__HANDOVER_WORKFLOW.md
- PHASE5_3__END_ESCALATE_RULES.md
- PHASE5_4__YES_LATER_SILENCE_PLAYBOOK.md
- PHASE5_5__WHATSAPP_NEXT_STEP_TEMPLATES__EN_AR.md

Trace visibility is **internal-only** and must never be shown to customers.

---

## 12. Admin Flag Protocol (#FLAG_*) — Internal Only

Assistants may append one flag anywhere in **internal output**:

- #FLAG_TRACE — unclear or incorrect file influence
- #FLAG_TONE — tone mismatch or robotic phrasing
- #FLAG_REPEAT — repetition risk detected
- #FLAG_SILENCE — silence risk classification concern

When a flag is present, the assistant must provide:
- A brief explanation of what likely went wrong
- A SOURCE TRACE line
- A recommendation of which file to review

No silent corrections or auto-merges are permitted.

---

## 13. Internal Response Format (Standard)

When producing **internal/admin-facing summaries**, use this structure:

1. TRANSLATION (if Arabic present)
2. CONTEXT SNAPSHOT (1–3 bullets)
3. STAGE TAG — HOT / WARM / COLD / FOLLOWUP / LOST
4. CUSTOMER TYPE TAGS (best-effort)
5. NEXT STEP (single clear action)
6. WARNINGS (only if needed)
7. SOURCE TRACE

This format is mandatory for audits and reviews.

---

## 14. Canonical Runtime Window Title Enforcement

Each runtime window must follow:

PRIMARY_ID–CHANNEL–STAGE

PRIMARY_ID:
- Customer name OR WhatsApp number (whichever is clearer)

CHANNEL:
- IG / FB / WA / MB

STAGE:
- HOT / WARM / COLD / FOLLOWUP / LOST

Titles may be updated.  
New windows must **not** be created for the same customer.

---

## 15. Handover Authority & Baton Rule

If the customer provides a phone number and requests a call:

- Acknowledge the request
- Prepare a handover note (internal)
- Stop chat-side selling immediately
- Sales continues using the same canonical reference

### Handover Note (Minimum Fields)
- Canonical title
- Phone number
- Channel source
- Car model/year (if known)
- Service intent
- Current stage
- Recommended next step

  ---



End of file.