# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


class UpdateMealPlanEntryNotes(Tool):
    """Set entry notes via a mapping {recipe_id: note} for a given meal_plan_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        notes_map = kwargs.get("notes_map")
        if meal_plan_id is None or not isinstance(notes_map, dict):
            return _json_dump({"error": "meal_plan_id and notes_map are required"})
        updated = 0
        for e in list(data.get("meal_plan_entries", {}).values()):
            if int(e.get("meal_plan_id")) != int(meal_plan_id):
                continue
            rid = str(e.get("recipe_id"))
            if rid in notes_map:
                e["notes"] = notes_map[rid]
                updated += 1
        return _json_dump({"updated_entries": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_meal_plan_entry_notes",
            "description":"Update notes for entries in a meal plan using a recipe_id->note map.",
            "parameters":{"type":"object","properties":{
                "meal_plan_id":{"type":"integer"},
                "notes_map":{"type":"object"}
            },"required":["meal_plan_id","notes_map"]}
        }}
