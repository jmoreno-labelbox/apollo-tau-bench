# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _find_repo(data: Dict[str, Any], owner: str, repo: str) -> Optional[Dict[str, Any]]:
    for r in _repos(data):
        if r.get("owner") == owner and (r.get("repo_name") or r.get("name")) == repo:
            return r
    return None

def _commits(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("commits", [])

def _actor_name(data: Dict[str, Any]) -> str:
    auth = data.get("authentication") or [{}]
    return auth[0].get("username") or "anonymous"

class AddCommit(Tool):
    """Record a commit on a branch (very lightweight)."""
    @staticmethod
    def invoke(data: Dict[str, Any], message, owner, repo, branch = "main") -> str:
        owner = owner or _actor_name(data)
        message = message or ""
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        seq = sum(1 for c in _commits(data) if c.get("owner") == owner and c.get("repo") == repo) + 1
        sha = f"{branch}-{seq:06d}"
        c = {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "sha": sha,
            "message": message,
            "author": _actor_name(data),
            "timestamp": get_current_timestamp(),
        }
        _commits(data).append(c)
        return json.dumps(c)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_commit",
                "description": "Add a commit record to a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"},
                        "message": {"type": "string"}
                    },
                    "required": ["repo"]
                }
            },
        }