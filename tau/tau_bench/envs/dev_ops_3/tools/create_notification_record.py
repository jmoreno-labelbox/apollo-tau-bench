from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class create_notification_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message: str) -> str:
        pass
        notifications = data.get("notifications", {}).values()
        existing_ids = [n["id"] for n in notifications.values()]
        new_id = _get_next_id("notification", existing_ids)
        new_notification = {
            "id": new_id,
            "message": message,
            "created_at": FIXED_TIMESTAMP,
            "status": "unread",
        }
        data["notifications"][notification_id] = new_notification
        data["notifications"] = notifications
        payload = {
                "success": f"Created notification record '{new_id}'.",
                "notification_id": new_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNotificationRecord",
                "description": "Creates a new notification record.",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }
