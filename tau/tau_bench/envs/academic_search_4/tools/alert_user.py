# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
import uuid
from datetime import datetime


class AlertUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message, recipient_user_id, sender_user_id = 'system') -> str:

        if not all([recipient_user_id, message]):
            return json.dumps({"error": "recipient_user_id and message are required."})

        new_notification = {"notification_id": f"notif_{uuid.uuid4().hex[:4]}", "recipient_user_id": recipient_user_id, "sender_user_id": sender_user_id, "message_content": message, "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'), "status": "unread"}
        data['notifications'].append(new_notification)
        return json.dumps({"success": True, "notification": new_notification})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "alert_user", "description": "Sends a direct alert message to a user.", "parameters": {"type": "object", "properties": {"recipient_user_id": {"type": "string", "description": "The ID of the user to receive the alert."}, "message": {"type": "string", "description": "The content of the alert message."}, "sender_user_id": {"type": "string", "description": "Optional. The user ID of the sender. Defaults to 'system'."}}, "required": ["recipient_user_id", "message"]}}}
