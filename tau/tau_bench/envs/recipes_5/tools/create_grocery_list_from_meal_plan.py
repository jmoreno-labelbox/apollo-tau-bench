# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id


class CreateGroceryListFromMealPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], created_by_user_id, household_id, meal_plan_id) -> str:
        if created_by_user_id is None:
            created_by_user_id = _first_user_id(data)
        if household_id is None:
            household_id = _default_household_id(data, created_by_user_id)
        if meal_plan_id is None:
            mp = _latest_meal_plan_for_household(data, household_id)
            if mp is None:
                mp_created = json.loads(CreateMealPlan.invoke(data, household_id=household_id, created_by_user_id=created_by_user_id))
                meal_plan_id = int(mp_created["meal_plan_id"])
                BulkAddMealPlanEntries.invoke(data, meal_plan_id=meal_plan_id)
            else:
                meal_plan_id = int(mp["meal_plan_id"])
        entries = [e for e in data.get("meal_plan_entries", []) if e.get("meal_plan_id") == meal_plan_id]
        recipe_ids = [int(e.get("recipe_id")) for e in entries]
        items = _sum_grocery_items(data, recipe_ids)
        gl_tbl = data.get("grocery_lists", [])
        next_list = _max_id(gl_tbl, "list_id", 8000) + 1
        new_gl = {
            "list_id": next_list,
            "household_id": household_id,
            "source_meal_plan_id": meal_plan_id,
            "created_by_user_id": created_by_user_id,
            "created_at": "2025-01-01T12:00:00Z",
            "status_enum": "initialized",
        }
        gl_tbl.append(new_gl)
        gli_tbl = data.get("grocery_list_items", [])
        next_item = _max_id(gli_tbl, "item_id", 8100)
        created_items = []
        for it in items:
            next_item += 1
            ingr = _ingredient_by_id(data, it["ingredient_id"])
            gli = {
                "item_id": next_item,
                "list_id": next_list,
                "ingredient_id": it["ingredient_id"],
                "quantity": it["quantity"],
                "unit": it["unit"],
                "grocery_section": (ingr or {}).get("grocery_section", "Misc"),
                "pantry_staple_flag": bool((ingr or {}).get("pantry_staple_flag", False)),
                "overlap_last_month_flag": False,
            }
            gli_tbl.append(gli)
            created_items.append(next_item)
        return _json_dump({"list_id": next_list, "created_item_ids": created_items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"create_grocery_list_from_meal_plan","description":"Create and populate a grocery list; infers meal plan, household, and creator.","parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"},"household_id":{"type":"integer"},"created_by_user_id":{"type":"integer"}},"required":[]}}}
