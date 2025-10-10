# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHouseholdStapleIngredientId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        # Resolve a staple ingredient by heuristic: pick a true pantry_staple_flag ingredient that exists in inventory for household
        inv = [
            i
            for i in data.get("inventory_items", [])
            if int(i.get("household_id")) == int(household_id)
        ]
        staple_ids = sorted(
            {
                int(r.get("ingredient_id"))
                for r in list(data.get("ingredients", {}).values())
                if bool(r.get("pantry_staple_flag", False))
            }
        )
        inv_staples = [
            row
            for row in inv
            if int(row.get("ingredient_id")) in set(staple_ids)
            and float(row.get("quantity", 0)) > 0
        ]
        chosen = (
            int(inv_staples[0].get("ingredient_id"))
            if inv_staples
            else (staple_ids[0] if staple_ids else 0)
        )
        return _json({"staple_ingredient_id": chosen})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_household_staple_ingredient_id",
                "description": "Resolve a staple ingredient_id for a household from inventory/ingredients (no hard-coding).",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
