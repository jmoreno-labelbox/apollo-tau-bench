# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ModerateSlackChannelTool(Tool):
    """Moderate Slack channel: archive, pin, unpin, or move canonical messages (bulk support)."""
    @staticmethod
    def invoke(data: Dict[str, Any], action, channel, moderator_id, target_channel, message_ids = []) -> str:
        messages = data.get("slack_messages", [])

        updated = []
        for msg in messages:
            if msg["message_id"] in message_ids and msg["channel"] == channel:
                if action == "archive":
                    msg["archived"] = True
                elif action == "pin":
                    msg["pinned"] = True
                elif action == "unpin":
                    msg["pinned"] = False
                elif action == "move" and target_channel:
                    msg["channel"] = target_channel
                updated.append(msg["message_id"])
        status = {"moderated": updated, "action": action}
        return json.dumps(status, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "moderate_slack_channel",
                "description": "Archive, pin, unpin, or move canonical Slack messages with proper RBAC moderation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string"},
                        "action": {"type": "string", "enum": ["archive", "pin", "unpin", "move"]},
                        "message_ids": {"type": "array", "items": {"type": "string"}},
                        "target_channel": {"type": "string"},
                        "moderator_id": {"type": "string"}
                    },
                    "required": ["channel", "action", "message_ids", "moderator_id"]
                }
            }
        }
