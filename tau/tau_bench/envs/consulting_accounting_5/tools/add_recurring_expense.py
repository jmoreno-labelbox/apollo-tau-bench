# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddRecurringExpense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Inserts a new recurring expense schedule.
        """
        new_rec = {
            "recurring_id": kwargs["recurring_id"],
            "category_code": kwargs["category_code"],
            "amount": kwargs["amount"],
            "frequency": kwargs["frequency"],  # for example, "monthly", "quarterly"
            "vendor": kwargs.get("vendor", ""),
            "start_date": kwargs.get("start_date", None),
            "end_date": kwargs.get("end_date", None)
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
