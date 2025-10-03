from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class FetchPlanForDate(Tool):
    """Provide a frozen snapshot of the plan for a specified date."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str = None) -> str:
        target_date = date
        for plan in data.get("plans", []):
            if plan.get("date") == target_date:
                payload = plan
                out = json.dumps(payload)
                return out
        payload = {"error": f"No plan found for {target_date}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchPlanForDate",
                "description": "Return a frozen plan snapshot for a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Plan date (YYYY-MM-DD)",
                        }
                    },
                    "required": ["date"],
                },
            },
        }
