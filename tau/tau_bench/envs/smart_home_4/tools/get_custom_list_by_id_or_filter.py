# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomListByIdOrFilter(Tool):
    """Retrieve a custom list by name/id."""
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str = "", name: str = "", filters: Optional[Dict[str, Any]] = None) -> str:
        custom_lists = data.get('custom_lists', [])
        if list_id:
            result = [l for l in custom_lists if l.get("list_id") == list_id]
        elif name:
            result = [l for l in custom_lists if l.get("name") == name]
        elif filters:
            result = [l for l in custom_lists if all(l.get(k) == v for k, v in filters.items())]
        else:
            return json.dumps({"error": "Either 'list_id', 'name', or 'filters' must be provided"}, indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_custom_list_by_filter_or_id",
                "description": "Retrieve a custom list by list_id, name, or filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "Custom list id to retrieve (optional if using name or filters)"
                        },
                        "name": {
                            "type": "string",
                            "description": "Custom list name to retrieve (optional if using list_id or filters)"
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter custom lists (optional if using list_id or name)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
