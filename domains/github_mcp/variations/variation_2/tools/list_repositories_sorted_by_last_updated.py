from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListRepositoriesSortedByLastUpdated(Tool):
    """Provides all repositories owned by the acting user, ordered by the most recent update time (in descending order)."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        repos = sorted(
            [r for r in _repos(data) if r.get("owner") == me],
            key=lambda r: r.get("last_updated", ""),
            reverse=True,
        )
        payload = [
            {"repo_name": r["repo_name"], "last_updated": r.get("last_updated")}
            for r in repos
        ]
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRepositoriesSortedByLastUpdated",
                "description": "Returns repositories owned by the current user, sorted by last_updated.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
