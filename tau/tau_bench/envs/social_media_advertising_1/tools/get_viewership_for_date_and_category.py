# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetViewershipForDateAndCategory(Tool):
    """Retrieves viewership data for a specific date and category."""

    @staticmethod
    def invoke(data: Dict[str, Any], category, date) -> str:
        viewership_data = list(data.get("f_viewership", {}).values())
        
        for entry in viewership_data:
            if entry.get("date") == date and entry.get("category") == category:
                return json.dumps({
                    "sessions": entry.get("sessions"),
                    "active_users": entry.get("active_users")
                })
        
        return json.dumps({"error": f"No viewership data found for category '{category}' on date '{date}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_viewership_for_date_and_category",
                "description": "Retrieves viewership data for a specific date and category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "The date to get viewership for (YYYY-MM-DD format).",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category to get viewership for.",
                        }
                    },
                    "required": ["date", "category"],
                },
            },
        }
