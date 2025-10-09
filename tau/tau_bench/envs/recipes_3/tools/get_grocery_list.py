from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetGroceryList(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: int) -> str:
        lists_ = _get_table(data, "grocery_lists")
        gli = _get_table(data, "grocery_list_items")
        lst = next((l for l in lists_ if l.get("list_id") == list_id), None)
        items = [i for i in gli.values() if i.get("list_id") == list_id]
        payload = {"grocery_list": lst, "items": items}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGroceryList",
                "description": "Returns grocery_list row and its items.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }
