from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class DispatchSystemNotification(Tool):
    """Utility for sending a direct notification to a user."""

    @staticmethod
    def invoke(data: dict[str, Any], recipient_user_id: Any = None, message_content: Any = None, sender_user_id: Any = None) -> str:
        if not all([recipient_user_id, message_content]):
            payload = {"error": "recipient_user_id and message_content are required."}
            out = json.dumps(payload)
            return out

        notifications = data.get("notifications", [])
        new_notification = {
            "notification_id": f"notif_{len(notifications) + 1:02d}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "unread",
        }
        notifications.append(new_notification)
        payload = new_notification
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DispatchSystemNotification",
                "description": "Dispatches a direct notification to a user, which can be from the system or another user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {
                            "type": "string",
                            "description": "The ID of the user who will receive the notification.",
                        },
                        "message_content": {
                            "type": "string",
                            "description": "The content of the notification message.",
                        },
                        "sender_user_id": {
                            "type": "string",
                            "description": "Optional. The user ID of the sender. Defaults to 'system'.",
                        },
                    },
                    "required": ["recipient_user_id", "message_content"],
                },
            },
        }
