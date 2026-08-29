#!/usr/bin/env python3
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'README.md','PROTOCOL.md','RANDOMIZATION.md','METRICS_SCHEMA.md',
    'CASE_REGISTRY.csv','cases/P0_EIS.md','templates/CASE_REPORT.md',
    'templates/INDEPENDENT_GRADE.md','scripts/select_next_task.py',
]
missing=[x for x in required if not (ROOT/x).is_file()]
assert not missing, missing
protocol=(ROOT/'PROTOCOL.md').read_text()
for text in [
    'Primary outcome','Human role and intervention policy','Clean-room and contamination controls',
    'Statistical analysis','Stopping and exclusions','Start gate']:
    assert text.lower() in protocol.lower(), text
randomization=(ROOT/'RANDOMIZATION.md').read_text()
assert 'No randomization has been executed' in randomization
with (ROOT/'CASE_REGISTRY.csv').open(newline='') as fh:
    rows=list(csv.DictReader(fh))
assert len(rows)==1 and rows[0]['case_id']=='P0'
assert rows[0]['phase']=='retrospective_pilot'
assert rows[0]['primary_endpoint_pass']=='0'
print('PROTOCOL_VALIDATION_OK files=9 registry_cases=1 prospective_started=0')
