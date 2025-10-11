# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAllTerminalMessage(Tool):
    """
    Return all terminal log lines formatted as 'timestamp : message'.
    Reads from data['terminal'] which may be a list (entry at index 0) or a dict
    with keys 'printed_ts' and 'messages'.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        # Import terminal input
        terminal = data.get("terminal", [])
        if isinstance(terminal, list):
            entry = terminal[0] if terminal else {"printed_ts": [], "messages": []}
        elif isinstance(terminal, dict):
            entry = terminal
        else:
            return json.dumps(
                {"error": "Invalid database format: 'terminal' must be a list or dict."},
                indent=2
            )

        ts_list = entry.get("printed_ts", [])
        msg_list = entry.get("messages", [])

        if not isinstance(ts_list, list) or not isinstance(msg_list, list):
            return json.dumps(
                {"error": "Invalid terminal entry: 'printed_ts' and 'messages' must be lists."},
                indent=2
            )

        # Match to the minimal length.
        n = min(len(ts_list), len(msg_list))
        lines: List[str] = [f"{ts_list[i]} : {msg_list[i]}" for i in range(n)]

        result = {
            "messages": lines[32:]
        }
        if len(ts_list) != len(msg_list):
            result["note"] = "Lengths differ; output truncated to the shortest list."

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_all_terminal_message",
                "description": "List all terminal messages formatted as 'timestamp : message'.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
