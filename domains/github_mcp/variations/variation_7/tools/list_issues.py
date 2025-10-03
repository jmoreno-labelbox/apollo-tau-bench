from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListIssues(Tool):
    """Display issues for a repository with an optional state filter."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, state: str = None) -> str:
        owner = owner or _actor_name(data)
        result = [
            i
            for i in _issues(data)
            if i.get("owner") == owner and i.get("repo") == repo
        ]
        if state:
            result = [i for i in result if i.get("state") == state]
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListIssues",
                "description": "List issues in a repository (optionally by state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "state": {"type": "string", "enum": ["open", "closed"]},
                    },
                    "required": ["repo"],
                },
            },
        }
