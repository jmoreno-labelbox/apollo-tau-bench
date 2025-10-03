from tau_bench.envs.tool import Tool
import json
from typing import Any

class FilterRecipesByInventory(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        recipe_ids: list[int],
        allow_pantry_staples: bool = True,
        max_missing_ingredients: int = 1,
        recent_history: list[dict[str, Any]] | None = None
    ) -> str:
        ingredients = _get_table(data, "ingredients")
        inv = _get_table(data, "inventory_items")
        ri = _get_table(data, "recipe_ingredients")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        # Create available set: quantity greater than 0 in inventory along with pantry staples (if permitted)
        inv_ids = {
            row.get("ingredient_id")
            for row in inv
            if row.get("household_id") == household_id
            and float(row.get("quantity") or 0) > 0
        }
        if allow_pantry_staples:
            for ing in ingredients:
                if bool(ing.get("pantry_staple_flag")):
                    inv_ids.add(ing.get("ingredient_id"))
        # Recent removal
        recent_set = {row.get("recipe_id") for row in (recent_history or [])}
        eligible: list[int] = []
        missing_counts: dict[str, int] = {}
        for rid in recipe_ids or []:
            if rid in recent_set:
                continue
            rows = [x for x in ri if x.get("recipe_id") == rid]
            missing = 0
            for x in rows:
                ing_id = x.get("ingredient_id")
                if ing_id in inv_ids:
                    continue
                missing += 1
                if missing > int(max_missing_ingredients or 0):
                    break
            if missing <= int(max_missing_ingredients or 0):
                eligible.append(rid)
                missing_counts[str(rid)] = missing
        payload = {"eligible_recipe_ids": eligible, "missing_counts": missing_counts}
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        ingredients = _get_table(data, "ingredients")
        inv = _get_table(data, "inventory_items")
        ri = _get_table(data, "recipe_ingredients")
        ing_map = {i.get("ingredient_id"): i for i in ingredients}
        #Create available set: quantity greater than 0 in inventory along with pantry staples (if permitted)
        inv_ids = {
            row.get("ingredient_id")
            for row in inv
            if row.get("household_id") == household_id
            and float(row.get("quantity") or 0) > 0
        }
        if allow_pantry_staples:
            for ing in ingredients:
                if bool(ing.get("pantry_staple_flag")):
                    inv_ids.add(ing.get("ingredient_id"))
        #Recent removal
        recent_set = {row.get("recipe_id") for row in (recent_history or [])}
        eligible: list[int] = []
        missing_counts: dict[str, int] = {}
        for rid in recipe_ids or []:
            if rid in recent_set:
                continue
            rows = [x for x in ri if x.get("recipe_id") == rid]
            missing = 0
            for x in rows:
                ing_id = x.get("ingredient_id")
                if ing_id in inv_ids:
                    continue
                missing += 1
                if missing > int(max_missing_ingredients or 0):
                    break
            if missing <= int(max_missing_ingredients or 0):
                eligible.append(rid)
                missing_counts[str(rid)] = missing
        payload = {"eligible_recipe_ids": eligible, "missing_counts": missing_counts}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterRecipesByInventory",
                "description": "Filters recipe_ids by household inventory with optional pantry staples and missing-ingredient budget; excludes recent_history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "allow_pantry_staples": {"type": "boolean"},
                        "max_missing_ingredients": {"type": "integer"},
                        "recent_history": {"type": "array"},
                    },
                    "required": ["household_id", "recipe_ids"],
                },
            },
        }
