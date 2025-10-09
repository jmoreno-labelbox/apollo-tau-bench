from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetPlanForDate(Tool):
    """Provide the frozen plan for a specified date (exact match on 'date')."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str) -> str:
        err = _require({"date": date}, ["date"])
        if err:
            return _fail(err)
        plans = _assert_table(data, "plans")
        for p in plans:
            if p.get("date") == date:
                payload = p
                out = json.dumps(payload)
                return out
        return _fail("plan_not_found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPlanForDate",
                "description": "Get a frozen plan for a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "The YYYY-MM-DD date of the plan.",
                        }
                    },
                    "required": ["date"],
                },
            },
        }
