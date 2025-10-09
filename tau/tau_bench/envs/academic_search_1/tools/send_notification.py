from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SendNotification(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipient_user_id: Any = None, message_content: Any = None, sender_user_id: Any = 'system') -> str:
        """
        Generates and dispatches a new notification to a user.
        - Needs recipient_user_id and message_content.
        - sender_user_id is optional and defaults to 'system'.
        """
        if not all([recipient_user_id, message_content]):
            payload = {"error": "recipient_user_id and message_content are required."}
            out = json.dumps(payload)
            return out

        notifications = data.get("notifications", [])
        new_notification = {
            "alert_id": f"notif_{uuid.uuid4().hex[:6]}",
            "receiver_person_id": recipient_user_id,
            "sender_person_id": sender_user_id,
            "note_text": message_content,
            "time_recorded": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "state": "unread",
        }
        notifications.append(new_notification)
        payload = {"success": True, "notification": new_notification}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Supplies the function schema for the language model's use.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SendNotification",
                "description": "Sends a direct notification to a specific user. Can be from another user or the system.",
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
                            "description": "Optional. The ID of the user sending the notification. Defaults to 'system'.",
                        },
                    },
                    "required": ["recipient_user_id", "message_content"],
                },
            },
        }
