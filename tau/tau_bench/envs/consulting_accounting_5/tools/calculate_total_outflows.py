# Copyright owned by Sierra

from datetime import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTotalOutflows(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], end_date, start_date) -> str:
        """
        Calculates the sum of all recurring expenses scheduled to be paid within a date range.
        """
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        total_outflow = 0

        for schedule in data["recurring_schedules"]:
            if not schedule.get("is_active"):
                continue

            # This represents a streamlined approach for handling monthly and quarterly payments.
            if schedule["frequency"] == "monthly":
                # Verify payments for the current and following month to ensure a 30-day coverage.
                for month_offset in range(2):
                    current_month_start = (start_date.replace(day=1) + timedelta(days=32 * month_offset)).replace(day=1)
                    if schedule["payment_day"] != "variable":
                        payment_date = current_month_start.replace(day=int(schedule["payment_day"]))
                        if start_date <= payment_date <= end_date:
                            total_outflow += schedule["amount"]
            elif schedule["frequency"] == "quarterly":
                 if start_date.month in schedule["payment_months"]:
                     total_outflow += schedule["amount"]

        return json.dumps({"period_start": start_date, "period_end": end_date, "total_outflows": round(total_outflow, 2)})

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
