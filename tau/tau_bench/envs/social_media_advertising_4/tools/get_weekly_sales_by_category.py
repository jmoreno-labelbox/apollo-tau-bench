# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWeeklySalesByCategory(Tool):
    """Retrieves weekly sales figures for a category."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category, start_date = kwargs.get("category"), kwargs.get("start_date")
        for record in data.get('f_sales', []):
            if record.get('category') == category and record.get('start_date') == start_date:
                return json.dumps(record)
        return json.dumps({"error": "Sales data not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_weekly_sales_by_category", "description": "Retrieves the units sold and revenue for a product category for a specific week.", "parameters": {"type": "object", "properties": {"category": {"type": "string"}, "start_date": {"type": "string"}}, "required": ["category", "start_date"]}}}
