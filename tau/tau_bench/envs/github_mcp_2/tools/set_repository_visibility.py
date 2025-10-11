# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_repo_record(data: Dict[str, Any], repo_name: str) -> Dict[str, Any]:
    """
    Find a repo owned by the acting user. repositories is a LIST in our dataset,
    so iterate; do NOT use dict.get.
    """
    me = _auth(data)["username"]
    repos = data.get("repositories") or []
    for r in repos:
        if r.get("owner") == me and r.get("repo_name") == repo_name:
            return r
    # Mirror RULES: if not found, surface a crisp error (no workarounds)
    raise Exception(f"Repository not found for owner '{me}': {repo_name}")

def _auth(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return acting identity as {"username": "...", "email": "..."}.
    Requires get_me(username=...) to have set data["_me"].
    """
    me = data.get("_me")
    if isinstance(me, dict) and "username" in me:
        return me
    raise Exception("No acting identity set. Call get_me(username=...) first.")

class SetRepositoryVisibility(Tool):
    """Changes the visibility of a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name, visibility) -> str:
        me = _auth(data)["username"]

        if not all([repo_name, visibility]):
            return json.dumps({"error": "repo_name and visibility are required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        if visibility not in ["public", "private"]:
            return json.dumps({"error": "Invalid visibility. Must be 'public' or 'private'."}, indent=2)

        repo["visibility"] = visibility
        return json.dumps({"message": "Visibility updated", "repo_name": repo_name, "visibility": visibility}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_repository_visibility",
                "description": "Updates visibility of a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "visibility": {"type": "string", "enum": ["public", "private"]}
                    },
                    "required": ["repo_name", "visibility"]
                }
            }
        }