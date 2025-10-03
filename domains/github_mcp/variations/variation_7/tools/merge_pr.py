from tau_bench.envs.tool import Tool
import json
from typing import Any

class MergePR(Tool):
    """Combine a pull request by its number (marks it as merged)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None) -> str:
        owner = owner or _actor_name(data)
        for p in _prs(data):
            if (
                p.get("owner") == owner
                and p.get("repo") == repo
                and p.get("number") == number
            ):
                p["state"] = "merged"
                p["merged_at"] = get_current_timestamp()
                payload = p
                out = json.dumps(payload)
                return out
        raise RuntimeError("PR not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mergePr",
                "description": "Mark a pull request as merged.",
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
