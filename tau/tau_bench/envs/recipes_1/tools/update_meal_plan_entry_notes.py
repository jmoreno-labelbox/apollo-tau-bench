from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateMealPlanEntryNotes(Tool):
    """Assign entry notes using a mapping {recipe_id: note} for a specified meal_plan_id."""

    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: int = None, notes_map: dict = None) -> str:
        if meal_plan_id is None or not isinstance(notes_map, dict):
            return _json_dump({"error": "meal_plan_id and notes_map are required"})
        updated = 0
        for e in data.get("meal_plan_entries", {}).values():
            if int(e.get("meal_plan_id")) != int(meal_plan_id):
                continue
            rid = str(e.get("recipe_id"))
            if rid in notes_map:
                e["notes"] = notes_map[rid]
                updated += 1
        return _json_dump({"updated_entries": updated})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateMealPlanEntryNotes",
                "description": "Update notes for entries in a meal plan using a recipe_id->note map.",
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
