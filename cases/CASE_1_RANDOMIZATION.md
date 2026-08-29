# Case 1 — Randomization Evidence

Executed per RANDOMIZATION.md (frozen at e818baa74ff4f3df8de8d2ae53421588d3c9f398) at the
investigator's explicit start cue. This evidence was committed before the selected task's
instruction or input files were opened, downloaded, or read.

## Cue
- Cue received (UTC): **2026-08-29T18:19:56Z** (harness-reported receipt time; Sirius session
  row `started_at` matches exactly)
- First agent command executed: 2026-08-29T18:22:27.305Z

## Primary randomness source attempt — NIST Randomness Beacon 2.0
RANDOMIZATION.md requires the first beacon pulse generated strictly after the cue timestamp.
The beacon was queried 2026-08-29T18:26–18:41Z (raw responses committed under
`cases/evidence/beacon/`):

| Query | Result |
|---|---|
| `/beacon/2.0/pulse/last` | chain 2, pulse 1920967, timeStamp **2026-08-28T00:02:00.000Z** |
| `/beacon/2.0/chain/2/pulse/last` | identical (chain 2, pulse 1920967, 2026-08-28T00:02:00.000Z) |
| `/beacon/2.0/chain/2/pulse/1` (genesis) | 2022-09-21T19:32:00.000Z (period 60000 ms) |
| `/beacon/2.0/chain/2/pulse/1920970` (last+3) | 404 "Pulse Not Available." |
| `/beacon/2.0/chain/2/pulse/2070703` (index expected for 2026-08-29T18:35Z) | 404 "Pulse Not Available." |
| `/beacon/2.0/chain/3/pulse/last` | 404 "Pulse Not Available." (no chain 3 exists) |
| Re-confirmation at commit time (timestamped captures 18:40:48–49Z) | still 2026-08-28T00:02:00.000Z |

- Newest pulse available at cue: 2026-08-28T00:02:00Z → gap at cue = **42.30 hours** (> 24 h).
- No pulse exists strictly after the cue timestamp; the beacon had been unavailable for more
  than 24 hours at the moment randomization was due.

**Fallback trigger:** RANDOMIZATION.md — "If the beacon is unavailable for more than 24 hours,
use the first Bitcoin block hash published after the cue and apply the same modulus procedure."
The investigator's start-cue instruction (item 10) preauthorized exactly this fallback and
required that no other selection method be substituted silently.

Interpretation note (recorded for transparency): the frozen text was read as a present-state
condition (beacon unavailable > 24 h), which was already objectively true at the cue; the text
specifies no mandatory waiting period. The alternative reading (wait up to 24 h from the cue
before falling back) was considered and rejected because the >24 h unavailability state predates
the cue, is a verifiable present fact, and the investigator's instruction conditions the
fallback on that same state.

## Fallback randomness — first Bitcoin block published strictly after the cue
- Method: boundary search over block heights via two independent public Esplora-API providers;
  raw responses committed under `cases/evidence/bitcoin/`.
- Providers: `https://blockstream.info/api` and `https://mempool.space/api` (boundary blocks
  cross-checked; both providers returned identical hashes and timestamps).
- Boundary proof:
  - Previous block: height 964605, hash `00000000000000000000dead6c74d8ce695ceb5f66bbb3e77fa9f5288e8a7203`,
    time 2026-08-29T18:18:35Z (≤ cue)
  - **Selected block: height 964606, hash `00000000000000000000cf227ba8712abfadaf6d5f2e848ae2b4a7abba95f05f`,
    time 2026-08-29T18:20:49Z (> cue)** — first block published strictly after the cue
- Re-verified at commit time via `/block-height/964606` on both providers.

## Selection (same modulus procedure as the beacon path)
- Remaining candidates (lexicographic, N=5, zero-based):
  0. `316L_POTENTIODYNAMIC_POLARIZATION`
  1. `HARD_CARBON_GITT`
  2. `HZO_PUND`
  3. `NMC_CYCLING`
  4. `RRDE_ORR_SELECTIVITY`
- Randomness value: the selected block hash interpreted as a base-16 integer
  (RANDOMIZATION.md step 3–4).
- Frozen selector: `scripts/select_next_task.py`
  (sha256 `7736b753b0b6ac2aa05a3d93505891d89619a5a985234747fb5cf1a739eea11e`), invoked with
  `--beacon-hex 00000000000000000000cf227ba8712abfadaf6d5f2e848ae2b4a7abba95f05f` (no exclusions).
- Selector output (verbatim, also committed as `cases/evidence/bitcoin/SELECTOR_OUTPUT.txt`):
  ```text
  candidate_count=5
  index=0
  selected=316L_POTENTIODYNAMIC_POLARIZATION
  ```
- Independent recomputation: `int(hash,16) mod 5 = 0` → `316L_POTENTIODYNAMIC_POLARIZATION` (agrees).

## Selected candidate
**`316L_POTENTIODYNAMIC_POLARIZATION`** — public benchmark task identifier to be attached at
ingestion per RANDOMIZATION.md; attaching an identifier may not change the candidate's position
in the sorted list.

## Ordering statement
This file and the executor configuration were committed and pushed to origin before the selected
task's instruction or input files were opened, downloaded, or read. No task content was inspected
before this commit.
