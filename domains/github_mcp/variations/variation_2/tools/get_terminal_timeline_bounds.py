from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetTerminalTimelineBounds(Tool):
    """Delivers the first and last printed_ts from the terminal log."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        logs = _terminal(data)
        timestamps = sorted(
            [entry.get("printed_ts") for entry in logs if entry.get("printed_ts")]
        )
        if not timestamps:
            payload = {"error": "No terminal entries with timestamps found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"first_timestamp": timestamps[0], "last_timestamp": timestamps[-1]}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTerminalTimelineBounds",
                "description": "Returns first and last terminal log timestamps.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
