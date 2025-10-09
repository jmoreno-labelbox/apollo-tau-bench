from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class WeeklySales(Tool):
    """Provide weekly sales figures for a specific product category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None, campaign_id: Any = None) -> str:
        cat, week = category, start_date
        for s in data.get("f_sales", []):
            if s.get("category") == cat and s.get("start_date") == week:
                payload = s
                out = json.dumps(payload)
                return out
        payload = {"error": "Sales not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WeeklySales",
                "description": "Return weekly sales totals for a category and week.",
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
