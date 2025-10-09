from tau_bench.envs.tool import Tool
import json
from typing import Any

class SendNotification(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: str = None,
        project_id: str = "project_001",
        notification_type: str = "info",
        title: str = "",
        message: str = "",
        recipient_id: str = "user_000",
        channel: str = "slack",
        sent_at: str = FIXED_TS,
        read_at: str = None,
        metadata: dict[str, Any] = None
    ) -> str:
        notifications = _table(data, "notifications")
        nid = id
        #--- FIX: Create ID if it is not supplied ---
        if not nid:
            nid = f"notification_{len(notifications) + 1:04d}"

        if any(n.get("id") == nid for n in notifications):
            return _err(f"notification id {nid} already exists")
        record = {
            "id": nid,
            "project_id": project_id,
            "notification_type": notification_type,
            "title": title,
            "message": message,
            "recipient_id": recipient_id,
            "channel": channel,
            "sent_at": sent_at,
            "read_at": read_at,
        }
        if not record["message"]:
            return _err("message must be non-empty")
        if metadata is not None:
            record["metadata"] = metadata
        notifications.append(record)
        return _ok({"notification": record})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "sendNotification",
                "description": "Record a notification (deterministic timestamp). Optionally include CI/linkage metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "notification_type": {"type": "string"},
                        "title": {"type": "string"},
                        "message": {"type": "string"},
                        "recipient_id": {"type": "string"},
                        "channel": {"type": "string"},
                        "sent_at": {"type": "string"},
                        "read_at": {"type": "string"},
                        "metadata": {"type": "object"},
                    },
                    "required": ["message"],
                },
            },
        }
