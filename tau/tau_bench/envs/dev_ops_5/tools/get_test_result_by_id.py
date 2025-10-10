# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTestResultById(Tool):
    """Retrieves a specific test result by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        test_result_id = kwargs.get("id")
        test_results = data.get("test_results", [])
        for result in test_results:
            if result.get("id") == test_result_id:
                return json.dumps(result)
        return json.dumps({"error": f"Test result with ID '{test_result_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_test_result_by_id",
                "description": "Retrieves a specific test result by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string", "description": "The unique ID of the test result."}},
                    "required": ["id"],
                },
            },
        }
