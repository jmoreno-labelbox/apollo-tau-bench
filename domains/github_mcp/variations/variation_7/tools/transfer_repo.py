from tau_bench.envs.tool import Tool
import json
from typing import Any

class TransferRepo(Tool):
    """Change repository ownership to a different username (string only)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, new_owner: str = None) -> str:
        current = owner or _actor_name(data)
        r = _find_repo(data, current, repo)
        if not r:
            raise RuntimeError("Repository not found")
        r["owner"] = new_owner
        payload = {"ok": True, "owner": new_owner}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransferRepo",
                "description": "Transfer repo ownership to a new owner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "new_owner": {"type": "string"},
                    },
                    "required": ["repo", "new_owner"],
                },
            },
        }
