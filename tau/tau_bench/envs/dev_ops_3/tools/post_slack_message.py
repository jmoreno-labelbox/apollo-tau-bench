# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class post_slack_message(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], channel: str, message: str) -> str:
        return json.dumps({"success": f"Message posted to channel '{channel}'."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "post_slack_message", "description": "Posts a message to a specified Slack channel.", "parameters": { "type": "object", "properties": { "channel": { "type": "string" }, "message": { "type": "string" } }, "required": ["channel", "message"] } } }
