from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindFailedTestResultsForTestRun(Tool):
    """Locates all unsuccessful test results for a specified test run ID."""

    @staticmethod
    def invoke(data: dict[str, Any], test_run_id: str = None) -> str:
        test_results = data.get("test_results", [])

        failed_tests = [
            tr
            for tr in test_results
            if tr.get("test_run_id") == test_run_id and tr.get("status") == "failed"
        ]

        if not failed_tests:
            payload = {"info": f"No failed tests found for test run '{test_run_id}'."}
            out = json.dumps(payload)
            return out
        payload = {"failed_tests": failed_tests}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findFailedTestResultsForTestRun",
                "description": "Finds all failed test results for a given test run ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {
                            "type": "string",
                            "description": "The ID of the test run.",
                        }
                    },
                    "required": ["test_run_id"],
                },
            },
        }
