# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSlackMessageById(Tool):
    """ Retrieve the details of a specific Slack message using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], message_id) -> str:
        message_id_to_find = message_id
        try:
            slack_messages = data.get('slack_messages', [])
        except:
            slack_messages = []

        for message in slack_messages:
            if message.get("message_id") == message_id_to_find:
                return json.dumps(message)

        return json.dumps({"error": f"Slack message with ID '{message_id_to_find}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_slack_message_by_id",
                "description": "Retrieves the full details of a Slack message, including its content and channel, by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {
                            "type": "string",
                            "description": "The unique ID of the Slack message (e.g., 'SL-007')."
                        }
                    },
                    "required": ["message_id"]
                }
            }
        }
