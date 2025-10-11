# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _prs(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("pull_requests", [])

def _auth(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return acting identity as {"username": "...", "email": "..."}.
    Requires get_me(username=...) to have set data["_me"].
    """
    me = data.get("_me")
    if isinstance(me, dict) and "username" in me:
        return me
    raise Exception("No acting identity set. Call get_me(username=...) first.")

class ListAllMergedPullRequests(Tool):
    """Returns all merged PRs across all repositories owned by acting user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        prs = [
            {
                "repo_name": pr["repo_name"],
                "number": pr["number"],
                "title": pr["title"],
                "state": pr["state"]
            }
            for pr in _prs(data)
            if pr.get("owner") == me and pr.get("state") == "merged"
        ]
        return json.dumps(prs, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_all_merged_pull_requests",
                "description": "Returns all merged pull requests for repos owned by current user.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }