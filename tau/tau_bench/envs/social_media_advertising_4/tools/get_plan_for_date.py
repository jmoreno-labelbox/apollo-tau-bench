# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPlanForDate(Tool):
    """Retrieves the entire frozen plan for a specific date."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_date = kwargs.get("date")
        for plan in data.get('plans', []):
            if plan.get('date') == report_date:
                return json.dumps(plan)
        return json.dumps({"error": f"Plan for date '{report_date}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_plan_for_date", "description": "Retrieves the entire frozen plan for a specific date, including total budget and all ad set allocations.", "parameters": {"type": "object", "properties": {"date": {"type": "string", "description": "The date of the plan in YYYY-MM-DD format."}}, "required": ["date"]}}}
