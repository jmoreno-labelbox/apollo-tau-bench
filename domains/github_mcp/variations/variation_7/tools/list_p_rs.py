from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListPRs(Tool):
    """Show pull requests for a repository with an optional state filter."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, state: str = None) -> str:
        pass
        owner = owner or _actor_name(data)
        result = [
            p for p in _prs(data) if p.get("owner") == owner and p.get("repo") == repo
        ]
        if state:
            result = [p for p in result if p.get("state") == state]
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPrs",
                "description": "List pull requests for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "state": {
                            "type": "string",
                            "enum": ["open", "closed", "merged"],
                        },
                    },
                    "required": ["repo"],
                },
            },
        }
