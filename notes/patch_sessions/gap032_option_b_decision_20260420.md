# GAP-032 — OPTION B DECISION (2026-04-20)

## Decision

Adopt Option B as the single source of truth for `objection_repeat_count`:

- 1 = first objection
- 2 = second objection
- 3 = third objection or more

## Why

Due diligence confirms:

- current UAT packs already use:
  - 1 = L1
  - 2 = L2
  - 3 = L3
- Phase 5 assembly logic is already aligned to this model in practice
- current patch planning and trusted evidence are reasoning in this model
- the old objection-engine 0/1/2 meaning is the outlier and creates contract drift

## Control interpretation

Treat the old model below as legacy drift, not active truth:

- 0 = first
- 1 = second
- 2 = third+

## Required alignment

The following must be aligned to Option B together:

- `00__LOCKED__UPLOAD_SET/01__Engines/OBJECTION_RESOLUTION_ENGINE.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
- `runner/context_reset_prompt.txt`
- affected UAT packs / canonical cases
- tracker / gap-register notes where needed

## Important exclusions

Do NOT mix this with:
- PPF narrow L2 forbidden-word issue
- phrase-library wording mismatch
- other non-runtime contract exclusions already separated in control docs

## Status

- GAP-032 decision chosen
- ready for aligned patch planning
- do not do isolated router-only edits from here
