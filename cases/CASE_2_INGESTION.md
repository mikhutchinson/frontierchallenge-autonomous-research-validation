# Case 2 — Task Ingestion Record
Committed after the randomization evidence (8c960361864cc3aec9f0235d8057667da7889303) and before
any analysis implementation.
## Selected task
- Candidate label: `RRDE_ORR_SELECTIVITY`
- Public benchmark task identifier (attached per RANDOMIZATION.md): **`task_042_rrde_orr_selectivity`**
- Registry metadata observed (public index only): difficulty=hard, domain=Electrochemistry,
  subdomain="Corrosion & electrocatalysis",
  source_task_sha256=29e4141220c591de97d706965afb93dd178870816b9428b3cb5319cf726dba19,
  verifier_commitment_sha256=c1bf6b18ff41e39c167d454af4751de75963cb4d68c08502c9f7f5487d8af0a2
  (commitment hash only; the verifier itself was never accessed, downloaded, or inspected)
## Public package source
- Dataset: https://huggingface.co/datasets/apodex/FrontierChallenge (ApodexAI)
- Package path: `tasks/task_042_rrde_orr_selectivity/` (instruction.md, task.json, task.toml,
  environment/{Dockerfile, env/{Dockerfile, requirements.txt},
  data/{README.md, README_input.md, acquisition_log.csv, analysis_config.json,
  electrode_metadata.csv, ferrocyanide_collection_calibration.csv,
  peroxide_transit_calibration.csv, rrde_raw_curves.csv}})
- Downloaded: 2026-08-29 ~20:20–20:22Z via huggingface.co resolve URLs
## Integrity verification
- 14/14 package files sha256-verified against the dataset's published `checksums.sha256`
  (verified_ok=14, mismatched=0, not_listed=0). First verification pass used task-relative paths
  and reported not_listed=14; re-run with full dataset paths verified all 14 files. No file was
  opened for content reading before verification completed.
- Visible-file manifest: `MANIFEST.sha256` in the clean-room workspace (covers all 14 files).
## Clean-room workspace
- Path: `/Users/mikhutchinsonstudio/Documents/Projects/frontierchallenge-rrde-orr-cleanroom`
- Fresh git repository (no shared history with any prior workspace).
- The Case 1 (316L) and EIS workspaces were not opened, reused, or modified.
## Contamination statement
- Opened materials: instruction.md, task.json, task.toml, environment/data/* (all agent-visible).
- Not accessed: any verifier, grader, scorer, reference output, expected-answer, or hidden-test
  material for this or any other task; the frontierchallenge-316l-polarization-cleanroom and
  frontierchallenge-eis-cleanroom repositories; prior session transcripts. `task.toml` contains
  public verifier *configuration metadata*; it discloses no expected results. No prior solutions
  to this task were sought or viewed.
