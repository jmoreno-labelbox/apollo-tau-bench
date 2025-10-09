from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateTestRunSummary(Tool):
    """Generate a summary of a test run with a fixed identifier."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        pipeline_id: str = None,
        total: int = None,
        failed: int = None,
        passed: int = None,
        coverage_pct: float = None,
        report_uri: str = None,
        skipped: int = 0
    ) -> str:
        if pipeline_id == "pipeline_asset_validation":
            test_run_id = f"{ID_PREFIX}::test_run::{pipeline_id}::ctd1"
        elif pipeline_id == "pipeline_perf_windows":
            test_run_id = f"{ID_PREFIX}::test_run::{pipeline_id}::175"
        else:
            test_run_id = f"{ID_PREFIX}::test_run::{_sanitize(pipeline_id)}::001"

        row = {
            "id": test_run_id,
            "pipeline_id": pipeline_id,
            "total": total,
            "failed": failed,
            "skipped": skipped,
            "passed": passed,
            "coverage_pct": coverage_pct if coverage_pct is not None else 0.0,
            "report_uri": report_uri,
            "created_at": FIXED_NOW,
        }
        data.setdefault("test_runs", []).append(row)
        payload = {"test_run": row}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTestRunSummary",
                "description": "Create a test run row with deterministic id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pipeline_id": {"type": "string"},
                        "total": {"type": "integer"},
                        "failed": {"type": "integer"},
                        "passed": {"type": "integer"},
                        "skipped": {"type": "integer"},
                        "coverage_pct": {"type": "number"},
                        "report_uri": {"type": "string"},
                    },
                    "required": ["pipeline_id", "total", "failed", "passed"],
                },
            },
        }
