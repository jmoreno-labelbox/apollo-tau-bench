from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2GetExpensesByCategory(Tool):
    """Retrieve expenses filtered by category and an optional date range."""

    @staticmethod
    def invoke(data: dict[str, Any], category_code: str = None, start_date: str = None, end_date: str = None) -> str:
        if not category_code:
            return _error("category_code is required.")

        expenses = data.get("expenses", [])
        filtered_expenses = _find_all(expenses, "category_code", category_code)

        if start_date and end_date:
            filtered_expenses = [
                exp
                for exp in filtered_expenses
                if start_date <= exp.get("expense_date", "") <= end_date
            ]
        payload = filtered_expenses
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetExpensesByCategory",
                "description": "Get expenses filtered by category code and optionally by date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category_code": {"type": "string"},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"},
                    },
                    "required": ["category_code"],
                },
            },
        }
