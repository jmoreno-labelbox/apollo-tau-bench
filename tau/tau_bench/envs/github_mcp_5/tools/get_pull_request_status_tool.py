# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPullRequestStatusTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get('owner')
        repo = kwargs.get('repo')
        pr_number = kwargs.get('pr_number')

        if not all([owner, repo, pr_number]):
            return json.dumps({
                "status": "error",
                "message": "Missing required parameters for get_pull_request_status.",
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
"message": f"Pull request number {pr_number} does not exist in the repository '{repo}'.",
            }, indent=2)

        # Emulate retrieving status, such as checks and mergeability.
        # A real API would provide more comprehensive information.
        status = {
            "checks": [
                {"name": "CI Check", "status": "success"},
                {"name": "Code Style", "status": "success"}
            ],
            "mergeable": pull_request.get("mergeable_flags", [False])[0],
            "state": pull_request.get("pr_states", ["open"])[0]
        }

        return json.dumps({
            "status": "success",
            "pull_request_status": status
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pull_request_status",
                "description": "Retrieves the status of a pull request, including checks and mergeability.",
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