# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_next_id(prefix: str, existing_ids: List[str]) -> str:
    """
    Generates the next sequential ID by finding the max existing ID for a given prefix.
    This is more robust than assuming the list is sorted.
    """
    max_id_num = 0
    for item_id in existing_ids:
        if item_id.startswith(prefix):
            try:
                num_part = int(item_id.split('_')[-1])
                if num_part > max_id_num:
                    max_id_num = num_part
            except (ValueError, IndexError):
                continue

    if max_id_num == 0:
        if not any(s.startswith(prefix) for s in existing_ids):
             return f"{prefix}_001"

    return f"{prefix}_{max_id_num + 1:03d}"

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