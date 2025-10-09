from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetTodayDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"today": "2025-10-02"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetTodayDate",
                "description": "Get today's date",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
