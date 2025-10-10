# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDateForPlan(Tool):
    """Retrieves the date for a specific plan."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id = kwargs.get("plan_id")
        plans = list(data.get("plans", {}).values())
        
        for plan in plans:
            if plan.get("plan_id") == plan_id:
                return json.dumps({"date": plan.get('date')})
        
        return json.dumps({"error": f"Plan with ID '{plan_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_date_for_plan",
                "description": "Retrieves the date for a specific plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The unique ID of the plan.",
                        }
                    },
                    "required": ["plan_id"],
                },
            },
        }
