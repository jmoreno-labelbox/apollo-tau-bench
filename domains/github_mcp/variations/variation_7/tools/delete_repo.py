from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeleteRepo(Tool):
    """Remove a repository that you possess."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        me = _actor_name(data)
        if not name:
            raise RuntimeError("'name' is required")
        before = len(_repos(data))
        data["repositories"] = [
            r
            for r in _repos(data)
            if not (
                r.get("owner") == me and (r.get("repo_name") or r.get("name")) == name
            )
        ]
        payload = {"deleted": before - len(_repos(data))}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteRepo",
                "description": "Delete a repository by name (owned by you).",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
