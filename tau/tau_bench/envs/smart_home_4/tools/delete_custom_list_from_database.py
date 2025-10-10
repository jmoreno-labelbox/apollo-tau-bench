# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteCustomListFromDatabase(Tool):
    """Remove a custom list by name/id."""
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str = "") -> str:
        if not list_id:
            return json.dumps({"error": "'list_id' parameter is required"}, indent=2)
        custom_lists = data.get('custom_lists', [])
        new_list = [l for l in custom_lists if l["list_id"] != list_id]
        if len(new_list) == len(custom_lists):
            return json.dumps({"error": "Custom list not found"}, indent=2)
        return json.dumps({"success": "Custom list deleted", "list_id": list_id, "custom_lists": new_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_custom_list_from_database",
                "description": "Remove a custom list by list_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The id of the custom list to delete."
                        }
                    },
                    "required": ["list_id"],
                    "additionalProperties": False
                }
            }
        }
