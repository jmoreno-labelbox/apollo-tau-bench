from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class GetSlackMessageById(Tool):
    """Fetch the details of a specific Slack message by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], message_id: str = None) -> str:
        message_id_to_find = message_id
        try:
            slack_messages = data.get("slack_messages", [])
        except:
            slack_messages = []

        for message in slack_messages:
            if message.get("message_id") == message_id_to_find:
                payload = message
                out = json.dumps(payload)
                return out
        payload = {"error": f"Slack message with ID '{message_id_to_find}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSlackMessageById",
                "description": "Retrieves the full details of a Slack message, including its content and channel, by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {
                            "type": "string",
                            "description": "The unique ID of the Slack message (e.g., 'SL-007').",
                        }
                    },
                    "required": ["message_id"],
                },
            },
        }
