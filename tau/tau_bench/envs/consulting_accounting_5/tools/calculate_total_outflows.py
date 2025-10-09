from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class CalculateTotalOutflows(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], start_date: str, end_date: str) -> str:
        """
        Calculates the sum of all recurring expenses scheduled to be paid within a date range.
        """
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        total_outflow = 0

        for schedule in data["recurring_schedules"]:
            if not schedule.get("is_active"):
                continue

            if schedule["frequency"] == "monthly":
                for month_offset in range(2):
                    current_month_start = (start_date_obj.replace(day=1) + timedelta(days=32 * month_offset)).replace(day=1)
                    if schedule["payment_day"] != "variable":
                        payment_date = current_month_start.replace(day=int(schedule["payment_day"]))
                        if start_date_obj <= payment_date <= end_date_obj:
                            total_outflow += schedule["amount"]
            elif schedule["frequency"] == "quarterly":
                if start_date_obj.month in schedule["payment_months"]:
                    total_outflow += schedule["amount"]

        return json.dumps({"period_start": start_date_obj.strftime("%Y-%m-%d"), "period_end": end_date_obj.strftime("%Y-%m-%d"), "total_outflows": round(total_outflow, 2)})
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
