# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddMemberToTeam(Tool):
    """Adds a user to a team with a specific role."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        members = data.get("team_members", [])
        new_member = {
            "team_id": kwargs.get("team_id"),
            "user_id": kwargs.get("user_id"),
            "role": kwargs.get("role"),
            "added_at": "2025-01-28T00:00:00Z"
        }
        members.append(new_member)
        return json.dumps({"status": "success", "message": f"User '{kwargs.get('user_id')}' added to team '{kwargs.get('team_id')}'."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_member_to_team",
                "description": "Adds a user to a team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "role": {"type": "string"}
                    },
                    "required": ["team_id", "user_id", "role"],
                },
            },
        }
