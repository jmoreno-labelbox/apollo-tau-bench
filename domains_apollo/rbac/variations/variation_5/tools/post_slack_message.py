from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class PostSlackMessage(Tool):
    """
    Add a Slack message record for notifications.

    kwargs:
      channel: str (mandatory) e.g., "#access-requests"
      message: str (mandatory)
      username: str = "RBAC_BOT"
      timestamp: str ISO (defaults to now)
    """

    @staticmethod
    def invoke(data: dict[str, Any], channel: str = "", message: str = "", username: str = "RBAC_BOT", timestamp: str = None) -> str:
        if timestamp is None:
            timestamp = get_current_timestamp()

        if not channel or not message:
            payload = {"error": "channel and message required"}
            out = json.dumps(payload)
            return out

        # Consistent rule: Standardize security incident messages
        # - When posting to #security-incidents, set the username to RBAC_BOT
        # - Remove excess whitespace from the message
        if channel.strip() == "#security-incidents":
            username = "RBAC_BOT"
            message = " ".join(str(message).split())

        rec = {
            "message_id": _next_id(data, "slack_messages", "SL"),
            "timestamp": timestamp,
            "username": username,
            "message": message,
            "channel": channel,
            # Conform to the dataset schema
            "created_at": timestamp,
            "updated_at": timestamp,
        }

        data.setdefault("slack_messages", []).append(rec)
        payload = {"ok": True, "slack_message": rec}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostSlackMessage",
                "description": "Post a message record to Slack notifications (e.g., #access-requests).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "Slack channel name (e.g., #access-requests).",
                        },
                        "message": {"type": "string", "description": "Message text."},
                        "username": {
                            "type": "string",
                            "description": "Posting bot username.",
                            "default": "RBAC_BOT",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO timestamp (optional).",
                        },
                    },
                    "required": ["channel", "message"],
                    "additionalProperties": False,
                },
            },
        }
