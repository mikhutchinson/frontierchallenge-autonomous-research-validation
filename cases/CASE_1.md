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
- Complete reconciliation: `cases/evaluations/CASE_1_FINAL_ADJUDICATION.md`.
- Protocol-designer evaluator: GPT-5.6 Sol; 98/100 PASS; proposed S0=1/S1=1/S2=0/S3=0;
  not independent under Amendment 1; verbatim grade and severity supplement preserved.
- Independent evaluator: Codex CLI independent evaluator (reported model GPT-5), Codex CLI
  0.146.0, separate ephemeral process, blinded to prior grades, no hidden materials, no conflicts,
  history-free exact-commit snapshot, read-only filesystem and sandbox.
- Materials accessed: 49 frozen files covering the public contract/metadata, raw inputs, frozen
  code and outputs, both PNGs, validation/reproduction evidence, README, requirements, and manifest;
  exact paths/hashes are preserved in `cases/evaluations/CASE_1_CODEX_01/`.
- Independent score/verdict: **94/100 — PASS**; Codex proposed S0=0/S1=3/S2=0/S3=0 and
  evaluator-level `primary_endpoint_pass=1`; all endpoints independently recomputed within 4.94e-7.
- Final unique-finding adjudication (duplicate descriptions not summed): **S0=1, S1=3, S2=0,
  S3=0**. The duplicated sample-count wording is final S0 (GPT proposed S0; Codex F1 proposed S1)
  because it is editorial only; the severity disagreement is preserved. Final S1 findings are the
  two-sample transient description, unsupported cross-unit Epit/ipass comparison, and clipped
  high-current plot tails.
- Study-level primary endpoint: **PASS (`primary_endpoint_pass=1`)** — S2=S3=0, artifacts complete,
  fresh-environment reproduction passed, central values independently recomputed, and no
  undisclosed pre-freeze scientific assistance.

## Correction cycle
- Decision: **used the single permitted correction cycle**. It was not needed for endpoint passage,
  but Codex marked correction required and all verified S0/S1 defects were low-burden.
- Frozen first-pass commit (unchanged): `eb324d0a14557f451a6af858d73124fd5d6a1537`.
- Correction commit: `83a7aa14af6b5d4576f72c8a8f1f283ce237e0d9` (direct child of frozen commit).
- Corrections: clarified 836 points/curve and two-sample transient; removed the unsupported
  cross-unit comparison; dynamically expanded the polarization y-limit to 1e12 µA/cm².
- Correction burden: one cycle/one commit; approximately 2.6 minutes; three scientific-deliverable
  paths changed plus correction/reproduction records; no quantitative CSV or principal-result change.
- Corrected validation: 305 checks, 0 failures — PASS.
- Corrected clean rebuild: all six corrected scientific artifacts byte-identical — PASS.
- Conclusions changed: no.

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

Amendment 2 was adopted and publicly pushed after Case 1 first-pass freeze and the disclosed
protocol-designer grade, but before final adjudication and Case 2 randomization. It standardizes
the independent Codex CLI evaluation. This mid-benchmark procedural amendment did not change the
frozen first pass, task eligibility, randomization, executing model, S0–S3 definitions, primary
endpoint, or one-correction-cycle limit.
