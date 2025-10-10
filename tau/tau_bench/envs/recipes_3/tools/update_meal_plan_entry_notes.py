# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateMealPlanEntryNotes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], meal_plan_id: int, notes_map: Dict[str, str]) -> str:
        updated = 0
        for e in data.get("meal_plan_entries", []):
            if int(e.get("meal_plan_id")) != int(meal_plan_id):
                continue
            rid_key = str(e.get("recipe_id"))
            if rid_key in (notes_map or {}):
                e["notes"] = notes_map[rid_key]
                updated += 1
        # Deterministic header write to ensure write semantics even if no entries updated
        plan = _require(data, "meal_plans", "meal_plan_id", int(meal_plan_id))
        if plan is not None:
            plan["notes_last_updated_at"] = "2025-01-01T00:00:00"
        return json({"updated_entries": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_meal_plan_entry_notes",
                "description": "Update notes for entries using a recipe_id->note map.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "notes_map": {"type": "object"},
                    },
                    "required": ["meal_plan_id", "notes_map"],
                },
            },
        }
