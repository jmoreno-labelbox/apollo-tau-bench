from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetTestResultById(Tool):
    """Fetches a specific test result using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        test_result_id = id
        test_results = data.get("test_results", {}).values()
        for result in test_results.values():
            if result.get("id") == test_result_id:
                payload = result
                out = json.dumps(payload)
                return out
        payload = {"error": f"Test result with ID '{test_result_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTestResultById",
                "description": "Retrieves a specific test result by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "The unique ID of the test result.",
                        }
                    },
                    "required": ["id"],
                },
            },
        }
