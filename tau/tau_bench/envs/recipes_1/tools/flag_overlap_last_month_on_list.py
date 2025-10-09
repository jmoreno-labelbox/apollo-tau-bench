from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FlagOverlapLastMonthOnList(Tool):
    """Set overlap_last_month_flag if the ingredient was used in recipes prepared in the last 30 days."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, household_id: int = None, anchor_date: str = None) -> str:
        if list_id is None or household_id is None:
            return _json_dump({"error": "list_id and household_id are required"})
        lr = json.loads(
            ListRecentMealHistory.invoke(
                data, household_id=household_id, days_back=30, anchor_date=anchor_date
            )
        )
        recent = [int(x) for x in lr.get("recent_recipe_ids", [])]
        ingr_recent = {
            int(r["ingredient_id"]) for r in _collect_recipe_ingredients(data, recent)
        }
        updated = 0
        for item in data.get("grocery_list_items", []):
            if int(item.get("list_id")) != int(list_id):
                continue
            item["overlap_last_month_flag"] = (
                int(item.get("ingredient_id")) in ingr_recent
            )
            updated += 1
        return _json_dump({"updated_items": updated})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FlagOverlapLastMonthOnList",
                "description": "Set overlap flag for list items based on last 30 days of meals.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "household_id": {"type": "integer"},
                        "anchor_date": {"type": "string"},
                    },
                    "required": ["list_id", "household_id"],
                },
            },
        }
