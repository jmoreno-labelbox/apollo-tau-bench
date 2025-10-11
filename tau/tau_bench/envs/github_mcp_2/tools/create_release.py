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

class CreateRelease(Tool):
    """Creates a release for a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name, tag, body = "", title = "") -> str:
        repo_name, tag, body = repo_name, tag, body
        if not all([repo_name, tag]):
            return json.dumps({"error": "repo_name and tag are required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        repo.setdefault("releases", []).append({
            "tag_name": tag,
            "body": body,
            "created_by": _auth(data)["username"],
            "created_at": get_current_timestamp()
        })

        return json.dumps({
            "message": "Release created.",
            "repo_name": repo_name,
            "tag_name": tag,
            "title": title
        }, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_release",
                "description": "Creates a new release (tag + body).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "tag": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"}
                    },
                    "required": ["repo_name", "tag"]
                }
            }
        }