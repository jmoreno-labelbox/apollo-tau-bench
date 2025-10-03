from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddCommit(Tool):
    """Log a commit on a branch (extremely lightweight)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, branch: str = "main", message: str = "") -> str:
        owner = owner or _actor_name(data)
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        seq = (
            sum(
                1
                for c in _commits(data)
                if c.get("owner") == owner and c.get("repo") == repo
            )
            + 1
        )
        sha = f"{branch}-{seq:06d}"
        c = {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "sha": sha,
            "message": message,
            "author": _actor_name(data),
            "timestamp": get_current_timestamp(),
        }
        _commits(data).append(c)
        payload = c
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCommit",
                "description": "Add a commit record to a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["repo"],
                },
            },
        }
