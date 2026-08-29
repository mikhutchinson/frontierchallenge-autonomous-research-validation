# Case 2 — Executor Configuration
Recorded before randomization per PROTOCOL.md §4 and Amendment 1.
## Recording
- Recorded: 2026-08-29 (~20:16Z), during the Case 2 start-cue turn, before any task content was opened
- Protocol repository commit at recording time base: 0af4aee5c30de6f3d61fdbe8c1e86fc9d6a6d8fe (Case 1 final adjudication)
## Executing agent identity
- Agent harness: Sirius (macOS agent application, bundle id `com.sirius.agent`; `TERM_PROGRAM=sirius`)
- Executing LLM model identifier: **`z-ai/glm-5.3-flash`**, served via **OpenRouter** (`provider_id=openrouter`)
- Amendment 1 declaration: the executing LLM is **not** GPT-5.6 Sol. GPT-5.6 Sol designed this
  protocol and is ineligible to execute prospective cases under Amendment 1.
### Identity evidence (harness-side, queryable)
- Sirius session database (`~/.sirius/sirius.db`), table `sessions`, row for the Case 2 session:
  - `id = 7cc6d613-d8aa-4e4e-808b-ea89b835b6ff`
  - `started_at = 2026-08-29T20:10:54+00:00` (the investigator's start-cue receipt time; used as
    the Case 2 cue timestamp for randomization)
  - `model = z-ai/glm-5.3-flash`
- Table `model_call_stats` for that session id (queried ~20:16Z): all calls
  `provider_id=openrouter`, `model_id=z-ai/glm-5.3-flash`; count of `model_id LIKE 'gpt%'` = 0.
### Fixed-series statement
This is the same executing configuration as prospective Case 1 (`z-ai/glm-5.3-flash` via
OpenRouter inside Sirius): the reference configuration remains fixed across the series per
Amendment 1 and PROTOCOL.md §4.
## Runtime environment
Same host and runtime family as recorded for Case 1 (`cases/CASE_1_EXECUTOR_CONFIG.md`):
macOS 26.5.2 arm64, Apple M3 Ultra (Mac15,14, 256 GB RAM), Homebrew Python (/opt/homebrew),
git shell zsh; investigator timezone America/Detroit; all evidence timestamps in UTC.
## Fixed-configuration statement
No capability-affecting configuration change has occurred between Case 1 and Case 2. Any later
change will be recorded before affected analysis proceeds and classified per PROTOCOL.md §4.
