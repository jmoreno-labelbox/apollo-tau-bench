# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DispatchUserAlert(Tool):
    """Dispatches an alert or notification to a user."""
    @staticmethod
    def invoke(data: Dict[str, Any], message_content, recipient_user_id, sender_user_id = 'system') -> str:

        if not all([recipient_user_id, message_content]):
            return json.dumps({"error": "recipient_user_id and message_content are required."})

        notifications = list(data.get('notifications', {}).values())
        new_alert = {
            "notification_id": f"notif_{uuid.uuid4().hex[:6]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "status": "unread"
        }
        notifications.append(new_alert)

        return json.dumps({"success": True, "alert": new_alert})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "dispatch_user_alert",
                "description": "Dispatches an alert or notification to a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {"type": "string", "description": "The ID of the user who will receive the alert."},
                        "message_content": {"type": "string", "description": "The content of the alert message."},
                        "sender_user_id": {"type": "string", "description": "Optional. The user ID of the sender. Defaults to 'system'."}
                    },
                    "required": ["recipient_user_id", "message_content"]
                }
            }
        }
