# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class NotifyUser(Tool):
    """Tool to send a notification to a user."""
    @staticmethod
    def invoke(data: Dict[str, Any], message_content, recipient_user_id, sender_user_id = 'system') -> str:
        if not recipient_user_id or not message_content:
            return json.dumps({"error": "recipient_user_id and message_content are required."})

        new_notification = {
            "notification_id": f"notif_{uuid.uuid4().hex[:4]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().isoformat() + "Z",
            "status": "unread"
        }
        data['notifications'].append(new_notification)
        return json.dumps({"success": True, "notification": new_notification})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notify_user",
                "description": "Sends a notification to a user within the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {"type": "string", "description": "The user ID of the recipient."},
                        "message_content": {"type": "string", "description": "The content of the notification message."},
                        "sender_user_id": {"type": "string", "description": "The user ID of the sender. Defaults to 'system'."}
                    },
                    "required": ["recipient_user_id", "message_content"]
                }
            }
        }
