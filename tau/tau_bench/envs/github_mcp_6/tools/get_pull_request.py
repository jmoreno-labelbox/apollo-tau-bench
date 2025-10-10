# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPullRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, pullNumber: int) -> str:
        """Get PR details by number."""
        pull_requests = list(data.get("pull_requests", {}).values())

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)
                    result = {
                        "state": pr_entry["pr_states"][pr_idx],
                        "head": pr_entry["head_branches"][pr_idx],
                        "base": pr_entry["base_branches"][pr_idx],
                        "mergeable": pr_entry["mergeable_flags"][pr_idx]
                    }
                    return json.dumps(result, indent=2)
                except ValueError:
                    pass

        return json.dumps({"error": f"Pull request # {pullNumber} could not be located"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pull_request",
                "description": "Get PR details by number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"}
                    },
                    "required": ["owner", "repo", "pullNumber"]
                }
            }
        }
