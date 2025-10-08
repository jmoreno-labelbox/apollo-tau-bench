from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class CreatePullRequestReview(Tool):
    """Incorporates a review (approval, requested changes, or merely a comment) into a pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: int = None, review_decision: str = None, comment: str = "",
    body: Any = None,
    ) -> str:
        if not all([repo_name, pr_number, review_decision]):
            payload = {"error": "repo_name, pr_number, and review_decision are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if review_decision not in ["approve", "request_changes", "comment"]:
            payload = {
                    "error": "Invalid review_decision (must be 'approve' or 'request_changes' or 'comment)."
                }
            out = json.dumps(
                payload, indent=2,
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

        pr.setdefault("reviews", []).append(
            {
                "author": me,
                "decision": review_decision,
                "comment": comment,
                "timestamp": get_current_timestamp(),
            }
        )
        payload = {"message": "Review submitted."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreatePullRequestReview",
                "description": "Adds a review (approve or request_changes or comment) to a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "review_decision": {
                            "type": "string",
                            "enum": ["approve", "request_changes", "comment"],
                        },
                        "comment": {"type": "string"},
                    },
                    "required": ["repo_name", "pr_number", "review_decision"],
                },
            },
        }
