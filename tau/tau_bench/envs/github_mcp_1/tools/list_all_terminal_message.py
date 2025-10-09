from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListAllTerminalMessage(Tool):
    """
    Return all terminal log lines formatted as 'timestamp : message'.
    Reads from data['terminal'] which may be a list (entry at index 0) or a dict
    with keys 'printed_ts' and 'messages'.
    """

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        # Load terminal entry
        terminal = data.get("terminal", {}).values()
        if isinstance(terminal, list):
            entry = terminal[0] if terminal else {"printed_ts": [], "messages": []}
        elif isinstance(terminal, dict):
            entry = terminal
        else:
            payload = {
                "error": "Invalid database format: 'terminal' must be a list or dict."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        ts_list = entry.get("printed_ts", [])
        msg_list = entry.get("messages", [])

        if not isinstance(ts_list, list) or not isinstance(msg_list, list):
            payload = {
                "error": "Invalid terminal entry: 'printed_ts' and 'messages' must be lists."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Pair up to the shortest length
        n = min(len(ts_list), len(msg_list))
        lines: list[str] = [f"{ts_list[i]} : {msg_list[i]}" for i in range(n)]

        result = {"messages": lines[32:]}
        if len(ts_list) != len(msg_list):
            result["note"] = "Lengths differ; output truncated to the shortest list."
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAllTerminalMessage",
                "description": "List all terminal messages formatted as 'timestamp : message'.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
