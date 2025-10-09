from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateGroceryListWithSubstitutes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, substitutions: list[dict[str, int]] = None) -> str:
        if substitutions is None:
            substitutions = []
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None:
            return _json_dump({"updated_items": 0})
        replaced = 0
        mapping = {
            int(s["ingredient_id"]): int(s["substitute_ingredient_id"])
            for s in substitutions
            if "ingredient_id" in s and "substitute_ingredient_id" in s
        }
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            old = int(item.get("ingredient_id"))
            if old in mapping:
                new_ing_id = mapping[old]
                item["ingredient_id"] = new_ing_id
                ing = _ingredient_by_id(data, new_ing_id)
                item["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
                replaced += 1
        return _json_dump({"updated_items": replaced})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateGroceryListWithSubstitutes",
                "description": "Replace ingredient_id for grocery items; defaults to latest list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "substitutions": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": [],
                },
            },
        }
