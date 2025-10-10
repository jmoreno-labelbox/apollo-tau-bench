# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id


class GenerateRecipePacket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        if meal_plan_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            meal_plan_id = _latest_meal_plan_id(data, household_id)
        if meal_plan_id is None:
            return _json_dump({"error": "no meal_plan available"})
        uri = f"packet://meal_plan/{int(meal_plan_id)}"
        return _json_dump({"packet_uri": uri})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"generate_recipe_packet","description":"Produce a deterministic packet URI; defaults to latest meal plan.","parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"}},"required":[]}}}
