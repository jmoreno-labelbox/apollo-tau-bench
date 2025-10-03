from tau_bench.envs.tool import Tool
import json
from typing import Any

class EnforceCuisineAndOverlap(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        recipe_ids: list[int],
        max_per_cuisine: int,
        max_unique_ingredients: int, candidate_recipe_ids_json: Any = None) -> str:
        recipes = _get_table(data, "recipes")
        ri = _get_table(data, "recipe_ingredients")
        by_id = {r.get("recipe_id"): r for r in recipes}
        cuisine_count: dict[str, int] = {}
        selected: list[int] = []
        # Monitor distinct ingredients throughout the selection
        selected_ing: set = set()
        for rid in recipe_ids or []:
            rec = by_id.get(rid)
            if not rec:
                continue
            cz = rec.get("cuisine")
            cnt = cuisine_count.get(cz, 0)
            if cnt >= max_per_cuisine:
                continue
            # calculate ingredients for this recipe
            ings = {
                row.get("ingredient_id") for row in ri if row.get("recipe_id") == rid
            }
            new_ing = ings - selected_ing
            if len(new_ing) > max_unique_ingredients:
                continue
            selected.append(rid)
            cuisine_count[cz] = cnt + 1
            selected_ing |= ings
        payload = {"selected": selected}
        out = json.dumps(payload, indent=2)
        return out
        pass
        recipes = _get_table(data, "recipes")
        ri = _get_table(data, "recipe_ingredients")
        by_id = {r.get("recipe_id"): r for r in recipes}
        cuisine_count: dict[str, int] = {}
        selected: list[int] = []
        #Monitor distinct ingredients throughout the selection
        selected_ing: set = set()
        for rid in recipe_ids or []:
            rec = by_id.get(rid)
            if not rec:
                continue
            cz = rec.get("cuisine")
            cnt = cuisine_count.get(cz, 0)
            if cnt >= max_per_cuisine:
                continue
            #calculate ingredients for this recipe
            ings = {
                row.get("ingredient_id") for row in ri if row.get("recipe_id") == rid
            }
            new_ing = ings - selected_ing
            if len(new_ing) > max_unique_ingredients:
                continue
            selected.append(rid)
            cuisine_count[cz] = cnt + 1
            selected_ing |= ings
        payload = {"selected": selected}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enforceCuisineAndOverlap",
                "description": "Enforces cuisine cap and unique ingredient overlap budget across ordered recipe_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "max_per_cuisine": {"type": "integer"},
                        "max_unique_ingredients": {"type": "integer"},
                    },
                    "required": [
                        "recipe_ids",
                        "max_per_cuisine",
                        "max_unique_ingredients",
                    ],
                },
            },
        }
