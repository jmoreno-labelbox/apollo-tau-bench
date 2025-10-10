# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListFailedTestsForRun(Tool):
    """List failed test results for a given test_run_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], test_run_id) -> str:
        results = list(data.get("test_results", {}).values())
        failed = [r for r in results if r.get("test_run_id") == test_run_id and r.get("status") == "failed"]
        return json.dumps({"count": len(failed), "failed_results": failed}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_failed_tests_for_run",
                "description": "List failed test results for a specific test_run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string"}
                    },
                    "required": ["test_run_id"]
                }
            }
        }
