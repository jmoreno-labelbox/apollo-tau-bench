# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendSlackMessage(Tool):
    """Sends a message to a specified Slack channel."""
    @staticmethod
    def invoke(data: Dict[str, Any], channel_name) -> str:
        messages = data.get('slack_messages', [])
        new_id = f"msg_{max((int(m['message_id'].split('_')[-1]) for m in messages), default=0) + 1:03d}"

        # Dynamically create a suitable message according to the channel name.
        if channel_name == "System Alerts":
            message = f"System alert notification sent to {channel_name} channel at {new_id}"
        elif channel_name == "Operations":
            message = f"Operations update sent to {channel_name} channel at {new_id}"
        elif channel_name == "File Check":
            message = f"File check notification sent to {channel_name} channel at {new_id}"
        else:
            message = f"Automated notification sent to {channel_name} channel at {new_id}"

        channel_id = ""
        for channel in data.get('slack_channels', []):
            if channel.get('name') == channel_name:
                channel_id = channel.get("channel_id")
                break
        if not channel_id:
            return json.dumps({"error": f"Channel '{channel_name}' not found."})

        new_message = {
            "message_id": new_id, "channel_id": channel_id, "user_id": "system_agent", "username": "AutomationAgent", "message": message, "timestamp": "2024-01-20T14:00:00Z", "type": "notification"}
        messages.append(new_message)
        data['slack_messages'] = messages
        return json.dumps(new_message)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "send_slack_message", "description": "Posts an automatically generated message to a Slack channel for notifications and alerts.", "parameters": {"type": "object", "properties": {"channel_name": {"type": "string", "description": "The name of the public channel (e.g., 'System Alerts', 'Operations', 'File Check')."}}, "required": ["channel_name"]}}}
