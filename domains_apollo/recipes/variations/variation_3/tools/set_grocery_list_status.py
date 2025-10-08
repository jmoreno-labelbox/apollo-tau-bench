from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetGroceryListStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: int, status_enum: str) -> str:
        lists_ = _get_table(data, "grocery_lists")
        lst = next((l for l in lists_ if l.get("list_id") == list_id), None)
        if not lst:
            return _error("list not found")
        lst["status_enum"] = status_enum
        payload = {"list_id": list_id, "status_enum": status_enum}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setGroceryListStatus",
                "description": "Sets status_enum for a grocery list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "status_enum": {"type": "string"},
                    },
                    "required": ["list_id", "status_enum"],
                },
            },
        }
