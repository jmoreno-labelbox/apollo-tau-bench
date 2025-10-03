from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListBranches(Tool):
    """Show branches associated with a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None) -> str:
        owner = owner or _actor_name(data)
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        payload = {"default": r.get("default_branch"), "branches": r.get("branches") or []}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListBranches",
                "description": "List branches in a repository.",
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
