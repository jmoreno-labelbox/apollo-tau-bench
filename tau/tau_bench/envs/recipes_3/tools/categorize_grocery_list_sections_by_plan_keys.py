# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CategorizeGroceryListSectionsByPlanKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, week_start_date: str) -> str:
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
            return json.dumps({"updated_items": 0})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return json.dumps({"updated_items": 0})
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(gl.get("list_id")):
                continue
            ing = _ingredient_by_id(data, int(it.get("ingredient_id")))
            it["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
            updated += 1
        gl["last_categorized_at"] = "2025-01-01T12:10:00"
        return json.dumps({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "categorize_grocery_list_sections_by_plan_keys",
                "description": "Refresh grocery_section for items by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                    },
                    "required": ["household_id", "week_start_date"],
                },
            },
        }
