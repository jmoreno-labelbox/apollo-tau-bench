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
    @staticmethod
    def invoke(data: dict[str, Any], username: str = None, channel: str = None, message: str = None,
    thread_id: Any = None,
    ) -> str:
        messages = data.get("slack_messages", {}).values()
        new_id_num = max((int(m["message_id"][3:]) for m in messages.values()), default=0) + 1
        new_message_id = f"SL-{new_id_num:03d}"
        new_message = {
            "message_id": new_message_id,
            "username": username,
            "channel": channel,
            "message": message,
            "timestamp": NOW.strftime(DT_STR_FORMAT),
        }
        data["slack_messages"][new_message["slack_message_id"]] = new_message
        data["slack_messages"] = messages
        payload = new_message
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendSlackMessage",
                "description": "Sends a message to a Slack user or channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "channel": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["username", "channel", "message"],
                },
            },
        }
