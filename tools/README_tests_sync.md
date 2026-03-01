# Test Sync Helper (Wrapper Mirroring)

When you add cases to a dedicated suite (example):
- `tests/regression_ppf_matte_audit.json`

…mirror them into the wrapper pack:
- `tests/regression_cases_uat__ppf_matte_audit.json`

Run:

```bash
python tools/sync_cases_into_wrapper.py \
  --source tests/regression_ppf_matte_audit.json \
  --wrapper tests/regression_cases_uat__ppf_matte_audit.json
```

Dry-run:

```bash
python tools/sync_cases_into_wrapper.py \
  --source tests/regression_ppf_matte_audit.json \
  --wrapper tests/regression_cases_uat__ppf_matte_audit.json \
  --dry-run
```
