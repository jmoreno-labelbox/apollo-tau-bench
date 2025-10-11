# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2GetExpensesByCategory(Tool):
    """Get expenses filtered by category and optional date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], category_code, end_date, start_date) -> str:

        if not category_code:
            return _error("category_code is required.")

        expenses = data.get("expenses", [])
        filtered_expenses = _find_all(expenses, "category_code", category_code)

        if start_date and end_date:
            filtered_expenses = [exp for exp in filtered_expenses
                               if start_date <= exp.get("expense_date", "") <= end_date]

        return json.dumps(filtered_expenses)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_expenses_by_category",
                "description": "Get expenses filtered by category code and optionally by date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category_code": {"type": "string"},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"}
                    },
                    "required": ["category_code"],
                },
            },
        }
