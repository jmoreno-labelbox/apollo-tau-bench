from tau_bench.envs.tool import Tool
import json
from typing import Any

class post_slack_message(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], channel: str, message: str) -> str:
        pass
        payload = {"success": f"Message posted to channel '{channel}'."}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostSlackMessage",
                "description": "Posts a message to a specified Slack channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["channel", "message"],
                },
            },
        }
