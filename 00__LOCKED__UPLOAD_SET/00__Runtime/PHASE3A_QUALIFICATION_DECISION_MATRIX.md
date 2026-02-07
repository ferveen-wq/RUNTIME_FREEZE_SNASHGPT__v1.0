# PHASE3A_QUALIFICATION_DECISION_MATRIX.md (LOCKED)

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

Paint-risk question (single question; one turn):
- “Before we proceed, is there any repaint work or deep scratches on the panels?”

Normalization:
- If customer indicates repaint OR deep scratches → paint_risk_flag=RISK, photo_requested=true, inspection_required=true, next_action=REQUEST_PHOTO (or RECOMMEND_INSPECTION if they refuse photos)
- If customer indicates no repaint/deep scratches → paint_risk_flag=OK, next_action=ASK_NEXT_QUALIFIER
- If unclear → paint_risk_flag=UNKNOWN, next_action=REQUEST_PHOTO

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
