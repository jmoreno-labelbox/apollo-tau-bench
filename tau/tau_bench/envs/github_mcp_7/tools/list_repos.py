# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _repos(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("repositories", [])

def _actor_name(data: Dict[str, Any]) -> str:
    auth = data.get("authentication") or [{}]
    return auth[0].get("username") or "anonymous"

class ListRepos(Tool):
    """List repositories owned by the authenticated user."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _actor_name(data)
        items = [r for r in _repos(data) if r.get("owner") == me]
        return json.dumps(items)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_repos",
                "description": "List repositories for the current user.",
                "parameters": {"type": "object", "properties": {}}
            },
        }