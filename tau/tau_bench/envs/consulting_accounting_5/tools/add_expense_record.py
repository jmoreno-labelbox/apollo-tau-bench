# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddExpenseRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], amount, category_code, expense_date, expense_id, project_id, vendor, created_at = None, description = "", payment_method = "") -> str:
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
