from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateCustomListInDatabase(Tool):
    """Modify items within a custom list."""

    @staticmethod
    def invoke(
        data: dict[str, Any], list_id: str = "", updates: dict[str, Any] | None = None
    ) -> str:
        if not list_id or not updates:
            payload = {"error": "'list_id' and 'updates' parameters are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        custom_lists = data.get("custom_lists", [])
        found = False
        for l in custom_lists:
            if l["list_id"] == list_id:
                for k, v in updates.items():
                    l[k] = v
                found = True
                break
        if not found:
            payload = {"error": "Custom list not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Custom list updated",
                "list_id": list_id,
                "updates": updates,
                "custom_lists": custom_lists,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomListInDatabase",
                "description": "Update any field of a custom list by list_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The id of the custom list to update.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["list_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }
