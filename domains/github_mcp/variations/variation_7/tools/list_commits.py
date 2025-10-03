from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListCommits(Tool):
    """Display commits for a repository (with an optional branch filter)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, branch: str = None) -> str:
        owner = owner or _actor_name(data)
        result = [
            c
            for c in _commits(data)
            if c.get("owner") == owner and c.get("repo") == repo
        ]
        if branch:
            result = [c for c in result if c.get("branch") == branch]
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listCommits",
                "description": "List commit records for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo"],
                },
            },
        }
