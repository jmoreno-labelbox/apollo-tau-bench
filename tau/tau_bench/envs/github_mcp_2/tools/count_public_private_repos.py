# Sierra Copyright

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

class CountPublicPrivateRepos(Tool):
    """Returns count of public vs private repositories owned by the acting user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        repos = [r for r in _repos(data) if r.get("owner") == me]

        result = {"public": 0, "private": 0}
        for r in repos:
            vis = r.get("visibility")
            if vis == "public":
                result["public"] += 1
            elif vis == "private":
                result["private"] += 1

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "count_public_private_repos",
                "description": "Returns counts of public and private repositories owned by the user.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }