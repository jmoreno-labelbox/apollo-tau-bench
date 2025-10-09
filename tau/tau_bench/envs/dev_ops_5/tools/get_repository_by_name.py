from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetRepositoryByName(Tool):
    """Fetches a repository using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        repo_name = name
        repositories = data.get("repositories", [])

        for repo in repositories:
            if repo.get("name") == repo_name:
                payload = repo
                out = json.dumps(payload)
                return out
        payload = {"error": f"Repository with name '{repo_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRepositoryByName",
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
