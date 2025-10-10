# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id


class ListRecentMealHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        days_back = int(kwargs.get("days_back", 14))
        anchor_date = kwargs.get("anchor_date")
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        out = _recent_recipe_ids(data, household_id, days_back, anchor_date)
        return _json_dump({"household_id": household_id, "days_back": days_back, "recent_recipe_ids": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"list_recent_meal_history","description":"Return recent recipe_ids; defaults to last 14 days for default household.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"},"days_back":{"type":"integer"},"anchor_date":{"type":"string"}},"required":[]}}}
