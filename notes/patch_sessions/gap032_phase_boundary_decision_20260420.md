# GAP-032 — PHASE-BOUNDARY RESOLUTION (2026-04-20)

## Final Model (Resolved)

`objection_repeat_count` is NOT a flat global counter.

It is a **phase-aware counter**:

### Phase 4 (first post-price reaction)
- 0 = first objection after price exposure
- Remains inside Phase 4 handling
- No Phase 5 escalation allowed

### Phase 5 (negotiation / repetition stage)
- 1 = second objection (first repeat after Phase 4)
- 2 = third objection
- 3+ = fourth or more → exit pressure

## Interpretation

- Phase 4 uses:
  - objection_repeat_count == 0

- Phase 5 uses:
  - objection_repeat_count >= 1

And inside Phase 5:

- 1 → L1 (deepen)
- 2 → L2 (narrow)
- 3+ → L3 (exit fork)

## Why this is correct

Evidence shows:

- Phase 4 UAT packs consistently use:
  - objection_repeat_count = 0

- Phase 5 UAT packs consistently use:
  - 1 / 2 / 3

- Runtime prompt already enforces:
  - Phase 4 guards at count == 0
  - Phase 5 router starts at count >= 1

- Only the objection engine documentation still reflects the legacy flat model.

## What this fixes

- Removes GAP-032 as a “global mismatch”
- Reclassifies it as:
  - documentation / contract misinterpretation
  - NOT a runtime routing defect

## Required updates

Align documentation and contracts to this model:

- OBJECTION_RESOLUTION_ENGINE.md
  - rewrite repeat_count_meaning section

- ARCHITECTURE_GAP_REGISTER.md
  - update GAP-032 from “mismatch” → “resolved via phase-boundary model”

- control_tower working memory / notes
  - remove “choose Option A vs B” ambiguity

## What must NOT be changed

- Phase 4 UAT packs (count = 0)
- Phase 5 UAT packs (1 / 2 / 3)
- Phase 5 router thresholds (already correct)
- runtime guards using == 0 for first objection

## Status

- GAP-032 root cause resolved
- No further router patching required for this issue
- Proceed to controlled doc alignment only
