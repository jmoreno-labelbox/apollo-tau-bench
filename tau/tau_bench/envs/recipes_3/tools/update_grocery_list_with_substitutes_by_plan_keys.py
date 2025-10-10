# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateGroceryListWithSubstitutesByPlanKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        week_start_date: str,
        substitutions: List[Dict[str, Any]],
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
        mapping = {
            int(s["ingredient_id"]): int(s["substitute_ingredient_id"])
            for s in substitutions
            if "ingredient_id" in s and "substitute_ingredient_id" in s
        }
        updated = 0
        validated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(gl.get("list_id")):
                continue
            iid = int(it.get("ingredient_id"))
            if iid in mapping:
                new_iid = mapping[iid]
                it["ingredient_id"] = new_iid
                ing = _ingredient_by_id(data, new_iid)
                it["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
                updated += 1
            # Flag all items as validated regardless of whether any substitution was made.
            it["substitutions_validated"] = True
            validated += 1
        gl["last_substitutions_applied_at"] = "2025-01-01T12:25:00"
        return json.dumps({"updated_items": updated, "validated_items": validated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_grocery_list_with_substitutes_by_plan_keys",
                "description": "Apply substitutions to grocery_list_items linked to (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "substitutions": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["household_id", "week_start_date", "substitutions"],
                },
            },
        }
