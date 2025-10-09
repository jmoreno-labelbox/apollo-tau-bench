from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FlagOverlapLastMonthOnList(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: str = None, household_id: str = None, anchor_date: str = None) -> str:
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        if list_id is None:
            list_id = _latest_list_id(data, household_id)
        if list_id is None or household_id is None:
            return _json_dump({"updated_items": 0})
        recent_ingrs = {
            row["ingredient_id"]
            for row in _collect_recipe_ingredients(
                data, _recent_recipe_ids(data, household_id, 30, anchor_date)
            )
        }
        cnt = 0
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            item["overlap_last_month_flag"] = (
                int(item.get("ingredient_id")) in recent_ingrs
            )
            cnt += 1
        return _json_dump({"updated_items": cnt})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FlagOverlapLastMonthOnList",
                "description": "Mark grocery items that overlap with last 30 days; defaults to latest list and household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "household_id": {"type": "integer"},
                        "anchor_date": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
