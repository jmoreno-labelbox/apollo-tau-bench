# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require, _json_dump






def _require(data: Dict[str, Any], table: str, key: str, value: Any) -> Optional[Dict[str, Any]]:
    row = next((r for r in data.get(table, []) if r.get(key) == value), None)
    return row

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

class GetMealPlanDetails(Tool):
    """Return a meal_plan row by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], meal_plan_id) -> str:
        if meal_plan_id is None:
            return _json_dump({"error": "meal_plan_id is required"})
        row = _require(data, "meal_plans", "meal_plan_id", int(meal_plan_id))
        return _json_dump(row or {"error": f"meal_plan_id {meal_plan_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_meal_plan_details",
            "description":"Get a meal_plan header by id.",
            "parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"}},"required":["meal_plan_id"]}
        }}