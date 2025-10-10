# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BulkAddMealPlanEntries(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        meal_plan_id: int,
        week_start_date: str,
        recipe_ids: List[int],
        servings_adult: int,
        servings_child: int,
    ) -> str:
        dates = _week_dates(str(week_start_date))
        tbl = _tbl(data, "meal_plan_entries")
        next_id = _max_id(tbl, "entry_id", 6100)
        created: List[int] = []
        for i, rid in enumerate((recipe_ids or [])[:7]):
            next_id += 1
            row = {
                "entry_id": next_id,
                "meal_plan_id": int(meal_plan_id),
                "plan_date": dates[i] if i < len(dates) else dates[-1],
                "meal_type": "Dinner",
                "recipe_id": int(rid),
                "servings_adult": int(servings_adult),
                "servings_child": int(servings_child),
                "notes": "",
            }
            tbl.append(row)
            created.append(next_id)
        # Deterministic header writing to maintain write semantics regardless of entry additions.
        plan = _require(data, "meal_plans", "meal_plan_id", int(meal_plan_id))
        if plan is not None:
            plan["entries_last_set_at"] = "2025-01-01T00:00:00"
        return json.dumps({"created_entry_ids": created})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "bulk_add_meal_plan_entries",
                "description": "Insert 7 Dinner entries for a meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "servings_adult": {"type": "integer"},
                        "servings_child": {"type": "integer"},
                    },
                    "required": [
                        "meal_plan_id",
                        "week_start_date",
                        "recipe_ids",
                        "servings_adult",
                        "servings_child",
                    ],
                },
            },
        }
