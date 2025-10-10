# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddExpenseRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Inserts a new expense record.
        """
        new_exp = {
            "expense_id": kwargs["expense_id"],
            "project_id": kwargs.get("project_id"),
            "vendor": kwargs["vendor"],
            "expense_date": kwargs["expense_date"],
            "amount": kwargs["amount"],
            "description": kwargs.get("description", ""),
            "payment_method": kwargs.get("payment_method", ""),
            "category_code": kwargs["category_code"],
            "created_at": kwargs.get("created_at", None)
        }
        data["expenses"].append(new_exp)
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
