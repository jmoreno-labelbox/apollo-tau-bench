from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetRepositoriesForProject(Tool):
    """Fetches all repositories for a specified project ID."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        repos = data.get("repositories", [])
        project_repos = [r for r in repos if r.get("project_id") == project_id]
        payload = project_repos
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRepositoriesForProject",
                "description": "Retrieves all repositories for a given project ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }
