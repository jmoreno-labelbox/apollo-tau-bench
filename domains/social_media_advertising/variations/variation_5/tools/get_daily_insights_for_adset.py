from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class GetDailyInsightsForAdset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        for i in data.get("f_insights", []):
            if i.get("adset_id") == adset_id and i.get("date") == date:
                payload = i
                out = json.dumps(payload)
                return out
        payload = {"error": "insights_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDailyInsightsForAdset",
                "description": "Gets insights for one ad set on a date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }
