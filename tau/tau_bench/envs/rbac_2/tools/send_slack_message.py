# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendSlackMessage(Tool):
    """ Send a message to a Slack channel. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
            slack_messages = data.get('slack_messages', [])
        except:
            slack_messages = []

        existing_ids = [int(item["message_id"].replace("SL-", "")) for item in slack_messages if item.get("message_id", "").startswith("SL-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        message_id = f"SL-{next_id_num:03d}"

        new_message = {
            "message_id": message_id,
            "timestamp": kwargs.get("timestamp"),
            "username": "RBAC_BOT",
            "message": kwargs.get("message"),
            "channel": kwargs.get("channel"),
            "reply_to_message_id": kwargs.get("reply_to_message_id", None) # Optional for threading
        }

        slack_messages.append(new_message)
        data['slack_messages'] = slack_messages

        return json.dumps({
            "message": "Slack message sent successfully.",
            "message_details": new_message
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_slack_message",
                "description": "Sends a message to a specified Slack channel. Can be used to post new messages or reply to existing ones.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "The channel to post the message in (e.g., '#access-requests')."
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the message to be sent."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the message record."
                        },
                        "reply_to_message_id": {
                            "type": "string",
                            "description": "Optional. The ID of the message to reply to, creating a thread."
                        }
                    },
                    "required": ["channel", "message", "timestamp"]
                }
            }
        }
