# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendNotification(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message_content, recipient_user_id, sender_user_id = 'system') -> str:
        """
        Creates and sends a new notification to a user.
        - Requires recipient_user_id and message_content.
        - sender_user_id is optional and defaults to 'system'.
        """

        if not all([recipient_user_id, message_content]):
            return json.dumps({"error": "recipient_user_id and message_content are required."})

        notifications = list(data.get('notifications', {}).values())
        new_notification = {
            "notification_id": f"notif_{uuid.uuid4().hex[:6]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "status": "unread"
        }
        notifications.append(new_notification)

        return json.dumps({"success": True, "notification": new_notification})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema for the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "send_notification",
                "description": "Sends a direct notification to a specific user. Can be from another user or the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {"type": "string", "description": "The ID of the user who will receive the notification."},
                        "message_content": {"type": "string", "description": "The content of the notification message."},
                        "sender_user_id": {"type": "string", "description": "Optional. The ID of the user sending the notification. Defaults to 'system'."}
                    },
                    "required": ["recipient_user_id", "message_content"]
                }
            }
        }
