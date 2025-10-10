# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectIdForRepositoryName(Tool):
    """Retrieves the project ID for a given repository name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repository_name = kwargs.get("repository_name")
        repositories = list(data.get("repositories", {}).values())
        
        for repo in repositories:
            if repo.get("name") == repository_name:
                return json.dumps({"project_id": repo.get("project_id")})
        
        return json.dumps({"error": f"Repository with name '{repository_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_id_for_repository_name",
                "description": "Retrieves the project ID for a given repository name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_name": {
                            "type": "string",
                            "description": "The name of the repository.",
                        }
                    },
                    "required": ["repository_name"],
                },
            },
        }
