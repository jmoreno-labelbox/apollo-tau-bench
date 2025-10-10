# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchHouseholdsByName(Tool):
    """Searches for households with names containing the specified text."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name_query")
        if not name_query:
            return json.dumps({"error": "name_query parameter is required."})
        households = data.get("households", [])
        matching_households = [
            household for household in households 
            if name_query.lower() in household.get("household_name", "").lower()
        ]
        return json.dumps(matching_households)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_households_by_name",
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
