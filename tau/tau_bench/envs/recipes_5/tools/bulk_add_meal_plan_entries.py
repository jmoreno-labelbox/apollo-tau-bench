# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id


class BulkAddMealPlanEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], meal_plan_id, selected_recipe_ids_json, week_start_date) -> str:
        recipe_ids_json = selected_recipe_ids_json
        if meal_plan_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            created = json.loads(CreateMealPlan.invoke(data, household_id=household_id))
            meal_plan_id = int(created.get("meal_plan_id"))
        if not week_start_date:
            mp_row = next((m for m in data.get("meal_plans", []) if m.get("meal_plan_id") == meal_plan_id), None)
            week_start_date = mp_row.get("week_start_date") if mp_row else _next_week_start_date_for_household(data, _default_household_id(data, _first_user_id(data)))
        recipes = _parse_json_list_ids(recipe_ids_json)
        if not recipes:
            token = BuildRecipeFilters.invoke(data)
            candidates = json.loads(ListRecipesByFilters.invoke(data, filter_token=json.loads(token)["filter_token"]))["candidate_recipe_ids_json"]
            excluded = json.loads(ExcludeRecentRecipes.invoke(data, candidate_recipe_ids_json=candidates))["filtered_recipe_ids_json"]
            limited = json.loads(ApplyCuisineLimit.invoke(data, recipe_ids_json=excluded))["cuisine_limited_recipe_ids_json"]
            ranked = json.loads(RankRecipesForTargets.invoke(data, recipe_ids_json=limited, needed_count=7))["selected_recipe_ids_json"]
            recipes = _parse_json_list_ids(ranked)
        dates = _plan_week_dates(str(week_start_date))
        entries_tbl = data.get("meal_plan_entries", [])
        created_ids: List[int] = []
        next_id = _max_id(entries_tbl, "entry_id", 6100)
        for i, rid in enumerate(recipes[:7]):
            next_id += 1
            row = {
                "entry_id": next_id,
                "meal_plan_id": meal_plan_id,
                "plan_date": dates[i] if i < len(dates) else dates[-1],
                "meal_type": "Dinner",
                "recipe_id": rid,
                "servings_adult": 2,
                "servings_child": 1,
                "notes": ""
            }
            entries_tbl.append(row)
            created_ids.append(next_id)
        return _json_dump({"created_entry_ids": created_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"bulk_add_meal_plan_entries","description":"Insert a week of Dinner entries; defaults to an auto-selected set of recipes.","parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"},"week_start_date":{"type":"string"},"selected_recipe_ids_json":{"type":"string"}},"required":[]}}}
