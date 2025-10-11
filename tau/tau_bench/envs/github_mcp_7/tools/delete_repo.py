# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _repos(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("repositories", [])

def _actor_name(data: Dict[str, Any]) -> str:
    auth = data.get("authentication") or [{}]
    return auth[0].get("username") or "anonymous"

class DeleteRepo(Tool):
    """Delete a repository you own."""
    @staticmethod
    def invoke(data: Dict[str, Any], name) -> str:
        me = _actor_name(data)
        if not name:
            raise RuntimeError("'name' is required")
        before = len(_repos(data))
        data["repositories"] = [r for r in _repos(data) if not (r.get("owner") == me and (r.get("repo_name") or r.get("name")) == name)]
        return json.dumps({"deleted": before - len(_repos(data))})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_repo",
                "description": "Delete a repository by name (owned by you).",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"]
                }
            },
        }