# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: Optional[str] = None, list_name: Optional[str] = None) -> str:
        custom_lists = data.get('custom_lists', [])
        if not list_id and not list_name:
            return json.dumps(custom_lists, indent=2)

        result = []
        for l in custom_lists:
            if list_id and l.get('list_id') == list_id:
                result.append(l)
            elif list_name and l.get('name') == list_name:
                result.append(l)

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_custom_list",
                "description": "Get one or more custom lists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the list to retrieve."
                        },
                        "list_name": {
                            "type": "string",
                            "description": "The name of the list to retrieve."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }
