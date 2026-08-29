# Prospective Validation of an Autonomous Research Agent

A preregistered, scorer-blind case series testing whether a fixed autonomous-agent configuration can repeatedly produce scientifically defensible and computationally reproducible analyses across heterogeneous electrochemistry tasks.

This repository contains the **study protocol and audit record**, not the scientific outputs for individual tasks. Each selected task is executed in a separate clean-room repository.

## Study status

| Item | Current state |
|---|---|
| Protocol | ARAV-ECHEM-01 v1.1, publicly frozen before Case 1 |
| Retrospective pilot | P0 — EIS equivalent-circuit analysis; protocol-forming and not confirmatory |
| Prospective series | 1 of 5 cases started; no prospective result yet |
| Case 1 | `task_010_polarization_316l_corrosion` — first pass frozen at `eb324d0a14557f451a6af858d73124fd5d6a1537`; awaiting external evaluation |
| Executing configuration | Sirius with `z-ai/glm-5.3-flash` via OpenRouter |
| Protocol designer | GPT-5.6 Sol; excluded from prospective execution under Amendment 1 |
| First-pass evaluation | Pending; the frozen submission is ready for independent grading |

### Case 1 checkpoint

The randomized selection and task ingestion have been committed publicly before scientific analysis:

- [Executor configuration](cases/CASE_1_EXECUTOR_CONFIG.md)
- [Randomization evidence](cases/CASE_1_RANDOMIZATION.md)
- [Task-ingestion record](cases/CASE_1_INGESTION.md)
- Selected candidate: **316L potentiodynamic polarization**
- Public task identifier: **`task_010_polarization_316l_corrosion`**
- Scientific outputs are being developed in a separate clean-room task repository

The primary NIST Randomness Beacon was more than 24 hours stale at the start cue, so the frozen Bitcoin-block fallback was used. The first block strictly after the cue selected candidate index 0. Full boundary evidence and independent modulus recomputation are preserved in the randomization record.

## Research question

> Can a fixed autonomous research-agent workflow repeatedly produce scientifically defensible, computationally reproducible analyses without access to graders, reference answers, rubrics, expected outputs, or evaluator-side artifacts?

The study is deliberately narrow. Any eventual conclusion will apply only to the tested model–harness configuration, electrochemistry task family, tool environment, and evaluation procedure. It will not establish general autonomous-science competence.

## Prospective design

The completed EIS analysis is retained as retrospective pilot **P0** because it informed the protocol. It cannot count as prospective confirmatory evidence. The prospective sample comprises all five remaining eligible electrochemistry tasks:

1. 316L potentiodynamic polarization
2. Hard-carbon GITT
3. HZO PUND
4. NMC cycling
5. RRDE ORR selectivity

Tasks are selected from the frozen set using public randomness. Poor performance is not a stopping or exclusion criterion, and all started cases—including failures and protocol deviations—remain in the registry.

For each case, the executing agent must:

1. Record the exact model and harness configuration before task access.
2. Commit public randomization evidence before opening the selected task package.
3. Work only from public agent-visible instructions, inputs, literature, and software documentation.
4. Use no subagents and access no grader, rubric, verifier, reference output, hidden test, or prior solution.
5. Build a separate clean-room workspace with visible-file hashes and provenance.
6. Produce code, machine-readable results, figures, uncertainty analysis, inline citations, pinned dependencies, and one-command reproduction instructions.
7. Run an independent validator that recomputes substantive outputs.
8. Rebuild in a fresh environment and compare scientific-artifact hashes.
9. Freeze and publish the first-pass commit before any evaluation is revealed.
10. Preserve the original result and permit at most one separately committed correction cycle.

## Primary endpoint

A prospective first pass succeeds only when all of the following hold:

- no independently identified **S2** or **S3** scientific error;
- all required analysis artifacts are complete;
- central results reproduce in a fresh environment; and
- no undisclosed human scientific assistance occurred before first-pass freeze.

Error severity is defined in [METRICS_SCHEMA.md](METRICS_SCHEMA.md):

- **S0:** editorial only;
- **S1:** minor scientific deficiency without a material result change;
- **S2:** material error affecting a required field, important interpretation, model comparison, or uncertainty claim;
- **S3:** critical failure invalidating the analysis or principal result.

P0 would fail this prospective endpoint because its original uncertainty calculation contained one S2 error. That failure is retained as part of the evidence rather than rewritten as a success.

## Role separation

Amendment 1 separates protocol design, execution, and evaluation:

- **GPT-5.6 Sol** designed the protocol and is ineligible to execute prospective cases.
- **`z-ai/glm-5.3-flash` inside Sirius** is the frozen prospective executing configuration.
- GPT-5.6 Sol may grade a frozen submission if its designer role is disclosed, but that grade is not described as evaluator-independent by itself.
- A human or separate model that neither designed the protocol nor executed the case may provide an additional independent grade.

See [AMENDMENTS.md](AMENDMENTS.md) for the controlling language.

## Repository map

| Path | Purpose |
|---|---|
| [PROTOCOL.md](PROTOCOL.md) | Frozen design, intervention rules, outcomes, analysis plan, and stopping rules |
| [AMENDMENTS.md](AMENDMENTS.md) | Prospective amendments with timing and rationale |
| [RANDOMIZATION.md](RANDOMIZATION.md) | Eligible task set and deterministic public-randomness procedure |
| [METRICS_SCHEMA.md](METRICS_SCHEMA.md) | Primary endpoint, registry fields, and S0–S3 severity definitions |
| [CASE_REGISTRY.csv](CASE_REGISTRY.csv) | Append-only case-level outcome registry |
| [`cases/`](cases/) | Timestamped configuration, randomization, ingestion, and case evidence |
| [cases/P0_EIS.md](cases/P0_EIS.md) | Retrospective pilot record and original material defect |
| [`templates/`](templates/) | Case-report and independent-grade templates |
| [`scripts/`](scripts/) | Frozen selector and protocol validator |

## Validate the protocol repository

```bash
python3 scripts/validate_protocol.py
```

Expected status at the current checkpoint:

```text
PROTOCOL_VALIDATION_OK files=10 registry_cases=1 prospective_started=0
```

The validator’s registry count remains one until the frozen Case 1 first-pass record is added. Case 1 configuration and ingestion evidence are already committed under `cases/`.

## Reporting commitments

Any resulting manuscript will:

- distinguish P0 from the prospective series;
- report every started case and first-pass failure;
- disclose model, harness, human intervention, and evaluator roles;
- report first-pass validity, correction burden, reproducibility, and severity counts separately;
- include a Wilson 95% confidence interval for the material-error-free first-pass proportion; and
- disclose significant generative-AI involvement in analysis, coding, execution, literature synthesis, validation, and drafting.

The autonomous system will not be listed as an author. Any human author must review the evidence and accept responsibility for the submitted work.
