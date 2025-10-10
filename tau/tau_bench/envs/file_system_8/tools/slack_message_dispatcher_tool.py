# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SlackMessageDispatcherTool(Tool):
    """Handles message delivery to designated Slack channels."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_slack_notification",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target_channel = kwargs["channel"]
        msg_content = kwargs["message"]

        # Initialize slack logging if not present
        if data.get("slack_log") is None:
            data["slack_log"] = []

        # Create and store log record
        notification_entry = {
            "channel": target_channel,
            "message": msg_content
        }
        data["slack_log"].append(notification_entry)

        result = {
            "status": "success",
            "log_entry": notification_entry
        }
        return json.dumps(result)
