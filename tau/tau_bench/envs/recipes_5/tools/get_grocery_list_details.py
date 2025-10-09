from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetGroceryListDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: str = None) -> str:
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None:
            return _json_dump({"error": "no grocery_list available"})
        header = _ensure_list_id(data, list_id)
        if not header:
            return _json_dump({"error": f"list_id {list_id} not found"})
        items = [
            i for i in data.get("grocery_list_items", {}).values() if i.get("list_id") == list_id
        ]
        return _json_dump({"grocery_list": header, "items": items})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGroceryListDetails",
                "description": "Get a grocery_list header and items; defaults to latest list.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": [],
                },
            },
        }
