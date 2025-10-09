from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListAllMergedPullRequests(Tool):
    """Provides all merged PRs from all repositories owned by the acting user."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        prs = [
            {
                "repo_name": pr["repo_name"],
                "number": pr["number"],
                "title": pr["title"],
                "state": pr["state"],
            }
            for pr in _prs(data)
            if pr.get("owner") == me and pr.get("state") == "merged"
        ]
        payload = prs
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "listAllMergedPullRequests",
                "description": "Returns all merged pull requests for repos owned by current user.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
