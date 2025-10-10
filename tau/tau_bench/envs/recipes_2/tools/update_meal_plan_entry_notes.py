# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateMealPlanEntryNotes(Tool):
    """Updates the notes for a specific meal plan entry."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        entry_id = kwargs.get("entry_id")
        new_notes = kwargs.get("new_notes")

        entries = list(data.get("meal_plan_entries", {}).values())
        for entry in entries:
            if entry.get("entry_id") == entry_id:
                entry["notes"] = new_notes
                return json.dumps(entry)
        return json.dumps({"error": f"Meal plan entry with ID '{entry_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_meal_plan_entry_notes",
                "description": "Updates the notes for a specific meal plan entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entry_id": {"type": "integer"},
                        "new_notes": {"type": "string"},
                    },
                    "required": ["entry_id", "new_notes"],
                },
            },
        }
