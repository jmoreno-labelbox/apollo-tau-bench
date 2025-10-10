# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MergePullRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int, merge_method: str, commit_message: str = None) -> str:
        """Merge a PR using the specified method with optional commit message."""
        pull_requests = list(data.get("pull_requests", {}).values())

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)
                    pr_entry["pr_states"][pr_idx] = "merged"
                    pr_entry["merged_flags"][pr_idx] = True

                    # Use commit_message if provided, otherwise generate default
                    if commit_message:
                        merge_sha = f"merge_{pullNumber}_{merge_method}_{hash(commit_message) % 10000}"
                    else:
                        merge_sha = f"merge_{pullNumber}_{merge_method}"

                    result = {"merged": True, "sha": merge_sha}
                    if commit_message:
                        result["commit_message"] = commit_message

                    return json.dumps(result, indent=2)
                except ValueError:
                    pass

        return json.dumps({"error": f"Pull request #{pullNumber} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_pull_request",
                "description": "Merge a PR using the specified method with optional commit message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"},
                        "merge_method": {"type": "string", "description": "Merge method"},
                        "commit_message": {"type": "string", "description": "Optional commit message for the merge"}
                    },
                    "required": ["owner", "repo", "pullNumber", "merge_method"]
                }
            }
        }
