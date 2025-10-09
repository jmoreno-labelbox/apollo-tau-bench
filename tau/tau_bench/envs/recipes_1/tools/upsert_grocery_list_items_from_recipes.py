from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertGroceryListItemsFromRecipes(Tool):
    """Substitute all items for list_id with the combined ingredients from recipe_ids_json."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, recipe_ids_json: str = "[]") -> str:
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        recipe_ids = _parse_json_list_ids(recipe_ids_json)
        ri = _collect_recipe_ingredients(data, recipe_ids)
        items = _sum_grocery_items(ri)

        #delete old
        gli_tbl = data.setdefault("grocery_list_items", [])
        gli_tbl[:] = [r for r in gli_tbl.values() if int(r.get("list_id")) != int(list_id)]

        #add new
        next_id = _max_id(gli_tbl, "item_id", 8100)
        created_ids: list[int] = []
        for it in items:
            next_id += 1
            ing = _ingredient_by_id(data, int(it["ingredient_id"]))
            row = {
                "item_id": next_id,
                "list_id": int(list_id),
                "ingredient_id": int(it["ingredient_id"]),
                "quantity": float(it["quantity"]),
                "unit": str(it["unit"]),
                "grocery_section": (ing or {}).get("grocery_section", "Misc"),
                "pantry_staple_flag": bool(
                    (ing or {}).get("pantry_staple_flag", False)
                ),
                "overlap_last_month_flag": False,
            }
            gli_tbl.append(row)
            created_ids.append(next_id)
        return _json_dump({"created_item_ids": created_ids})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertGroceryListItemsFromRecipes",
                "description": "Replace list items with aggregation from the provided recipe_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "recipe_ids_json": {"type": "string"},
                    },
                    "required": ["list_id", "recipe_ids_json"],
                },
            },
        }
