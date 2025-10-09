from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetViewershipForCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, date: str = None) -> str:
        cat = category
        d = date
        for r in data.get("f_viewership", []):
            if r.get("category") == cat and r.get("date") == d:
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": "viewership_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetViewershipForCategory",
                "description": "Gets viewership for a category on a date.",
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
