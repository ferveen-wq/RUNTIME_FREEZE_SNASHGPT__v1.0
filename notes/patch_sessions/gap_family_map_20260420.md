# Gap Family Map — 2026-04-20

## Family A — Phase 5 router / precedence / cross-service collapse
Treat as one defect family unless evidence proves different executable owners.

Members:
- GAP-031
- GAP-030
- GAP-029
- GAP-028
- GAP-TR-004
- GAP-TR-006

Shared pattern:
- non-PPF routing collapses into PPF
- service-family precedence instability
- polishing / ceramic leak into PPF authority
- prompt-bridge local fixes may improve one lane without being boundary-safe

Working rule:
- do not reopen each of these as isolated new defects unless owner/evidence differs

## Family B — Harness / test-contract / verbatim mismatch
Members:
- GAP-032
- GAP-025
- GAP-019
- GAP-021
- GAP-022
- GAP-024

Shared pattern:
- validated runner/harness lane
- failures may be contract/verbatim/body mismatch
- do not automatically classify as runtime-routing defects

## Family C — Phase/debug mismatch
Members:
- GAP-TR-005
- GAP-TR-007
- GAP-023
- GAP-024
- possible overlap with GAP-028 / GAP-027 / GAP-026

Shared pattern:
- selected phrase / phase / debug inconsistency
- likely separate from pure service-family router collapse

## Duplicate-authority risk
Relevant:
- GAP-029
- GAP-019

Interpretation:
- duplicate authority is a patching hazard
- not the main root family by itself
- avoid adding parallel authority blocks

## Control decision
From here:
- classify before patching
- do not work Family A members as if each is brand new
- keep runtime-owner defects separate from harness/test-contract defects
- keep phase/debug defects separate from router-precedence defects
