from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateTestRunCoverage(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateTestRunCoverage",
                "description": "Updates the coverage percentage of a test run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string", "description": "Test run id"},
                        "coverage_pct": {
                            "type": "number",
                            "description": "Coverage percentage 0..100",
                        },
                    },
                    "required": ["test_run_id", "coverage_pct"],
                },
            },
        }

    @staticmethod
    def invoke(data, test_run_id=None, coverage_pct=None):
        test_runs = data.get("test_runs", {}).values()
        row = next((t for t in test_runs.values() if t.get("id") == test_run_id), None)
        if not row:
            payload = {"error": "test_run_not_found", "test_run_id": test_run_id}
            out = json.dumps(payload)
            return out
        if "stats" in row and isinstance(row["stats"], dict):
            row["stats"]["coverage_pct"] = coverage_pct
        row["coverage_pct"] = coverage_pct
        payload = {"test_run": row}
        out = json.dumps(payload, indent=2)
        return out
