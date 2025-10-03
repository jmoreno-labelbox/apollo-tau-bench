from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReopenPR(Tool):
    """Reactivate a pull request that was closed earlier."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None) -> str:
        owner = owner or _actor_name(data)
        for p in _prs(data):
            if (
                p.get("owner") == owner
                and p.get("repo") == repo
                and p.get("number") == number
            ):
                p["state"] = "open"
                p["reopened_at"] = get_current_timestamp()
                payload = p
                out = json.dumps(payload)
                return out
        raise RuntimeError("PR not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReopenPr",
                "description": "Reopen a pull request.",
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
