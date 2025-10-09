from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetAircraftByTail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tail_number: str) -> str:
        for a in data.get("aircraft", []):
            if a.get("tail_number") == tail_number:
                return _j(a)
        return _j({})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftByTail",
                "description": "Return an aircraft row by tail number.",
                "parameters": {
                    "type": "object",
                    "properties": {"tail_number": {"type": "string"}},
                    "required": ["tail_number"],
                },
            },
        }
