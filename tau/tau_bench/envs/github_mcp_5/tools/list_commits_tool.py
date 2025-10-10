# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCommitsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get('owner')
        repo = kwargs.get('repo')
        path = kwargs.get('path') # This parameter seems unused in the provided data structure for commits, but kept for consistency if needed later.

        if not all([owner, repo]):
            return json.dumps({
                "status": "error",
                "message": "Missing required parameters for list_commits.",
                "required": ["owner", "repo"]
            }, indent=2)

        repositories = list(data.get('repositories', {}).values())
        repository = next((r for r in repositories if r['repo_name'] == repo and r['owner'] == owner), None)

        if not repository:
            return json.dumps({
                "status": "error",
                "message": f"Repository '{repo}' not found for owner '{owner}'.",
            }, indent=2)

        commits_data = repository.get('commits', [])
        # In a real scenario, you might filter commits by branch, path, etc.
        # For this simulation, we return all commits associated with the repository.
        return json.dumps({
            "status": "success",
            "commits": commits_data
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_commits",
                "description": "Lists the commits in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "The owner of the repository."},
                        "repo": {"type": "string", "description": "The name of the repository."},
                        "path": {"type": "string", "description": "The path to filter commits by (optional)."}
                    },
                    "required": ["owner", "repo"],
                },
            },
        }
