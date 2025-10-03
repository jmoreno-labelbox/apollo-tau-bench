from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class GetCurrentTime(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"current_time": NOW.strftime(DT_STR_FORMAT)}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCurrentTime",
                "description": "Returns the current date and time.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
