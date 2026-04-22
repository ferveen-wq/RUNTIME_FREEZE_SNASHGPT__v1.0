# Probe Archive

Purpose:
Archive probe-only, temporary, forensic, or interim UAT packs so they do not remain mixed with active trusted-lane validation packs.

Rules:
- Files in this folder are NOT active rollout-truth packs.
- They may be useful for historical tracing, ownership forensics, or intermediate debugging.
- They must not be treated as current trusted validation unless explicitly re-promoted.
- Active validation packs must remain in tests/uat only when they are part of the current trusted testing surface.

Archived here on 2026-04-22:
- stage5_ppf_narrow_l2_state_probe_v1.json
- phase7_reentered_continue_probe_v1.json
- stage4_block16_price_entry_probe_v1.json
- stage5_ppf_narrow_l2_probe_v1.json
- stage5_polish_l1_probe_v1.json
- deferred_family_classification_probe_v1.json
- tmp_phase6_probe_tint.json
- stage4_block8_services_probe_v1.json
- tmp_phase6_probe_matrix.json
