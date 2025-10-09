from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SendSlackMessage(Tool):
    """Dispatch a message to a Slack channel."""

    @staticmethod
    def invoke(data: dict[str, Any], timestamp: str = None, message: str = None, channel: str = None, reply_to_message_id: str = None,
    thread_id: Any = None,
    ) -> str:
        try:
            slack_messages = data.get("slack_messages", {}).values()
        except:
            slack_messages = []

        existing_ids = [
            int(item["message_id"].replace("SL-", ""))
            for item in slack_messages.values() if item.get("message_id", "").startswith("SL-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        message_id = f"SL-{next_id_num:03d}"

        new_message = {
            "message_id": message_id,
            "timestamp": timestamp,
            "username": "RBAC_BOT",
            "message": message,
            "channel": channel,
            "reply_to_message_id": reply_to_message_id,
        }

        data["slack_messages"][new_message["slack_message_id"]] = new_message
        data["slack_messages"] = slack_messages
        payload = {
            "message": "Slack message sent successfully.",
            "message_details": new_message,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendSlackMessage",
                "description": "Sends a message to a specified Slack channel. Can be used to post new messages or reply to existing ones.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "The channel to post the message in (e.g., '#access-requests').",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the message to be sent.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the message record.",
                        },
                        "reply_to_message_id": {
                            "type": "string",
                            "description": "Optional. The ID of the message to reply to, creating a thread.",
                        },
                    },
                    "required": ["channel", "message", "timestamp"],
                },
            },
        }
