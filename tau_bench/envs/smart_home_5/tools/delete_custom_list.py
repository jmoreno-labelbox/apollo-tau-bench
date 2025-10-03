from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeleteCustomList(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: str) -> str:
        custom_lists = data.get("custom_lists", [])
        initial_len = len(custom_lists)
        custom_lists[:] = [l for l in custom_lists if l.get("list_id") != list_id]

        if len(custom_lists) == initial_len:
            payload = {"error": f"Custom list with ID '{list_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"success": f"Custom list '{list_id}' deleted."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteCustomList",
                "description": "Delete a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the custom list to delete.",
                        }
                    },
                    "required": ["list_id"],
                    "additionalProperties": False,
                },
            },
        }
