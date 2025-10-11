# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckPullRequestMergeability(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int) -> str:
        """Check if a pull request is mergeable by examining its status and review state."""
        pull_requests = list(data.get("pull_requests", {}).values())

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)

                    # Retrieve pull request information.
                    pr_state = pr_entry["pr_states"][pr_idx]
                    mergeable = pr_entry["mergeable_flags"][pr_idx]
                    merged = pr_entry["merged_flags"][pr_idx]
                    review_states = pr_entry["review_states"][pr_idx] if pr_idx < len(pr_entry["review_states"]) else []

                    # Verify if the pull request has been merged.
                    if merged:
                        return json.dumps({
                            "mergeable": False,
                            "reason": "Pull request is already merged",
                            "state": pr_state,
                            "review_states": review_states
                        }, indent=2)

                    # Verify if the pull request is closed.
                    if pr_state == "closed":
                        return json.dumps({
                            "mergeable": False,
                            "reason": "Pull request is closed",
                            "state": pr_state,
                            "review_states": review_states
                        }, indent=2)

                    # Verify if the pull request can be merged.
                    if not mergeable:
                        return json.dumps({
                            "mergeable": False,
                            "reason": "Pull request has conflicts or is not mergeable",
                            "state": pr_state,
                            "review_states": review_states
                        }, indent=2)

                    # Verify review statuses
                    if not review_states:
                        return json.dumps({
                            "mergeable": False,
                            "reason": "Pull request has no reviews",
                            "state": pr_state,
                            "review_states": review_states
                        }, indent=2)

                    # Verify if any reviews are outstanding or need modifications.
                    for review_state in review_states:
                        if review_state in ["PENDING", "REQUEST_CHANGES", "COMMENT"]:
                            return json.dumps({
                                "mergeable": False,
                                "reason": f"Pull request has {review_state} review state",
                                "state": pr_state,
                                "review_states": review_states
                            }, indent=2)

                    # Reaching this point indicates that the PR is ready to be merged.
                    return json.dumps({
                        "mergeable": True,
                        "reason": "All checks passed and reviews approved",
                        "state": pr_state,
                        "review_states": review_states
                    }, indent=2)

                except (ValueError, IndexError):
                    pass

        return json.dumps({"error": f"Pull request # {pullNumber} not located"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_pull_request_mergeability",
                "description": "Check if a pull request is mergeable by examining its status, review states, and mergeable flags.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number to check"}
                    },
                    "required": ["owner", "repo", "pullNumber"]
                }
            }
        }
