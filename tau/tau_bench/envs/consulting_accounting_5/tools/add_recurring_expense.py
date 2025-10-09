from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class AddRecurringExpense(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], 
        recurring_id: str, 
        category_code: str, 
        amount: float, 
        frequency: str, 
        vendor: str = "", 
        start_date: Any = None, 
        end_date: Any = None
    ) -> str:
        """
        Inserts a new recurring expense schedule.
        """
        new_rec = {
            "recurring_id": recurring_id,
            "category_code": category_code,
            "amount": amount,
            "frequency": frequency,
            "vendor": vendor,
            "start_date": start_date,
            "end_date": end_date
        }
        data["recurring_schedules"].append(new_rec)
        return json.dumps(new_rec["recurring_id"])
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddRecurringExpense",
                "description": "Insert a new recurring expense schedule into recurring_schedules.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recurring_id": {"type": "string"},
                        "category_code": {"type": "string"},
                        "amount": {"type": "number"},
                        "frequency": {"type": "string"},
                        "vendor": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"}
                    },
                    "required": ["recurring_id", "category_code", "amount", "frequency"],
                },
            },
        }
