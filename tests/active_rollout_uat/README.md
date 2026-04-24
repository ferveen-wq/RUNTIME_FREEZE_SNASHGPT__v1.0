# Active Rollout UAT Surface

Purpose:
- This is the only active rollout UAT working folder.
- Use this for current smoke tests and rollout validation.
- Do not use old reports, tmp tests, backup UAT files, or deprecated probes as active evidence.

Rules:
- Runtime upload source: `00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime`
- Active test cases: `tests/active_rollout_uat`
- Active reports: `tests/active_rollout_uat/reports`
- Any old UAT file must be copied here only after classification.
