# ARCH_CHANGELOG.md

## Format (required)
- Date:
- Files:
- Changed:
- Why:
- UAT:

---

## Entries

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
  - tests/uat_cases.json
  - tests/regression_cases_uat.json
- Changed:
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
  - UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py (16/16 green)
  - Tag: uat_pass_2026-02-21b