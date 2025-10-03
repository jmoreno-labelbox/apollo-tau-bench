from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListRepos(Tool):
    """Display repositories that belong to the authenticated user."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _actor_name(data)
        items = [r for r in _repos(data) if r.get("owner") == me]
        payload = items
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRepos",
                "description": "List repositories for the current user.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
