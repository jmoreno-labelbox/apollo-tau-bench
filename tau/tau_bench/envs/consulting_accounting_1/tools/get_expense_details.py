from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetExpenseDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], expense_id: str = None) -> str:
        if not expense_id:
            payload = {"error": "expense_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        expenses = data.get("expenses", [])
        exp = next((e for e in expenses if e.get("expense_id") == expense_id), None)
        payload = exp or {"error": f"Expense {expense_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getExpenseDetails",
                "description": "Retrieve all data for a specific expense.",
                "parameters": {
                    "type": "object",
                    "properties": {"expense_id": {"type": "string"}},
                    "required": ["expense_id"],
                },
            },
        }
