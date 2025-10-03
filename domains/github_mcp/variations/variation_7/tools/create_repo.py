from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateRepo(Tool):
    """Establish a repository with fundamental attributes."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, private: bool = False) -> str:
        me = _actor_name(data)
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
        payload = repo
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRepo",
                "description": "Create a repository for the current user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "private": {"type": "boolean"},
                    },
                    "required": ["name"],
                },
            },
        }
