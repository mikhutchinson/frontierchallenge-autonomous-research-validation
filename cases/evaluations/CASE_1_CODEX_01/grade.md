# Independent Codex Evaluation — CASE_1

- Frozen commit: `eb324d0a14557f451a6af858d73124fd5d6a1537`
- Evaluator system: Codex CLI independent evaluator
- Evaluator model: GPT-5
- Codex CLI: `codex-cli 0.146.0`
- Separate process: yes
- Blinded to prior grades: yes
- Hidden materials accessed: no

## Grade: 94/100 — PASS

**Evaluator-level `primary_endpoint_pass = 1`**

## Severity counts

| S0 | S1 | S2 | S3 |
|---:|---:|---:|---:|
| 0 | 3 | 0 | 0 |

## Findings

### F1 — S1: QC report understates the total number of raw samples

output/corrosion_report.md:69 says “All 12 curves: 836 samples,” but every raw curve has 836 data rows (837 lines including its header), for 10,032 observations across 12 curves. The intended statement was evidently 836 samples per curve. This does not affect any calculation.

- Required result affected: no
- Principal conclusion affected: no

### F2 — S1: Cross-metric claim about condition differences is unsupported and directionally misleading on a relative scale

output/corrosion_report.md:133-135 claims the surfaces differ “far more” in pitting potentials than passive current densities. The reported means span 0.5642–1.0323 V for Epit (1.83-fold) but 0.570–5.983 µA/cm² for ipass (10.5-fold). Comparing raw spreads across different units is not meaningful, while the relative spread gives the opposite impression. The individual values and resistance rankings remain correct.

- Required result affected: no
- Principal conclusion affected: no

### F3 — S1: Polarization figure clips high-current portions of several supplied curves

output/analysis.py:329 fixes the semilog limit at 1e9 µA/cm². In the attached polarization_curves.png, the blue and red curves visibly run into and beyond the upper frame, so their high-current endpoints are not shown. Axes, units, threshold, condition colors, replicate styles, and the scientifically important corrosion/passive/pitting regions remain legible.

- Required result affected: no
- Principal conclusion affected: no

## Reproducibility

Using a separate read-only Python calculation based directly on metadata.csv, analysis_constants.json, and all 12 raw curves, I independently recomputed the SHE conversion, area normalization, zero crossing, two OLS Tafel fits, line intersection, beta values, corrosion rate, sustained-threshold Epit, and grouped means/sample SDs. All per-curve values agreed with the delivered CSV after six-decimal rounding; maximum absolute CSV discrepancy was 4.94e-7. Independently obtained group means included icorr=0.719279, 0.322716, 0.133741, and 0.056864 µA/cm² and Epit=0.564182, 0.717560, 0.885609, and 1.032255 V SHE in the reported condition order. The snapshot is read-only, so I did not execute the artifact-producing fresh-environment workflow. The preserved reproduction log reports a newly created pinned virtual environment, 305 validator checks, and byte-identical hashes for all six scientific artifacts. Inspection of the bundled validator shows that it reimplements the calculations rather than importing analysis.py, although its PASS alone was not treated as proof.

- Central results independently recomputed: yes
- Fresh environment rerun by evaluator: no

## Overall determination

The analysis is scientifically sound and complete. Independent recomputation confirms the Tafel parameters, corrosion rates, sustained-threshold pitting potentials—including rejection of the LPBF_AS_BUILT_R2 transient—and sample statistics. Both required figures are readable and scientifically interpretable, though the polarization plot clips some high-current tails. Corrections are limited to two report statements and the plot ceiling; no required result or principal conclusion changes.

**Primary-endpoint rationale:** There are no S2 or S3 findings; all required artifacts are present; central numerical results independently reproduce from raw inputs; preserved fresh-environment evidence is specific and internally consistent; and the disclosed autonomous pre-freeze provenance contains no evidence of undisclosed scientific assistance. The three findings are minor reporting/visualization deficiencies only.

**Correction required:** yes

## Audit artifacts

- `grade.json` — schema-constrained evaluator output
- `codex_events.jsonl` — complete Codex CLI event stream
- `prompt.txt` — exact blinded evaluation prompt
- `evidence_manifest.json` — hashes of the frozen evidence snapshot
- `run_metadata.json` — invocation and environment metadata
- `evaluation.schema.json` — enforced output schema
