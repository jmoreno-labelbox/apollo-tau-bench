from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddMemberToTeam(Tool):
    """Inserts a user into a team with a designated role."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None, user_id: str = None, role: str = None) -> str:
        members = data.get("team_members", [])
        new_member = {
            "team_id": team_id,
            "user_id": user_id,
            "role": role,
            "added_at": "2025-01-28T00:00:00Z",
        }
        members.append(new_member)
        payload = {
            "status": "success",
            "message": f"User '{user_id}' added to team '{team_id}'.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addMemberToTeam",
                "description": "Adds a user to a team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "role": {"type": "string"},
                    },
                    "required": ["team_id", "user_id", "role"],
                },
            },
        }
