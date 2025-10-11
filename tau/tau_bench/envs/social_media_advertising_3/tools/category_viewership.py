# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CategoryViewership(Tool):
    """Return viewership metrics for a product category on a date."""
    @staticmethod
    def invoke(data: Dict[str, Any], category, date) -> str:
        cat, date = category, date
        for v in data.get("f_viewership", []):
            if v.get("category") == cat and v.get("date") == date:
                return json.dumps(v)
        return json.dumps({"error": "Viewership not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "category_viewership",
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
