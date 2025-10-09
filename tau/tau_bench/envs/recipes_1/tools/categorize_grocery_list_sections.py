from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CategorizeGroceryListSections(Tool):
    """Update grocery_section for all items in a list based on ingredient definitions."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None) -> str:
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        updated = 0
        for item in data.get("grocery_list_items", []):
            if int(item.get("list_id")) != int(list_id):
                continue
            ing = _ingredient_by_id(data, int(item.get("ingredient_id")))
            item["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
            updated += 1
        return _json_dump({"updated_items": updated})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CategorizeGroceryListSections",
                "description": "Set grocery_section on each item in a list from ingredients table.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }
