# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateGroceryListWithSubstitutes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int, substitutions: List[Dict[str, Any]]) -> str:
        mapping = {
            int(s["ingredient_id"]): int(s["substitute_ingredient_id"])
            for s in substitutions
            if "ingredient_id" in s and "substitute_ingredient_id" in s
        }
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(list_id):
                continue
            iid = int(it.get("ingredient_id"))
            if iid in mapping:
                new_iid = mapping[iid]
                it["ingredient_id"] = new_iid
                ing = _ingredient_by_id(data, new_iid)
                it["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
                updated += 1
        # Deterministic header write to ensure write semantics
        gl = _require(data, "grocery_lists", "list_id", int(list_id))
        if gl is not None:
            gl["last_substitutions_applied_at"] = "2025-01-01T12:25:00"
        return json({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_grocery_list_with_substitutes",
                "description": "Apply substitutions to grocery_list_items.",
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
