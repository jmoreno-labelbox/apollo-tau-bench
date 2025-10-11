# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGroceryListBySourcePlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], source_meal_plan_id: int) -> str:
        row = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(source_meal_plan_id)
            ),
            None,
        )
        return json.dumps({"grocery_list": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_list_by_source_plan",
                "description": "Find grocery_list linked to a meal_plan via source_meal_plan_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"source_meal_plan_id": {"type": "integer"}},
                    "required": ["source_meal_plan_id"],
                },
            },
        }
