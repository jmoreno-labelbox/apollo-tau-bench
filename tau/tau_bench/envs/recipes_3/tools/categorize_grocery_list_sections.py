# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CategorizeGroceryListSections(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int) -> str:
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(list_id):
                continue
            ing = _ingredient_by_id(data, int(it.get("ingredient_id")))
            it["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
            updated += 1
        # Deterministic header write to ensure write semantics
        gl = _require(data, "grocery_lists", "list_id", int(list_id))
        if gl is not None:
            gl["last_categorized_at"] = "2025-01-01T12:10:00"
        return json({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "categorize_grocery_list_sections",
                "description": "Refresh grocery_section for items in a list.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }
