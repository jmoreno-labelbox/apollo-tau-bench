# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPlanForDate(Tool):
    """Return the frozen plan for a given date (exact match on 'date')."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["date"])
        if err: return _fail(err)
        plans = _assert_table(data, "plans")
        for p in plans:
            if p.get("date") == kwargs["date"]:
                return json.dumps(p)
        return _fail("plan_not_found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_plan_for_date", "description": "Get a frozen plan for a given date.",
                             "parameters": {"type": "object", "properties": {
                                 "date": {"type": "string", "description": "The YYYY-MM-DD date of the plan."}},
                                            "required": ["date"]}}}
