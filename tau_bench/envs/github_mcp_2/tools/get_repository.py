from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetRepository(Tool):
    """Provides information about a repository based on its name, irrespective of the owner."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, name: Any = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            # Examine all repositories in the dataset, not solely those owned by the authenticated user
            for repo in _repos(data):
                if repo.get("repo_name") == repo_name:
                    payload = repo
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Repository not found: {repo_name}"}
            out = json.dumps(payload, indent=2)
            return out
        except Exception as e:
            payload = {"error": str(e)}
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRepository",
                "description": "Returns details about a repository by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {
                            "type": "string",
                            "description": "The name of the repository",
                        },
                    },
                    "required": ["repo_name"],
                },
            },
        }
