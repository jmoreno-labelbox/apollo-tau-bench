from tau_bench.envs.tool import Tool
import json
from typing import Any

class AssignUser(Tool):
    """Designate a user for an issue or pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], kind: str = None, owner: str = None, repo: str = None, number: int = None, username: str = None) -> str:
        owner = owner or _actor_name(data)
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if (
                obj.get("owner") == owner
                and obj.get("repo") == repo
                and obj.get("number") == number
            ):
                assignees = obj.setdefault("assignees", [])
                if username and username not in assignees:
                    assignees.append(username)
                payload = obj
                out = json.dumps(payload)
                return out
        raise RuntimeError("Target not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignUser",
                "description": "Assign a username to an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "username": {"type": "string"},
                    },
                    "required": ["kind", "repo", "number", "username"],
                },
            },
        }
