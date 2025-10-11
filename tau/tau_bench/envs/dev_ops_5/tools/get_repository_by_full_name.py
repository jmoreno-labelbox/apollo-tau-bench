# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRepositoryByFullName(Tool):
    """Retrieves a repository by its full name (e.g., 'gamecorp/engine-core')."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_full_name) -> str:
        repositories = list(data.get("repositories", {}).values())
        
        for repo in repositories:
            if repo.get("repo_full_name") == repo_full_name:
                return json.dumps(repo)
        
        return json.dumps({"error": f"Repository with full name '{repo_full_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repository_by_full_name",
                "description": "Retrieves a repository by its full name (e.g., 'gamecorp/engine-core').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_full_name": {
                            "type": "string",
                            "description": "The full name of the repository, including the owner.",
                        }
                    },
                    "required": ["repo_full_name"],
                },
            },
        }
