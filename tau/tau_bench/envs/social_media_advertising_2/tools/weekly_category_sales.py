# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WeeklyCategorySales(Tool):
    """Return weekly sales for a product category."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cat, week = kwargs.get("category"), kwargs.get("start_date")
        for s in list(data.get("f_sales", {}).values()):
            if s.get("category") == cat and s.get("start_date") == week:
                return json.dumps(s)
        return json.dumps({"error": "Sales not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "weekly_category_sales",
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
