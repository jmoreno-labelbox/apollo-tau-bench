# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _repos(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("repositories", [])

def _auth(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return acting identity as {"username": "...", "email": "..."}.
    Requires get_me(username=...) to have set data["_me"].
    """
    me = data.get("_me")
    if isinstance(me, dict) and "username" in me:
        return me
    raise Exception("No acting identity set. Call get_me(username=...) first.")

class CreateRepository(Tool):
    """Creates a new repository owned by the current user."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name, default_branch = "main", visibility = "public") -> str:

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