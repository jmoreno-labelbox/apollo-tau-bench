from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DeleteCustomListFromDatabase(Tool):
    """Delete a custom list using name or id."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: str = "") -> str:
        if not list_id:
            payload = {"error": "'list_id' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        custom_lists = data.get("custom_lists", [])
        new_list = [l for l in custom_lists if l["list_id"] != list_id]
        if len(new_list) == len(custom_lists):
            payload = {"error": "Custom list not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Custom list deleted",
                "list_id": list_id,
                "custom_lists": new_list,
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
                "name": "deleteCustomListFromDatabase",
                "description": "Remove a custom list by list_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The id of the custom list to delete.",
                        }
                    },
                    "required": ["list_id"],
                    "additionalProperties": False,
                },
            },
        }
