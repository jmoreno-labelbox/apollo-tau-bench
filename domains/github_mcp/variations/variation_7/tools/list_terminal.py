from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListTerminal(Tool):
    """Display terminal log entries with the most recent ones first."""

    @staticmethod
    def invoke(data: dict[str, Any], limit: int = 50) -> str:
        logs = list(reversed(_terminal(data)))[:limit]
        payload = logs
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listTerminal",
                "description": "List recent terminal log entries.",
                "parameters": {
                    "type": "object",
                    "properties": {"limit": {"type": "integer"}},
                },
            },
        }
