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
