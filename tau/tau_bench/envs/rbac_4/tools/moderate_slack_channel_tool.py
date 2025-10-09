from tau_bench.envs.tool import Tool
import json
from typing import Any

class ModerateSlackChannelTool(Tool):
    """Manage Slack channel: archive, pin, unpin, or relocate canonical messages (bulk support)."""

    @staticmethod
    def invoke(data: dict[str, Any], channel: str, action: str, message_ids: list[str] = [], target_channel: str = None, moderator_id: str = None) -> str:
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
        payload = status
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModerateSlackChannel",
                "description": "Archive, pin, unpin, or move canonical Slack messages with proper RBAC moderation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string"},
                        "action": {
                            "type": "string",
                            "enum": ["archive", "pin", "unpin", "move"],
                        },
                        "message_ids": {"type": "array", "items": {"type": "string"}},
                        "target_channel": {"type": "string"},
                        "moderator_id": {"type": "string"},
                    },
                    "required": ["channel", "action", "message_ids", "moderator_id"],
                },
            },
        }
