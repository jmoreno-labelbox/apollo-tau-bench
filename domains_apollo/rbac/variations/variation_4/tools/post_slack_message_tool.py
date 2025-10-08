from tau_bench.envs.tool import Tool
import json
from typing import Any

class PostSlackMessageTool(Tool):
    """Send a new message to a Slack channel (write operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], channel: str = None, message: str = None) -> str:
        pass
        # Anticipate: data["slack_messages"] is a collection of dicts sourced from /mnt/data/slack_messages.json
        slack_messages = data.get("slack_messages", [])
        if not isinstance(slack_messages, list):
            payload = {"error": "slack_messages must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(channel, str) or not channel.strip():
            payload = {"error": "channel must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(message, str) or not message.strip():
            payload = {"error": "message must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out

        # Add a new message to the log (simulated posting)
        new_entry = {
            "channel": channel,
            "message": message,
        }
        slack_messages.append(new_entry)
        payload = {"success": f"Message posted to {channel}", "message": new_entry}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostSlackMessage",
                "description": "Post a new message into a Slack channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "Slack channel name or ID, e.g. #general",
                        },
                        "message": {
                            "type": "string",
                            "description": "Text content of the message to post",
                        },
                    },
                    "required": ["channel", "message"],
                },
            },
        }
