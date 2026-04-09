# VIDEO TRIGGER MATRIX (PHASE 8)

Purpose:
Central authority mapping customer intent → visual trigger → category → phase behavior.

This file normalizes trigger usage across:
- VIDEO_LIBRARY_INDEX.md
- PHASE8_VISUAL_INTELLIGENCE_MAP.md
- runtime visual tools

---

## STRUCTURE

Each trigger defines:

- TRIGGER_ID
- CUSTOMER_INTENT
- SERVICE
- CATEGORY_PREFERENCE
- PHASE_BEHAVIOR
- VIDEO_SELECTION_RULE

---

## CORE TRIGGERS

### 1. PPF_SELF_HEAL_QUESTION

CUSTOMER_INTENT:
Customer asks if PPF self-heals scratches

SERVICE:
PPF

CATEGORY_PREFERENCE:
PROOF

PHASE_BEHAVIOR:
- Early phase → defer
- Mid phase → allow
- Comparison → immediate release

VIDEO_SELECTION_RULE:
Select video where:
- PRIMARY_TRIGGER = PPF_SELF_HEAL_QUESTION
- CATEGORY = PROOF

---

### 2. PPF_PROTECTION_STRENGTH_QUESTION

CUSTOMER_INTENT:
Customer asks how strong PPF is (stone chips, scratches)

SERVICE:
PPF

CATEGORY_PREFERENCE:
PROOF

PHASE_BEHAVIOR:
- Same as self-heal

VIDEO_SELECTION_RULE:
PRIMARY_TRIGGER = PPF_PROTECTION_STRENGTH_QUESTION

---

### 3. PPF_VS_CERAMIC_CONFUSION

CUSTOMER_INTENT:
Customer confused between PPF and ceramic

SERVICE:
MULTI

CATEGORY_PREFERENCE:
COMPARISON

PHASE_BEHAVIOR:
- Allow earlier than proof
- Can trigger immediate visual

VIDEO_SELECTION_RULE:
SERVICE = MULTI
CATEGORY = COMPARISON

---

### 4. PPF_INSTALLATION_QUALITY_QUESTION

CUSTOMER_INTENT:
Customer doubts installation quality

SERVICE:
PPF

CATEGORY_PREFERENCE:
PROCESS

PHASE_BEHAVIOR:
- Mid / late phase preferred
- Trust-building context

VIDEO_SELECTION_RULE:
PRIMARY_TRIGGER = PPF_INSTALLATION_QUALITY_QUESTION

---

### 5. PPF_BRAND_QUALITY_QUESTION

CUSTOMER_INTENT:
Customer doubts brand / film quality

SERVICE:
PPF

CATEGORY_PREFERENCE:
TRUST

PHASE_BEHAVIOR:
- Late phase preferred
- After proof/process

VIDEO_SELECTION_RULE:
PRIMARY_TRIGGER = PPF_BRAND_QUALITY_QUESTION

---

### 6. PPF_DECISION_CONFUSION

CUSTOMER_INTENT:
Customer unsure what to choose

SERVICE:
PPF

CATEGORY_PREFERENCE:
RESULT

PHASE_BEHAVIOR:
- Phase 5 only
- Must include follow-up question

VIDEO_SELECTION_RULE:
PRIMARY_TRIGGER = PPF_DECISION_CONFUSION

---

## RULES

- Do not introduce new triggers without mapping to existing videos
- Trigger must map to PRIMARY_TRIGGER in VIDEO_LIBRARY_INDEX
- Category must follow rollout schema unless explicitly allowed
- One trigger → one dominant intent (no mixing)

---

STATUS:
Phase 8 refinement — trigger normalization layer

---

## EXPANDED TRIGGERS

### 7. CERAMIC_PROCESS_VALUE_QUESTION

CUSTOMER_INTENT:
Customer wants to understand ceramic process and why it matters

SERVICE:
CERAMIC

CATEGORY_PREFERENCE:
PROCESS

PHASE_BEHAVIOR:
- Mid / late phase preferred
- Best when customer questions value or process quality

VIDEO_SELECTION_RULE:
PRIMARY_TRIGGER = CERAMIC_PROCESS_VALUE_QUESTION

---

### 8. CERAMIC_TRUST_VALIDATION

CUSTOMER_INTENT:
Customer wants reassurance through real customer credibility

SERVICE:
CERAMIC

CATEGORY_PREFERENCE:
TESTIMONIAL

PHASE_BEHAVIOR:
- Late phase preferred
- Trust-building context

VIDEO_SELECTION_RULE:
PRIMARY_TRIGGER = CERAMIC_TRUST_VALIDATION

---

### 9. CERAMIC_RESULT_VISUAL_PROOF

CUSTOMER_INTENT:
Customer wants to see final ceramic result visually

SERVICE:
CERAMIC

CATEGORY_PREFERENCE:
RESULT

PHASE_BEHAVIOR:
- Phase 5 / decision support
- Can support confidence after explanation

VIDEO_SELECTION_RULE:
PRIMARY_TRIGGER = CERAMIC_RESULT_VISUAL_PROOF

---

### 10. POLISH_RESULT_VISUAL_PROOF

CUSTOMER_INTENT:
Customer wants to see polishing result visually

SERVICE:
POLISHING

CATEGORY_PREFERENCE:
RESULT

PHASE_BEHAVIOR:
- Mid / late phase
- Best for before/after understanding

VIDEO_SELECTION_RULE:
PRIMARY_TRIGGER = POLISH_RESULT_VISUAL_PROOF

---

### 11. POLISH_TRUST_VALIDATION

CUSTOMER_INTENT:
Customer wants reassurance from other polishing customers

SERVICE:
POLISHING

CATEGORY_PREFERENCE:
TESTIMONIAL

PHASE_BEHAVIOR:
- Late phase preferred
- Trust-building context

VIDEO_SELECTION_RULE:
PRIMARY_TRIGGER = POLISH_TRUST_VALIDATION

---

### 12. CUSTOMER_UNSURE_PROTECTION

CUSTOMER_INTENT:
Customer is unsure which protection direction makes sense

SERVICE:
MULTI

CATEGORY_PREFERENCE:
EDUCATION

PHASE_BEHAVIOR:
- Early to mid phase
- Best for broad confusion before narrowing

VIDEO_SELECTION_RULE:
PRIMARY_TRIGGER = CUSTOMER_UNSURE_PROTECTION

