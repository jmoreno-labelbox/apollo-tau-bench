# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetMilestone(Tool):
    """Set a plain-text milestone field on an issue or PR."""
    @staticmethod
    def invoke(data: Dict[str, Any], kind, milestone, number, owner, repo) -> str:
        owner = owner or _actor_name(data)
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if obj.get("owner") == owner and obj.get("repo") == repo and obj.get("number") == number:
                obj["milestone"] = milestone
                return json.dumps(obj)
        raise RuntimeError("Target not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_milestone",
                "description": "Set a milestone string on an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "milestone": {"type": "string"}
                    },
                    "required": ["kind", "repo", "number", "milestone"]
                }
            },
        }
