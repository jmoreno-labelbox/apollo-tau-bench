from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class CreateRepository(Tool):
    """Generates a new repository that is owned by the current user."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, visibility: str = "public", default_branch: str = "main") -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        me = _auth(data)["username"]

        repos = _repos(data)
        if any(r["owner"] == me and r["repo_name"] == repo_name for r in repos):
            payload = {"error": "Repository already exists."}
            out = json.dumps(payload, indent=2)
            return out

        new_repo = {
            "owner": me,
            "repo_name": repo_name,
            "visibility": visibility,
            "default_branch": default_branch,
            "branches": [default_branch],
            "branch_files": [[]],
            "branch_contents": [[]],
            "branch_shas": [get_next_commit_sha()],
            "branch_protections": [{}],
            "topics": [],
            "releases": [],
        }
        repos.append(new_repo)
        payload = {"message": "Repository created", "repo_name": repo_name}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateRepository",
                "description": "Creates a new repository for the current user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "visibility": {"type": "string"},
                        "default_branch": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }
