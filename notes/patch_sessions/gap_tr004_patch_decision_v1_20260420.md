# GAP-TR-004 Patch Decision v1 — 2026-04-20

## Decision

Phase 5 phrase selection must have one runtime owner only:

- `runner/context_reset_prompt.txt`
- `PHASE 5 SERVICE-OWNER ROUTER`

## What remains as non-routing authority

Keep:
- `PHASE5_PPF_PRICE_GAP_DEEPEN_L1 VERBATIM LOCK`
- `PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1 VERBATIM LOCK`
- `PHASE 5 VERBATIM RENDERING`

Reason:
- these control rendering only
- they do not decide service family or branch ownership

## What must stop acting as independent Phase 5 selectors

Demote from routing ownership:
- `CERAMIC REPEAT OBJECTION MUST NARROW`
- `PHASE 5 TINT PHRASE SELECTION`

Reason:
- they assign `selected_phrase_id` outside the central router
- this creates mixed Phase 5 ownership
- mixed ownership is not aligned with the accepted business model

## Accepted runtime model

Phase 5 order must be:

1. service already locked from earlier phases
2. price already exposed
3. objection detected
4. central router selects path inside locked service
5. render selected phrase only

## Patch intent

Patch only the ownership shape.

Do not:
- add new phrase blocks
- patch phrase library
- widen into other phases
- add parallel runtime authorities

## Validation

Target:
- `tests/uat/phase5_polish_verbatim_strict_v1.json`

Boundary:
- `tests/uat/phase5_ceramic_verbatim_strict_v1.json`
- `tests/uat/phase5_ppf_verbatim_strict_v1.json`

Optional stable-lane protection:
- tint Phase 5 pack if available

## Expected success

- polishing L1 stays inside polishing
- no ceramic/tint regression from ownership cleanup
- no new cross-service leakage
