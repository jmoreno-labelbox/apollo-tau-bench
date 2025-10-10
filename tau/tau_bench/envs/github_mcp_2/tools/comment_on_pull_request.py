# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CommentOnPullRequest(Tool):
    """Adds a human comment to the pull request discussion thread."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        pr_number = kwargs.get("pr_number")
        comment = kwargs.get("comment")

        if not all([repo_name, pr_number, comment]):
            return json.dumps({"error": "repo_name, pr_number and comment are required."}, indent=2)

        me = _auth(data)["username"]
        pr = next((p for p in _prs(data) if p["owner"] == me and p["repo_name"] == repo_name and int(pr_number) in p["pr_numbers"]), None)

        if not pr:
            return json.dumps({"error": "Pull request not found."}, indent=2)

        pr.setdefault("comments", []).append({
            "author": me,
            "comment": comment,
            "timestamp": get_current_timestamp()
        })

        return json.dumps({"message": "Comment added to pull request."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "comment_on_pull_request",
                "description": "Adds a comment to a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "comment": {"type": "string"}
                    },
                    "required": ["repo_name", "pr_number", "comment"]
                }
            }
        }
