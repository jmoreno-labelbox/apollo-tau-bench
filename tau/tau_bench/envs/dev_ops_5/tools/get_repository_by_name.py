# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRepositoryByName(Tool):
    """Retrieves a repository by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("name")
        repositories = list(data.get("repositories", {}).values())
        
        for repo in repositories:
            if repo.get("name") == repo_name:
                return json.dumps(repo)
        
        return json.dumps({"error": f"Repository with name '{repo_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repository_by_name",
                "description": "Retrieves a repository by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the repository.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }
