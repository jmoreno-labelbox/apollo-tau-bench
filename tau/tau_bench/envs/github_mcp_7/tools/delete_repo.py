# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteRepo(Tool):
    """Delete a repository you own."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _actor_name(data)
        name = kwargs.get("name")
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
