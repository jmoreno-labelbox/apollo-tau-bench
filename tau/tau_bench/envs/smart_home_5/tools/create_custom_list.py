# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCustomList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_list: Dict[str, Any]) -> str:
        custom_lists = data.get('custom_lists', [])
        if 'list_id' not in new_list:
            return json.dumps({"error": "New list must have 'list_id' and 'name'."}, indent=2)

        custom_lists.append(new_list)
        return json.dumps({"success": "Custom list created."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_custom_list",
                "description": "Create a new custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_list": {
                            "type": "object",
                            "description": "A dictionary representing the new custom list.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["new_list"],
                    "additionalProperties": False
                }
            }
        }
