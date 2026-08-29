#!/usr/bin/env python3
"""Run a blinded, read-only Codex CLI evaluation of a frozen submission.

The script exports exactly one Git commit into a disposable history-free snapshot,
locks the snapshot read-only, invokes ``codex exec`` directly, and preserves the
prompt, evidence hashes, CLI event stream, structured grade, and rendered report.
It never uses the Sirius subagent-dispatch surface.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROTOCOL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = "package/instruction.md"
SEVERITIES = ("S0", "S1", "S2", "S3")

GRADE_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": False,
    "required": [
        "reviewer", "score", "verdict", "artifact_complete", "reproducibility",
        "findings", "severity_counts", "principal_conclusion_changes",
        "required_result_changes", "primary_endpoint_pass",
        "primary_endpoint_rationale", "correction_required", "overall_summary",
    ],
    "properties": {
        "reviewer": {
            "type": "object", "additionalProperties": False,
            "required": [
                "system", "model", "separate_process", "blinded_to_prior_grades",
                "conflicts", "hidden_materials_accessed", "materials_accessed",
            ],
            "properties": {
                "system": {"type": "string"},
                "model": {"type": "string"},
                "separate_process": {"type": "boolean"},
                "blinded_to_prior_grades": {"type": "boolean"},
                "conflicts": {"type": "array", "items": {"type": "string"}},
                "hidden_materials_accessed": {"type": "boolean"},
                "materials_accessed": {"type": "array", "items": {"type": "string"}},
            },
        },
        "score": {"type": "integer", "minimum": 0, "maximum": 100},
        "verdict": {"type": "string", "enum": ["PASS", "FAIL"]},
        "artifact_complete": {"type": "boolean"},
        "reproducibility": {
            "type": "object", "additionalProperties": False,
            "required": ["central_results_recomputed", "fresh_environment_rerun", "assessment"],
            "properties": {
                "central_results_recomputed": {"type": "boolean"},
                "fresh_environment_rerun": {"type": "boolean"},
                "assessment": {"type": "string"},
            },
        },
        "findings": {
            "type": "array",
            "items": {
                "type": "object", "additionalProperties": False,
                "required": [
                    "id", "severity", "title", "evidence",
                    "required_result_affected", "principal_conclusion_affected",
                ],
                "properties": {
                    "id": {"type": "string"},
                    "severity": {"type": "string", "enum": list(SEVERITIES)},
                    "title": {"type": "string"},
                    "evidence": {"type": "string"},
                    "required_result_affected": {"type": "boolean"},
                    "principal_conclusion_affected": {"type": "boolean"},
                },
            },
        },
        "severity_counts": {
            "type": "object", "additionalProperties": False,
            "required": list(SEVERITIES),
            "properties": {s: {"type": "integer", "minimum": 0} for s in SEVERITIES},
        },
        "principal_conclusion_changes": {"type": "boolean"},
        "required_result_changes": {"type": "boolean"},
        "primary_endpoint_pass": {"type": "integer", "enum": [0, 1]},
        "primary_endpoint_rationale": {"type": "string"},
        "correction_required": {"type": "boolean"},
        "overall_summary": {"type": "string"},
    },
}


def run_checked(args: list[str], *, cwd: Path | None = None) -> str:
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"command failed ({result.returncode}): {' '.join(args)}\n{detail}")
    return result.stdout.strip()


def path_is_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def resolve_commit(repo: Path, revision: str) -> str:
    commit = run_checked(["git", "-C", str(repo), "rev-parse", "--verify", f"{revision}^{{commit}}"])
    if len(commit) != 40 or any(c not in "0123456789abcdef" for c in commit.lower()):
        raise RuntimeError(f"unexpected resolved commit: {commit!r}")
    return commit.lower()


def safe_extract_tar(tar_path: Path, destination: Path) -> None:
    root = destination.resolve()
    with tarfile.open(tar_path, "r") as archive:
        for member in archive.getmembers():
            target = (destination / member.name).resolve()
            try:
                target.relative_to(root)
            except ValueError as exc:
                raise RuntimeError(f"unsafe archive member: {member.name}") from exc
            if member.issym() or member.islnk():
                raise RuntimeError(f"links are not allowed in evidence snapshot: {member.name}")
        archive.extractall(destination)


def export_snapshot(repo: Path, commit: str, destination: Path) -> None:
    tar_path = destination.parent / "submission.tar"
    run_checked([
        "git", "-C", str(repo), "archive", "--format=tar",
        f"--output={tar_path}", commit,
    ])
    safe_extract_tar(tar_path, destination)
    tar_path.unlink()


def file_manifest(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        rows.append({
            "path": path.relative_to(root).as_posix(),
            "sha256": digest,
            "size_bytes": path.stat().st_size,
        })
    return rows


def lock_read_only(root: Path) -> None:
    for path in sorted(root.rglob("*"), reverse=True):
        if path.is_file():
            path.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        elif path.is_dir():
            path.chmod(stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
    root.chmod(stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)


def unlock_for_cleanup(root: Path) -> None:
    if not root.exists():
        return
    root.chmod(stat.S_IRWXU)
    for path in root.rglob("*"):
        try:
            if path.is_dir():
                path.chmod(stat.S_IRWXU)
            else:
                path.chmod(stat.S_IRUSR | stat.S_IWUSR)
        except FileNotFoundError:
            pass


def build_prompt(case_id: str, commit: str, contract: str, metrics_text: str) -> str:
    return f"""You are the sole independent evaluator for {case_id}. Review the history-free evidence snapshot exported exactly from frozen first-pass commit {commit}.

INDEPENDENCE AND ACCESS RULES
- You are a separate Codex CLI process commissioned only after first-pass freeze.
- You have not been given prior grades, evaluator findings, correction history, or private chain of reasoning. Do not seek or infer them.
- Use only the public task contract at {contract}, the raw supplied inputs, the frozen implementation/artifacts, and public validation/reproduction evidence inside this snapshot.
- Do not access hidden graders, rubrics, reference outputs, expected outputs, verifier archives, or ground truth.
- The snapshot is read-only. Do not modify it and do not perform a correction cycle.
- Critically assess bundled validators; do not treat their PASS result as independent proof.
- Independently recompute substantive scientific results from raw inputs using separate code paths where feasible.
- Inspect every required figure supplied as an image attachment for legibility and scientific correctness.

FROZEN SEVERITY AND ENDPOINT RULES
{metrics_text}

REQUIRED OUTPUT
Return only the structured evaluation required by the supplied JSON schema. Report every substantive defect with concrete file, line, numeric, or raw-data evidence. Assign S0/S1/S2/S3 counts exactly from the listed findings. State whether any required result or principal conclusion changes. Set primary_endpoint_pass=1 only when S2=0, S3=0, required artifacts are complete, central results reproduce, and no evidence contradicts the disclosed pre-freeze assistance record. If a fresh-environment workflow cannot be rerun because this review is read-only, distinguish that from independent numerical recomputation and assess the preserved reproduction evidence explicitly.
"""


def validate_grade(grade: dict[str, Any]) -> None:
    missing = [k for k in GRADE_SCHEMA["required"] if k not in grade]
    if missing:
        raise ValueError(f"grade missing required keys: {missing}")
    if grade["verdict"] not in {"PASS", "FAIL"}:
        raise ValueError("verdict must be PASS or FAIL")
    if not isinstance(grade["score"], int) or not 0 <= grade["score"] <= 100:
        raise ValueError("score must be an integer from 0 to 100")
    counts = {s: 0 for s in SEVERITIES}
    for finding in grade["findings"]:
        severity = finding.get("severity")
        if severity not in counts:
            raise ValueError(f"invalid finding severity: {severity!r}")
        counts[severity] += 1
    if grade["severity_counts"] != counts:
        raise ValueError(
            f"severity_counts {grade['severity_counts']} do not match findings {counts}"
        )
    endpoint = grade["primary_endpoint_pass"]
    if endpoint not in (0, 1):
        raise ValueError("primary_endpoint_pass must be 0 or 1")
    if endpoint == 1:
        if counts["S2"] or counts["S3"]:
            raise ValueError("primary endpoint cannot pass with S2 or S3 findings")
        if not grade["artifact_complete"]:
            raise ValueError("primary endpoint cannot pass with incomplete artifacts")
        if not grade["reproducibility"]["central_results_recomputed"]:
            raise ValueError("primary endpoint pass requires central-result recomputation")
        if grade["reviewer"]["hidden_materials_accessed"]:
            raise ValueError("independent endpoint cannot pass after hidden-material access")


def render_markdown(grade: dict[str, Any], metadata: dict[str, Any]) -> str:
    r = grade["reviewer"]
    lines = [
        f"# Independent Codex Evaluation — {metadata['case_id']}", "",
        f"- Frozen commit: `{metadata['commit']}`",
        f"- Evaluator system: {r['system']}",
        f"- Evaluator model: {r['model']}",
        f"- Codex CLI: `{metadata['codex_cli_version']}`",
        f"- Separate process: {'yes' if r['separate_process'] else 'no'}",
        f"- Blinded to prior grades: {'yes' if r['blinded_to_prior_grades'] else 'no'}",
        f"- Hidden materials accessed: {'yes' if r['hidden_materials_accessed'] else 'no'}",
        "",
        f"## Grade: {grade['score']}/100 — {grade['verdict']}", "",
        f"**Evaluator-level `primary_endpoint_pass = {grade['primary_endpoint_pass']}`**", "",
        "## Severity counts", "",
        "| S0 | S1 | S2 | S3 |", "|---:|---:|---:|---:|",
        "| {S0} | {S1} | {S2} | {S3} |".format(**grade["severity_counts"]), "",
        "## Findings", "",
    ]
    if not grade["findings"]:
        lines.append("No substantive defects identified.")
    for finding in grade["findings"]:
        lines.extend([
            f"### {finding['id']} — {finding['severity']}: {finding['title']}", "",
            finding["evidence"], "",
            f"- Required result affected: {'yes' if finding['required_result_affected'] else 'no'}",
            f"- Principal conclusion affected: {'yes' if finding['principal_conclusion_affected'] else 'no'}",
            "",
        ])
    lines.extend([
        "## Reproducibility", "", grade["reproducibility"]["assessment"], "",
        f"- Central results independently recomputed: {'yes' if grade['reproducibility']['central_results_recomputed'] else 'no'}",
        f"- Fresh environment rerun by evaluator: {'yes' if grade['reproducibility']['fresh_environment_rerun'] else 'no'}",
        "", "## Overall determination", "", grade["overall_summary"], "",
        f"**Primary-endpoint rationale:** {grade['primary_endpoint_rationale']}", "",
        f"**Correction required:** {'yes' if grade['correction_required'] else 'no'}", "",
        "## Audit artifacts", "",
        "- `grade.json` — schema-constrained evaluator output",
        "- `codex_events.jsonl` — complete Codex CLI event stream",
        "- `prompt.txt` — exact blinded evaluation prompt",
        "- `evidence_manifest.json` — hashes of the frozen evidence snapshot",
        "- `run_metadata.json` — invocation and environment metadata",
        "- `evaluation.schema.json` — enforced output schema",
        "",
    ])
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("submission_repo", type=Path, help="Git repository containing the frozen submission")
    parser.add_argument("--commit", required=True, help="Frozen first-pass commit or revision")
    parser.add_argument("--case-id", required=True, help="Case identifier, for example CASE_1")
    parser.add_argument("--contract", default=DEFAULT_CONTRACT, help="Contract path inside the submission snapshot")
    parser.add_argument("--metrics-schema", type=Path, default=PROTOCOL_ROOT / "METRICS_SCHEMA.md")
    parser.add_argument("--output-dir", type=Path, help="Audit-artifact directory")
    parser.add_argument("--model", help="Optional explicit Codex model identifier")
    parser.add_argument("--codex-bin", default="codex", help="Codex CLI executable")
    parser.add_argument("--keep-workdir", action="store_true", help="Preserve the disposable evidence snapshot")
    parser.add_argument("--dry-run", action="store_true", help="Prepare and audit the prompt/snapshot without invoking Codex")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = args.submission_repo.expanduser().resolve()
    if not (repo / ".git").exists():
        raise SystemExit(f"not a Git working tree: {repo}")
    commit = resolve_commit(repo, args.commit)
    metrics_path = args.metrics_schema.expanduser().resolve()
    metrics_text = metrics_path.read_text(encoding="utf-8")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_dir = (args.output_dir or (
        PROTOCOL_ROOT / "cases" / "evaluations" / f"{args.case_id}_CODEX_{stamp}"
    )).expanduser().resolve()
    if path_is_within(output_dir, repo):
        raise SystemExit(
            "--output-dir must be outside the submission repository so grading cannot modify it"
        )
    output_dir.mkdir(parents=True, exist_ok=False)

    codex_path = shutil.which(args.codex_bin)
    if not codex_path and not args.dry_run:
        raise SystemExit(f"Codex CLI not found: {args.codex_bin}")
    codex_version = (
        run_checked([codex_path, "--version"]) if codex_path else "not checked (dry run)"
    )

    work_parent = Path(tempfile.mkdtemp(prefix="arav-codex-evaluator-"))
    snapshot = work_parent / "submission"
    snapshot.mkdir()
    completed = False
    try:
        export_snapshot(repo, commit, snapshot)
        contract_path = snapshot / args.contract
        if not contract_path.is_file():
            raise RuntimeError(f"contract not found in frozen snapshot: {args.contract}")
        manifest = file_manifest(snapshot)
        prompt = build_prompt(args.case_id, commit, args.contract, metrics_text)
        images = sorted((snapshot / "output").glob("*.png")) if (snapshot / "output").is_dir() else []

        schema_path = output_dir / "evaluation.schema.json"
        prompt_path = output_dir / "prompt.txt"
        manifest_path = output_dir / "evidence_manifest.json"
        events_path = output_dir / "codex_events.jsonl"
        grade_path = output_dir / "grade.json"
        metadata_path = output_dir / "run_metadata.json"
        schema_path.write_text(json.dumps(GRADE_SCHEMA, indent=2) + "\n", encoding="utf-8")
        prompt_path.write_text(prompt, encoding="utf-8")
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

        command = [
            codex_path or args.codex_bin, "exec", "--ephemeral", "--ignore-user-config",
            "--ignore-rules", "--sandbox", "read-only", "--skip-git-repo-check",
            "--cd", str(snapshot), "--output-schema", str(schema_path),
            "--output-last-message", str(grade_path), "--json",
        ]
        if args.model:
            command += ["--model", args.model]
        for image in images[:16]:
            command += ["--image", str(image)]
        command.append("-")

        metadata: dict[str, Any] = {
            "case_id": args.case_id,
            "source_repository": str(repo),
            "requested_revision": args.commit,
            "commit": commit,
            "contract": args.contract,
            "metrics_schema_sha256": hashlib.sha256(metrics_text.encode()).hexdigest(),
            "codex_cli_path": codex_path,
            "codex_cli_version": codex_version,
            "explicit_model": args.model,
            "sandbox": "read-only",
            "ephemeral": True,
            "history_free_snapshot": True,
            "prior_evaluations_supplied": False,
            "image_attachments": [p.relative_to(snapshot).as_posix() for p in images[:16]],
            "evidence_file_count": len(manifest),
            "evidence_manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
            "started_at_utc": datetime.now(timezone.utc).isoformat(),
            "status": "prepared",
            "command": command,
        }
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        lock_read_only(snapshot)

        if args.dry_run:
            metadata["status"] = "dry_run_complete"
            metadata["completed_at_utc"] = datetime.now(timezone.utc).isoformat()
            metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
            print(f"EVALUATOR_DRY_RUN_OK commit={commit} files={len(manifest)} images={len(images[:16])}")
            print(f"artifacts={output_dir}")
            completed = True
            return 0

        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        with prompt_path.open("r", encoding="utf-8") as prompt_fh, events_path.open("w", encoding="utf-8") as events_fh:
            process = subprocess.Popen(
                command, stdin=prompt_fh, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, bufsize=1, env=env,
            )
            assert process.stdout is not None
            for line in process.stdout:
                events_fh.write(line)
                events_fh.flush()
                print(line, end="")
            returncode = process.wait()
        if returncode:
            metadata["status"] = "codex_failed"
            metadata["codex_exit_code"] = returncode
            metadata["completed_at_utc"] = datetime.now(timezone.utc).isoformat()
            metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
            raise RuntimeError(f"Codex CLI failed with exit code {returncode}; see {events_path}")

        grade = json.loads(grade_path.read_text(encoding="utf-8"))
        validate_grade(grade)
        report_path = output_dir / "grade.md"
        metadata["status"] = "complete"
        metadata["codex_exit_code"] = 0
        metadata["completed_at_utc"] = datetime.now(timezone.utc).isoformat()
        metadata["grade_sha256"] = hashlib.sha256(grade_path.read_bytes()).hexdigest()
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        report_path.write_text(render_markdown(grade, metadata), encoding="utf-8")
        print(
            "EVALUATOR_OK "
            f"commit={commit} score={grade['score']} verdict={grade['verdict']} "
            f"S0={grade['severity_counts']['S0']} S1={grade['severity_counts']['S1']} "
            f"S2={grade['severity_counts']['S2']} S3={grade['severity_counts']['S3']} "
            f"primary_endpoint_pass={grade['primary_endpoint_pass']}"
        )
        print(f"artifacts={output_dir}")
        completed = True
        return 0
    finally:
        if args.keep_workdir:
            print(f"workdir_preserved={work_parent}")
        else:
            unlock_for_cleanup(snapshot)
            shutil.rmtree(work_parent, ignore_errors=True)
        if not completed:
            print(f"evaluation_incomplete artifacts={output_dir}", file=sys.stderr)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"EVALUATOR_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
