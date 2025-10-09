from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetGroceryListStatus(Tool):
    """Modify grocery_lists.status_enum for the specified list_id."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, status_enum: str = None) -> str:
        if list_id is None or not status_enum:
            return _json_dump({"error": "list_id and status_enum are required"})
        row = _require(data, "grocery_lists", "list_id", int(list_id))
        if not row:
            return _json_dump({"error": f"list_id {list_id} not found"})
        row["status_enum"] = str(status_enum)
        return _json_dump(row)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetGroceryListStatus",
                "description": "Set the status of a grocery list.",
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
