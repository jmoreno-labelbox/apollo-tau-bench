# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRecentMealHistory(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, days_back: int, anchor_date: Optional[str] = None
    ) -> str:
        from datetime import date, timedelta

        if anchor_date:
            y, m, d = [int(x) for x in str(anchor_date).split("-")]
            end = date(y, m, d)
        else:
            rows = [
                h
                for h in data.get("meal_history", [])
                if int(h.get("household_id")) == int(household_id)
            ]
            if rows:
                max_date = max(str(r.get("plan_date")) for r in rows)
                y, m, d = [int(x) for x in max_date.split("-")]
                end = date(y, m, d)
            else:
                end = date(2025, 1, 1)
        start = end - timedelta(days=int(days_back))
        rids = [
            int(r.get("recipe_id"))
            for r in data.get("meal_history", [])
            if int(r.get("household_id")) == int(household_id)
            and str(r.get("plan_date")) >= start.isoformat()
        ]
        return _json({"recent_recipe_ids": rids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_recent_meal_history",
                "description": "List recent recipe_ids for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "days_back": {"type": "integer"},
                        "anchor_date": {"type": "string"},
                    },
                    "required": ["household_id", "days_back"],
                },
            },
        }
