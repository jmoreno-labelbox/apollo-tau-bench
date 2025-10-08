from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class ListRecentMealHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None, days_back: int = 14, anchor_date: str = None) -> str:
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        out = _recent_recipe_ids(data, household_id, days_back, anchor_date)
        return _json_dump(
            {
                "household_id": household_id,
                "days_back": days_back,
                "recent_recipe_ids": out,
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRecentMealHistory",
                "description": "Return recent recipe_ids; defaults to last 14 days for default household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "days_back": {"type": "integer"},
                        "anchor_date": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
