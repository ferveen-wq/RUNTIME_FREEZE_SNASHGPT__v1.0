# PATCH GATE RULES

Before patching any locked runtime file, confirm all items below.

1. File role confirmed
- runtime authority / control tower / tooling / test

2. Raw defect proven
- failing report snippet captured
- raw output captured
- debug block captured

3. Tooling ruled out
- runner injection/normalization checked
- prompt-level forcing checked
- test helper behavior checked

4. Duplicate authority check done
- searched phrase id / signal / route / parameter across runtime, runner, tests

5. Strong failing test exists first
- strict test fails before patch
- failure reason matches intended defect

6. Narrowest patch target chosen
- prefer test or tooling fix before runtime doctrine fix

7. Validation defined before patch
- exact pack to run
- nearby smoke pack
- lint/integrity if needed

Hard rule:
If any item above is missing, do not patch locked runtime files.
