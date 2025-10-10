# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendSlackMessage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        messages = data.get('slack_messages', [])
        new_id_num = max((int(m['message_id'][3:]) for m in messages), default=0) + 1
        new_message_id = f"SL-{new_id_num:03d}"
        new_message = {
                "message_id": new_message_id,
                "username": kwargs.get("username"),
                "channel": kwargs.get("channel"),
                "message": kwargs.get("message"),
                "timestamp": NOW.strftime(DT_STR_FORMAT)
        }
        messages.append(new_message)
        data['slack_messages'] = messages
        return json.dumps(new_message)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "send_slack_message",
                        "description": "Sends a message to a Slack user or channel.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "username": {"type": "string"},
                                        "channel": {"type": "string"},
                                        "message": {"type": "string"}
                                },
                                "required": ["username", "channel", "message"]
                        }
                }
        }
