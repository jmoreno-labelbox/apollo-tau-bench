from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetIssueState(Tool):
    """Either close or reactivate an issue."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None, state: str = None) -> str:
        owner = owner or _actor_name(data)
        for i in _issues(data):
            if (
                i.get("owner") == owner
                and i.get("repo") == repo
                and i.get("number") == number
            ):
                i["state"] = state
                i["updated_at"] = get_current_timestamp()
                payload = i
                out = json.dumps(payload)
                return out
        raise RuntimeError("Issue not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setIssueState",
                "description": "Set issue state to open or closed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "state": {"type": "string", "enum": ["open", "closed"]},
                    },
                    "required": ["repo", "number", "state"],
                },
            },
        }
