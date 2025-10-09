from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetCurrentTimestamp(Tool):
    """Provides a fixed current timestamp value."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"timestamp": "2025-08-13T01:01:01Z"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCurrentTimestamp",
                "description": "Returns a hardcoded current timestamp value (2025-08-13T01:01:01Z).",
                "parameters": {},
            },
        }
