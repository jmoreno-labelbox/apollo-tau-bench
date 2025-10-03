from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListAlerts(Tool):
    """Show code scanning alerts for a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None) -> str:
        owner = owner or _actor_name(data)
        result = [
            a
            for a in _alerts(data)
            if a.get("owner") == owner and a.get("repo") == repo
        ]
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listAlerts",
                "description": "List static analysis / scanning alerts for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                    },
                    "required": ["repo"],
                },
            },
        }
