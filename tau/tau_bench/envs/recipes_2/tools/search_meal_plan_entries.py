from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchMealPlanEntries(Tool):
    """Looks for meal plan entries in a specific plan and date range that have a substring in their notes."""

    @staticmethod
    def invoke(data: dict[str, Any], meal_plan_id: str = None, start_date: str = None, end_date: str = None, notes_substring: str = None) -> str:
        if not all([meal_plan_id, start_date, end_date, notes_substring]):
            payload = {
                    "error": "meal_plan_id, start_date, end_date, and notes_substring are required parameters."
                }
            out = json.dumps(
                payload)
            return out
        meal_plan_entries = data.get("meal_plan_entries", [])
        matching_entries = []
        for entry in meal_plan_entries:
            if entry.get("meal_plan_id") != meal_plan_id:
                continue
            plan_date = entry.get("plan_date", "")
            if not (start_date <= plan_date <= end_date):
                continue
            notes = entry.get("notes", "")
            if notes and notes_substring.lower() in notes.lower():
                matching_entries.append(entry)
        payload = matching_entries
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchMealPlanEntries",
                "description": "Searches for meal plan entries within a specific plan and date range that contain a substring in their notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {
                            "type": "integer",
                            "description": "The unique ID of the meal plan to search within.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the search range (YYYY-MM-DD).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the search range (YYYY-MM-DD).",
                        },
                        "notes_substring": {
                            "type": "string",
                            "description": "The text to search for within the entry notes.",
                        },
                    },
                    "required": [
                        "meal_plan_id",
                        "start_date",
                        "end_date",
                        "notes_substring",
                    ],
                },
            },
        }
