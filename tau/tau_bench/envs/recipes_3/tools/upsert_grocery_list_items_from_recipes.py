# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpsertGroceryListItemsFromRecipes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int, recipe_ids: List[int]) -> str:
        gli_tbl = _tbl(data, "grocery_list_items")
        gli_tbl[:] = [r for r in gli_tbl if int(r.get("list_id")) != int(list_id)]
        next_item = _max_id(gli_tbl, "item_id", 8100)
        ri = data.get("recipe_ingredients", [])
        agg: Dict[Tuple[int, str], float] = {}
        for rid in recipe_ids or []:
            rows = [r for r in ri if int(r.get("recipe_id")) == int(rid)]
            for row in rows:
                iid = int(row.get("ingredient_id"))
                unit = str(row.get("unit"))
                qty = float(row.get("quantity", 0))
                agg[(iid, unit)] = agg.get((iid, unit), 0.0) + qty
        created_ids: List[int] = []
        for (iid, unit), qty in agg.items():
            next_item += 1
            ing = _ingredient_by_id(data, iid)
            rec = {
                "item_id": next_item,
                "list_id": int(list_id),
                "ingredient_id": int(iid),
                "quantity": float(qty),
                "unit": unit,
                "grocery_section": (ing or {}).get("grocery_section", "Misc"),
                "pantry_staple_flag": bool((ing or {}).get("pantry_staple_flag", False)),
                "overlap_last_month_flag": False,
            }
            gli_tbl.append(rec)
            created_ids.append(next_item)
        # Deterministic header write to ensure write semantics even if no items created
        gl = _require(data, "grocery_lists", "list_id", int(list_id))
        if gl is not None:
            gl["last_upserted_at"] = "2025-01-01T12:05:00"
        return json({"created_item_ids": created_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_grocery_list_items_from_recipes",
                "description": "Replace list items by consolidating ingredients for recipe_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                    },
                    "required": ["list_id", "recipe_ids"],
                },
            },
        }
