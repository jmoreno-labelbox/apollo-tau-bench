from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCurrentTimeTool(Tool):
    """
    Provides the fixed canonical current time utilized in evaluation.
    """

    @staticmethod
    def invoke(data: dict) -> str:
        payload = {"current_time": "2025-08-17T00:00:00Z"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetCurrentTime",
                "description": "Return the canonical current time for use in audit logs and decisions.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
