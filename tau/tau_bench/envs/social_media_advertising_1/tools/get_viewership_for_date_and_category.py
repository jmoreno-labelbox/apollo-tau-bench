from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetViewershipForDateAndCategory(Tool):
    """Fetches viewership statistics for a specific date and category."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str = None, category: str = None) -> str:
        viewership_data = data.get("f_viewership", [])

        for entry in viewership_data:
            if entry.get("date") == date and entry.get("category") == category:
                payload = {
                    "sessions": entry.get("sessions"),
                    "active_users": entry.get("active_users"),
                }
                out = json.dumps(payload)
                return out
        payload = {
            "error": f"No viewership data found for category '{category}' on date '{date}'."
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetViewershipForDateAndCategory",
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
                        },
                    },
                    "required": ["date", "category"],
                },
            },
        }
