from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateCustomList(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], new_list: dict[str, Any]) -> str:
        custom_lists = data.get("custom_lists", [])
        if "list_id" not in new_list:
            payload = {"error": "New list must have 'list_id' and 'name'."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        custom_lists.append(new_list)
        payload = {"success": "Custom list created."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCustomList",
                "description": "Create a new custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_list": {
                            "type": "object",
                            "description": "A dictionary representing the new custom list.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["new_list"],
                    "additionalProperties": False,
                },
            },
        }
