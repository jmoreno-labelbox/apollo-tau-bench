from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class NotifyHr(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message: str) -> str:
        notification = {
            "message": message,
            "timestamp": "2025-07-04",
            "type": "HR_NOTIFICATION",
        }
        data.setdefault("hr_notifications", []).append(notification)
        payload = {"success": "HR notified", "message": message}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "notifyHr",
                "description": "Send a notification to HR",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }
