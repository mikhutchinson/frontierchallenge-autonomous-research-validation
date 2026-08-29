# Prospective Evaluation Protocol

**Protocol identifier:** ARAV-ECHEM-01  
**Version:** 1.1
**Status:** Frozen before prospective Case 1; Amendment 1 adopted
**Scope:** Public FrontierChallenge electrochemistry analysis tasks  

## 1. Research question

Can a fixed autonomous research-agent workflow repeatedly produce scientifically defensible, computationally reproducible analyses across heterogeneous electrochemistry tasks without access to graders, reference answers, rubrics, expected outputs, or evaluator-side artifacts?

## 2. Design

This is a prospective case series. The completed EIS analysis is designated retrospective pilot **P0** because it informed this protocol and therefore cannot count as prospective confirmatory evidence. Five remaining eligible electrochemistry tasks constitute the prospective series unless a task is unavailable or legally inaccessible; exclusions must be documented before any task content is inspected.

All eligible tasks will be reported. Failures, low scores, withdrawals, and protocol deviations may not be omitted from the registry.

## 3. Fixed research workflow

For every prospective case, the agent will:

1. Receive only the public agent-visible instruction and input files.
2. Establish a separate clean-room workspace and record hashes of all visible materials.
3. Avoid all graders, rubrics, verifier archives, reference outputs, expected values, and ground truth.
4. Use no subagents.
5. Inspect the task contract and input data before implementation.
6. Research only public scientific and software sources needed for methods or interpretation.
7. Implement the complete analysis and generate machine-readable results, figures, provenance, pinned dependencies, and one-command reproduction instructions.
8. Run an independent local validator that recomputes substantive numerical outputs rather than checking file existence alone.
9. Freeze and commit the first-pass submission before any external grade or scientific critique is revealed.
10. Obtain an independent evaluation of the frozen first pass.
11. Record all material errors and protocol deviations.
12. Permit one clearly separated correction cycle after evaluation, preserving the original commit and grade.
13. Rebuild the corrected output in a fresh environment and compare scientific-artifact hashes.

## 4. Agent and harness freeze

Under Amendment 1, GPT-5.6 Sol designed this protocol and is excluded from serving as the prospective executing research agent. A different LLM within the Sirius harness must execute the prospective cases. GPT-5.6 Sol may grade frozen submissions if its protocol-designer role is disclosed; such a grade is not labeled independent unless supplied by a separate qualified evaluator.

At the start of Case 1, the case record will capture the exact model identifier, harness/runtime version, system policy version when available, operating system, Python/runtime versions, enabled tools, and repository commit. Those fields become the reference configuration.

Later configuration changes are permitted only when required by infrastructure or safety. Every change must be recorded before the affected analysis proceeds and classified as:

- non-substantive infrastructure change;
- capability-affecting change; or
- protocol deviation.

Cases run under capability-affecting changes will be analyzed separately from the original fixed configuration.

## 5. Human role and intervention policy

The investigator may:

- provide the start cue and public task package;
- approve credential use;
- resolve access, licensing, or corrupted-input problems;
- request a pause for external reasons; and
- arrange independent grading after the first-pass freeze.

Before first-pass freeze, the investigator will not provide scientific interpretation, numerical targets, debugging guidance, preferred conclusions, hidden evaluation information, or selective hints. Any unplanned scientific intervention is recorded verbatim and the case is marked assisted.

The agent may ask only questions required to avoid unsafe action, identify missing public inputs, or resolve genuine contract ambiguity. Scientific uncertainty should be handled in the analysis rather than transferred to the investigator.

## 6. Clean-room and contamination controls

Prohibited before first-pass freeze:

- grader or scorer source code;
- grading rubrics not included in the public instruction;
- reference answers or expected output archives;
- prior solutions to the same task;
- evaluator logs or hidden tests;
- task-specific hints derived from any of the above.

Public documentation, primary literature, software documentation, and the supplied task materials are allowed. Every external source used for scientific claims must be cited inline and listed in the references.

## 7. Outcomes

### Primary outcome

A **first-pass scientifically valid case** has no independently identified material scientific error. A material error is severity S2 or S3 under `METRICS_SCHEMA.md` and includes any defect that invalidates a required quantitative field, materially changes model preference or a principal conclusion, or makes the analysis irreproducible.

### Secondary outcomes

- contract-compliance score;
- independent overall score;
- number of S0/S1/S2/S3 findings;
- exact clean-rebuild success;
- citation accuracy;
- first-pass convergence and artifact completeness;
- human scientific interventions before freeze;
- elapsed wall time and correction time;
- correction success after one evaluation cycle; and
- cross-task performance by analytical modality.

The EIS pilot would fail the prospective primary endpoint because its original uncertainty calculation contained an S2 material error, even though its central fits and most conclusions were valid.

## 8. Independent evaluation

The frozen first-pass commit must be evaluated without allowing the agent to alter it. The evaluator should receive the public task contract, first-pass repository, and scoring instructions, but not the agent's private chain of reasoning.

The evaluator should report:

- numeric score and scoring dimensions;
- reproducibility result;
- every substantive defect with evidence;
- severity classification proposal; and
- whether any principal conclusion changes.

Evaluator type, identity or system, conflicts, access to hidden materials, and whether agent provenance was blinded must be disclosed.

## 9. Statistical analysis

Results will be descriptive because the eligible series is small. The final report will provide:

- first-pass valid cases divided by all started eligible cases;
- a Wilson 95% confidence interval for that proportion;
- median and range of independent scores;
- total and per-case error severity counts;
- reproducibility success rate;
- assisted versus unassisted outcomes; and
- task-by-task narratives without pooling away failures.

No claim of general autonomous scientific competence will be made. Any conclusion will be bounded to the tested agent configuration, task family, tool environment, and evaluation procedure.

## 10. Stopping and exclusions

The intended prospective sample is all five remaining eligible electrochemistry tasks. The study may stop early only for:

- loss of legal access to the benchmark;
- inability to obtain required public inputs;
- permanent loss of the fixed agent configuration;
- an external safety or policy constraint; or
- investigator termination, which must be reported with the existing registry intact.

Poor performance is not a stopping or exclusion criterion.

## 11. Reporting and AI disclosure

Any resulting manuscript will distinguish the retrospective P0 pilot from prospective cases. It will report the autonomous agent's role in analysis, coding, execution, literature synthesis, validation, and drafting. The agent will not be listed as an author. Human authors must review the evidence and accept responsibility for the submitted work.

## 12. Start gate

Prospective Case 1 may begin only when all of the following are true:

- this protocol and Amendment 1 are committed to a public timestamped repository;
- the prospective executing LLM is not GPT-5.6 Sol and its configuration is recorded;
- the candidate set and deterministic randomization method are frozen;
- the registry contains only P0 and no prospective result;
- the validation script passes; and
- the investigator explicitly gives the start cue.
