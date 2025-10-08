from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCurrentTimestamp(Tool):
    """Provides a fixed current timestamp value."""

    def invoke(data: dict[str, Any], unused: Any = None) -> str:
        payload = {"timestamp": "2025-08-13T01:01:01Z"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCurrentTimestamp",
                "description": "Returns a hardcoded current timestamp value (2025-08-13T01:01:01Z).",
                "parameters": {},
            },
        }
