from tau_bench.envs.tool import Tool
import json
from typing import Any

class CommentIssue(Tool):
    """Post a comment on an issue."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None, comment: str = "") -> str:
        owner = owner or _actor_name(data)
        for i in _issues(data):
            if (
                i.get("owner") == owner
                and i.get("repo") == repo
                and i.get("number") == number
            ):
                i.setdefault("comments", []).append(
                    {
                        "author": _actor_name(data),
                        "message": comment,
                        "created_at": get_current_timestamp(),
                    }
                )
                payload = {"ok": True}
                out = json.dumps(payload)
                return out
        raise RuntimeError("Issue not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "commentIssue",
                "description": "Add a comment to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "comment": {"type": "string"},
                    },
                    "required": ["repo", "number", "comment"],
                },
            },
        }
