# MANUAL SIMULATION PROTOCOL — 2026-04-23

## Purpose
Create a controlled manual simulation lane for rollout-reality checking where runner/UAT evidence is unstable or harness-shaped.

## Why this exists
Current narrow PPF qualification-to-price behavior is not deterministic in the runner-tested lane.
Written contradiction audit is complete, but execution remains unstable.
Therefore manual simulation must be controlled, recorded, and separated from memory.

## Rules
- Use NEW chat for each simulation
- Paste only the approved runtime customer-assistant prompt
- Send customer messages one by one
- Do not explain, coach, or correct mid-simulation
- Stop immediately when a material drift appears
- Paste exact output back into control lane
- Record result before next simulation

## Scope
Current first target:
- PPF front-coverage qualification chain
- expected path:
  - coverage recognized
  - driving-pattern question asked
  - price only after required qualifier is present

## Do not do
- do not treat manual simulation alone as runtime closure
- do not reopen broad phase closure from one unstable lane
- do not patch further without recorded evidence
- do not mix multiple services in one simulation lane

## Current reading
- runner/UAT remains useful but not sufficient alone for this narrow path
- manual simulation is now the preferred reality-check lane for this issue family


## RESULT — PPF FRONT COVERAGE TEST (STEP 1)

Input:
ppf camry 2022 front

Observed:
- system asked coverage again

Expected:
- system should recognize FULL_FRONT
- system should ask driving pattern

Conclusion:
- confirmed failure in coverage capture
- not a random instability
- reproducible in manual simulation
- qualifies for targeted fix planning

