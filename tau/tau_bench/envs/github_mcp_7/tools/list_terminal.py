# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _terminal(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("terminal", [])

class ListTerminal(Tool):
    """List terminal log entries (most recent first)."""
    @staticmethod
    def invoke(data: Dict[str, Any], limit = 50) -> str:
        limit = int(limit)
        logs = list(reversed(_terminal(data)))[:limit]
        return json.dumps(logs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_terminal",
                "description": "List recent terminal log entries.",
                "parameters": {"type": "object", "properties": {"limit": {"type": "integer"}}}
            },
        }