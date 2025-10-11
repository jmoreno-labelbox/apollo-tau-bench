# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateBranch(Tool):
    """Create a new branch off default."""
    @staticmethod
    def invoke(data: Dict[str, Any], branch, owner, repo) -> str:
        owner = owner or _actor_name(data)
        name = branch
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        if not name:
            raise RuntimeError("'branch' is required")
        branches = r.setdefault("branches", [])
        if name in branches:
            raise RuntimeError("Branch exists")
        branches.append(name)
        return json.dumps({"created": name})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_branch",
                "description": "Create a branch in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"}
                    },
                    "required": ["repo", "branch"]
                }
            },
        }
