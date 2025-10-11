# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _issues(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("issues", [])

def _actor_name(data: Dict[str, Any]) -> str:
    auth = data.get("authentication") or [{}]
    return auth[0].get("username") or "anonymous"

class SetIssueState(Tool):
    """Close or reopen an issue."""
    @staticmethod
    def invoke(data: Dict[str, Any], number, owner, repo, state) -> str:
        owner = owner or _actor_name(data)
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