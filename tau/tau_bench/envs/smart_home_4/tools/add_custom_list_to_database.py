# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddCustomListToDatabase(Tool):
    """Add a new custom list."""
    @staticmethod
    def invoke(data: Dict[str, Any], custom_list: Optional[Dict[str, Any]] = None) -> str:
        if not custom_list:
            return json.dumps({"error": "'custom_list' parameter is required"}, indent=2)
        custom_lists = data.get('custom_lists', [])
        if any(l["list_id"] == custom_list.get("list_id") for l in custom_lists):
            return json.dumps({"error": "Custom list with this id already exists"}, indent=2)
        custom_lists.append(custom_list)
        return json.dumps({"success": "Custom list added", "custom_list": custom_list, "custom_lists": custom_lists}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_custom_list_to_database",
                "description": "Add a new custom list. All fields must be provided in the 'custom_list' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "custom_list": {
                            "type": "object",
                            "description": "The full custom list object to add (must include list_id, name, created_at, updated_at, tags, items)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["custom_list"],
                    "additionalProperties": False
                }
            }
        }
