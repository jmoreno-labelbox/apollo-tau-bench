from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetPullRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str, repo: str, pullNumber: int) -> str:
        """Get PR details by number."""
        pass
        pull_requests = data.get("pull_requests", [])

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)
                    result = {
                        "state": pr_entry["pr_states"][pr_idx],
                        "head": pr_entry["head_branches"][pr_idx],
                        "base": pr_entry["base_branches"][pr_idx],
                        "mergeable": pr_entry["mergeable_flags"][pr_idx],
                    }
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
                "name": "getPullRequest",
                "description": "Get PR details by number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"},
                    },
                    "required": ["owner", "repo", "pullNumber"],
                },
            },
        }
