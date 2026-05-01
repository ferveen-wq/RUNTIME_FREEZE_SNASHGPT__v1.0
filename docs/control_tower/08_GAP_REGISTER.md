# GAP REGISTER

## Status
ACTIVE MONITORED GAPS EXIST — updated 2026-04-30

## Current active / monitored gaps

### GAP-A — Phase3B deterministic stability not fully proven
Status: MONITORED
Evidence:
- Ceramic Phase3B price: 1x PASS on 2026-04-30
- Tint Phase3B price: 1x PASS on 2026-04-30
- Polishing Phase3B price: 1x PASS after Route E execution lock + runner guards on 2026-04-30
- PPF Phase3B front price: functional PASS on 2026-04-30 after strengthened anti-leak test

Reading:
- Functional Phase3B price coverage exists across PPF, Ceramic, Tint, Polishing.
- Not all services are marked 3x deterministic stable due to cost-control decision.

### GAP-B — Ceramic Phase5 debug phase-label determinism
Status: MONITORED / NOT PATCHING NOW
Evidence:
- selected_phrase_id reached PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1
- one determinism run emitted phase PHASE_4 instead of PHASE_5
Reading:
- Routing/phrase selection passed.
- Debug phase-label emission is the monitored instability.

### GAP-C — Project instruction independence
Status: OPEN
Reason:
- Runtime-only / project-instruction-free validation is not completed.

## Closed lanes still treated as resolved
- GAP-022 — Deferred-family routing residual drift
- Ceramic Phase 3A progression / wash-pattern progression
- Phase 5 PPF price-gap routing regression
- Phase 5 polishing expectation deepen regression
- Wrap ready-path wording contract issue
- ISSUE_016 Phase 4 first-objection boundary for PPF path

## Rule
- Do not reopen closed lanes without fresh failing active raw evidence.
- Future gaps must come from active rollout evidence, real validation drift, or production-confirmed mismatch.



GAP-021 — Phase3A interruption not executable
STATUS: REOPENED
ROOT_CAUSE:
- Qualification engine missing ignored qualifier detection
- Assembly patched before decision layer
IMPACT:
- Infinite qualifier loop on price push
