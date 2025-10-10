# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListOpenPullRequests(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        me = _auth(data)["username"]

        prs = _prs(data)
        for block in prs:
            # print("block:::", block)
            if block["owner"] == me and block["repo_name"] == repo_name:
                results = [
                    {
                        "number": n,
                        "title": t,
                        "state": s,
                        "base": b,
                        "head": h
                    }
                    for n, t, s, b, h in zip(
                        block["pr_numbers"],
                        block["pr_titles"],
                        block["pr_states"],
                        block["base_branches"],
                        block["head_branches"]
                    ) if s == "open"
                ]
                return json.dumps({"pull_requests": results}, indent=2)

        return json.dumps({"pull_requests": []}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_open_pull_requests",
                "description": "Lists all open pull requests in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"}
                    },
                    "required": ["repo_name"]
                }
            }
        }
