# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MergePR(Tool):
    """Merge a PR by number (marks as merged)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo and p.get("number") == number:
                p["state"] = "merged"
                p["merged_at"] = get_current_timestamp()
                return json.dumps(p)
        raise RuntimeError("PR not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_pr",
                "description": "Mark a pull request as merged.",
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
