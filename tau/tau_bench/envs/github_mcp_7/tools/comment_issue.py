# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CommentIssue(Tool):
    """Add a comment to an issue."""
    @staticmethod
    def invoke(data: Dict[str, Any], comment, number, owner, repo) -> str:
        owner = owner or _actor_name(data)
        comment = comment or ""
        for i in _issues(data):
            if i.get("owner") == owner and i.get("repo") == repo and i.get("number") == number:
                i.setdefault("comments", []).append({
                    "author": _actor_name(data),
                    "message": comment,
                    "created_at": get_current_timestamp()
                })
                return json.dumps({"ok": True})
        raise RuntimeError("Issue not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "comment_issue",
                "description": "Add a comment to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "comment": {"type": "string"}
                    },
                    "required": ["repo", "number", "comment"]
                }
            },
        }
