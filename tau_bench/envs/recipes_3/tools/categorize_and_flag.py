from tau_bench.envs.tool import Tool
import json
from typing import Any

class CategorizeAndFlag(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        items: list[dict[str, Any]],
        household_id: int,
        recent_30d: list[dict[str, Any]],
        ingredient_id: int = None,
        quantity: float = None,
        unit: str = None
    ) -> str:
        ingredients = _get_table(data, "ingredients")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        recent_set = {h.get("recipe_id") for h in (recent_30d or [])}
        # To set the overlap flag, identify ingredients present in any recipe utilized in the past 30 days
        ri = _get_table(data, "recipe_ingredients")
        recent_ings = {
            x.get("ingredient_id") for x in ri if x.get("recipe_id") in recent_set
        }
        out_items = []
        for it in items or []:
            ing = ing_map.get(it.get("ingredient_id")) or {}
            out_items.append(
                {
                    "ingredient_id": it.get("ingredient_id"),
                    "quantity": it.get("quantity"),
                    "unit": it.get("unit"),
                    "grocery_section": ing.get("grocery_section"),
                    "pantry_staple_flag": bool(ing.get("pantry_staple_flag")),
                    "overlap_last_month_flag": it.get("ingredient_id") in recent_ings,
                }
            )
        payload = {"categorized_items": out_items}
        out = json.dumps(payload, indent=2)
        return out
        pass
        ingredients = _get_table(data, "ingredients")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        recent_set = {h.get("recipe_id") for h in (recent_30d or [])}
        #To set the overlap flag, identify ingredients present in any recipe utilized in the past 30 days
        ri = _get_table(data, "recipe_ingredients")
        recent_ings = {
            x.get("ingredient_id") for x in ri if x.get("recipe_id") in recent_set
        }
        out_items = []
        for it in items or []:
            ing = ing_map.get(it.get("ingredient_id")) or {}
            out_items.append(
                {
                    "ingredient_id": it.get("ingredient_id"),
                    "quantity": it.get("quantity"),
                    "unit": it.get("unit"),
                    "grocery_section": ing.get("grocery_section"),
                    "pantry_staple_flag": bool(ing.get("pantry_staple_flag")),
                    "overlap_last_month_flag": it.get("ingredient_id") in recent_ings,
                }
            )
        payload = {"categorized_items": out_items}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "categorizeAndFlag",
                "description": "Adds grocery_section and flags to consolidated items using ingredients and recent history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "items": {"type": "array", "items": {"type": "object"}},
                        "household_id": {"type": "integer"},
                        "recent_30d": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["items", "household_id", "recent_30d"],
                },
            },
        }
