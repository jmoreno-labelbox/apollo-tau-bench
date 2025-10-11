# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchPlanForDate(Tool):
    """Return a frozen plan snapshot for a given date."""
    @staticmethod
    def invoke(data: Dict[str, Any], date) -> str:
        target_date = date
        for plan in data.get("plans", []):
            if plan.get("date") == target_date:
                return json.dumps(plan)
        return json.dumps({"error": f"No plan found for {target_date}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_plan_for_date",
                "description": "Return a frozen plan snapshot for a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string", "description": "Plan date (YYYY-MM-DD)"}
                    },
                    "required": ["date"],
                },
            },
        }
