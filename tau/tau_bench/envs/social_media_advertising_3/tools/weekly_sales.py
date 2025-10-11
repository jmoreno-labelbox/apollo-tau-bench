# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WeeklySales(Tool):
    """Return weekly sales for a product category."""
    @staticmethod
    def invoke(data: Dict[str, Any], category, start_date) -> str:
        cat, week = category, start_date
        for s in data.get("f_sales", []):
            if s.get("category") == cat and s.get("start_date") == week:
                return json.dumps(s)
        return json.dumps({"error": "Sales not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "weekly_sales",
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
