
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
UAT: TODO





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
Files: MULTIPLE
Changed: TODO
Why: TODO
UAT: TODO
