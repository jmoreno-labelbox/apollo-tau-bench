from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetPullRequest(Tool):
    """Provides information about a particular pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: int = None) -> str:
        if not all([repo_name, pr_number]):
            payload = {"error": "repo_name and pr_number are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        me = _auth(data)["username"]
        for pr in _prs(data):
            if pr["owner"] == me and pr["repo_name"] == repo_name:
                if pr_number in pr["pr_numbers"]:
                    idx = pr["pr_numbers"].index(pr_number)
                    single_pr = {
                        "repo_name": pr["repo_name"],
                        "pr_number": pr_number,
                        "title": pr["pr_titles"][idx],
                        "body": pr["pr_bodies"][idx],
                        "state": pr["pr_states"][idx],
                        "head_branch": pr["head_branches"][idx],
                        "base_branch": pr["base_branches"][idx],
                        "head_sha": pr["head_shas"][idx],
                        "mergeable": pr["mergeable_flags"][idx],
                        "merged": pr["merged_flags"][idx],
                        "files": pr["pr_files"][idx],
                        "comments": pr["pr_comments"][idx],
                        "comment_users": pr["pr_comment_users"][idx],
                        "reviewers": pr["reviewers"][idx],
                        "review_states": pr["review_states"][idx],
                        "review_events": pr["review_events"][idx],
                        "created_ts": pr["created_ts"][idx],
                        "updated_ts": pr["updated_ts"][idx],
                    }
                    payload = single_pr
                    out = json.dumps(payload, indent=2)
                    return out
        payload = {"error": "Pull request not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetPullRequest",
                "description": "Returns details of a specific pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["repo_name"],
                },
            },
        }
