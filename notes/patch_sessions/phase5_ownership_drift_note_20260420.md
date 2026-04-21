# Phase 5 Ownership Drift Note — 2026-04-20

## Conclusion from wiring audit

Phase 5 is intended to work as a post-price objection / clarification layer only.

Correct business/runtime order:
1. service already known from earlier phases
2. price already exposed
3. objection detected
4. correct Phase 5 path selected
5. only that service-specific phrase may speak

So Phase 5 should NOT be:
- objection detected
- then service locked

It should be:
- service already locked
- then objection handled inside that service

## What the live runtime currently shows

The live prompt currently uses mixed ownership shapes inside Phase 5:
- shared service-owner router
- ceramic pre-router special authority
- tint post-router dedicated authority
- PPF logic embedded inside the shared router
- polishing depends mainly on router behavior

This is not one clean ownership model.

## Likely defect pattern

Family A defects are consistent with:
- mixed Phase 5 ownership structure
- cross-service leakage
- unstable precedence between service-specific and shared authorities

This explains why:
- earlier phases can remain stable
- while Phase 5 still leaks or drifts

## Control interpretation

This is likely not just a single bad phrase rule.
It is likely a Phase 5 ownership-shape drift problem.

## Locked planning rule

Do NOT patch runtime again until one ownership shape is chosen.

Approved target direction:
- one central Phase 5 selector
- service already locked before Phase 5
- objection type selects path
- output remains strictly inside locked service family
- no side authorities outside the chosen selector model

## Applies to
- GAP-TR-004
- Family A review context
- future Phase 5 patch planning
