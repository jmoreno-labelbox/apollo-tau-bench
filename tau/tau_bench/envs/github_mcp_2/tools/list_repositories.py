from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListRepositories(Tool):
    """Enumerates all repositories that belong to the current user."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        owned = [r for r in _repos(data) if r["owner"] == me]
        payload = {"repositories": owned}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListRepositories",
                "description": "Returns all repositories owned by the current user.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
