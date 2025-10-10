# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListTerminalLastMessage(Tool):
    """Returns last terminal log entry."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        terminal_log = _terminal(data)
        # print("terminal log:", terminal_log)
        if not terminal_log:
            return json.dumps({"error": "No terminal messages found."}, indent=2)

        # Get the last message from the most recent log group
        last_ts = terminal_log[-1]["printed_ts"]
        # print("term_log::", terminal_log)
        last_item = terminal_log[-1]
        last_msg = (
            last_item.get("messages")[-1]
            if last_item.get("messages")
            else last_item.get("message")
        )
        print("last_msg:::", last_msg)

        return json.dumps({
            "timestamp": last_ts,
            "message": last_msg
        }, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_terminal_last_message",
                "description": "Returns terminal last log message with timestamp.",
                "parameters": {"type": "object", "properties": {}},
            }
        }
