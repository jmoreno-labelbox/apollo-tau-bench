# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


class ListRecentMealHistory(Tool):
    """Return recipe_ids from meal_history for household within last N days (anchor_date optional)."""
    @staticmethod
    def invoke(data: Dict[str, Any], anchor_date, days_back, household_id) -> str:
        if household_id is None or days_back is None:
            return _json_dump({"error": "household_id and days_back are required"})
        from datetime import date, timedelta
        if anchor_date:
            y, m, d = [int(x) for x in str(anchor_date).split("-")]
            end = date(y, m, d)
        else:
            hh = [h for h in list(data.get("meal_history", {}).values()) if int(h.get("household_id")) == int(household_id)]
            if hh:
                md = max(str(h["plan_date"]) for h in hh)
                y, m, d = [int(x) for x in md.split("-")]
                end = date(y, m, d)
            else:
                end = date(2025, 1, 1)
        start = end - timedelta(days=int(days_back))
        out = [
            int(r.get("recipe_id"))
            for r in list(data.get("meal_history", {}).values())
            if int(r.get("household_id")) == int(household_id) and str(r.get("plan_date")) >= start.isoformat()
        ]
        return _json_dump({"household_id": household_id, "days_back": days_back, "recent_recipe_ids": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "list_recent_meal_history",
            "description": "List recent recipe_ids from meal_history for a household.",
            "parameters": {"type": "object", "properties": {
                "household_id": {"type": "integer"},
                "days_back": {"type": "integer"},
                "anchor_date": {"type": "string"}
            }, "required": ["household_id", "days_back"]}
        }}
