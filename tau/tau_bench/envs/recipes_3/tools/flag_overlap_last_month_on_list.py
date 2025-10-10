# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FlagOverlapLastMonthOnList(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], list_id: int, household_id: int, anchor_date: Optional[str] = None
    ) -> str:
        from datetime import date, timedelta

        if anchor_date:
            y, m, d = [int(x) for x in str(anchor_date).split("-")]
            end = date(y, m, d)
        else:
            mh_rows = [
                h
                for h in data.get("meal_history", [])
                if int(h.get("household_id")) == int(household_id)
            ]
            if mh_rows:
                max_date = max(str(r.get("plan_date")) for r in mh_rows)
                y, m, d = [int(x) for x in max_date.split("-")]
                end = date(y, m, d)
            else:
                end = date(2025, 1, 1)
        start = end - timedelta(days=30)
        recent_rids = [
            int(r.get("recipe_id"))
            for r in data.get("meal_history", [])
            if int(r.get("household_id")) == int(household_id)
            and str(r.get("plan_date")) >= start.isoformat()
        ]
        recent_iids = set(
            int(r.get("ingredient_id"))
            for r in data.get("recipe_ingredients", [])
            if int(r.get("recipe_id")) in recent_rids
        )
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(list_id):
                continue
            it["overlap_last_month_flag"] = int(it.get("ingredient_id")) in recent_iids
            updated += 1
        # Deterministic header write to ensure write semantics
        gl = _require(data, "grocery_lists", "list_id", int(list_id))
        if gl is not None:
            gl["last_overlap_check_at"] = "2025-01-01T12:20:00"
        return _json({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "flag_overlap_last_month_on_list",
                "description": "Flag items whose ingredient appeared in last 30 days of meals.",
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
