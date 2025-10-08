from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetPlanForDate(Tool):
    """Fetches the complete frozen plan for a given date."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str = None) -> str:
        report_date = date
        for plan in data.get("plans", []):
            if plan.get("date") == report_date:
                payload = plan
                out = json.dumps(payload)
                return out
        payload = {"error": f"Plan for date '{report_date}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPlanForDate",
                "description": "Retrieves the entire frozen plan for a specific date, including total budget and all ad set allocations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "The date of the plan in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["date"],
                },
            },
        }
