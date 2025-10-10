# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBranchByName(Tool):
    """Retrieves a branch by its name within a specific repository."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_id = kwargs.get("repository_id")
        branch_name = kwargs.get("branch_name")
        branches = list(data.get("branches", {}).values())
        for branch in branches:
            if branch.get("repository_id") == repo_id and branch.get("name") == branch_name:
                return json.dumps(branch)
        return json.dumps({"error": f"Branch '{branch_name}' not found in repository '{repo_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_branch_by_name",
                "description": "Retrieves a branch by its name within a specific repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {"type": "string", "description": "The ID of the repository."},
                        "branch_name": {"type": "string", "description": "The name of the branch."}
                    },
                    "required": ["repository_id", "branch_name"],
                },
            },
        }
