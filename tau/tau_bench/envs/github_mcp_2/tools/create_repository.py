# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRepository(Tool):
    """Creates a new repository owned by the current user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        visibility = kwargs.get("visibility", "public")
        default_branch = kwargs.get("default_branch", "main")

        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        me = _auth(data)["username"]

        repos = _repos(data)
        if any(r["owner"] == me and r["repo_name"] == repo_name for r in repos):
            return json.dumps({"error": "Repository already exists."}, indent=2)

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

        return json.dumps({"message": "Repository created", "repo_name": repo_name}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_repository",
                "description": "Creates a new repository for the current user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "visibility": {"type": "string"},
                        "default_branch": {"type": "string"},
                    },
                    "required": ["repo_name"]
                }
            }
        }
