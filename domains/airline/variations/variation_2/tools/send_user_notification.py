from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class SendUserNotification(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], channel_or_user_id: str, message: str) -> str:
        pass
        #This tool does not store notifications — it provides a deterministic response
        return _j({"notified": channel_or_user_id, "message": message})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendUserNotification",
                "description": "Send a message to a specified user or operations channel (non-persistent, returns confirmation).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel_or_user_id": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["channel_or_user_id", "message"],
                },
            },
        }
