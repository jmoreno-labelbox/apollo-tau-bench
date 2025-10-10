# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppendMealHistory(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        plan_date: str,
        recipe_id: int,
        was_prepared: bool,
        rating_int: Optional[int] = None,
    ) -> str:
        tbl = _tbl(data, "meal_history")
        next_id = _max_id(tbl, "history_id", 6200) + 1
        row = {
            "history_id": next_id,
            "household_id": int(household_id),
            "plan_date": str(plan_date),
            "recipe_id": int(recipe_id),
            "was_prepared": bool(was_prepared),
            "rating_int": int(rating_int) if rating_int is not None else None,
        }
        tbl.append(row)
        return json({"history_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_meal_history",
                "description": "Append meal_history row and return history_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "plan_date": {"type": "string"},
                        "recipe_id": {"type": "integer"},
                        "was_prepared": {"type": "boolean"},
                        "rating_int": {"type": "integer"},
                    },
                    "required": ["household_id", "plan_date", "recipe_id", "was_prepared"],
                },
            },
        }
