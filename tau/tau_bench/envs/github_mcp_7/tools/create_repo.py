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

class CreateRepo(Tool):
    """Create a repository with basic fields."""
    @staticmethod
    def invoke(data: Dict[str, Any], name, private = False) -> str:
        me = _actor_name(data)
        private = bool(private)
        if not name:
            raise RuntimeError("'name' is required")
        if _find_repo(data, me, name):
            raise RuntimeError("Repository already exists")
        repo = {
            "owner": me,
            "repo_name": name,
            "private": private,
            "default_branch": "main",
            "branches": ["main"],
            "created_at": get_current_timestamp(),
            "topics": [],
        }
        _repos(data).append(repo)
        return json.dumps(repo)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_repo",
                "description": "Create a repository for the current user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "private": {"type": "boolean"}
                    },
                    "required": ["name"]
                }
            },
        }