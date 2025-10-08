from tau_bench.envs.tool import Tool
import json
from typing import Any

class FetchEnvironment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        env = data.get("environment", {}) or {}
        payload = env
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEnvironment",
                "description": "Read environment variables/secrets map.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
