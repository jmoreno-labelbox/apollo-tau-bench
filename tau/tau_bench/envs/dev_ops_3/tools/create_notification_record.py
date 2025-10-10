# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_notification_record(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message: str) -> str:
        notifications = list(data.get("notifications", {}).values())
        existing_ids = [n['id'] for n in notifications]
        new_id = _get_next_id("notification", existing_ids)
        new_notification = {
            "id": new_id,
            "message": message,
            "created_at": FIXED_TIMESTAMP,
            "status": "unread"
        }
        notifications.append(new_notification)
        data["notifications"] = notifications
        return json.dumps({"success": f"Created notification record '{new_id}'.", "notification_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "create_notification_record", "description": "Creates a new notification record.", "parameters": { "type": "object", "properties": { "message": { "type": "string" } }, "required": ["message"] } } }
