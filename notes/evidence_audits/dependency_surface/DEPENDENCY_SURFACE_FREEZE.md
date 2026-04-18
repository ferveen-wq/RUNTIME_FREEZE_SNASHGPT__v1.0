# DEPENDENCY SURFACE FREEZE

Status: IN_PROGRESS

## Classification rules
- MANIFEST_ACTIVE = explicitly loaded in RUNTIME_LOAD_MANIFEST.md
- INDIRECTLY_CONSUMED = not manifest-loaded, but referenced by runtime/engines
- PRESENT_NOT_PROVEN = exists in repo, but runtime consumption not proven

## Targets
- GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
- GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
- SKU_SELECTION_MATRIX.md
- PRICE_TABLE_VAT_INCL.md
- GLOBAL_CORE_CONTEXT_PARAMETERS.md
- CONVERSATION_DYNAMIC_PARAMETERS.md
- PHASE6__SERVICE_CANON_BUNDLE.md
- PRODUCT_SERVICE_CANON.md



## Initial classification (current evidence)

### MANIFEST_ACTIVE
- GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
- GLOBAL_CORE_CONTEXT_PARAMETERS.md
- CONVERSATION_DYNAMIC_PARAMETERS.md
- SKU_SELECTION_MATRIX.md
- PRICE_TABLE_VAT_INCL.md
- PHASE6__SERVICE_CANON_BUNDLE.md

### INDIRECTLY_CONSUMED
- GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
- PRODUCT_SERVICE_CANON.md

### PRESENT_NOT_PROVEN
- Any repo/support file not explicitly loaded in manifest and not yet shown as runtime-consumed

## Notes
- Phase 6 confusion happened because manifest-active runtime truth was later described like support-only material.
- PRODUCT_SERVICE_CANON.md is referenced, but current evidence does not show it as manifest-active.
- GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md historically appeared in manifest, but current live manifest must remain the source of truth unless runtime restoration is explicitly chosen.
