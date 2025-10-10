# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendUserNotification(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], channel_or_user_id: str, message: str) -> str:
        notifications = list(data.get("notifications", {}).values())
        the_notification = {
            "channel_or_user_id": channel_or_user_id,
            "message": message
        }
        notifications.append(the_notification)
        data["notifications"] = notifications
        return _j({
            "notified": the_notification
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_user_notification",
                "description": "Send a message to a specified user or operations channel (non-persistent, returns confirmation).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel_or_user_id": {"type": "string"},
                        "message": {"type": "string"}
                    },
                    "required": ["channel_or_user_id", "message"]
                }
            }
        }
