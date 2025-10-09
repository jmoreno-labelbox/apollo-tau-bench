from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SendNotification(Tool):
    """Emulates sending a notification by appending it to the notifications log."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        notification_type: str = "system_notification",
        title: str = None,
        message: str = None,
        recipient_id: str = None,
        channel: str = "slack"
    ) -> str:
        notifications = data.get("notifications", [])

        # Create a new distinct ID
        if not notifications:
            new_id_num = 1
        else:
            new_id_num = max(int(n["id"].split("_")[1]) for n in notifications) + 1
        new_id = f"notification_{new_id_num:03d}"

        # Construct the new notification object
        new_notification = {
            "id": new_id,
            "project_id": project_id,
            "notification_type": notification_type,
            "title": title,
            "message": message,
            "recipient_id": recipient_id,
            "channel": channel,
            "sent_at": "2025-01-28T00:00:00Z",  # Utilize a standard placeholder timestamp
            "read_at": None,
        }

        notifications.append(new_notification)
        payload = {
            "status": "success",
            "message": f"Notification '{new_id}' sent successfully.",
            "notification_id": new_id,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendNotification",
                "description": "Simulates sending a notification by adding it to the notifications log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project related to the notification.",
                        },
                        "recipient_id": {
                            "type": "string",
                            "description": "The ID of the user who should receive the notification.",
                        },
                        "title": {
                            "type": "string",
                            "description": "The title of the notification.",
                        },
                        "message": {
                            "type": "string",
                            "description": "The body content of the notification.",
                        },
                        "channel": {
                            "type": "string",
                            "description": "The channel for the notification (e.g., 'slack', 'email').",
                            "default": "slack",
                        },
                        "notification_type": {
                            "type": "string",
                            "description": "The type of notification (e.g., 'incident_alert', 'bug_assignment').",
                            "default": "system_notification",
                        },
                    },
                    "required": ["project_id", "recipient_id", "title", "message"],
                },
            },
        }
