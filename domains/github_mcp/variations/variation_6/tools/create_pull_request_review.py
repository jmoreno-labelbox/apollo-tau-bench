from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreatePullRequestReview(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str,
        repo: str,
        pullNumber: int,
        body: str,
        event: str,
    ) -> str:
        """Create a PR review (comment/approval)."""
        pass
        pull_requests = data.get("pull_requests", [])

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)

                    #Incorporate review into the current structure
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
                    payload = {"review_id": review_id, "state": event}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                except ValueError:
                    pass
        payload = {"error": f"Pull request #{pullNumber} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createPullRequestReview",
                "description": "Create a PR review (comment/approval).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"},
                        "body": {"type": "string", "description": "Review body"},
                        "event": {"type": "string", "description": "Review event type"},
                    },
                    "required": ["owner", "repo", "pullNumber", "body", "event"],
                },
            },
        }
