# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetExpenseDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], expense_id) -> str:
        if not expense_id:
            return json.dumps({"error": "expense_id is required"}, indent=2)
        expenses = list(data.get("expenses", {}).values())
        exp = next((e for e in expenses if e.get("expense_id") == expense_id), None)
        return json.dumps(exp or {"error": f"Expense {expense_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_expense_details","description": "Retrieve all data for a specific expense.","parameters": {"type": "object","properties": {"expense_id": {"type": "string"}},"required": ["expense_id"]}}}
