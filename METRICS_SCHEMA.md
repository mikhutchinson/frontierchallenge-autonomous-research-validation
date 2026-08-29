# Metrics and Error-Severity Schema

## Error severity

| Level | Definition | Examples |
|---|---|---|
| S0 | Editorial only; no scientific or reproducibility effect | Typo, formatting inconsistency |
| S1 | Minor scientific deficiency that does not alter a required result or principal conclusion | Missing qualification, weak citation placement |
| S2 | Material scientific error affecting a required field, important interpretation, model comparison, or uncertainty claim | Invalid standard errors, materially optimistic statistic without disclosure |
| S3 | Critical failure invalidating the analysis or making the principal result unusable | Wrong input sign, data leakage, fabricated source, irreproducible central result |

Severity is assigned independently after first-pass freeze. Disagreements are preserved and adjudicated transparently.

## Registry fields

- `case_id`
- `phase` (`retrospective_pilot` or `prospective`)
- `task_label`
- `task_identifier`
- `selection_method`
- `cue_timestamp_utc`
- `first_pass_commit`
- `first_pass_score`
- `s0_count` through `s3_count`
- `primary_endpoint_pass`
- `clean_rebuild_pass`
- `human_scientific_interventions`
- `correction_commit`
- `correction_validated`
- `status`
- `notes`

## Primary endpoint rule

`primary_endpoint_pass = 1` only if:

- S2 count is zero;
- S3 count is zero;
- required analysis artifacts are complete;
- the central results reproduce in a fresh environment; and
- no undisclosed scientific assistance occurred before first-pass freeze.
