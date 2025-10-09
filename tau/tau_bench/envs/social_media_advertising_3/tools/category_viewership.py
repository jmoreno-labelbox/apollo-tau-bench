from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class CategoryViewership(Tool):
    """Deliver viewership statistics for a product category on a specific date."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, date: str = None) -> str:
        cat, date = category, date
        for v in data.get("f_viewership", []):
            if v.get("category") == cat and v.get("date") == date:
                payload = v
                out = json.dumps(payload)
                return out
        payload = {"error": "Viewership not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "categoryViewership",
                "description": "Return viewership metrics for a product category on a date.",
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
