# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _commits(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("commits", [])

def _auth(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return acting identity as {"username": "...", "email": "..."}.
    Requires get_me(username=...) to have set data["_me"].
    """
    me = data.get("_me")
    if isinstance(me, dict) and "username" in me:
        return me
    raise Exception("No acting identity set. Call get_me(username=...) first.")

class GetCommitSummary(Tool):
    """Returns commit count for a given repo and owner, broken down by branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], owner, repo_name) -> str:
        owner = owner or _auth(data)["username"]
        if not all([owner, repo_name]):
            return json.dumps({"error": "owner and repo_name are required."}, indent=2)

        commits = _commits(data)
        summary = {}

        for c in commits:
            if c.get("owner") == owner and c.get("repo_name") == repo_name:
                for branch, shas in zip(c["branch_names"], c["commit_shas"]):
                    summary[branch] = len(shas)

        return json.dumps({"repo_name": repo_name, "commit_summary": summary}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_commit_summary",
                "description": "Returns commit summary per branch for a repo and owner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo_name": {"type": "string"},
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }