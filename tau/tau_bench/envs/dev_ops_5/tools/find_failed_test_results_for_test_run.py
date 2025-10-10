# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindFailedTestResultsForTestRun(Tool):
    """Finds all failed test results for a given test run ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        test_run_id = kwargs.get("test_run_id")
        test_results = data.get("test_results", [])

        failed_tests = [tr for tr in test_results if tr.get("test_run_id") == test_run_id and tr.get("status") == "failed"]

        if not failed_tests:
            return json.dumps({"info": f"No failed tests found for test run '{test_run_id}'."})
            
        return json.dumps({"failed_tests": failed_tests})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_failed_test_results_for_test_run",
                "description": "Finds all failed test results for a given test run ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string", "description": "The ID of the test run."}
                    },
                    "required": ["test_run_id"]
                }
            }
        }
