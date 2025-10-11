# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
def _auth(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return acting identity as {"username": "...", "email": "..."}.
    Requires get_me(username=...) to have set data["_me"].
    """
    me = data.get("_me")
    if isinstance(me, dict) and "username" in me:
        return me
    raise Exception("No acting identity set. Call get_me(username=...) first.")


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

class RemoveRepoTopic(Tool):
    """Removes a topic from a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name, topic) -> str:
        repo = _find_repo_record(data, repo_name)
        if not topic:
            return json.dumps({"error": "topic is required."}, indent=2)

        repo["topics"] = [t for t in repo.get("topics", []) if t != topic]
        return json.dumps({"message": f"Topic '{topic}' removed."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "remove_repo_topic",
                "description": "Removes a topic from a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "topic": {"type": "string"}
                    },
                    "required": ["repo_name", "topic"]
                }
            }
        }