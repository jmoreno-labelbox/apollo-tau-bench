from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetWeeklySalesByCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None) -> str:
        cat = category
        start = start_date
        for r in data.get("f_sales", {}).values():
            if r.get("category") == cat and r.get("start_date") == start:
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": "sales_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWeeklySalesByCategory",
                "description": "Gets weekly sales for a category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string"},
                        "start_date": {"type": "string"},
                    },
                    "required": ["category", "start_date"],
                },
            },
        }
