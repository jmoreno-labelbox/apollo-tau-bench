# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchRepositories(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], query: str) -> str:
        """Search repositories by query string (exact-match permitted)."""
        repositories = list(data.get("repositories", {}).values())
        matching_repos = []

        for repo in repositories:
            if query.lower() in repo["repo_name"].lower():
                matching_repos.append(repo["repo_name"])

        return json.dumps({"repo_names": matching_repos}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_repositories",
                "description": "Search repositories by query string (exact-match permitted).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search query string"}
                    },
                    "required": ["query"]
                }
            }
        }
