# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetIssueState(Tool):
    """Close or reopen an issue."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        state = kwargs.get("state")
        for i in _issues(data):
            if i.get("owner") == owner and i.get("repo") == repo and i.get("number") == number:
                i["state"] = state
                i["updated_at"] = get_current_timestamp()
                return json.dumps(i)
        raise RuntimeError("Issue not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_issue_state",
                "description": "Set issue state to open or closed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "state": {"type": "string", "enum": ["open", "closed"]}
                    },
                    "required": ["repo", "number", "state"]
                }
            },
        }
