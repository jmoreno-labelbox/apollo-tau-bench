# Sierra copyright

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DispatchSystemNotification(Tool):
    """Tool to dispatch a direct notification to a user."""
    @staticmethod
    def invoke(data: Dict[str, Any], message_content, recipient_user_id, sender_user_id = 'system') -> str:

        if not all([recipient_user_id, message_content]):
            return json.dumps({"error": "recipient_user_id and message_content are required."})

        notifications = list(data.get('notifications', {}).values())
        new_notification = {
            "notification_id": f"notif_{len(notifications) + 1:02d}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "status": "unread"
        }
        notifications.append(new_notification)

        return json.dumps(new_notification, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "dispatch_system_notification",
                "description": "Dispatches a direct notification to a user, which can be from the system or another user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {"type": "string", "description": "The ID of the user who will receive the notification."},
                        "message_content": {"type": "string", "description": "The content of the notification message."},
                        "sender_user_id": {"type": "string", "description": "Optional. The user ID of the sender. Defaults to 'system'."}
                    },
                    "required": ["recipient_user_id", "message_content"]
                }
            }
        }
