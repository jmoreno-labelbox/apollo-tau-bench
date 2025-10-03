from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetGroceryListDetails(Tool):
    """Retrieve the grocery_list header and all items associated with list_id."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None) -> str:
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        header = _require(data, "grocery_lists", "list_id", int(list_id))
        if not header:
            return _json_dump({"error": f"list_id {list_id} not found"})
        items = [
            i
            for i in data.get("grocery_list_items", [])
            if int(i.get("list_id")) == int(list_id)
        ]
        return _json_dump({"grocery_list": header, "items": items})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGroceryListDetails",
                "description": "Get a grocery_list header plus items.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }
