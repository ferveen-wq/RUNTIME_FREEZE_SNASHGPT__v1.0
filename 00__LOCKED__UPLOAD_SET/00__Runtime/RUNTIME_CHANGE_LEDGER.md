# RUNTIME_CHANGE_LEDGER.md

Status: ACTIVE
Owner: Runtime Governance
Purpose: Track runtime changes from discussion to freeze, so patching stays sequential, auditable, and non-drifting.

---

## STATUS DEFINITIONS

Use only these statuses:

- DISCUSSED
- APPROVED_FOR_PATCH
- PATCHED_LOCAL
- VALIDATED_LOCAL
- PR_OPEN
- MERGED_MAIN
- TAGGED_GREEN
- FROZEN
- DEFERRED
- AUDITED_ONLY

---

## ENTRY FORMAT

Each change must record:

- CHANGE_ID
- AREA
- GOAL
- FILES
- STATUS
- VALIDATION
- MERGED
- TAGGED
- NOTES

---

## CHANGES

### CHANGE_ID: GOV_001
- AREA: Governance
- GOAL: Add runtime patch protocol into locked runtime
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PATCH_PROTOCOL.md
- STATUS: TAGGED_GREEN
- VALIDATION: Passed
- MERGED: Yes
- TAGGED:
  - runtime_green_pre_edu_recovery_v1_20260305
- NOTES:
  - Runtime patch discipline introduced

### CHANGE_ID: GOV_002
- AREA: Governance
- GOAL: Add zsh-safe shell / patch delivery standard
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PATCH_PROTOCOL.md
- STATUS: VALIDATED_LOCAL
- VALIDATION: Present in local validated runtime state
- MERGED: Yes
- TAGGED: runtime_ppf_phrase_rebalance_v1
- NOTES:
  - Default all runtime patch commands to zsh-safe format
  - VC Codex only for large or risky multi-file edits

### CHANGE_ID: GOV_003
- AREA: Governance
- GOAL: Add phrase governance standard
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md
- STATUS: VALIDATED_LOCAL
- VALIDATION: Present in local validated runtime state
- MERGED: Yes
- TAGGED: runtime_ppf_phrase_rebalance_v1
- NOTES:
  - Governs layman-first phrasing, mixed-answer safety, no false binary, no early front-PPF exposure

### CHANGE_ID: GOV_004
- AREA: Governance
- GOAL: Create runtime change ledger
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md
- STATUS: VALIDATED_LOCAL
- VALIDATION: Present in local validated runtime state
- MERGED: Yes
- TAGGED: runtime_ppf_phrase_rebalance_v1
- NOTES:
  - Tracks discussed vs patched vs merged vs frozen changes

---

### CHANGE_ID: SIL_001
- AREA: Silence Routing
- GOAL: Add silence suppression reasons / suppression-aware routing
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md
  - related silence routing files
- STATUS: TAGGED_GREEN
- VALIDATION: Passed
- MERGED: Yes
- TAGGED:
  - runtime_green_pre_edu_recovery_v1_20260305
- NOTES:
  - Prevent silence actions when PIM / visit / manual hold is active

### CHANGE_ID: SIL_002
- AREA: Silence Routing
- GOAL: Add global silence routing to assembly map
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- STATUS: TAGGED_GREEN
- VALIDATION: Passed
- MERGED: Yes
- TAGGED:
  - runtime_green_pre_edu_recovery_v1_20260305
- NOTES:
  - Silence becomes the message when active
  - No hooks / no extra blocks

### CHANGE_ID: SIL_003
- AREA: Phrase Layer / PPF Silence
- GOAL: Refine PHASE4_PPF_SILENCE_PRIMARY to reopen conversation without early front/full framing
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- STATUS: VALIDATED_LOCAL
- VALIDATION:
  - phrase_library_validator: passed
  - pre-commit: passed
  - regression_phase3a_chain: passed
  - silence_state_pack: passed
- MERGED: Yes
- TAGGED: runtime_ppf_phrase_rebalance_v1
- NOTES:
  - Patched locally only
  - New phrasing invites clarification instead of coverage-first narrowing

### CHANGE_ID: SIL_004
- AREA: Phrase Layer / PPF Silence
- GOAL: Refine PHASE4_PPF_SILENCE_COVERAGE_NARROW to avoid early front-PPF emphasis
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- STATUS: TAGGED_GREEN
- VALIDATION:
  - phrase_library_validator: passed
  - pre-commit: passed
  - regression_phase3a_chain: passed
  - silence_state_pack: passed
- MERGED: Yes
- TAGGED:
  - runtime_ppf_phrase_rebalance_v1
- NOTES:
  - Patched locally and validated
  - Keeps full protection as main path and avoids direct front-only push

### CHANGE_ID: SIL_005
- AREA: Phrase Layer / PPF Silence
- GOAL: Refine PHASE4_PPF_SILENCE_COMPARISON_SIMPLIFY to reopen comparison safely without creating loops
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- STATUS: TAGGED_GREEN
- VALIDATION:
  - phrase_library_validator: passed
  - pre-commit: passed
  - regression_phase3a_chain: passed
  - silence_state_pack: passed
- MERGED: Yes
- TAGGED:
  - runtime_ppf_phrase_rebalance_v1
- NOTES:
  - Patched locally and validated
  - Must follow silence recovery order
  - Must not trigger front PPF early
  - Must not create price / brand comparison loops

---

### CHANGE_ID: EDU_001
- AREA: Education Routing
- GOAL: Add basic micro-education routing before pricing
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- STATUS: TAGGED_GREEN
- VALIDATION: Passed
- MERGED: Yes
- TAGGED:
  - runtime_green_pre_edu_recovery_v1_20260305
- NOTES:
  - Uses existing Phase 4.6 wording only
  - Routes C.1 PPF and C.2 Ceramic explanation blocks

### CHANGE_ID: CMP_001
- AREA: Comparison Routing
- GOAL: Add minimal Phase 8 service comparison routing
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- STATUS: TAGGED_GREEN
- VALIDATION: Passed
- MERGED: Yes
- TAGGED:
  - runtime_green_post_phase8_comparison_v1_20260307
- NOTES:
  - Uses existing comparison phrase only
  - No new wording introduced

### CHANGE_ID: CMP_002
- AREA: Intake / Comparison Confusion
- GOAL: Detect vague compare / recommend requests
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/CUSTOMER_CHAT_INTAKE_RULES.md
- STATUS: TAGGED_GREEN
- VALIDATION: Passed
- MERGED: Yes
- TAGGED:
  - runtime_green_post_confusion_detector_v1_20260307
- NOTES:
  - Handles questions like difference / which one / recommend / Arabic equivalents

---

### CHANGE_ID: PPF_001
- AREA: Phase 3A PPF Framing
- GOAL: Shift PPF qualifier from coverage-first to protection-intent framing
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE3A_QUALIFICATION_DECISION_MATRIX.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- STATUS: TAGGED_GREEN
- VALIDATION: Passed
- MERGED: Yes
- TAGGED:
  - runtime_green_pre_ppf_framing_patch1_20260307
  - runtime_green_post_ppf_framing_patch1_20260307
- NOTES:
  - Kept same qualifier ID
  - Changed customer-facing phrasing to maximum protection vs practical protection

### CHANGE_ID: PPF_002
- AREA: PPF Phrase Audit
- GOAL: Remove early front/full bias from later-stage PPF phrases
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- STATUS: IN_PROGRESS
- VALIDATION: Partial
- MERGED: Yes
- TAGGED:
  - runtime_ppf_phrase_rebalance_v1
- NOTES:
  - Phase 4 / 5 phrase tightening in progress
  - Keep SKU ladder unchanged
  - Front PPF should remain last fallback unless customer explicitly asks

### CHANGE_ID: PPF_003
- AREA: PPF Negotiation Phrases
- GOAL: Refine PHASE5_PPF_NARROW_L2 to keep affordable full-body emphasis before front PPF fallback
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- STATUS: TAGGED_GREEN
- VALIDATION:
  - phrase_library_validator: passed
  - pre-commit: passed
  - regression_phase3a_chain: passed
  - silence_state_pack: passed
- MERGED: Yes
- TAGGED:
  - runtime_ppf_phrase_rebalance_v1
- NOTES:
  - Patched locally and validated
  - Keeps full-body coverage as the main path
  - Front PPF remains final fallback only

### CHANGE_ID: PPF_004
- AREA: PPF Negotiation Phrases
- GOAL: Refine PHASE5_PPF_EXIT_FORK_L3 so front PPF appears only as final budget fallback
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- STATUS: TAGGED_GREEN
- VALIDATION:
  - phrase_library_validator: passed
  - pre-commit: passed
  - regression_phase3a_chain: passed
  - silence_state_pack: passed
- MERGED: Yes
- TAGGED:
  - runtime_ppf_phrase_rebalance_v1
- NOTES:
  - Patched locally and validated
  - Uses budget framing, not comfort framing
  - Keeps front PPF as the last fallback after full-body options

### CHANGE_ID: PPF_005
- AREA: Phase 3A PPF Qualifier Phrasing
- GOAL: Refine PHASE3A_Q_PPF_COMPARISON_FOCUS to detect brand/quality vs coverage vs price more naturally
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- STATUS: VALIDATED_LOCAL
- VALIDATION:
  - phrase_library_validator: passed
  - pre-commit: passed
  - regression_phase3a_chain: passed
  - silence_state_pack: passed
- MERGED: Yes
- TAGGED:
  - runtime_phase3a_ceramic_goal_v1
- NOTES:
  - Replaces vague 'quality' wording with 'film brand/quality'
  - Keeps existing decision-matrix logic unchanged
  - Improves real-world PPF comparison detection

---

### CHANGE_ID: CER_001
- AREA: Phase 3A Ceramic Qualifier
- GOAL: Refine PHASE3A_Q_CERAMIC_GOAL wording to emphasize long-term gloss and maintenance instead of cosmetic refresh framing
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE3A_QUALIFICATION_DECISION_MATRIX.md
- STATUS: TAGGED_GREEN
- VALIDATION:
  - phrase_library_validator: passed
  - pre-commit: passed
  - regression_phase3a_chain: passed
  - silence_state_pack: passed
- MERGED: No
- TAGGED: None
- NOTES:
  - Keeps decision matrix values unchanged
  - Aligns ceramic framing with maintenance-backed service model

---
### CHANGE_ID: MATTE_001
- AREA: Matte PPF Audit
- GOAL: Verify matte / stealth / matte-front routing
- FILES:
  - 00__LOCKED__UPLOAD_SET/03__Parameters/SKU_SELECTION_MATRIX.md
  - related matte logic files
- STATUS: AUDITED_ONLY
- VALIDATION: Audit completed
- MERGED: Not applicable
- TAGGED: None
- NOTES:
  - No new patch applied in this sequence

### CHANGE_ID: RVH_001
- AREA: Rare Vehicle Guardrail
- GOAL: Rare vehicle / phrase guardrail stabilization
- FILES:
  - historical merged runtime files
- STATUS: MERGED_MAIN
- VALIDATION: Historical merged state
- MERGED: Yes
- TAGGED: Historical
- NOTES:
  - Pre-existing merged runtime enhancement from earlier branch history

---

### CHANGE_ID: CNV_001
- AREA: Conversion / Visit Path
- GOAL: Audit whether runtime has booking / visit bridge after price and hesitation
- FILES:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/OUTPUT_RESPONSE_TEMPLATE.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
  - 00__LOCKED__UPLOAD_SET/01__Engines/NEGOTIATION_LOGIC_MODULE.md
  - related visit / orchestration files
- STATUS: AUDITED_ONLY
- VALIDATION: Audit completed
- MERGED: Not applicable
- TAGGED: None
- NOTES:
  - Conversion bridge exists
  - Future refinement possible but no structural gap found

---

## RULES FOR UPDATING THIS LEDGER

Before any runtime patch:
- Add or update the relevant change entry
- Mark exact current status only

After local patch:
- Move status to PATCHED_LOCAL

After validator + pre-commit + UAT pass:
- Move status to VALIDATED_LOCAL

After PR opens:
- Move status to PR_OPEN

After merge to main:
- Move status to MERGED_MAIN

After green tag:
- Move status to TAGGED_GREEN or FROZEN

Do not mark anything patched, validated, merged, or tagged unless it has actually happened.


---

## ACTIVE PIPELINE / NEXT STEPS

Use this section to track what is currently active, what is blocked, and what must be handled next.
This section should be updated before moving to a different runtime topic.

### ACTIVE_NOW
- PPF phrase rebalancing remains in progress
- Core objective:
  - keep full-body protection as the main path
  - keep front PPF as last fallback only
  - remove early phrase-layer emphasis on front / partial coverage

### NEXT_UP
1. Confirm exact local status of:
   - PHASE4_PPF_SILENCE_COVERAGE_NARROW
   - PHASE4_PPF_SILENCE_COMPARISON_SIMPLIFY
   - PHASE5_PPF_NARROW_L2
   - PHASE5_PPF_EXIT_FORK_L3

2. Review Phase 5 phrasing against:
   - PHRASE_GOVERNANCE_STANDARD.md
   - front-PPF exposure control
   - affordable full-body emphasis before fallback

3. Patch remaining approved PPF phrases sequentially:
   - one phrase at a time
   - validate after each phrase or tightly grouped phrase set

4. After phrase rebalancing completes:
   - run validator
   - run pre-commit
   - run targeted UAT
   - update ledger statuses
   - commit / push / PR / merge / tag

### BLOCKED_UNTIL_CLARIFIED
- No new PPF phrase patch should proceed if its exact live/local status is unclear
- Do not assume discussed phrases are patched
- Do not move to unrelated runtime topics until the current PPF phrase sequence is either:
  - merged and tagged
  - or explicitly deferred

### FUTURE_AFTER_CURRENT_SEQUENCE
- Optional git log / merged PR audit to backfill older historical changes
- Optional automation/checker for ledger + phrase governance enforcement
- Later refinement:
  - payment incentive sequencing
  - Phase 5 negotiation phrasing
  - conversion / visit refinement if needed
  - Phase 7 snippet trigger mapping inside existing enforced files / ledger notes (no separate governance file unless later required)

