from tau_bench.envs.tool import Tool
import json
from typing import Any

class ResolvePullRequestBlockers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str, repo: str, pullNumber: int) -> str:
        """Resolve blocking issues on a pull request to make it mergeable."""
        pass
        pull_requests = data.get("pull_requests", [])

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)

                    pr_state = pr_entry["pr_states"][pr_idx]
                    mergeable = pr_entry["mergeable_flags"][pr_idx]
                    merged = pr_entry["merged_flags"][pr_idx]
                    review_states = (
                        pr_entry["review_states"][pr_idx]
                        if pr_idx < len(pr_entry["review_states"])
                        else []
                    )

                    if merged:
                        payload = {
                                "resolved": False,
                                "reason": "Pull request is already merged",
                                "state": pr_state,
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    if pr_state == "closed":
                        payload = {
                                "resolved": False,
                                "reason": "Pull request is closed",
                                "state": pr_state,
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out

                    #Verify if any review states are blocking
                    blocking_states = []
                    for review_state in review_states:
                        if review_state in ["PENDING", "REQUEST_CHANGES", "COMMENT"]:
                            blocking_states.append(review_state)

                    if blocking_states:
                        #Address blocking states by converting them to APPROVE
                        resolved_states = []
                        for state in review_states:
                            if state in blocking_states:
                                resolved_states.append("APPROVE")
                            else:
                                resolved_states.append(state)

                        #Refresh the review states within the data
                        pr_entry["review_states"][pr_idx] = resolved_states
                        pr_entry["review_events"][pr_idx] = resolved_states
                        payload = {
                                "resolved": True,
                                "reason": f"Resolved blocking review states: {blocking_states} -> APPROVE",
                                "original_states": review_states,
                                "resolved_states": resolved_states,
                                "mergeable": True,
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out

                    if not mergeable:
                        payload = {
                                "resolved": False,
                                "reason": "Pull request has conflicts that require manual resolution",
                                "mergeable": False,
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    payload = {
                            "resolved": True,
                            "reason": "Pull request is already mergeable",
                            "mergeable": True,
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
                "name": "resolvePullRequestBlockers",
                "description": "Resolve blocking issues on a pull request to make it mergeable by addressing pending reviews, request changes, and other blockers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {
                            "type": "integer",
                            "description": "PR number to resolve blockers for",
                        },
                    },
                    "required": ["owner", "repo", "pullNumber"],
                },
            },
        }
