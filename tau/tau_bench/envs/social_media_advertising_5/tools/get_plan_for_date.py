# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPlanForDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        d = kwargs.get("date")
        for p in list(data.get("plans", {}).values()):
            if p.get("date") == d:
                return json.dumps(p)
        return json.dumps({"error": f"plan for {d} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_plan_for_date", "description": "Retrieves a frozen plan by date.",
                             "parameters": {"type": "object", "properties": {"date": {"type": "string"}},
                                            "required": ["date"]}}}
