# ISSUE_005 — Active UAT must not pass without strict expectations

## Type
Test Harness / UAT Discipline

## Problem
A Phase 3A Ceramic smoke test passed even though the output jumped directly to Phase 3B pricing.

Reason:
The test case only provided input/turns and did not assert:
- expected phase
- expected selected_phrase_id
- expected QUALIFICATION_STATUS
- forbidden premature price route

## Risk
False positive UAT results can mark Phase 0–3 as stable while runtime behavior is wrong.

## Rule
No Phase 0–3 active UAT test may be considered valid unless it checks at least:
- phase
- selected_phrase_id
- QUALIFICATION_STATUS

For price-entry tests, also check:
- price_ladder_state
- READY_FOR_NEGOTIATION

For qualifier tests, also forbid:
- premature PHASE3B_* route

## Status
OPEN

## Runtime Patch Due Diligence Rule — 2026-04-24

Owner-map alone is not sufficient before patching runtime files.

Before any runtime patch, the following checklist is mandatory:

1. Run owner-map for relevant signals / phrase IDs.
2. Check `AUTHORITY_INDEX.md` for declared owner/reader boundaries.
3. Inspect the surrounding section of the candidate owner file.
4. Inspect adjacent exception/gate sections.
5. Compare similar-service behavior if applicable.
6. Check whether the intended rule already exists.
   - If it already exists, strengthen that rule.
   - Do NOT add a duplicate or parallel authority.
7. Define validation before patching.
8. Patch only the confirmed owner surface.

ISSUE_006 example:
- Initial owner-map pointed to `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`.
- Further section inspection showed the correct patch area is likely the existing
  `QUALIFICATION NOT-READY SUPPRESSION (HARD)` block, not a new parallel rule near Route E.

## Owner Proof Standard — 2026-04-24

`AUTHORITY_INDEX.md` is a governance claim, not final truth by itself.

Before accepting an owner decision, require three proof layers:

1. Declared Owner
   - `AUTHORITY_INDEX.md`
   - control-tower issue notes
   - architecture docs

2. Actual Active Runtime Owner
   - active runtime file contents
   - owner_map output
   - surrounding section inspection
   - adjacent gate/exception inspection

3. Behavioral Owner
   - strict active UAT proves the suspected owner path is involved
   - patch validation must show the specific failure changes
   - no unrelated surface should be patched first

Rule:
- If architecture docs disagree with active runtime behavior, active runtime + strict UAT evidence wins.
- Do not trust trackers or authority docs alone.
