# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _max_id, _json_dump










def _plan_week_dates(week_start_date: str) -> List[str]:
    # Deterministic: generate 7 consecutive ISO dates from a start date YYYY-MM-DD
    from datetime import date, timedelta
    y, m, d = [int(x) for x in str(week_start_date).split("-")]
    start = date(y, m, d)
    return [(start + timedelta(days=i)).isoformat() for i in range(7)]

def _parse_json_list_ids(json_str: str) -> List[int]:
    try:
        arr = json.loads(json_str)
        if isinstance(arr, list):
            return [int(x) for x in arr]
    except Exception:
        pass
    return []

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

class BulkAddMealPlanEntries(Tool):
    """Create Dinner entries for a week using ordered recipe_ids_json; returns entry_ids."""
    @staticmethod
    def invoke(data: Dict[str, Any], meal_plan_id, week_start_date, selected_recipe_ids_json = "[]") -> str:
        if meal_plan_id is None or not week_start_date or not selected_recipe_ids_json:
            return _json_dump({"error": "meal_plan_id, week_start_date, selected_recipe_ids_json are required"})
        recipes = _parse_json_list_ids(selected_recipe_ids_json)
        if not recipes:
            return _json_dump({"error": "no recipes provided"})
        dates = _plan_week_dates(str(week_start_date))
        tbl = data.setdefault("meal_plan_entries", [])
        next_id = _max_id(tbl, "entry_id", 6100)
        created: List[int] = []
        for i, rid in enumerate(recipes[:7]):
            next_id += 1
            row = {
                "entry_id": next_id,
                "meal_plan_id": int(meal_plan_id),
                "plan_date": dates[i] if i < len(dates) else dates[-1],
                "meal_type": "Dinner",
                "recipe_id": int(rid),
                "servings_adult": 2,
                "servings_child": 1,
                "notes": ""
            }
            tbl.append(row)
            created.append(next_id)
        return _json_dump({"created_entry_ids": created})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"bulk_add_meal_plan_entries",
            "description":"Insert a week of Dinner entries for a meal plan.",
            "parameters":{"type":"object","properties":{
                "meal_plan_id":{"type":"integer"},
                "week_start_date":{"type":"string"},
                "selected_recipe_ids_json":{"type":"string"}
            },"required":["meal_plan_id","week_start_date","selected_recipe_ids_json"]}
        }}