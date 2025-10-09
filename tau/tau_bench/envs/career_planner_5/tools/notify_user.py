from tau_bench.envs.tool import Tool
import json
from typing import Any

class NotifyUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, message: str) -> str:
        data.setdefault("user_notifications", []).append(
            {"user_id": user_id, "message": message}
        )
        payload = {"notified_user": user_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "notifyUser",
                "description": "Push a notification message to an individual user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["user_id", "message"],
                },
            },
        }
