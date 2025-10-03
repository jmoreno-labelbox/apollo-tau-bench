from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListTerminalLastMessage(Tool):
    """Provides the most recent terminal log entry."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        terminal_log = _terminal(data)
        #print("terminal log:", terminal_log)
        if not terminal_log:
            payload = {"error": "No terminal messages found."}
            out = json.dumps(payload, indent=2)
            return out

        #Retrieve the last message from the latest log group
        last_ts = terminal_log[-1]["printed_ts"]
        #print("term_log::", terminal_log)
        last_item = terminal_log[-1]
        last_msg = (
            last_item.get("messages")[-1]
            if last_item.get("messages")
            else last_item.get("message")
        )
        print("last_msg:::", last_msg)
        payload = {"timestamp": last_ts, "message": last_msg}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListTerminalLastMessage",
                "description": "Returns terminal last log message with timestamp.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
