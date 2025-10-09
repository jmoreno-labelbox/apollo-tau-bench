from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SendSlackMessage(Tool):
    """Delivers a message to a designated Slack channel."""

    @staticmethod
    def invoke(data: dict[str, Any], channel_name: str = None, message: str = None) -> str:
        messages = data.get("slack_messages", [])
        new_id = f"msg_{max((int(m['message_id'].split('_')[-1]) for m in messages), default=0) + 1:03d}"

        # Automatically create a relevant message based on the channel name
        if channel_name == "System Alerts":
            message = (
                f"System alert notification sent to {channel_name} channel at {new_id}"
            )
        elif channel_name == "Operations":
            message = f"Operations update sent to {channel_name} channel at {new_id}"
        elif channel_name == "File Check":
            message = (
                f"File check notification sent to {channel_name} channel at {new_id}"
            )
        else:
            message = (
                f"Automated notification sent to {channel_name} channel at {new_id}"
            )

        channel_id = ""
        for channel in data.get("slack_channels", []):
            if channel.get("name") == channel_name:
                channel_id = channel.get("channel_id")
                break
        if not channel_id:
            payload = {"error": f"Channel '{channel_name}' not found."}
            out = json.dumps(payload)
            return out

        new_message = {
            "message_id": new_id,
            "channel_id": channel_id,
            "user_id": "system_agent",
            "username": "AutomationAgent",
            "message": message,
            "timestamp": "2024-01-20T14:00:00Z",
            "type": "notification",
        }
        messages.append(new_message)
        data["slack_messages"] = messages
        payload = new_message
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendSlackMessage",
                "description": "Posts an automatically generated message to a Slack channel for notifications and alerts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel_name": {
                            "type": "string",
                            "description": "The name of the public channel (e.g., 'System Alerts', 'Operations', 'File Check').",
                        }
                    },
                    "required": ["channel_name"],
                },
            },
        }
