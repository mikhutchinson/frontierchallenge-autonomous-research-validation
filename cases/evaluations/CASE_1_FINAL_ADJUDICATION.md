# Case 1 — Final Evaluation Reconciliation and Study Adjudication

## Frozen evidence boundary
- Frozen first-pass commit: `eb324d0a14557f451a6af858d73124fd5d6a1537`
- Frozen tree: `0172a913ab794213017937e3d3365f3cd542c090`
- The first-pass commit was not amended.
- Amendment 2 was adopted after this freeze and after the protocol-designer grade, but before
  final adjudication and Case 2 randomization. It changed only the evaluator procedure.

## Evaluations

### GPT-5.6 Sol protocol-designer evaluation
- Preserved verbatim:
  - `CASE_1_GRADE_01_GPT56_SOL.md`
  - `CASE_1_GRADE_01_GPT56_SOL_SEVERITY.md`
- Score/verdict: 98/100, PASS.
- Proposed counts: S0=1, S1=1, S2=0, S3=0.
- Proposed endpoint: PASS.
- Role disclosure: GPT-5.6 Sol designed ARAV-ECHEM-01; this evaluation is valid disclosed
  protocol-designer evidence but is not independent under Amendment 1.

### Independent Codex CLI evaluation under Amendment 2
- Artifacts: `CASE_1_CODEX_01/` (grade JSON/Markdown, complete event stream, exact prompt,
  evidence manifest, run metadata, enforced schema).
- Evaluator: Codex CLI independent evaluator; model reported as GPT-5; Codex CLI 0.146.0;
  separate ephemeral process; no conflicts disclosed.
- Blinding: prior grades/evaluations not supplied; no hidden materials; history-free export of the
  exact frozen commit; filesystem and Codex sandbox read-only.
- Materials: 49 frozen evidence files comprising the public task contract/metadata, raw inputs,
  frozen implementation and outputs, both PNG figures, public validation/reproduction evidence,
  README, requirements, and input manifest. Exact paths and hashes are preserved in
  `grade.json`, `evidence_manifest.json`, and `run_metadata.json`.
- Runtime: started 2026-08-29T20:01:49.560449Z; completed 2026-08-29T20:03:20.340199Z;
  Codex exit code 0; standardized evaluator terminal result `EVALUATOR_OK`.
- Score/verdict: 94/100, PASS.
- Proposed counts: S0=0, S1=3, S2=0, S3=0.
- Proposed endpoint: PASS; correction required.
- Independent recomputation: every per-curve endpoint matched the frozen CSV after six-decimal
  rounding (maximum absolute discrepancy 4.94e-7).

## Unique-finding reconciliation

Evaluator descriptions of the same defect are not summed.

| Unique ID | Final severity | Finding | Evaluator proposals and reconciliation |
|---|---|---|---|
| U1 | S0 | “All 12 curves: 836 samples” is ambiguous; each curve has 836 points, 10,032 total. | GPT-5.6 Sol proposed S0; Codex F1 proposed S1. These are duplicate descriptions. Final S0 because the defect is purely editorial and both evaluators agree no calculation, required result, conclusion, or reproducibility is affected. Codex's S1 proposal is preserved as a severity disagreement. |
| U2 | S1 | LPBF_AS_BUILT_R2 was called a one-point transient although two adjacent points (0.609, 0.611 V SHE) exceed threshold before the sustained crossing. | GPT-5.6 Sol proposed S1; Codex did not separately report it. Direct verification confirms two points and unchanged Epit=0.724905993 V SHE. Minor scientific-description defect only. |
| U3 | S1 | The report's claim that conditions differ “far more” in Epit than ipass compares unlike units and is unsupported/directionally misleading on a relative scale. | Codex F2 proposed S1. Direct verification confirms Epit means span 1.83-fold while ipass means span 10.50-fold; all individual values and rankings remain correct. |
| U4 | S1 | The fixed 1e9 µA/cm² y-limit clips high-current tails in the polarization figure. | Codex F3 proposed S1. Direct verification finds six curves above 1e9 µA/cm²; required corrosion/passive/pitting regions remain legible and no numeric result changes. |

### Final first-pass severity counts
- **S0 = 1**
- **S1 = 3**
- **S2 = 0**
- **S3 = 0**

## Study-level primary endpoint

**PASS (`primary_endpoint_pass = 1`).** The frozen rule is satisfied:
1. final S2 count = 0;
2. final S3 count = 0;
3. all required artifacts are complete;
4. central results reproduced in a fresh pinned environment with all six artifacts byte-identical,
   and Codex independently recomputed all per-curve endpoints from raw inputs; and
5. human scientific interventions before freeze = 0, with no evidence of undisclosed assistance.

## Single correction-cycle decision and outcome

**Decision B — use the one permitted correction cycle.** Although no correction was necessary to
pass the primary endpoint, the independent Codex evaluator explicitly marked correction required,
and all four unique S0/S1 defects were low-burden reporting/visualization changes.

- Correction commit: `83a7aa14af6b5d4576f72c8a8f1f283ce237e0d9`
- Parent: frozen first pass `eb324d0a14557f451a6af858d73124fd5d6a1537`
- Commit time: 2026-08-29T20:05:54Z
- Burden: one cycle, one commit, approximately 2.6 minutes from independent evaluation completion;
  three corrected scientific-deliverable paths (`analysis.py`, report, polarization figure), plus
  a correction record and reproduction log.
- Central-result changes: none. All three quantitative CSVs and the corrosion-metrics figure retain
  their frozen hashes.
- Corrected validator: 305 checks, 0 failures — PASS.
- Corrected fresh rebuild: all six corrected scientific artifacts byte-identical — PASS.
- Corrected plot range: maximum |j| = 2.4411079e11 µA/cm²; deterministic y-limit = 1e12 µA/cm².
- Principal conclusions changed: no.

The correction commit is distinct and does not rewrite or replace the frozen first-pass commit.
