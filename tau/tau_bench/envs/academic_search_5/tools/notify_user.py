from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class NotifyUser(Tool):
    """Utility for dispatching a notification to a user."""

    @staticmethod
    def invoke(data: dict[str, Any], recipient_user_id: Any = None, message_content: Any = None, sender_user_id: Any = None) -> str:
        if not recipient_user_id or not message_content:
            payload = {"error": "recipient_user_id and message_content are required."}
            out = json.dumps(payload)
            return out

        new_notification = {
            "notification_id": f"notif_{uuid.uuid4().hex[:4]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().isoformat() + "Z",
            "status": "unread",
        }
        data["notifications"][notification_id] = new_notification
        payload = {"success": True, "notification": new_notification}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotifyUser",
                "description": "Sends a notification to a user within the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {
                            "type": "string",
                            "description": "The user ID of the recipient.",
                        },
                        "message_content": {
                            "type": "string",
                            "description": "The content of the notification message.",
                        },
                        "sender_user_id": {
                            "type": "string",
                            "description": "The user ID of the sender. Defaults to 'system'.",
                        },
                    },
                    "required": ["recipient_user_id", "message_content"],
                },
            },
        }
