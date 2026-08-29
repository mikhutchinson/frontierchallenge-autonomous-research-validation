# Case 1 — 316L Potentiodynamic Polarization Analysis

## Registration
- Phase: prospective
- Task label: `316L_POTENTIODYNAMIC_POLARIZATION`
- Task identifier: `task_010_polarization_316l_corrosion`
- Selection method: randomized — NIST Randomness Beacon unavailable >24 h at cue;
  documented Bitcoin-block fallback per RANDOMIZATION.md (`cases/CASE_1_RANDOMIZATION.md`)
- Cue timestamp UTC: 2026-08-29T18:19:56Z
- Randomness evidence: first block strictly after cue = height 964606,
  hash `00000000000000000000cf227ba8712abfadaf6d5f2e848ae2b4a7abba95f05f`
  @ 2026-08-29T18:20:49Z; dual-provider verified (blockstream.info, mempool.space);
  frozen selector `scripts/select_next_task.py` output index=0/5 → selected candidate.
- Agent model and harness: Sirius harness (`com.sirius.agent`); executing LLM
  `z-ai/glm-5.3-flash` via OpenRouter (`cases/CASE_1_EXECUTOR_CONFIG.md`; zero gpt% calls).
- Environment: macOS 26.5.2 arm64 (Apple M3 Ultra); Python 3.14.5 system;
  pinned fresh venv (numpy==2.5.2, pandas==3.0.5, matplotlib==3.11.1, pillow==12.3.0) for rebuild;
  git 2.52.0.

## Clean-room boundary
- Visible files and hashes: `MANIFEST.sha256` in the clean-room repository — all 20 package
  files sha256-matched against the dataset's published `checksums.sha256` before any content
  was read; one re-download (`task.toml`) documented in `cases/CASE_1_INGESTION.md`.
- Prohibited materials accessed: no (no verifier/grader/reference/hidden-test material; no EIS
  workspace; no prior-session transcripts; no prior solutions to this task).
- Public sources used (bibliographically verified via Crossref/publisher pages):
  Chemistry LibreTexts reference-electrode potentials; Tafel 1905 (Z. Phys. Chem. 50, 641);
  Stern & Geary 1957 (JES 104, 56); ASTM G102-89(2015)e1; Kong et al. 2019 (npj Mater. Degrad.
  3:24); Vukkum et al. 2022 (npj Mater. Degrad. 6:2).

## First-pass execution
- Workspace: `/Users/mikhutchinsonstudio/Documents/Projects/frontierchallenge-316l-polarization-cleanroom`
  — public mirror: https://github.com/mikhutchinson/frontierchallenge-316l-polarization-cleanroom
- Start timestamp (first task-content read): 2026-08-29T18:45Z
- Freeze timestamp: first-pass commit `eb324d0a14557f451a6af858d73124fd5d6a1537` pushed to origin
- First-pass commit: `eb324d0a14557f451a6af858d73124fd5d6a1537`
- Human scientific interventions before freeze: **0**
- Validator evidence: `validation/validate_outputs.py` — independent recomputation of every
  substantive output via separate code paths; **305 checks, 0 failures → PASS**
  (`validation/VALIDATION_RESULTS.json`).
- Clean rebuild evidence: `reproduction/fresh_env_rebuild.sh` — fresh pinned venv rebuilt from
  `requirements.txt`; analysis rerun into a temp directory; validator re-PASSed there; all six
  scientific artifacts **byte-identical** to committed outputs (`reproduction/REPRODUCTION_LOG.md`,
  run at 2026-08-29T19:05:11Z).

## Independent evaluation
- Evaluation 1 received: GPT-5.6 Sol protocol-designer grade, preserved verbatim at
  `cases/evaluations/CASE_1_GRADE_01_GPT56_SOL.md`.
- Reported score/verdict: **A+ — 98/100; PASS; no material scientific error identified.**
- Evaluator disclosure: GPT-5.6 Sol designed the protocol. Under Amendment 1 this is valid
  protocol-designer grading but **not an independent external evaluation** without an additional
  separate evaluator.
- Reported findings: all scientific calculations and required outputs correct; 305/305 validator
  checks and byte-identical rebuild confirmed; two minor reporting defects identified (transient
  spans two adjacent samples, not one; “836 samples” should read 836 points per curve / 10,032 total).
- S0/S1/S2/S3 adjudication: **deferred pending the remainder of the evaluation grades**. The
  evaluator proposed two minor reporting issues and no S2/S3-equivalent finding.
- Severity-classification supplement received from the same protocol-designer evaluator and
  preserved verbatim at `cases/evaluations/CASE_1_GRADE_01_GPT56_SOL_SEVERITY.md`:
  proposed **S0=1, S1=1, S2=0, S3=0** and evaluator-level `primary_endpoint_pass=1`.
- Frozen-commit verification of those findings (read-only, `eb324d0a`): all 12 curves contain
  exactly 836 points (10,032 total); `LPBF_AS_BUILT_R2` has exactly two pre-sustained samples above
  100 µA/cm² at 0.609 and 0.611 V SHE; independently recomputed Epit=0.724905993 V SHE. Both
  findings are accurate and do not affect Epit or any principal conclusion.
- Primary endpoint: **not yet finalized at study level**; the supplied determination is explicitly
  evaluator-level, and the complete intended evaluation set / independent evaluation remains pending.

## Correction cycle
- Correction commit: none (not started; permitted only after external evaluation)
- Corrected validation: pending
- Conclusions changed: pending

## Protocol deviations
None before freeze. One documented interpretation decision (recorded transparently in
`cases/CASE_1_RANDOMIZATION.md`, not classified as a deviation): the beacon-unavailability
fallback was triggered on the objectively verified >24 h outage state at cue time, per the
frozen text and the investigator's preauthorization (start-cue item 10). One non-substantive
infrastructure maintenance change to protocol tooling accompanies this freeze:
`scripts/validate_protocol.py` registry assertions were generalized to accept prospective rows
(P0 assertions unchanged) because instruction item 17 requires the registry row before grading;
classified per PROTOCOL.md §4 as a non-substantive infrastructure change, disclosed here and in
the commit message.
