from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetExpensesByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], category_code: str) -> str:
        """
        Returns expense_ids for all expenses under a given category_code.
        """
        expense_ids = [exp["expense_id"] for exp in data["expenses"].values() if exp["category_code"] == category_code]
        return json.dumps(expense_ids)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetExpensesByCategory",
                "description": "Fetch all expense_ids under a given category_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category_code": {"type": "string", "description": "Expense category code"}
                    },
                    "required": ["category_code"],
                },
            },
        }
