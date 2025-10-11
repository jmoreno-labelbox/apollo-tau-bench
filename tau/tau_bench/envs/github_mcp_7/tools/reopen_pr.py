# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReopenPR(Tool):
    """Reopen a previously closed PR."""
    @staticmethod
    def invoke(data: Dict[str, Any], number, owner, repo) -> str:
        owner = owner or _actor_name(data)
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo and p.get("number") == number:
                p["state"] = "open"
                p["reopened_at"] = get_current_timestamp()
                return json.dumps(p)
        raise RuntimeError("PR not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reopen_pr",
                "description": "Reopen a pull request.",
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
