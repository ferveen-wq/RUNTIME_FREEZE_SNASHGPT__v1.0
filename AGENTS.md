# AGENTS.md

Purpose:
This file gives Cursor a safe operating brief for the SNASHGPT repo.

## Repo operating rule

Do not patch blindly.
Always identify the correct layer first:
- locked runtime
- tooling
- tests/UAT
- control tower
- notes/evidence
- legacy/archive

Start with:
- 00__CONTROL_TOWER/PROJECT_OPERATING_MAP.md

## Live runtime authority

Treat these as the live runtime authority:
- 00__LOCKED__UPLOAD_SET/00__Runtime
- 00__LOCKED__UPLOAD_SET/01__Engines
- 00__LOCKED__UPLOAD_SET/02__Repositories
- 00__LOCKED__UPLOAD_SET/03__Parameters
- 00__LOCKED__UPLOAD_SET/03__Playbooks

Key authority files:
- 00__LOCKED__UPLOAD_SET/00__Runtime/AUTHORITY_INDEX.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PATCH_PROTOCOL.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md

## Patch discipline

Before any patch:
1. confirm file role
2. prove raw defect
3. rule out tooling/UAT shaping
4. check duplicate authority
5. choose narrowest patch target
6. define validation first

Never patch phrase wording first if the issue may actually belong to:
- QUALIFICATION_ENGINE.md
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- runner/context_reset_prompt.txt
- runner/run_uat.py
- tests/UAT expectations

## Runtime-specific tracing order

When a defect appears, trace in this order:
1. intake / qualification output shape
2. orchestration and readiness
3. assembly precedence
4. phrase selection
5. runner prompt forcing
6. UAT harness normalization/injection
7. test expectation shape

## Working style

- Prefer small diffs
- Keep runtime fixes separate from cleanup commits
- Preserve legacy/reference material instead of deleting blindly
- Use existing authorities instead of creating parallel files
- Treat notes as evidence, not runtime authority

## Current project context

Current control document:
- 00__CONTROL_TOWER/PROJECT_OPERATING_MAP.md

Recent repo work:
- validated reentered continue and strict Phase 3B guards
- relocated legacy root governance docs into notes archive
- added patch gate rules and Phase 0-2 wording audit notes

## High-risk areas

- Phase 0-2 vs Phase 3A boundary
- Phase 3B strict price-ready behavior
- assembly precedence vs phrase defects
- support-routing precedence
- duplicate governance text
- tooling/UAT shaping false positives
