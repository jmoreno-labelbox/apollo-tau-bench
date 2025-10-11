# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _next_id(data: Dict[str, Any], collection: str, prefix: str) -> str:
    n = len(data.get(collection, [])) + 1
    return f"{prefix}-{n:03d}"

class PostSlackMessage(Tool):
    """
    Append a Slack message record for notifications.

    kwargs:
      channel: str (required) e.g., "#access-requests"
      message: str (required)
      username: str = "RBAC_BOT"
      timestamp: str ISO (defaults now)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        channel = kwargs.get("channel", "")
        message = kwargs.get("message", "")
        username = kwargs.get("username", "RBAC_BOT")
        timestamp = kwargs.get("timestamp") or get_current_timestamp()

        if not channel or not message:
            return json.dumps({"error": "channel and message required"})

        # Deterministic guideline: Standardize security incident notifications.
        # - If posting to # - When posting to #security-incidents, set the username to RBAC_BOT.
        # - Remove whitespace discrepancies from the message.
        if channel.strip() == "#security-incidents":
            username = "RBAC_BOT"
            message = " ".join(str(message).split())

        rec = {
            "message_id": _next_id(data, "slack_messages", "SL"),
            "timestamp": timestamp,
            "username": username,
            "message": message,
            "channel": channel,
                        # Conform to dataset structure.
                        "created_at": timestamp,
                        "updated_at": timestamp,
        }

        data.setdefault("slack_messages", []).append(rec)
        return json.dumps({"ok": True, "slack_message": rec})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "post_slack_message",
"description": "Post a message record to Slack notifications (e.g., # access-requests).",
                "parameters": {
                    "type": "object",
                    "properties": {
"channel": {"type": "string", "description": "Slack channel name (e.g., # access-requests)."},
                        "message": {"type": "string", "description": "Message text."},
                        "username": {"type": "string", "description": "Posting bot username.", "default": "RBAC_BOT"},
                        "timestamp": {"type": "string", "description": "ISO timestamp (optional)."}
                    },
                    "required": ["channel", "message"],
                    "additionalProperties": False
                }
            }
        }