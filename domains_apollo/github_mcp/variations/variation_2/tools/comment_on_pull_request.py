from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class CommentOnPullRequest(Tool):
    """Inserts a human comment into the discussion thread of the pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: int = None, comment: str = None) -> str:
        if not all([repo_name, pr_number, comment]):
            payload = {"error": "repo_name, pr_number and comment are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        me = _auth(data)["username"]
        pr = next(
            (
                p
                for p in _prs(data)
                if p["owner"] == me
                and p["repo_name"] == repo_name
                and int(pr_number) in p["pr_numbers"]
            ),
            None,
        )

        if not pr:
            payload = {"error": "Pull request not found."}
            out = json.dumps(payload, indent=2)
            return out

        pr.setdefault("comments", []).append(
            {"author": me, "comment": comment, "timestamp": get_current_timestamp()}
        )
        payload = {"message": "Comment added to pull request."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CommentOnPullRequest",
                "description": "Adds a comment to a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "comment": {"type": "string"},
                    },
                    "required": ["repo_name", "pr_number", "comment"],
                },
            },
        }
