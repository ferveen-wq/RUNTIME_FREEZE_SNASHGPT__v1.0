## 2026-02-24 — PPF PRICE_REQUEST fast-path (null Phase3A qualifier guard) (UAT green)

- Files:
  - 00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md

- Changed:
  - Added a HARD fast-path for PPF when request_type == PRICE_REQUEST and the same message already contains:
    - PPF_COVERAGE_INTENT (known) AND PPF_DRIVING_PATTERN (known)
  - Prevents Phase 3A from triggering with phase3a_required=true while phase3a_qualifier_id is null.
  - Preserves conditional comparison-focus behavior by excluding competitor/brand-fixation triggers from the fast-path.

- Why:
  - Regression: Phase 3B ladder pack intermittently routed into Phase 3A with a null qualifier-id, blocking Route E pricing even when the user already gave full + highway context.
  - This aligns runtime behavior with Architecture B (price progression when qualification is already satisfied in-message).

- UAT:
  - python runner/run_uat.py tests/regression_phase3b_ladder.json (3/3 green)
  - python runner/run_uat.py tests/regression_e2e_core.json (3/3 green)
  - UAT_CASES_FILE=tests/regression_cases_uat.json python runner/run_uat.py (13/13 green)
## 2026-02-24 — Negotiation Core Stabilization + PRICE_REQUEST carry-forward (Phase 3B E2E fix)

## 2026-02-24 — Phase 0–2 greeting + new-car browsing hygiene (Option A contract alignment)

- Files:
  - runner/context_reset_prompt.txt
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
  - tests/regression_cases_uat.json

- Changed:
  - Runner prompt request_type enum set aligned to runtime outputs (kept GREETING_ONLY/BROWSING_GENERIC etc. as-is).
  - GREETING_ONLY phrase A4_GREETING_SERVICE_CONTEXT updated to be neutral and NOT ask vehicle model/year.
  - “New car / generic automotive inquiry” redirect updated to avoid forcing model-year question (ask which car only).
  - Updated regression expectation to match runtime enum (GREETING_ONLY).

- Why:
  - Prevent Phase 0–2 regressions where greeting-only or new-car browsing incorrectly forces vehicle model/year too early.
  - Keep runtime contract stable (Option A) while making customer-facing behavior match real reception/showroom flow.

- UAT:
  - UAT_CASES_FILE=tests/regression_cases_uat.json python runner/run_uat.py (verify greeting + new-car cases)

- Files:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - 00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md
  - tests/regression_negotiation_core.json

- Changed:
  - Scoped **Exception C (Competitor Cheaper / Price Pressure while NOT_READY)** to require missing vehicle_model OR vehicle_year.
    - Prevents Phase 0–2 competitor handling from leaking into post-price flows.
  - Added **2.47 PRICE_REQUEST_CARRY_FORWARD (HARD)** rule.
    - Ensures qualifier answers inside an active pricing conversation retain `request_type = PRICE_REQUEST`.
    - Prevents regression where Phase 3A resumed instead of returning to Phase 3B pricing.

- Why:
  - Multi-turn E2E regression revealed:
    1) NOT_READY competitor logic incorrectly triggering after vehicle context was already known.
    2) `request_type` dropping to `OTHER` on qualifier answers, breaking return-to-pricing behavior.
  - Required deterministic stabilization of Architecture B:
    qualification → price ladder → anchor → negotiation.

- UAT Proof:
  - tests/regression_phase3a_chain.json → 10/10 green
  - tests/regression_phase3b_ladder.json → 3/3 green
  - tests/regression_e2e_core.json → 3/3 green
  - tests/regression_negotiation_core.json → 2/2 green

Status: Stable. Phase 5 negotiation core deterministic.
## 2026-02-24 — PRICE_REQUEST carry-forward stabilization (Phase 3B E2E fix)

- Files:
  - 00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md
  - tests/regression_negotiation_core.json

- Changed:
  - Added **2.47 PRICE_REQUEST_CARRY_FORWARD (HARD)** rule.
  - Ensures qualifier answers inside an active pricing conversation retain `request_type = PRICE_REQUEST`.
  - Prevents regression where Phase 3A resumed instead of returning to Phase 3B pricing.

- Why:
  - Multi-turn E2E regression revealed `request_type` dropped to `OTHER` on qualifier answers.
  - Required deterministic return-to-pricing behavior after qualification completion.
  - Maintains Architecture B: qualification → price ladder → anchor → negotiation.

- UAT Proof:
  - `tests/regression_phase3a_chain.json` → 10/10 green
  - `tests/regression_phase3b_ladder.json` → 3/3 green
  - `tests/regression_e2e_core.json` → 3/3 green
  - `tests/regression_negotiation_core.json` → 2/2 green

Status: Stable.
## 2026-02-24 — UAT runner CLI + Phase 3B ladder alignment (Architecture B) + Route E pricing gate fix

- Date: 2026-02-24

- Files:
  - runner/run_uat.py
  - runner/context_reset_prompt.txt
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - tests/regression_phase3b_ladder.json

- Changed:
  - Runner: added CLI support to run a specific cases JSON path (kept env var `UAT_CASES_FILE` behavior).
  - Debug contract: expanded DEBUG_OUTPUT field list in runner prompt to include service/vehicle + Phase 3A fields.
  - HIGH-RISK (PHASE4_8): Route E pricing gate now allows pricing when `phase3a_qualifier_id` is null (prevents `selected_phrase_id: null` fallthrough on PRICE_REQUEST when no qualifier is pending).
  - Phase 3B ladder regression: aligned expectations to Architecture B (qualify first for ceramic/tint; price only when truly READY).

- Why:
  - Prevent accidental default-pack execution (runner ignoring CLI args) and enable deterministic pack runs.
  - Fix a PRICE_REQUEST fallthrough that produced customer-facing output with `selected_phrase_id: null`.
  - Align Phase 3B ladder regression coverage with the chosen safer contract: do not auto-capture same-message qualifiers.

- UAT:
  - python runner/run_uat.py tests/regression_phase3a_chain.json (10/10 green)
    - Report: tests/reports/uat_report_20260223_204715.json
  - python runner/run_uat.py tests/regression_phase3b_ladder.json (3/3 green)
    - Report: tests/reports/uat_report_20260223_212847.json

### Tags / commits
- Tag: (pending) phase3b_ladder_uat_green_v2

## 2026-02-23 — Phase 3A drift cleanup (low risk)
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md: VEHICLE_ONLY__ASK_SERVICE made generic (removed hardcoded model/year).
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md: removed unreferenced Z_DEPRECATED__PHASE3B_WRAP_STANDARD__LEGACY block (mixed EN/AR pairs).
# ARCH_CHANGELOG

## 2026-02-23 — Phase 3A Freeze (tag: phase3a_uat_green_v1)

### Goal
Freeze Phase 3A qualifier chain so it is deterministic, UAT-covered, and resistant to drift.

### Changes
- QUALIFICATION_ENGINE.md
  - Enforced SERVICE_CONFIRMED routing for service-keyword messages.
  - Added/validated Phase 3A qualifier sequencing:
    - PPF: coverage → driving → comparison (conditional)
    - Ceramic: goal → wash pattern
    - Tint: goal → coverage
    - Wrap: finish (wrap-scope not routed in Phase 3A)
  - Added “old vehicle PPF” gate to ask paint/repaint/bodywork first while keeping request_type=SERVICE_CONFIRMED.

- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - Locked Phase 3A routing: when phase3a_required=true, output must be verbatim from PHASE4_6, exactly one question, no extra blocks.

- PHASE4_6_HUMAN_PHRASE_LIBRARY.md
  - Added missing qualifier blocks:
    - PHASE3A_Q_CERAMIC_GOAL
    - PHASE3A_Q_TINT_GOAL
  - Ensured qualifier blocks are single-question and bilingual.

- runner/run_uat.py
  - Fixed execution to define ROOT properly (prevents NameError).

- runner/audit_runtime.sh
  - Added lightweight audits to prevent drift (missing qualifier IDs, duplicate headings, wrap-scope sanity).

- tests/regression_phase3a_chain.json
  - Added regression suite for Phase 3A chain.

### Verification
- runner/audit_runtime.sh: PASS
- UAT_CASES_FILE=tests/regression_phase3a_chain.json python runner/run_uat.py: Passed=10, Failed=0

### Notes / Guardrails
- Any future Phase 3A change requires:
  1) update test(s),
  2) audit_runtime.sh pass,
  3) UAT green,
  4) new tag.# ARCH_CHANGELOG.md

## Format (required)
- Date:
- Files:
- Changed:
- Why:
- UAT:

---

## Entries

- 2026-02-23: Fix Phase 3A eligibility by aligning `service_intent` comparisons with runtime lowercase normalization (ppf/ceramic/tint), preventing Phase 0–2 fallthrough when model+year are present.

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

Date: 2026-02-21
- Files: tests/uat_cases.json
- Changed: Added SAFE/AMBIGUOUS/digits-only vehicle alias Phase 0–2 UAT coverage
- Why: Protect vehicle repo rules (no guessing) + prevent regressions
- UAT: UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py

- Date: 2026-02-21
- Files: MULTIPLE
- Changed: Phase 0–2 stabilization guardrails + UAT harness hardening (request_type enums, JSON validation, Phase 0–2 regression coverage).
- Why: Prevent patch drift and ensure Phase 0–2 routing remains stable (greeting/browsing/service-confirmed/price-hold/vehicle alias behavior).
- UAT: UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py

	Date: 2026-02-21
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


## 2026-02-23 — Phase 0–3A guardrails + Phase 3B ladder regression (UAT green)

- Files:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/OUTPUT_RESPONSE_TEMPLATE.md
  - 02__Parameters/SKU_SELECTION_MATRIX.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - tests/regression_phase3a_chain.json
  - tests/regression_phase3b_ladder.json

- Changed:
  - Relaxed acknowledgement rule (allow max 1 natural acknowledgement; blocked when NOT_READY)
  - Converted polishing from “prep-only” contradiction to standalone priced service (only when service_intent == polishing)
  - Hardened Phase 3 vehicle-only guard to prevent qualifier override
  - Restored canonical price_ladder_state enums (APPLICABLE / NONE / NOT_APPLICABLE)

- Why:
  - Align runtime contract with actual pricing ladder behavior
  - Remove polishing logic contradiction
  - Prevent Phase 3A override drift when vehicle-only message is sent
  - Lock Phase 3B ladder regression before negotiation expansion

- UAT:
  - UAT_CASES_FILE=tests/regression_phase3a_chain.json python runner/run_uat.py (10/10 green)
  - UAT_CASES_FILE=tests/regression_phase3b_ladder.json python runner/run_uat.py (3/3 green)
  - Tag: phase3b_ladder_uat_green_v1

### Summary
Stabilized output hygiene + Phase 3A vehicle-only routing, aligned polishing pricing logic, and added Phase 3B ladder regression coverage. UAT green after fixes.

### Why
- Phase 3A regression failed when the user provided only vehicle model+year (no service): system incorrectly asked a PPF qualifier instead of asking which service.
- Needed a single-source authority update for acknowledgement words (allowed only if natural / non-templated).
- Polishing logic needed to be explicit: priced only when the customer is asking for polishing; never bundled into other service pricing.

### Changes (files)
- `00__LOCKED__UPLOAD_SET/00__Runtime/OUTPUT_RESPONSE_TEMPLATE.md`
  - Updated acknowledgement rule: allowed only if natural/non-templated; max 1 word; do not use when NOT_READY / ask_missing_info; “Thanks” allowed only if customer thanked first.
- `02__Parameters/SKU_SELECTION_MATRIX.md`
  - Updated polishing section: polishing is a standalone service priced only when `service_intent == polishing`; never added to ceramic/graphene/ppf/wrap/tint pricing; treat correction as prep/inspection gate when needed for other services.
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md`
  - De-templatized Phase 3B transition phrasing (kept meaning; reduced “templated” tone).
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
  - Enforced Phase 3 vehicle-only (model+year only, no service) hard route to `VEHICLE_ONLY__ASK_SERVICE` (stop, verbatim, 1 question).
- `tests/manual_single_case.json`
  - Added a manual single-case UAT for PASS 1 “BMW X5 2025 full PPF, mostly highway, how much?”
- `tests/regression_phase3b_ladder.json`
  - Added Phase 3B ladder regression cases (PPF / ceramic / tint) validating selected_phrase_id + `price_ladder_state: APPLICABLE`.

### Verification
- UAT green: `tests/regression_phase3a_chain.json` (10/10)
- UAT green: `tests/manual_single_case.json` (1/1)
- UAT green: `tests/regression_phase3b_ladder.json` (3/3)

### Tags / commits
- Tag: `phase0_3a_freeze_guardrails_green_v2` (Phase 0–3A guardrails + polishing alignment)
- Tag: `phase3b_ladder_uat_green_v1` (Phase 3B ladder regression green)
