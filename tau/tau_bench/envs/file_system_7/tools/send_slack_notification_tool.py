from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class SendSlackNotificationTool(Tool):
    """Versatile tool for sending notifications to a Slack channel."""

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
    def invoke(data: dict[str, Any], channel: str, message: str,
    priority: Any = None,
    mention_users: Any = None,
    include_timestamp: Any = None,
    thread_ts: Any = None,
    ) -> str:
        if "slack_log" not in data:
            data["slack_log"] = []
        log_entry = {"channel": channel, "message": message}
        data["slack_log"].append(log_entry)
        payload = {"status": "success", "log_entry": log_entry}
        out = json.dumps(payload)
        return out
