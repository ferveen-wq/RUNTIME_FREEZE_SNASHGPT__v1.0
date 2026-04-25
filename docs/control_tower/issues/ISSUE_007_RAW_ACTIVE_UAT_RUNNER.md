# ISSUE_007 — Create raw active UAT runner for rollout truth

## Type
Test Harness / Rollout Validation

## Problem
`runner/run_uat.py` contains many post-processing force functions that can reshape model output after runtime execution.

This means active UAT may not represent pure runtime behavior.

## Risk
- False passes
- False failures
- Wrong runtime patches
- API credit waste
- Phase 0–3 stability claims based on polluted evidence

## Decision
Create a separate raw active UAT runner.

## Requirements
The raw runner must:
- use `00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime`
- support `input` and `turns`
- preserve multi-turn state
- extract debug output
- enforce strict expectations
- reject weak active UAT cases
- perform contradiction guards
- NOT run any `_force_*`, `_enforce_*`, `_sanitize_*`, or `_rebuild_*` post-processing

## Status
CLOSED — raw runner created and guarded

Closure note — 2026-04-25:
Raw active runner exists, supports strict expectations, cost controls, multi-turn state preservation, and runner health checks. Pre-UAT guard now verifies runner health and stale prompt overrides before trusted UAT.

## Legacy Runner Argument Risk — 2026-04-24

Inspection found `runner/run_uat.py` does not use:
- `argparse`
- `sys.argv`
- `--runtime-dir`
- `--output`

This means command-line flags previously passed to `runner/run_uat.py` may have been ignored.

Risk:
- Tests believed to be using `00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime` may not have been using that folder directly.
- Reports believed to be written to custom `--output` paths may instead be written only to default `tests/reports`.
- Prior active rollout validation may be partially untrusted until verified by a raw active runner.

Decision:
- `runner/run_uat.py` must not be treated as rollout truth.
- `runner/run_active_uat_raw.py` must explicitly load the active runtime folder and explicitly write its report path.

## Raw Runner Dependency Gap — 2026-04-24

Dependency scan showed current active runtime folder contains:
- `PHASE6__SERVICE_CANON_BUNDLE.md`
- `SKU_SELECTION_MATRIX.md`
- `PRICE_TABLE_VAT_INCL.md`

But active runtime folder does NOT contain:
- `GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md`
- `PRODUCT_SERVICE_CANON.md`

These files were part of the earlier uploaded/runtime testing context and are referenced by active runtime rules.

Risk:
- Raw Phase 0–2 service/product recognition tests may be incomplete if product alias/canon files are missing.
- Running raw tests before resolving this may create false failures or false confidence.

Decision:
- Do not treat raw runner results as final until active runtime dependency set is reconciled.
- Next step: decide whether these files must be copied into `00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime` or explicitly loaded from locked repository paths.

## Raw UAT Cost Control Rule — 2026-04-24

Raw active UAT is expensive because each API call loads the active runtime bundle.

Rules:
- Do not run multi-run raw loops unless a specific hypothesis requires determinism proof.
- Do not run full-service packs during normal debugging.
- Use single-case raw checks for diagnosis.
- Use 3-run checks only after a single-case issue is isolated.
- Use 5-run checks only for final validation or instability classification.
- Full all-service packs are milestone checks only.

Required runner improvements:
- Add `CASE_ID` filter.
- Add `MAX_CASES` limit.
- Add warning/confirmation for multi-case raw runs using `RAW_UAT_CONFIRM=YES`.
- Print number of cases before execution.

## Raw Runner Multi-Turn Health Finding — 2026-04-25

Audit found `runner/run_active_uat_raw.py` supports `turns`, but appends assistant output back into conversation as raw text only:

`conversation.append({"role": "assistant", "content": text})`

Risk:
- Runtime expects next turn continuity through signals such as:
  - `previous_turn.selected_phrase_id`
  - `phase`
  - `QUALIFICATION_STATUS`
  - `active_service_context`
- If these signals are not preserved clearly between turns, multi-turn UAT may falsely fail and cause unnecessary runtime patching.

Decision:
- Before trusting multi-turn raw UAT, add a runner health check.
- Raw runner must prove it preserves parsed debug/state signals into the conversation context.
- Do not patch runtime based on multi-turn failures until runner health is confirmed.
