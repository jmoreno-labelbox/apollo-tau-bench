from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListFailedTestsForRun(Tool):
    """Display failed test results for a specified test_run_id."""

    @staticmethod
    def invoke(data: dict[str, Any], test_run_id: str = None) -> str:
        results = data.get("test_results", [])
        failed = [
            r
            for r in results
            if r.get("test_run_id") == test_run_id and r.get("status") == "failed"
        ]
        payload = {"count": len(failed), "failed_results": failed}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListFailedTestsForRun",
                "description": "List failed test results for a specific test_run.",
                "parameters": {
                    "type": "object",
                    "properties": {"test_run_id": {"type": "string"}},
                    "required": ["test_run_id"],
                },
            },
        }
