# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRepo(Tool):
    """Create a repository with basic fields."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _actor_name(data)
        name = kwargs.get("name")
        private = bool(kwargs.get("private", False))
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
