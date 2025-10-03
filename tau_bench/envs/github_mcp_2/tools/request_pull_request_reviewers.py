from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class RequestPullRequestReviewers(Tool):
    """Solicits one or more reviewers for a pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: str = None, reviewers: list[str] = None) -> str:
        if reviewers is None:
            reviewers = []

        if (
            not all([repo_name, pr_number])
            or not isinstance(reviewers, list)
            or len(reviewers) == 0
        ):
            payload = {
                    "error": "repo_name, pr_number and non-empty reviewers[] are required."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        me = _auth(data)["username"]

        #locate PR owned by the current user (aligned with your other tools)
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

        #Include reviewers
        existing = set(pr.get("requested_reviewers", []))
        for r in reviewers:
            if r != me:
                existing.add(r)
        pr["requested_reviewers"] = sorted(existing)
        payload = {
                "message": "Reviewers requested.",
                "pr_number": pr_number,
                "requested_reviewers": pr["requested_reviewers"],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RequestPullRequestReviewers",
                "description": "Request reviewers on a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "reviewers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Usernames to request for review",
                        },
                    },
                    "required": ["repo_name", "pr_number", "reviewers"],
                },
            },
        }
