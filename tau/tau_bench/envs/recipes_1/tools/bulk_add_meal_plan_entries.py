# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BulkAddMealPlanEntries(Tool):
    """Create Dinner entries for a week using ordered recipe_ids_json; returns entry_ids."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        week_start_date = kwargs.get("week_start_date")
        selected_recipe_ids_json = kwargs.get("selected_recipe_ids_json", "[]")
        if meal_plan_id is None or not week_start_date or not selected_recipe_ids_json:
            return _json_dump({"error": "meal_plan_id, week_start_date, selected_recipe_ids_json are required"})
        recipes = _parse_json_list_ids(selected_recipe_ids_json)
        if not recipes:
            return _json_dump({"error": "no recipes provided"})
        dates = _plan_week_dates(str(week_start_date))
        tbl = data.setdefault("meal_plan_entries", [])
        next_id = _max_id(tbl, "entry_id", 6100)
        created: List[int] = []
        for i, rid in enumerate(recipes[:7]):
            next_id += 1
            row = {
                "entry_id": next_id,
                "meal_plan_id": int(meal_plan_id),
                "plan_date": dates[i] if i < len(dates) else dates[-1],
                "meal_type": "Dinner",
                "recipe_id": int(rid),
                "servings_adult": 2,
                "servings_child": 1,
                "notes": ""
            }
            tbl.append(row)
            created.append(next_id)
        return _json_dump({"created_entry_ids": created})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"bulk_add_meal_plan_entries",
            "description":"Insert a week of Dinner entries for a meal plan.",
            "parameters":{"type":"object","properties":{
                "meal_plan_id":{"type":"integer"},
                "week_start_date":{"type":"string"},
                "selected_recipe_ids_json":{"type":"string"}
            },"required":["meal_plan_id","week_start_date","selected_recipe_ids_json"]}
        }}
