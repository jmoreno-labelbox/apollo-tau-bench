# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMealPlansByHouseholdId(Tool):
    """Retrieves all meal plans for a specific household ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        if household_id is None:
            return json.dumps({"error": "household_id parameter is required."})
        meal_plans = list(data.get("meal_plans", {}).values())
        matching_plans = [plan for plan in meal_plans if plan.get("household_id") == household_id]
        return json.dumps(matching_plans)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_meal_plans_by_household_id",
                "description": "Retrieves all meal plans for a specific household ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer", "description": "The unique ID of the household."}},
                    "required": ["household_id"],
                },
            },
        }
