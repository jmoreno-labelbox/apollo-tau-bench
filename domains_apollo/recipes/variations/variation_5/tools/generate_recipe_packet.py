from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class GenerateRecipePacket(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: int = None) -> str:
        if meal_plan_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            meal_plan_id = _latest_meal_plan_id(data, household_id)
        if meal_plan_id is None:
            return _json_dump({"error": "no meal_plan available"})
        uri = f"packet://meal_plan/{int(meal_plan_id)}"
        return _json_dump({"packet_uri": uri})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateRecipePacket",
                "description": "Produce a deterministic packet URI; defaults to latest meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {"meal_plan_id": {"type": "integer"}},
                    "required": [],
                },
            },
        }
