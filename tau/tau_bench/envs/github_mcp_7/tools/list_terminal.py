# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListTerminal(Tool):
    """List terminal log entries (most recent first)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        limit = int(kwargs.get("limit", 50))
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
