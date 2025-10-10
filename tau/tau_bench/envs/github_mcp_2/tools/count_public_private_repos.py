# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
