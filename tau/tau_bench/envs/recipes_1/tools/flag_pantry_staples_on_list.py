from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FlagPantryStaplesOnList(Tool):
    """Assign pantry_staple_flag to list items according to the ingredients table."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None) -> str:
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        updated = 0
        for item in data.get("grocery_list_items", []):
            if int(item.get("list_id")) != int(list_id):
                continue
            ing = _ingredient_by_id(data, int(item.get("ingredient_id")))
            item["pantry_staple_flag"] = bool(
                (ing or {}).get("pantry_staple_flag", False)
            )
            updated += 1
        return _json_dump({"updated_items": updated})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FlagPantryStaplesOnList",
                "description": "Fill pantry_staple_flag for items in a list.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }
