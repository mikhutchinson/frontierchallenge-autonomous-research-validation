from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "evaluator.py"
SPEC = importlib.util.spec_from_file_location("arav_evaluator", MODULE_PATH)
assert SPEC and SPEC.loader
E = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(E)


def valid_grade():
    return {
        "reviewer": {
            "system": "Codex CLI", "model": "test", "separate_process": True,
            "blinded_to_prior_grades": True, "conflicts": [],
            "hidden_materials_accessed": False, "materials_accessed": ["contract"],
        },
        "score": 99, "verdict": "PASS", "artifact_complete": True,
        "reproducibility": {
            "central_results_recomputed": True, "fresh_environment_rerun": False,
            "assessment": "Independent recomputation passed.",
        },
        "findings": [{
            "id": "F1", "severity": "S1", "title": "Minor issue",
            "evidence": "Exact evidence.", "required_result_affected": False,
            "principal_conclusion_affected": False,
        }],
        "severity_counts": {"S0": 0, "S1": 1, "S2": 0, "S3": 0},
        "principal_conclusion_changes": False, "required_result_changes": False,
        "primary_endpoint_pass": 1, "primary_endpoint_rationale": "No S2/S3.",
        "correction_required": False, "overall_summary": "Valid first pass.",
    }


class EvaluatorTests(unittest.TestCase):
    def test_grade_validation_accepts_consistent_endpoint(self):
        E.validate_grade(valid_grade())

    def test_grade_validation_rejects_count_mismatch(self):
        grade = valid_grade()
        grade["severity_counts"]["S1"] = 0
        with self.assertRaisesRegex(ValueError, "do not match"):
            E.validate_grade(grade)

    def test_grade_validation_rejects_endpoint_with_s2(self):
        grade = valid_grade()
        grade["findings"][0]["severity"] = "S2"
        grade["severity_counts"] = {"S0": 0, "S1": 0, "S2": 1, "S3": 0}
        with self.assertRaisesRegex(ValueError, "cannot pass with S2 or S3"):
            E.validate_grade(grade)

    def test_safe_extract_rejects_traversal(self):
        import io
        import tarfile
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            tar_path = root / "bad.tar"
            with tarfile.open(tar_path, "w") as archive:
                info = tarfile.TarInfo("../escape.txt")
                payload = b"bad"
                info.size = len(payload)
                archive.addfile(info, io.BytesIO(payload))
            destination = root / "out"
            destination.mkdir()
            with self.assertRaisesRegex(RuntimeError, "unsafe archive member"):
                E.safe_extract_tar(tar_path, destination)

    def test_path_is_within(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.assertTrue(E.path_is_within(root / "child", root))
            self.assertFalse(E.path_is_within(root.parent / "sibling", root))

    def test_markdown_contains_endpoint_and_counts(self):
        metadata = {
            "case_id": "CASE_X", "commit": "a" * 40,
            "codex_cli_version": "codex-cli test",
        }
        report = E.render_markdown(valid_grade(), metadata)
        self.assertIn("primary_endpoint_pass = 1", report)
        self.assertIn("| 0 | 1 | 0 | 0 |", report)


if __name__ == "__main__":
    unittest.main()
