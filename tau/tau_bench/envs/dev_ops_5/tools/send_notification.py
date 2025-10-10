# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendNotification(Tool):
    """Simulates sending a notification by adding it to the notifications log."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        notifications = list(data.get("notifications", {}).values())
        
        # Generate a new unique ID
        if not notifications:
            new_id_num = 1
        else:
            new_id_num = max(int(n["id"].split("_")[1]) for n in notifications) + 1
        new_id = f"notification_{new_id_num:03d}"
        
        # Create the new notification object
        new_notification = {
            "id": new_id,
            "project_id": kwargs.get("project_id"),
            "notification_type": kwargs.get("notification_type", "system_notification"),
            "title": kwargs.get("title"),
            "message": kwargs.get("message"),
            "recipient_id": kwargs.get("recipient_id"),
            "channel": kwargs.get("channel", "slack"),
            "sent_at": "2025-01-28T00:00:00Z",  # Use a consistent placeholder timestamp
            "read_at": None
        }
        
        notifications.append(new_notification)
        
        return json.dumps({
            "status": "success",
            "message": f"Notification '{new_id}' sent successfully.",
            "notification_id": new_id
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_notification",
                "description": "Simulates sending a notification by adding it to the notifications log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project related to the notification."},
                        "recipient_id": {"type": "string", "description": "The ID of the user who should receive the notification."},
                        "title": {"type": "string", "description": "The title of the notification."},
                        "message": {"type": "string", "description": "The body content of the notification."},
                        "channel": {"type": "string", "description": "The channel for the notification (e.g., 'slack', 'email').", "default": "slack"},
                        "notification_type": {"type": "string", "description": "The type of notification (e.g., 'incident_alert', 'bug_assignment').", "default": "system_notification"}
                    },
                    "required": ["project_id", "recipient_id", "title", "message"],
                },
            },
        }
