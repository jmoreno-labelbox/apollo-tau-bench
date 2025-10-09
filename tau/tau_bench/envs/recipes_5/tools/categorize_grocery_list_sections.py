from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class CategorizeGroceryListSections(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: str = None) -> str:
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None:
            return _json_dump({"updated_items": 0})
        cnt = 0
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            ingr = _ingredient_by_id(data, int(item.get("ingredient_id")))
            item["grocery_section"] = (ingr or {}).get("grocery_section", "Misc")
            cnt += 1
        return _json_dump({"updated_items": cnt})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CategorizeGroceryListSections",
                "description": "Refresh grocery_section on all items; defaults to latest list.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": [],
                },
            },
        }
