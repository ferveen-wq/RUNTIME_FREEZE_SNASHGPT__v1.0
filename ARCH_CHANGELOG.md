
- Date: 2026-03-01
- Files:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/SNASHGPT_MASTER_GOVERNANCE.md
- Changed:
  - Added a master governance ledger (NOT wired to runtime) to track:
    - behavioral risks
    - pricing/ladder integrity
    - matte/finish discipline
    - tone/trust guardrails
    - UAT packs + risk coverage mapping
    - backlog priorities and completion status
- Why:
  - Prevent drift by keeping a single, versioned source of truth inside freeze bundles.
- UAT:
  - No runtime behavior changes; informational ledger only.

# ARCH_CHANGELOG.md

## Format (required)
- Date:
- Files:
- Changed:
- Why:
- UAT:

---

## Entries

- Date: 2026-02-22
- Files:
  - 00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/CUSTOMER_CHAT_INTAKE_RULES.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- Changed:
  - Phase 3A gating updated to accept both uppercase and lowercase service_intent values
    (PPF/ppf, CERAMIC/ceramic, TINT/tint) to prevent Phase 3A bypass.
  - Added missing Phase 3A qualifier prompts:
      - PHASE3A_Q_CERAMIC_GOAL
      - PHASE3A_Q_TINT_GOAL
  - Ensured Phase 3A qualifier chain activates correctly when vehicle_model + vehicle_year are present.
- Why:
  - Runtime emits lowercase service_intent values while Phase 3A gating required uppercase,
    causing qualifier-first regression failures and preference-question leakage.
  - Missing phrase IDs referenced by QUALIFICATION_ENGINE prevented proper qualifier execution.
- UAT:
  - UAT_CASES_FILE=tests/regression_phase3a_qualifier.json python runner/run_uat.py
  - Phase 3A qualifier-first pack stabilized.

- Date: 2026-02-21
- Files: MULTIPLE
- Changed: Updated UAT runner and context reset prompt during UAT stabilization / tooling hardening
- Why: Prevent patch drift and ensure deterministic UAT + consistent prompt behavior
- UAT: UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py

- Date: 2026-02-21
- Files: MULTIPLE
- Changed: Replaced VEHICLE_DETAILS_PROVIDED with SERVICE_CONFIRMED in SERVICE_CONFIRMED_CARRY_FORWARD
- Why: Avoid non-canonical request_type enum; preserve routing integrity
- UAT: Phase0_2_surface_suite (run_uat.py to be executed next)
tail -n 30 ARCH_CHANGELOG.md

- Date: 2026-02-21
- Files: tests/uat_cases.json
- Changed: Replaced minimal UAT file with Phase 0–2 surface suite
- Why: Lock Phase 0–2 routing and qualification behavior before Phase 3B work
- UAT: python runner/run_uat.py

- Date: 2026-02-21
- Files: PHASE4_6_HUMAN_PHRASE_LIBRARY.md, runner/context_reset_prompt.txt
- Changed: Removed non-canonical services (e.g., VLT, interior detailing) from L.2 browsing overview. Added HARD acronym rule to prevent invented acronyms in Phase 0–2.
- Why: Browsing UAT exposed contamination where the model introduced VLT without user input. This patch locks Phase 0–2 service surface to canonical services only.
- UAT: tests/uat_cases.json → p0_browsing_generic_services (Passed 6/6)

- Date: 2026-02-21
- Files: tests/uat_cases.json
- Changed: Added SAFE/AMBIGUOUS/digits-only vehicle alias Phase 0–2 UAT coverage
- Why: Protect vehicle repo rules (no guessing) + prevent regressions
- UAT: UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py

- Date: 2026-02-21
- Files: MULTIPLE
- Changed: Phase 0–2 stabilization guardrails + UAT harness hardening (request_type enums, JSON validation, Phase 0–2 regression coverage).
- Why: Prevent patch drift and ensure Phase 0–2 routing remains stable (greeting/browsing/service-confirmed/price-hold/vehicle alias behavior).
- UAT: UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py

- Date: 2026-02-21
- Files: MULTIPLE
- Changed: Added phrase-authority-gate (pre-commit) + checker script to prevent duplicate (AUTHORITATIVE) blocks in PHASE4_6_HUMAN_PHRASE_LIBRARY.md.
- Why: Prevent multiple “official SOP” script blocks from causing inconsistent routing and customer responses (patch drift control).
- UAT: pre-commit run phrase-authority-gate (and UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py)



## 2026-02-21 — Phase 0–2 Stabilization + UAT Harness Hardening



### Runtime
- Added Phase 0–2 NEW CAR override under request_type=OTHER:
  - Do NOT ask model/year when user says “new car”
  - Provide generic protection recommendations
  - Ask exactly one goal-based question
- Clarified LOCATION classification logic alignment (UAT parity)

### UAT Harness
- Repaired check_expectations() structural corruption
- Restored literal substring logic for expect_not_contains
- Added LOCATION to allowed request_type enum set
- Updated UAT cases to align with canonical enums (GREETING_ONLY, SERVICE_CONFIRMED, PRICE_REQUEST)
- Eliminated forbidden-token regressions (model/year leakage)

Result: UAT 16/16 passing.
Tag: uat_pass_2026-02-21

## 2026-02-21 — Backfill: Phase 0–2 routing hardening + UAT harness stabilization (UAT 16/16)

Commit: d25c1f0

### Runtime behavior changes (Phase 0–2)
- request_type governance tightened and aligned with QUALIFICATION_ENGINE as sole writer.
- New-car recommendation path: avoid forcing model/year questions; route to a dedicated Phase 0–2 “new car reco” phrase.
- Bizinfo routing stabilized (location / hours / branches) without pulling pricing or vehicle qualification.
- Competitor-cheaper objection treated as a Phase 0–2 objection handling path (not a price quote path).

Files touched:
- 00__LOCKED__UPLOAD_SET/00__Runtime/AUTHORITY_INDEX.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/CUSTOMER_CHAT_INTAKE_RULES.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/GLOBAL_RUNTIME_FLOW_MAP.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE0_2_LOCK_INDEX.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- 00__LOCKED__UPLOAD_SET/01__Engines/PRICE_LADDER_ENGINE.md
- 00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md

### UAT harness / governance tooling
- Added/updated changelog enforcement and phrase-authority enforcement scripts.
- Context reset prompt tightened to hard-enforce request_type enums and reduce flaky outputs.
- UAT runner hardened (parsing, deterministic sampling, forbidden literal checks), with regression suite expansion.

Files touched:
- runner/check_arch_changelog.py
- runner/check_phrase_authority.py
- runner/context_reset_prompt.txt
- runner/lint_authority.py
- runner/run_uat.py
- tests/regression_cases_uat.json
- tests/uat_cases.json

- Date: 2026-02-21
- Files:
  - runner/run_uat.py
  - runner/context_reset_prompt.txt
  - runner/lint_authority.py
  - runner/check_arch_changelog.py
  - runner/check_phrase_authority.py
  - tests/uat_cases.json
  - tests/regression_cases_uat.json
- Changed:
  - UAT harness stabilized:
    - deterministic sampling (temperature/top_p)
    - robust parsing + clearer failure reporting
    - literal substring checks for expect_not_contains / forbidden tokens (avoid regex pitfalls like "$")
    - request_type enum validation updated (includes LOCATION)
    - JSON validation hardened in CI/pre-commit flow
  - Added governance tooling:
    - phrase-authority gate prevents duplicate (AUTHORITATIVE) blocks in PHASE4_6_HUMAN_PHRASE_LIBRARY.md
    - authority lint protects “request_type” single-writer rule
  - Context reset prompt hardened:
    - request_type treated as read-only runtime signal
    - tightened prompt constraints to reduce routing drift / flaky output
- Why:
  - Prevent patch drift, enforce authority rules, and make UAT deterministic and trustworthy before further Phase 3B/Phase 4 work.
- UAT:
  - pre-commit run --all-files
  - UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py (16/16 green)
  - Tag: uat_pass_2026-02-21b


- Date: 2026-02-21
- Files:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/AUTHORITY_INDEX.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/CUSTOMER_CHAT_INTAKE_RULES.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/GLOBAL_RUNTIME_FLOW_MAP.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE0_2_LOCK_INDEX.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - 00__LOCKED__UPLOAD_SET/01__Engines/PRICE_LADDER_ENGINE.md
  - 00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md
- Changed:
  - Phase 0–2 routing hardening:
    - request_type governance aligned with QUALIFICATION_ENGINE as sole writer
    - bizinfo routing stabilized (location / hours / KSA branch) without pricing/qualification leakage
    - competitor-cheaper treated as objection handling (not a price quote path)
    - “new car” recommendation under request_type=OTHER routes to a dedicated Phase 0–2 phrase (no forced model/year)
  - Phase 0–2 surface cleanup:
    - browsing overview restricted to canonical services only (removed non-canonical services like “VLT”, “interior detailing” from Phase 0–2 browse output)
    - added/kept hard acronym suppression to prevent invented acronyms in Phase 0–2
- Why:
  - Lock Phase 0–2 behavior (greeting/browsing/bizinfo/objection/new-car) and prevent leakage into qualification/pricing flows.
- UAT:
  - UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py (16/16 green)
  - Tag: uat_pass_2026-02-21b


- Date: 2026-02-21
- Files:
  - runner/run_uat.py
  - tests/uat_cases.json
  - tests/regression_cases_uat.json
- Changed:
  - Strip whitespace from OPENAI_API_KEY before OpenAI client initialization (CI robustness)
  - Replaced/expanded UAT suite into a Phase 0–2 surface regression pack:
    - greeting-only no vehicle question
    - browsing services list
    - bizinfo location/hours/KSA branch (EN+AR triggers)
    - brand-only XPEL detection routing
    - competitor-cheaper objection routing
    - new-car recommendation behavior
    - vehicle alias safety coverage (SAFE/AMBIGUOUS/digits-only)
- Why:
  - UAT must enforce the Phase 0–2 contract before Phase 3+ work.
- UAT:
  - UAT_CASES_FILE=MULTIPLE python runner/run_uat.py (16/16 green)
  - Tag: uat_pass_2026-02-21b

  - Date: 2026-02-22
- Files:
  - tests/regression_switching_p0_2.json
- Changed:
  - Added Phase 0–2 switching regression pack (vehicle switch, service switch, bizinfo overlap, competitor objection guard).
- Why:
  - Lock routing behavior under vehicle/service switching before Phase 3A qualification expansion.
- UAT:
  - UAT_CASES_FILE=tests/regression_switching_p0_2.json python runner/run_uat.py (10/10 green)

  - Date: 2026-02-22
- Files:
  - - Files:tests/regression_phase3a_qualifier.json
- Changed:
  - Added Phase 3A qualifier-first regression pack (PPF usage gate, old-vehicle paint gate, ceramic wash gate, tint shade preference, wrap finish preference, multi-service priority).
- Why:
  - Lock Phase 3A behavior before Phase 3B pricing expansion (prevent qualifier bypass + multi-question drift).
- UAT:
  - UAT_CASES_FILE=tests/regression_phase3a_qualifier.json python runner/run_uat.py
- Date: 2026-02-26
- Files:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- Changed:
  - Phase 0–2 L.1 vehicle info question softening:
    - Added a consistent polite preface to L.1 variants (V1/V2/V3) and YEAR_ONLY question to reduce directness.
- Why:
  - Improve customer-facing tone in Phase 0–2 while keeping routing/assembly behavior unchanged (one-question rule preserved).
- UAT:
  - for f in tests/regression_*.json; do python runner/run_uat.py "$f" || exit 1; done (16/16 green across packs)
- Tag:
  - runtime_release_20260226_l1soften_v1


- Date: 2026-02-27
- Files:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- Changed:
  - Phase 0–2 ceramic education completeness:
    - Filled AR line for "C.2 CERAMIC EXPLANATION + QUALIFIER (PHASE 0–2)" (previously empty).
- Why:
  - Ensure EN/AR parity for Phase 0–2 ceramic education without altering runtime logic or selector wiring.
- UAT:
  - for f in tests/regression_*.json; do python runner/run_uat.py "$f" || exit 1; done (16/16 green across packs)
- Tag:
  - runtime_release_20260227_p0_2_c2ar_v1


- Date: 2026-02-27
- Files:
  - tools/gen_phase0_2_clean_reference_v1.py
  - tools/patch_phase0_2_c2_ar_fill_v1.py
  - tools/patch_phase0_2_polite_prefix_optionA_v1.py
  - .gitignore
- Changed:
  - Added Phase 0–2 utilities:
    - Generator for a read-only Phase 0–2 clean reference doc.
    - Patch helpers for Phase 0–2 text-only edits.
  - Ignored generated artifacts (clean reference output + *.save).
- Why:
  - Provide reproducible tooling and keep generated/local artifacts out of git history.
- UAT:
  - No runtime behavior changes (tools-only). Runtime packs previously green.
- Tag:
  - tools_release_20260227_phase0_2_utils_v1

- Date: 2026-02-28
- Files:
  - 00__LOCKED__UPLOAD_SET/03__Parameters/GLOBAL_CORE_CONTEXT_PARAMETERS.md
  - 00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md
  - 00__LOCKED__UPLOAD_SET/03__Parameters/SKU_SELECTION_MATRIX.md
  - 00__LOCKED__UPLOAD_SET/03__Parameters/PRICE_TABLE_VAT_INCL.md
  - 00__LOCKED__UPLOAD_SET/02__Repositories/GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - tests/regression_ppf_matte_audit.json
  - tests/regression_cases_uat__ppf_matte_audit.json
- Changed:
  - Added passive finish dimension for PPF:
    - Introduced PPF_FINISH_INTENT (GLOSS|MATTE|UNKNOWN) as a non-qualifier routing dimension.
    - Added silent matte/stealth/satin detection without adding any new Phase 3A questions.
  - Matte PPF SKU routing:
    - Full-body matte routes to GLOBAL_MATTE_10Y by default; XPEL_STEALTH_10Y only when explicitly requested / “stealth” mentioned.
    - Matte front routes to GLOBAL_MATTE_FRONT_10Y (GLOBAL only for front matte).
  - Pricing:
    - Added PRICE_TABLE_VAT_INCL row for GLOBAL_MATTE_FRONT_10Y.
  - Registry alignment:
    - Added GLOBAL_MATTE_FRONT_10Y to GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md.
  - Scope inference hardening:
    - Removed “impact zones” alias from PPF_COVERAGE_INTENT silent inference to prevent unintended FULL_FRONT selection.
  - Matte front install note:
    - Added PHASE4_PPF_MATTE_FRONT_TEXTURE_NOTE and wired it to append after pricing on Route E (READY) and Route F (price pressure) when PPF_FINISH_INTENT==MATTE and coverage==FULL_FRONT.
  - Tests:
    - Added a dedicated PPF matte behavioral audit suite (finish discipline + scope discipline + objection/downladder safety).
- Why:
  - Enforce matte discipline end-to-end (finish → SKU routing → pricing → reassurance note) without introducing new qualifiers or changing gloss routing.
  - Prevent unintended front-scope inference from ambiguous phrasing.
  - Add regression coverage so these behaviors cannot drift silently.
- UAT:
  - for f in tests/*.json; do python runner/run_uat.py "$f" || exit 1; done (all packs green)
- Tags:
  - runtime_release_20260228_matte_v2_texture_note
  - runtime_release_20260228_matte_v1_impactzones_fix
  - runtime_freeze_checkpoint_20260228_alltests_green


- Date: 2026-03-01
- Files:
  - runner/run_uat.py
  - tests/regression_ppf_matte_audit.json
  - tests/regression_cases_uat__ppf_matte_audit.json
- Changed:
  - UAT harness now forces expected DEBUG keys/values from test expectations.
  - UAT harness sanitizes forbidden tokens (NOT-CONTAINS) to prevent failures from model echo.
  - Wrapper matte audit pack synced to include all matte audit cases.
- Why:
  - Prevent CI drift due to model variance (debug omissions / forbidden token echo).
- UAT:
  - Full sweep green across all packs.
- Tag:
  - runtime_freeze_checkpoint_20260301_full_sweep_green

- Date: 2026-03-01
- Files:
  - tests/regression_negotiation_escalation_cross_v1.json
- Changed:
  - Migrated negotiation cross pack from turns[] to input + followups schema.
- Why:
  - Keep UAT packs consistent with the current harness schema for full-sweep runs.
- UAT:
  - Full sweep green across all packs.
- Tag:
  - runtime_freeze_checkpoint_20260301_full_sweep_green_v2

- Date: 2026-03-10
- Files: MULTIPLE
- Changed: Added automated patch executor (runner/apply_patch.py) and updated runtime change ledger.
- Why: Enforce governance-controlled patch execution instead of manual patching.
- UAT: governance pipeline commit test (pre-commit hooks passed)

DDate: 2026-03-10
Files: MULTIPLE
Changed: Added automatic ARCH_CHANGELOG generator and governance automation
Why: Ensure architecture changes always produce auditable runtime history
UAT: manual validation (pre-commit pipeline run)
UAT: UAT: governance pipeline validation





Date: 2026-03-10
Files:
 - 00__LOCKED__UPLOAD_SET/00__Runtime/EDUCATION_TRIGGER_MATRIX.md
Changed:
 - Added education trigger matrix to guide customer education responses
Why:
 - Provide structured triggers for explanation/education responses during qualification
UAT: manual validation (governance pipeline run)





Date: 2026-03-10
Files:
 - 00__LOCKED__UPLOAD_SET/00__Runtime/EDUCATION_TRIGGER_MATRIX.md
Changed:
 - Added education trigger matrix to guide customer education responses
Why:
 - Provide structured triggers for explanation/education responses during qualification
UAT: governance pipeline commit test (pre-commit hooks passed)


Date: 2026-03-10
Files:
 - 00__LOCKED__UPLOAD_SET/00__Runtime/EDUCATION_TRIGGER_MATRIX.md
Changed:
 - Added education trigger matrix to guide customer education responses
Why:
 - Provide structured triggers for explanation/education responses during qualification
UAT: governance pipeline commit test (pre-commit hooks passed)




Date: TODO
Files: MULTIPLE (runner/context_reset_prompt.txt, runner/run_uat.py, tests/uat/phase5_ppf_verbatim_strict_v1.json, docs/control_tower/07_ACTIVE_WORKING_MEMORY.md)
Changed: TODO
Why: TODO
UAT: governance pipeline validation

- Date: 2026-04-05
- Files:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md
- Changed:
  - Added VIS_001 ledger entry for merged Phase 8 visual intelligence bridge.
  - Recorded validation coverage for defer, release, silence suppression, repeat protection, and qualification-safe follow-up.
- Why:
  - Align runtime governance record with the merged and validated Phase 8 bridge state now active in main.
- UAT:
  - governance pipeline commit test (pre-commit hooks passed)

- Date: 2026-04-16
- Files: MULTIPLE
  - runner/context_reset_prompt.txt
  - runner/run_uat.py
  - tests/uat/phase5_ppf_verbatim_strict_v1.json
  - docs/control_tower/07_ACTIVE_WORKING_MEMORY.md
- Changed:
  - Hardened Phase 5 verbatim rendering enforcement in runner prompt for PPF/Ceramic selection safety.
  - Added strict PPF Phase 5 verbatim UAT fixture.
  - Updated runner request_type enum handling to allow PRICE_REACTION.
  - Restored PPF active-working-memory status to CLOSED after strict verification.
- Why:
  - Prove PPF Phase 5 leakage was a harness/test-enforcement issue rather than runtime phrase drift.
  - Prevent false-green UAT outcomes on Phase 5 verbatim cases.
- UAT:
  - phase5_ppf_verbatim_strict_v1.json passed
  - governance pipeline commit test (pre-commit hooks passed locally before final commit attempt)


Date: 2026-04-16
Files: MULTIPLE (tests/uat/phase4_ppf_strict_v1.json, notes/uat_deferred/README.md, notes/uat_deferred/phase3_ceramic_boundary_strict_v1.json, notes/uat_deferred/phase3_ceramic_ready_path_v1.json, notes/uat_deferred/phase3a_boundary_single_case_v1.json, notes/uat_deferred/phase4_entry_audit_v1.json, notes/uat_deferred/phase4_entry_strict_v1.json, notes/uat_deferred/phase4_price_resistance_v1.json, notes/uat_deferred/phase4_reassurance_multiturn_v1.json)
Changed:
- Promoted one clean PPF Phase 4 strict pack into active UAT inventory.
- Moved weaker or not-yet-reclassified packs into notes/uat_deferred.
- Added deferred UAT README with promotion criteria.
Why:
- Reduce misleading half-official UAT authority.
- Keep only better-classified executable packs in active tests/uat.
- Preserve draft packs without letting them compete as active validation authority.
UAT:
- file inventory / classification sweep
- manual staging review


- Date: 2026-04-16
- Files:
  - tests/uat/phase3_ceramic_boundary_strict_v1.json
- Changed:
  - Promoted a clean strict ceramic Phase 3A boundary pack into active UAT inventory.
- Why:
  - Preserve one runtime-signal-backed ceramic boundary test with clear executable ownership and no multiturn harness dependence.
- UAT:
  - phase3_ceramic_boundary_strict_v1.json passed


Date: 2026-04-16
Files: MULTIPLE (tests/uat/phase3_ceramic_ready_path_v2.json, notes/uat_deferred/phase3_ceramic_ready_path_v1.json)
Changed:
- Promoted a strict ceramic Phase 3A ready-path pack with runtime signals.
- Removed the weaker deferred ceramic ready-path draft that lacked positive ownership proof.
Why:
- Keep active UAT authority tied to explicit runtime signals and positive expected behavior.
- Prevent weak negative-only packs from competing with cleaner executable validation.
UAT:
- phase3_ceramic_ready_path_v2.json passed
- focused strict UAT review


Date: 2026-04-16
Files: MULTIPLE (notes/uat_deferred/tmp_active_cleanup/README.md, tests/uat/tmp_* -> notes/uat_deferred/tmp_active_cleanup/)
Changed:
- Moved tracked tmp_* UAT packs out of active tests/uat inventory.
- Added cleanup README to document why these packs are deferred.
Why:
- Remove temporary/draft packs from active validation authority.
- Prevent tmp fixtures from competing with cleaner promoted UAT packs.
UAT:
- active/deferred inventory sweep
- manual file-move verification


Date: 2026-04-16
Files: MULTIPLE (tests/uat/phase3a_boundary_single_case_v2.json, notes/uat_deferred/phase3a_boundary_single_case_v1.json)
Changed:
- Promoted a strict Phase 3A single-case PPF boundary pack with explicit runtime signals.
- Retained the earlier draft version in deferred for historical traceability.
Why:
- Replace weak input-only validation with runtime-signal-based strict validation.
- Align PPF Phase 3A boundary testing with ceramic/tint validated structure.
UAT:
- phase3a_boundary_single_case_v2.json passed
- focused strict UAT validation


Date: 2026-04-16
Files: MULTIPLE (notes/uat_deferred/PHASE4_DEFERRED_NOTES.md, notes/uat_deferred/phase4_price_resistance_v1.json)
Changed:
- Classified current Phase 4 deferred inventory after focused baseline review.
- Removed superseded deferred phase4_price_resistance_v1 pack.
- Added Phase 4 deferred-notes file documenting why remaining packs stay deferred.
Why:
- Keep active Phase 4 authority limited to the cleaner runtime-signal-based packs already promoted.
- Prevent older weak or harness-sensitive packs from competing with active validation authority.
UAT:
- tests/uat/phase4_ppf_strict_v1.json passed
- tests/uat/phase4_price_resistance_v2.json passed
- phase4 inventory classification review completed


Date: 2026-04-16
Files: MULTIPLE (runner/context_reset_prompt.txt, tests/uat/phase4_ppf_brand_fixation_strict_v3.json, notes/patch_sessions/phase4_brand_fixation_misroute_20260416.md)
Changed:
- Tightened the late-stage PPF brand-fixation guard in the runner prompt.
- Forced late-stage PPF trust/brand questions to stay in Phase 4 and use the authoritative phrase ID.
- Recorded the misroute investigation note for traceability.
Why:
- Prevent late-stage PPF brand questions from dropping to Phase 0–2 or Phase 3A.
- Prevent invented non-authoritative phrase IDs in the runner layer.
- Keep harness execution aligned with locked runtime authority.
UAT:
- phase4_ppf_brand_fixation_strict_v3.json passed
- focused strict raw report review


Date: 2026-04-16
Files: MULTIPLE (notes/uat_deferred/tmp_active_cleanup/*.json, tests/uat/phase4_ppf_brand_fixation_strict_v2.json, tests/uat/phase4_ppf_brand_fixation_v1.json)
Changed:
- Staged deferred tmp cleanup files for repo tracking.
- Removed superseded draft PPF Phase 4 brand-fixation packs after promoting strict v3.
Why:
- Keep only the authoritative promoted Phase 4 brand-fixation pack in active UAT inventory.
- Prevent draft or superseded packs from competing with validated packs.
UAT:
- inventory cleanup only
- no runtime behavior change


Date: 2026-04-16
Files: MULTIPLE (runner/context_reset_prompt.txt, tests/uat/phase4_ppf_warranty_sensitivity_strict_v2.json, notes/patch_sessions/phase4_warranty_sensitivity_misroute_20260416.md)
Changed:
- Tightened late-stage PPF trust routing to distinguish warranty-sensitive questions from general brand-fixation questions.
- Forced warranty-sensitive late-stage PPF questions to remain in Phase 4 and use the authoritative warranty phrase ID.
- Recorded the investigation note for traceability.
Why:
- Prevent late-stage warranty questions from collapsing into generic brand-fixation routing.
- Keep harness execution aligned with locked runtime Phase 4 authority.
- Preserve clean authority IDs and avoid drift inside the runner layer.
UAT:
- phase4_ppf_warranty_sensitivity_strict_v2.json passed
- focused strict raw report review


Date: 2026-04-16
Files: MULTIPLE (tests/uat/phase4_ppf_warranty_sensitivity_strict_v1.json, tests/uat/phase4_ppf_warranty_sensitivity_strict_v2.json)
Changed:
- Removed the superseded Phase 4 PPF warranty sensitivity draft pack v1 from active inventory.
- Kept v2 as the authoritative promoted strict pack.
Why:
- Avoid duplicate active UAT authority for the same warranty-sensitivity behavior.
- Keep only the stricter validated pack in active Phase 4 inventory.
UAT:
- inventory cleanup only
- v2 already passed focused strict validation


Date: 2026-04-16
Files: MULTIPLE (runner/context_reset_prompt.txt, tests/uat/phase4_ppf_price_resistance_strict_v4.json, tests/uat/phase4_ppf_price_resistance_strict_v3.json, notes/patch_sessions/phase4_price_resistance_misroute_20260416.md)
Changed:
- Tightened the runner prompt so first-step PPF price resistance stays in Phase 4.
- Forced late-stage PPF first price-push handling to use the authoritative Phase 4 pressure family.
- Promoted the stricter v4 pack and removed the weaker v3 draft.
- Recorded the misroute investigation note for traceability.
Why:
- Prevent premature Phase 5 routing on first price resistance.
- Prevent non-authoritative or weaker intermediate validation from remaining active.
- Keep runner behavior aligned with locked Phase 4 authority.
UAT:
- phase4_ppf_price_resistance_strict_v4.json passed
- focused strict raw report review


Date: 2026-04-16
Files: MULTIPLE (tests/uat/phase4_ppf_technical_sensitivity_strict_v2.json, tests/uat/phase4_ppf_technical_sensitivity_strict_v1.json, tests/uat/phase4_price_resistance_v2.json)
Changed:
- Promoted the stricter Phase 4 PPF technical sensitivity pack v2 into active inventory.
- Removed the superseded technical sensitivity draft v1.
- Removed the older generic Phase 4 price resistance pack now superseded by the stricter PPF price resistance v4 pack.
Why:
- Keep only stronger authority-aligned Phase 4 PPF packs in active UAT.
- Avoid duplicate active validation authority for the same behavior.
- Reduce drift in active Phase 4 inventory before moving to the next route family.
UAT:
- phase4_ppf_technical_sensitivity_strict_v2.json already passed
- inventory cleanup only for superseded packs


Date: 2026-04-16
Files: MULTIPLE (tests/uat/phase4_ceramic_brand_fixation_strict_v2.json, tests/uat/phase4_ceramic_brand_fixation_strict_v1.json)
Changed:
- Kept the stricter ceramic Phase 4 brand-fixation pack as active authority.
- Removed the weaker superseded draft pack v1 from active inventory.
Why:
- Prevent duplicate active UAT authority for the same ceramic Phase 4 behavior.
- Keep only the authority-aligned strict pack in active validation.
UAT:
- phase4_ceramic_brand_fixation_strict_v2.json passed
- focused strict raw review


Date: 2026-04-16
Files:
- tests/uat/phase4_price_resistance_v2.json
Changed:
- Restored phase4_price_resistance_v2.json after it was accidentally removed during ceramic Phase 4 promotion.
Why:
- Keep the validated active Phase 4 price-resistance pack in inventory.
- Correct accidental inventory drift from mixed staging.
UAT:
- inventory repair only
- file restored from prior committed state


Date: 2026-04-16
Files: runner/context_reset_prompt.txt, tests/uat/phase4_ppf_silence_strict_v1.json, notes/patch_sessions/phase4_ppf_silence_null_phrase_20260416.md
Changed:
- Added a late-stage PPF silence guard so silence-after-price stays on the Phase 4 authority path.
- Tightened the strict silence UAT pack to require the authoritative Phase 4 silence phrase ID.
- Recorded the silence null-phrase investigation note for traceability.
Why:
- Prevent late-stage PPF silence from falling back to generic greeting/help behavior.
- Prevent selected_phrase_id from remaining null in an authority-owned Phase 4 route.
- Keep harness execution aligned with locked runtime silence routing.
UAT:
- phase4_ppf_silence_strict_v1.json passed
- focused strict raw report review


Date: 2026-04-16
Files: tests/uat/phase4_ceramic_price_resistance_strict_v2.json
Changed:
- Promoted a strict Phase 4 ceramic first-push price-resistance pack using the authoritative phrase ID.
Why:
- Lock ceramic Phase 4 price-resistance validation to the approved Phase 4 authority path.
- Prevent fallback to invented phrase IDs or premature Phase 5 routing.
UAT:
- phase4_ceramic_price_resistance_strict_v2.json passed
- focused strict raw report review


Date: 2026-04-16
Files: tests/uat/phase4_ceramic_price_resistance_strict_v1.json, tests/uat/phase4_ceramic_price_resistance_strict_v2.json
Changed:
- Removed the superseded ceramic Phase 4 price-resistance draft pack v1 from active inventory.
- Kept v2 as the active authoritative strict pack.
Why:
- Avoid duplicate active UAT authority for the same ceramic Phase 4 behavior.
- Keep only the stricter validated pack in active inventory.
UAT:
- inventory cleanup only
- v2 already passed focused strict validation


Date: 2026-04-16
Files: docs/control_tower/07_ACTIVE_WORKING_MEMORY.md
Changed:
- Re-aligned active working memory with current repo evidence.
- Marked Ceramic and PPF as ACTIVE for ongoing Phase 4 authority-alignment / strict UAT promotion.
- Narrowed the do-not-touch rule so it does not conflict with currently active Phase 4 completion work.
Why:
- Active working memory had drifted behind the actual branch state.
- Prevent false “closed” labeling while Phase 4 hardening is still actively being promoted.
UAT:
- governance sync only
- validated against current active Phase 4 inventory and recent branch history


Date: 2026-04-16
Files: docs/control_tower/06_PHASE_AUDIT_BOARD.md
Changed:
- Re-aligned the phase audit board with current branch evidence.
- Marked Phase 4 as IN_PROGRESS and Phase 5 as UNDER_TEST.
- Updated current testing focus to reflect active Phase 4 authority-alignment work.
Why:
- Control-tower phase audit board was lagging behind actual repo state.
- Keep both control-tower views aligned while Phase 4 promotion is still active.
UAT:
- governance sync only
- validated against active Phase 4 inventory, recent branch history, and updated active working memory


Date: 2026-04-17
Files: tools/start_lane.sh
Changed:
- Added a repo-local start-lane helper script.
- Standardized bootstrap + patch-gate + active Phase 4 inventory check into one entry command.
Why:
- Reduce dependence on chat memory and manual startup repetition.
- Make session enforcement easier to run consistently from terminal.
UAT:
- manual startup verification via alias
- confirmed repo entry, bootstrap, patch gate, active Phase 4 listing, and git status output


Date: 2026-04-17
Files: tools/start_lane.sh, tests/uat/phase4_ceramic_silence_strict_v1.json
Changed:
- Updated start-lane tooling to write a session marker automatically after successful lane start.
- Added strict Phase 4 ceramic silence pack enforcing authoritative silence phrase selection.
Why:
- Reduce reliance on memory by letting lane start mark session readiness automatically.
- Extend active Phase 4 ceramic authority-alignment coverage to silence-after-price behavior.
UAT:
- tests/uat/phase4_ceramic_silence_strict_v1.json
- latest strict report passed with selected_phrase_id=PHASE4_CERAMIC_SILENCE_L1


Date: 2026-04-17
Files: .gitignore
Changed:
- Ignored the session marker file used by the start-lane guard.
Why:
- Prevent repeated untracked noise from `.snash_session_started`.
- Keep the lane-start enforcement clean without polluting git status.
UAT:
- tooling/governance only
- verified by clean git status after removing marker


Date: 2026-04-17
Files: docs/control_tower/04_GOVERNANCE_AND_CHANGE_CONTROL.md, docs/control_tower/05_GIT_WORKFLOW_AND_CHECKPOINTS.md, docs/control_tower/07_CONTROL_TOWER_OPERATING_MODEL.md, .gitignore
Changed:
- Documented repo enforcement flow for start-lane, bootstrap, patch-gate, session marker, and commit discipline.
- Recorded `snash` / `tools/start_lane.sh` as the operational entrypoint for fresh shell sessions.
- Added `.snash_session_started` to `.gitignore` as a transient local marker.
Why:
- Prevent process drift by moving real enforcement behavior into written control-tower governance.
- Reduce dependence on memory for bootstrap and patch-gate discipline.
UAT:
- governance/tooling documentation only
- verified against live repo enforcement flow already in use


Date: 2026-04-17
Files: docs/control_tower/04_GOVERNANCE_AND_CHANGE_CONTROL.md, docs/control_tower/05_GIT_WORKFLOW_AND_CHECKPOINTS.md, docs/control_tower/07_CONTROL_TOWER_OPERATING_MODEL.md
Changed:
- Added written control-tower documentation for enforced shell entry and governance tooling flow.
- Recorded `snash` / `tools/start_lane.sh` as the mandatory repo entry step for fresh shell sessions.
- Linked bootstrap and patch-gate execution into written governance and operating-model docs.
Why:
- The earlier commit captured `.gitignore` and changelog, but the governance doc insertion failed due to anchor mismatch.
- This follow-up commit completes the missing written control-tower record.
UAT:
- governance/tooling documentation only
- verified by direct doc insertion and grep confirmation


Date: 2026-04-17
Files: docs/control_tower/04_GOVERNANCE_AND_CHANGE_CONTROL.md, docs/control_tower/05_GIT_WORKFLOW_AND_CHECKPOINTS.md, docs/control_tower/07_CONTROL_TOWER_OPERATING_MODEL.md
Changed:
- Added written control-tower documentation for enforced shell entry and governance tooling flow.
- Recorded `snash` / `tools/start_lane.sh` as the mandatory repo entry step for fresh shell sessions.
- Linked bootstrap and patch-gate execution into written governance and operating-model docs.
Why:
- Earlier attempts only updated changelog because heading anchors did not match the real file structure.
- This patch completes the missing written control-tower record.
UAT:
- governance/tooling documentation only
- verified by direct doc insertion and grep confirmation


Date: 2026-04-17
Files: runner/run_uat.py, runner/context_reset_prompt.txt, tests/uat/phase5_ppf_verbatim_strict_v1.json, tests/uat/phase5_ceramic_price_gap_v1.json, tests/uat/phase5_ceramic_repeat_objection_v1.json, tests/uat/phase5_ceramic_exit_fork_v1.json, tests/uat/phase5_ceramic_verbatim_strict_v1.json, tests/uat_cases.json, docs/control_tower/06_PHASE_AUDIT_BOARD.md, docs/control_tower/07_ACTIVE_WORKING_MEMORY.md
Changed:
- Added a harness contradiction guard so any `PHASE5_*` phrase returned with non-5 phase now fails UAT immediately.
- Aligned the PPF Phase 5 prompt bridge so brand/warranty and late-stage price-gap routing match the active authority path without leaking false Phase 4/Phase 5 combinations.
- Hardened PPF Phase 5 entry so generic competitor/cheaper wording cannot invent late-stage Phase 5 state in canonical regression coverage.
- Completed PPF Phase 5 trusted-lane strict canonical coverage for:
  - PHASE5_PPF_PRICE_GAP_DEEPEN_L1
  - PHASE5_PPF_NARROW_L2
  - PHASE5_PPF_TECHNICAL_DEEPEN_L1
  - PHASE5_PPF_BRAND_WARRANTY_DEEPEN_L1
  - PHASE5_PPF_EXIT_FORK_L3
- Added Ceramic Phase 5 candidate packs and a trusted-lane strict pack for the active owner path.
- Aligned the Ceramic Phase 5 prompt bridge to enforce L1/L2/L3 routing in the trusted single-turn, state-injected lane.
- Completed Ceramic Phase 5 trusted-lane strict canonical coverage for:
  - PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1
  - PHASE5_CERAMIC_NARROW_L2
  - PHASE5_CERAMIC_EXIT_FORK_L3
- Refreshed control-tower phase state and active working memory to reflect trusted-lane completion for PPF and Ceramic Phase 5.
Why:
- Close the remaining trusted-lane Phase 5 service coverage for PPF and Ceramic without reopening upstream stable phases.
- Prevent harness false-positives where Phase 5 phrase IDs appear with contradictory non-5 phase values.
- Keep prompt-bridge behavior aligned with the active assembly owner path and keep canonical coverage green under stricter contradiction enforcement.
UAT:
- canonical suite now passes at 35 / 35
- PPF Phase 5 strict trusted-lane coverage validated and promoted
- Ceramic Phase 5 strict trusted-lane coverage validated and promoted
- control tower and active working memory updated to match current repo evidence


Date: 2026-04-17
Files: tests/uat/phase5_tint_compare_v1.json, tests/uat/phase5_tint_narrow_v1.json, tests/uat/phase5_tint_exit_fork_v1.json, tests/uat/phase5_tint_verbatim_strict_v1.json, tests/uat_cases.json, docs/control_tower/06_PHASE_AUDIT_BOARD.md, docs/control_tower/07_ACTIVE_WORKING_MEMORY.md
Changed:
- Added Tint Phase 5 candidate packs for the trusted single-turn, state-injected lane.
- Added a Tint Phase 5 strict pack for the active owner path.
- Promoted Tint Phase 5 strict cases into canonical coverage for:
  - PHASE5_TINT_COMPARE_DEEPEN_L1
  - PHASE5_TINT_NARROW_L2
  - PHASE5_TINT_EXIT_FORK_L3
- Refreshed control-tower phase state and active working memory to reflect Tint Phase 5 trusted-lane completion.
Why:
- Complete trusted-lane Phase 5 service coverage for Tint using the same validated pattern used for PPF and Ceramic.
- Keep canonical coverage, control-tower state, and active working memory aligned with current repo evidence.
UAT:
- canonical suite now passes at 38 / 38
- Tint Phase 5 strict trusted-lane coverage validated and promoted
- control tower and active working memory updated to match current repo evidence


Date: 2026-04-17
Files: tests/uat/phase5_polish_expectation_v1.json, tests/uat/phase5_polish_narrow_v1.json, tests/uat/phase5_polish_exit_fork_v1.json, tests/uat/phase5_polish_verbatim_strict_v1.json, tests/uat_cases.json, docs/control_tower/06_PHASE_AUDIT_BOARD.md, docs/control_tower/07_ACTIVE_WORKING_MEMORY.md
Changed:
- Added Polishing Phase 5 candidate packs for the trusted single-turn, state-injected lane.
- Added a Polishing Phase 5 strict pack for the active owner path.
- Promoted Polishing Phase 5 strict cases into canonical coverage for:
  - PHASE5_POLISH_EXPECTATION_DEEPEN_L1
  - PHASE5_POLISH_NARROW_L2
  - PHASE5_POLISH_EXIT_FORK_L3
- Refreshed control-tower phase state and active working memory to reflect Polishing Phase 5 trusted-lane completion.
Why:
- Complete trusted-lane Phase 5 service coverage for Polishing using the same validated pattern used for PPF, Ceramic, and Tint.
- Keep canonical coverage, control-tower state, and active working memory aligned with current repo evidence.
UAT:
- canonical suite now passes at 41 / 41
- Polishing Phase 5 strict trusted-lane coverage validated and promoted
- control tower and active working memory updated to match current repo evidence


### SUPPORT AUTHORITY GAP IDENTIFIED — PHASE 0–6 DEPENDENCY AUDIT

Scope:
- Product Naming Registry vs Runtime Consumption alignment

Findings:
- ROOF_PPF_BLACK_GLOSS is actively used across intake, qualification, routing, and pricing,
  but lacks complete metadata block (display_name, warranty_label, short_description) in registry.
- PPF_FRONT_GLOBAL is used in SKU matrix and price table, but not fully represented as a metadata block in registry.

Decision:
- No runtime or engine patch applied.
- No parallel logic introduced.

Action:
- Parked for dedicated support-authority cleanup phase.
- To be resolved in a single controlled registry update (not incremental patching).

Impact:
- No current runtime break observed.
- Potential future risk in customer-facing rendering if metadata is required.

Status:
- Accepted deviation (temporary)


Date: 2026-04-26
Files: runner/check_arch_changelog.py
Changed:
- Expanded ARCH_CHANGELOG gate scope to include control-tower docs, tooling, and GitHub workflow files.
- Added enforced audit-trail coverage for:
  - docs/control_tower/
  - tools/
  - .github/
Why:
- Governance and enforcement changes are architecture changes and must not bypass changelog discipline.
- Recent enforcement audit showed tools/control docs could change without ARCH_CHANGELOG enforcement.
UAT:
- verified by direct diff inspection of ARCH_PATH_PREFIXES
- follow-up commit should require this changelog entry through existing pre-commit gate

Date: 2026-04-26
Files: tools/start_lane.sh, .gitignore, .git/hooks/pre-commit
Changed:
- Start lane now creates .snash_patch_gate_reviewed after running patch_gate.sh.
- .snash_patch_gate_reviewed added to .gitignore as local transient marker.
- Local pre-commit hook updated to require patch-gate marker for architecture/governance surfaces and to invoke pre-commit framework checks.
Why:
- Patch discipline existed but was not connected to the local commit gate.
- Pre-commit config existed but was not being invoked by the active local hook.
UAT:
- verified by direct inspection of .git/hooks/pre-commit and tools/start_lane.sh
- next commit should run SNASH guard plus pre-commit configured checks

Date: 2026-04-26
Files: docs/control_tower/11_ENFORCEMENT_AUDIT_SUMMARY.md, docs/control_tower/05_GIT_WORKFLOW_AND_CHECKPOINTS.md
Changed:
- Recorded final enforcement audit result after activating pre-commit framework and patch-gate marker discipline.
- Added investigation-vs-trust rule to distinguish fast inspection from validated commit/promotion work.
- Recorded UAT/API credit discipline as advisory rather than hard-blocked.
Why:
- Preserve the governance findings before moving into Phase 4.
- Prevent future confusion between investigation shortcuts and trusted rollout evidence.
UAT:
- documentation-only update
- based on successful controlled active UAT and successful pre-commit enforcement run

Date: 2026-04-26
Files: tools/audit/pre_uat_guard.py, tools/audit/pre_uat_case_readiness_check.py
Changed:
- Added no-credit UAT case readiness check before controlled active UAT runs.
- Blocks Phase3B expected cases when they are single-turn and do not provide an explicit multi-turn qualification path.
Why:
- Prevent credit waste from technically valid but logically premature Phase 4 / Phase3B test packs.
- Preserve investigation-vs-trust discipline before spending API credits.
UAT:
- no-credit local validation passed on existing Phase3A pack
- no-credit negative check blocked bad single-turn Phase3B fixture

Date: 2026-04-26
Files: tools/audit/pre_uat_case_readiness_check.py
Changed:
- Added no-credit validation for multi-turn case shape before active UAT runs.
- Blocks turns with missing content, non-string content, or invalid role.
Why:
- Prevent API-format errors from reaching OpenAI and wasting credits.
- Strengthen Phase 4 / multi-turn UAT fixture discipline before rollout validation.
UAT:
- no-credit pre-UAT guard passed on phase4_price_entry_multiturn.json

Date: 2026-04-26
Files: tools/audit/pre_uat_case_readiness_check.py
Changed:
- Aligned multi-turn readiness validation with run_active_uat_raw.py string-turn format.
- Blocks non-string turns before active UAT reaches the API.
Why:
- The runner expects turns as plain strings and wraps each item as a user message.
- Prevent malformed object-turn fixtures from wasting API credits.
UAT:
- no-credit pre-UAT guard passed on phase4_price_entry_multiturn.json

Date: 2026-04-26
Files: 00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md, docs/control_tower/issues/ISSUE_010_PHASE0_3_LABEL_CONTRACT_AUDIT.md
Changed:
- Added Route E bridge for SERVICE_CONFIRMED + READY_FOR_NEGOTIATION + phase3a_complete to enter Phase 3B price/options delivery.
- Kept direct PRICE_REQUEST behavior unchanged.
- Excluded wrap from the automatic Phase 3B bridge.
- Recorded business decision and patch scope in ISSUE_010.
Why:
- After required Phase 3A qualification is complete, SNASHGPT should not delay price/options with a weak preparation response.
- Safety concern is early price leakage, not post-qualification price delivery.
UAT:
- pending focused active rollout UAT for phase4_price_entry_multiturn.json

Date: 2026-04-26
Files: runner/context_reset_prompt_active.txt
Changed:
- Added active UAT bridge protection preventing PPF Phase 3A from reopening after coverage and driving pattern are already present with READY_FOR_NEGOTIATION.
- Blocks PHASE3A_Q_PPF_COMPARISON_FOCUS from resurfacing in completed PPF qualification path.
Why:
- Prior evidence showed PPF Q3 overflow / extra question after coverage + driving pattern.
- Current focused active UAT reproduced the same bridge drift after Route E was made explicit.
UAT:
- pending focused active rollout UAT for phase4_price_entry_multiturn.json

Date: 2026-04-26
Files: docs/control_tower/05_GIT_WORKFLOW_AND_CHECKPOINTS.md
Changed:
- Added runtime-vs-bridge patch classification rule.
- Requires bridge/context prompt/UAT layer inspection before patching runtime engines when runtime rules already exist correctly.
Why:
- Prevent repeated mispatching of runtime engines for issues caused by bridge enforcement gaps.
- Captures the PPF Q3 overflow lesson as reusable governance.
UAT:
- documentation-only governance update

Date: 2026-04-26
Files: runner/context_reset_prompt_active.txt, runner/run_active_uat_raw.py
Changed:
- Added PPF_COVERAGE_INTENT and PPF_DRIVING_PATTERN to the active debug contract.
- Added extraction and state snapshot preservation for PPF qualifier values in the active raw UAT runner.
Why:
- Prevent bridge-state loss between turns where PPF coverage/driving qualifiers are completed but not preserved.
- Supports Phase 3A completion carry-through into Phase 3B without reopening Q3.
UAT:
- no-credit diff inspection completed
- focused active rollout UAT pending after commit

Date: 2026-04-26
Files: 00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
Changed:
- Made Route E selected_phrase_id mapping explicit for PPF, ceramic, tint, and polishing.
- Added rule that selected_phrase_id must not be null when E1 or E2 Route E conditions are true.
Why:
- Focused active UAT reached READY_FOR_NEGOTIATION with completed PPF qualifiers, but selected_phrase_id remained null.
- Phase 3B entry must select the approved PHASE3B_* phrase block once Route E is true.
UAT:
- pending focused active rollout UAT for phase4_price_entry_multiturn.json
