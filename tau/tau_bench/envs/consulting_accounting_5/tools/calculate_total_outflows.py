# Copyright Sierra

from datetime import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTotalOutflows(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Calculates the sum of all recurring expenses scheduled to be paid within a date range.
        """
        start_date = datetime.strptime(kwargs["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(kwargs["end_date"], "%Y-%m-%d")
        total_outflow = 0

        for schedule in data["recurring_schedules"]:
            if not schedule.get("is_active"):
                continue

            # This is a simplified logic for monthly/quarterly payments
            if schedule["frequency"] == "monthly":
                # Check for payment in the start month and next month to cover the 30-day window
                for month_offset in range(2):
                    current_month_start = (start_date.replace(day=1) + timedelta(days=32 * month_offset)).replace(day=1)
                    if schedule["payment_day"] != "variable":
                        payment_date = current_month_start.replace(day=int(schedule["payment_day"]))
                        if start_date <= payment_date <= end_date:
                            total_outflow += schedule["amount"]
            elif schedule["frequency"] == "quarterly":
                 if start_date.month in schedule["payment_months"]:
                     total_outflow += schedule["amount"]

        return json.dumps({"period_start": kwargs["start_date"], "period_end": kwargs["end_date"], "total_outflows": round(total_outflow, 2)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "CalculateTotalOutflows",
                "description": "Calculates the sum of all recurring expenses scheduled to be paid within a date range.",
                "parameters": {
                    "type": "object", "properties": {
                        "start_date": {"type": "string", "description": "Start of the forecast period (YYYY-MM-DD)"},
                        "end_date": {"type": "string", "description": "End of the forecast period (YYYY-MM-DD)"},
                    }, "required": ["start_date", "end_date"],
                },
            },
        }
