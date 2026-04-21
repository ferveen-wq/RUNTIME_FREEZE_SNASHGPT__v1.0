# GAP-TR-004 Patch Plan v1 — 2026-04-20

## Target model

Phase 5 must use one central selector only.

Business/runtime order:
1. service already locked from earlier phases
2. price already exposed
3. objection detected
4. Phase 5 selects the correct path inside that same service
5. only that service family may output

## Must stay

- central brain across all services
- one universal sales flow
- service-specific objection handling
- service-specific phrase ownership
- no re-qualification
- no re-pricing inside Phase 5

## Must not remain

- mixed Phase 5 ownership shapes
- pre-router service-specific selector competing with main router
- post-router service-specific selector competing with main router
- side authority that can still assign PHASE5 selected_phrase_id outside the chosen owner

## Patch direction

Use:
- one central Phase 5 selector in `runner/context_reset_prompt.txt`

That selector must:
- assume service is already locked
- never re-decide service family from scratch
- map objection path only within locked service
- stop immediately after selected service phrase

## Planning constraints

- do not add parallel authority blocks
- do not patch phrase library
- do not widen beyond Phase 5 ownership structure
- do not treat Family A historical gaps as new independent defects

## Validation plan

Target:
- tests/uat/phase5_polish_verbatim_strict_v1.json

Boundaries:
- tests/uat/phase5_ceramic_verbatim_strict_v1.json
- tests/uat/phase5_ppf_verbatim_strict_v1.json

Stable lane protection:
- tint Phase 5 pack if available / currently trusted lane references

Success condition:
- GAP-TR-004 target case passes
- no new cross-service leakage
- no regression in ceramic/tint stable lanes
- no new PPF branch collapse beyond already known non-runtime exclusions
