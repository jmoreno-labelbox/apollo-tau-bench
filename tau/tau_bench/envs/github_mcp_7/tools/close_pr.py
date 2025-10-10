# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ClosePR(Tool):
    """Close (but not merge) a PR."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo and p.get("number") == number:
                p["state"] = "closed"
                p["closed_at"] = get_current_timestamp()
                return json.dumps(p)
        raise RuntimeError("PR not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "close_pr",
                "description": "Close a pull request without merging.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"}
                    },
                    "required": ["repo", "number"]
                }
            },
        }
