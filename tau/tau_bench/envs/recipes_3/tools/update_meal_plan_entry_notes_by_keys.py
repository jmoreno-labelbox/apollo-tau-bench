# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateMealPlanEntryNotesByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, week_start_date: str, notes_map: Dict[str, str]
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
            return _json({"error": "meal_plan not found for keys"})
        updated = 0
        for e in data.get("meal_plan_entries", []):
            if int(e.get("meal_plan_id")) != int(plan.get("meal_plan_id")):
                continue
            rid_key = str(e.get("recipe_id"))
            if rid_key in (notes_map or {}):
                e["notes"] = notes_map[rid_key]
                updated += 1
        plan["notes_last_updated_at"] = "2025-01-01T00:00:00"
        return _json({"updated_entries": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_meal_plan_entry_notes_by_keys",
                "description": "Update notes for entries by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "notes_map": {"type": "object"},
                    },
                    "required": ["household_id", "week_start_date", "notes_map"],
                },
            },
        }
