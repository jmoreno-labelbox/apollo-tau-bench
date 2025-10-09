from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetRepositoryByFullName(Tool):
    """Fetches a repository using its complete name (e.g., 'gamecorp/engine-core')."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_full_name: str = None) -> str:
        repositories = data.get("repositories", [])

        for repo in repositories:
            if repo.get("repo_full_name") == repo_full_name:
                payload = repo
                out = json.dumps(payload)
                return out
        payload = {"error": f"Repository with full name '{repo_full_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRepositoryByFullName",
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
