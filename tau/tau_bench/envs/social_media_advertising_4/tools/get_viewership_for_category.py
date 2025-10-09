from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetViewershipForCategory(Tool):
    """Obtains user engagement statistics for a category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, report_date: str = None,
    date: Any = None,
    ) -> str:
        for record in data.get("f_viewership", []):
            if record.get("category") == category and record.get("date") == report_date:
                payload = record
                out = json.dumps(payload)
                return out
        payload = {"error": "Viewership data not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetViewershipForCategory",
                "description": "Retrieves user session and engagement data for a category on a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["category", "date"],
                },
            },
        }
