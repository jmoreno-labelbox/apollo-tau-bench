from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class SearchRepositories(Tool):
    """Looks for repositories using a name substring or owner."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = "", owner: str = "") -> str:
        name_query = name.lower()
        owner_query = owner.lower()
        results = []

        for repo in _repos(data):
            if (name_query and name_query in repo.get("repo_name", "").lower()) or (
                owner_query and owner_query in repo.get("owner", "").lower()
            ):
                results.append(repo)
        payload = {"results": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchRepositories",
                "description": "Search repositories by name or owner substring.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "owner": {"type": "string"},
                    },
                },
            },
        }
