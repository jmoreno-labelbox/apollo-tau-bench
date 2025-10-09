from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class AddExpenseRecord(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        expense_id: str,
        project_id: str = None,
        vendor: str = None,
        expense_date: str = None,
        amount: float = None,
        description: str = "",
        payment_method: str = "",
        category_code: str = None,
        created_at: str = None
    ) -> str:
        """
        Inserts a new expense record.
        """
        new_exp = {
            "expense_id": expense_id,
            "project_id": project_id,
            "vendor": vendor,
            "expense_date": expense_date,
            "amount": amount,
            "description": description,
            "payment_method": payment_method,
            "category_code": category_code,
            "created_at": created_at
        }
        data["expenses"][expense_id] = new_exp
        return json.dumps(new_exp["expense_id"])
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddExpenseRecord",
                "description": "Insert a new expense record into expenses.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expense_id": {"type": "string"},
                        "vendor": {"type": "string"},
                        "expense_date": {"type": "string"},
                        "amount": {"type": "number"},
                        "description": {"type": "string"},
                        "payment_method": {"type": "string"},
                        "category_code": {"type": "string"},
                        "created_at": {"type": "string"}
                    },
                    "required": ["expense_id", "vendor", "expense_date", "amount", "category_code"],
                },
            },
        }
