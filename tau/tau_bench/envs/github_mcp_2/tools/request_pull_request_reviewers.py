# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RequestPullRequestReviewers(Tool):
    """Requests one or more reviewers on a pull request."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        pr_number = kwargs.get("pr_number")
        reviewers = kwargs.get("reviewers", [])  # List of strings

        if not all([repo_name, pr_number]) or not isinstance(reviewers, list) or len(reviewers) == 0:
            return json.dumps({"error": "repo_name, pr_number and non-empty reviewers[] are required."}, indent=2)

        me = _auth(data)["username"]

        # retrieve PRs controlled by the active user (aligned with your other utilities)
        pr = next(
            (p for p in _prs(data)
             if p["owner"] == me and p["repo_name"] == repo_name and int(pr_number) in p["pr_numbers"]),
            None
        )
        if not pr:
            return json.dumps({"error": "Pull request not found."}, indent=2)

        # Include reviewers
        existing = set(pr.get("requested_reviewers", []))
        for r in reviewers:
            if r != me:
                existing.add(r)
        pr["requested_reviewers"] = sorted(existing)

        return json.dumps({
            "message": "Reviewers requested.",
            "pr_number": pr_number,
            "requested_reviewers": pr["requested_reviewers"]
        }, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "request_pull_request_reviewers",
                "description": "Request reviewers on a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "reviewers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Usernames to request for review"
                        }
                    },
                    "required": ["repo_name", "pr_number", "reviewers"]
                }
            }
        }
