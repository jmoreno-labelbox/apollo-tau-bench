from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SubmitPullRequestForReview(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str,
        repo: str,
        pullNumber: int,
        reviewers: str,
        submission_message: str = None,
    ) -> str:
        """Submit a PR for review by requesting specific reviewers and marking it ready for review."""
        pass
        pull_requests = data.get("pull_requests", [])
        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)
                    #Indicate PR is ready for review (not in draft status)
                    pr_entry["pr_states"][pr_idx] = "open"

                    #Analyze reviewers (string separated by commas)
                    reviewer_list = [
                        r.strip() for r in reviewers.split(",") if r.strip()
                    ]

                    #Set up review structures if necessary
                    if len(pr_entry["reviewers"][pr_idx]) == 0:
                        pr_entry["reviewers"][pr_idx] = [[]]
                        pr_entry["review_states"][pr_idx] = [[]]
                        pr_entry["review_events"][pr_idx] = [[]]

                    #Include reviewers with a pending status
                    for reviewer in reviewer_list:
                        if reviewer not in pr_entry["reviewers"][pr_idx][0]:
                            pr_entry["reviewers"][pr_idx][0].append(reviewer)
                            pr_entry["review_states"][pr_idx][0].append("pending")
                            pr_entry["review_events"][pr_idx][0].append(
                                "review_requested"
                            )

                    #Include submission comment if available
                    if submission_message:
                        if len(pr_entry["pr_comments"][pr_idx]) == 0:
                            pr_entry["pr_comments"][pr_idx] = [[]]
                            pr_entry["pr_comment_users"][pr_idx] = [[]]
                        pr_entry["pr_comments"][pr_idx][0].append(submission_message)
                        pr_entry["pr_comment_users"][pr_idx][0].append(owner)

                    result = {
                        "submitted": True,
                        "pr_number": pullNumber,
                        "state": "ready_for_review",
                        "requested_reviewers": reviewer_list,
                        "submission_timestamp": "2023-12-05T12:30:00Z",
                    }
                    if submission_message:
                        result["submission_message"] = submission_message
                    payload = result
                    out = json.dumps(payload, indent=2)
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
                "name": "submitPullRequestForReview",
                "description": "Submit a PR for review by requesting specific reviewers and marking it ready for review.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"},
                        "reviewers": {
                            "type": "string",
                            "description": "Comma-separated list of reviewer usernames",
                        },
                        "submission_message": {
                            "type": "string",
                            "description": "Optional comment to add when submitting for review",
                        },
                    },
                    "required": ["owner", "repo", "pullNumber", "reviewers"],
                },
            },
        }
