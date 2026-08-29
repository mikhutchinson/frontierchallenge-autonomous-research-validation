# Case 1 — Executor Configuration (Reference Configuration)

Recorded before randomization per PROTOCOL.md §4 and Amendment 1. These fields are the
reference configuration for ARAV-ECHEM-01 prospective Case 1 and are intended to remain
fixed across the prospective series.

## Recording
- Recorded: 2026-08-29 (~18:45Z), during the Case 1 start-cue turn, before any task content was opened
- Protocol repository commit at recording: e818baa74ff4f3df8de8d2ae53421588d3c9f398 (Amendment 1)

## Executing agent identity
- Agent harness: Sirius (macOS agent application, bundle id `com.sirius.agent`; `TERM_PROGRAM=sirius`)
- Executing LLM model identifier: **`z-ai/glm-5.3-flash`**, served via **OpenRouter** (`provider_id=openrouter`)
- Amendment 1 declaration: the executing LLM is **not** GPT-5.6 Sol. GPT-5.6 Sol designed this
  protocol and is ineligible to execute prospective cases under Amendment 1.

### Identity evidence (harness-side, queryable)
- Sirius session database (`~/.sirius/sirius.db`), table `sessions`, row for the Case 1 session:
  - `id = eb949864-94f3-4627-8bbb-24b552135a0d`
  - `started_at = 2026-08-29T18:19:56+00:00` (exactly the investigator's start-cue receipt time)
  - `model = z-ai/glm-5.3-flash`
- Table `model_call_stats` for that session id: 12 calls, all `provider_id=openrouter`,
  `model_id=z-ai/glm-5.3-flash`, `created_at` 2026-08-29 18:22:27 → 18:30:02 UTC (matching the
  live tool-call sequence of this session); count of `model_id LIKE 'gpt%'` = 0.
- Harness config file (`~/.sirius/config.toml`) contains a default `model = "gpt-5.6-sol"` field;
  it was **not used** for any call in this session (zero `gpt%` calls recorded). Disclosed for
  transparency; the session-level OpenRouter model override was active throughout.

## Runtime environment
- OS: macOS 26.5.2 (Build 25F84), arm64, Apple M3 Ultra (Mac15,14, 256 GB RAM)
- Python: 3.14.5 (Homebrew `/opt/homebrew/Cellar/python@3.14`); Sirius bundled Python.framework 3.13
- git: 2.52.0; shell: zsh
- Investigator timezone: America/Detroit; all evidence timestamps in UTC

## Enabled tools (Sirius harness)
api_request, bash, browser_use_* (open/find/click/eval/observe/transaction/type/probe_reachability),
computer_use_* (observe/observe_desktop/click_element/click_point/edit_text/launch_app/press/
quit_app/screenshot/select_menu_item/set_value/transaction/type/activate_app), credential broker
(credential_request/status/diagnose), memory, read_attachment, session_search, spotlight_search,
tool_search, wallet_status, goal, web_read, web_search, write_file/edit_file/read_file/glob/grep,
execute_dag, dynamic_ui, skills system, apple_* integrations. Subagents are prohibited by the
protocol and were not used.

## Fixed-configuration statement
Per PROTOCOL.md §4, this configuration is the reference configuration for the prospective series.
Any later change will be recorded before affected analysis proceeds and classified as a
non-substantive infrastructure change, a capability-affecting change, or a protocol deviation.
