from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchHouseholdsByName(Tool):
    """Looks for households whose names include the given text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        if not name_query:
            payload = {"error": "name_query parameter is required."}
            out = json.dumps(payload)
            return out
        households = data.get("households", {}).values()
        matching_households = [
            household
            for household in households.values() if name_query.lower() in household.get("household_name", "").lower()
        ]
        payload = matching_households
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchHouseholdsByName",
                "description": "Searches for households with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in household names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }
