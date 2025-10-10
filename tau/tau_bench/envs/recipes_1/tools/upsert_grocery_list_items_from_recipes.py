# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpsertGroceryListItemsFromRecipes(Tool):
    """Replace all items for list_id with the aggregated ingredients from recipe_ids_json."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        recipe_ids_json = kwargs.get("recipe_ids_json", "[]")
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        recipe_ids = _parse_json_list_ids(recipe_ids_json)
        ri = _collect_recipe_ingredients(data, recipe_ids)
        items = _sum_grocery_items(ri)

        # remove old
        gli_tbl = data.setdefault("grocery_list_items", [])
        gli_tbl[:] = [r for r in gli_tbl if int(r.get("list_id")) != int(list_id)]

        # insert new
        next_id = _max_id(gli_tbl, "item_id", 8100)
        created_ids: List[int] = []
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
                "pantry_staple_flag": bool((ing or {}).get("pantry_staple_flag", False)),
                "overlap_last_month_flag": False
            }
            gli_tbl.append(row)
            created_ids.append(next_id)
        return _json_dump({"created_item_ids": created_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"upsert_grocery_list_items_from_recipes",
            "description":"Replace list items with aggregation from the provided recipe_ids.",
            "parameters":{"type":"object","properties":{
                "list_id":{"type":"integer"},
                "recipe_ids_json":{"type":"string"}
            },"required":["list_id","recipe_ids_json"]}
        }}
