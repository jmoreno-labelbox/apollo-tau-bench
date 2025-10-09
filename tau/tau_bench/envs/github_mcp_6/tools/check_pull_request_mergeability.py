from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CheckPullRequestMergeability(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str, repo: str, pullNumber: int) -> str:
        """Check if a pull request is mergeable by examining its status and review state."""
        pass
        pull_requests = data.get("pull_requests", [])

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)

                    #Retrieve details of the PR
                    pr_state = pr_entry["pr_states"][pr_idx]
                    mergeable = pr_entry["mergeable_flags"][pr_idx]
                    merged = pr_entry["merged_flags"][pr_idx]
                    review_states = (
                        pr_entry["review_states"][pr_idx]
                        if pr_idx < len(pr_entry["review_states"])
                        else []
                    )

                    #Verify if the PR has been merged
                    if merged:
                        payload = {
                                "mergeable": False,
                                "reason": "Pull request is already merged",
                                "state": pr_state,
                                "review_states": review_states,
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out

                    #Determine if the PR is closed
                    if pr_state == "closed":
                        payload = {
                                "mergeable": False,
                                "reason": "Pull request is closed",
                                "state": pr_state,
                                "review_states": review_states,
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out

                    #Assess if the PR can be merged
                    if not mergeable:
                        payload = {
                                "mergeable": False,
                                "reason": "Pull request has conflicts or is not mergeable",
                                "state": pr_state,
                                "review_states": review_states,
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out

                    #Examine the states of reviews
                    if not review_states:
                        payload = {
                                "mergeable": False,
                                "reason": "Pull request has no reviews",
                                "state": pr_state,
                                "review_states": review_states,
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out

                    #Determine if any review is awaiting action or needs modifications
                    for review_state in review_states:
                        if review_state in ["PENDING", "REQUEST_CHANGES", "COMMENT"]:
                            payload = {
                                    "mergeable": False,
                                    "reason": f"Pull request has {review_state} review state",
                                    "state": pr_state,
                                    "review_states": review_states,
                                }
                            out = json.dumps(
                                payload, indent=2,
                            )
                            return out
                    payload = {
                            "mergeable": True,
                            "reason": "All checks passed and reviews approved",
                            "state": pr_state,
                            "review_states": review_states,
                        }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out

                except (ValueError, IndexError):
                    pass
        payload = {"error": f"Pull request #{pullNumber} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "checkPullRequestMergeability",
                "description": "Check if a pull request is mergeable by examining its status, review states, and mergeable flags.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {
                            "type": "integer",
                            "description": "PR number to check",
                        },
                    },
                    "required": ["owner", "repo", "pullNumber"],
                },
            },
        }
