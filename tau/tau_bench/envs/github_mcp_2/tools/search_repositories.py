# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchRepositories(Tool):
    """Searches repositories by name substring or owner."""

    @staticmethod
    def invoke(data: Dict[str, Any], name = "", owner = "") -> str:
        name_query = name.lower()
        owner_query = owner.lower()
        results = []

        for repo in _repos(data):
            if (
                (name_query and name_query in repo.get("repo_name", "").lower()) or
                (owner_query and owner_query in repo.get("owner", "").lower())
            ):
                results.append(repo)

        return json.dumps({"results": results}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "search_repositories",
                "description": "Search repositories by name or owner substring.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "owner": {"type": "string"},
                    },
                },
            }
        }
