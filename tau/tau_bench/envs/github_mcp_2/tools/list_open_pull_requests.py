from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListOpenPullRequests(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        pass
        me = _auth(data)["username"]

        prs = _prs(data)
        for block in prs:
            #print("block:::", block)
            if block["owner"] == me and block["repo_name"] == repo_name:
                results = [
                    {"number": n, "title": t, "state": s, "base": b, "head": h}
                    for n, t, s, b, h in zip(
                        block["pr_numbers"],
                        block["pr_titles"],
                        block["pr_states"],
                        block["base_branches"],
                        block["head_branches"],
                    )
                    if s == "open"
                ]
                payload = {"pull_requests": results}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"pull_requests": []}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListOpenPullRequests",
                "description": "Lists all open pull requests in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
