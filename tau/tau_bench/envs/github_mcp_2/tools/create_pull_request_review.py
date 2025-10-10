# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePullRequestReview(Tool):
    """Adds a review (approve or changes requested or just a comment) to a pull request."""

    @staticmethod
    def invoke(data: Dict[str, Any], pr_number, repo_name, review_decision, comment = "") -> str:

        if not all([repo_name, pr_number, review_decision]):
            return json.dumps({"error": "repo_name, pr_number, and review_decision are required."}, indent=2)

        if review_decision not in ["approve", "request_changes", "comment"]:
            return json.dumps({"error": "Invalid review_decision (must be 'approve' or 'request_changes' or 'comment)."}, indent=2)

        me = _auth(data)["username"]
        pr = next((p for p in _prs(data) if p["owner"] == me and p["repo_name"] == repo_name and int(pr_number) in p["pr_numbers"]), None)

        if not pr:
            return json.dumps({"error": "Pull request not found."}, indent=2)

        pr.setdefault("reviews", []).append({
            "author": me,
            "decision": review_decision,
            "comment": comment,
            "timestamp": get_current_timestamp()
        })

        return json.dumps({"message": "Review submitted."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_pull_request_review",
                "description": "Adds a review (approve or request_changes or comment) to a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "review_decision": {"type": "string", "enum": ["approve", "request_changes", "comment"]},
                        "comment": {"type": "string"}
                    },
                    "required": ["repo_name", "pr_number", "review_decision"]
                }
            }
        }
