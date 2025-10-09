from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddCustomListToDatabase(Tool):
    """Introduce a new custom list."""

    @staticmethod
    def invoke(data: dict[str, Any], custom_list: dict[str, Any] | None = None) -> str:
        if not custom_list:
            payload = {"error": "'custom_list' parameter is required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        custom_lists = data.get("custom_lists", {}).values()
        if any(l["list_id"] == custom_list.get("list_id") for l in custom_lists.values()):
            payload = {"error": "Custom list with this id already exists"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        data["custom_lists"][custom_list["custom_list_id"]] = custom_list
        payload = {
                "success": "Custom list added",
                "custom_list": custom_list,
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
                "name": "AddCustomListToDatabase",
                "description": "Add a new custom list. All fields must be provided in the 'custom_list' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "custom_list": {
                            "type": "object",
                            "description": "The full custom list object to add (must include list_id, name, created_at, updated_at, tags, items)",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["custom_list"],
                    "additionalProperties": False,
                },
            },
        }
