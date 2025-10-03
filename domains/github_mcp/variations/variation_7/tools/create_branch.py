from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateBranch(Tool):
    """Generate a new branch from the default one."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, branch: str = None) -> str:
        owner = owner or _actor_name(data)
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        if not branch:
            raise RuntimeError("'branch' is required")
        branches = r.setdefault("branches", [])
        if branch in branches:
            raise RuntimeError("Branch exists")
        branches.append(branch)
        payload = {"created": branch}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateBranch",
                "description": "Create a branch in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo", "branch"],
                },
            },
        }
