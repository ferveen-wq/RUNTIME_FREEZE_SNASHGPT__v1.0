# tmp_active_cleanup

These packs were moved out of tests/uat because they are temporary or draft fixtures and should not remain in active UAT authority.

Reason:
- tmp_* naming indicates draft / scratch / temporary usage
- keeping them in tests/uat creates parallel or misleading active validation authority
- promotion should happen only after reclassification and stable naming

Promotion rule:
- rename out of tmp_* form
- define executable owner
- define validation method
- prove the pack is clean enough for active UAT inventory
