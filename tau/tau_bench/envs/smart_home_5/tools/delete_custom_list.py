# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteCustomList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str) -> str:
        custom_lists = data.get('custom_lists', [])
        initial_len = len(custom_lists)
        custom_lists[:] = [l for l in custom_lists if l.get('list_id') != list_id]

        if len(custom_lists) == initial_len:
            return json.dumps({"error": f"Custom list with ID '{list_id}' not found."}, indent=2)

        return json.dumps({"success": f"Custom list '{list_id}' deleted."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_custom_list",
                "description": "Delete a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the custom list to delete."
                        }
                    },
                    "required": ["list_id"],
                    "additionalProperties": False
                }
            }
        }
