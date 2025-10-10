# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListBranches(Tool):
    """List branches for a repo."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        return json.dumps({
            "default": r.get("default_branch"),
            "branches": r.get("branches") or []
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_branches",
                "description": "List branches in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"}
                    },
                    "required": ["repo"]
                }
            },
        }
