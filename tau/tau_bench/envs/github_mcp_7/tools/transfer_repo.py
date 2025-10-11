# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
def _repos(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("repositories", [])


def _find_repo(data: Dict[str, Any], owner: str, repo: str) -> Optional[Dict[str, Any]]:
    for r in _repos(data):
        if r.get("owner") == owner and (r.get("repo_name") or r.get("name")) == repo:
            return r
    return None

def _actor_name(data: Dict[str, Any]) -> str:
    auth = data.get("authentication") or [{}]
    return auth[0].get("username") or "anonymous"

class TransferRepo(Tool):
    """Transfer repository ownership to another username (string only)."""
    @staticmethod
    def invoke(data: Dict[str, Any], new_owner, owner, repo) -> str:
        current = owner or _actor_name(data)
        r = _find_repo(data, current, repo)
        if not r:
            raise RuntimeError("Repository not found")
        r["owner"] = new_owner
        return json.dumps({"ok": True, "owner": new_owner})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_repo",
                "description": "Transfer repo ownership to a new owner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "new_owner": {"type": "string"}
                    },
                    "required": ["repo", "new_owner"]
                }
            },
        }