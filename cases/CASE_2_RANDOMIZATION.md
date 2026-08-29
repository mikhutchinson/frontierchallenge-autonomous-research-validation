# Case 2 — Randomization Evidence
Executed per RANDOMIZATION.md at the investigator's explicit start cue ("set a goal to complete
case 2-5", received 2026-08-29T20:10:54Z). This evidence was committed before the selected task's
instruction or input files were opened, downloaded, or read.
## Cue
- Cue received (UTC): **2026-08-29T20:10:54Z** (harness-reported receipt time; Sirius session row
  `started_at` for session `7cc6d613-d8aa-4e4e-808b-ea89b835b6ff` matches exactly)
- First agent command executed: 2026-08-29T20:12:45Z
## Primary randomness source attempt — NIST Randomness Beacon 2.0
The beacon was re-probed at the cue using the same endpoints as Case 1 (raw responses committed
under `cases/evidence/beacon/case2/`, timestamped captures at 20:14:06Z):
| Query | Result |
|---|---|
| `/beacon/2.0/pulse/last` | chain 2, pulse **1920967**, timeStamp **2026-08-28T00:02:00.000Z** |
| `/beacon/2.0/chain/2/pulse/last` | identical |
| `/beacon/2.0/pulse/time/<now>` (20:12Z) | HTTP 404 "Pulse Not Available." |
| `/beacon/2.0/pulse/next`, `/pulse/previous`, `/chains` | HTTP 302 → CSRC project landing page |
- Newest pulse available at cue: unchanged since Case 1's gate → gap at cue = **68.15 hours** (> 24 h).
- No pulse exists strictly after the cue timestamp; beacon unavailability >24 h remains an
  objectively verifiable present state (same condition and interpretation note as Case 1).
**Fallback trigger:** RANDOMIZATION.md — first Bitcoin block hash published after the cue.
## Fallback randomness — first Bitcoin block published strictly after the cue
- Method: boundary search via two independent public Esplora-API providers; raw responses
  committed under `cases/evidence/bitcoin/case2/`.
- Providers: `https://mempool.space/api` and `https://blockstream.info/api` (identical hashes/times).
- Boundary proof:
  - Previous block: height **964614**, hash `000000000000000000000eb9bdacf7524d9bd606bd53ae60c1082534340879ea`,
    time **2026-08-29T20:07:07Z** (≤ cue)
  - **Selected block: height 964615, hash `000000000000000000011c6d5cb33aea5609420af8498970ae7443c883e35d27`,
    time 2026-08-29T20:15:42Z (> cue)** — first block published strictly after the cue;
    detected by background monitor at observed_at=2026-08-29T20:16:46Z and re-fetched from both providers.
## Selection (same modulus procedure as the beacon path)
- Remaining candidates (lexicographic, N=4, zero-based; Case 1's task excluded):
  0. `HARD_CARBON_GITT`
  1. `HZO_PUND`
  2. `NMC_CYCLING`
  3. `RRDE_ORR_SELECTIVITY`
- Randomness value: selected block hash interpreted as a base-16 integer (RANDOMIZATION.md steps 3–4).
- Frozen selector: `scripts/select_next_task.py`
  (sha256 `7736b753b0b6ac2aa05a3d93505891d89619a5a985234747fb5cf1a739eea11e`, verified before use),
  invoked with `--beacon-hex <selected block hash> --exclude 316L_POTENTIODYNAMIC_POLARIZATION`.
- Selector output (verbatim, also committed as `cases/evidence/bitcoin/case2/SELECTOR_OUTPUT.txt`):
    candidate_count=4
    index=3
    selected=RRDE_ORR_SELECTIVITY
- Independent recomputation: `int(hash,16) mod N = int(hash,16) mod N with N=4 → index=3` →
    RRDE_ORR_SELECTIVITY (agrees).
## Selected candidate
**`RRDE_ORR_SELECTIVITY`** — public benchmark task identifier to be attached at ingestion per
RANDOMIZATION.md; attaching an identifier may not change the candidate's position in the sorted list.
## Ordering statement
This file and the executor configuration (`cases/CASE_2_EXECUTOR_CONFIG.md`) were committed and pushed to origin before the selected task's instruction or input files were opened, downloaded, or read. No task content was inspected before this commit.
