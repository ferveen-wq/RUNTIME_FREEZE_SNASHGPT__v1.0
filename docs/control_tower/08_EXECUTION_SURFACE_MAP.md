# 08_EXECUTION_SURFACE_MAP.md

## Purpose
This file defines which repo surfaces are active, reference-only, stale, or ignored during SNASHGPT rollout validation.

## Active Surfaces

### Runtime Upload Surface
`00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime`

Status: ACTIVE

Rule:
Only files copied from the approved runtime manifest are allowed here.

### Active UAT Surface
`tests/active_rollout_uat`

Status: ACTIVE

Rule:
Only current rollout smoke tests and reports are active evidence here.

### Issue Tracking Surface
`docs/control_tower/issues`

Status: ACTIVE CONTROL-TOWER SURFACE

Rule:
All active runtime/UAT defects must be logged here before patching.
Each issue must include problem, expected vs actual behavior, classification, owner candidate, validation plan, and status.

## Reference Surfaces

`00__LOCKED__UPLOAD_SET`

Status: SOURCE OF TRUTH / LOCKED SOURCE

Rule:
Do not run Project UAT directly from this folder unless copied into the active rollout surface.

## Stale / Ignored Surfaces Pending Classification

`tests/uat`
`tests/reports`
`notes/deprecated_uat`
`notes/uat_deferred`
`notes/deferred_invalid_uat`
`Runtime for the uploads`
`99__ARCHIVE__LEGACY_IMPORTS`
`00__LOCKED__UPLOAD_SET__MATTE_BACKUP_20260228_043718`

Rule:
These must not be treated as active rollout evidence unless explicitly reclassified.

## Findings

### MANIFEST-DUP-001
Status: OPEN
Surface: `RUNTIME_LOAD_MANIFEST.md`

Finding:
The manifest currently has duplicate file references:
- `KNOWLEDGE__RUNTIME_CORE_BUNDLE.md`
- `PHASE0_2_LOCK_INDEX.md`
- `PHASE3A_QUALIFICATION_DECISION_MATRIX.md`

Impact:
- Active rollout upload surface still resolves to 25 unique files.
- No missing active files.
- No extra active files.
- This does not prove a runtime logic defect.

Action:
Do not patch yet. Revisit after wired-but-not-manifested audit.

### RUNTIME-REGISTRY-001
Status: CLASSIFIED
Surface: `docs/control_tower/08_RUNTIME_CANDIDATE_FILE_REGISTRY.md`

Finding:
`00__LOCKED__UPLOAD_SET` contains 63 candidate markdown files.

Classification summary:
- 25 ACTIVE_PHASE_0_4
- 14 CANDIDATE_PHASE_5_PLUS
- 1 CANDIDATE_PHASE_7_PLUS
- 2 RUNTIME_CANDIDATE_READ_ONLY_AUTHORITY
- Remaining files are reference/control/skeleton/draft surfaces
- 0 UNKNOWN files remain

Impact:
The 25-file active upload set is valid for Phase 0-4 UAT only.
It is not the complete future runtime universe.

Action:
Do not expand active upload surface until the next UAT scope requires it.
Do not patch runtime logic until Phase 3A smoke evidence is generated from the clean active surface.

## Commit Guard vs Active Rollout Validation — 2026-04-25

SNASH Guard currently acts as commit hygiene / repository safety only.

It must NOT be treated as proof that active rollout runtime behavior is correct.

Active rollout validation authority is:

1. `tools/audit/run_active_uat_controlled.sh`
2. `runner/run_active_uat_raw.py`
3. `tests/active_rollout_uat`
4. `tools/audit/report_analyzer.py`
5. `tools/audit/owner_map.py` with active-only default

Known limitation:
Several legacy governance tools still point to `00__LOCKED__UPLOAD_SET`, `tests/uat`, or `runner/context_reset_prompt.txt`.

Rule:
For Phase 0–3 rollout evidence, prefer controlled active UAT over legacy guard output.

## Legacy Governance Tool Classification — 2026-04-25

Several commit / CI / governance tools still intentionally point to `00__LOCKED__UPLOAD_SET`, `tests/uat`, or `runner/context_reset_prompt.txt`.

Classification:
- These tools are LEGACY / LOCKED-SOURCE governance.
- They are not active rollout validation authority.
- They may remain useful for locked-source hygiene, phrase-library safety, and historical governance.
- They must not be used as proof that `00__ACTIVE_ROLLOUT_UPLOAD_SET` behavior is correct.

Active rollout proof must come from:
- `tools/audit/active_rollout_guard.py`
- `tools/audit/run_active_uat_controlled.sh`
- `runner/run_active_uat_raw.py`
- `tests/active_rollout_uat`
- `tools/audit/report_analyzer.py`
- `tools/audit/owner_map.py` active-only default

Future work:
- Do not mass-rewrite legacy tools until rollout scope requires it.
- If a legacy tool is promoted into active rollout governance, create a separate issue and verify it does not duplicate or compete with active rollout tools.
