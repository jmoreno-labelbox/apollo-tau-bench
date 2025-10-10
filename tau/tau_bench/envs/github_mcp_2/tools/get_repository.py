# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRepository(Tool):
    """Returns details about a repository by name, regardless of owner."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        try:
            # Search all repositories in the dataset, including those not owned by the authenticated user.
            for repo in _repos(data):
                if repo.get("repo_name") == repo_name:
                    return json.dumps(repo, indent=2)
            return json.dumps({"error": f"Repository not found: {repo_name}"}, indent=2)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repository",
                "description": "Returns details about a repository by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string", "description": "The name of the repository"},
                    },
                    "required": ["repo_name"],
                },
            },
        }
