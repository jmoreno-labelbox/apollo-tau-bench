# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpsertGroceryListItemsForPlanByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, week_start_date: str, recipe_ids: List[int]
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return json.dumps({"error": "meal_plan not found for keys"})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return json.dumps({"error": "grocery_list not found for plan"})
        gli_tbl = _tbl(data, "grocery_list_items")
        gli_tbl[:] = [r for r in gli_tbl if int(r.get("list_id")) != int(gl.get("list_id"))]
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
                "list_id": int(gl.get("list_id")),
                "ingredient_id": int(iid),
                "quantity": float(qty),
                "unit": unit,
                "grocery_section": (ing or {}).get("grocery_section", "Misc"),
                "pantry_staple_flag": bool((ing or {}).get("pantry_staple_flag", False)),
                "overlap_last_month_flag": False,
            }
            gli_tbl.append(rec)
            created_ids.append(next_item)
        gl["last_upserted_at"] = "2025-01-01T12:05:00"
        return json.dumps({"created_item_ids": created_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_grocery_list_items_for_plan_by_keys",
                "description": "Replace grocery_list_items for list linked to (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                    },
                    "required": ["household_id", "week_start_date", "recipe_ids"],
                },
            },
        }
