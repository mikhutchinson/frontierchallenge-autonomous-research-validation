#!/usr/bin/env python3
"""Deterministically select a remaining task from recorded public randomness."""
from __future__ import annotations
import argparse

CANDIDATES = sorted([
    "316L_POTENTIODYNAMIC_POLARIZATION",
    "HARD_CARBON_GITT",
    "HZO_PUND",
    "NMC_CYCLING",
    "RRDE_ORR_SELECTIVITY",
])

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--beacon-hex", required=True)
    parser.add_argument("--exclude", action="append", default=[])
    args = parser.parse_args()
    value = args.beacon_hex.lower().removeprefix("0x")
    if not value or any(c not in "0123456789abcdef" for c in value):
        raise SystemExit("--beacon-hex must be a hexadecimal string")
    remaining = [x for x in CANDIDATES if x not in set(args.exclude)]
    if not remaining:
        raise SystemExit("no candidates remain")
    index = int(value, 16) % len(remaining)
    print(f"candidate_count={len(remaining)}")
    print(f"index={index}")
    print(f"selected={remaining[index]}")

if __name__ == "__main__":
    main()
