from tau_bench.envs.tool import Tool
import json
from typing import Any

class ClosePR(Tool):
    """Shut a pull request without merging."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None) -> str:
        owner = owner or _actor_name(data)
        for p in _prs(data):
            if (
                p.get("owner") == owner
                and p.get("repo") == repo
                and p.get("number") == number
            ):
                p["state"] = "closed"
                p["closed_at"] = get_current_timestamp()
                payload = p
                out = json.dumps(payload)
                return out
        raise RuntimeError("PR not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ClosePr",
                "description": "Close a pull request without merging.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                    },
                    "required": ["repo", "number"],
                },
            },
        }
