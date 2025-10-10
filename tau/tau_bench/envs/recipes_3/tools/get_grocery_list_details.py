# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGroceryListDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int) -> str:
        header = _require(data, "grocery_lists", "list_id", int(list_id))
        items = [
            i for i in data.get("grocery_list_items", []) if int(i.get("list_id")) == int(list_id)
        ]
        return _json({"grocery_list": header, "items": items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_list_details",
                "description": "Return grocery_list header and items.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }
