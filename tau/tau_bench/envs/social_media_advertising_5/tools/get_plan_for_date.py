from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class GetPlanForDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], date: str = None) -> str:
        d = date
        for p in data.get("plans", []):
            if p.get("date") == d:
                payload = p
                out = json.dumps(payload)
                return out
        payload = {"error": f"plan for {d} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPlanForDate",
                "description": "Retrieves a frozen plan by date.",
                "parameters": {
                    "type": "object",
                    "properties": {"date": {"type": "string"}},
                    "required": ["date"],
                },
            },
        }
