# Eligible Tasks and Randomization

## Prospective candidate set

The EIS equivalent-circuit task is excluded from randomization because it served as retrospective pilot P0 and informed the protocol.

The frozen prospective candidate labels are:

1. `316L_POTENTIODYNAMIC_POLARIZATION`
2. `HARD_CARBON_GITT`
3. `HZO_PUND`
4. `NMC_CYCLING`
5. `RRDE_ORR_SELECTIVITY`

Exact benchmark task identifiers will be attached when their public task packages are supplied. Attaching an identifier may not change the candidate's position in the sorted list.

## Selection method

At the investigator's start cue, use the first available NIST Randomness Beacon 2.0 pulse generated strictly after the cue timestamp.

1. Sort remaining candidate labels lexicographically.
2. Record the cue timestamp, beacon pulse timestamp, pulse URI, and `outputValue`.
3. Interpret `outputValue` as a base-16 integer.
4. Select index `integer mod N`, where `N` is the number of remaining candidates and indices are zero-based.
5. Commit the selection evidence before opening the selected task's instruction or input files.

If the beacon is unavailable for more than 24 hours, use the first Bitcoin block hash published after the cue and apply the same modulus procedure. The fallback and evidence must be recorded.

If the investigator directly selects a task instead, the case remains eligible but is labeled `investigator_selected`, not randomized.

**No randomization has been executed. The agent is standing by.**
