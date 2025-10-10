# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTestRunCoverage(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_test_run_coverage",
                "description": "Updates the coverage percentage of a test run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string", "description": "Test run id"},
                        "coverage_pct": {"type": "number", "description": "Coverage percentage 0..100"}
                    },
                    "required": ["test_run_id", "coverage_pct"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        test_run_id = kwargs.get("test_run_id")
        coverage_pct = kwargs.get("coverage_pct")
        test_runs = data.get("test_runs", [])
        row = next((t for t in test_runs if t.get("id") == test_run_id), None)
        if not row:
            return json.dumps({"error": "test_run_not_found", "test_run_id": test_run_id})
        if "stats" in row and isinstance(row["stats"], dict):
            row["stats"]["coverage_pct"] = coverage_pct
        row["coverage_pct"] = coverage_pct
        return json.dumps({"test_run": row}, indent=2)
