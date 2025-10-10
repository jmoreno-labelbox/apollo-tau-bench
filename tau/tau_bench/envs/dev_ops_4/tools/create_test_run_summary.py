# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTestRunSummary(Tool):
    """Create a test run summary with a deterministic id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pipeline_id = kwargs.get("pipeline_id")
        total = kwargs.get("total")
        failed = kwargs.get("failed")
        passed = kwargs.get("passed")
        skipped = kwargs.get("skipped", 0)
        coverage_pct = kwargs.get("coverage_pct")
        report_uri = kwargs.get("report_uri")

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
            "created_at": FIXED_NOW
        }
        data.setdefault("test_runs", []).append(row)
        return json.dumps({"test_run": row}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_test_run_summary",
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
                        "report_uri": {"type": "string"}
                    },
                    "required": ["pipeline_id", "total", "failed", "passed"]
                }
            }
        }
