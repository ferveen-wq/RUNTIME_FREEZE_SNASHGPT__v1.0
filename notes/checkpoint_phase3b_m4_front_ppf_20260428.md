# CHECKPOINT — Phase 3B / M4 Front PPF Recovery

## Current state
- Branch: fix/phase3-gate-alignment
- Modified:
  - 00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime/PRICE_LADDER_ENGINE.md
  - runner/context_reset_prompt_active.txt
- Temporary UAT files:
  - tests/active_rollout_uat/tmp_phase3b_front_ppf_single.json
  - tests/active_rollout_uat/tmp_ppf_front_multiturn_guard.json
  - tests/active_rollout_uat/tmp_ppf_front_multiturn_price_guard.json

## What was fixed
- FULL_FRONT non-matte PPF now has terminal lock:
  - selected_skus MUST be [PPF_FRONT_GLOBAL]
  - no DEFAULT / SECOND / UPLADDER / DOWNLADDER
  - no gloss full-body/highway path
  - single price from VCB table only
- Gloss full-body PPF block now applies ONLY when PPF_COVERAGE_INTENT == FULL_BODY.
- Context bridge now preserves known qualifier fields:
  - prevents FULL_FRONT being rewritten to FULL_BODY unless customer explicitly asks.

## Evidence
- Controlled UAT passed:
  - tests/reports/raw_uat_20260428_164402.json
  - case: ppf_front_camry_vcb2
  - selected_skus: [PPF_FRONT_GLOBAL]
  - price_source_rows: PPF_FRONT_GLOBAL / VCB_2 / 295
  - PPF_COVERAGE_INTENT: FULL_FRONT
  - price_ladder_state: FINAL_PRICE_REACHED

## Guards
- git diff --check: PASS
- tools/audit/pre_uat_guard.py: PASS
- runner/price_preflight_check.py: PASS
- runner/price_resolver_offline.py: PASS
- explicit offline front resolver: PASS
- active_rollout_guard.py: FAILS due to pre-existing active prompt business-routing text
- ruff check runner tools: FAILS due to unrelated existing repo issues

## Open question
- Need decide whether to:
  1. accept controlled-UAT lane as current validation lane, or
  2. fix active_rollout_guard / active prompt governance before widening UAT.

## Resume instruction
When resuming, start by reading this checkpoint and running:
- git status --short
- git diff --stat
- python3 tools/audit/pre_uat_guard.py
- python3 runner/price_preflight_check.py
