from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetWeeklySalesByCategory(Tool):
    """Fetches weekly sales data for a category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None) -> str:
        for record in data.get("f_sales", {}).values():
            if (
                record.get("category") == category
                and record.get("start_date") == start_date
            ):
                payload = record
                out = json.dumps(payload)
                return out
        payload = {"error": "Sales data not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWeeklySalesByCategory",
                "description": "Retrieves the units sold and revenue for a product category for a specific week.",
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
