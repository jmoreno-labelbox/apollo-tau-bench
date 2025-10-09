from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DispatchUserAlert(Tool):
    """Sends an alert or notification to a user."""

    @staticmethod
    def invoke(data: dict[str, Any], recipient_user_id: Any = None, message_content: Any = None, sender_user_id: Any = None) -> str:
        recipient_user_id = recipient_user_id
        message_content = message_content
        sender_user_id = sender_user_id

        if not all([recipient_user_id, message_content]):
            payload = {"error": "recipient_user_id and message_content are required."}
            out = json.dumps(
                payload)
            return out

        notifications = data.get("notifications", {}).values()
        new_alert = {
            "notification_id": f"notif_{uuid.uuid4().hex[:6]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "unread",
        }
        data["notifications"][notification_id] = new_alert
        payload = {"success": True, "alert": new_alert}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DispatchUserAlert",
                "description": "Dispatches an alert or notification to a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {
                            "type": "string",
                            "description": "The ID of the user who will receive the alert.",
                        },
                        "message_content": {
                            "type": "string",
                            "description": "The content of the alert message.",
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
