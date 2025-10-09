from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SendSlackNotification(Tool):
    """Dispatches a notification to a Slack channel."""

    @staticmethod
    def invoke(data: dict[str, Any], channel_name: str = None, message: str = None) -> str:
        channel_id = None
        for channel in data.get("slack_channels", {}).values():
            if channel.get("name") == channel_name:
                channel_id = channel.get("channel_id")
                break

        if not channel_id:
            payload = {"error": f"Channel '{channel_name}' not found."}
            out = json.dumps(payload)
            return out

        slack_messages = data.get("slack_messages", {}).values()
        max_id = 0
        if slack_messages:
            for msg in slack_messages.values():
                try:
                    current_id_num = int(msg.get("message_id", "msg_000").split("_")[1])
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
        new_id_num = max_id + 1
        message_id = f"msg_{new_id_num:03d}"

        new_message = {
            "message_id": message_id,
            "channel_id": channel_id,
            "user_id": "system_agent",
            "username": "SystemMonitor",
            "message": message,
            "timestamp": "2025-08-13T01:01:01Z",
            "type": "system_alert",
        }
        data["slack_messages"].append(new_message)
        payload = {"status": "success", "message": f"Message sent to {channel_name}."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendSlackNotification",
                "description": "Sends a notification to a Slack channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel_name": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["channel_name", "message"],
                },
            },
        }
