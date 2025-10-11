# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PostSlackMessageTool(Tool):
    """Post a new message into a Slack channel (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Assume: data["slack_messages"] consists of a list of dictionaries sourced from /mnt/data/slack_messages.json.
        slack_messages = data.get("slack_messages", [])
        if not isinstance(slack_messages, list):
            return json.dumps({"error": "slack_messages must be a list"}, indent=2)

        channel = kwargs.get("channel")
        message = kwargs.get("message")

        if not isinstance(channel, str) or not channel.strip():
            return json.dumps({"error": "channel must be a non-empty string"}, indent=2)
        if not isinstance(message, str) or not message.strip():
            return json.dumps({"error": "message must be a non-empty string"}, indent=2)

        # Add a new entry to the log (simulated posting)
        new_entry = {
            "channel": channel,
            "message": message,
        }
        slack_messages.append(new_entry)

        return json.dumps({"success": f"Message posted to {channel}", "message": new_entry}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "post_slack_message",
                "description": "Post a new message into a Slack channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
"description": "Slack channel name or ID, e.g. #broad"
                        },
                        "message": {
                            "type": "string",
                            "description": "Text content of the message to post"
                        }
                    },
                    "required": ["channel", "message"],
                },
            },
        }