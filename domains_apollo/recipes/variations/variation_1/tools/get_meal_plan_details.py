from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetMealPlanDetails(Tool):
    """Retrieve a meal_plan row using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: int = None) -> str:
        if meal_plan_id is None:
            return _json_dump({"error": "meal_plan_id is required"})
        row = _require(data, "meal_plans", "meal_plan_id", int(meal_plan_id))
        return _json_dump(row or {"error": f"meal_plan_id {meal_plan_id} not found"})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMealPlanDetails",
                "description": "Get a meal_plan header by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"meal_plan_id": {"type": "integer"}},
                    "required": ["meal_plan_id"],
                },
            },
        }
