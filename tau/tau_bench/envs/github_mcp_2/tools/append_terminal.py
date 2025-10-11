# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _terminal(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("terminal", [])

class AppendTerminal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message) -> str:
        msg = message
        if not msg:
            return json.dumps({"error": "message is required."}, indent=2)
        entry = {"printed_ts": get_current_timestamp(), "message": str(msg)}
        _terminal(data).append(entry)
        return json.dumps(entry, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "append_terminal",
                "description": "Appends a message to terminal log with timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string"}
                    },
                    "required": ["message"]
                }
            }
        }