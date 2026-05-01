# ACTIVE ROLLOUT BASELINE — 2026-05-01

Current rollout truth is:

00__ACTIVE_ROLLOUT_UPLOAD_SET

00__LOCKED__UPLOAD_SET is legacy/reference only.

Evidence zones:
- Zone 1: LOCKED upload set and old docs = historical evidence only.
- Zone 2: ACTIVE rollout before 2026-05-01 = useful active history, must be checked against current state.
- Zone 3: From 2026-05-01 onward = current truth, ACTIVE rollout only.

Workflow rule:
- Runtime patches target 00__ACTIVE_ROLLOUT_UPLOAD_SET.
- UAT uses tests/active_rollout_uat and runner/run_active_uat_raw.py.
- Governance must not create false confidence by validating locked-set files only.
- Codex must not read or patch 00__LOCKED__UPLOAD_SET unless explicitly asked for historical comparison.
- Runtime patches must be tracked in ARCH_CHANGELOG and validated against ACTIVE rollout files.
