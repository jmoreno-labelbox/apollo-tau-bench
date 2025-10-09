from tau_bench.envs.tool import Tool
import json
from typing import Any

class NotifyHr(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message: str) -> str:
        data.setdefault("hr_notifications", []).append({"message": message})
        payload = {"notified": "HR", "message": message}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "notifyHr",
                "description": "Send an informational notification to the HR team.",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }
