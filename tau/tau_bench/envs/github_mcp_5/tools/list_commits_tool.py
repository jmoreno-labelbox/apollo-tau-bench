# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCommitsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner, path, repo) -> str:

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
        # In a practical situation, filtering commits by branch, path, and other criteria may be applied.
        # This simulation retrieves all commits linked to the repository.
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
