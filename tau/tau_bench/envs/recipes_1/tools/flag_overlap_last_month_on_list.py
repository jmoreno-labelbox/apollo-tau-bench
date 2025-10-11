# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump








def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _collect_recipe_ingredients(data: Dict[str, Any], recipe_ids: List[int]) -> List[Dict[str, Any]]:
    ri = data.get("recipe_ingredients", [])
    ridset = set(recipe_ids)
    return [row for row in ri if int(row.get("recipe_id")) in ridset]

class ListRecentMealHistory(Tool):
    """Return recipe_ids from meal_history for household within last N days (anchor_date optional)."""
    @staticmethod
    def invoke(data: Dict[str, Any], household_id, days_back, anchor_date) -> str:
        if household_id is None or days_back is None:
            return _json_dump({"error": "household_id and days_back are required"})
        from datetime import date, timedelta
        if anchor_date:
            y, m, d = [int(x) for x in str(anchor_date).split("-")]
            end = date(y, m, d)
        else:
            hh = [h for h in data.get("meal_history", []) if int(h.get("household_id")) == int(household_id)]
            if hh:
                md = max(str(h["plan_date"]) for h in hh)
                y, m, d = [int(x) for x in md.split("-")]
                end = date(y, m, d)
            else:
                end = date(2025, 1, 1)
        start = end - timedelta(days=int(days_back))
        out = [
            int(r.get("recipe_id"))
            for r in data.get("meal_history", [])
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

class FlagOverlapLastMonthOnList(Tool):
    """Mark overlap_last_month_flag if ingredient appeared in recipes cooked in last 30 days."""
    @staticmethod
    def invoke(data: Dict[str, Any], anchor_date, household_id, list_id) -> str:
        if list_id is None or household_id is None:
            return _json_dump({"error": "list_id and household_id are required"})
        lr = json.loads(ListRecentMealHistory.invoke(data, household_id=household_id, days_back=30, anchor_date=anchor_date))
        recent = [int(x) for x in lr.get("recent_recipe_ids", [])]
        ingr_recent = set(int(r["ingredient_id"]) for r in _collect_recipe_ingredients(data, recent))
        updated = 0
        for item in list(data.get("grocery_list_items", {}).values()):
            if int(item.get("list_id")) != int(list_id):
                continue
            item["overlap_last_month_flag"] = int(item.get("ingredient_id")) in ingr_recent
            updated += 1
        return _json_dump({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"flag_overlap_last_month_on_list",
            "description":"Set overlap flag for list items based on last 30 days of meals.",
            "parameters":{"type":"object","properties":{
                "list_id":{"type":"integer"},
                "household_id":{"type":"integer"},
                "anchor_date":{"type":"string"}
            },"required":["list_id","household_id"]}
        }}