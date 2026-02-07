# PHASE0_2_LOCK_INDEX.md
Version: 1.0
Scope: Phase 0–2 Stability Lock (L0 + L1 + minimum routing invariants)
Status: LOCKED
Last Updated: 2026-02-07

## PURPOSE
This file freezes Phase 0–2 behavior so later phrase edits (Phase 3–5 content, persuasion, pricing, education)
cannot leak into Phase 0–2 intake + minimal qualification.

This file introduces NO new selling content.
It is a governance fence: what Phase 0–2 is allowed to do, and what it must never do.

---

## AUTHORITATIVE DEPENDENCIES (READ-ONLY IN PHASE 0–2)
- CUSTOMER_CHAT_INTAKE_RULES.md
- QUALIFICATION_ENGINE.md
- GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
- GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- OUTPUT_RESPONSE_TEMPLATE.md
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md

---

## PHASE 0–2 HARD BOUNDARIES
1) Phase 0–2 MUST NOT:
   - Enter Phase 3 or Phase 4 behaviors
   - Output pricing, options, ladders, discounts, timelines, guarantees, regulations
   - Output hooks beyond minimum qualification
   - Introduce brands unless explicitly asked by the customer

2) Phase 0–2 MUST:
   - Capture minimum context safely (service intent + vehicle model/year)
   - Keep responses short, one question max
   - Preserve already-known vehicle fields (no “forgetting” year)
   - Avoid clarification loops (same missing_fields asked repeatedly)

---

## LOCKED OUTPUT SURFACES (ONLY THESE MAY BE USED IN PHASE 0–2)

### L0 — BROWSING / GENERIC DISCOVERY
Allowed phrase IDs:
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md → "L.0 BROWSING SAFE PRIMER"

Lock rules:
- L0 is used ONLY when request_type = BROWSING_GENERIC
- L0 must be service-anchored but must NOT ask vehicle qualification
- L0 must contain exactly ONE soft question
- L0 must not mention price or packages

### L1 — QUALIFICATION CLARIFIERS (VEHICLE DETAILS)
Allowed phrase IDs:
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md → "L.1 QUALIFICATION CLARIFIER (V1/V2/V3)"
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md → "L.1 MODEL_ONLY"
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md → "L.1 YEAR_ONLY"

Lock rules:
- Exactly ONE question total
- Selection is driven ONLY by missing_fields:
  - [vehicle_model, vehicle_year] → ask V1/V2/V3 (model+year)
  - [vehicle_model] → ask MODEL_ONLY
  - [vehicle_year] → ask YEAR_ONLY

### A2 — SERVICE LIST REQUEST (WHEN CUSTOMER ASKS “what services”)
Allowed phrase IDs:
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md → "A2_SERVICE_LIST_REQUEST"

Lock rules:
- Must list only approved services (PPF / ceramic / tint / wrap / polishing)
- Must end with ONE question max (model+year)

### A4 — GREETING (BUSINESS-FOCUSED, MINIMUM QUALIFICATION)
Allowed phrase IDs:
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md → "A4_GREETING_SERVICE_CONTEXT"

Lock rules:
- Greeting must be business-focused and ask model+year (one question)

---

## LOCKED ROUTING INVARIANTS (PHASE 0–2)

### 1) Service Confirmed Priority (HARD)
If user explicitly mentions a known service keyword:
- request_type MUST be SERVICE_CONFIRMED
- service_intent MUST be set to that service
- active_service_context MUST track service_intent
- If minimum vehicle context missing → missing_fields must be set accordingly and L1 must be used

Source of truth:
- QUALIFICATION_ENGINE.md (SERVICE_CONFIRMED_PRIORITY)
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md (L1 routing rules)

### 2) Vehicle Model Validation (STRICT — Phase 0–2)
If vehicle_model AND vehicle_year are present:
- Validate vehicle_model against GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
- If validation FAILS:
  - Preserve vehicle_year (do not clear)
  - missing_fields MUST become [vehicle_model] only
  - Route to L1 MODEL_ONLY

Source of truth:
- QUALIFICATION_ENGINE.md (VEHICLE_MODEL_VALIDATION)

### 3) Partial Vehicle Carry-Forward (HARD — preserve year)
If the customer corrects only the model after a previous “model+year” attempt:
- vehicle_year MUST be carried forward
- next question MUST be MODEL_ONLY (not model+year again)

If the customer provides only year after model is known:
- next question MUST be YEAR_ONLY

Implementation requirement:
- missing_fields must always reflect only what is actually missing
- known vehicle_year must not be dropped by any routing overlay

### 4) Service Context Continuity Gate (HARD) — Phase 0–2
If missing_fields is non-empty (vehicle incomplete):
- The system MUST NOT enter “switch/stay on service” loops
- The system MUST prioritize L1 to complete vehicle context
- Service switching clarifiers are allowed ONLY if:
  - missing_fields is empty

Source of truth:
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md continuity gate sections

### 5) Debug Output Discipline (Owner only)
If debug_mode=on (owner testing):
- DEBUG_OUTPUT must be shown exactly once at top
- Must include:
  phase, request_type, service_intent, active_service_context, missing_fields, suppress_hooks, selected_phrase_id
- Must not leak internal file paths or extra analysis blocks

---

## ACCEPTANCE CRITERIA (PASS/FAIL)
Phase 0–2 is considered “LOCK PASS” only if all are true:
1) “bmx 2023” → keeps 2023, asks MODEL_ONLY
2) “jetour 52 2024” → treats “52” as invalid model token, preserves 2024, asks MODEL_ONLY (or clarifies model)
3) Service switch attempts while missing_fields non-empty do NOT cause switch/stay loop; system asks L1 only
4) No Phase 3/4 outputs appear (no options, no ladders, no persuasion blocks)
5) One question max per reply

End of file.
