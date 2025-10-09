from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateMealPlanEntryNotes(Tool):
    """Modifies the notes for a particular meal plan entry."""

    @staticmethod
    def invoke(data: dict[str, Any], entry_id: str = None, new_notes: str = None) -> str:
        entries = data.get("meal_plan_entries", {}).values()
        for entry in entries:
            if entry.get("entry_id") == entry_id:
                entry["notes"] = new_notes
                payload = entry
                out = json.dumps(payload)
                return out
        payload = {"error": f"Meal plan entry with ID '{entry_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateMealPlanEntryNotes",
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
