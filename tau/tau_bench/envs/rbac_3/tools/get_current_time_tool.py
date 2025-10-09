from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class GetCurrentTimeTool(Tool):
    """get_current_time: provides a consistent timestamp utilized across writes."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"timestamp": _HARD_TS}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCurrentTime",
                "description": "Return deterministic current time used for writes.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
