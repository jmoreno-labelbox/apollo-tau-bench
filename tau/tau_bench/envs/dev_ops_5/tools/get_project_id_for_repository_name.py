from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetProjectIdForRepositoryName(Tool):
    """Fetches the project ID for a specified repository name."""

    @staticmethod
    def invoke(data: dict[str, Any], repository_name: str = None) -> str:
        repositories = data.get("repositories", [])

        for repo in repositories:
            if repo.get("name") == repository_name:
                payload = {"project_id": repo.get("project_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Repository with name '{repository_name}' not found."}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectIdForRepositoryName",
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
