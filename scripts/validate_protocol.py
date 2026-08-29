#!/usr/bin/env python3
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'README.md','PROTOCOL.md','AMENDMENTS.md','RANDOMIZATION.md','METRICS_SCHEMA.md',
    'CASE_REGISTRY.csv','cases/P0_EIS.md','templates/CASE_REPORT.md',
    'templates/INDEPENDENT_GRADE.md','scripts/select_next_task.py','scripts/evaluator.py',
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
amendment=(ROOT/'AMENDMENTS.md').read_text()
assert 'ineligible to execute any prospective benchmark case' in amendment
assert 'not excluded from grading' in amendment
assert 'Standardized independent Codex CLI evaluation' in amendment
assert 'mid-benchmark procedural amendment' in amendment
assert 'GPT-5.6 Sol' in protocol and 'Amendment 1' in protocol
with (ROOT/'CASE_REGISTRY.csv').open(newline='') as fh:
    rows=list(csv.DictReader(fh))
p0=[r for r in rows if r['case_id']=='P0']
assert len(p0)==1 and p0[0]['phase']=='retrospective_pilot'
assert p0[0]['primary_endpoint_pass']=='0'
for r in rows:
    if r['phase']=='prospective':
        assert r['cue_timestamp_utc'] and r['first_pass_commit'], r['case_id']
print(f'PROTOCOL_VALIDATION_OK files=11 registry_cases={len(rows)} prospective_started={len([r for r in rows if r["phase"]=="prospective"])}')
