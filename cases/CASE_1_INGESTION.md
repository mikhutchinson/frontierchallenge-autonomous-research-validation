# Case 1 — Task Ingestion Record

Committed after the randomization evidence (254109c) and before any analysis implementation.
## Selected task
- Candidate label: `316L_POTENTIODYNAMIC_POLARIZATION`
- Public benchmark task identifier (attached per RANDOMIZATION.md): **`task_010_polarization_316l_corrosion`**
- Registry metadata observed (public index only): difficulty=hard, image=open, judge=true,
  source_task_sha256=92afc439267a507db7c4a0ff9cbbb5f951e5029fa025e1abd0d325b649804639,
  verifier_commitment_sha256=31a263f62531c13c4e16402910d6ff0ad53accb085fe64122fc12ce736b7e27f
  (commitment hash only; the verifier itself was never accessed, downloaded, or inspected)
## Public package source
- Dataset: https://huggingface.co/datasets/apodex/FrontierChallenge (ApodexAI)
- Package path: `tasks/task_010_polarization_316l_corrosion/` (instruction.md, task.json,
  task.toml, environment/{Dockerfile, env/Dockerfile, data/{metadata.csv, analysis_constants.json,
  README_input.md, curves/*.csv ×12}})
- Downloaded: 2026-08-29 ~18:44–18:46Z via huggingface.co resolve URLs
## Integrity verification
- 20/20 package files sha256-verified against the dataset's published `checksums.sha256`
  (verified_ok=20, mismatched=0, not_listed=0). One file (`task.toml`) failed on first download
  pass and was re-downloaded and verified before any task content was read.
- Visible-file manifest: `MANIFEST.sha256` in the clean-room workspace (covers all 20 files).
## Clean-room workspace
- Path: `/Users/mikhutchinsonstudio/Documents/Projects/frontierchallenge-316l-polarization-cleanroom`
- Fresh git repository (no shared history with any prior workspace); commits 3305582, 791ae0e.
- The EIS workspace was not opened, reused, or modified.
## Contamination statement
- Opened materials: instruction.md, task.json, task.toml, environment/data/* (all agent-visible).
- Not accessed: any verifier, grader, scorer, reference output, expected-answer, or hidden-test
  material for this or any other task; the frontierchallenge-eis-cleanroom repository; prior
  session transcripts. `task.toml` contains public verifier *configuration metadata*
  (JUDGE_MODEL name, timeouts); it was read as part of the package and discloses no expected
  results. No prior solutions to this task were sought or viewed.
