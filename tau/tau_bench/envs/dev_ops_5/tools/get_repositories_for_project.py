# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRepositoriesForProject(Tool):
    """Retrieves all repositories for a given project ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], project_id) -> str:
        repos = list(data.get("repositories", {}).values())
        project_repos = [r for r in repos if r.get("project_id") == project_id]
        return json.dumps(project_repos)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repositories_for_project",
                "description": "Retrieves all repositories for a given project ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }
