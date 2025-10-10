# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ResolvePullRequestBlockers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int) -> str:
        """Resolve blocking issues on a pull request to make it mergeable."""
        pull_requests = list(data.get("pull_requests", {}).values())

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)

                    pr_state = pr_entry["pr_states"][pr_idx]
                    mergeable = pr_entry["mergeable_flags"][pr_idx]
                    merged = pr_entry["merged_flags"][pr_idx]
                    review_states = pr_entry["review_states"][pr_idx] if pr_idx < len(pr_entry["review_states"]) else []

                    if merged:
                        return json.dumps({"resolved": False, "reason": "Pull request is already merged", "state": pr_state}, indent=2)
                    if pr_state == "closed":
                        return json.dumps({"resolved": False, "reason": "Pull request is closed", "state": pr_state}, indent=2)

                    # Verify for any obstructing review statuses.
                    blocking_states = []
                    for review_state in review_states:
                        if review_state in ["PENDING", "REQUEST_CHANGES", "COMMENT"]:
                            blocking_states.append(review_state)

                    if blocking_states:
                        # Change blocking states to APPROVE to resolve them.
                        resolved_states = []
                        for state in review_states:
                            if state in blocking_states:
                                resolved_states.append("APPROVE")
                            else:
                                resolved_states.append(state)

                        # Revise the review statuses in the dataset.
                        pr_entry["review_states"][pr_idx] = resolved_states
                        pr_entry["review_events"][pr_idx] = resolved_states

                        return json.dumps({
                            "resolved": True,
                            "reason": f"Resolved blocking review states: {blocking_states} -> APPROVE",
                            "original_states": review_states,
                            "resolved_states": resolved_states,
                            "mergeable": True
                        }, indent=2)

                    if not mergeable:
                        # If there are conflicts preventing a merge, we cannot handle resolution through code.
                        return json.dumps({"resolved": False, "reason": "Pull request has conflicts that require manual resolution", "mergeable": False}, indent=2)

                    return json.dumps({"resolved": True, "reason": "Pull request is already mergeable", "mergeable": True}, indent=2)

                except (ValueError, IndexError):
                    pass

        return json.dumps({"error": f"Pull request # {pullNumber} does not exist"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolve_pull_request_blockers",
                "description": "Resolve blocking issues on a pull request to make it mergeable by addressing pending reviews, request changes, and other blockers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number to resolve blockers for"}
                    },
                    "required": ["owner", "repo", "pullNumber"]
                }
            }
        }
