# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRepositoriesSortedByLastUpdated(Tool):
    """Returns all repositories owned by the acting user, sorted by last update time (descending)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        repos = sorted(
            [r for r in _repos(data) if r.get("owner") == me],
            key=lambda r: r.get("last_updated", ""),
            reverse=True
        )
        return json.dumps([{"repo_name": r["repo_name"], "last_updated": r.get("last_updated")} for r in repos], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_repositories_sorted_by_last_updated",
                "description": "Returns repositories owned by the current user, sorted by last_updated.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
