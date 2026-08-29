# Protocol Amendments

## Amendment 1 — Separation of protocol designer and prospective executor

**Timing:** Adopted after protocol v1.0 was publicly frozen and before randomization or prospective Case 1.  
**Prospective cases started at adoption:** 0  
**Reason:** Prevent the model that designed the evaluation protocol from also serving as the prospective test-taking research agent.

### Amendment

GPT-5.6 Sol, operating within the Sirius harness, designed and drafted protocol ARAV-ECHEM-01 and its validation materials. That model configuration is **ineligible to execute any prospective benchmark case** in this study.

A different LLM, operating inside the Sirius harness, will serve as the prospective executing research agent. Before randomization, its first case record must capture its exact model identifier and available harness/runtime configuration. That executing model should remain fixed across the prospective series; any replacement or capability-affecting configuration change must be documented and analyzed as a separate configuration under the existing protocol rules.

GPT-5.6 Sol is not excluded from grading. It may evaluate a frozen first-pass submission, reproduce results, classify defects, and assess protocol compliance. Any such evaluation must disclose that the grader designed the protocol. It must not be described as evaluator-independent on that basis alone. A human or separate model that neither designed the protocol nor executed the case may provide an additional independent grade when available.

The executing LLM must not receive the protocol-design session transcript, GPT-5.6 Sol's private reasoning, or task-specific analysis from the EIS pilot. It may read the public protocol repository and the selected public task package.

### Effect on interpretation

Prospective results will validate the named executing LLM–Sirius configuration under this protocol. They will not validate GPT-5.6 Sol as the executing agent and will not establish general autonomous-science competence.

## Amendment 2 — Standardized independent Codex CLI evaluation

**Timing:** Adopted after protocol v1.1, after prospective Case 1 was frozen and received a protocol-designer evaluation, and before Case 1 final adjudication or any Case 2 randomization.
**Prospective cases started at adoption:** 1
**Reason:** Replace ad hoc evaluator handoff with a reproducible, blinded, permission-constrained procedure for obtaining an additional grade from a separate model that neither designed the protocol nor executed the case.

### Amendment

The study may use `scripts/evaluator.py` to obtain an independent model grade after a first-pass commit has been frozen and published. The script invokes the local **Codex CLI directly**, not the Sirius subagent-dispatch tool. It must:

1. resolve and record the exact immutable first-pass commit;
2. export that commit into a disposable, history-free evidence snapshot so later corrections and prior evaluations are not visible;
3. pass only the public task contract, frozen inputs, implementation, outputs, public validation/reproduction evidence, and the frozen `METRICS_SCHEMA.md` definitions;
4. exclude prior grades, evaluator findings, hidden benchmark materials, private reasoning, and correction history;
5. run Codex as an ephemeral separate process under the CLI's `read-only` sandbox, with the evidence snapshot also made filesystem-read-only;
6. attach required PNG figures for direct visual review;
7. require structured output containing score, findings, S0–S3 counts, principal-result effects, reproducibility assessment, and evaluator-level primary-endpoint recommendation; and
8. preserve the exact prompt, Codex event stream, evidence hashes, runtime metadata, structured grade, and rendered report.

The evaluator must remain a separate model that neither designed ARAV-ECHEM-01 nor executed the prospective case. Launching the process from the same host or through a parent Sirius session does not by itself defeat role independence, but orchestration, model identity when available, CLI version, conflicts, blinding, and accessed materials must be disclosed.

This procedure may be applied to the already-frozen Case 1 because it cannot influence the first-pass artifact. It applies prospectively to subsequent frozen cases unless superseded by a later documented amendment. The executing agent remains prohibited from seeing any evaluation before its first-pass freeze.

### Effect on interpretation

This is a **mid-benchmark procedural amendment**. It does not change task eligibility or randomization, the frozen S0–S3 definitions, the primary endpoint, the one-correction-cycle limit, the executing model configuration, or any frozen first-pass result. Automated Codex output is evaluator evidence, not automatic study-level adjudication: disagreements among evaluators must still be preserved and reconciled transparently in the case record.
