from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetMilestone(Tool):
    """Establish a plain-text milestone attribute on an issue or pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], kind: str = None, owner: str = None, repo: str = None, number: int = None, milestone: str = None) -> str:
        owner = owner or _actor_name(data)
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if (
                obj.get("owner") == owner
                and obj.get("repo") == repo
                and obj.get("number") == number
            ):
                obj["milestone"] = milestone
                payload = obj
                out = json.dumps(payload)
                return out
        raise RuntimeError("Target not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setMilestone",
                "description": "Set a milestone string on an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "milestone": {"type": "string"},
                    },
                    "required": ["kind", "repo", "number", "milestone"],
                },
            },
        }
