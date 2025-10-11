# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPullRequestTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get('owner')
        repo = kwargs.get('repo')
        pr_number = kwargs.get('pr_number')

        if not all([owner, repo, pr_number]):
            return json.dumps({
                "status": "error",
                "message": "Missing required parameters for get_pull_request.",
                "required": ["owner", "repo", "pr_number"]
            }, indent=2)

        repositories = list(data.get('repositories', {}).values())
        repository = next((r for r in repositories if r['repo_name'] == repo and r['owner'] == owner), None)

        if not repository:
            return json.dumps({
                "status": "error",
                "message": f"Repository '{repo}' not found for owner '{owner}'.",
            }, indent=2)

        pull_requests = repository.get('pull_requests', [])
        pull_request = next((pr for pr in pull_requests if pr['pr_number'] == pr_number), None)

        if not pull_request:
            return json.dumps({
                "status": "error",
"message": f"Pull request number {pr_number} does not exist in the '{repo}' repository.",
            }, indent=2)

        return json.dumps({
            "status": "success",
            "pull_request": pull_request
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pull_request",
                "description": "Retrieves a specific pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "The owner of the repository."},
                        "repo": {"type": "string", "description": "The name of the repository."},
                        "pr_number": {"type": "integer", "description": "The number of the pull request."}
                    },
                    "required": ["owner", "repo", "pr_number"],
                },
            },
        }