from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateGroceryListWithSubstitutes(Tool):
    """Implement substitutions on grocery_list_items by modifying ingredient_id and updating grocery_section."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, substitutions: list = None) -> str:
        if list_id is None or not isinstance(substitutions, list):
            return _json_dump({"error": "list_id and substitutions are required"})
        mapping = {
            int(s["ingredient_id"]): int(s["substitute_ingredient_id"])
            for s in substitutions
            if "ingredient_id" in s and "substitute_ingredient_id" in s
        }
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(list_id):
                continue
            old = int(it.get("ingredient_id"))
            if old in mapping:
                new_iid = mapping[old]
                it["ingredient_id"] = new_iid
                ing = _ingredient_by_id(data, new_iid)
                it["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
                updated += 1
        return _json_dump({"updated_items": updated})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateGroceryListWithSubstitutes",
                "description": "Replace ingredient_ids on list items using a substitution mapping.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "substitutions": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["list_id", "substitutions"],
                },
            },
        }
