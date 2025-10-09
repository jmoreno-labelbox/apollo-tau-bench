from tau_bench.envs.tool import Tool
import json
from typing import Any

class SearchRepositories(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], query: str) -> str:
        """Search repositories by query string (exact-match permitted)."""
        _queryL = query or ''.lower()
        pass
        repositories = data.get("repositories", [])
        matching_repos = []

        for repo in repositories:
            if query.lower() in repo["repo_name"].lower():
                matching_repos.append(repo["repo_name"])
        payload = {"repo_names": matching_repos}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchRepositories",
                "description": "Search repositories by query string (exact-match permitted).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query string",
                        }
                    },
                    "required": ["query"],
                },
            },
        }
