# P0 — EIS Equivalent-Circuit Analysis

## Classification

Retrospective protocol-forming pilot. This case is not part of the prospective primary sample.

## Evidence

- Task: `task_116_eis_equivalent_circuit_analysis`
- Public repository: https://github.com/mikhutchinson/frontierchallenge-eis-cleanroom
- Frozen graded commit: `c4ff684bfb2515e45736d232e274ba2fbaa194d8`
- Independent score: 89/100
- Material first-pass finding: unscaled `pinv(JᵀJ)` covariance produced invalid primary standard errors for poorly scaled parameters
- Primary endpoint under prospective rule: fail (one S2 finding)
- Scientific correction commit: `d85caadb75fbc71d44569862b376d7213e45f5ff`
- Citation-format follow-up: `f0e06e195e85f92989f969c62e426b0fbe0c907b`
- Corrected validation: 11 required outputs, 8 converged fits, 61 parameter rows, 508 fitted-spectrum rows, exact eight-artifact isolated rebuild match

## Why it is retained

P0 demonstrates feasibility, exposes a material autonomous-analysis failure, and motivates the prospective controls. It cannot establish consistency and will not be pooled as a prospectively registered success.
