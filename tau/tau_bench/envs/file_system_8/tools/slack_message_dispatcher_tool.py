from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SlackMessageDispatcherTool(Tool):
    """Manages message delivery to specified Slack channels."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendSlackNotification",
                "description": "Sends a message to a specified Slack channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "The Slack channel to send the message to (e.g., 'File Check').",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the message.",
                        },
                    },
                    "required": ["channel", "message"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], channel: str, message: str, mention_users: list = None, priority: str = None) -> str:
        target_channel = channel
        msg_content = message

        # Set up slack logging if it is absent
        if data.get("slack_log") is None:
            data["slack_log"] = []

        # Generate and save a log record
        notification_entry = {"channel": target_channel, "message": msg_content}
        data["slack_log"].append(notification_entry)

        result = {"status": "success", "log_entry": notification_entry}
        payload = result
        out = json.dumps(payload)
        return out
