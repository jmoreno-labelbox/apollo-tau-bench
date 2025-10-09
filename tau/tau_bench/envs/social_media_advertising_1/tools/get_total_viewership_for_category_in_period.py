from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTotalViewershipForCategoryInPeriod(Tool):
    """Computes total viewership for a category within a date range."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None, end_date: str = None) -> str:
        viewership_data = data.get("f_viewership", [])

        total_sessions = 0
        total_active_users = 0

        for entry in viewership_data:
            if (
                entry.get("category") == category
                and start_date <= entry.get("date") <= end_date
            ):
                total_sessions += entry.get("sessions", 0)
                total_active_users += entry.get("active_users", 0)
        payload = {"total_sessions": total_sessions, "total_active_users": total_active_users}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTotalViewershipForCategoryInPeriod",
                "description": "Calculates total viewership for a category over a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to analyze.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the period (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the period (YYYY-MM-DD format).",
                        },
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }
