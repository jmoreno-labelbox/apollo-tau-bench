# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomListInDatabase(Tool):
    """Update items in a custom list."""
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str = "", updates: Optional[Dict[str, Any]] = None) -> str:
        if not list_id or not updates:
            return json.dumps({"error": "'list_id' and 'updates' parameters are required"}, indent=2)
        custom_lists = data.get('custom_lists', [])
        found = False
        for l in custom_lists:
            if l["list_id"] == list_id:
                for k, v in updates.items():
                    l[k] = v
                found = True
                break
        if not found:
            return json.dumps({"error": "Custom list not found"}, indent=2)
        return json.dumps({"success": "Custom list updated", "list_id": list_id, "updates": updates, "custom_lists": custom_lists}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_custom_list_in_database",
                "description": "Update any field of a custom list by list_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The id of the custom list to update."
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["list_id", "updates"],
                    "additionalProperties": False
                }
            }
        }
