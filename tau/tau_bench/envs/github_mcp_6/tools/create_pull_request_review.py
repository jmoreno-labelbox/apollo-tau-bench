# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePullRequestReview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int, body: str, event: str) -> str:
        """Create a PR review (comment/approval)."""
        pull_requests = list(data.get("pull_requests", {}).values())

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)

                    # Incorporate review into the current framework.
                    if not pr_entry["pr_comments"][pr_idx]:
                        pr_entry["pr_comments"][pr_idx] = [[]]
                        pr_entry["pr_comment_users"][pr_idx] = [[]]
                        pr_entry["reviewers"][pr_idx] = [[]]
                        pr_entry["review_states"][pr_idx] = [[]]
                        pr_entry["review_events"][pr_idx] = [[]]

                    pr_entry["pr_comments"][pr_idx][0].append(body)
                    pr_entry["pr_comment_users"][pr_idx][0].append(owner)
                    pr_entry["reviewers"][pr_idx][0].append(owner)
                    pr_entry["review_states"][pr_idx][0].append(event)
                    pr_entry["review_events"][pr_idx][0].append(event)

                    review_id = len(pr_entry["pr_comments"][pr_idx][0])
                    return json.dumps({"review_id": review_id, "state": event}, indent=2)
                except ValueError:
                    pass

        return json.dumps({"error": f"Pull request # {pullNumber} is missing"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_pull_request_review",
                "description": "Create a PR review (comment/approval).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"},
                        "body": {"type": "string", "description": "Review body"},
                        "event": {"type": "string", "description": "Review event type"}
                    },
                    "required": ["owner", "repo", "pullNumber", "body", "event"]
                }
            }
        }
