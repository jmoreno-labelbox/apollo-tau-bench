# Sierra copyright notice

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _terminal(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("terminal", [])

class GetTerminalTimelineBounds(Tool):
    """Returns first and last printed_ts from terminal log."""

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        logs = _terminal(data)
        timestamps = sorted([entry.get("printed_ts") for entry in logs if entry.get("printed_ts")])
        if not timestamps:
            return json.dumps({"error": "No terminal entries with timestamps found."}, indent=2)

        return json.dumps({
            "first_timestamp": timestamps[0],
            "last_timestamp": timestamps[-1]
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_terminal_timeline_bounds",
                "description": "Returns first and last terminal log timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }