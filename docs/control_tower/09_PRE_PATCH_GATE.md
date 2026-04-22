# 09 — PRE-PATCH GATE (ENFORCED)

## Purpose
This file is the mandatory gate before any new patch lane.

It does NOT replace earlier control-tower / governance / due-diligence docs.
It is the enforcement layer that makes those materials operational.

## Hard rules
1. No patch before evidence-gate output is pasted.
2. No tracker update before a real rerun is completed.
3. No commit before tracker truth matches the latest real rerun.
4. If worktree is dirty, inspect diff before patching.
5. Prefer the smallest proving pack before any broader rerun.
6. If broader rerun contradicts local rerun, broader rerun becomes source of truth.
7. Do not claim “resolved” from a probe pack if broader regression still fails.
8. Do not open a new patch lane until the current lane has:
   - latest failing evidence
   - patch target identified
   - smallest rerun result
   - broader rerun result
   - tracker truth aligned

## Mandatory order
For every patch lane, follow this order exactly:

### A. Evidence gate
Capture:
- current branch / head
- current worktree
- latest real failing report
- exact failing case definitions
- relevant control-tower truth
- recent runner / prompt commit history
- current dirty diff

### B. Patch
Only after A is pasted and reviewed.

### C. Small proving rerun
Run the smallest pack that proves the intended fix.

### D. Broader rerun
Run the nearest broader regression pack that can disprove false confidence.

### E. Tracker truth
Update control tower only after D is real and clean enough to support the claim.

### F. Commit
Commit only after tracker truth matches the latest real rerun.

## API / Credit Discipline
1. Do not run a new trace if the latest pasted evidence already isolates the failing lane.
2. Do not rerun the same pack unless code changed after the previous report.
3. Prefer the smallest unresolved proving pack before any broader rerun.
4. Reuse the latest valid gate output unless target lane, report source, or worktree changed.
5. If a broader rerun remains the source of truth, do not spend more runs on already-proven side lanes.
6. Before every new run, ask: what new information will this run produce that we do not already have?

## Stop conditions
Stop immediately if any of these happen:
- dirty worktree is ignored
- local probe passes but broader rerun fails
- tracker wording claims “clean” while report is not clean
- patch changes a lane outside the scoped evidence
- a case-specific tooling fix starts reopening other packs

## Current operating truth
- Deferred-family lane is not the active problem now.
- Phase 0–5 broader regression is clean.
- Latest real broader rerun:
  - tests/reports/uat_report_20260422_115835.json
  - result: 40/40 passed
- Phase 6 focused validation is also clean:
  - tests/reports/uat_report_20260422_121438.json
  - tests/reports/uat_report_20260422_121749.json
- Current status:
  - no active broader regression failure is open
  - no active gap is open
- Therefore:
  - do NOT open speculative patch lanes
  - use this gate only when fresh failing evidence appears
  - next work can proceed to controlled Phase 6 / rollout validation
