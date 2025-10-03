from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class CountPublicPrivateRepos(Tool):
    """Provides the count of public and private repositories owned by the acting user."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        repos = [r for r in _repos(data) if r.get("owner") == me]

        result = {"public": 0, "private": 0}
        for r in repos:
            vis = r.get("visibility")
            if vis == "public":
                result["public"] += 1
            elif vis == "private":
                result["private"] += 1
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "countPublicPrivateRepos",
                "description": "Returns counts of public and private repositories owned by the user.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
