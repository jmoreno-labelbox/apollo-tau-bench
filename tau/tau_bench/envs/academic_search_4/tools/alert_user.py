from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class AlertUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipient_user_id: Any = None, message: Any = None, sender_user_id: Any = None) -> str:
        if not all([recipient_user_id, message]):
            payload = {"error": "recipient_user_id and message are required."}
            out = json.dumps(payload)
            return out

        new_notification = {
            "notification_id": f"notif_{uuid.uuid4().hex[:4]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message,
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "unread",
        }
        if "notifications" not in data:
            data["notifications"] = []
        data["notifications"][notification_id] = new_notification
        payload = {"success": True, "notification": new_notification}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AlertUser",
                "description": "Sends a direct alert message to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {
                            "type": "string",
                            "description": "The ID of the user to receive the alert.",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the alert message.",
                        },
                        "sender_user_id": {
                            "type": "string",
                            "description": "Optional. The user ID of the sender. Defaults to 'system'.",
                        },
                    },
                    "required": ["recipient_user_id", "message"],
                },
            },
        }
