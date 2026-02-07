# PHASE3A_QUALIFICATION_DECISION_MATRIX.md (LOCKED)

────────────────────────────────────────────────────────────
PHASE 3A — QUALIFIER-FIRST MATRIX (NO DRIFT SPEC)
────────────────────────────────────────────────────────────

Purpose:
- Define the ONE-question qualifier gate behavior for Phase 3A.
- Define deterministic normalization rules (Answer → Canonical Value).
- Define sequencing rules for AGE buckets (including the “2nd qualifier” flow).
- Ensure Phase 3A hands off cleanly into Phase 3B with normalized params.

Hard rules:
- Max 1 question per assistant turn.
- Phase 3A must NOT price.
- Phase 3A must NOT re-ask vehicle details.
- If the user does NOT answer the qualifier and repeats “how much” or repeats the service:
  - Repeat the SAME qualifier question (no new question).

Terminology:
- “Primary qualifier” = service-specific question (PPF/CERAMIC/TINT/WRAP/POLISHING).
- “Paint-gate qualifier” = repaint/deep-scratch check (used by AGE rules).

────────────────────────────────────────────────────────────
3A.0 SEQUENCING RULES — VEHICLE_AGE_BUCKET (HARD)
────────────────────────────────────────────────────────────

Goal:
- AGE_7_PLUS_YEARS must prioritize paint-gate first (prevents unsafe assumptions).
- AGE_3_6_YEARS allows a SECOND qualifier (paint-gate) after the primary qualifier answer.
- AGE_0_3_YEARS goes straight: primary qualifier → Phase 3B.

RULE A — AGE_0_3_YEARS
- Ask PRIMARY qualifier (PPF/CERAMIC/TINT/WRAP/POLISHING).
- After answer is normalized → move to PHASE_3B immediately.

RULE B — AGE_3_6_YEARS
- Ask PRIMARY qualifier first.
- After answer is normalized:
  - If PAINT_CONDITION_GATE is UNKNOWN:
    - Ask paint-gate qualifier (repaint/deep scratches) as the SECOND qualifier (next turn).
    - Then normalize PAINT_CONDITION_GATE and proceed to PHASE_3B.
  - If PAINT_CONDITION_GATE already known → proceed to PHASE_3B.

RULE C — AGE_7_PLUS_YEARS
- Ask paint-gate qualifier FIRST (repaint/deep scratches).
- If user answers YES (repaint/deep scratches present):
  - Normalize PAINT_CONDITION_GATE=REQUIRES_REVIEW
  - Proceed to PHASE_3B, but Phase 3B must treat it as constrained (no confident “prep path” claims).
  - If your Phase 3B supports an inspection/photo request route, it may trigger there.
- If user answers NO:
  - Normalize PAINT_CONDITION_GATE=CLEAR
  - Ask PRIMARY qualifier next (next turn)
  - Then proceed to PHASE_3B.

Note:
- This spec does NOT require adding any new engines.
- Implementation lives in QUALIFICATION_ENGINE.md (Phase 3A section),
  using this exact order and using the normalization tables below.

────────────────────────────────────────────────────────────
3A.1 NORMALIZATION TABLES (HARD) — ANSWER → CANONICAL VALUES
────────────────────────────────────────────────────────────

These tables are “spec-only” and must be implemented deterministically in QUALIFICATION_ENGINE.md.
No fuzzy interpretation beyond the listed patterns.

3A.1.1 PAINT CONDITION GATE (REPAINT / DEEP SCRATCHES)
Parameter: PAINT_CONDITION_GATE
Allowed Values:
- CLEAR
- REQUIRES_REVIEW
- UNKNOWN

Answer mapping:
- YES patterns → REQUIRES_REVIEW
  Examples: "yes", "y", "yeah", "repaint", "رش", "صبغ", "فيه رش", "فيه صبغ", "خدوش عميقة", "scratch", "deep"
- NO patterns → CLEAR
  Examples: "no", "n", "never", "ما فيه", "لا", "بدون"
- Otherwise → UNKNOWN

3A.1.2 PPF DRIVING PATTERN
Parameter: PPF_DRIVING_PATTERN
Allowed Values:
- CITY
- HIGHWAY
- MIXED
- UNKNOWN

Answer mapping:
- CITY patterns → CITY
  Examples: "city", "inside city", "mostly city", "المدينة", "داخل المدينة"
- HIGHWAY patterns → HIGHWAY
  Examples: "highway", "long distance", "travel", "lines", "خطوط", "سفر", "سريع"
- MIXED patterns → MIXED
  Examples: "both", "mix", "sometimes", "اثنين", "خليط"
- Otherwise → UNKNOWN

3A.1.3 CERAMIC WASH PATTERN
Parameter: CERAMIC_WASH_PATTERN
Allowed Values:
- BUCKET_LOCALITY
- AUTO_TUNNEL
- WATERLESS_MALL
- PRO_WASH_CENTER
- MIXED
- UNKNOWN

Answer mapping:
- BUCKET_LOCALITY patterns → BUCKET_LOCALITY
  Examples: "bucket", "hand", "manual", "سطل", "يدوي", "في المواقف", "بالمنطقة"
- AUTO_TUNNEL patterns → AUTO_TUNNEL
  Examples: "automatic", "tunnel", "machine", "آلي", "نفق"
- WATERLESS_MALL patterns → WATERLESS_MALL
  Examples: "waterless", "mall", "بدون ماء", "في المول", "في المولات"
- PRO_WASH_CENTER patterns → PRO_WASH_CENTER
  Examples: "professional", "wash center", "detailing", "مركز غسيل", "محترف", "دِتيلنق"
- MIXED patterns → MIXED
  Examples: "mix", "both", "sometimes", "خليط"
- Otherwise → UNKNOWN

3A.1.4 TINT COVERAGE
Parameter: TINT_COVERAGE
Allowed Values:
- FRONT_ONLY
- SIDES_REAR
- FULL
- UNKNOWN

Answer mapping:
- FRONT_ONLY patterns → FRONT_ONLY
  Examples: "front", "front only", "windshield only", "الأمامي", "قدام"
- SIDES_REAR patterns → SIDES_REAR
  Examples: "sides", "rear", "sides and back", "الجوانب", "الخلف", "الجوانب والخلف"
- FULL patterns → FULL
  Examples: "full", "all", "everything", "كامل", "الكل"
- Otherwise → UNKNOWN

3A.1.5 WRAP FINISH
Parameter: WRAP_FINISH
Allowed Values:
- GLOSS
- SATIN
- MATTE
- UNKNOWN

Answer mapping:
- GLOSS patterns → GLOSS
  Examples: "gloss", "shiny", "لامع"
- SATIN patterns → SATIN
  Examples: "satin", "ساتان"
- MATTE patterns → MATTE
  Examples: "matte", "مطفي"
- Otherwise → UNKNOWN

3A.1.6 POLISHING PACKAGE SCOPE
Parameter: POLISHING_PACKAGE
Allowed Values:
- SILVER_EXTERIOR_ONLY
- GOLD_FULL_DETAIL
- UNKNOWN

Answer mapping:
- SILVER_EXTERIOR_ONLY patterns → SILVER_EXTERIOR_ONLY
  Examples: "exterior", "outside", "خارجي", "الخارجي فقط", "silver", "سلفر"
- GOLD_FULL_DETAIL patterns → GOLD_FULL_DETAIL
  Examples: "full", "interior", "engine", "inside", "كامل", "داخلي", "غرفة المكينة", "gold", "قولد"
- Otherwise → UNKNOWN

Implementation note:
- If any parameter remains UNKNOWN after a user answer:
  - Phase 3A should repeat the SAME qualifier question once (no new question).
  - If still UNKNOWN after repetition, allow Phase 3B to proceed with “needs clarification / human follow-up” posture.

────────────────────────────────────────────────────────────
END OF SPEC BLOCK — BELOW: EXISTING MATRIX CONTENT
────────────────────────────────────────────────────────────

Role:
- Phase 3A runs AFTER Phase 0–2 is complete (service_intent + vehicle_model + vehicle_year are known).
- Phase 3A asks the minimum necessary qualifier question(s) (one question per turn max).
- Phase 3A outputs ONLY normalized keys for Phase 3B (SKU/pricing/prep). No pricing. No education blocks.

Hard rules:
- One question per assistant reply (max).
- No product/SKU claims, no durations, no warranties, no regulations.
- Do NOT invent services beyond the canonical service intents.
- Do NOT output brand claims unless explicitly allowed elsewhere.

Dependencies (authoritative sources):
- VEHICLE_AGE_BUCKET: GLOBAL_CORE_CONTEXT_PARAMETERS.md
- Vehicle normalization/aliases: GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
- Service intent canon/detection: GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md (+ service canon bundle if present)
- Phrase selection/routing: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md + PHASE4_6_HUMAN_PHRASE_LIBRARY.md

Canonical service intents (Phase 3A output keys):
- PPF
- CERAMIC
- TINT
- WRAP
- POLISHING

Vehicle age buckets (input):
- AGE_0_3_YEARS
- AGE_3_6_YEARS
- AGE_7_PLUS_YEARS
- UNKNOWN

Normalized output keys (Phase 3A → Phase 3B):
- service_intent (PPF|CERAMIC|TINT|WRAP|POLISHING)
- vehicle_model
- vehicle_year
- vehicle_age_bucket
- qualifier_question_id (string)
- qualifier_answer (string enum per service)
- paint_risk_flag (OK|RISK|UNKNOWN)  // “RISK” = repaint or deep scratches mentioned
- inspection_required (true|false)
- photo_requested (true|false)
- next_action (HANDOFF_3B|ASK_NEXT_QUALIFIER|REQUEST_PHOTO|RECOMMEND_INSPECTION)

## 1.1) Canonical Phase 3A Output Requirements (HARD)
Phase 3A must emit:
- phase = PHASE_3A
- service_intent (canonical)
- vehicle_age_bucket (canonical)
- qualifier_triggered = TRUE/FALSE
- selected_phrase_id (PHASE3A_Q_* if triggered)

When qualifier is answered and normalized:
- next_phase must become PHASE_3B

--------------------------------------------------------------------------
## 0) Global gating (applies to ALL services)

G0.1) Minimum context required
Trigger:
- If vehicle_model OR vehicle_year missing → this is NOT Phase 3A. Return to Phase 0–2 qualification.

G0.2) Vehicle age bucket resolution
Input:
- vehicle_year
Output:
- vehicle_age_bucket set via VEHICLE_AGE_BUCKET parameter rules

G0.3) Paint risk override (AGE_7_PLUS_YEARS only)
Trigger:
- vehicle_age_bucket == AGE_7_PLUS_YEARS
Behavior:
- Ask paint-risk question FIRST before service-specific qualifier.
- If paint_risk_flag == RISK → request photo and/or recommend inspection (do not proceed to 3B yet).
- If paint_risk_flag == OK → proceed to service-specific qualifier next turn.
- If customer cannot provide photo/details now → allow a controlled handoff with paint_risk_flag=UNKNOWN,
  inspection_required=true, next_action=HANDOFF_3B (Phase 3B should keep it conservative and may suggest inspection later).

Paint-risk question (single question; one turn):
- “Before we proceed, is there any repaint work or deep scratches on the panels?”

Normalization:
- If customer indicates repaint OR deep scratches → paint_risk_flag=RISK, photo_requested=true, inspection_required=true, next_action=REQUEST_PHOTO (or RECOMMEND_INSPECTION if they refuse photos)
- If customer indicates no repaint/deep scratches → paint_risk_flag=OK, next_action=ASK_NEXT_QUALIFIER
- If unclear → paint_risk_flag=UNKNOWN, next_action=REQUEST_PHOTO

--------------------------------------------------------------------------
## 8) Qualifier non-response handling (Option A — MAX ONE REPEAT)

Goal:
- Avoid looping the same question endlessly.
- Keep the customer experience natural while preserving Phase 3A gating.

Rule:
If a qualifier is pending and the customer:
- asks “how much / price / cost”
- repeats only the service word
- asks an unrelated question without answering the qualifier

Then:
1) Repeat the qualifier ONCE using a “nudge” variant (justification + same single question).
2) If still not answered after the nudge:
  - Set qualifier_answer=UNKNOWN
  - Set next_action=HANDOFF_3B
  - Set selected_phrase_id=PHASE3B_ACK_NEUTRAL_UNKNOWN

Notes:
- One question per turn remains mandatory.
- This prevents deadlocks and reduces silence risk.

--------------------------------------------------------------------------
## 2.1) Age Bucket Derivation (HARD)
If vehicle_year is known:
- Compute VEHICLE_AGE_BUCKET using GLOBAL_CORE_CONTEXT_PARAMETERS.md allowed values:
  - AGE_0_3_YEARS
  - AGE_3_6_YEARS
  - AGE_7_PLUS_YEARS
If vehicle_year is missing:
- VEHICLE_AGE_BUCKET = UNKNOWN
- Phase 3A must not attempt “age-based gating” (fall back to primary qualifier only).

--------------------------------------------------------------------------
## 2.2) Phase 3A Sequencing (HARD)
Apply the sequencing rules in section 3A.0 exactly:
- AGE_0_3_YEARS: primary qualifier only
- AGE_3_6_YEARS: primary qualifier then paint-gate as second qualifier (if unknown)
- AGE_7_PLUS_YEARS: paint-gate first, then primary qualifier

No other sequencing is allowed.

--------------------------------------------------------------------------
## 1) PPF — Phase 3A qualifier matrix

PPF primary qualifier:
- Driving pattern: CITY vs HIGHWAY

PPF-AGE_0_3_YEARS
Step order:
1) Ask PPF driving pattern qualifier (city/highway)
Outputs:
- qualifier_question_id=PPF_DRIVING_PATTERN
- qualifier_answer=CITY|HIGHWAY|MIXED|UNKNOWN
- next_action=HANDOFF_3B

PPF-AGE_3_6_YEARS
Step order:
1) Ask PPF driving pattern qualifier (city/highway)
2) If customer mentions paint concerns (chips/scratches/repaint) OR answer is unclear → request photo/inspection
Outputs:
- qualifier_question_id=PPF_DRIVING_PATTERN
- qualifier_answer=CITY|HIGHWAY|MIXED|UNKNOWN
- If concerns: paint_risk_flag=RISK or UNKNOWN, photo_requested=true, inspection_required=true, next_action=REQUEST_PHOTO
- Else: next_action=HANDOFF_3B

PPF-AGE_7_PLUS_YEARS
Step order:
1) Ask paint-risk question (repaint/deep scratches) (GLOBAL G0.3)
2) If OK → ask PPF driving pattern qualifier next turn
Outputs:
- Step 1 outputs paint_risk_flag + next_action
- Step 2 outputs qualifier_question_id=PPF_DRIVING_PATTERN, qualifier_answer, next_action=HANDOFF_3B

PPF qualifier question (one question):
- “Do you mostly drive in the city, or do you often travel long distances on highways?”

### 1.1B) Normalization (PPF Driving Pattern)
After user answers the PPF driving qualifier:
- Normalize into PPF_DRIVING_PATTERN using table 3A.1.2
- If UNKNOWN after answer:
  - Repeat the same qualifier question once
  - If still UNKNOWN, proceed to Phase 3B with PPF_DRIVING_PATTERN=UNKNOWN

--------------------------------------------------------------------------
## 2) CERAMIC — Phase 3A qualifier matrix

CERAMIC primary qualifier:
- Wash pattern: HAND|AUTOMATIC|WATERLESS|MIXED

CERAMIC-AGE_0_3_YEARS
Step order:
1) Ask ceramic wash-pattern qualifier
Outputs:
- qualifier_question_id=CERAMIC_WASH_PATTERN
- qualifier_answer=HAND|AUTOMATIC|WATERLESS|MIXED|UNKNOWN
- next_action=HANDOFF_3B

CERAMIC-AGE_3_6_YEARS
Step order:
1) Ask ceramic wash-pattern qualifier
2) If customer indicates “bad paint”, “needs correction”, “scratches”, “repaint”, “heavy swirls” → request photo/inspection (do not block 3B if they insist; set inspection_required=true)
Outputs:
- qualifier_question_id=CERAMIC_WASH_PATTERN
- qualifier_answer=HAND|AUTOMATIC|WATERLESS|MIXED|UNKNOWN
- If concerns: paint_risk_flag=RISK, photo_requested=true, inspection_required=true, next_action=REQUEST_PHOTO
- Else: next_action=HANDOFF_3B

CERAMIC-AGE_7_PLUS_YEARS
Step order:
1) Ask paint-risk question (repaint/deep scratches) (GLOBAL G0.3)
2) If OK → ask ceramic wash-pattern qualifier next turn
Outputs:
- Step 1 outputs paint_risk_flag + next_action
- Step 2 outputs qualifier_question_id=CERAMIC_WASH_PATTERN, qualifier_answer, next_action=HANDOFF_3B

Ceramic qualifier question (one question):
- “To guide this properly, how do you usually wash the car — bucket/hand wash, tunnel/automatic wash, mall waterless wash, or a mix?”

### 2.1B) Normalization (Ceramic Wash Pattern)
After user answers the ceramic wash qualifier:
- Normalize into CERAMIC_WASH_PATTERN using table 3A.1.3
- If UNKNOWN after answer:
  - Repeat the same qualifier question once
  - If still UNKNOWN, proceed to Phase 3B with CERAMIC_WASH_PATTERN=UNKNOWN

--------------------------------------------------------------------------
## 3) TINT — Phase 3A qualifier matrix

TINT primary qualifier:
- Coverage choice: FRONT_ONLY vs SIDES_REAR vs FULL

TINT-ALL_AGE_BUCKETS (0–3 / 3–6 / 7+)
Notes:
- Tint is not paint-risk sensitive. Paint-risk override does not apply.
Step order:
1) Ask coverage qualifier (front / sides+rear / full)
Outputs:
- qualifier_question_id=TINT_COVERAGE
- qualifier_answer=FRONT_ONLY|SIDES_REAR|FULL|UNKNOWN
- next_action=HANDOFF_3B

Tint qualifier question (one question):
- “For tint, do you want front only, sides and back, or full coverage?”

### 3.1B) Normalization (Tint Coverage)
After user answers the tint coverage qualifier:
- Normalize into TINT_COVERAGE using table 3A.1.4
- If UNKNOWN after answer:
  - Repeat the same qualifier question once
  - If still UNKNOWN, proceed to Phase 3B with TINT_COVERAGE=UNKNOWN

--------------------------------------------------------------------------
## 4) WRAP — Phase 3A qualifier matrix

WRAP primary qualifier:
- Finish choice: GLOSS vs SATIN vs MATTE

WRAP-AGE_0_3_YEARS
Step order:
1) Ask wrap finish qualifier (gloss/satin/matte)
Outputs:
- qualifier_question_id=WRAP_FINISH
- qualifier_answer=GLOSS|SATIN|MATTE|UNKNOWN
- next_action=HANDOFF_3B

WRAP-AGE_3_6_YEARS
Step order:
1) Ask wrap finish qualifier (gloss/satin/matte)
2) If customer mentions repaint or deep scratches → request photo/inspection
Outputs:
- qualifier_question_id=WRAP_FINISH
- qualifier_answer=GLOSS|SATIN|MATTE|UNKNOWN
- If concerns: paint_risk_flag=RISK, photo_requested=true, inspection_required=true, next_action=REQUEST_PHOTO
- Else: next_action=HANDOFF_3B

WRAP-AGE_7_PLUS_YEARS
Step order:
1) Ask paint-risk question (repaint/deep scratches) (GLOBAL G0.3)
2) If OK → ask wrap finish qualifier next turn
Outputs:
- Step 1 outputs paint_risk_flag + next_action
- Step 2 outputs qualifier_question_id=WRAP_FINISH, qualifier_answer, next_action=HANDOFF_3B

Wrap finish qualifier question (one question):
- “For wrap, do you prefer gloss, satin, or matte?”

### 4.1B) Normalization (Wrap Finish)
After user answers the wrap finish qualifier:
- Normalize into WRAP_FINISH using table 3A.1.5
- If UNKNOWN after answer:
  - Repeat the same qualifier question once
  - If still UNKNOWN, proceed to Phase 3B with WRAP_FINISH=UNKNOWN

--------------------------------------------------------------------------
## 5) POLISHING — Phase 3A qualifier matrix

POLISHING qualifiers:
P1) Goal qualifier (factory-restore intent)
P2) Package qualifier (Exterior only vs Exterior+Interior+Engine bay)

POLISHING-ALL_AGE_BUCKETS (0–3 / 3–6 / 7+)
Notes:
- Polishing inherently touches paint condition; do not block based on age.
Step order:
1) Ask goal qualifier: “restore to factory condition?”
2) Then ask package qualifier: exterior only vs exterior+interior+engine bay

Goal qualifier question (one question):
- “Is your main goal to restore the car closer to factory condition?”

Goal normalization:
- YES|NO|UNKNOWN

Package qualifier question (one question):
- “Do you want exterior polishing only, or exterior + interior + engine bay?”

Package normalization (internal only; do NOT output as public product name unless registry confirms):
- EXTERIOR_ONLY
- EXTERIOR_INTERIOR_ENGINE

Outputs after Step 1:
- qualifier_question_id=POLISHING_GOAL_FACTORY_RESTORE
- qualifier_answer=YES|NO|UNKNOWN
- next_action=ASK_NEXT_QUALIFIER

Outputs after Step 2:
- qualifier_question_id=POLISHING_PACKAGE
- qualifier_answer=EXTERIOR_ONLY|EXTERIOR_INTERIOR_ENGINE|UNKNOWN
- next_action=HANDOFF_3B

### 5.1B) Normalization (Polishing Package)
After user answers the polishing scope qualifier:
- Normalize into POLISHING_PACKAGE using table 3A.1.6
- If UNKNOWN after answer:
  - Repeat the same qualifier question once
  - If still UNKNOWN, proceed to Phase 3B with POLISHING_PACKAGE=UNKNOWN

--------------------------------------------------------------------------
## 8) Paint Condition Gate (Age Override)

Goal:
- For older vehicles, do not assume paint is suitable without a repaint/deep-scratch check.
- This gate must not conflict with the “one question per turn” rule.

### 8.1) Paint Gate Normalization
After user answers the paint-gate question:
- Normalize into PAINT_CONDITION_GATE using table 3A.1.1
- If UNKNOWN after answer:
  - Repeat the same paint-gate question once
  - If still UNKNOWN:
    - Set PAINT_CONDITION_GATE=UNKNOWN
    - Proceed to Phase 3B (conservative posture; no strong assumptions).

### 8.2) Paint Gate Placement (MUST FOLLOW)
- AGE_7_PLUS_YEARS: paint-gate first
- AGE_3_6_YEARS: paint-gate second (after primary qualifier answer), only if unknown
- AGE_0_3_YEARS: no paint-gate unless customer explicitly raises repaint/scratch concern

--------------------------------------------------------------------------
## 6) Phase 3A completion conditions (handoff to Phase 3B)

HANDOFF_3B allowed only when:
- vehicle_model present AND vehicle_year present
- service_intent present
- Required qualifier for that service_intent is captured (per sections above)
- If vehicle_age_bucket == AGE_7_PLUS_YEARS:
  - paint_risk_flag != UNKNOWN (prefer OK/RISK)
  - If RISK: photo_requested=true OR inspection_required=true and customer refused photo (logged elsewhere)

--------------------------------------------------------------------------
## 7) Non-negotiables (governance lock)

- Phase 3A MUST NOT output pricing.
- Phase 3A MUST NOT output SKU names.
- Phase 3A MUST NOT ask more than one question in a single assistant message.
- Phase 3A MUST defer all quoting/option ladders/objection handling to Phase 3B+ engines.
