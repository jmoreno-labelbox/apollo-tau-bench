# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendSlackNotificationTool(Tool):
    """General-purpose tool to send a notification to a Slack channel."""

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
        channel = kwargs["channel"]
        message = kwargs["message"]
        if "slack_log" not in data:
            data["slack_log"] = []
        log_entry = {"channel": channel, "message": message}
        data["slack_log"].append(log_entry)
        return json.dumps({"status": "success", "log_entry": log_entry})
