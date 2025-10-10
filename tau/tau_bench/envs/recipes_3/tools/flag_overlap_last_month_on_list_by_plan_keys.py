# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FlagOverlapLastMonthOnListByPlanKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, week_start_date: str, anchor_date: str
    ) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return _json({"flagged_item_ids": [], "matched_count": 0})
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return _json({"flagged_item_ids": [], "matched_count": 0})
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
        matched = 0
        flagged_ids: List[int] = []
        # Update database: set recent_overlap_flag on items with recent overlap
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(gl.get("list_id")):
                continue
            if int(it.get("ingredient_id")) in recent_iids:
                it["recent_overlap_flag"] = True
                matched += 1
                flagged_ids.append(int(it.get("item_id")))
            else:
                it["recent_overlap_flag"] = False
        # Update grocery list timestamp
        gl["last_overlap_flagged_at"] = "2025-01-01T12:20:00"
        return _json({"flagged_item_ids": flagged_ids, "matched_count": matched})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "flag_overlap_last_month_on_list_by_plan_keys",
                "description": "Flag items with recent overlap by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "anchor_date": {"type": "string"},
                    },
                    "required": ["household_id", "week_start_date", "anchor_date"],
                },
            },
        }
