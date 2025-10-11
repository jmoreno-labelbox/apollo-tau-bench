# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _max_id, _json_dump






def _max_id(records: List[Dict[str, Any]], key: str, default: int) -> int:
    if not records:
        return default
    vals = []
    for r in records:
        try:
            vals.append(int(r.get(key)))
        except Exception:
            pass
    return max(vals) if vals else default

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

class CreateMealPlan(Tool):
    """Insert a new meal_plan row and return meal_plan_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], created_by_user_id, household_id, week_start_date) -> str:
        if household_id is None or created_by_user_id is None or not week_start_date:
            return _json_dump({"error": "household_id, week_start_date, created_by_user_id are required"})
        tbl = data.setdefault("meal_plans", [])
        next_id = _max_id(tbl, "meal_plan_id", 6000) + 1
        row = {
            "meal_plan_id": next_id,
            "household_id": int(household_id),
            "week_start_date": str(week_start_date),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T00:00:00Z"
        }
        tbl.append(row)
        return _json_dump({"meal_plan_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_meal_plan",
            "description":"Create a new meal plan (header).",
            "parameters":{"type":"object","properties":{
                "household_id":{"type":"integer"},
                "week_start_date":{"type":"string"},
                "created_by_user_id":{"type":"integer"}
            },"required":["household_id","week_start_date","created_by_user_id"]}
        }}