# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchMealPlanEntries(Tool):
    """Searches for meal plan entries within a specific plan and date range that contain a substring in their notes."""
    @staticmethod
    def invoke(data: Dict[str, Any], end_date, meal_plan_id, notes_substring, start_date) -> str:
        if not all([meal_plan_id, start_date, end_date, notes_substring]):
            return json.dumps({"error": "meal_plan_id, start_date, end_date, and notes_substring are required parameters."})
        meal_plan_entries = list(data.get("meal_plan_entries", {}).values())
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
        return json.dumps(matching_entries)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_meal_plan_entries",
                "description": "Searches for meal plan entries within a specific plan and date range that contain a substring in their notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer", "description": "The unique ID of the meal plan to search within."},
                        "start_date": {"type": "string", "description": "The start date of the search range (YYYY-MM-DD)."},
                        "end_date": {"type": "string", "description": "The end date of the search range (YYYY-MM-DD)."},
                        "notes_substring": {"type": "string", "description": "The text to search for within the entry notes."},
                    },
                    "required": ["meal_plan_id", "start_date", "end_date", "notes_substring"],
                },
            },
        }
