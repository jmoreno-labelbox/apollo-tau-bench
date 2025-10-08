from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class GetCurrentTime(Tool):
    """Provides a static current date and time formatted as "YYYY-MM-DD HH:MM:SS+00:00". For example, "2025-08-09 10:00:00+00:00"""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        # Format the date and time in the format "YYYY-MM-DD HH:MM:SS+00:00"
        formatted_time = NOW.isoformat(timespec="seconds").replace("T", " ")
        payload = {"current_time": formatted_time}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCurrentTime",
                "description": "Returns the current date and time as YYYY-MM-DD HH:MM:SS+00:00",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
